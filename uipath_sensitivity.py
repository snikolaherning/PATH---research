"""Lab 11 one-at-a-time sensitivity; standard library only.
Keep beside the unchanged Lab 10 uipath_proforma.py.
Run: python3 uipath_sensitivity.py
Writes visible report and full statements/input/check audit beside this file.
Ranges were selected by the student before the locked prediction was run.
"""
from copy import deepcopy
from pathlib import Path
from math import isclose
import hashlib
import json
import uipath_proforma as model

ROOT = Path(__file__).resolve().parent
BASE = deepcopy(model.A)
OPENING = deepcopy(model.OPENING)
TOL = 1e-7  # USD millions; also used for per-share comparison, in USD.
RANGES = {
    'sga': {
        'label': 'SG&A / gross profit', 'units': '% of gross profit',
        'lower': (.65, .62, .59, .56, .53),
        'base': (.65, .635, .62, .605, .59),
        'higher': (.65, .65, .65, .65, .65)},
    'growth': {
        'label': 'Revenue growth', 'units': 'annual % revenue growth',
        'lower': (.102, .08, .07, .06, .05),
        'base': (.112, .10, .09, .08, .07),
        'higher': (.122, .12, .11, .10, .09)},
}
OUTPUTS = ('operating_profit_m', 'fcfe_m', 'value_per_share')


def same(a, b):
    """Recursive comparison for every statement/input, not just printed outputs."""
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, (list, tuple)):
        return len(a) == len(b) and all(same(x,y) for x,y in zip(a,b))
    if isinstance(a, (float,int)):
        return isclose(a,b,rel_tol=0.,abs_tol=TOL)
    return a == b


def run(driver=None, case='base'):
    a=deepcopy(BASE)
    if driver:
        a[driver]=tuple(RANGES[driver][case])
    changed=[k for k in BASE if a[k]!=BASE[k]]
    expected=[] if driver is None or case=='base' else [driver]
    if changed != expected:
        raise AssertionError(f'One-input isolation failed: {changed} vs {expected}')
    prior_inputs=deepcopy(a)
    # Legacy engine reads its opening state from a global. Give every run its
    # own independent copy, restoring the original object even after failure.
    original_opening=model.OPENING
    model.OPENING=deepcopy(OPENING)
    result=dict(driver=driver,case=case,assumptions=deepcopy(a),
        opening=deepcopy(OPENING),changed_independent_inputs=changed,
        status='invalid',outputs={k:None for k in OUTPUTS},statements=[],checks=[])
    try:
        rows=model.project(a)
        model.assert_valid(rows,a)
        p=model.OPENING
        for r in rows:
            c=model.checks(r,p,a)
            if any(abs(x)>TOL for x in c.values()):
                raise ValueError(f"FY{r['year']} accounting check failed")
            result['checks'].append(dict(year=r['year'],residuals=c))
            p=r
        result['statements']=deepcopy(rows)
        result['outputs']['operating_profit_m']=rows[-1]['ebit']
        result['outputs']['fcfe_m']=rows[-1]['fcfe']
        result['status']='accounting valid; value unavailable'
        try:
            valuation=model.value(rows,a)
            result['valuation']=valuation
            result['outputs']['value_per_share']=valuation['value_per_share']
            result['status']='valid (qualified annual-base value)'
        except ValueError as error:
            result['valuation_error']=str(error)
        result['negative_fcfe_years']=[r['year'] for r in rows if r['fcfe']<0]
    except ValueError as error:
        result['error']=str(error)
    finally:
        if a != prior_inputs:
            raise AssertionError('Engine mutated scenario assumptions')
        if model.OPENING != OPENING:
            raise AssertionError('Engine mutated opening inputs')
        model.OPENING=original_opening
    return result


def fmt(x, signed=False, digits=3):
    if x is None: return 'N/A'
    return f'{x:+,.{digits}f}' if signed else f'{x:,.{digits}f}'


