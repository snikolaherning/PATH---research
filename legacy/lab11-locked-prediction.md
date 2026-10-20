# Lab 11 — changed-input prediction

**Chronological record: earlier pending notes are preserved as originally written; confirmation, actual results and student reconciliation appear in later dated/order sections below.**

Recorded by AI from the student's message at **2026-09-29T18:09:19.382357+00:00**. This timestamps receipt/preservation, not a claimed earlier offline save. No Lab 11 changed-input case has been run. Student confirmation of an independently saved note and reciprocal partner unit/range checks remains pending.

## Student-selected change

SG&A / gross profit, FY2027–FY2031:

- Base: 65%, 63.5%, 62%, 60.5%, 59%.
- Changed: 65%, 62%, 59%, 56%, 53%.
- Changes: 0, −1.5, −3, −4.5, −6 percentage points.
- All other independent inputs remain at base; linked statements recalculate.

## Student prediction — preserve unchanged

| Output | Base | Expected result | Expected change | Rough range |
| --- | ---: | ---: | ---: | ---: |
| FY2031 operating profit, USD millions | 268.00 | about 387 | +119, about +44% | 375–395 |
| FY2031 FCFE, USD millions | 193.37 | about 285 | +92, about +47% | 275–295 |
| Annual-base value per share, USD | 5.69 | about 7.30 | about +1.60 | 7.10–7.40 |

The student's +$1.60 is rounded; $7.30 − $5.69 equals $1.61. Keep both the prediction and its intended approximation, not an after-the-fact adjustment.

## Before-run items still needed

- Student's short causal explanation for this particular change.
- Confirmation of the note saved with AI closed, with its timestamp or commit if available.
- Partner's unit/one-input check and the student's reciprocal check on the partner's prediction.

## Actual result and reconciliation

Not run. Append actual outputs and the student's interpretation later; do not replace this prediction.


## Student's pre-run causal explanation — added before changed runs

**Operating profit (+$119M):** SG&A dollars equal the ratio times gross profit, and cutting SG&A doesn't change revenue or gross profit. In FY2031 the ratio falls 6 points on about $1,986M of gross profit, so SG&A drops about $119M. Operating profit is gross profit minus SG&A minus R&D, so the full $119M saving becomes operating profit, taking it from $268M to about $387M.

**FCFE (+$92M):** The saving is taxed at 23% in FY2031, leaving $119M × 0.77 ≈ $92M. FCFE picks up all of that because every other piece is tied to revenue, which didn't change: capex, depreciation, working capital and the SBC offset. With no debt, there's no interest or borrowing to change.

**Value/share (+$1.60):** Equity value is the present value of FCFE at 11%. Student's rough breakdown:

| Piece | Calculation | Approximate present value |
| --- | --- | ---: |
| Forecast years | Extra FCFE of about $22M, $47M, $64M and $92M in FY2028–31, discounted | $149M |
| Terminal | $92M × 1.03 / (11% − 3%), discounted five years | $703M |
| Total | Approximately $852M / 537.037M shares | $1.59/share |

Student's interpretation: almost 85% of the gain comes from terminal value because the lower final-year cost level persists, with subsequent growth at 3%.

**Pre-run AI qualification:** preserve these as rough predictions, not verified model output. In the actual model, the cash reserve depends on cash operating costs, including SG&A, and FCFE deducts the annual change in that reserve. Therefore after-tax profit is not necessarily the entire FCFE change. Terminal cash flows also recalculate the reserve at sustainable growth. Reconcile this link and the intermediate-year estimates after the run; do not overwrite the original prediction with results. No Lab 11 changed-input scenarios have been run. Offline save and the partner's one-input-only confirmation remain unreported.


## Before-run confirmation received

The student answered yes to the offline-save and partner one-input check, reporting **Tuesday, September 29, 2026, 2:12 p.m.** Interpreted in the workspace timezone, America/New_York (EDT). This is a student-reported save time, not an independently inspected editor timestamp. Reciprocal unit checking was reported earlier. The originally supplied prediction remains unchanged.


## Actual results appended after confirmation — original prediction unchanged

| Output | Original point prediction | Actual | Actual minus prediction | Original rough range |
| --- | ---: | ---: | ---: | --- |
| FY2031 operating profit, $m | 387.000 | 387.112 | +0.112 | 375–395: inside |
| FY2031 FCFE, $m | 285.000 | 293.993 | +8.993 | 275–295: inside |
| Annual-base value/share, $ | 7.300 | 7.307 | +0.007 | 7.10–7.40: inside |

Machine-calculated FY2031 bridge: +$119.111m operating profit − $27.396m additional cash taxes + $8.906m reduction in annual reserve investment = +$100.621m FCFE (rounding applies). Revenue, gross profit, capex, depreciation, operating NWC and SBC are unchanged in the lower-SG&A case. The reserve balance is $29.778m lower; that is not the same as the one-year reduction in reserve investment.

PV changes: forecast FCFE +$161.388m; post-FY2031 cash flows +$707.398m; NOL and opening excess liquidity changes zero. Total equity gain +$868.785m, divided by 537.037m shares gives +$1.618/share. These numbers are calculation evidence. Student's explanation of prediction error and whether conclusions/research priorities change: pending.


## Student reconciliation supplied after results

The student attributes the FCFE underestimate to the additional reduction in cash-reserve investment, approximately $9m, beyond after-tax operating savings. The executed bridge is +$91.716m after-tax profit plus $8.906m less reserve investment, giving +$100.621m FCFE. This is a reduction relative to the base, not an absolute year-over-year decline in SG&A spending.

The student states that the valuation conclusion and research priority do not change: the favorable SG&A case remains below the dated $12.68 comparison and SG&A efficiency deserves further evidence. The student recognizes that chosen ranges affect rankings and do not imply probabilities. Full original answers and qualifications are recorded in `lab11-uipath-sensitivity.md`; original pre-run estimates above have not been replaced.
