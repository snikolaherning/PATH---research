"""Student-only execution aid. Close generative AI before the prediction/run.

Reads a student-created docs/human-change.json committed before execution.
Never supplies or fills in the student's prediction or reasoning.
"""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
import model

ROOT=Path(__file__).resolve().parent

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()

def main():
    path=ROOT/'docs/human-change.json'
    if not path.exists(): raise SystemExit('First create and commit your own human-change.json with AI closed. Read docs/student-only-validation.md.')
    if git('status','--porcelain'):
        raise SystemExit('Working tree must be clean: commit the prediction and exact model/input files before execution.')
    git('ls-files','--error-unmatch','docs/human-change.json')
    record=json.loads(path.read_text())
    required=('author','prediction_written_at','field','old_value','new_value','units','expected_direction','expected_decision_effect','causal_reason','ai_closed_attestation')
    if any(k not in record or record[k] in ('',None) for k in required):
        raise SystemExit('Missing student-authored record fields; no run performed.')
    if record['ai_closed_attestation'] is not True: raise SystemExit('AI-closed attestation missing.')
    d=model.load(); a=model.assumptions(d)
    key=record['field']
    if key not in a: raise SystemExit('Unknown assumption field.')
    if a[key]!=record['old_value']: raise SystemExit('Old value does not match the committed base input.')
    if record['new_value']==record['old_value']: raise SystemExit('Input must change.')
    commit=git('rev-parse','HEAD'); commit_time=git('show','-s','--format=%cI','HEAD')
    baseline=model.run(d)[2]
    changed=model.run(d,override={key:record['new_value']})[2]
    result={'run_at':datetime.now(timezone.utc).isoformat(),'pre_run_commit':commit,
            'commit_time':commit_time,'prediction':record,'baseline':baseline,'changed':changed,
            'actual_value_change':changed['per_share']-baseline['per_share'],
            'student_reconciliation':'Not supplied. Student must append actual direction, decision effect and failure diagnosis/no-change reason after inspecting output.'}
    out=ROOT/'reports/human-changed-input-result.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('Preserve original prediction. Add your own reconciliation, then commit the result.')

if __name__=='__main__': main()
