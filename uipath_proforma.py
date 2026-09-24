"""Lab 10 UiPath annual-base teaching model (USD millions).
Run: python3 uipath_proforma.py --test
Sources, student judgments and provisional simplifications: lab10-uipath-proforma.md.
Not a current-date investment valuation: starts January 31, 2026 using later
forecast information. Tax utilization and settlement timing are judgment proxies.
"""
from copy import deepcopy
from math import isfinite
import argparse

TOL = 1e-7
# History: FY2026 10-K p.78; current and non-current balances aggregated.
OPENING = dict(year=2026, revenue=1610.572, cash=871.157,
    securities=818.319, restricted_cash=.438, receivables=488.265,
    contract_assets=94.386, deferred_costs=238.447, prepaids=105.577,
    ppe=46.014, rou=64.472, intangibles=19.989, goodwill=125.310,
    dta=233.401, other_assets=73.425, payables=10.161,
    accruals=117.882, compensation=121.029, deferred_revenue=707.305,
    lease_liabilities=81.246, tax_payable=14.784, acquisition_payable=9.532,
    repurchase_payable=10.015, equity_withholdings=7.977,
    other_liabilities=16.682, equity=2082.587, acquired_other_liabilities=0., workfusion_payable=0.,
    nol=662.4)
ASSETS = ('cash','securities','restricted_cash','receivables','contract_assets',
    'deferred_costs','prepaids','ppe','rou','intangibles','goodwill','dta',
    'other_assets')
LIABILITIES = ('payables','accruals','compensation','deferred_revenue',
    'lease_liabilities','tax_payable','acquisition_payable',
    'repurchase_payable','equity_withholdings','other_liabilities',
    'acquired_other_liabilities','workfusion_payable')
WC_ASSETS = ('receivables','contract_assets','deferred_costs','prepaids')
WC_LIABS = ('payables','accruals','compensation','deferred_revenue')
# Student judgments except FY27 growth (guidance-derived).
A = dict(growth=(.112,.10,.09,.08,.07), gm=(.82,.81,.805,.80,.80),
    sga=(.65,.635,.62,.605,.59), rd=(.24,.235,.23,.225,.22),
    sbc=(.16,.145,.13,.12,.11), capex=(.012,.011,.01,.01,.01),
    dr=(.43,)*5, depreciation=.18, tax=.23, reserve_months=3.,
    ke=.11, g=.03, shares=537.037,
    # July 2026 10-Q Note 7 schedule plus rounded H1 actual $10.6m for FY27.
    amortization=(22.425,22.896,18.320,17.120,15.953),
    # AI implementation judgments, pending student review:
    # Conservative aggregate NOL proxy; NOT a legal limit on all NOL vintages.
    nol_annual_cap=29., federal_rate=.21, nol_income_limit=.8,
    acquisition_cash=149.403, acquisition_settlement=9.532,
    acquired_intangibles=92.4, acquired_dta=30.436, acquired_goodwill=58.157,
    acquired_other_liabilities=2.023, workfusion_payable=29.567,
    # Existing repurchase payable is an opening financing obligation.
    repurchase_settlement=10.015)


def total(row, keys):
    return sum(row[k] for k in keys)


def nwc(row):
    return total(row, WC_ASSETS) - total(row, WC_LIABS)


def validate_inputs(a):
    for k in ('growth','gm','sga','rd','sbc','capex','dr','amortization'):
        if len(a[k]) != 5 or not all(isfinite(x) for x in a[k]):
            raise ValueError(f'{k}: require five finite inputs')
    if any(not isfinite(v) for v in a.values() if isinstance(v, (int,float))):
        raise ValueError('Non-finite assumption')
    if not 0 <= a['g'] < a['ke'] or a['shares'] <= 0:
        raise ValueError('Require 0 <= terminal growth < cost of equity; shares > 0')
    for k in ('gm','sga','rd','sbc','capex','dr'):
        if any(not 0 <= x <= 1 for x in a[k]):
            raise ValueError(f'{k}: ratios must lie between zero and one')
    if min(a['growth']) <= -1 or not 0 <= a['depreciation'] <= 1:
        raise ValueError('Invalid growth or depreciation')
    if not 0 <= a['tax'] <= 1 or not 0 <= a['nol_income_limit'] <= 1:
        raise ValueError('Invalid tax inputs')
    if any(a[k] < 0 for k in ('reserve_months','nol_annual_cap','federal_rate',
        'acquisition_cash','acquisition_settlement','repurchase_settlement')):
        raise ValueError('Negative cash policy or tax input')


def opening_reserve(a):
    # Cash cost proxy includes COGS + SG&A + R&D, less D&A and SBC.
    return (270.984 + 897.620 + 385.208 - 16.969 - 290.676)*a['reserve_months']/12


