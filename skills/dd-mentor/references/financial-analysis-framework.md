# Financial analysis framework

Use this framework whenever the user provides usable financial data after the confidentiality gate has been confirmed. Financial data includes financial statements, management accounts, trial-balance summaries, operating KPI tables, budgets, forecasts, financing models, or multi-period figures pasted into the conversation.

The purpose is not to produce a ratio dump. Teach the user how a numerical signal becomes a risk hypothesis, what alternative explanations may exist, what evidence distinguishes them, and how the diligence plan should change.

## 1. Establish the data perimeter

Before calculating, identify and disclose, to the extent available:

- reporting entity and consolidation perimeter;
- period covered and whether figures are point-in-time, year-to-date, annual, budget, forecast, or actual;
- currency and unit;
- accounting basis and whether figures are audited, reviewed, or unaudited;
- consolidated or standalone basis;
- any restatement, reclassification, normalization, or missing period.

Extract information already contained in uploaded materials instead of asking the user to repeat it. Preserve original figures and clearly label every transformation. Do not invent a missing number or silently mix periods, entities, currencies, or accounting bases.

If a metric cannot be calculated reliably, state `无法计算`, identify the missing input, and explain why that input matters. Continue with the metrics that can be calculated; do not wait for a perfect dataset.

## 2. List the main financial indicators

Select all indicators that are relevant and supported by the available data. At minimum consider:

### Scale and growth

- revenue, year-on-year growth, CAGR, and contribution by product, customer, geography, or segment when available;
- order intake, backlog, unit volume, average selling price, or other industry KPIs when available;
- total assets and operating scale.

### Profitability

- gross profit and gross margin;
- operating profit and margin;
- EBITDA and EBITDA margin only when EBITDA is supplied or can be transparently reconciled;
- net profit and net margin;
- selling, administrative, R&D, and finance expense ratios;
- normalized earnings, with every adjustment shown separately.

### Cash flow and earnings quality

- operating cash flow;
- operating cash flow to net profit;
- free cash flow and capital expenditure;
- cash conversion and the difference between accounting profit and cash generation;
- non-recurring or non-cash items that materially affect earnings.

### Working capital

- accounts receivable, inventory, accounts payable, contract assets, and contract liabilities;
- DSO, DIO, DPO, and cash conversion cycle where the required data exists;
- growth of working-capital balances compared with revenue or cost growth;
- aging, impairment, write-off, and concentration indicators when available.

### Liquidity and solvency

- cash, restricted cash, interest-bearing debt, and net debt;
- current ratio and quick ratio;
- debt-to-equity, net debt to EBITDA, and interest coverage where meaningful;
- debt maturity concentration, covenant headroom, and refinancing dependence;
- cash burn and runway for loss-making or early-stage companies.

### Returns and operating efficiency

- ROA, ROE, ROIC, and asset turnover where inputs are adequate;
- fixed-asset utilization, capacity utilization, or unit economics when available.

### Transaction-specific indicators

- financing use-of-proceeds coverage, milestone funding needs, dilution, and runway for financing projects;
- leverage, debt service, covenant capacity, and downside headroom for debt financing;
- quality of earnings, normalized working capital, net debt, and potential purchase-price adjustments for M&A.

For turnover and return ratios, use average opening and closing balances when available. State when ending balances are used as a proxy. Use 365 days unless a shorter reporting period requires a disclosed annualization convention. Never present an internally derived EBITDA or normalized profit as audited.

## 3. Identify and classify anomalies

Analyze changes across periods and relationships among statements, notes, and operating data. Use external peer or industry benchmarks only when a current, verifiable source is available; identify the source and keep benchmark differences separate from internal trend anomalies.

For each signal:

1. quantify its magnitude and the affected period;
2. classify it as `已确认异常`, `异常迹象`, or `数据限制`;
3. identify both plausible benign explanations and adverse explanations;
4. state what evidence would distinguish those explanations;
5. assign P0, P1, or P2 based on transaction relevance and materiality.

Common patterns to test include:

- revenue growth without corresponding operating cash flow or with disproportionate receivables growth;
- abrupt gross-margin or expense-ratio changes not explained by product mix, pricing, input costs, or accounting classification;
- inventory growth, aging, write-down, or turnover changes inconsistent with sales and production;
- persistent profit with negative free cash flow;
- short-term debt, covenant, or runway pressure;
- unusual related-party, non-recurring, fair-value, subsidy, capitalized-cost, or other accounting items;
- inconsistencies among capex, fixed assets, depreciation, capacity, and output;
- divergence between book profit, taxable income, tax expense, and cash taxes;
- unexplained changes in impairment, provisions, estimates, or accounting policies;
- inconsistencies between financial data and operating KPIs, contracts, invoices, logistics, bank flows, or disclosed business facts.

An anomaly is a signal to investigate, not proof of misstatement or misconduct. State uncertainty explicitly.

## 4. Convert anomalies into targeted diligence

For every P0/P1 anomaly and every material P2 anomaly, teach and apply this chain:

`metric signal → risk hypothesis → plausible alternative explanations → distinguishing evidence → verification procedure → red flag → next branch`

Each recommendation must be specific enough to execute. Avoid generic wording such as `关注收入真实性`. State:

- the assertion or transaction issue being tested;
- the data, documents, third-party evidence, and reconciliations required;
- the analytical, inspection, confirmation, interview, recalculation, cutoff, tracing, or other procedure to perform;
- the population and sampling consideration when relevant;
- the expected relationship or result;
- the exception threshold or red flag;
- the next procedure, escalation, specialist involvement, or scope change if the exception remains.

Map anomaly-driven procedures back to the applicable Layer 1 baseline matter and Layer 2 topic-specific detail. Add or reprioritize checklist items when the financial signal changes the project risk profile.

## 5. Apply Mentor teaching rules

For each P0/P1 anomaly:

- explain the metric and formula in beginner-friendly language;
- explain why the movement matters for this transaction;
- distinguish accounting presentation from economic substance;
- describe at least one innocent explanation and one adverse explanation;
- show why the proposed evidence is persuasive and where it is limited;
- identify a common beginner mistake, such as treating correlation as proof or relying on a management explanation without reconciliation.

Financial analysis must remain integrated with Planning, Teaching, Risk Thinking, and Dynamic Update. It is not a separate conclusion and does not replace audit, valuation, legal, tax, or investment work.

## 6. Mandatory output

### Main indicators

| 指标 | 公式及口径 | 各期数据 | 变化趋势 | 初步解读 | 数据限制 |
| --- | --- | --- | --- | --- | --- |

### Anomalies

| 优先级 | 异常或信号 | 量化依据 | 性质 | 可能的正常解释 | 可能的风险解释 | 尚需区分的关键证据 |
| --- | --- | --- | --- | --- | --- | --- |

### Targeted diligence advice

| 关联异常 | 风险假设 | 所需资料及证据 | 核查程序 | 异常标准或红旗 | 下一步及升级路径 | 对应基础/专项事项 |
| --- | --- | --- | --- | --- | --- | --- |

Follow these tables with teaching cards for P0/P1 anomalies. Carry unresolved anomalies into the priority map, open items, scope-change triggers, and risk-control-versus-defense hearing minutes.

## 7. Three-review requirement

The financial analysis is subject to the same three internal reviews as the rest of the DD Mentor output:

1. **Calculation and definition review**: recalculate material indicators; reconcile formulas, periods, units, signs, entity perimeter, and source figures; identify unavailable inputs and proxy assumptions.
2. **Manual and anomaly completeness review**: compare each material signal and proposed procedure against the applicable general and topic-specific manuals; check cross-statement, trend, cash-flow, working-capital, solvency, profitability, and transaction-specific relationships.
3. **Risk-control challenge and defense**: have the risk-control reviewer challenge whether the anomaly is real, material, properly interpreted, and adequately addressed; have the defense distinguish confirmed facts, alternative explanations, evidence gaps, and proposed procedures; record the disposition and resulting checklist change in the teaching minutes.

If a review changes a calculation, priority, risk hypothesis, or procedure, rerun every affected review before delivery.
