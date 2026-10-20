"""Read-only integrity/preflight checks; never invents missing video evidence."""
import argparse, json, re, sys, hashlib, subprocess, tempfile
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import model

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--submission',action='store_true');args=parser.parse_args()
    errors=[]
    def require(ok,message):
        if not ok: errors.append(message)
    data=model.load(); lineage=json.loads((ROOT/'data/history-lineage.json').read_text())
    for field,row in lineage['rows'].items():
        computed=row['annual']+row['current_half']-row['prior_half']
        require(abs(computed-data['history'][field])<1e-8,'Historical lineage mismatch: '+field)
        for part in ('current','prior'):
            if part+'_components' in row:
                require(abs(sum(row[part+'_components'])-row[part+'_half'])<1e-8,'SG&A components mismatch')
    h=data['history']; reserve=(h['ltm_revenue']-h['ltm_gp']+h['ltm_sga']+h['ltm_rd']-h['ltm_da']-h['ltm_sbc'])/4
    require(abs(reserve-h['opening_reserve'])<1e-8,'Reserve lineage mismatch')
    require(json.loads((ROOT/'reports/results.json').read_text())==model.results(data),'Saved results differ from current engine')
    html=(ROOT/'index.html').read_text()
    match=re.search(r'const DATA=(.*?);function render',html)
    require(bool(match) and json.loads(match.group(1))==model.results(data),'Dashboard differs from engine')
    source=ROOT/'docs/edition-a-supplied-unchanged.md'
    require(hashlib.sha256(source.read_bytes()).hexdigest()=='08085403ab466521316ed4404ac8f5150fb7d132f519531f33eb77853981b60b','Edition A bytes changed')
    human=json.loads((ROOT/'docs/human-change.json').read_text());result=json.loads((ROOT/'reports/human-changed-input-result.json').read_text())
    require(human==result['prediction'],'Prediction differs from original run')
    require(datetime.fromisoformat(human['prediction_written_at']) < datetime.fromisoformat(result['run_at']),'Prediction not before run')
    require(datetime.fromisoformat(result['commit_time'])<=datetime.fromisoformat(result['run_at']),'Commit not before run')
    require((ROOT/'docs/human-change-reconciliation.md').stat().st_size>200,'Missing reconciliation')
    with tempfile.TemporaryDirectory(prefix='path-evidence-check-') as tmp:
        subprocess.run(['git','init','-q',tmp],check=True)
        bundle=ROOT/'reports/human-exercise-history.bundle'
        subprocess.run(['git','fetch','-q',str(bundle),'refs/heads/main:refs/heads/evidence'],cwd=tmp,check=True)
        original=subprocess.check_output(['git','show',result['pre_run_commit']+':docs/human-change.json'],cwd=tmp)
        require(original==(ROOT/'docs/human-change.json').read_bytes(),'Git bundle does not preserve exact prediction')
    # Only current artifacts; legacy lab links are preserved historically, not certified current.
    for p in [ROOT/'README.md',*sorted((ROOT/'docs').glob('*.md'))]:
        if p.name=='edition-a-supplied-unchanged.md':continue
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text()):
            if re.match(r'^[a-z]+:',target) or target.startswith('#'):continue
            require((p.parent/target.split('#')[0]).exists(),f'Broken current local link in {p.name}: {target}')
    for file in ['decision-memo.pdf','research-evolution.pdf','validation-and-ai-use.pdf']:
        require((ROOT/'docs'/file).stat().st_size>1000,'Missing PDF: '+file)
    if args.submission:
        videos=json.loads((ROOT/'docs/video-evidence.json').read_text())
        for video in videos['videos']:
            n=video['number']
            for key in ('url','provider','video_id','title','duration_seconds','evidence_timestamps','access_checked_at','transcript_reviewed'):
                require(bool(video.get(key)),f'Video {n} missing actual {key}')
            if video.get('duration_seconds'):
                require(0<video['duration_seconds']<=(180 if n==1 else 300),f'Video {n} exceeds time limit')
            path=ROOT/f'docs/transcript-video-{n}.txt'
            require(path.exists() and path.stat().st_size>100,f'Missing actual corrected transcript {n}')
        require(bool(videos.get('repository_final_commit')),'Final accessible repository commit not recorded')
        require(bool(videos.get('repository_access_checked_at')),'Repository access check not recorded')
    if errors:
        print('\n'.join('INCOMPLETE: '+x for x in errors));return 1
    print('PASS: historical lineage, saved outputs/dashboard, unchanged Edition A, original human prediction/Git evidence, local links and PDF presence.')
    if not args.submission: print('Pre-recording check only. Videos, transcript accuracy, public access and final submission are NOT certified.')
    return 0

if __name__=='__main__':sys.exit(main())
