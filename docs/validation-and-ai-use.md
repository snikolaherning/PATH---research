# Validation and AI-use record

Updated October 19 after the student exercise and receipt of three completed recordings. This document separates automated checks from student-only evidence. Its PDF and Markdown must match at submission.

## Evidence status

| Requirement | Evidence | Status |
| --- | --- | --- |
| Synthetic/known-answer reconciliation | test_classroom_known_answer reproduces saved ABG training answers: $5,237.34m equity and $291.75/share; legacy lab records source | PASS, AI executed; preserve course answer sheet if separately supplied |
| Independent source/definition check | July 10-Q versus Q2 release: cash and securities $1,405.025m; restricted cash excluded; source-register links | PASS, Codex checked; not a claim of student verification today |
| Written directional test before execution | reports/directional-test-plan.md: normalized tax 23% to 26%; predicted value decrease and unchanged non-initiation | PASS; AI-authored ordinary test, not human locked exercise |
| Directional actual | Base $4.492870; changed $4.375455; change $-0.117416/share | Expected decrease; both below the original $12.60 test snapshot; also below the updated $13.03; action unchanged |
| Human Locked Changed-Input Record | Original prediction, result, reconciliation and Git history bundle | Completed; 10.37% value decrease, action unchanged; AI-closed status student-attested |
| Pro-forma articulation | All five years in all three cases: BS, cash, equity, asset and cash-flow bridges | PASS; see test-log and visible output |
| Historical reconciliation | July assets/liabilities/equity and H1 cash-flow including FX/restricted cash | PASS; historical deferred-revenue residual from Lab 10 remains unresolved |
| DCF boundaries / monotonicity | g >= WACC, zero shares and invalid inputs refused; WACC up -> value down; g up -> value up across tested grid | PASS; tested domain, not a universal theorem for all possible cash flows |
| Enterprise/equity and SBC bridges | Direct operating FCFF equals CFO less SBC, capex and reserve investment; claims deducted once; shares reconcile | PASS |
| Peer definitions | Same price date; EV/LTM sales and annual reported diluted P/E; cash and debt conventions stated | PASS on calculation consistency; one-peer and lag limitations remain |
| Highest-risk failure test | Corrupt cash, FCFF and other statement values by $1m; valuation must refuse | PASS; verifies integrity, not operating assumptions |
| Clean environment | reports/cold-run-log.txt: fresh copy, new venv without pip, no network, successful run/tests | PASS; AI text log and Video 2 full-suite demonstration at 01:36-02:08 |
| Tested AI output | Lab 08 rejected incorrect Gemini EPS figures using annual company releases | Historical evidence preserved; full explanation in Edition B |
| Final videos/transcripts/access | Three actual-recording transcripts and Unlisted YouTube links in manifest | Signed-out access checked; repository publication and Brightspace submission tracked separately |

## Package consistency audit

The pre-recording audit verifies historical operands against inputs, saved report/dashboard against the current engine, unchanged Edition A bytes and the exact committed human prediction recovered from the bundled Git history. `tools/check_package.py --submission` additionally checks for actual video metadata/transcript files and deliberately fails while these are missing. It does not certify transcript accuracy, external link access or grading quality. See `docs/quality-audit.md` for unresolved rubric risks.

## Execution evidence

`python3 -m unittest -v test_model` passed 10 tests. `python3 run.py` generates statements, sensitivity, reverse DCF and offline display without network dependencies. The clean-environment run passed the same tests in a fresh venv. Source files and outputs are included; Video 2 shows the student fresh-environment run and full test suite at 01:36-02:08.

The first attempt to save a 25% tax test plan used an incorrect relative path, so that file was not created before that test ran. It is not claimed as the saved-before-run record. A separate plan for a previously unrun 26% case was saved before executing that case. The correction is preserved in the plan file; no history was backdated.

## Human locked record completed October 19

Stefan Herning independently selected gross margin (`gm`). The five-year path changed from **82%, 81%, 80.5%, 80%, 80%** to **79%, 78.5%, 78%, 77.5%, 77%**. The saved raw numeric arrays use decimal ratios; his units answer says "%". This note clarifies the representation without editing his original.

