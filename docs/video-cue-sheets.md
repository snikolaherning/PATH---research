# Recording cue sheets

AI-assisted preparation, to be disclosed in the AI-use record. These are notes, not transcripts. Use your own voice and explain only claims you understand. Targets leave room below the hard 3:00 / 5:00 / 5:00 limits; stop before the limits. Keep a small webcam view unless an approved accommodation applies. Record three separate videos with readable screens and clear audio.

Before recording, open the needed files and source pages in tabs. Do not spend recorded time searching for files. Use the final PATH-project folder, not old lab outputs or the frozen AI-off exercise copy. The current market comparison is a frozen October 19 morning snapshot, not a live quote at recording time.

## Video 1 — Research evolution and AI-output check

Target 2:45; maximum 3:00. The updated Research-Evolution.pdf puts the finished current analysis on pages 1–2 and the unchanged original on pages 3–7. Briefly show original page 3, then use pages 1–2 for the explanation and open source links for the EPS check.

| Time | Show | Speaking cues |
| --- | --- | --- |
| 0:00–0:20 (20 sec) | docs/edition-a-supplied-unchanged.md | My original submitted file was September 1 at 2:40 p.m. Initial view: initiate/buy, based on platform and agent opportunity. It is preserved unchanged, including its incomplete fields. |
| 0:20–0:55 (35 sec) | docs/edition-b.md, change table | My judgment shifted toward do not initiate. Agents may replace bot licenses instead of adding revenue; competition, inference costs and weaker upfront collections matter. This is a risk hypothesis, not an observed fact. Own judgment and peer challenges drove the change; AI helped implement and check it. |
| 0:55–1:20 (25 sec) | Operating-leverage row; docs/assumption-challenges.md | I do not accept 59% SG&A/gross profit as the base. Base is 65% to 63%; 59% is upside. Anika Rao's recorded feedback raised dilution and reversal evidence; the separate Lab 10 SG&A challenger is not identified as Anika. Explain why limited efficiency better fits your concern. |
| 1:20–2:00 (40 sec) | legacy/lab08-uipath-comps.md AND annual company EPS source tables | The lab record identifies Gemini's EPS claims of $0.15 for PATH and $1.42 for PEGA. Annual releases report $0.52 and $2.13. Reject the AI figures and use consistent reported diluted annual EPS. These earnings still contain tax effects, so this is a qualified cross-check. Distinguish your original lab work from Codex's later source checks; do not claim checks you did not perform. |
| 2:00–2:30 (30 sec) | docs/human-change-reconciliation.md and reports/human-changed-input-result.json | My independent test lowered the five-year gross-margin path. I predicted lower value before running. Value fell from $4.49 to $4.03, about 10.4%; do not initiate remained. This supports sensitivity to margin risk, not proof the margin decline will occur. |
| 2:30–2:45 (15 sec) | Edition B final paragraph | My question is now whether agentic growth is incremental and profitable. Better retention, margin stability and selling efficiency would prompt a new valuation. |

EPS source pages to open before recording: PATH annual release https://ir.uipath.com/news/detail/431/uipath-reports-fourth-quarter-and-full-year-fiscal-2026-financial-results and PEGA annual release https://www.sec.gov/Archives/edgar/data/1013857/000101385726000015/q42025_ex-991.htm . Find the annual diluted earnings-per-share row, not a quarterly or non-GAAP row. If unavailable, use the actual saved source evidence; a typed summary alone is not an independent source table.

## Video 2 — Code, financial logic, validation and reproduction

Target 4:40; maximum 5:00. Show actual code and an actual fresh run. Reading the README or showing only the dashboard is insufficient.

