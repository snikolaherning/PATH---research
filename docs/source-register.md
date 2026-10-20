# Source register

All amounts are USD millions, converted from thousands by dividing by 1,000; shares are millions. The valuation was refreshed October 19, 2026 using morning intraday quotes and latest available reported financials. Financial statement dates have not been relabeled as current observations. See `market-update-oct19.md` for the intervening-event check.

| Key | Source and locator | Dates | Inputs / check |
| --- | --- | --- | --- |
| PATH-A | [UiPath FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1734722/000173472226000012/path-20260131.htm), financial statements pp. 78-83; Notes 9, 10 and 13 | Period January 31, 2026; March 2026 filing | Annual revenue, GP, SG&A, R&D, CFO, capex, SBC, D&A; normalization, tax and accrual definitions. |
| PATH-Q | [UiPath July 2026 10-Q](https://ir.uipath.com/financials/sec-filings/content/0001734722-26-000050/path-20260731.htm), cover; balance sheet; income/cash-flow statements; Notes 6-9 | Filed September 8; balances July 31; cover shares September 3 | Full opening balance sheet; current/prior H1 history; 456.464703m A + 64.690706m B = 521.155409m shares; acquisition claims; amortization. |
| PATH-Q-release | [Q2 FY2027 release](https://ir.uipath.com/news/detail/461/uipath-reports-second-quarter-fiscal-2027-financial-results), financial highlights and consolidated statements | September 2026 release; period July 31 | Independently cross-check cash 607.414 + current securities 676.576 + noncurrent securities 121.035 = 1,405.025; restricted cash excluded. ARR and retention definitions; operating metric baseline. |
| PATH-EPS | [FY2026 annual release](https://ir.uipath.com/news/detail/431/uipath-reports-fourth-quarter-and-full-year-fiscal-2026-financial-results), annual diluted EPS column and tax reconciliation | March 11, 2026; year ended January 31 | Reported diluted EPS $0.52; retained as reported, not normalized P/E. |
| PEGA-A | [PEGA FY2025 release](https://www.sec.gov/Archives/edgar/data/1013857/000101385726000015/q42025_ex-991.htm), annual operations and EPS | February 10, 2026; December 31 year end | Revenue 1,745.812; diluted EPS $2.13. Values reflect split-adjusted convention. |
| PEGA-Q | [PEGA June 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1013857/000101385726000050/pega-20260630.htm), cover, statements, Note 9 | July 21, 2026 filing; shares July 13 | 164.404945m basic shares; cash/securities 361.907; no cash borrowings; H1 revenue 850.689 versus 860.145. |
| PEGA-Q-release | [PEGA Q2 release](https://www.sec.gov/Archives/edgar/data/1013857/000101385726000049/q22026_ex-991.htm), balance sheet and operations | July 21, 2026 | Cross-check quarterly inputs; newer growth weakness qualifies peer selection. |
| PATH-price | [StockAnalysis PATH quote](https://stockanalysis.com/stocks/path/) | October 19, 2026, 11:15 a.m. EDT | $13.03 intraday; replaces September 24 close $12.60. |
| PEGA-price | [StockAnalysis PEGA quote](https://stockanalysis.com/stocks/pega/) | October 19, 2026, 11:25 a.m. EDT | $34.37 intraday; replaces September 24 close $34.23. Quotes are ten minutes apart. |
| Training | [Lab 09 course instructions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-05/lab-09-proforma-build.md); saved `legacy/lab09-proforma.md` benchmark table | Course training case | Saved known answers: ABG equity 5,237.34; per share 291.75. Final automated check reproduces both. Preserve instructor answer sheet if separately supplied. |

## Opening balance mapping (PATH-Q)

| Code fields | Filing mapping |
| --- | --- |
| Cash; securities; restricted cash | 607.414; 676.576 + 121.035; 1.475 |
| Receivables; contract assets; deferred costs; prepaids | 307.112; 135.222 + 4.832; 86.526 + 165.022; 112.305 |
| PP&E; ROU; intangibles; goodwill; DTA; other assets | 46.436; 63.470; 101.479; 179.481; 230.087; 68.895 |
| Payables; compensation; deferred revenue | 16.848; 89.853; 543.627 + 71.722 |
| Lease liabilities | 10.322 current within accruals + 69.438 noncurrent = 79.760 |
| Acquisition claims | 3.859 deferred + 30.392 contingent = 34.251 |
| Tax payable; equity withholdings | 9.777; 3.204 + 2.748 = 5.952 |
| Operating accruals | 156.930 total - 10.322 leases - 9.777 tax - 34.251 acquisitions - 5.952 equity = 96.628 |
| Other liabilities; equity | 10.398; 1,948.551 |
| Aggregate check | Assets 2,907.367 = liabilities 958.816 + equity 1,948.551 |

## LTM construction and definitions

PATH LTM revenue = 1,610.572 + 828.638 - 718.352 = 1,720.858. PEGA LTM revenue = 1,745.812 + 850.689 - 860.145 = 1,736.356. Each includes its latest available half-year and subtracts the matching prior half-year. Period endpoints differ by one month and are disclosed.

PATH LTM GP, SG&A, R&D, D&A and SBC are constructed the same way in `data/inputs.json` and the reproducible input values are visible in the output. No annualization of one quarter is substituted for LTM revenue.

WACC inputs, future operating ratios, tax rate and cash-reserve policy are assumptions, not sourced market facts. See the challenge record for their basis and reversal evidence. No quote, filing value or completed human action is inferred from an AI assertion alone.

## Reproducible historical transformations

`data/history-lineage.json` preserves the annual/current-half/prior-half operands and source URLs for every LTM line. `python3 tools/check_package.py` recomputes these against the engine inputs. SG&A combines sales and marketing with general and administrative; capex uses the positive magnitude of the filing's cash outflow. Opening operating reserve = (LTM revenue - gross profit + SG&A + R&D - D&A - SBC) / 4. This is a reported-LTM cash-cost proxy, not a fully adjusted recurring-cost estimate. Historical restructuring normalization is shown separately in model-method.md and is not silently applied to the reserve.

## Exclusions, revisions, use rights and privacy

Use the named annual and quarterly periods; no missing quarterly amount is silently imputed. Forecasts, discount-rate inputs and cash policy are analyst assumptions. Exclude restricted cash from excess liquidity, unsupported NOL/DTA monetization, repeat capitalization of future cash, and unqualified acquisition multiples. Peer selection chronology is retained in the original lab record. The September market snapshot and human exercise are preserved separately; subsequent presentation corrections do not overwrite them.

The package uses selected numerical facts and links to public company/SEC sources, with attribution. Public access is not a blanket license to redistribute provider databases: no proprietary bulk feed or paid database is bundled or claimed licensed. Original lab materials are retained as student/course evidence, not offered under a new open-source license. The project contains the student's name and the peer name supplied for attribution; no customer-level personal records, credentials or financial account details are required. AI-off Git emails are explicitly local placeholders. Review new uploads for secrets and private information before publication.

No new accounting restatement was identified in the limited review; that is not a comprehensive restatement audit. If a source revision is discovered, retain the old observation, date the correction and rerun the engine. The intraday quote pages are dynamic; exact observations/timestamps are frozen in inputs.json, with a disclosed ten-minute peer-quote mismatch.
