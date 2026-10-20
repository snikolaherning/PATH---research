# Lab 11 — UiPath: find the operating drivers

**Written analysis and code complete; GitHub submission outstanding.**

## Question

Which assumptions drive my company's forecast and value, and what explains their effects?

## Base checkpoint — September 29, 2026

The Lab 10 model was rerun without changing inputs. Its full visible output exactly matches `lab10-model-results.txt`; the base output is saved as `lab11-base-output.txt`, with inputs and model hash in `lab11-base-inputs.json`. All accounting and refusal checks pass.

Comparable base outputs, FY2031: operating profit $268.000m; FCFE $193.372m. The conditional annual-base valuation is $5.6891/share. It retains the Lab 10 tax, date, acquisition and deferred-revenue-reconciliation qualifications; it is not an updated September 29 fair-value estimate. If those qualifications prevent a defensible valuation comparison for a scenario, report value unavailable and retain signed operating-profit/FCFE outputs. The positive-only course valuation is not used in Lab 11; negative cash flows must remain signed.

Lab 10 already included some sensitivity examples. Their existence is prior knowledge, not a new locked prediction. The changed runs were subsequently performed only after the save and partner-check confirmation below.


## Student-selected ranges and rationale

Second operating driver: revenue growth, to test the student's claim that growth matters less than SG&A. Tests change only one independent input path at a time; SG&A is not simultaneously changed in the revenue-growth cases. Lower/higher refers to the numerical input, not the attractiveness of the outcome.

| Independent input / case | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
| --- | ---: | ---: | ---: | ---: | ---: |
| SG&A / gross profit — lower | 65% | 62% | 59% | 56% | 53% |
| SG&A / gross profit — base | 65% | 63.5% | 62% | 60.5% | 59% |
| SG&A / gross profit — higher | 65% | 65% | 65% | 65% | 65% |
| Revenue growth — lower | 10.2% | 8% | 7% | 6% | 5% |
| Revenue growth — base | 11.2% | 10% | 9% | 8% | 7% |
| Revenue growth — higher | 12.2% | 12% | 11% | 10% | 9% |

Student's SG&A range reason:

> The high case assumes no efficiency beyond the restructuring, while the low case assumes growth from existing customers and falling stock comp keep cutting costs to a mature-software level near 53%.

Student's revenue-growth range reason:

> FY2027 moves less because reaffirmed guidance anchors it, while the high case keeps growth near the current 12% ARR pace and the low case assumes net retention slips and growth fades to 5%.

Both ranges are **judgments**, not confidence intervals or company guidance. The mature-software 53% ratio is the student's scenario assumption, not a sourced peer benchmark. FY2027 ±1 percentage point is wider than the disclosed FY2027 guidance band, so these are stress departures from guidance; only the base is guidance-derived. ARR growth is contextual operating evidence, not a forecast of GAAP revenue growth.

SG&A's tested FY2031 input span is 12 percentage points; revenue growth's is 4 points, with different denominators and paths. Any eventual ranking must say **over these ranges** and cannot establish universal driver importance. The terminal growth input remains 3% and all other independent assumptions remain base; the existing terminal model mechanically inherits final-year operating ratios.


## Locked changed-input record and partner confirmation

Before the changed runs, the student selected the lower-SG&A path: 65%, 63.5%, 62%, 60.5%, 59% → 65%, 62%, 59%, 56%, 53%, with every other independent input at base. The original prediction was preserved by AI at September 29, 2026, 18:09:19 UTC (2:09:19 p.m. EDT). The student subsequently confirmed an offline save with AI closed at **Tuesday, September 29, 2026, 2:12 p.m. EDT**, and the partner's one-input-only check. That save time is student-reported, not an independently inspected editor timestamp. Reciprocal unit checks were also reported.

| Predicted FY2031 output | Base | Student point prediction | Student rough range |
| --- | ---: | ---: | ---: |
| Operating profit, $m | 268.00 | 387 | 375–395 |
| FCFE, $m | 193.37 | 285 | 275–295 |
| Annual-base value/share, $ | 5.69 | 7.30 | 7.10–7.40 |

The student's pre-run mechanism: a 6-percentage-point cut in the SG&A/gross-profit ratio on approximately $1,986m of FY2031 gross profit saves about $119m; after 23% tax, about $92m reaches FCFE. The student estimated additional discounted forecast cash flows at $149m and terminal cash flows at $703m, or roughly $1.59/share, and expected most of the gain after FY2031. These are preserved predictions, not actual results. AI pointed out the reserve-investment link before running; the point estimates remained unchanged.