| Time | Show | Speaking cues |
| --- | --- | --- |
| 0:00–0:25 (25 sec) | README repository map and data/inputs.json | Data inputs feed model.py; run.py generates statements, valuation and offline display; test_model.py checks financial integrity. Standard-library Python, no API keys or network required. Codex assisted implementation; I own the assumptions and judgment. |
| 0:25–0:55 (30 sec) | docs/source-register.md, then inputs opening/history | Dollars are millions; shares are millions; ratios are decimals. July 31 balance sheet and LTM revenue are sourced from filings. LTM = annual + current half-year minus prior half-year. Five rolling years end October 19; the July opening position is a proxy, not observed October cash. |
| 0:55–1:40 (45 sec) | model.py: project, row_checks | Growth drives revenue, gross margin drives gross profit; SG&A is a share of gross profit and R&D a share of revenue. Income, cash flow and balance sheet link. Cash follows actual modeled flows, not a balancing plug. FCFF retains SBC's economic cost; CFO's noncash add-back is reconciled separately, avoiding double counting. |
| 1:40–2:15 (35 sec) | model.py: value | FCFF goes to all capital providers, so discount at WACC to enterprise value. Add excess liquidity, subtract funded debt and acquisition claims, divide by basic shares. Do not add forecast accumulated cash again. Terminal calculation lets finite acquired intangibles run off rather than assuming their amortization lasts forever. |
| 2:15–3:15 (60 sec) | Terminal: fresh-copy commands below; generated report | Run the commands on screen. New folder, fresh virtual environment, generate output, run all ten tests. Show the resulting valuation-output.md. State what the tests cover: known answer, source reconciliation, statement articulation, boundaries, sensitivity directions and valuation bridges. Do not say these tests prove the forecast. |
| 3:15–3:55 (40 sec) | test_model.py: test_highest_risk_corruption_is_refused; targeted command | The high-risk failure is an internally inconsistent model producing a plausible valuation. The test corrupts cash, equity, PP&E, CFO, FCFF and deferred revenue separately and requires valuation to refuse. Run the targeted test; an OK means the expected refusal occurred. |
| 3:55–4:25 (30 sec) | Human prediction, result and Git log | Prediction commit preceded execution. Gross-margin stress lowered value 10.4%, consistent with my prediction; action unchanged. The original independent exercise is preserved. This recorded presentation is a later demonstration, not a replacement AI-off run. |
| 4:25–4:40 (15 sec) | docs/validation-and-ai-use.md | Tests establish calculation consistency. They do not establish the right assumptions: 11% WACC is a classroom assumption; opening balances and share treatment are approximations. |

### Fresh run commands for Video 2

Start screen recording BEFORE running these. Copy/paste the block into Terminal. It creates a new temporary directory each time, copies the actual submission files, and creates a fresh environment. No network, installations or credentials are needed. Keep the full run visible.

```bash
recording_dir=$(mktemp -d /tmp/path-recording.XXXXXX)
cp -R '/Users/stefanherning/Documents/Codex/2026-10-19/we-ba/outputs/PATH-project/.' "$recording_dir/"
cd "$recording_dir"
python3 -m venv --without-pip .venv
.venv/bin/python run.py
.venv/bin/python -m unittest -v test_model
open reports/valuation-output.md
```

If Markdown opens in an unsuitable app, show the generated report in your usual editor; prepare the editor beforehand. The fresh output is in the temporary directory printed by `pwd`. For the targeted demonstration, return to that same Terminal and run:

```bash
.venv/bin/python -m unittest -v test_model.FinanceTests.test_highest_risk_corruption_is_refused
```

Do not rerun locked_run.py for the recording: show your preserved independent evidence instead.

## Video 3 — Investment committee recommendation with local demonstration

Target 4:10; maximum 5:00. Keep the working local application as the main visual. Switch cases during the explanation, then use the full output for sensitivity and peer evidence. This is the investment decision, not a second code walkthrough.

