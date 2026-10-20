# Model method and limitations

Prepared October 19, 2026. October 19, 2026 valuation; timestamped morning market quotes. This is a review draft, not an assertion that the student has approved every implementation choice.

## Decision and scope

The investment committee has no PATH position. The student's updated Hold/Sell view is translated into **do not initiate**, not a sale or short recommendation. Monitoring horizon is 12-18 months, approximately four to six quarterly reports. The valuation uses five annual forecast periods plus terminal cash flow. Banks, insurers and REITs are excluded by the assignment's FCFF architecture; UiPath is an operating software company.

## Dates, periods and share basis

The final engine replaces the old January annual-base valuation. It starts with the July 31, 2026 reported balance sheet and LTM operating history (FY2026 + H1 FY2027 - H1 FY2026), then forecasts **five rolling 12-month periods ending October 19, 2027-2031**. These are not UiPath fiscal-year forecasts. The first 11.2% growth rate is an analyst assumption transferred from the lab; it is no longer described as a direct forecast of FY2027 guidance.

July balances are used as the latest reported proxy for the October opening position. The model does not assert that cash, working capital or liabilities were unchanged during the intervening 80 days; it makes that simplifying assumption. It does not charge the February WorkFusion cash purchase again. There is no false January discount date using September information. Reporting lag remains material, and the output shows a $100m cash reduction and 5% larger denominator stress. These are not bounds on all possible lag errors.

Shares are **521.155409m basic shares outstanding**, Class A plus Class B as of September 3, per the 10-Q cover. They are not historical weighted-average diluted EPS shares. Future shares stay fixed under an economic SBC cash-cost approximation. Existing and future awards are not modeled grant by grant; a 5% denominator stress measures sensitivity but is not an estimate of actual dilution. P/E consistently uses reported diluted EPS for both firms, a different denominator convention that is explicitly labeled.

## Statements and FCFF

Revenue follows each scenario's growth path. Gross profit is revenue times GAAP gross margin; SG&A is a percentage of gross profit, while R&D is a percentage of revenue. Forecast cost ratios include SBC and D&A. The model does not deduct those expenses a second time from EBIT.

Operating NWC includes receivables, contract assets, net deferred contract acquisition costs and prepaids, less trade payables, operating accruals, compensation and deferred revenue. Acquisition claims, income-tax payable, equity withholdings and lease liabilities are separated from operating accruals. Other operating balances scale with revenue; deferred revenue has its own scenario path. Net contract-cost changes already reflect amortization, so commission amortization is not added back a second time.

Net income is operating profit after a normalized 23% cash tax; no interest income or nonoperating gains are capitalized. CFO adds back D&A and SBC, and deducts NWC investment. CFI contains capex. CFF contains the SBC-offset cash payment and settlement of existing acquisition obligations. Cash is calculated from flows. Equity rolls forward from net income plus SBC less the offset payment. The balance sheet must balance without a cash plug.

**FCFF = EBIT - normalized cash taxes + D&A - capex - change in operating NWC - change in required operating cash.** SBC remains an economic expense in FCFF. The equivalent CFO bridge subtracts its add-back once. Acquisition-claim settlement is a financing/claim payment outside operating FCFF, deducted once in the equity bridge. The forecast statements still show the actual modeled cash settlement.

There is no funded debt in the selected reported balance sheet. WACC equals cost of equity under this capital structure. Operating leases remain operating: rent is included in costs, lease balances are held constant through renewal assumptions, and lease liabilities are not also deducted as funded debt. No preferred stock or minority claim is identified in the reported capitalization. Restricted cash and unsupported private-investment values are excluded from the cash addition.

## Discount rate and terminal value

WACC of 11% follows the lab's **assumed** 4.5% risk-free rate + 1.3 beta x 5% equity premium. These are classroom parameters, not verified October market estimates. The main cases hold WACC fixed so operating effects remain visible; a 9%-13% grid challenges it. A production investment decision would require dated capital-market inputs and a defensible beta estimate.

Terminal growth is 3%, tested at 2%-4%, and must be below WACC. Final operating ratios persist after year five. The engine continues PP&E, finite intangibles, NWC and operating reserve schedules for 200 transition years, then applies a Gordon tail after convergence. It does not perpetuate amortization of an asset that has run out. The long transition is a numerical implementation, not a detailed 205-year forecast. Terminal cash flows are discounted at the same WACC. About 79% of base enterprise value is terminal; this is a central risk.

## Enterprise-to-equity bridge

Reported cash plus securities is $1,405.025m. Required operating reserve is $326.832m, derived from one quarter of LTM cash operating-cost proxy. Excess liquidity is $1,078.193m. Restricted cash of $1.475m is excluded.

