# Output schema

In every section, an `依据` field must comply with the manual-basis and regulatory-case citation rules in `SKILL.md`. Never output only a number or code. Resolve it into the source name, section or item title, and the corresponding diligence attention content.

## 0. Material-assisted planning discussion

In Plan mode with uploaded materials, do not use the full output schema until the three-phase planning discussion in [conversation-engine.md](conversation-engine.md) is complete or the user explicitly requests immediate output.

During the discussion, use the complete fixed structure in [round-response-format.md](round-response-format.md). It must include:

- the user-feedback and project-understanding update;
- Teaching on why the feedback changes diligence;
- the rolling risk map;
- provisional snapshots for **基础尽调事项**, **业务及专项尽调细节**, and **行业、业务特点及近年监管关注**;
- open items and provisional assumptions;
- one to three questions, why each needs an answer, what each answer changes, and the `请建议` option.

The three phases are understanding calibration, risk interpretation, and scope alignment. Do not append the first full checklist merely because the materials appear complete.

## 1. Project profile

Begin with “我对项目的理解”. Summarize the purpose, listing intent, industry/products, business model, approximate scale, stage, role, known risk flags, assumptions, and missing facts in plain language.

## 1A. Textual-material extraction (when materials are provided)

Apply [textual-material-extraction.md](textual-material-extraction.md) whenever the user uploads or pastes textual materials. Before continuing the analysis, present:

1. the document scope, dates, versions, and extraction limitations;
2. standardized financial data with period, entity, perimeter, currency, unit, status, and exact source location;
3. structured business facts with fact status, source location, scope impact, and verification need;
4. conflicting figures or assertions, important missing information, and unsupported claims.

Then carry the extracted data and facts into the project profile, financial anomaly analysis, priority map, three-layer checklist, follow-up questions, completeness review, and risk-control-versus-defense hearing. Do not provide only a narrative summary.

## 2. Priority map

- **P0 — critical**: could undermine transaction eligibility, financial authenticity, ownership, or a central investment thesis.
- **P1 — high**: material risk requiring dedicated procedures and senior review.
- **P2 — baseline**: standard diligence required for completeness.

Explain why each P0/P1 area is elevated for this project. A priority label without the project fact and risk logic is invalid.

## 2A. Financial indicators and anomaly analysis (when data is provided)

Apply [financial-analysis-framework.md](financial-analysis-framework.md) whenever usable financial data is available. Present:

1. the main applicable indicators, with formulas, periods, units, perimeter, trends, and data limitations;
2. quantified anomalies classified as `已确认异常`, `异常迹象`, or `数据限制`, with both plausible normal and adverse explanations;
3. anomaly-driven targeted diligence advice mapped to the relevant Layer 1 and Layer 2 matters;
4. teaching cards for every P0/P1 anomaly.

Carry material financial anomalies into the priority map, completeness review, risk-control-versus-defense hearing, open items, and dynamic update. Do not present a financial signal as proof, use an unsourced peer benchmark, or provide generic advice without an evidence and procedure chain.

## 3. Layer 1 — Complete baseline checklist

Start from `GEN-001 通用尽调手册`. List every applicable baseline diligence matter, grouped under clear workstreams. Do not cap the baseline at 8–15 items. If a source item is not applicable, mark it `不适用` and briefly explain why; do not silently omit it.

For every item include:

- **需要做什么**
- **要证明什么**
- **为什么要做**
- **不做或做错会有什么风险**
- **先取得哪些资料**
- **怎样核查**
- **发现异常后怎么办**
- **知识库依据**（编号、来源文件、章节或事项标题，以及该编号对应的尽调关注内容）

Use a table only when it remains easy for a beginner to read:

| 优先级 | 尽调事项 | 要证明什么 | 为什么要查及主要风险 | 主要资料与程序 | 异常信号及下一步 | 依据及对应尽调关注内容 |
| --- | --- | --- | --- | --- | --- | --- |

Never list a diligence requirement without explaining why it exists.

For P0/P1 items, follow the baseline table with a teaching card using [teaching-framework.md](teaching-framework.md).

## 4. Layer 2 — Business and topic-specific detail

For each relevant baseline workstream, use the applicable topic-specific practice manual to add:

- detailed information requests;
- evidence and reconciliation requirements;
- verification procedures and sampling considerations;
- common exception signals;
- escalation and follow-up procedures;
- the exact manual number, source name, section title, and the corresponding diligence attention content.

Map each detail back to its Layer 1 baseline matter. Avoid duplicating the same requirement as an unrelated new item.

## 5. Layer 3 — Industry, business model, and recent regulatory focus

Separate this layer from the manual-derived checklist. For each direction include:

- the project feature that makes it relevant;
- whether it is industry-specific, business-model-specific, or market-specific;
- the latest available period reviewed;
- whether the pattern is recurring or based on a limited number of cases;
- what regulators asked, what evidence was used in replies, and how to prepare;
- the cited inquiry-and-reply records, with a specific company name, source file, and exact page or page range for every case.