| Time | Show | Speaking cues |
| --- | --- | --- |
| 0:00–0:25 (25 sec) | index.html, base selected | Recommendation: do not initiate. The fund holds no position. Compare the $4.49 base and $2.68–$6.11 range with the frozen October 19, 11:15 a.m. EDT quote of $13.03. Monitor for 12–18 months, four to six reports. |
| 0:25–1:00 (35 sec) | Base forecast | Agents could replace robot revenue, pressure retention and require inference spending. Base growth fades to 7%, gross margin to 80%, and SG&A/gross profit to 63%. Explain that these are assumptions translating your thesis, not company guidance. |
| 1:00–1:40 (40 sec) | Switch downside, then upside, then base | Downside: slower growth, 78% final gross margin, SG&A at 65% of gross profit, weaker advance collections. Upside: stronger growth, 81% gross margin and SG&A efficiency to 59%. All remain below the quoted price; upside here means better operations, not necessarily a buy. |
| 1:40–2:10 (30 sec) | reports/valuation-output.md: WACC/g table and reverse DCF | At 11% WACC and 3% terminal growth, about 79% of enterprise value comes from the terminal period. Show the sensitivity range on screen. Holding other base assumptions fixed, supporting $13.03 requires SG&A/gross profit near 34.24% by year five. That is a conditional one-driver solution, not proof of what the market expects. |
| 2:10–2:40 (30 sec) | Comparables table | PEGA sales multiple implies $12.75; annual reported P/E implies $8.39. Sales valuation is counterevidence to blanket overvaluation. DCF focuses on cash profitability after economic SBC cost. Do not average methods; one peer, different financial periods and tax-affected EPS limit confidence. |
| 2:40–3:25 (45 sec) | Dashboard monitoring section | Reconsider if ARR growth exceeds 12% twice, retention reaches 110%, agentic ARR is disclosed as incremental, gross margin stabilizes near 81%, and selling costs grow slower than gross profit. Retention below 105% twice strengthens the downside. Reaching a trigger means rerun the valuation, not automatically buy. |
| 3:25–3:55 (30 sec) | Base display and memo limitations | Limitations: July opening cash proxy, basic shares with SBC cost approximation, assumed discount rate and high terminal dependence. Cash/share stresses measure sensitivity, not all uncertainty. Partnership news supports product activity but does not establish incremental profitable ARR. |
| 3:55–4:10 (15 sec) | Dashboard recommendation | Committee ask: retain zero exposure and reassess over the next four to six earnings reports. Initiate only if updated evidence and valuation justify the prevailing price with a margin of safety. |

## Rubric coverage and remaining evidence

| Rubric criterion | Where the videos show it | Required underlying evidence / remaining limitation |
| --- | --- | --- |
| Problem definition, 45 | V1 original-to-current judgment; V3 user, action, horizon and ask | Unchanged A and B. Receipt time is student-attested; receipt itself not independently inspected. |
| Data integrity, 45 | V1 source-table check; V2 inputs, dates, units and LTM transformation | Source register and dated inputs. Preserve reporting lag, exclusions and provider definitions. |
| Financial judgment, 60 | V2 FCFF/WACC/bridge; V3 cases, peer disagreement and reversal triggers | Linked statements, sensitivity, reverse DCF and challenge record. WACC and one-peer limitations remain. |
| Technical execution, 45 | V2 actual code, fresh environment, executed output | Runnable repository, dependency instructions and visible report; final files must be uploaded and accessible. |
| Validation/reproduction, 75 | V1 tested AI claim; V2 clean run, deliberate corruption and locked human test | Raw prediction, commits, before/after output and reconciliation; known-answer and other automated tests. Recorded clean run still must actually occur. |
| Communication, 30 | Three distinct, concise videos with consistent numbers | Corrected transcripts, working video links, timestamped manifest, matching PDFs and final submission. |

Coverage is not a score guarantee. Video narration cannot repair missing underlying evidence or unresolved financial limitations. The prompt asks for a downside that could alter the recommendation; this model's downside reinforces non-initiation rather than changing the action. State that honestly; do not claim the test reversed the decision. Reversal triggers are conditional evidence for future revaluation.

## After recording

Send the three files or accessible links and the actual captions/transcripts. Correct substantive errors in finance terms, names and numbers. Do not rename these cues as transcripts. Use three distinct Unlisted/Public links or approved Purdue hosting. Record actual durations and timestamps for required evidence in the manifest. Disclose Codex-assisted cue preparation alongside existing AI assistance.
