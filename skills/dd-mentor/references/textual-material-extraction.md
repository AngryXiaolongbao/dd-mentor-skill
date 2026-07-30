# Textual material extraction framework

Use this framework after the confidentiality gate is confirmed whenever the user uploads or pastes narrative materials. These include project introductions, teasers, information memoranda, financing materials, prospectuses, application documents, annual reports, audit reports, management reports, meeting materials, contracts, Word files, PDFs, presentations, emails, and OCR text.

The extraction is an input to DD Mentor analysis, not a separate summary exercise and not a substitute for the planning discussion. Extract facts first, preserve their source and status, then use them to update the project profile, financial analysis, risk hypotheses, checklist, and follow-up questions.

## 1. Establish the document set

For each material, identify when available:

- document name and type;
- reporting or reference date;
- covered entity and consolidation perimeter;
- whether the content is historical, current, budget, forecast, target, management assertion, or third-party statement;
- whether it is audited, reviewed, verified, unaudited, or of unknown status;
- page, section, table, note, or other precise source location;
- OCR, truncation, illegibility, missing-page, or version limitations.

Do not silently combine different entities, periods, currencies, units, accounting bases, or document versions. If two materials conflict, retain both values, identify the conflict, and state what must be verified.

## 2. Extract standard financial data

Extract every reliably identifiable financial figure and standardize it into the following fields:

| 字段 | 要求 |
| --- | --- |
| 指标 | Use a standard account or metric name; retain the source label when it differs |
| 期间/时点 | State the exact period or balance-sheet date |
| 金额 | Preserve the reported value |
| 币种及单位 | Do not infer silently; mark unknown when absent |
| 主体及口径 | Consolidated/standalone, entity, segment, actual/budget/forecast |
| 数据性质 | Reported, derived, management assertion, or inference |
| 审计状态 | Audited, reviewed, unaudited, or unknown |
| 来源定位 | Document name plus exact page/section/table when available |
| 备注 | Restatement, reclassification, normalization, ambiguity, or limitation |

At minimum look for, when present:

- revenue, cost of sales, gross profit, operating profit, EBITDA, net profit, and major expense categories;
- cash, restricted cash, accounts receivable, inventory, accounts payable, contract assets/liabilities, fixed assets, total assets, debt, total liabilities, and equity;
- operating, investing, and financing cash flow; capital expenditure and free cash flow;
- segment, product, geography, customer, channel, recurring/non-recurring, or related-party breakdowns;
- orders, backlog, units, price, capacity, utilization, headcount, stores, users, or other operating KPIs;
- budgets, forecasts, valuation assumptions, financing needs, use of proceeds, debt maturities, covenants, and transaction adjustments.

Apply these controls:

1. Keep historical actuals separate from budgets, forecasts, targets, and pro forma figures.
2. Preserve signs and units; disclose every unit conversion.
3. Label a calculated value `derived` and show its formula.
4. Do not treat rounded narrative wording such as “约一亿元” as an exact number.
5. Reconcile repeated figures across summaries, statements, notes, and different documents. Flag unreconciled differences.
6. Do not infer a missing financial statement line from narrative context unless the derivation is mathematically supportable and labelled.
7. If no reliable financial figures exist, state that no standard financial dataset could be extracted; do not manufacture one.

Pass the standardized dataset to [financial-analysis-framework.md](financial-analysis-framework.md). List the main indicators, identify anomalies, and convert material anomalies into targeted diligence advice.

## 3. Extract business facts

Create a structured business profile from statements supported by the materials. At minimum consider:

- company identity, history, ownership and group structure;
- principal products or services and their use cases;
- industry, market position, competitors, and growth drivers;
- business model, value chain, revenue model, pricing, settlement, and recognition logic;
- sales channels, customer types and concentration statements;
- procurement model, supplier types, key inputs, outsourcing, and supply dependencies;
- production or service delivery process, facilities, capacity, utilization, and geographic footprint;
- R&D model, technology, intellectual property, product pipeline, and commercialization stage;
- licenses, permits, quality systems, environmental, safety, data, healthcare, export-control, or other regulatory dependencies;
- employees, management, incentives, related parties, and key-person dependencies;
- strategy, expansion plans, financing purpose, transaction rationale, and principal risks disclosed by management.

For every material fact, record:

| 业务主题 | 提取事实 | 事实状态 | 来源定位 | 对尽调范围的影响 | 待验证事项 |
| --- | --- | --- | --- | --- | --- |

Use `事实状态` to distinguish:

- `文件明确陈述`;
- `多份资料相互印证`;
- `合理推断`;
- `存在冲突`;
- `尚无法确认`.

Do not convert promotional language into confirmed fact. For example, “行业领先” remains a management assertion until supported by a defined market, period, metric, and independent evidence.

## 4. Continue DD Mentor analysis

After extraction:

1. update “我对项目的理解” and separate confirmed facts, reasonable inferences, conflicts, and unknowns;
2. run the financial analysis framework on the extracted standardized financial dataset;
3. use business facts to determine transaction type, listing intent, industry, business and revenue model, scale, venue, stage, and role;
4. identify how each material fact changes a risk hypothesis, priority, evidence need, procedure, or follow-up branch;
5. prepare, but do not yet deliver, the three knowledge layers;
6. enter the material-assisted discussion path in [conversation-engine.md](conversation-engine.md);
7. ask only one to three questions per phase, focused on interpretation and scope rather than facts already extracted;
8. after the discussion gate is completed, retrieve and deliver all three knowledge layers and show what remains to be verified during diligence.

Teach the link:

`source statement or figure → reliability and limitation → project fact → risk implication → evidence needed → diligence response`

Do not merely summarize the materials. A narrative extraction that is not carried into the risk analysis and diligence scope is incomplete.

## 5. Mandatory staged output when textual materials are provided

### Before the planning discussion is complete

Provide only the material needed for the current dialogue phase:

1. **资料范围及限制**: documents read, dates, versions, OCR or missing-page limitations.
2. **材料初步理解**: the key standardized figures and business facts needed to calibrate understanding.
3. **冲突、缺失及待核实事项**: material inconsistencies, ambiguous periods or units, unsupported claims, and important gaps.
4. **本轮讨论**: one to three questions plus why each answer changes the risk view or scope.

Do not append the first full checklist, exhaustive financial analysis, or final recommendations while the discussion gate is pending.

### After the planning discussion is complete

Include:

1. **标准财务数据表**: all reliable figures in the standard fields above.
2. **业务情况提取表**: material business facts, status, source, scope impact, and verification need.
3. **继续分析结果**: updated project profile, financial indicators and anomalies, targeted diligence advice, priority changes, and checklist changes.

Exact page references are required when the source format has stable pages. Otherwise cite the narrowest available section, heading, table, slide, paragraph, or message identifier.

## 6. Review requirements

Apply the same three DD Mentor review rounds:

1. verify extraction completeness, transcription accuracy, units, periods, entities, document locations, and reconciliation;
2. compare extracted facts and resulting procedures with applicable general and topic-specific manuals;
3. challenge the reliability of key assertions and figures from both risk-control and project-defense perspectives, then record the disposition and resulting checklist change.

If a correction changes a figure, fact, anomaly, priority, or procedure, rerun the affected analysis and review rounds before delivery.