His prediction was a decrease in value and no reversal of his bearish stance, because lower gross margin leaves less income per dollar of revenue. Prediction saved at 5:28:21 p.m. EDT; committed at 5:28:24 p.m. before the runner executed at 5:28:24.233 p.m. The pre-run commit is `30bebd0e9f433ca58a337c368eeab49ae7470eec`. Reconciliation was committed at 5:30:37 p.m. in `f0ab9912cbd8c9332c46dea5ba9d8714da44ea66`.

Actual base value **$4.492870** fell to **$4.026833**, a **$0.466037 / 10.37% decrease**. The student correctly reported approximately 10.4%, matched his directional prediction, and retained **do not initiate**. His original prediction's "hard sell" wording is preserved; the final action remains non-initiation because the fund has no position.

Source evidence: `docs/human-change.json`, `docs/human-change-reconciliation.md`, `reports/human-changed-input-result.json`, console log, Git log and `reports/human-exercise-history.bundle`. The result JSON's "reconciliation not supplied" placeholder describes the moment of execution; the separate student reconciliation was written afterward. Both are preserved unchanged.

Codex supplied the mechanical questionnaire/runner before the exercise and packaged evidence afterward. The student attests AI was closed for prediction, execution and reconciliation. Local commits establish saved ordering; they do not independently prove AI was closed. Commit emails are explicit local placeholders, not claimed personal addresses.

Interpretation added by Codex after completion: this is a conditional sensitivity test, not proof future margins will fall or that the valuation is correct. SG&A remains a percentage of gross profit, so lower gross profit also lowers modeled SG&A dollars; that partly offsets the earnings effect. The student reported no errors. Original wording and typos are retained in the raw evidence.

## Named AI tools and roles

**Codex:** inspected the supplied repository and project prompt; read the supplied A working copy; checked selected primary filings and historical market prices; proposed numerical scenario paths; implemented the integrated FCFF engine, tests and output; drafted the memo, Edition B, source/challenge records and timed recording cue sheets; performed ordinary automated and clean-environment checks. It also prepared local Whisper transcripts, corrected terminology/numbers against the project and sampled visuals while preserving the spoken account, and checked signed-out video access. It did not record videos, supply the student's human-only prediction, verify the Brightspace receipt or submit the project.

**Gemini:** historical Lab 08 record identifies it as a second AI used for peer suggestions and numerical claims. Its suggestions were not accepted automatically. Contradictory annual EPS figures were rejected against company releases. Complete prior context is limited to the saved lab record.

**Student:** supplied the October 19 Hold/Sell judgment, retained growth/margin slowdown, questioned SG&A reaching 59%, described the cannibalization/competition/cost/collection risk chain, supplied reversal thresholds and the 12-18-month horizon, and identified Anika Rao as the Apple-feedback partner. The student reviewed the memo and supplied three recordings presenting the project. No independent source opening or code authorship is attributed beyond the student's actual reports.

## AI-output decision example

Gemini's recorded UiPath annual EPS $0.15 and PEGA EPS $1.42 conflict with the annual releases' $0.52 and $2.13. **Reject those two AI figures.** Use reported diluted annual EPS consistently and disclose tax distortions. The sources are PATH-EPS and PEGA-A in `source-register.md`; the original discrepancy record is `legacy/lab08-uipath-comps.md`. A correct division cannot rescue an incorrectly defined input.

## Open issues requiring honest disclosure

- Student confirms the exact supplied Edition A was submitted September 1 at 2:40 p.m. The receipt itself is not independently inspected; original file labels and blanks remain unchanged.
- Student explicitly approved the SG&A paths October 19; three completed recordings are supplied.
- WACC is classroom-calibrated, NOL relief omitted, opening balances lag valuation date, and basic fixed shares are a proxy.
- Historical deferred-revenue cash-flow residual is not resolved; exact monthly amortization/award schedules and agentic unit economics are unavailable.
- Partner name for the separate Lab 10/Tesla exchange is not supplied. Anika is credited only for the Apple exchange identified by the student.
- Three recordings and actual-recording transcripts are supplied; publication verification is tracked in the manifest. The Brightspace receipt remains outstanding.

## Preserved original

The supplied Markdown is copied byte-for-byte without filling blanks. SHA-256: `08085403ab466521316ed4404ac8f5150fb7d132f519531f33eb77853981b60b`. This proves the copy matches the supplied file; it does not prove it matches the historical Brightspace submission or establish pre-AI authorship.

