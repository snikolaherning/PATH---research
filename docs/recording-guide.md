For timed screen-by-screen preparation, use `docs/video-cue-sheets.md`. Its targets leave room below the maximum durations.

# Three recordings - preparation outline, not transcripts

These are AI-assisted talking points. Review the model and speak in your own words. Do not claim you wrote all code or independently performed checks that Codex performed. The shared architecture requires a small webcam view unless an approved accommodation applies. Use clear audio; production polish is unnecessary.

## Video 1 - Research evolution and AI check (maximum 3:00)

Suggested title: PATH - research evolution and evidence check.

- 0:00-0:30: Show the supplied initial document and state that you submitted this exact file September 1 at 2:40 p.m. It records initiate/buy; do not imply verified pre-AI receipt unless you have it.
- 0:30-1:15: Show Edition B. Explain the shift toward do-not-initiate: potential substitution rather than incremental agentic revenue, margin and cash-collection pressure. Your October 19 judgment moved 59% SG&A/GP out of the base.
- 1:15-2:15: Show the Lab 08 Gemini discrepancy record and annual EPS source tables. Explain why $0.15/$1.42 were rejected in favor of reported $0.52/$2.13. Name what you personally checked versus Codex's source work.
- 2:15-2:50: Show one consequential model check or bridge and explain why it matters. A balanced model is not proof of realistic assumptions.
- 2:50-3:00: End with what evidence would change your current view.

## Video 2 - Code, validation and clean run (maximum 5:00)

Suggested title: PATH - model walkthrough and validation.

- 0:00-0:40: Show README, input JSON, model and saved output. Explain data -> statements -> FCFF -> EV -> equity -> per share.
- 0:40-1:40: In `model.py`, show `project`, especially cash calculated from flows and the FCFF line. Explain SG&A/GP versus R&D/revenue, SBC expense/add-back/offset, and why remaining acquisition claims belong outside operating FCFF.
- 1:40-2:30: Show `value`: WACC, terminal runoff, excess cash, debt/claims, basic shares. Explain the July-to-October opening proxy and terminal-value dependence.
- 2:30-3:40: Record a clean checkout/extraction, fresh environment and run. Keep full end-to-end screen evidence; use the required time limit. Commands are in README. Show saved financial output and test results.
- 3:40-4:30: Run the targeted failure test or show its full output: `python3 -m unittest -v test_model.FinanceTests.test_highest_risk_corruption_is_refused`. Explain that altered cash/FCFF must block valuation. This ordinary demonstration is separate from your AI-closed exercise.
- 4:30-5:00: Identify a real limitation (market-calibrated WACC, precise dilution, opening-date lag or agentic unit economics) and point to the validation record.

## Video 3 - Committee defense with live local demonstration (maximum 5:00)

Suggested title: PATH - investment committee recommendation.

- 0:00-0:35: Open `index.html`. Lead with do-not-initiate at the dated $13.03 price, a $2.68-$6.11 DCF range and 12-18-month monitoring horizon.
- 0:35-1:40: Switch base/downside/upside in the local display. Explain the causal business changes and how profit and FCFF move. Make the application the main visual evidence.
- 1:40-2:30: Show the full output's WACC/growth table and reverse DCF. Explain what is held fixed and why 34.24% SG&A/GP is a conditional implication, not a forecast.
- 2:30-3:20: Defend conflicting methods: peer EV/revenue is near market while DCF is much lower. Explain why you do not average them and why the operating view drives your decision.
- 3:20-4:20: State positive and negative triggers. ARR >12% twice, retention 110%, incremental agentic revenue, 81% GM, efficiency evidence; bearish retention below 105% twice. Crossing a threshold prompts a rerun.
- 4:20-5:00: Acknowledge the highest-impact limitation and request zero exposure pending evidence. Use the October 19 morning quote timestamp; do not describe it as a closing price.

## After recording

Use three separate Unlisted/Public YouTube links or approved Purdue-hosted equivalents; not Private. Correct automatic captions for finance terms, tickers and material numbers. Save actual corrected transcripts as `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt`, `docs/transcript-video-3.txt`. These outlines are not transcripts and must not be renamed as such. Record actual durations and evidence timestamps in the manifest after the recordings exist.

## Explain-back checklist

Before recording, be able to explain: why FCFF uses WACC; why cash is added only once; why basic shares and diluted EPS differ; how SBC is charged once; why deferred revenue can provide cash; why ARR is not revenue; what the 63% assumption means; why PEGA's sales multiple disagrees; and what the tests establish versus what remains judgment.