def execute():
    for driver in RANGES:
        if tuple(BASE[driver]) != RANGES[driver]['base']:
            raise AssertionError(f'{driver}: saved range base differs from Lab 10')
    initial=run()
    if initial['outputs']['operating_profit_m'] is None:
        raise ValueError('Base accounting failed; do not run/rank sensitivities')
    # If a saved snapshot accompanies the files, verify it before any changes.
    snapshot_path=ROOT/'lab11-base-inputs.json'
    if snapshot_path.exists():
        snapshot=json.loads(snapshot_path.read_text())
        if not same(snapshot['assumptions'], BASE) or not same(snapshot['opening'], OPENING):
            raise AssertionError('Saved pre-run base inputs differ')
        digest=hashlib.sha256((ROOT/'uipath_proforma.py').read_bytes()).hexdigest()
        if digest != snapshot['model_sha256']:
            raise AssertionError('Lab 10 source changed since the base snapshot')
        for key,old_key in [('operating_profit_m','operating_profit_usd_m'),
                            ('fcfe_m','fcfe_usd_m'),
                            ('value_per_share','annual_base_value_per_share')]:
            if not same(initial['outputs'][key],snapshot['base_outputs'][old_key]):
                raise AssertionError('Saved output differs: '+key)
    scenarios=[]
    for driver in RANGES:
        for case in ('lower','base','higher'):
            r=run(driver,case)
            r['changes_from_base']={k:(None if r['outputs'][k] is None or initial['outputs'][k] is None
                else r['outputs'][k]-initial['outputs'][k]) for k in OUTPUTS}
            if case=='base' and not same(r['statements'],initial['statements']):
                raise AssertionError('Driver base does not match original base')
            scenarios.append(r)
    restored=run()
    if not same(initial,restored) or model.A!=BASE or model.OPENING!=OPENING:
        raise AssertionError('Restored base differs or module inputs mutated')
    spans={}
    for driver in RANGES:
        group=[r for r in scenarios if r['driver']==driver]
        spans[driver]={}
        for k in OUTPUTS:
            vals=[r['outputs'][k] for r in group if r['outputs'][k] is not None]
            spans[driver][k]={'span':max(vals)-min(vals) if vals else None,
                'valid_count':len(vals),'ranking_eligible':len(vals)==3}
    return dict(base=initial,scenarios=scenarios,restored=restored,
        spans=spans,restored_base_pass=True,tolerance=TOL)


