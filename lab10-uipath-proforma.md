# Lab 10 — UiPath (PATH): five-year three-statement base case

**Status: lab responses recorded and engine tested; ready for GitHub upload, with the limitations below disclosed.** Prepared September 24, 2026. This is a teaching model with explicit simplifications, not a completed investment recommendation.

**Question:** What are five years of UiPath's financial statements worth, built from assumptions I can defend?

Run `python3 uipath_proforma.py --test`. The companion `lab10-model-results.txt` shows the statements, checks and valuation. Amounts are USD millions except share prices; shares are millions. Fiscal years end January 31.

## Result and dating convention

The selected assumptions produce **$5.69 per share**, or **$3,055.276 million of equity value**, on **537.037 million shares**. This is an annual-base value discounted to **January 31, 2026**, using information available through September 24, including FY2027 guidance and acquisition disclosures. It is not a valuation that was available in January, nor a fully rebased September estimate.

A market quote retrieved September 24 was **$12.68 at 3:01 p.m. EDT**, with the market open: [StockAnalysis PATH quote](https://stockanalysis.com/stocks/path/). The quote is a timestamped snapshot, not the day's closing price. The preceding September 23 close was $13.04. The company's quote page did not expose a machine-readable quote, so a dated provider quote was used.

At the model's common denominator of 537.037 million shares, $12.68 implies **$6,809.629 million**. This is a normalized comparison, **not the company's actual current market capitalization**: actual outstanding shares have changed since January. The quote itself is per share; no historical EPS share count is substituted for the model denominator. The large model/market difference is a question about assumptions and timing, not a buy/sell conclusion.

**Student's comparison and question are recorded in the checkout below.** The selected limited-NOL scenario remains $5.69 per share.

## Reopen and rerun

The Lab 09 ABG engine was rerun September 24, 2026 and reproduced $291.75 per share. Its balance, cash reconciliation, minimum-cash and revolver checks passed. The UiPath engine is saved separately and does not reuse ABG inventory or floor-plan economics.

## Company-specific line and opening partner discussion

Student's explanation, lightly edited for spelling:

> UiPath receives money for subscriptions upfront, records deferred revenue, and recognizes revenue over the contract term. Deferred revenue should stay in operating NWC and be projected from ARR/billings or, at least, as a percentage of revenue.

Precision: licenses may be recognized at a point in time; SaaS and maintenance/support are recognized over their service periods. ARR is not billings or revenue. A **rise** in deferred revenue releases cash through lower operating NWC, other things equal; its balance alone does not guarantee positive total working-capital cash flow. The model uses the student's selected **43% of revenue** and counts its change once.

Opening partner question reported by the student: **“If rising deferred revenue boosts FCF, does that boost terminal value?”**

Student-approved answer (AI refined wording):

> I would include the deferred-revenue cash benefit supported by sustainable growth and a stable deferred-revenue-to-revenue ratio, excluding temporary billing effects. With an exit multiple, I would avoid adding a separate benefit already reflected in the terminal valuation.

This opening discussion does not substitute for the later numerical-assumption partner review.

## History collection

Opened annual filings: [FY2026](https://ir.uipath.com/financials/sec-filings/content/0001734722-26-000012/path-20260131.htm), [FY2025](https://www.sec.gov/Archives/edgar/data/1734722/000173472225000007/path-20250131.htm), and [FY2024](https://www.sec.gov/Archives/edgar/data/1734722/000173472224000011/path-20240131.htm). Fiscal years end January 31. Figures below are USD millions, converted from the filings' thousands by dividing by 1,000. The required history grid is sourced below; the forecast assumptions follow in a separate table.

| History item | FY2024 | FY2025 | FY2026 | Filing and locator |
| --- | ---: | ---: | ---: | --- |
| Revenue | 1,308.072 | 1,429.664 | 1,610.572 | FY2026 10-K, p. 79, Consolidated Statements of Operations, Total revenue |
| Gross profit | 1,112.148 | 1,182.722 | 1,339.588 | Same statement, Gross profit |
| Sales and marketing | 713.130 | 738.493 | 683.329 | Same statement, Sales and marketing |
| General and administrative | 231.637 | 226.116 | 214.291 | Same statement, General and administrative |
| Research and development | 332.101 | 380.682 | 385.208 | Same statement, Research and development |
| Net income (loss) | -89.883 | -73.694 | 282.330 | Same statement, Net income (loss) |
| PP&E, net | 23.982 | 32.740 | 46.014 | FY2025 10-K p. 78 for FY2024; FY2026 10-K p. 78 for FY2025–26 |

UiPath separates sales/marketing and G&A; the lab's SG&A measure will sum those two lines while preserving R&D separately. Depreciation is already embedded in functional costs, so blindly copying ABG's separate depreciation deduction would risk double counting.

Student independently confirmed both requested source checks: FY2026 revenue of 1,610,572 thousand (p. 79) and deferred revenue of 603,737 thousand current plus 103,568 thousand non-current, totaling 707,305 thousand (p. 78). The additional history and ratios below complete the initial research pass; limitations are explicitly noted.

## Additional history and definitions

Amounts below are USD millions. Source keys refer to the linked FY2026 (F26), FY2025 (F25), and FY2024 (F24) filings above. F26 p. 79 contains comparative income-statement data for all three years; F24 p. 80 and F25 p. 79 corroborate prior annual income figures. F24 p. 79 and F25 p. 78 provide prior balance-sheet comparisons.

| Item | FY2024 | FY2025 | FY2026 | Source/definition |
| --- | ---: | ---: | ---: | --- |
| SG&A, derived | 944.767 | 964.609 | 897.620 | Sales and marketing + general and administrative, F26 p. 79; R&D excluded |
| Shareholders' equity | 2,016.114 | 1,845.762 | 2,082.587 | F24 p. 79; F25 p. 78; F26 p. 78 |
| Current deferred revenue | 486.805 | 569.464 | 603.737 | Same balance sheets |
| Non-current deferred revenue | 161.027 | 135.843 | 103.568 | Same balance sheets |
| Total deferred revenue, derived | 647.832 | 705.307 | 707.305 | Sum of both maturities |
| Inventory | Not separately reported | Not separately reported | Not separately reported | No inventory line in the three balance sheets; not a reported numeric zero |
| Depreciation only | 11.100 | 8.100 | 5.800 | F26 Note 9, PP&E, p. 101; rounded company disclosure |
| Depreciation and amortization | 22.597 | 17.232 | 16.969 | F26 cash-flow statement, p. 82; not interchangeable with PP&E depreciation |
| Cash purchases of PP&E | 7.342 | 14.923 | 19.048 | F26 cash-flow statement, pp. 82–83; spending magnitude |
| Pretax income (loss) | -75.815 | -78.100 | 100.628 | F26 p. 79 |
| Income-tax provision (benefit) | 14.068 | -4.406 | -181.702 | F26 p. 79; negative means tax benefit |
| Operating cash flow | 299.082 | 320.565 | 371.208 | F26 p. 82 |
| Deferred-revenue cash-flow adjustment | 137.471 | 68.348 | -22.431 | F26 p. 82, Changes in operating assets and liabilities |
| Stock-based compensation expense | 371.955 | 358.151 | 290.676 | F26 p. 82, noncash reconciliation |

## Three-year ratios

| Ratio | FY2024 | FY2025 | FY2026 |
| --- | ---: | ---: | ---: |
| Gross margin (%) | 85.02 | 82.73 | 83.17 |
| SG&A / gross profit (%) | 84.95 | 81.56 | 67.01 |
| R&D / revenue (%) | 25.39 | 26.63 | 23.92 |
| Reported revenue growth (%) | 23.57 | 9.30 | 12.65 |
| Depreciation / year-end net PP&E (%) | 46.28 | 24.74 | 12.60 |
| Capex / revenue (%) | 0.56 | 1.04 | 1.18 |
| Reported effective tax rate (%) | -18.56 | 5.64 | -180.57 |
| Total deferred revenue / revenue (%) | 49.53 | 49.33 | 43.92 |
| Inventory days | N/A | N/A | N/A |
| Organic / same-store revenue growth | Not identified | Not identified | Not identified |

Ratios use the history immediately above. Depreciation divided by **year-end net PP&E** follows the video's historical calibration convention, not an average-asset rate; applying the selected rate to future opening PP&E is a separate forecast choice. Rounded depreciation disclosures limit precision. Inventory days is not meaningful without a reported inventory balance; do not import ABG's dealer ratio.

Reported growth uses prior revenue: FY2023 $1,058.581 million (F24 p. 80), then the preceding year in the history table. Searches for organic growth in all three filings did not identify a company-reported organic rate. UiPath's MD&A discusses revenue sources and customer expansion, but these are not a separately reconciled organic/same-store growth measure. Do not rename reported growth or ARR growth as organic growth. Acquisition/FX-adjusted growth remains unresolved without a reconciliation.

### Capex filing versus provider

[StockAnalysis annual cash-flow statement](https://stockanalysis.com/stocks/path/financials/cash-flow-statement/), Capital Expenditures row, accessed September 24, 2026. Use fiscal-year columns, not TTM. USD millions:

| Source | FY2024 | FY2025 | FY2026 |
| --- | ---: | ---: | ---: |
| Filing: purchases of PP&E, cash-outflow sign | -7.342 | -14.923 | -19.048 |
| Provider: Capital Expenditures | -7.34 | -14.92 | -19.05 |

These match to provider rounding. The model should use the positive spending magnitude as an input and subtract it once. Acquisitions and securities purchases are separate from PP&E capex. Provider D&A classification differs from the filing; use filing depreciation for the PP&E schedule rather than importing the provider's combined measure.

### Modeling issues identified before assumptions

1. FY2026 total deferred revenue increased only $1.998 million, while the cash-flow statement's deferred-revenue adjustment was **negative $22.431 million**. Note 3's deferred-revenue rollforward identifies $3.332 million of acquisition additions and $4.535 million of translation adjustments. Removing those from the balance change gives -$5.869 million, still $16.562 million above the cash-flow adjustment; that residual remains unresolved. Historical cash-flow benefit cannot be inferred from the raw balance difference alone. Forecasting its cash effect from balance changes requires an explicit assumption about those other effects.
2. Reported effective tax rates are distorted by losses and tax benefits and should not be mechanically projected. A normalized forecast tax rate needs a judgment and supporting reason.
3. R&D is material and must remain modeled. GAAP functional expenses already contain depreciation/amortization and stock compensation: avoid a second expense deduction. Any SBC cash-flow add-back needs consistent equity and per-share treatment; it is not costless financing.
4. Deferred-revenue/revenue declined from roughly 49.5% to 43.9%. A constant ratio going forward is a judgment, not an observed constant historical relationship.



## Student-selected assumptions

Five-number sequences run **FY2027 → FY2031**. Reasons below retain the student's reasoning, with spelling and grammar edited. A declining expense ratio does not imply declining dollar spending. All forecast ratios use GAAP costs unless explicitly indicated otherwise.

| Value | Label | Student's reason |
| --- | --- | --- |
| Revenue growth: 11.2%, 10%, 9%, 8%, 7% | FY2027 guidance-derived, rounded; subsequent years judgment | FY2027 is anchored to the guidance midpoint. Growth relies heavily on existing-customer expansion; nearly flat customer count, 12% ARR growth and 109% retention support my maturity judgment of fading growth. These metrics do not mechanically prove the annual fade. |
| Gross margin: 82%, 81%, 80.5%, 80%, 80% | Judgment | Revenue shifts away from licenses toward subscription/SaaS services; I assume margins stabilize around 80% as that shift matures. Subscription services also include maintenance/support, so they are not entirely SaaS. |
| SG&A / gross profit: 65%, 63.5%, 62%, 60.5%, 59% | Judgment | Expansion-led growth allows spending to grow more slowly than gross profit. SG&A includes sales/marketing and G&A; R&D remains separate. |
| R&D / revenue: 24%, 23.5%, 23%, 22.5%, 22% | Judgment | FY2026 R&D grew about 1% versus revenue growth of about 13%. I allow continued efficiency, but competition in agentic AI requires sustained product investment. |
| Total deferred revenue / revenue: 43% each year | Judgment | I expect billing practices and contract lengths to remain broadly unchanged. I assume future stabilization; the historical ratio had declined. |
| Other operating working-capital balances: FY2026 percentages of revenue | Judgment, calibrated to history | FY2026 reflects the current billing mix better than the earlier license-heavy baseline. This applies only to identified operating balances, not all balance-sheet accounts. |
| Capex / revenue: 1.2%, 1.1%, 1%, 1%, 1% | Judgment | Reliance on third-party cloud services limits investment in owned infrastructure; office improvements drive much of physical capital spending. Service costs are expensed as consumed, not all when a future commitment is signed. |
| Depreciation: 18% of opening net PP&E | Judgment | I expect the longer-lived leasehold-improvement mix to persist, but use a rate above FY2026's low observed ratio to allow for recently constructed assets entering service. Historical timing supports an interpretation, not proof of the exact 18% rate. |
| SBC / revenue: 16%, 14.5%, 13%, 12%, 11% | Judgment | SBC dollars are already falling. The final 11% corrects my initial 1% typo. |
| Normalized tax expense: 23% of positive pretax income | Judgment | Approximately the U.S. federal rate plus state taxes and foreign mix; foreign revenue is 54%. Revenue geography does not itself determine taxable-income geography. |
| Cash-tax relief only as usable NOLs offset income | Judgment / policy | NOLs reduce cash taxes as taxable income uses them up; the whole deferred-tax asset is not spendable upfront. The student subsequently retained the limited-NOL scenario; see the checkout and its qualification. |
| Cash reserve: three months of cash-cost proxy | Judgment | Seasonal business activity calls for a buffer. The filing confirms second-half bookings seasonality; the Q2 cash-flow observation alone does not prove Q4 collections concentration. |
| Cash cost equal to SBC for dilution-offset repurchases; constant shares | Judgment | Counts SBC's economic cost once and reflects repurchase activity. Corrected FY2026 cash buybacks were $329.101m, above $290.676m SBC; $59.061m employee tax withholdings were separate. Equal dollars do not ensure exact share neutrality. |
| Cost of equity: 11% | Judgment | My illustrative CAPM inputs are about 4% risk-free, 1.3 beta and 5% equity premium. Their arithmetic is 10.5%; 11% is a rounded-up choice, not the exact CAPM result. These are my estimates, not verified current market inputs. |
| Perpetual growth: 3% | Judgment | Below FY2031's 7%, consistent with a mature company eventually growing within long-run nominal economic bounds. No company can permanently outgrow the economy. |

FY2027 revenue guidance is $1,789–$1,794m; its midpoint implies 11.2338% growth over $1,610.572m FY2026 revenue. The student's rounded 11.2% gives $1,790.956m. Source: [Q2 FY2027 results, September 3, 2026](https://ir.uipath.com/news/detail/461/uipath-reports-second-quarter-fiscal-2027-financial-results).

## Opening balance sheet and implementation assumptions

Opening history comes from FY2026 Form 10-K p. 78, with accrual decomposition in Note 9 p. 102 and repurchase payable in the cash-flow supplemental disclosure p. 82. All opening code fields are mapped below. Assets sum to $3,179.200m; liabilities $1,096.613m; equity $2,082.587m.

| Value | Label | Source, transformation or reason |
| --- | --- | --- |
| Cash 871.157; marketable securities 818.319; restricted cash 0.438 | History | Securities = 601.329 current + 216.990 noncurrent. Restricted cash is excluded from excess liquidity. |
| Receivables 488.265; contract assets 94.386 | History | Contract assets = 92.440 current + 1.946 noncurrent. |
| Deferred acquisition costs 238.447; prepaids 105.577 | History | Deferred costs = 84.739 current + 153.708 noncurrent. |
| PP&E 46.014; ROU assets 64.472; intangibles 19.989; goodwill 125.310 | History | Direct balance-sheet lines. |
| DTA 233.401; other noncurrent assets 73.425 | History | DTA is not unrestricted cash. Other assets include investments and capitalized costs, so they are not scaled mechanically as operating NWC. |
| Payables 10.161; compensation 121.029; deferred revenue 707.305 | History | Deferred revenue = 603.737 current + 103.568 noncurrent. |
| Lease liabilities 81.246 | History | 70.940 noncurrent + 10.306 current included within reported accrued liabilities. |
| Tax payable 14.784; acquisition payable 9.532; repurchase payable 10.015 | History | Acquisition payable = 8.000 deferred + 1.532 contingent. Separated from operating accruals. |
| Equity-related withholdings 7.977; remaining operating accruals 117.882 | History-derived classification | Withholdings = 4.763 + 3.214. Accruals = 170.496 − 10.306 − 14.784 − 9.532 − 10.015 − 7.977. |
| Other noncurrent liabilities 16.682; equity 2,082.587 | History | Direct balance-sheet lines. |
| Shares 537.037m | History + judgment to keep constant | 472.346m Class A + 64.691m Class B outstanding. This is neither annual diluted EPS shares nor today's outstanding shares. |
| Opening federal NOL pool 662.4 | History | Note 13 p. 113; separate from the DTA balance and from foreign/state pools. |
| Aggregate NOL use capped at 29m/year and 80% of positive modeled pretax income, benefit at 21% | **Judgment—AI proxy, retained by student** | A limited-benefit scenario, not a reconstruction of tax law by jurisdiction/vintage. The filing's $29m Section 382 limit applies to older losses, not the whole pool; the proxy also uses consolidated pretax income rather than a U.S. taxable-income forecast. Do not describe this as an established legal limit or guaranteed conservatism. |
| Other DTA held unchanged; no incremental valuation credit | Judgment—AI simplification | Avoids valuing unsupported tax-asset realization. Only modeled NOL use reduces DTA and enters cash flow; no double counting. No tax benefit on projected losses is booked. |
| Operating NWC = receivables + contract assets + net deferred contract costs + prepaids − payables − operating accruals − compensation − deferred revenue | Implementation of student policy | Forecast net balance changes once. Do not separately add back commission amortization when using changes in NET deferred contract costs. |
| Zero forecast FX, OCI, working-capital acquisition/reclassification adjustments after the disclosed aggregate acquisition entry | Judgment—AI simplification | Forecast changes in modeled operating balances are assumed cash-related. The historical deferred-revenue discrepancy remains disclosed; it is not filled with an invented explanation. |
| Stable securities, restricted cash, ROU assets/lease liabilities, other noncurrent assets/liabilities and remaining tax/withholding balances | Judgment—AI simplification | Keeps nonoperating and lease balances out of revenue-ratio NWC. Stable lease balances assume renewals replace runoff and cash rent equals embedded lease expense. No additional value for unmodeled noncurrent investments is added. |
| Zero investment income/nonoperating gains; no new borrowing or further acquisitions | Judgment—AI base-case convention | Existing excess liquidity is valued separately, so its future interest is not also capitalized. The one disclosed WorkFusion transaction is included. Leases stay operating; there is no separate debt deduction for lease liabilities while rent is expensed. |
| Three-month reserve = 25% × (COGS + SG&A + R&D − depreciation − acquired-intangible amortization − SBC) | Implementation of student cash policy | A cash-cost proxy, not a forecast of intra-year cash troughs. Reserve growth reduces cash available for valuation. Opening reserve is $311.542m. |
| Opening excess cash/securities 1,377.934 | Derived | 871.157 + 818.319 − 311.542. Added once; forecast accumulated cash is not added again. |
| Terminal ratios fixed at FY2031 levels, growth 3% | Judgment—implementation of student long-run case | Continue the actual PP&E, intangible, NWC and reserve schedules as growth slows; finite NOL relief ends when used. Normalized tax cash flows are permanent, NOL shields are not. |

### WorkFusion and acquisition accounting

Source: [Q2 FY2027 Form 10-Q](https://ir.uipath.com/financials/sec-filings/content/0001734722-26-000050/path-20260731.htm), filed September 8, 2026, Note 6, Note 7 and cash-flow statement.

| Value | Label | Source, transformation or reason |
| --- | --- | --- |
| WorkFusion net cash cost 149.403 in FY2027 | History | Cash-flow statement; February 5 acquisition occurred after the annual opening date. |
| Intangibles 92.400; DTA 30.436; goodwill 58.157; contingent payable 29.567 | History | Disclosed purchase-price allocation and acquisition-date contingent consideration. |
| Other acquired net liabilities excluding cash 2.023 | History-derived | 189.527 consideration − 29.567 contingent = 159.960 gross cash. Less 149.403 net cash implies 10.557 acquired cash. Disclosed other net assets 8.534 − cash 10.557 = −2.023. |
| Acquired net liabilities held constant | Judgment—AI simplification | Aggregate disclosure does not permit a detailed operating-working-capital split; do not invent one. |
| Settle WorkFusion contingent payable in FY2028 at acquisition-date value | Judgment—AI simplification | Counts the obligation once. Actual payment is performance-dependent; July fair value had increased to $30.392m. This is a timing/value assumption, not company guidance. |
| Settle opening acquisition payable 9.532 and repurchase payable 10.015 in FY2027 | Judgment—AI timing assumption | Keeps preexisting obligations out of operating growth funding; settlement reduces cash and liabilities, not equity a second time. |
| Intangible amortization 22.425, 22.896, 18.320, 17.120, 15.953 | Guidance-derived schedule, FY2027 includes history | July Note 7: FY2027 = rounded H1 actual 10.6 + remaining-year estimate 11.825; subsequent years use the disclosed schedule. No forecast FX adjustment; remaining net intangibles amortize after FY2031. |

The purchase entry balances independently: 92.400 + 30.436 + 58.157 − 29.567 − 2.023 = 149.403 net cash paid. Acquisition DTA does not increase the modeled federal NOL pool without jurisdictional support. GAAP expense ratios already contain D&A and SBC: none is deducted a second time from earnings.


## Validation and limits

The script prints five years of income statements, balance sheets and cash flows. Cash is computed last from opening cash plus operating, investing and financing cash flows. It is never typed to force a balance.

All annual checks are zero at full-precision tolerance (1e-7 million dollars): balance sheet, cash flow, equity, PP&E, tax bridge, DTA, deferred-revenue cash effect, net income, NWC change, CFO/CFI/CFF bridges, reserve change, FCFE, NOL and intangible rollforwards. Minimum-cash shortfall is zero in every year. No borrowing or revolver is needed in the base case. This tests annual endpoints, not liquidity every day within a year.

Executed refusal tests independently changed FY2029 cash, equity, PP&E, deferred revenue, CFO, DTA, FCFE, reserve investment, NOLs and intangibles by $1m: all were rejected before valuation. Terminal growth equal to the cost of equity and an unaffordable cash floor were also rejected. An independent cash-tax formulation reproduces all five FCFE figures, confirming that the SBC add-back and offsetting repurchase cash cost cancel once.

### Negative cash flow and course convention

After acquisition spending, dilution-offset repurchases, settlement of opening obligations and reserve investment, FY2027 FCFE is **negative $137.753m**; FY2028–31 FCFE is **$46.614m, $106.997m, $147.297m, $193.372m**. These are cash flows available to continuing shareholders under the constant-share convention, not the company's reported adjusted FCF measure.

The economic valuation retains the first-year funding cost and gives **$5.69/share**. The lab's literal positive-only explicit-cash-flow convention gives **$5.92/share**, displayed separately; omitting negative cash flows removes a real funding cost. The main value is $5.69, with this distinction disclosed rather than hidden. A negative sustainable cash-flow base cannot support the positive going-concern terminal estimate used here; the model refuses such a terminal case.

### Tax qualification

The $29m cap is a **scenario parameter**, not a verified company-wide legal limit. UiPath has multiple NOL vintages and jurisdictions; the public figures do not determine a precise five-year utilization schedule. The model does not recreate a tax return or automatically monetize the whole DTA. The student retained the limited-NOL scenario for the reason recorded below; the cap does not guarantee that benefits cannot be overstated. The no-modeled-NOL-relief case is $5.60/share, only about $0.09 lower. No separate DTA balance is added to equity value.

### Deferred-revenue reconciliation qualification

The historical balance change and reported cash-flow adjustment do not reconcile fully using the disclosed acquisition and FX items: the remaining $16.562m is unresolved. Both filing values are retained. Contract-asset/liability netting is disclosed, but no specific amount explains the residual; it would be wrong to invent that explanation. The forecast explicitly assumes no such noncash/reclassification effect within its revenue-scaled operating balances.

For scale only, a one-year $16.562m additional cash outflow discounted at 11% would reduce value by approximately **$0.028/share**, holding everything else fixed. This is an illustrative sensitivity, not a proven maximum error or an actual modeled expense. A recurring or larger discrepancy would require a different sensitivity.

### Operating and valuation sensitivities

All scenarios rerun the statements and their checks before valuation; market price is not used to calibrate the base case.

| Scenario | Value per share |
| --- | ---: |
| Selected base case | $5.69 |
| No modeled NOL relief | $5.60 |
| Cost of equity 10% | $6.24 |
| Cost of equity 12% | $5.26 |
| Terminal growth 2% | $5.43 |
| Gross margin 2 percentage points lower each year | $5.37 |
| SG&A / gross profit stays at 65% | $4.07 |
| R&D stays at 24% of revenue | $5.02 |
| Deferred revenue stays at 40% of revenue | $5.54 |

The SG&A improvement is a meaningful assumption to attack: removing it reduces value by about $1.62/share. Merely making the statements balance does not validate that economic assumption.

## Investor-day cross-check

Reviewed the financial section of [UiPath Investor Day, September 22, 2026](https://ir.uipath.com/events-presentations/detail/20260922-uipath-investor-day-2026), especially slides 95, 102–104, 109–118. [Presentation PDF](https://d1io3yog0oux5.cloudfront.net/_5c0a0bb66ca56305a8399b7302c1035e/uipath/db/1167/25108/presentation/UiPath_Investor-Day_2026.pdf).

Management retained FY2027 revenue guidance of $1.789–$1.794bn. Its long-term profile targets non-GAAP gross margin of 80%+, non-GAAP operating margin of 30%+, and SBC at 8–10% of revenue; these are targets without a guaranteed achievement date. Reported first-half FY2027 SBC was about 12% of revenue, below the student's 16% full-year assumption.

The student's FY2031 **GAAP** operating margin is **10.8%**. Adding back modeled SBC of 11% and acquired-intangible amortization of about 0.64% yields approximately **22.4%**, before other non-GAAP adjustments. This is an illustrative partial reconciliation, not company-defined non-GAAP guidance. It shows that the student's case remains below management's long-term aspiration. The student subsequently retained the selected case and framed the market gap as a question about stronger growth or profitability; AI has not changed the assumptions to match management targets.

## Organic growth and transfer

AI explanation to review: organic growth measures expansion in the existing business while excluding specified acquisition/disposal effects and sometimes currency effects, depending on the company's definition. No separately reconciled UiPath organic/same-store series was identified in the three annual filings reviewed; neither reported growth nor ARR growth should be renamed organic growth. Acquisitions contribute to the scope of reported revenue.

The course's ABG 1.8% assumption focuses on growth of the existing store base rather than automatically repeating the 4.7% reported growth rate that can include additions to the business. The student's own explanation is now recorded in the reflection below.

## Student checkout — recorded answers

### Model judgments

Student's answer:

> I'd keep the limited-NOL case at $5.69, because releasing the valuation allowance means the company judged its U.S. NOLs more likely than not to be usable, and capping the relief keeps the benefit from being overstated; it is only $0.09 above the no-relief case. Holding noncore balances stable and simplifying the timing of acquisition payments is reasonable for a teaching model, because deals the size of Peak ($40.1M) are small next to about $1.4B of cash and don't change the operating forecast.

AI qualification: the allowance release supports management's judgment about realization of U.S. deferred tax assets, not proof of this model's specific annual NOL usage. The scenario cap limits relief relative to uncapped usage but does not guarantee no overstatement. The acquisition timing assumption concerns WorkFusion as well as Peak: WorkFusion's $149.403m net initial cash outflow and $29.567m acquisition-date contingent payable are explicitly modeled. It would be inaccurate to justify all acquisition simplifications solely with the smaller $40.1m Peak transaction. The student's revised rationale is recorded below; the assumed early settlement is distinguished from a confirmed contractual payment date.

The $1.4bn comparison refers approximately to later cash plus marketable securities, not unrestricted cash alone or January opening liquidity. Acquisitions can affect operations as well as cash. The forecast's consolidated revenue and expense ratios incorporate assumed operations without separately attributing acquisition revenue; that is a simplification, not proof of no operating effect.

### Market comparison and question

Student's answer:

> At the model's 537.037M-share basis, my $5.69 implies about $3.06B of equity value, versus about $6.81B at the $12.68 price on September 24 at 3:01 p.m. EDT, roughly 2.2x my estimate. Some of that gap may simply reflect the timing mismatch, since my base uses FY2026 annual data ended January 31 while the price reflects news through Q2 FY27, such as ARR re-accelerating to 12% and reaffirmed guidance. So what evidence of faster growth, or of profitability beyond my 59% SG&A and 80% gross margin paths, could explain why the market prices UiPath at more than twice my value?

AI precision: 59% means SG&A **as a share of gross profit**, not revenue. The model already uses FY2027 guidance and later acquisition evidence; timing is a limitation, not an established explanation of the price gap. No quantitative attribution of the difference to timing has been made.

Condensed one-sentence version (AI edit of the student's answer, not a new recommendation):

> On the common 537.037-million-share basis, my $5.69 annual-base estimate implies about $3.06bn versus $6.81bn at the September 24, 2026, 3:01 p.m. EDT price of $12.68; recognizing that the model has not been rebased from its January opening date, what evidence of faster growth or profitability beyond my 59% SG&A/gross-profit and 80% gross-margin assumptions could explain the difference?

### Partner's numerical attack and student's defense

The student reports that the partner actually asked the same numerical question suggested in the chat. Recorded wording (reconstructed from that confirmation, not a verbatim transcript):

> Why let SG&A fall to 59% of gross profit when keeping it at 65% cuts modeled value to $4.07?

Student's two-sentence answer:

> I let SG&A fall to 59% of gross profit because 85% of FY26 growth came from existing customers, who are cheaper to sell to, and because stock comp inside SG&A is shrinking. However, holding the ratio at 65% cuts value to $4.07, so the base case depends heavily on this assumption, and I'd present both cases rather than defend 59% as certain.

Qualification: the filing's existing-customer contribution supports an expansion-led rationale, but lower marginal selling cost is the student's economic inference, not a measured customer-acquisition-cost comparison. Continued SBC reductions are also a forecast judgment. A failure condition is that expansion requires enough additional selling expense to prevent the expected ratio improvement.

**Student's specific attack on the partner's model — Tesla:**

> Partner company Tesla, assumption of 20%+ annual revenue growth at software-like operating margins of 30% or more driven by robotaxi and FSD, because that revenue depends on city-by-city regulatory approval and safety records that haven't been proven at scale, so it belongs in a probability-weighted upside scenario.

This records the student's reported critique of the partner's assumptions, not an independently verified description of every jurisdiction's regulatory process or Tesla's current operations. The numerical challenge is specific: the student questions treating rapid growth and high margins from uncertain services as a base case rather than a probability-weighted upside case. No partner response to this critique was supplied; none is fabricated.

### Reflection and organic-growth explanation

Student's answer:

> I'd defend the gross-margin decline to 80% the longest, because it follows directly from the filings: near-zero-cost licenses are shrinking as a share of revenue while money-losing professional services grow. The number that surprised me most was the $181.7M tax benefit, which turned $100.6M of pretax income into $282.3M of net income. ABG's base case should use existing-store growth because total reported growth includes dealerships it bought, which cost cash and can't be counted on to repeat, while same-store growth shows real underlying demand.

AI qualification: the revenue-category and cost disclosures support the direction of the margin concern, but **80% does not follow mechanically** from history. It remains a judgment about future mix and costs. The tax arithmetic reconciles: $100.628m pretax income minus a negative $181.702m tax provision equals $282.330m net income. Same-store growth is a useful underlying-demand measure but can also include pricing and mix effects; it is not guaranteed to repeat either.

## Acquisition timing — student's final clarification

> Simplifying the timing is reasonable because WorkFusion's $149.4M cash payment and its contingent consideration all fall early in the forecast, so shifting them by a quarter barely changes present value, but the full cost still belongs in the model because it is real cash leaving shareholders and WorkFusion's revenue is already inside FY27 guidance.

AI precision: the initial payment is historical; early contingent settlement is a **model assumption**, not a verified payment date. The code includes the $149.403m net initial cash cost and the acquisition-date $29.567m contingent liability, assumed paid in FY2028. That contingent estimate is not a guaranteed final amount or the contractual maximum. The July disclosed fair value was $30.392m. Keeping consolidated FY2027 guidance while including acquisition cash costs is consistent; the filing does not separately identify the exact WorkFusion contribution assumed in that guidance.

For scale, shifting the two modeled payments later by one quarter at an 11% discount rate, holding amounts and everything else fixed, changes their combined present cost by about $4.08m, or $0.008/share. This illustrates the student's timing argument; it does not establish that actual timing or consideration can vary only that much.

## Submission

Upload **lab10-uipath-proforma.md** and **uipath_proforma.py** to the course GitHub repository. **lab10-model-results.txt** is optional supporting output. Open the uploaded Markdown and Python files and copy their GitHub links into the Lab 10 checkout location specified by the course.

No GitHub upload has been performed by AI. All known source/model limitations remain disclosed above, including the unresolved historical deferred-revenue cash-flow reconciliation and the aggregate tax proxy. The student elected to retain the limited-NOL scenario and supplied reasons for the teaching-model simplifications. Recorded student answers and reported partner feedback are distinguished from AI explanations. A 25/25 grade cannot be guaranteed.