The detailed chronological record is saved in `lab11-locked-prediction.md`. The previously observed Lab 10 high-SG&A result was prior knowledge, not presented as a new blind prediction. No changed-input run occurred before the student's confirmation.

## Implementation and reproducibility

Run **`python3 uipath_sensitivity.py`** with the unchanged **`uipath_proforma.py`** in the same folder. Both use Python's standard library. Ranges are embedded in the sensitivity runner; it needs no spreadsheet or external market data. Every lower/base/higher run receives a fresh copy of all assumptions and opening inputs. The runner verifies that only the named driver changes, checks all statements, reports signed differences and output spans, and restores and compares the entire base at the end.

Visible output is included below and written to `lab11-sensitivity-results.md`; full input sets, statements and named check residuals are retained in `lab11-sensitivity-audit.json`. The saved input snapshot and source hash are additionally checked if `lab11-base-inputs.json` accompanies the code. Invalid accounting runs are flagged and excluded; unavailable valuations retain valid profit/FCFE outputs and explain the limitation. Incomplete scenario sets are not eligible for a driver ranking.

An independent arithmetic audit confirmed signed deltas, spans, the cash-tax FCFE bridge, the SG&A/gross-profit link and restored base. This is a conditional sensitivity of the existing teaching model: the unresolved Lab 10 historical deferred-revenue residual, tax proxy and valuation-date limitations are not silently resolved by passing accounting checks.

## Executed sensitivity results

Ranges supplied by student; one independent input path changed per run.
Years: FY2027–FY2031. Profit and FCFE: USD millions; value/share: USD.
FCFE retains negative cash flows and the Lab 10 dilution-offset and cash-reserve conventions.
Value is conditional on the unchanged Lab 10 annual-base assumptions and disclosed limitations; it is not a September 29 price target.
Lower/higher describe the input, not a better/worse outcome. All other independent inputs, including 11% cost of equity and 3% terminal growth, stay at base.

## Actual input paths

| Driver | Case | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 | Units |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| SG&A / gross profit | lower | 65% | 62% | 59% | 56% | 53% | % of gross profit |
| SG&A / gross profit | base | 65% | 63.5% | 62% | 60.5% | 59% | % of gross profit |
| SG&A / gross profit | higher | 65% | 65% | 65% | 65% | 65% | % of gross profit |
| Revenue growth | lower | 10.2% | 8% | 7% | 6% | 5% | annual % revenue growth |
| Revenue growth | base | 11.2% | 10% | 9% | 8% | 7% | annual % revenue growth |
| Revenue growth | higher | 12.2% | 12% | 11% | 10% | 9% | annual % revenue growth |

## Comparable outputs and signed changes from base

| Driver | Case | FY2031 operating profit | Change | FY2031 FCFE | Change | Value/share | Change | Status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SG&A / gross profit | lower | 387.112 | +119.111 | 293.993 | +100.621 | 7.307 | +1.618 | valid (qualified annual-base value) |
| SG&A / gross profit | base | 268.000 | +0.000 | 193.372 | +0.000 | 5.689 | +0.000 | valid (qualified annual-base value) |
| SG&A / gross profit | higher | 148.889 | -119.111 | 92.750 | -100.621 | 4.071 | -1.618 | valid (qualified annual-base value) |
| Revenue growth | lower | 246.540 | -21.460 | 188.023 | -5.349 | 5.488 | -0.202 | valid (qualified annual-base value) |
| Revenue growth | base | 268.000 | +0.000 | 193.372 | +0.000 | 5.689 | +0.000 | valid (qualified annual-base value) |
| Revenue growth | higher | 290.909 | +22.908 | 198.537 | +5.165 | 5.904 | +0.215 | valid (qualified annual-base value) |

## Spans: maximum minus minimum over the stated ranges

| Driver | Profit span, $m | FCFE span, $m | Value/share span, $ |
| --- | ---: | ---: | ---: |
| SG&A / gross profit | 238.223 | 201.242 | 3.235 |
| Revenue growth | 44.368 | 10.514 | 0.416 |

## Accounting and isolation checks

Each figure is the largest absolute residual/shortfall across ALL printed checks for that year. Full named checks are retained in the JSON audit. Tolerance: 1e-7.

