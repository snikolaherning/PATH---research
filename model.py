"""UiPath committee model. Python 3.9+, standard library, USD millions.

Five rolling 12-month forecast periods ending October 19, 2027-2031.
Latest reported July balances proxy the October 19 opening position; see
docs/model-method.md for the reporting lag and sensitivities. No live data.
"""
from copy import deepcopy
from math import isfinite
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TOL = 1e-7
ASSETS = ('cash','securities','restricted_cash','receivables','contract_assets',
          'deferred_costs','prepaids','ppe','rou','intangibles','goodwill','dta','other_assets')
LIABS = ('payables','accruals','compensation','deferred_revenue','lease_liabilities',
         'tax_payable','acquisition_payable','equity_withholdings','other_liabilities')
WCA = ('receivables','contract_assets','deferred_costs','prepaids')
WCL = ('payables','accruals','compensation','deferred_revenue')

def load():
    return json.loads((ROOT/'data/inputs.json').read_text())

def total(r, keys):
    return sum(r[k] for k in keys)

def nwc(r):
    return total(r,WCA)-total(r,WCL)

def validate(a):
    for k in ('growth','gm','sga','rd','sbc','capex','dr','amortization'):
        if len(a[k])!=5 or not all(isfinite(x) for x in a[k]):
            raise ValueError(k+': five finite inputs required')
    for k in ('gm','sga','rd','sbc','capex','dr'):
        if any(x<0 or x>1 for x in a[k]): raise ValueError(k+': ratio out of bounds')
    if min(a['growth'])<=-1: raise ValueError('Growth must exceed -100%')
    if not 0<=a['g']<a['wacc']: raise ValueError('Require 0 <= g < WACC')
    if not 0<=a['tax']<=1 or a['shares']<=0: raise ValueError('Tax/share input invalid')
    if not all(isfinite(x) for x in (a['tax'],a['shares'],a['wacc'],a['g'])):
        raise ValueError('Nonfinite scalar input')

def project(a, opening, history):
    validate(a)
    if abs(total(opening,ASSETS)-total(opening,LIABS)-opening['equity'])>TOL:
        raise ValueError('Opening balance sheet does not balance')
    rows=[]; p=deepcopy(opening)
    previous_reserve=history['opening_reserve']
    for i in range(5):
        r=deepcopy(p); r['year']=2027+i
        r['revenue']=p['revenue']*(1+a['growth'][i])
        r['gp']=r['revenue']*a['gm'][i]
        r['cogs']=r['revenue']-r['gp']
        r['sga']=r['gp']*a['sga'][i]
        r['rd']=r['revenue']*a['rd'][i]
        r['ebit']=r['gp']-r['sga']-r['rd']
        r['tax']=max(0,r['ebit'])*a['tax']
        r['ni']=r['ebit']-r['tax']
        r['dep']=p['ppe']*a['depreciation']
        r['amort']=min(p['intangibles'],a['amortization'][i])
        r['ppe']=p['ppe']+r['revenue']*a['capex'][i]-r['dep']
        r['intangibles']=p['intangibles']-r['amort']
        r['capex']=r['revenue']*a['capex'][i]
        r['sbc']=r['revenue']*a['sbc'][i]
        for k in WCA+WCL:
            r[k]=opening[k]*r['revenue']/opening['revenue']
        r['deferred_revenue']=r['revenue']*a['dr'][i]
        r['delta_nwc']=nwc(r)-nwc(p)
        r['cfo']=r['ni']+r['dep']+r['amort']+r['sbc']-r['delta_nwc']
        r['cfi']=-r['capex']
        r['offset_buybacks']=r['sbc']
        r['acquisition_settlement']=p['acquisition_payable'] if i==0 else 0.
        r['acquisition_payable']=p['acquisition_payable']-r['acquisition_settlement']
        r['cff']=-r['offset_buybacks']-r['acquisition_settlement']
        r['cash']=p['cash']+r['cfo']+r['cfi']+r['cff']
        r['equity']=p['equity']+r['ni']+r['sbc']-r['offset_buybacks']
        r['cash_costs']=r['cogs']+r['sga']+r['rd']-r['dep']-r['amort']-r['sbc']
        r['reserve']=r['cash_costs']*a['reserve_months']/12
        r['reserve_investment']=r['reserve']-previous_reserve
        # FCFF keeps SBC as an economic operating cost. Never add it back here.
        # Acquisition obligations are deducted separately in the equity bridge.
        r['fcff']=r['ebit']-r['tax']+r['dep']+r['amort']-r['capex']-r['delta_nwc']-r['reserve_investment']
        r['assets']=total(r,ASSETS); r['liabilities']=total(r,LIABS)
        rows.append(r); p=r; previous_reserve=r['reserve']
    assert_rows(rows,a,opening,history)
    return rows