def checks(r, p, a):
    prior_reserve=opening_reserve(a) if p['year']==2026 else p['reserve']
    return {
        'balance gap': total(r, ASSETS)-total(r, LIABILITIES)-r['equity'],
        'cash flow gap': r['cash']-p['cash']-r['cfo']-r['cfi']-r['cff'],
        'equity rollforward gap': r['equity']-p['equity']-r['ni']-r['sbc']
            +r['offset_buybacks'],
        'PPE rollforward gap': r['ppe']-p['ppe']-r['capex']+r['dep'],
        'tax bridge gap': r['tax_expense']-r['cash_tax']-r['tax_shield'],
        'DTA rollforward gap': r['dta']-p['dta']+r['tax_shield']-r['dta_acquired'],
        'DR cash effect gap': r['dr_cash']-r['deferred_revenue']+p['deferred_revenue'],
        'minimum cash shortfall': max(0.,r['reserve']-r['cash']),
        'net income gap': r['ni']-r['pretax']+r['tax_expense'],
        'NWC change gap': r['delta_nwc']-nwc(r)+nwc(p),
        'CFO bridge gap': r['cfo']-r['ni']-r['dep']-r['amort']-r['sbc']-r['tax_shield']+r['delta_nwc'],
        'CFI bridge gap': r['cfi']+r['capex']+r['acquisition_cash'],
        'CFF bridge gap': r['cff']+r['offset_buybacks']+r['acquisition_settlement']+r['repurchase_settlement']+r['workfusion_settlement'],
        'reserve change gap': r['reserve_investment']-r['reserve']+prior_reserve,
        'FCFE bridge gap': r['fcfe']-r['cfo']-r['cfi']-r['cff']+r['reserve_investment'],
        'NOL rollforward gap': r['nol']-p['nol']+r['nol_used'],
        'intangible rollforward gap': r['intangibles']-p['intangibles']+r['amort']-(a['acquired_intangibles'] if r['year']==2027 else 0.),
    }


def assert_valid(rows,a=A):
    validate_inputs(a)
    if len(rows)!=5 or [r['year'] for r in rows] != list(range(2027,2032)):
        raise ValueError('Require FY2027–FY2031 statements')
    p=OPENING
    if abs(total(p,ASSETS)-total(p,LIABILITIES)-p['equity'])>TOL:
        raise ValueError('Opening balance sheet does not balance')
    for r in rows:
        if any(not isfinite(v) for v in r.values()):
            raise ValueError(f"FY{r['year']}: non-finite statement value")
        for key,gap in checks(r,p,a).items():
            if abs(gap)>TOL:
                raise ValueError(f"FY{r['year']}: {key} = {gap:+.6f}")
        if min(r[k] for k in ASSETS+LIABILITIES+('nol',)) < -TOL:
            raise ValueError(f"FY{r['year']}: negative asset/liability balance")
        p=r


