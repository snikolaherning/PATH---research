"""Mechanical capture only: student supplies every prediction and explanation."""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
import model

ROOT = Path(__file__).resolve().parent

def ask(question):
    while True:
        answer = input(question + '\n> ').strip()
        if answer:
            return answer
        print('Please enter your own answer.')

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()

def commit(author, message, paths):
    git('add', '--', *paths)
    # Local metadata only, not an email address supplied by the student.
    git('-c', 'user.name=' + author, '-c', 'user.email=ai-off-exercise@localhost',
        'commit', '-m', message)

def main():
    if '--check' in sys.argv:
        model.run(model.load())
        assert (ROOT / '.git').is_dir()
        print('Setup check passed. No student prediction or changed-input test created.')
        return
    print('\nYOUR INDEPENDENT CHANGED-INPUT EXERCISE\n')
    print('Close this AI chat and all other generative AI tools before continuing.')
    print('This program only saves your answers and runs calculations. It does not generate reasoning.')
    print('Keep this Terminal window open until both parts are finished.')
    if ask('Have you closed generative AI and are you ready to answer independently? Type YES.') != 'YES':
        print('Stopped. Close AI first, then reopen this launcher.'); return
    if (ROOT/'docs/human-change.json').exists():
        print('A prediction already exists. Stopped to preserve it. Do not overwrite earlier evidence.'); return
    if git('status','--porcelain'):
        print('Setup has uncommitted changes. Stopped before collecting your prediction.'); return
    author = ask('Your full name:')
    a = model.assumptions(model.load())
    labels = {'growth':'Revenue growth, five years', 'gm':'Gross margin, five years',
              'sga':'SG&A / gross profit, five years', 'rd':'R&D / revenue, five years',
              'wacc':'Discount rate', 'g':'Terminal growth rate'}
    print('\nExisting assumptions (decimals: 0.11 means 11%):')
    for k,label in labels.items(): print(k, '|', label, '|', json.dumps(a[k]))
    while True:
        field=ask('Choose ONE assumption. Type its exact field name from the list:')
        if field in labels: break
        print('Use a field name displayed above.')
    print('Original value:', json.dumps(a[field]))
    print('For a five-year path, use [number, number, number, number, number].')
    while True:
        raw=ask('Enter your independently chosen NEW value, using decimals and no percent signs:')
        try:
            new=json.loads(raw)
            if isinstance(a[field],list):
                assert isinstance(new,list) and len(new)==5 and all(type(x) in (int,float) for x in new)
            else: assert type(new) in (int,float)
            assert new != a[field]
            break
        except (ValueError,AssertionError): print('Enter a different numeric value, or five-number array matching the original format.')
    units=ask('State the units of this assumption:')
    meaningful=ask('Why is this change meaningful to investigate?')
    direction=ask('Before calculating: do you predict value per share will increase, decrease, or stay approximately unchanged?')
    reason=ask('Explain your own financial reasoning for that prediction:')
    effect=ask('Do you expect the do-not-initiate recommendation to change or remain unchanged, and WHY?')
    record={'author':author,'prediction_written_at':datetime.now().astimezone().isoformat(),
            'field':field,'old_value':a[field],'new_value':new,'units':units,
            'expected_direction':direction,'expected_decision_effect':effect,
            'causal_reason':reason,'why_material':meaningful,'ai_closed_attestation':True}
    print('\nYOUR PREDICTION — NO CHANGED-INPUT CALCULATION HAS RUN:\n'+json.dumps(record,indent=2))
    if ask('Type SAVE to lock these answers and run the test, or anything else to stop:')!='SAVE':
        print('Stopped without running. No prediction saved.'); return
    (ROOT/'docs/human-change.json').write_text(json.dumps(record,indent=2)+'\n')
    commit(author,'Save student-authored AI-off prediction BEFORE execution',['docs/human-change.json'])
    pre=git('rev-parse','HEAD')
    print('\nPrediction saved and committed:',pre)
    print('Running the test now. Keep AI closed.\n')
    result=subprocess.run([sys.executable,'locked_run.py'],cwd=ROOT,text=True,capture_output=True)
    print(result.stdout)
    if result.stderr: print(result.stderr)
    (ROOT/'reports/human-run-console.txt').write_text(result.stdout+result.stderr)
    answers=[]
    if result.returncode==0:
        out=json.loads((ROOT/'reports/human-changed-input-result.json').read_text())
        print('\nRESULTS:')
        print('Baseline value/share:',out['baseline']['per_share'])
        print('Changed value/share:',out['changed']['per_share'])
        print('Difference:',out['actual_value_change'])
    else:
        print('The run failed or refused the input. The error has been preserved; explain it below.')
    print('\nPART 2: Your own interpretation, still with AI closed.')
    for q in ['What was the actual direction and size of the change (or what error occurred)?',
              'Did the result match your prediction?',
              'Explain the financial mechanism behind the result or mismatch.',
              'What is your recommendation after the test, and why did it change or stay the same?',
              'Describe any error, unexpected behavior, or limitation. Write None if none occurred.']:
        answers.append((q,ask(q)))
    if ask('Did you complete BOTH parts and the test with generative AI closed? Type YES only if true.')!='YES':
        attestation='Student did not confirm AI remained closed throughout; do not certify this exercise.'
    else: attestation='Student confirms both parts and execution completed with generative AI closed.'
    text='# Student reconciliation\n\nAuthor: '+author+'\n\nCompleted: '+datetime.now().astimezone().isoformat()+'\n\nPre-run commit: '+pre+'\n\n'+attestation+'\n'
    for q,answer in answers: text+='\n## '+q+'\n\n'+answer+'\n'
    (ROOT/'docs/human-change-reconciliation.md').write_text(text)
    paths=['docs/human-change-reconciliation.md','reports/human-run-console.txt']
    if (ROOT/'reports/human-changed-input-result.json').exists(): paths.append('reports/human-changed-input-result.json')
    commit(author,'Save actual result and student AI-off reconciliation AFTER execution',paths)
    print('\nDONE. Your original prediction, results and explanation are saved locally.')
    print('You may now reopen AI and say: I finished the exercise. Please inspect the AI-off-exercise folder.')
    print('Nothing was uploaded or submitted. Local commit email is a documented placeholder, not your contact address.')

if __name__=='__main__':
    try: main()
    except (KeyboardInterrupt, EOFError): print('\nStopped. Preserve any files already saved; do not overwrite a committed prediction.')
    except Exception as exc:
        print('\nStopped:',exc)
        print('Preserve this window and existing files. Do not erase evidence or claim completion.')
    if '--check' not in sys.argv:
        try: input('\nPress Return to close this window.')
        except (KeyboardInterrupt,EOFError): pass