def row_checks(r,p,previous_reserve):
    return {
        'balance_sheet':total(r,ASSETS)-total(r,LIABS)-r['equity'],
        'cash_flow':r['cash']-p['cash']-r['cfo']-r['cfi']-r['cff'],
        'equity':r['equity']-p['equity']-r['ni']-r['sbc']+r['offset_buybacks'],
        'ppe':r['ppe']-p['ppe']-r['capex']+r['dep'],
        'intangibles':r['intangibles']-p['intangibles']+r['amort'],
        'income':r['ni']-r['ebit']+r['tax'],
        'nwc':r['delta_nwc']-nwc(r)+nwc(p),
        'cfo':r['cfo']-r['ni']-r['dep']-r['amort']-r['sbc']+r['delta_nwc'],
        'cfi':r['cfi']+r['capex'],
        'cff':r['cff']+r['offset_buybacks']+r['acquisition_settlement'],
        'acquisition_claim':r['acquisition_payable']-p['acquisition_payable']+r['acquisition_settlement'],
        'reserve':r['reserve_investment']-r['reserve']+previous_reserve,
        'fcff_operating':r['fcff']-r['ebit']+r['tax']-r['dep']-r['amort']+r['capex']+r['delta_nwc']+r['reserve_investment'],
        'fcff_cash_bridge':r['fcff']-r['cfo']-r['cfi']+r['sbc']+r['reserve_investment'],
        'cash_available_bridge':r['fcff']-r['acquisition_settlement']-(r['cash']-p['cash']-r['reserve_investment']),
        'minimum_cash_shortfall':max(0,r['reserve']-r['cash']),
    }

def assert_rows(rows,a,opening,history):
    validate(a)
    if len(rows)!=5: raise ValueError('Five statement periods required')
    p=opening; reserve=history['opening_reserve']
    for r in rows:
        if any(not isfinite(v) for v in r.values()): raise ValueError('Nonfinite statement value')
        for name,gap in row_checks(r,p,reserve).items():
            if abs(gap)>TOL: raise ValueError(f"{r['year']} {name}: {gap:.9f}")
        if min(r[k] for k in ASSETS+LIABS)<-TOL: raise ValueError('Negative balance')
        p=r; reserve=r['reserve']

