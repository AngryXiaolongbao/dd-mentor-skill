# Knowledge map

## Knowledge root

Set the knowledge root with:

`DDMENTOR_KNOWLEDGE_ROOT`

For backward compatibility, the skill also accepts `DDBIBLE_KNOWLEDGE_ROOT`. If neither environment variable is present, the skill looks for `<skill-directory>/knowledge`. The GitHub package includes teaching guidance and public regulatory inquiry-and-response records.

## Modules

| Module | Path | Purpose |
| --- | --- | --- |
| Root index | `README.md` | Module overview and counts |
| IPO topic guide | `ipo_dd_manuals/IPO-001 专项尽调教学指南.md` | IPO and financial verification guidance |
| M&A and financing guide | `ma_financing_dd_manuals/MAF-001 并购及融资DDQ教学指南.md` | M&A, equity financing, debt financing, valuation, deal terms, and DDQ guidance |
| General framework | `general_dd_manuals/GEN-001 通用尽调教学框架.md` | Cross-transaction diligence framework |
| Regulatory cases | `review_comments/` | One exchange question and its corresponding reply per Markdown file |
| SSE index | `review_comments/上交所监管问询及回复索引.md` | SSE project index |
| SZSE index | `review_comments/深交所监管问询及回复索引.md` | SZSE project index |

Actual counts and the corpus cutoff depend on the authorized knowledge base configured by the user. Read its root and module indexes before describing coverage.

## Regulatory record schema

The YAML frontmatter normally includes:

- `source_id`
- `company`
- `project`
- `market`
- `industry_code` (`Wind行业`)
- `industry_name`
- `industry_classification_status`
- `industry_basis`
- `question_number`
- `topic`
- `question_scope` (`通用问题` or `行业特有问题`)
- `tags`
- `source_title` (the formal or normalized source title; normalized variants omit every occurrence of “关于”)
- `source_file`
- `source_pages`
- `boundary_basis`

The body contains `分类信息`, `问询`, and `回复`.

## Retrieval guidance

Use the sources in this order:

1. Read `general_dd_manuals/GEN-001 通用尽调教学框架.md` for the complete applicable baseline.
2. Select the transaction-specific module:
   - IPO: read `ipo_dd_manuals/README.md`;
   - M&A, equity financing, or debt financing: read `ma_financing_dd_manuals/README.md`;
   - mixed or pre-IPO financing: read both.
   Then retrieve each relevant practice section for business and financial detail.
3. Search `review_comments/` for industry, business-model, and market-specific regulatory focus.

For manual retrieval and display:

- Never return `document_id`, a section number, or a checklist ID alone as `依据`.
- Open the relevant source section and display `编号｜来源文件名称｜章节或事项标题｜本项对应的尽调关注内容`.
- Derive the attention content from the opened section's proposition, principal risk, evidence, or verification focus; do not guess from the number.
- If the mapping cannot be resolved, mark it unverified and omit the bare code from the user-facing basis.

For regulatory retrieval:

- Start broad with the diligence topic.
- Add business-model terms such as `经销商`, `境外销售`, `委外加工`, or `研发`.
- Use `--market` and `--industry` as scoring boosts, not absolute filters, unless strict filtering is requested.
- Prefer records from the latest available three to five years and disclose the actual date range and corpus cutoff.
- Treat repeated questions across multiple projects as a regulatory pattern; label isolated cases accordingly.
- Open the returned source file before citing it. Search results are candidate evidence, not final conclusions.
- Cite a record as a case only when `company`, `source_title`, `source_file`, and `source_pages` are all present and verified against the title-resolution rule in `SKILL.md`.
- In the answer, show the specific company name, `source_title` enclosed in `【】`, and exact page or page range together for each individual case.
- Use `source_file` only to locate and audit the underlying record. Never display its coded PDF filename in place of the first-page formal title.