| Driver / case | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 | Changed independent inputs |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| SG&A / gross profit / lower | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | sga |
| SG&A / gross profit / base | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| SG&A / gross profit / higher | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | sga |
| Revenue growth / lower | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | growth |
| Revenue growth / base | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| Revenue growth / higher | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | growth |

Negative FCFE retained in sga/lower: FY2027.

Negative FCFE retained in sga/base: FY2027.

Negative FCFE retained in sga/higher: FY2027.

Negative FCFE retained in growth/lower: FY2027.

Negative FCFE retained in growth/base: FY2027.

Negative FCFE retained in growth/higher: FY2027.

**Restored base: PASS.** All inputs, all five years of statements, checks, and valuation outputs match the initial run within the stated absolute tolerance. Lab 10 source and module inputs are unchanged.

## Selected lower-SG&A trace

Base versus changed, by year. This is calculation evidence for the student to interpret, not a replacement for the student explanation.

| Year | Gross profit (unchanged) | Base SG&A | Changed SG&A | Profit change | Cash-tax change | Reserve change vs base | Change in annual reserve investment | FCFE change |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| FY2027 | 1,468.584 | 954.580 | 954.580 | +0.000 | +0.000 | +0.000 | +0.000 | +0.000 |
| FY2028 | 1,595.742 | 1,013.296 | 989.360 | +23.936 | +5.505 | -5.984 | -5.984 | +24.415 |
| FY2029 | 1,728.622 | 1,071.746 | 1,019.887 | +51.859 | +11.927 | -12.965 | -6.981 | +46.912 |
| FY2030 | 1,855.316 | 1,122.466 | 1,038.977 | +83.489 | +19.203 | -20.872 | -7.908 | +72.194 |
| FY2031 | 1,985.188 | 1,171.261 | 1,052.150 | +119.111 | +27.396 | -29.778 | -8.906 | +100.621 |

### Locked prediction versus actual

| Output | Predicted | Actual | Actual minus predicted | Inside rough range? |
| --- | ---: | ---: | ---: | --- |
| operating_profit_m | 387.000 | 387.112 | +0.112 | Yes |
| fcfe_m | 285.000 | 293.993 | +8.993 | Yes |
| value_per_share | 7.300 | 7.307 | +0.007 | Yes |

### Present-value change components, $m

- pv_explicit: +161.387571
- pv_terminal: +707.397613
- pv_nol: +0.000000
- opening_excess: +0.000000
- equity: +868.785184


## Student's post-run interpretation and reported partner exchange

### Prediction reconciliation

Student's answer:

> Lower SG&A also lowers cash operating expenses, so the required reserve, three months of those expenses, shrinks, and the smaller reserve investment releases extra cash to FCFE on top of the $92M after-tax saving. The extra should be roughly a quarter of the year-over-year drop in cash SG&A, or about $9M in FY2031.

Precision: the changed case's reserve is lower **relative to base**; SG&A dollars and the reserve need not fall in absolute terms. The FY2031 reduction in annual reserve investment is $8.906m. After-tax operating-profit improvement is $91.716m, producing $100.621m additional FCFE and $293.993m total. This reconciles the original $285m point prediction while leaving the original locked record intact.

### Driver ranking over the chosen ranges

Student's answer:

> SG&A is the larger driver, moving value about ±$1.60 versus a predicted ±$0.30–0.50 for growth. The ranking could flip if the growth range were much wider (for example, agentic AI pushing growth back to 20%), if the SG&A range were narrower, or if margins were higher, since each dollar of growth would then earn more profit.

Numerical correction: actual growth-case value changes are **−$0.202 and +$0.215/share**, not ±$0.30–0.50. SG&A changes value by approximately ±$1.618. SG&A has the larger observed span for **all three outputs**: profit $238.223m versus $44.368m, FCFE $201.242m versus $10.514m, and value/share $3.235 versus $0.416. These comparisons hold **over the student's tested ranges**. The student's 20% example is hypothetical, not a new selected or executed scenario. A changed ranking is possible, not established without testing. Changing the base margin would change the underlying model as well as the sensitivity comparison.

### Research priority and valuation conclusion

Student's answer:

> SG&A ranks first on both impact and uncertainty, because it moves value most and its recent improvement came from a one-time restructuring, so I'd track sales and marketing growth against gross profit over the next few quarters and any Investor Day margin targets. My valuation conclusion doesn't change, since even the low-SG&A case (about $7.30) sits well below $12.68, and my research priority stays on SG&A rather than growth.