def value(rows,a,opening,history):
    assert_rows(rows,a,opening,history)
    w,g=a['wacc'],a['g']; last=rows[-1]
    pv_explicit=sum(r['fcff']/(1+w)**(i+1) for i,r in enumerate(rows))
    # Finite intangible amortization runs out. PP&E/NWC/reserve converge before
    # a Gordon tail; no perpetual addback of a finite acquired asset.
    revenue=last['revenue']; ppe=last['ppe']; intangible=last['intangibles']
    wc=nwc(last); reserve=last['reserve']; pv_terminal=0.; first=None
    for year in range(6,206):
        revenue*=1+g
        ebit=revenue*(a['gm'][-1]*(1-a['sga'][-1])-a['rd'][-1])
        dep=ppe*a['depreciation']; capex=revenue*a['capex'][-1]
        amort=min(intangible,a['amortization'][-1]); intangible-=amort
        ppe+=capex-dep; next_wc=wc*(1+g)
        next_reserve=(revenue-ebit-dep-amort-revenue*a['sbc'][-1])*a['reserve_months']/12
        cf=ebit-max(0,ebit)*a['tax']+dep+amort-capex-(next_wc-wc)-(next_reserve-reserve)
        if first is None: first=cf
        pv_terminal+=cf/(1+w)**year
        wc=next_wc; reserve=next_reserve
    if cf<=0: raise ValueError('Nonpositive sustainable terminal FCFF')
    pv_terminal+=cf*(1+g)/(w-g)/(1+w)**205
    ev=pv_explicit+pv_terminal
    excess=opening['cash']+opening['securities']-history['opening_reserve']
    # Deduct at face value, not again inside FCFF; timing conservatism disclosed.
    claim=opening['acquisition_payable']
    equity=ev+excess-claim
    return dict(ev=ev,equity=equity,per_share=equity/a['shares'],
                pv_explicit=pv_explicit,pv_terminal=pv_terminal,
                terminal_share=pv_terminal/ev,terminal_first_fcff=first,
                excess_cash=excess,acquisition_claim=claim,funded_debt=0.)

def assumptions(data,case='base'):
    a=deepcopy(data['assumptions']); a.update(deepcopy(data['scenarios'][case])); return a

def run(data,case='base',override=None):
    a=assumptions(data,case)
    if override: a.update(override)
    rows=project(a,data['opening'],data['history'])
    return a,rows,value(rows,a,data['opening'],data['history'])

def reverse_sga(data):
    """Market-implied final SG&A/GP; linear five-year path, all else base."""
    lo,hi=.30,.70; target=data['market']['PATH']['price']
    def calc(end):
        path=[.65+(.25*i)*(end-.65) for i in range(5)]
        return run(data,override={'sga':path})[2]['per_share']
    # Upper endpoint can have nonpositive going-concern cash flows. Restrict it
    # to the base endpoint, whose valuation must be below market for this solve.
    hi=assumptions(data)['sga'][-1]
    if not calc(hi)<=target<=calc(lo): return {'status':'not bracketed'}
    for _ in range(100):
        mid=(lo+hi)/2; v=calc(mid)
        if v>target: lo=mid
        else: hi=mid
    end=(lo+hi)/2
    return {'status':'solved','year5_sga_gp':end,'price':calc(end),
            'description':'Only SG&A/GP path changes linearly from 65%; not an ARR forecast.'}

def comps(data):
    t,p=data['market']['PATH'],data['market']['PEGA']
    def ev(x): return x['price']*x['shares']+x['funded_debt']-x['cash_securities']
    peer_ev_sales=ev(p)/p['ltm_revenue']; target_ev_sales=ev(t)/t['ltm_revenue']
    peer_pe=p['price']/p['annual_diluted_eps']; target_pe=t['price']/t['annual_diluted_eps']
    return dict(peer_ev_sales=peer_ev_sales,target_ev_sales=target_ev_sales,
                peer_pe=peer_pe,target_pe=target_pe,
                implied_ev_sales_price=(peer_ev_sales*t['ltm_revenue']+t['cash_securities']-t['funded_debt'])/t['shares'],
                implied_pe_price=peer_pe*t['annual_diluted_eps'],
                note='Single qualified peer; no mechanical averaging. EV deducts all liquid financial assets in both firms; DCF deducts only excess cash.')

def results(data):
    cases={}
    for name in data['scenarios']:
        a,rows,v=run(data,name)
        cases[name]={'assumptions':a,'statements':rows,'valuation':v}
    grid=[]
    for w in (.09,.10,.11,.12,.13):
        grid.append({'wacc':w,'values':[run(data,override={'wacc':w,'g':g})[2]['per_share'] for g in (.02,.03,.04)]})
    return {'metadata':data['metadata'],'cases':cases,'wacc_growth':grid,
            'reverse_dcf':reverse_sga(data),'comps':comps(data)}

if __name__=='__main__':
    print(json.dumps(results(load()),indent=2))
