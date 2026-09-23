# Lab 09 — ABG pro-forma engine

## Purpose and source

Build a five-year income statement, balance sheet, and cash-flow engine, then test it against the supplied ABG classroom case. This is an instructional valuation, not a new investment recommendation. Source: [Lab 09 instructions and supplied assumptions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-05/lab-09-proforma-build.md), sections R, I, and V, accessed September 22, 2026. Model periods: FY2026E–FY2030E; opening balances: FY2025. Monetary amounts are USD millions, shares are millions, and value per share is USD.

## Prework — student's own explanations

> the three judgements that i think carry ABG's valuation are SG&A as a share of gross profit (66.5% falling to 64.5% recovery path), the 10% cost of equity and the 2.5% terminal growth rate. Since 80% of the $291.75 value sits beyond 2030, the terminal value is an enormous part of ABG's valuation

> Cash is computed last because it is not an assumption, it depends on how non-cash charges, capex, working capital and debt repayment assumptions work out, and then the number becomes known, and gives a balance check.

The student confirmed completing the explanation aloud to their partner. AI clarified that buybacks and revolver movements also enter the cash calculation. Cash is derived from flows, not set as a balancing plug.

## Workspace check

The saved Week 3 `dcf.py` was rerun successfully. UiPath base value remained $14.3050 per diluted share; the sensitivity range remained $13.31–$20.86. The ABG engine is separate from those UiPath assumptions.

## Implementation

Deliverable: `proforma.py`, a single Python file using only the standard library. The `OPENING` and `ASSUMPTIONS` blocks contain the course case inputs. Each assumption is labeled history, guidance, judgment, or fact in the code, following the course labels. These labels do not claim independent filing research by the student. Historical ratios retain the exact divisions supplied by the course.

Annual computation follows operations, noncash balance-sheet balances, cash flows, and finally cash and revolver financing. Impairment reduces other assets; depreciation reduces PP&E. Floor-plan borrowing changes enter operating cash flow under this course convention. Buybacks reduce both cash and book equity. Revolver interest uses its opening balance, avoiding circularity.

The valuation discounts FCFE at the cost of equity. The terminal convention adds back the final scheduled term-debt repayment before applying perpetual growth, assuming those repayments cease after 2030. It is a simplifying classroom convention, not proof that future financing needs disappear. The supplied share count stays fixed despite modeled buybacks; no future repurchase-price or share-count schedule is supplied.

Run from the deliverables folder:

```bash
python3 proforma.py
```

## Known-answer validation — AI executed

| Measure | FY2026E | FY2030E |
| --- | ---: | ---: |
| Revenue | 18,323.0 | 19,678.3 |
| Operating income | 844.2 | 971.4 |
| Net income | 413.6 | 527.5 |
| FCFE | 211.4 | 342.3 |
| Closing cash | 101.8 | 719.8 |
| Assets less liabilities and equity | 0.0 | 0.0 |

All supplied benchmark figures match at the required displayed precision. Equity value is **$5,237.34 million**, value per share **$291.75**, and the share of value beyond 2030 **79.76%**.

Full-precision checks, with a $0.0000001 million tolerance, verify every year's balance sheet, cash-flow-to-balance-sheet cash reconciliation, cash minimum, and revolver capacity. The code recomputes checks rather than trusting cached totals. `value_equity` calls `assert_balanced` before calculating a value.

### Failure and financing tests

- In a separate in-memory copy, AI changed FY2026E balance-sheet cash to 40.4, leaving the computed flows unchanged. Valuation refused with **FY2026E: balance gap -61.4 USD million**. The delivered base file remains unbroken.
- A higher-buyback scenario required a revolver draw and later repayment; statements continued to balance and cash stayed at or above the minimum.
- A buyback exceeding available financing exhausted the revolver and triggered a cash-minimum error instead of an unfunded valuation.
- Terminal growth equal to the discount rate was rejected.

These are AI-run technical checks. They do not claim the student completed the separate partner swap exercise.

## Out-of-class completion — instructor-approved alternative

The student clarified that a partner was no longer available and reports that the instructor approved finishing this section out of class. This corrects the earlier statement that the partner swap was done. No partner-model results are claimed. The student's own engine reproduced $291.75 per share; the AI-run broken-cash test rejected valuation with a FY2026E gap of -$61.4 million, as documented above. The delivered model remains unbroken.

## Floor-plan explanation and final reflection

The student reports completing the remaining floor-plan explanation and final reflection aloud, including why cash is computed last and what the broken-case gap means. No partner attendance or verbatim written reflection is claimed.

## Checkout

Submission files: `proforma.py` and `lab09-proforma.md`. The model, validation results, reported instructor-approved alternative, and oral-reflection completion are recorded. Remaining action: upload both files to GitHub and submit their links in the Lab 09 checkout. No GitHub upload has been performed by AI for Lab 09.
