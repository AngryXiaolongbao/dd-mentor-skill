# Knowledge map

## Knowledge root

Set the knowledge root with:

`DDMENTOR_KNOWLEDGE_ROOT`

For backward compatibility, the skill also accepts `DDBIBLE_KNOWLEDGE_ROOT`. If neither environment variable is present, the skill looks for `<skill-directory>/knowledge`. The GitHub package includes rewritten teaching guidance and public regulatory inquiry-and-response records. It excludes original proprietary manual text.

## Modules

| Module | Path | Purpose |
| --- | --- | --- |
| Root index | `README.md` | Module overview and counts |
| IPO topic guide | `ipo_dd_manuals/IPO-RW-001 专项尽调教学指南.md` | Rewritten IPO and financial verification guidance |
| General framework | `general_dd_manuals/GEN-RW-001 通用尽调教学框架.md` | Rewritten cross-transaction diligence framework |
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
- `source_file`
- `source_pages`
- `boundary_basis`

The body contains `分类信息`, `问询`, and `回复`.

## Retrieval guidance

Use the sources in this order:

1. Read `general_dd_manuals/GEN-RW-001 通用尽调教学框架.md` for the complete applicable baseline.
2. Read `ipo_dd_manuals/README.md`, then retrieve each relevant topic-specific practice standard for business and financial detail.
3. Search `review_comments/` for industry, business-model, and market-specific regulatory focus.

For regulatory retrieval:

- Start broad with the diligence topic.
- Add business-model terms such as `经销商`, `境外销售`, `委外加工`, or `研发`.
- Use `--market` and `--industry` as scoring boosts, not absolute filters, unless strict filtering is requested.
- Prefer records from the latest available three to five years and disclose the actual date range and corpus cutoff.
- Treat repeated questions across multiple projects as a regulatory pattern; label isolated cases accordingly.
- Open the returned source file before citing it. Search results are candidate evidence, not final conclusions.