Present cases in a structure that preserves the one-to-one mapping:

| 公司名称 | 项目/板块 | 监管问题 | 回复要点及所用证据 | 对本项目的启示 | 引用文件 | 页码 |
| --- | --- | --- | --- | --- | --- | --- |

In `引用文件`, use the formal or normalized source title and enclose it in Chinese square brackets, for example `【××公司首次公开发行股票并上市申请文件审核问询函的回复】`. When equivalent title variants differ only by “关于”, remove every occurrence of “关于”. Do not show an internal PDF code, local Markdown filename, `source_id`, archive name, or an inferred abbreviation.

Do not use “某公司” or combine several companies under one shared citation. If `公司名称`、正式或规范化文件名 or `页码` cannot be verified from the opened record, omit the case rather than presenting it with an incomplete citation.

Prefer cases from the latest available three to five years and disclose the knowledge-base cutoff. Do not label older or undated material as “recent”.

## 6. Completeness review statement

Before displaying Layer 1 or Layer 2, complete the three internal reviews required by Workflow Step 8 of `SKILL.md`. Include a concise result without exposing private chain-of-thought:

| 复核轮次 | 风控复核目标 | 对照依据 | 复核结论及已修正事项 | 剩余限制 |
| --- | --- | --- | --- | --- |
| 第一轮 | 基础事项完备性 | 通用尽调教学框架的全部适用章节 | 已覆盖、补充或调整的主要事项 | 因资料缺失仍需确认的范围 |
| 第二轮 | 业务及专项细节完备性 | 相关业务及财务专项指南 | 已补充的证据链、程序、抽样或异常分支 | 尚无适用指引或需专家判断的事项 |
| 第三轮 | 风控挑战及项目答辩 | 项目事实、P0/P1风险、监管关注及前两轮结果 | 经挑战、答辩和风控裁定后纠正的优先级、逻辑、引用或范围问题 | 未解决议题及其补充证据和升级路径 |

Do not use generic statements such as “已复核，无遗漏” without identifying the sources compared and any remaining limitation. If a review identifies a material issue, revise the checklist and rerun the affected round before presenting the result.

In `对照依据`, `项目答辩及依据`, and any Manual-basis field below, expand every numbered reference into its source name, section or matter title, and the diligence attention content relevant to the conclusion.

## 7. Risk-control and defense hearing minutes

After the completeness statement, include **风控—答辩纪要** for every material Round 3 challenge. Summarize the exchange rather than exposing private chain-of-thought.

| 议题及关联清单项 | 风控挑战 | 项目答辩及依据 | 风控结论 | 清单或优先级调整 | 新人学习要点 |
| --- | --- | --- | --- | --- | --- |
| 具体 P0/P1 风险或跨工作流矛盾 | 指出哪个结论尚不充分、可能错在哪里以及为何现有程序不足 | 区分已确认事实、假设、现有证据、Manual依据、证据缺口和拟补程序 | `已解决`、`部分解决`或`未解决`，并说明理由 | 列明新增、深化、调级、责任人、所需证据和触发条件 | 解释本次挑战体现的 DD 思维及新人容易忽略的点 |

Apply these rules:

- Cover every P0/P1 item and every material issue identified in Rounds 1 and 2. Consolidate genuinely repetitive challenges, but do not hide a distinct unresolved risk.
- Let the defense answer only from identified evidence and authority. If evidence is missing, state that directly and do not portray a proposed procedure as a completed conclusion.
- Let the reviewer make the final disposition; the defense cannot mark its own answer as sufficient.
- For `部分解决` or `未解决`, state the required evidence, next procedure, responsible workstream or specialist, and the fact that would change scope or priority.
- Include a short **答辩教学总结** after the table: the strongest defense, the weakest defense, the most important unresolved issue, and how a beginner should prepare a better answer next time.

## 8. Diligence focus

Highlight three to five project-specific priorities. Explain which project fact elevates each priority and how it differs from baseline diligence.

## 9. Teaching summary

Conclude the first plan with:

- **本项目最重要的三条 DD 逻辑**
- **新人最容易犯的错误**
- **如果只能先做三件事**
- an invitation to choose one workstream for a deeper teaching walkthrough.

## 10. Open items

List missing facts, unavailable documents, assumptions, specialist needs, and facts that would change scope.

Separate:

- information the user may provide now;
- documents to request from the company;
- matters to investigate during diligence.

Do not turn the latter two into retrospective criticism that the user failed to answer the intake interview.

## 11. Dynamic update

When new information arrives, show:

| 新事实或发现 | 风险判断变化 | 清单变化 | 优先级变化 | 为什么 |
| --- | --- | --- | --- | --- |

Then provide only revised or newly affected sections unless a full regenerated checklist is requested.
