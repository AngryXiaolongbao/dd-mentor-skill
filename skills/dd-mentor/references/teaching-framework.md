# Teaching framework

## Purpose

Teach the user how to think through diligence, not merely what documents to request. Use plain language and connect every conclusion to the current project.

## Teaching card

For each P0/P1 item or requested explanation, cover:

1. **一句话结论** — explain why this item exists.
2. **要证明什么** — identify the transaction, accounting, legal, or business proposition.
3. **风险是怎样发生的** — describe the plausible failure mode without assuming misconduct.
4. **证据链** — show the sequence of documents, data, third-party evidence, and reconciliations.
5. **为什么这些证据有效** — explain the strength and limitation of each link.
6. **怎样执行** — give the procedure in a practical order.
7. **看到什么要警惕** — identify exception signals.
8. **异常后走哪条分支** — give conditional follow-up rather than “further investigate”.
9. **与本项目的关系** — connect the lesson to known project facts.
10. **监管视角** — explain why an exchange or reviewer may care, with a source when available.
11. **新人常见误区** — correct one likely misconception when useful.
12. **依据及对应关注内容** — never show only a manual number; identify the source file, section or matter title, and explain which diligence concern that source supports.

## Causal-chain rule

Use this structure:

`目标命题 → 可能错在哪里 → 用什么证据证明 → 证据之间如何勾稽 → 什么异常推翻原判断 → 下一步查什么`

Do not replace causality with a longer document list.

## Example 1 — Revenue cut-off

### 一句话结论

收入截止测试不是为了检查日期格式，而是为了判断收入是否被确认在正确期间，防止提前确认或延后确认收入。

### Logic

`收入真实性和期间准确性`
`→ 临近期末交易可能被确认在错误期间`
`→ 抽取期末前后订单和合同`
`→ 对照出库单、物流记录、客户签收或验收、发票和回款`
`→ 判断合同约定的控制权转移条件是否在期末前真正满足`

Each document proves a different link:

- contract/order: what event should trigger recognition;
- outbound record: goods left the warehouse, but does not alone prove customer acceptance;
- logistics record: movement and timing, but may not prove control transfer;
- receipt/acceptance: whether the customer received or accepted the product;
- invoice: tax or billing evidence, not automatically the accounting recognition point;
- payment: commercial substance support, but timing may differ from recognition.

### Red flags and branches

- Shipment before year-end but receipt after year-end → reassess the contractual recognition point and test whether revenue was recorded early.
- Receipt evidence created in batches or with identical handwriting → obtain third-party logistics data, customer confirmation, system logs, or alternative evidence.
- Invoice date, shipment date, acceptance date, and ledger date do not reconcile → expand the sample and quantify the possible period misstatement.

### Beginner misconception

“已经开票” or “已经出库” does not automatically mean revenue can be recognized.

## Example 2 — Bank-flow review

### 一句话结论

Bank-flow review tests whether the recorded business and related-party picture is consistent with actual movement of funds.

### Objectives

- support revenue and collection authenticity;
- identify undisclosed related parties or circular fund flows;
- detect fund occupation, third-party payments, personal-card use, or off-book arrangements;
- reconcile cash flow with contracts, invoices, ledgers, and counterparties.

### Evidence chain

`bank statement → material or unusual transaction → counterparty identity → contract/order/invoice → ledger entry → business purpose and approval → related-party and fund-occupation assessment`

### Red flags and branches

- Large receipt quickly transferred to another party → trace both legs, identify ultimate counterparties, inspect contracts and invoices, and assess circular funding.
- Frequent personal or employee accounts → identify beneficial users, reconcile underlying transactions, assess personal-card or off-book activity, and expand the review population.
- Counterparty name differs from the customer or supplier → test third-party payment rationale, authorization, commercial substance, and related-party links.
- Unexplained transfers with shareholders or management → inspect purpose, approvals, repayment, interest, and possible fund occupation.

### Beginner misconception

Bank-flow review is not satisfied by collecting statements. The work begins when flows are reconciled to counterparties and business evidence.

## Teaching depth

- Give every baseline item a concise “要证明什么 + 为什么 + 风险”.
- Give every P0/P1 item a full teaching card.
- Expand any P2 item into a full teaching card when the user asks “为什么” or when an exception emerges.
- Prefer one well-explained causal chain over several unexplained procedures.