def project(a=A):
    validate_inputs(a)
    rows=[]
    p=OPENING
    prior_reserve=opening_reserve(a)
    for i in range(5):
        r=dict(p,year=2027+i)
        r['revenue']=p['revenue']*(1+a['growth'][i])
        r['gp']=r['revenue']*a['gm'][i]
        r['cogs']=r['revenue']-r['gp']
        r['sga']=r['gp']*a['sga'][i]
        r['rd']=r['revenue']*a['rd'][i]
        r['ebit']=r['gp']-r['sga']-r['rd']
        # Financial assets valued separately: no investment income capitalized.
        r['pretax']=r['ebit']
        r['tax_expense']=max(0.,r['pretax'])*a['tax']
        r['nol_used']=min(p['nol'],a['nol_annual_cap'],
            max(0.,r['pretax'])*a['nol_income_limit'])
        r['tax_shield']=min(r['tax_expense'],p['dta'],r['nol_used']*a['federal_rate'])
        r['nol_used']=r['tax_shield']/a['federal_rate'] if a['federal_rate'] else 0.
        r['nol']=p['nol']-r['nol_used']
        r['dta_acquired']=a['acquired_dta'] if i==0 else 0.
        r['dta']=p['dta']-r['tax_shield']+r['dta_acquired']
        r['cash_tax']=r['tax_expense']-r['tax_shield']
        r['ni']=r['pretax']-r['tax_expense']
        r['dep']=p['ppe']*a['depreciation']
        added_intangibles=a['acquired_intangibles'] if i==0 else 0.
        r['amort']=min(p['intangibles']+added_intangibles,a['amortization'][i])
        r['intangibles']=p['intangibles']+added_intangibles-r['amort']
        r['capex']=r['revenue']*a['capex'][i]
        r['ppe']=p['ppe']+r['capex']-r['dep']
        r['sbc']=r['revenue']*a['sbc'][i]
        for k in WC_ASSETS+WC_LIABS:
            r[k]=OPENING[k]*r['revenue']/OPENING['revenue']
        r['deferred_revenue']=r['revenue']*a['dr'][i]
        r['dr_cash']=r['deferred_revenue']-p['deferred_revenue']
        r['delta_nwc']=nwc(r)-nwc(p)
        # Net deferred-cost balance changes already incorporate amortization.
        # No second add-back of commission amortization.
        r['cfo']=r['ni']+r['dep']+r['amort']+r['sbc']+r['tax_shield']-r['delta_nwc']
        r['acquisition_cash']=a['acquisition_cash'] if i==0 else 0.
        r['goodwill']=p['goodwill']+(a['acquired_goodwill'] if i==0 else 0.)
        r['acquired_other_liabilities']=p['acquired_other_liabilities']+(a['acquired_other_liabilities'] if i==0 else 0.)
        r['workfusion_settlement']=p['workfusion_payable'] if i==1 else 0.
        r['workfusion_payable']=p['workfusion_payable']+(a['workfusion_payable'] if i==0 else 0.)-r['workfusion_settlement']
        r['acquisition_settlement']=min(p['acquisition_payable'],a['acquisition_settlement']) if i==0 else 0.
        r['repurchase_settlement']=min(p['repurchase_payable'],a['repurchase_settlement']) if i==0 else 0.
        r['acquisition_payable']=p['acquisition_payable']-r['acquisition_settlement']
        r['repurchase_payable']=p['repurchase_payable']-r['repurchase_settlement']
        r['cfi']=-r['capex']-r['acquisition_cash']
        r['offset_buybacks']=r['sbc']
        r['cff']=-r['offset_buybacks']-r['acquisition_settlement']-r['repurchase_settlement']-r['workfusion_settlement']
        r['equity']=p['equity']+r['ni']+r['sbc']-r['offset_buybacks']
        r['cash_costs']=r['cogs']+r['sga']+r['rd']-r['dep']-r['amort']-r['sbc']
        if r['cash_costs']<0: raise ValueError('Noncash costs exceed operating costs')
        r['reserve']=r['cash_costs']*a['reserve_months']/12
        r['reserve_investment']=r['reserve']-prior_reserve
        r['fcfe']=r['cfo']+r['cfi']+r['cff']-r['reserve_investment']
        # Cash computed LAST from cash flow, never as a balancing plug.
        r['cash']=p['cash']+r['cfo']+r['cfi']+r['cff']
        rows.append(r)
        prior_reserve=r['reserve']
        p=r
    assert_valid(rows,a)
    return rows


def value(rows,a=A):
    assert_valid(rows,a)
    last=rows[-1]
    ke,g=a['ke'],a['g']
    # Continue the actual closing schedules at 3% growth. This prevents a jump
    # from five-year asset balances to an assumed steady-state asset balance.
    revenue=last['revenue']; ppe=last['ppe']; intangible=last['intangibles']
    wc=nwc(last); reserve=last['reserve']; nol=last['nol']; dta=last['dta']
    pv_terminal=0.; pv_shield=0.; first_terminal_fcfe=None
    for year in range(6,206):
        revenue*=1+g
        ebit=revenue*(a['gm'][-1]*(1-a['sga'][-1])-a['rd'][-1])
        dep=ppe*a['depreciation']; capex=revenue*a['capex'][-1]
        ppe+=capex-dep
        amort=min(intangible,a['amortization'][-1])
        intangible-=amort
        new_wc=wc*(1+g)
        new_reserve=(revenue-ebit-dep-amort-revenue*a['sbc'][-1])*a['reserve_months']/12
        normal_fcfe=ebit*(1-a['tax'])+dep+amort-capex-(new_wc-wc)-(new_reserve-reserve)
        if first_terminal_fcfe is None: first_terminal_fcfe=normal_fcfe
        pv_terminal+=normal_fcfe/(1+ke)**year
        use=min(nol,a['nol_annual_cap'],max(0.,ebit)*a['nol_income_limit'])
        benefit=min(use*a['federal_rate'],max(0.,ebit)*a['tax'],dta)
        pv_shield+=benefit/(1+ke)**year
        nol-=benefit/a['federal_rate'] if a['federal_rate'] else 0.
        dta-=benefit
        wc,reserve=new_wc,new_reserve
    if normal_fcfe<=0 or first_terminal_fcfe<=0:
        raise ValueError('Nonpositive sustainable terminal FCFE: no going-concern terminal estimate')
    # After 200 transition years, PP&E and operating ratios have converged.
    pv_terminal+=normal_fcfe*(1+g)/(ke-g)/(1+ke)**205
    pv_explicit=sum(r['fcfe']/(1+ke)**(i+1) for i,r in enumerate(rows))
    excess=OPENING['cash']+OPENING['securities']-opening_reserve(a)
    equity=pv_explicit+pv_terminal+pv_shield+excess
    # Literal course positive-only convention shown separately, not presented
    # as economic value: dropping negative cash flows omits funding costs.
    omitted_cost=sum(-min(0.,r['fcfe'])/(1+ke)**(i+1) for i,r in enumerate(rows))
    return dict(value_per_share=equity/a['shares'],equity=equity,
        pv_explicit=pv_explicit,pv_terminal=pv_terminal,pv_nol=pv_shield,
        opening_excess=excess,terminal_fcfe=first_terminal_fcfe,
        course_positive_only_per_share=(equity+omitted_cost)/a['shares'])