Equity = operating EV + $1,078.193m excess liquidity - $0 funded debt - $34.251m existing acquisition obligations. The acquisition claims are deducted at face value although the statement model settles them in year one: this conservatively forgoes a timing discount, and does not double deduct them in FCFF. Future accumulated cash is never added again. DTA is not added to cash or equity.

## Normalization and contamination catalog

| Item | Reported evidence | Treatment and unresolved risk |
| --- | --- | --- |
| FY2026 earnings | Revenue 1,610.572; GP 1,339.588; SG&A 897.620; R&D 385.208; EBIT 56.760; net income 282.330 ($m) | Reported net income is not recurring operating cash profit. Reconcile to operating lines before forecasting. |
| Tax benefit | FY2026 tax benefit 181.702; valuation-allowance effects documented in annual report | Replace forecast effective rate with 23%; do not repeat the benefit or add DTA as cash. |
| Restructuring | FY2026 expense 4.407 ($m), Note 10 | Illustrative normalized EBIT = 56.760 + 4.407 = 61.167; at 23% tax, normalized NOPAT = 47.099. This historical normalization is distinct from scenario forecasts. |
| SBC | GAAP functional costs contain SBC; LTM SBC derived from annual plus current H1 less prior H1 | Retain economic cost; cash add-back offset once. No claim that equal repurchase dollars ensure exact share neutrality. |
| Acquisitions | WorkFusion initial net cash 149.403 already paid by July | Start from post-acquisition balance sheet; do not repay it. Deduct remaining claims once. No new M&A assumed. |
| Deferred revenue | January balance and historical CFO adjustment did not reconcile fully in Lab 10 | Keep reported numbers; no invented explanation. Forecast assumes no further FX/acquisition reclassification. July seasonal balance anchors final ratio, not the old 43% year-end ratio. |
| Cash flow | H1 CFO 162.627, CFI -128.565, CFF -287.124, FX -9.644 ($m) | 871.595 opening cash including restricted cash reconciles to 608.889; subtract restricted 1.475 to obtain unrestricted cash 607.414. |
| Basis changes | Old models mixed annual EPS shares, outstanding shares and differing dates | Final basic share basis and common price date stated; old outputs are history, not current results. |

Sources and exact locators are in `source-register.md`. Base-year normalization is transparent; not every historical cash-flow adjustment has been independently resolved.

## Taxes, amortization and cash reserve

No NOL relief is valued because the lab's $29m aggregate cap was not an established company-wide limit. This removes an unsupported precision claim, but can understate value. The entire reported $230.087m DTA would equal about $0.44/share before discounting if realizable; that is an extreme arithmetic comparison, not a forecast of recoverability. Tax changes are tested separately.

Year-one amortization of 23.650 is twice the filing's remaining-half-year 11.825 estimate; later annual amounts borrow the filing schedule as a rolling-period approximation, always capped at remaining intangible book value. This is not an exact October-to-October fiscal schedule. Depreciation remains the lab's 18% of opening net PP&E assumption. Capex is modeled separately. Acquired-intangible runoff therefore cannot create a perpetual add-back.

Three months of cash operating costs is a policy assumption. The reserve grows with costs; its increase reduces FCFF. Annual liquidity checks do not prove intra-year liquidity. Cash reserve treatment should be challenged if seasonality, collections or infrastructure commitments change.

## What the scenarios do and do not establish

The student supplied the cannibalization, competitive-pressure, inference-cost and collection-risk thesis. The numerical paths are AI-assisted implementations; the student approved the SG&A paths on October 19. No probability is attached. ARR and retention triggers are monitoring evidence, not a mechanical mapping to revenue growth.

The downside lowers growth, margin and advance collections together while retaining higher operating costs. It reduces value but does not change today's do-not-initiate action. It would undermine a future initiation argument based on improving efficiency. At the current price, all three operating cases reject initiation; no artificial recommendation flip is claimed.

The reverse DCF changes only the SG&A/GP path. Its approximately 34.24% terminal ratio is an extreme requirement relative to the selected paths; it is not proof that the market literally forecasts that ratio. Other combinations of growth, margins, SBC, taxes and discount rates could reconcile price.

## October refresh convention

The previous September 24 snapshot is preserved under `reports/september-24-snapshot/`. October 19 resets the five rolling annual forecasts to the new valuation date using the same LTM base and assumptions. It is a fresh conditional forecast with an 80-day opening-balance proxy, not a discounted rollforward of the prior fixed-date cash flows. Thus DCF endpoints stay unchanged by construction; market multiples and the reverse DCF change. PATH and PEGA quotes are ten minutes apart; no claim of synchronized intraday pricing is made. WACC remains the disclosed classroom assumption.
