from __future__ import annotations

import argparse
import json
import os
import re
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
}


def value(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\r?$", text)
    return match.group(1).strip() if match else ""


def tags(text: str) -> list[str]:
    match = re.search(r"(?ms)^tags:\r?\n(?P<items>(?:\s+-\s+.*?\r?\n)+)", text)
    if not match:
        return []
    return [
        item.strip()
        for item in re.findall(r"(?m)^\s+-\s+(.*?)\r?$", match.group("items"))
    ]


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
    lower = text.lower()
    score = 0
    for term in needles:
        token = term.lower()
        if token in topic:
            score += 12
        if token in tag_text:
            score += 8
        score += min(lower.count(token), 5) * 2
    record_market = value(text, "market")
    record_industry = value(text, "industry_name")
    record_scope = value(text, "question_scope")
    if market and market == record_market:
        score += 8
    if industry and (
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
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for path in (root / "review_comments").rglob("Q*.md"):
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        company = value(text, "company")
        source_file = value(text, "source_file")
        source_pages = value(text, "source_pages")
        if not company or not source_file or not source_pages:
            continue
        score = score_record(text, needles, market, industry, scope)
        if score <= 0:
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
                "source_file": source_file,
                "source_pages": source_pages,
                "excerpt": excerpt(text, needles, max_chars),
            }
        )
    return results


def scan_manuals(
    root: Path,
    needles: list[str],
    max_chars: int,
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    directories = [
        root / "ipo_dd_manuals",
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
    args = parser.parse_args()

    root = args.root or Path(
        os.environ.get(
            "DDMENTOR_KNOWLEDGE_ROOT",
            os.environ.get("DDBIBLE_KNOWLEDGE_ROOT", DEFAULT_ROOT),
        )
    )
    if not (root / "README.md").exists():
        raise SystemExit(f"DD Mentor knowledge root not found: {root}")

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
            )
        )
    results.sort(key=lambda item: (-int(item["score"]), str(item["path"])))
    limit = max(args.limit, 0)
    payload = {
        "query": args.query,
        "expanded_terms": needles,
        "filters": {
            "market": args.market,
            "industry": args.industry,
            "scope": args.scope,
            "module": args.module,
        },
        "result_count": min(len(results), limit),
        "results": results[:limit],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
