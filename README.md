# UiPath investment committee valuation

**Committee recommendation: do not initiate at the October 19, 2026 intraday quote of $13.03 (11:15 a.m. EDT).** Five-year FCFF scenario range $2.68-$6.11 per basic share; base $4.49. The investment committee holds no position. Monitoring horizon: 12-18 months / four to six earnings reports.

## View without running

Open `index.html` for the offline scenario display, `reports/valuation-output.md` for material inputs and complete statements, or `docs/decision-memo.pdf` for the committee memo. The displayed results are saved executed output, not live prices. No web hosting is required.

## Reproduce

Python 3.9+ and its standard library are sufficient. No network, API keys or pip install is needed.

```bash
python3 run.py
python3 -m unittest -v test_model
```

Optional fresh environment:

```bash
python3 -m venv --without-pip .venv
.venv/bin/python run.py
.venv/bin/python -m unittest -v test_model
```

For a clean recorded demonstration, use a new checkout or extracted copy, create the fresh environment, and record the commands and visible output. The AI text log is not a substitute for the student's recording.

## Repository map

| File | Purpose |
| --- | --- |
| `data/inputs.json` | Dated historical inputs, assumptions and three operating scenarios |
| `model.py` | Three statements, checks, FCFF, terminal value, equity bridge, sensitivity and reverse DCF |
| `run.py` | Generate saved results, full report and offline HTML display |
| `test_model.py` | Ten ordinary technical tests; not the human AI-off exercise |
| `locked_run.py` | Execute a separately committed student-authored changed-input record while AI is closed |
| `reports/` | Visible financial output, raw results, test and clean-run logs |
| `docs/` | Memo, research evolution, sources, method, challenges, validation, recording guide and completion checklist |
| `legacy/` | Unchanged lab source files for provenance; not the final entry point |

## Sources and conventions

See `docs/source-register.md` and `docs/model-method.md`. October 19 timestamped intraday prices are paired with the latest reported financial positions; July PATH balances proxy opening financial position. Forecasts are five rolling years ending October 19, 2027-2031, not fiscal years. Basic shares of 521.155409m stay fixed under an SBC cash-cost approximation. P/E uses annual reported diluted EPS for both firms and is labeled separately. No NOL asset is added to equity.

The original DCF and FCFE teaching outputs remain under `legacy/`; do not present them as the final current model. Historical notes may reference outputs not included in the original repository. New complete statement outputs are in `reports/valuation-output.md`.

## Limitations and completion status

The student approved the SG&A paths on October 19. WACC uses classroom parameters. Reporting lag, basic fixed shares, amortization timing, NOL omission, one-peer evidence and terminal dependence limit precision. See the memo for conflicting peer evidence. The student completed the separately preserved AI-off changed-input exercise. Three completed recordings and actual-recording transcripts are linked in `docs/manifest.md`; Brightspace submission remains the student’s final step. The student confirms this exact Edition A was submitted September 1 at 2:40 p.m.; the receipt itself has not been inspected. `docs/finish-checklist.md` identifies the remaining actions.

AI-use disclosure: Codex performed final implementation, research checks and draft writing; historical labs also record Gemini suggestions. Human authorship and verification claims are limited to what the student actually supplied. See `docs/validation-and-ai-use.md`.

## Evidence preflight

Run `python3 tools/check_package.py` to verify lineage, output consistency, original Edition A and the human exercise Git bundle. After the recordings/transcripts and actual access checks are entered in `docs/video-evidence.json`, run `python3 tools/check_package.py --submission`. Missing video evidence deliberately fails the submission check; no outline is presented as a transcript. See `docs/quality-audit.md` for unresolved limitations.
