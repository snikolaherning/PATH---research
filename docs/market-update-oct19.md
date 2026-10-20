# October 19 market and information refresh

Reviewed October 19, 2026 morning. This is a frozen intraday snapshot, not the closing price or a live feed.

| Input | Prior September 24 close | October 19 observed quote | Source |
| --- | --- | --- | --- |
| PATH | $12.60 | $13.03, 11:15 a.m. EDT | [StockAnalysis](https://stockanalysis.com/stocks/path/) |
| PEGA | $34.23 | $34.37, 11:25 a.m. EDT | [StockAnalysis](https://stockanalysis.com/stocks/pega/) |

These quotes are ten minutes apart and have not been independently corroborated tick-for-tick. Reported shares and balance sheets remain lagged. Provider pages are dynamic; the extracted numerical observations and timestamps are frozen in `data/inputs.json`. Prior inputs/results/logs remain under `reports/september-24-snapshot/`.

## New information since September 24

[UiPath filing index](https://ir.uipath.com/financials/sec-filings) lists Forms 4 and 144 dated October 2, 5, 9, 13 and 15. These are ownership/proposed-sale reports, so saying there were no new filings would be incorrect. [Page 2](https://ir.uipath.com/financials/sec-filings?page=2) shows the latest 10-Q on September 8 for July 31. No newer quarterly financial report was found in this review. Ownership forms do not replace a consolidated cash-flow statement; opening liquidity is still a proxy.

[BDO, September 29](https://ir.uipath.com/news/detail/472/uipath-and-bdo-expand-partnership-to-build-agentic-solution-accelerators-for-continuous-monitoring-and-testing): expanded collaboration for agentic audit and controls solutions. [Snowflake, September 30](https://ir.uipath.com/news/detail/473/uipath-and-snowflake-announce-two-way-integration-connecting-automation-and-governed-data-now-available-on-snowflake-marketplace): expanded two-way integration of automation and governed data. These support distribution/use cases but do not quantify incremental agentic ARR, cannibalization or contribution margin. The [company news index](https://ir.uipath.com/news) also lists Oracle Marketplace availability and analyst recognition in October. No numerical forecast change is inferred from promotional announcements alone.

[Pega's announced Q3 release](https://www.pega.com/it/about/news/press-releases/pega-announce-financial-results-third-quarter-2026-and-host-conference) is scheduled for October 20 after market close, outside this snapshot. June financial inputs remain in use. This limited event check is not a complete legal/ownership-event audit of the peer.

## Decision effect

Operating paths and classroom WACC remain unchanged. The five rolling annual forecasts are reset to October 19 using the same LTM starting history; unchanged DCF values follow from this convention, not from a fixed-cash-flow time-value rollforward. July 31 balances now have an 80-day lag. The DCF range remains $2.68-$6.11, base $4.49. The higher PATH quote does not reverse do-not-initiate. PEGA multiples and reverse DCF were recomputed by the engine; see `reports/valuation-output.md`.

Student confirmation recorded today: exact Edition A file submitted September 1 at 2:40 p.m.; SG&A paths approved. The receipt itself has not been inspected. The original file and human-only validation boundary remain intact.