Qualifications: impact is measured over these ranges; uncertainty is the student's assessment, not a measured probability. The evidence reviewed does not establish that all of the recent improvement came from a one-time restructuring. A precise research question is whether efficiency improvements persist after restructuring and lower SBC. Track G&A as well as sales/marketing because the modeled numerator includes both. The September 22 investor-day targets have already been reviewed in Lab 10; the next evidence should test progress against them, distinguishing non-GAAP targets from GAAP modeled margins. The $12.68 comparator is the **September 24, 2026, 3:01 p.m. EDT snapshot**, not a September 29 quote. This remains a comparison to an annual-base model, not proof of current overvaluation.

### Why sensitivity is not probability

Student's answer:

> The cases are what-if ranges chosen to show how much each input moves value, not outcomes weighted by how likely they are, so an endpoint like 53% says nothing about its odds of happening.

### Reported partner question and student's response

Partner question reported by the student:

> Your low-SG&A case still lands near $7.30, so what would have to be true for UiPath to be worth $12.68?

Student's response:

> SG&A would have to fall well below 53% of gross profit while growth also stayed near 12%, a combination that neither my filings evidence nor my ranges support, so I'd treat the market price as pricing in an outcome I can't yet justify.

AI qualification: no reverse valuation or combined-input scenario has been run. Therefore this response is a proposed explanation, **not a demonstrated necessary combination**. The tested cases alone do not show what must be true to reach $12.68; other changes in margins, growth, valuation inputs and timing could affect value. A supported conclusion is that none of the individual tested cases reaches the dated comparator under the unchanged assumptions. No new joint scenario was run after this response.


## Reciprocal partner evidence check — Apple

The student reports checking the partner's lower/base/higher revenue-growth and gross-margin cases, recomputing differences and confirming their units. Specific example provided:

> Apple's FY2030 gross margin input changed from 49% to 46%, and its value per share changed from about $186 to about $171 (operating profit from about $189B to about $173B).

| Apple downside check | Base | Changed | Recomputed difference |
| --- | ---: | ---: | ---: |
| FY2030 gross margin | 49% | 46% | −3 percentage points |
| Operating profit | about $189bn | about $173bn | about −$16bn |
| Value/share | about $186 | about $171 | about −$15/share |

The student's reported rule of thumb was $5.6bn operating profit and $5/share per gross-margin point, with most of the value effect through terminal value. The rounded supplied numbers imply **about $5.3bn of operating profit and $5/share per point**, averaged over this 3-point change. They do not establish an exact $5.6bn local marginal effect. The partner model has not been independently opened by AI, so the terminal attribution remains student-reported rather than verified from an Apple valuation decomposition.

The student explains the asymmetry: the downside range is 3 points below base while the upside is 2 points above base, chosen to reflect perceived risks to Google-related payments and App Store fees. This is the reported scenario rationale, not independent legal research. Unequal ranges can generate unequal output moves even in a linear model; the absent numerical upside result prevents measuring any additional nonlinearity here. The ranges are not event probabilities.

**Cross-company mechanism comparison, based on the reported models:** Apple's selected gross-margin change operates through gross profit, whereas UiPath's SG&A/gross-profit change leaves gross profit fixed and changes the expenses below it. Both then affect profit, cash flow and potentially terminal value. Apple's size alone does not explain a driver ranking, and raw dollar spans between unlike companies should not be ranked. The supplied Apple case does not establish whether gross margin outranks Apple's revenue-growth driver.

## Completion and submission

Recorded: two operating-driver ranges and reasons, visible lower/base/higher results, accounting/input-isolation checks, passing restored base, a timestamped student-reported pre-run save, an unchanged prediction with actual-result reconciliation, the student's range-aware driver ranking and research priority, a reported partner question and response, and a numerical check performed on the partner's Apple analysis.

Submit this Markdown and `uipath_sensitivity.py`; keep the unchanged Lab 10 `uipath_proforma.py` alongside the runner. The separate `lab11-locked-prediction.md` is recommended supporting evidence of the original record. Full audit/output files are optional because this document includes visible results. No GitHub upload has been performed by AI. Questions and checks are recorded as the student reported them; no partner replies or unobserved partner-model results are fabricated.
