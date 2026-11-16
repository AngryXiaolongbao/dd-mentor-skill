from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "knowledge"
ALIASES = {
    "收入": ["收入", "销售", "客户", "回款", "截止", "终端销售"],
    "经销商": ["经销商", "经销模式", "渠道", "终端销售"],
    "存货": ["存货", "库存", "盘点", "跌价"],
    "研发": ["研发", "研发费用", "研发投入", "资本化", "核心技术"],
    "资金流水": ["资金流水", "银行流水", "个人卡", "体外循环", "资金占用"],
    "境外": ["境外", "海外", "出口", "海关", "外销"],
    "关联交易": ["关联交易", "关联方", "资金占用", "利益输送"],
    "供应商": ["供应商", "采购", "外协", "委外加工"],
    "客户": ["客户", "销售", "终端客户", "客户集中"],
    "毛利": ["毛利", "毛利率", "成本", "定价"],
    "并购": ["并购", "收购", "交易结构", "股权收购", "资产收购", "控制权变更", "交割"],
    "融资": ["融资", "投资", "资金用途", "股权融资", "债务融资", "可转债", "投资人权利", "现金跑道"],
    "估值": ["估值", "盈利质量", "营运资金", "净债务", "预测", "现金流", "交易价格"],
}


def frontmatter(text: str) -> str:
    parts = text.lstrip("\ufeff").split("---", 2)
    return parts[1] if len(parts) == 3 and not parts[0].strip() else ""


def value(text: str, key: str) -> str:
    # Scalar metadata only; never consume the next line or body as a value.
    match = re.search(rf"(?m)^{re.escape(key)}:[ \t]*(.*?)[ \t]*$", frontmatter(text))
    raw = match.group(1).strip() if match else ""
    if raw in {"", "null", "~", "|", ">"}:
        return ""
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        raw = raw[1:-1]
    return raw


def tags(text: str) -> list[str]:
    match = re.search(r"(?m)^tags:[ \t]*\r?\n((?:[ \t]+-[ \t]+[^\n]*\n?)+)", frontmatter(text))
    return re.findall(r"(?m)^[ \t]+-[ \t]+(.*)", match.group(1)) if match else []


def record_date(text: str) -> tuple[str, str]:
    for key in ("source_date", "publication_date", "document_date"):
        raw = value(text, key)
        if raw:
            try:
                return date.fromisoformat(raw).isoformat(), key
            except ValueError:
                return "", f"invalid:{key}"
    # A filename date is not evidence of the source publication date.
    return "", "missing"


def metadata_warnings(text: str) -> list[str]:
    board = value(text, "market")
    title = value(text, "source_title")
    title_boards = [b for b in ("创业板", "科创板", "主板", "北交所", "GEM") if b in title]
    return ["market_title_conflict"] if board and title_boards and board not in title_boards else []


def terms(query: str) -> list[str]:
    base = [part for part in re.split(r"[\s,，;；、]+", query.strip()) if part]
    expanded: list[str] = []
    for item in base:
        expanded.append(item)
        for key, related in ALIASES.items():
            if key in item or item in key:
                expanded.extend(related)
    return list(dict.fromkeys(expanded))


