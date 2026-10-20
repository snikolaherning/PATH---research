# UiPath DCF inputs and conclusion

Valuation date: September 10, 2026  
Ticker: NYSE: PATH  
Amounts are USD millions unless stated otherwise.

## Sourced inputs

| Input | Value | Unit | As-of date | Source and locator | Treatment |
| --- | ---: | --- | --- | --- | --- |
| Starting FCFF | 352.160 | USD millions | January 31, 2026 | UiPath FY2026 results, reconciliation of operating cash flow to adjusted free cash flow: GAAP operating cash flow of 371.208 less purchases of property and equipment of 19.048. [FY2026 results](https://ir.uipath.com/financials/sec-filings/content/0001734722-26-000007/path-2026131xex991.htm) | FCFF proxy because UiPath reports no funded debt or interest expense requiring an after-tax interest add-back. |
| Growth, Year 1 | 12.0% | annual FCFF growth | Forecast | UiPath reported FY2026 revenue growth of 13%; Q2 FY2027 revenue growth of 13% and ARR growth of 12%. [FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1734722/000173472226000012/path-20260131.htm), [Q2 FY2027 results](https://ir.uipath.com/news/detail/461/uipath-reports-second-quarter-fiscal-2027-financial-results) | Analyst forecast beginning near recent revenue and ARR growth. |
| Growth, Year 2 | 11.0% | annual FCFF growth | Forecast | Same operating evidence as Year 1. | Analyst forecast. |
| Growth, Year 3 | 10.0% | annual FCFF growth | Forecast | Same operating evidence as Year 1. | Analyst forecast. |
| Growth, Year 4 | 9.0% | annual FCFF growth | Forecast | Same operating evidence as Year 1. | Analyst forecast. |
| Growth, Year 5 | 8.0% | annual FCFF growth | Forecast | Same operating evidence as Year 1. | Analyst forecast with a gradual fade. |
| WACC | 11.0% | discount rate | September 10, 2026 estimate | Course method in Lab 06: cost of equity = risk-free rate + beta × equity risk premium. Using the class inputs of 4.5% + 1.3 × 5.0% gives 11.0%; UiPath has no funded debt in this model, so WACC equals the estimated cost of equity. [Lab 06](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-06-sensitivity-and-reverse-dcf.md) | Estimate, not a company-reported figure. This is the input I trust least. |
| Terminal growth | 3.0% | annual perpetual growth | After Year 5 | Course guidance says terminal growth should represent the long-run economy and remain below WACC. [Lab 06](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-06-sensitivity-and-reverse-dcf.md) | Long-run assumption. |
| Non-operating cash | 1,405.0 | USD millions | July 31, 2026 | Cash, cash equivalents, and marketable securities in UiPath's Q2 FY2027 results. [Q2 FY2027 results](https://ir.uipath.com/news/detail/461/uipath-reports-second-quarter-fiscal-2027-financial-results) | Added in the enterprise-to-equity bridge. |
| Debt | 0.0 | USD millions | July 31, 2026 | UiPath Q2 FY2027 balance sheet lists current and non-current liabilities but no funded borrowings. [Q2 FY2027 results](https://ir.uipath.com/news/detail/461/uipath-reports-second-quarter-fiscal-2027-financial-results) | Operating lease liabilities are excluded from funded debt for this simplified classroom model. |
| Diluted shares | 523.013 | millions of shares | Quarter ended July 31, 2026 | GAAP weighted-average common shares outstanding, diluted. [Q2 FY2027 results](https://ir.uipath.com/news/detail/461/uipath-reports-second-quarter-fiscal-2027-financial-results) | Used to calculate value per diluted share. |
| Market price | 13.57 | USD per share | September 9, 2026, 4:00 p.m. EDT | UiPath closing price. [StockAnalysis price history](https://stockanalysis.com/stocks/path/history/) | Reverse-DCF target. |

## Base DCF result

The five-year DCF produces an enterprise value of **$6,076.7039 million**, an equity value of **$7,481.7039 million**, and a value of **$14.3050 per diluted share**. The present value of the terminal value represents **71.28%** of enterprise value.

## Reasonableness

The DCF value is approximately **1.05×** the $13.57 market price, which falls within the course's 0.5×–2.0× reasonableness range. I would not adjust the inputs simply to force a closer match. WACC is the least reliable input because the 11.0% estimate depends on classroom capital-market assumptions rather than a company-reported value.

The sensitivity grid ranges from **$13.31** per share at an 11% WACC and 2% terminal growth to **$20.86** at a 9% WACC and 4% terminal growth. The base combination of an 11% WACC and 3% terminal growth produces **$14.31** per share.

## Reverse DCF

At a target price of $13.57, the reverse DCF solves for a **−1.6208 percentage-point uniform shift** to all five explicit growth rates. The market-implied growth path is therefore approximately **10.38%, 9.38%, 8.38%, 7.38%, and 6.38%**, while starting FCFF, WACC, terminal growth, cash, debt, and diluted shares remain fixed. This result describes the assumptions consistent with the price; it does not prove that the shares are mispriced.

## Conditional call

**Watch-defer. Initiate if UiPath's reported cash generation and ARR growth continue to support at least the market-implied growth path, or if the share price falls below the $13.31 low corner of the sensitivity grid while the operating outlook remains intact; otherwise remain on watch. Monitor adjusted free cash flow in the next quarterly report.**

## Run command

```bash
python3 dcf.py
```

One command prints the twelve-line DCF, sensitivity grid, and reverse-DCF result.
