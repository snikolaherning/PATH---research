# Student-only changed-input exercise

Status: COMPLETED October 19; see human-change.json, human-change-reconciliation.md and the reports evidence. The instructions below are preserved as the procedure used. This page provides process instructions, not your financial prediction. The required prediction and execution are AI closed under the shared submission architecture. Do not describe the ordinary AI-assisted tests as this exercise.

1. Review and approve the final model first. Put these files in your Git working copy and commit the baseline. Confirm normal `python3 run.py` works before the separate exercise.
2. Close generative AI. Independently choose one material model assumption, exact old and new values and units. Write your predicted output direction, expected decision effect and causal reasoning before running it. The existing input names and values are in `data/inputs.json`.
3. Save `docs/human-change.json` using the field names below. All content inside the fields must be yours. `old_value` and `new_value` must be JSON numbers or five-number arrays matching the assumption's type. Do not put percent signs in numeric fields; ratios use decimals.

```json
{
  "author": "",
  "prediction_written_at": "",
  "field": "",
  "old_value": null,
  "new_value": null,
  "units": "",
  "expected_direction": "",
  "expected_decision_effect": "",
  "causal_reason": "",
  "ai_closed_attestation": false
}
```

4. Enter a real timestamp with time zone, set the attestation truthfully, and commit the prediction **before** execution. Commit identity is your existing Git configuration. Do not backdate or claim an earlier timestamp.

```bash
git add docs/human-change.json
git commit -m "Record my AI-off prediction before changed-input run"
git status --short
python3 locked_run.py
```

The runner requires a clean working tree. It records the exact pre-run commit, commit time, unchanged prediction and old/new results. It does not verify that AI was actually closed; only you can truthfully attest to that process. If the input makes the model invalid, preserve the refusal output and diagnose it rather than silently choosing a successful result.

5. Still with AI closed, save `docs/human-change-reconciliation.md`: compare predicted versus actual direction; explain the financial mechanism and any error; state actual committee effect; explain if the action is unchanged. Preserve both outputs and your original prediction. Commit the results afterward.
6. After the exercise, those genuine records can be included in the validation PDF. Do not paste an AI-authored replacement into the original prediction.

The prior Lab 11 note remains historical evidence. Its final repository upload includes results and pre-run AI commentary, and does not independently establish the final assignment's pre-run commit/AI-closed requirements. A new properly recorded exercise avoids representing uncertain history as proven compliance.