def excerpt(text: str, needles: list[str], limit: int) -> str:
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    positions = [body.lower().find(term.lower()) for term in needles]
    positions = [position for position in positions if position >= 0]
    start = max(0, (min(positions) if positions else 0) - limit // 4)
    return re.sub(r"\s+", " ", body[start : start + limit]).strip()


def score_record(
    text: str,
    needles: list[str],
    market: str,
    industry: str,
    scope: str,
) -> int:
    topic = value(text, "topic").lower()
    tag_text = " ".join(tags(text)).lower()
    lower = (value(text, "topic") + " " + " ".join(tags(text)) + " " + text.split("---", 2)[-1]).lower()
    score = 0
    for term in needles:
        token = term.lower()
        if token in topic:
            score += 12
        if token in tag_text:
            score += 8
        score += min(lower.count(token), 5) * 2
    if score == 0:
        return 0
    record_market = value(text, "market")
    record_industry = value(text, "industry_name")
    record_scope = value(text, "question_scope")
    if market and market == record_market:
        score += 8
    if industry and record_industry and (
        industry.lower() in record_industry.lower()
        or record_industry.lower() in industry.lower()
    ):
        score += 8
    if scope and scope == record_scope:
        score += 5
    return score


def scan_regulatory(
    root: Path,
    needles: list[str],
    market: str,
    industry: str,
    scope: str,
    max_chars: int,
    *, strict_market: bool = False, date_from: str = "", date_to: str = "",
    stats: dict | None = None,
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    stats = stats if stats is not None else {}
    stats.update(scanned=0, missing_citation=0, missing_date=0, invalid_date=0,
                 metadata_conflicts=0, no_topic_match=0, excluded_market=0,
                 excluded_date=0, matched=0)
    dates: list[str] = []
    for path in sorted((root / "review_comments").rglob("Q*.md")):
        stats["scanned"] += 1
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        source_date, date_field = record_date(text)
        if source_date:
            dates.append(source_date)
        else:
            stats["invalid_date" if date_field.startswith("invalid:") else "missing_date"] += 1
        warnings = metadata_warnings(text)
        stats["metadata_conflicts"] += bool(warnings)
        company = value(text, "company")
        source_title = value(text, "source_title")
        source_file = value(text, "source_file")
        source_pages = value(text, "source_pages")
        if not company or not source_title or not source_file or not source_pages:
            stats["missing_citation"] += 1
            continue
        score = score_record(text, needles, market, industry, scope)
        if score <= 0:
            stats["no_topic_match"] += 1
            continue
        if strict_market and (value(text, "market") != market or warnings):
            stats["excluded_market"] += 1
            continue
        if (date_from or date_to) and (not source_date or (date_from and source_date < date_from) or (date_to and source_date > date_to)):
            stats["excluded_date"] += 1
            continue
        results.append(
            {
                "module": "regulatory_case",
                "score": score,
                "path": str(path),
                "company": company,
                "project": value(text, "project"),
                "market": value(text, "market"),
                "industry": value(text, "industry_name"),
                "topic": value(text, "topic"),
                "scope": value(text, "question_scope"),
                "citation_file": f"【{source_title.strip('【】')}】",
                "source_title": source_title,
                "source_file": source_file,
                "source_pages": source_pages,
                "source_date": source_date or None,
                "date_field": date_field,
                "metadata_warnings": warnings,
                "source_url": value(text, "source_url") or None,
                "excerpt": excerpt(text, needles, max_chars),
            }
        )
    stats["matched"] = len(results)
    stats["known_date_range"] = [min(dates), max(dates)] if dates else None
    stats["date_range_complete"] = bool(stats["scanned"]) and not (stats["missing_date"] or stats["invalid_date"])
    return results


def scan_manuals(
    root: Path,
    needles: list[str],
    max_chars: int,
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    directories = [
        root / "ipo_dd_manuals",
        root / "ma_financing_dd_manuals",
        root / "general_dd_manuals",
        root / "industry_classification_guidance",
    ]
    for directory in directories:
        for path in directory.glob("*.md"):
            if path.name == "README.md":
                continue
            text = path.read_text(encoding="utf-8-sig", errors="replace")
            lower = text.lower()
            score = sum(min(lower.count(term.lower()), 8) * 3 for term in needles)
            if score <= 0:
                continue
            title = next(
                (
                    line.removeprefix("# ").strip()
                    for line in text.splitlines()
                    if line.startswith("# ")
                ),
                path.stem,
            )
            results.append(
                {
                    "module": "manual",
                    "score": score,
                    "path": str(path),
                    "title": title,
                    "excerpt": excerpt(text, needles, max_chars),
                }
            )
    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search DD Mentor manuals and regulatory Q&A."
    )
    parser.add_argument("--query", required=True)
    parser.add_argument("--market", default="")
    parser.add_argument("--industry", default="")
    parser.add_argument("--scope", choices=["", "通用问题", "行业特有问题"], default="")
    parser.add_argument("--module", choices=["all", "manuals", "review"], default="all")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--max-chars", type=int, default=500)
    parser.add_argument("--root", type=Path)
    parser.add_argument("--strict-market", action="store_true", help="Require exact market metadata and exclude title conflicts (regulatory cases only)")
    parser.add_argument("--date-from", default="", help="Inclusive verified source date YYYY-MM-DD; excludes undated regulatory cases")
    parser.add_argument("--date-to", default="", help="Inclusive historical cutoff YYYY-MM-DD; excludes undated regulatory cases")
    parser.add_argument("--sort", choices=["relevance", "date"], default="relevance")
    args = parser.parse_args()
    if not args.query.strip():
        parser.error("--query must contain a topic")
    if args.strict_market and not args.market:
        parser.error("--strict-market requires --market")
    for raw in (args.date_from, args.date_to):
        if raw:
            try:
                date.fromisoformat(raw)
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
                    raise ValueError()
            except ValueError:
                parser.error("dates must be YYYY-MM-DD")
    if args.date_from and args.date_to and args.date_from > args.date_to:
        parser.error("--date-from must not exceed --date-to")
    if args.max_chars < 1 or args.limit < 0:
        parser.error("--max-chars must be positive and --limit nonnegative")

    root = args.root or Path(
        os.environ.get(
            "DDMENTOR_KNOWLEDGE_ROOT",
            os.environ.get("DDBIBLE_KNOWLEDGE_ROOT", DEFAULT_ROOT),
        )
    )
    if not (root / "README.md").exists():
        raise SystemExit(f"DD Mentor knowledge root not found: {root}")

    stats: dict = {}
    needles = terms(args.query)
    results: list[dict[str, object]] = []
    if args.module in {"all", "manuals"}:
        results.extend(scan_manuals(root, needles, args.max_chars))
    if args.module in {"all", "review"}:
        results.extend(
            scan_regulatory(
                root,
                needles,
                args.market,
                args.industry,
                args.scope,
                args.max_chars,
                strict_market=args.strict_market, date_from=args.date_from,
                date_to=args.date_to, stats=stats,
            )
        )
    results.sort(key=lambda item: (-int(item["score"]), str(item["path"])))
    if args.sort == "date":
        results.sort(key=lambda item: str(item.get("source_date") or ""), reverse=True)
    limit = args.limit
    payload = {
        "query": args.query,
        "expanded_terms": needles,
        "filters": {
            "module": args.module,
            "strict_market": args.market if args.strict_market else None,
            "date_from": args.date_from or None,
            "date_to": args.date_to or None,
            "applies_to": "regulatory_case; manuals are not date/market filtered",
        },
        "ranking_preferences": {
            "market": args.market, "industry": args.industry, "scope": args.scope,
            "sort": args.sort,
        },
        "regulatory_stats": stats,
        "total_matches": len(results),
        "truncated": len(results) > limit,
        "coverage_note": "Ranked candidates, not a completeness or regulatory-frequency estimate. Missing dates and metadata conflicts require source verification.",
        "result_count": min(len(results), limit),
        "results": results[:limit],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