def table(title,rows,fields):
    print('\n'+title+' — USD millions')
    print('Line'.ljust(30)+''.join(f"FY{r['year']}".rjust(12) for r in rows))
    for k in fields:
        print(k.ljust(30)+''.join(f'{r[k]:12,.3f}' for r in rows))


def tests():
    rows=project()
    for key in ('cash','equity','ppe','deferred_revenue','cfo','dta','fcfe','reserve_investment','nol','intangibles'):
        broken=deepcopy(rows); broken[2][key]+=1.
        try: value(broken)
        except ValueError: print(f'PASS refusal: altered FY2029 {key}')
        else: raise AssertionError(f'Failed to reject broken {key}')
    for label,edit in [('g equals ke',{'g':.11}),('cash floor',{'reserve_months':36.})]:
        try: value(project(dict(A,**edit)),dict(A,**edit))
        except ValueError: print('PASS refusal: '+label)
        else: raise AssertionError('Failed to reject '+label)
    no_nol=dict(A,nol_annual_cap=0.)
    assert value(project(no_nol),no_nol)['equity'] < value(rows)['equity']
    assert all(abs(r['sbc']-r['offset_buybacks'])<TOL for r in rows)
    print('PASS: no-NOL value lower; SBC cash offset counted once')
    # An independently calculated cash-tax bridge must equal the CFO bridge.
    for r in rows:
        direct=r['ebit']-r['cash_tax']+r['dep']+r['amort']-r['delta_nwc']-r['capex']-r['acquisition_cash']-r['acquisition_settlement']-r['repurchase_settlement']-r['workfusion_settlement']-r['reserve_investment']
        assert abs(direct-r['fcfe'])<TOL
    print('PASS: cash-tax formulation reproduces all five FCFE figures')


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--test',action='store_true')
    args=parser.parse_args()
    rows=project()
    print('UiPath: annual-base teaching model; read limitations in companion MD.')
    table('Income statement',rows,('revenue','gp','cogs','sga','rd','ebit','tax_expense','ni'))
    for r in rows:
        r['total_assets']=total(r,ASSETS)
        r['total_liabilities']=total(r,LIABILITIES)
        r['liabilities_and_equity']=r['total_liabilities']+r['equity']
    table('Balance sheet',rows,ASSETS+('total_assets',)+LIABILITIES+('total_liabilities','equity','liabilities_and_equity'))
    table('Cash flow and distributable FCFE',rows,('ni','dep','amort','sbc','tax_shield',
        'delta_nwc','dr_cash','cfo','capex','acquisition_cash','cfi','offset_buybacks',
        'acquisition_settlement','repurchase_settlement','workfusion_settlement','cff','reserve',
        'reserve_investment','fcfe','cash'))
    print('\nCHECKS (full precision; displayed residuals zeroed only below tolerance)')
    p=OPENING
    for r in rows:
        print(f"FY{r['year']}: "+'; '.join(f'{k}={0. if abs(v)<TOL else v:.6f}' for k,v in checks(r,p,A).items()))
        if r['fcfe']<0: print('  NEGATIVE FCFE retained as a cost in valuation.')
        p=r
    print('\nANNUAL-BASE VALUATION: January 31, 2026 base, later forecast information')
    for k,v in value(rows).items(): print(f'{k}: {v:,.4f}')
    print('\nMarket reference: $12.68, September 24, 2026 at 3:01 p.m. EDT (intraday).')
    print('Source: https://stockanalysis.com/stocks/path/')
    print('Annual-base model uses January 31 opening assets and 537.037m shares;')
    print('this is a qualified comparison, not a September-rebased fair-value estimate.')
    if args.test: tests()

if __name__=='__main__':
    try: main()
    except ValueError as e: raise SystemExit('VALUATION REFUSED: '+str(e)) from e