def report(audit):
    b=audit['base']; cases=audit['scenarios']
    lines=['# Lab 11 — UiPath sensitivity results','',
        'Ranges supplied by student; one independent input path changed per run.',
        'Years: FY2027–FY2031. Profit and FCFE: USD millions; value/share: USD.',
        'FCFE retains negative cash flows and the Lab 10 dilution-offset and cash-reserve conventions.',
        'Value is conditional on the unchanged Lab 10 annual-base assumptions and disclosed limitations; it is not a September 29 price target.',
        'Lower/higher describe the input, not a better/worse outcome. All other independent inputs, including 11% cost of equity and 3% terminal growth, stay at base.','',
        '## Actual input paths','',
        '| Driver | Case | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 | Units |',
        '| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |']
    for r in cases:
        d=r['driver']; vals=r['assumptions'][d]
        lines.append('| '+RANGES[d]['label']+' | '+r['case']+' | '+' | '.join(f'{x*100:g}%' for x in vals)+' | '+RANGES[d]['units']+' |')
    lines+=['','## Comparable outputs and signed changes from base','',
        '| Driver | Case | FY2031 operating profit | Change | FY2031 FCFE | Change | Value/share | Change | Status |',
        '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |']
    for r in cases:
        out=r['outputs']; diff=r['changes_from_base']; cells=[]
        for k in OUTPUTS: cells += [fmt(out[k]),fmt(diff[k],True)]
        lines.append('| '+RANGES[r['driver']]['label']+' | '+r['case']+' | '+' | '.join(cells)+' | '+r['status']+' |')
        if 'error' in r: lines.append('\nInvalid run: '+r['error'])
        if 'valuation_error' in r: lines.append('\nValue unavailable: '+r['valuation_error'])
    lines+=['','## Spans: maximum minus minimum over the stated ranges','',
        '| Driver | Profit span, $m | FCFE span, $m | Value/share span, $ |',
        '| --- | ---: | ---: | ---: |']
    for d in RANGES:
        cells=[]
        for k in OUTPUTS:
            x=audit['spans'][d][k]
            cells.append(fmt(x['span'])+(' (incomplete; do not rank)' if not x['ranking_eligible'] else ''))
        lines.append('| '+RANGES[d]['label']+' | '+' | '.join(cells)+' |')
    lines+=['','## Accounting and isolation checks','',
        'Each figure is the largest absolute residual/shortfall across ALL printed checks for that year. Full named checks are retained in the JSON audit. Tolerance: 1e-7.','',
        '| Driver / case | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 | Changed independent inputs |',
        '| --- | ---: | ---: | ---: | ---: | ---: | --- |']
    for r in cases:
        cells=[]
        for c in r['checks']:
            x=max(abs(v) for v in c['residuals'].values())
            cells.append(f'{0. if x<TOL else x:.6f}')
        cells+=['N/A']*(5-len(cells))
        lines.append('| '+RANGES[r['driver']]['label']+' / '+r['case']+' | '+' | '.join(cells)+' | '+(', '.join(r['changed_independent_inputs']) or 'none')+' |')
    for r in cases:
        if r.get('negative_fcfe_years'):
            lines.append('\nNegative FCFE retained in '+r['driver']+'/'+r['case']+': '+', '.join('FY'+str(x) for x in r['negative_fcfe_years'])+'.')
    lines+=['','**Restored base: PASS.** All inputs, all five years of statements, checks, and valuation outputs match the initial run within the stated absolute tolerance. Lab 10 source and module inputs are unchanged.','',
        '## Selected lower-SG&A trace','',
        'Base versus changed, by year. This is calculation evidence for the student to interpret, not a replacement for the student explanation.','',
        '| Year | Gross profit (unchanged) | Base SG&A | Changed SG&A | Profit change | Cash-tax change | Reserve change vs base | Change in annual reserve investment | FCFE change |',
        '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    chosen=next(r for r in cases if r['driver']=='sga' and r['case']=='lower')
    if chosen['statements']:
        for old,new in zip(b['statements'],chosen['statements']):
            cells=[fmt(old['gp']),fmt(old['sga']),fmt(new['sga'])]+[fmt(new[k]-old[k],True) for k in ('ebit','cash_tax','reserve','reserve_investment','fcfe')]
            lines.append('| FY'+str(new['year'])+' | '+' | '.join(cells)+' |')
        lines+=['','### Locked prediction versus actual','',
            '| Output | Predicted | Actual | Actual minus predicted | Inside rough range? |',
            '| --- | ---: | ---: | ---: | --- |']
        predictions={'operating_profit_m':(387.,375.,395.),'fcfe_m':(285.,275.,295.),'value_per_share':(7.30,7.10,7.40)}
        for k,(pred,lo,hi) in predictions.items():
            act=chosen['outputs'][k]
            lines.append('| '+k+' | '+fmt(pred)+' | '+fmt(act)+' | '+fmt(None if act is None else act-pred,True)+' | '+('N/A' if act is None else 'Yes' if lo<=act<=hi else 'No')+' |')
        if 'valuation' in chosen and 'valuation' in b:
            lines+=['','### Present-value change components, $m','']
            for k in ('pv_explicit','pv_terminal','pv_nol','opening_excess','equity'):
                lines.append(f"- {k}: {chosen['valuation'][k]-b['valuation'][k]:+.6f}")
    lines+=['','## Student follow-up (not written by AI)','',
        'Recompute a changed-minus-base difference with your partner. Explain the prediction error and statement links. State which driver has the larger span OVER THESE RANGES, why the range choice matters, and what to research using impact and uncertainty. Record both directions of partner checks and the question/response. State whether your valuation conclusion or research priority changes, and why.','']
    return '\n'.join(lines)


def main():
    audit=execute()
    text=report(audit)
    (ROOT/'lab11-sensitivity-results.md').write_text(text)
    (ROOT/'lab11-sensitivity-audit.json').write_text(json.dumps(audit,indent=2,allow_nan=False)+'\n')
    print(text)

if __name__=='__main__':
    main()
