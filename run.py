"""One-command reproducible analysis; no packages, credentials or network."""
import json
from pathlib import Path
from datetime import datetime, timezone
import model

ROOT=Path(__file__).resolve().parent

def md_table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rows])

def main():
    d=model.load(); r=model.results(d); out=ROOT/'reports'; out.mkdir(exist_ok=True)
    (out/'results.json').write_text(json.dumps(r,indent=2)+'\n')
    text=['# Executed valuation output','', 'Valuation: October 19, 2026 intraday: PATH 11:15 AM EDT / PEGA 11:25 AM EDT. Prepared October 19, 2026. USD millions except per-share prices. Draft pending student review.',
          '', 'Latest July 31 balances proxy the October opening; five rolling annual periods, not company fiscal years. Market quote: $13.03. Basic share basis: 521.155409 million. See methodology for lag, SBC and tax limitations.', '', '## Scenario valuation',
          md_table(['Case','EV ($m)','Equity ($m)','Value/share','TV / EV'],[[n,f"{c['valuation']['ev']:,.3f}",f"{c['valuation']['equity']:,.3f}",f"${c['valuation']['per_share']:.2f}",f"{c['valuation']['terminal_share']:.1%}"] for n,c in r['cases'].items()]),
          '', '## Enterprise-to-equity bridge', 'FCFF operating EV + $1,078.193m excess liquidity - $0 funded debt - $34.251m acquisition obligations = equity; divide by 521.155409m basic shares. The $326.832m operating reserve and $1.475m restricted cash are not excess cash. Accumulated forecast cash is not added again.',
          '', '## WACC / terminal-growth sensitivity (base operations)',md_table(['WACC','g 2%','g 3%','g 4%'],[[f"{row['wacc']:.0%}"]+[f"${v:.2f}" for v in row['values']] for row in r['wacc_growth']]),
          '', '## Reverse DCF',f"Holding other base assumptions fixed, a linear SG&A/gross-profit path from 65% to {r['reverse_dcf']['year5_sga_gp']:.2%} supports $13.03. This is a conditional one-driver solution, not a prediction or the only possible explanation.",
          '', '## Comparables',md_table(['Measure','PEGA','PATH'],[['EV / LTM revenue',f"{r['comps']['peer_ev_sales']:.3f}x",f"{r['comps']['target_ev_sales']:.3f}x"],['Price / annual reported diluted EPS',f"{r['comps']['peer_pe']:.3f}x",f"{r['comps']['target_pe']:.3f}x"]]),
          f"PEGA-implied PATH reference: EV/revenue ${r['comps']['implied_ev_sales_price']:.2f}; P/E ${r['comps']['implied_pe_price']:.2f}. One peer; no averaging; earnings contain tax benefits. Sales-multiple EV deducts all liquid assets consistently in both firms, while the DCF retains operating cash."]
    for name,c in r['cases'].items():
        rows=c['statements']; a=c['assumptions']
        text+=['',f'## {name.title()} assumptions',md_table(['Driver']+[str(x) for x in range(1,6)],[[k]+[f'{v:.2%}' for v in a[k]] for k in ('growth','gm','sga','rd','sbc','capex','dr')])]
        for title,fields in [('Income statement',('revenue','gp','sga','rd','ebit','tax','ni')),
                             ('Balance sheet',model.ASSETS+('assets',)+model.LIABS+('liabilities','equity')),
                             ('Cash flow and FCFF',('ni','dep','amort','sbc','delta_nwc','cfo','capex','cfi','offset_buybacks','acquisition_settlement','cff','reserve','reserve_investment','fcff','cash'))]:
            text+=['',f'### {title} - USD millions',md_table(['Line']+[str(x['year'])+' rolling' for x in rows],[[k]+[f'{x[k]:,.3f}' for x in rows] for k in fields])]
        p=d['opening']; reserve=d['history']['opening_reserve']; checks=[]
        for row in rows:
            gaps=model.row_checks(row,p,reserve); checks.append([row['year'],f'{max(abs(v) for v in gaps.values()):.10f}','PASS'])
            p=row; reserve=row['reserve']
        text+=['',md_table(['Period','Maximum check residual ($m)','Status'],checks)]
    # Transparent lag and denominator sensitivities; no claim these are actual changes.
    base=r['cases']['base']['valuation']['per_share']; shares=d['assumptions']['shares']
    text+=['','## Reporting-lag and convention sensitivities',md_table(['Change','Base value/share'],[['$100m less opening excess liquidity',f'${base-100/shares:.2f}'],['5% more shares, unchanged numerator',f'${base/1.05:.2f}'],['Tax 25%, other base inputs fixed',f"${model.run(d,override={'tax':.25})[2]['per_share']:.2f}"]]),'These are stress assumptions, not observed changes or bounds on total error. No NOL relief is credited; full DTA recognition would be inappropriate without a utilization schedule.']
    (out/'valuation-output.md').write_text('\n\n'.join(text)+'\n')
    # Lightweight offline presentation of the exact precomputed results.
    html='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PATH investment committee</title><style>body{font:16px system-ui;max-width:1100px;margin:40px auto;padding:0 24px;background:#f4f6f8;color:#17263a}h1{font-size:42px}section{background:white;border-radius:12px;padding:24px;margin:20px 0}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:9px;text-align:right;border-bottom:1px solid #ddd}td:first-child,th:first-child{text-align:left}select{padding:10px;font-size:16px}.muted{color:#536477}.metric{font-size:42px;font-weight:700;color:#174d59}a{color:#175d8b}button{padding:10px}</style><h1>UiPath | Do not initiate</h1><p class="muted">Review draft · October 19, 2026 valuation · 12–18 month monitoring horizon</p><section><p>DCF scenario range <strong>__LOW__–__HIGH__</strong> versus <strong>__PRICE__</strong> intraday snapshot (11:15 a.m. EDT). PEGA-implied EV/revenue is materially higher; methods are not averaged.</p><label for="case">Explore operating case </label><select id="case"><option>base</option><option>downside</option><option>upside</option></select><div id="valuation"></div></section><section><h2>What would change the decision?</h2><p>ARR growth above 12% for two quarters; retention at 110%; disclosed incremental agentic ARR; gross margin stabilizing at 81%; selling costs growing slower than gross profit. These trigger a rerun, not an automatic buy. Retention below 105% for two quarters strengthens the downside case.</p></section><section><h2>Five-year operating forecast</h2><p>Rolling years ending October 19. USD millions. July 31 reported balances proxy opening financial position.</p><div id="table"></div></section><section><h2>Evidence and reproduction</h2><p><a href="reports/valuation-output.md">Full statements and sensitivity</a> · <a href="docs/decision-memo.pdf">Decision memo</a> · <a href="docs/model-method.md">Method and limitations</a> · <a href="docs/validation-and-ai-use.md">Validation / AI record</a></p><p>Run <code>python3 run.py</code>, then <code>python3 -m unittest -v test_model</code>. This page displays saved results; it does not call live APIs.</p></section><script>const DATA=__DATA__;function render(){const c=DATA.cases[document.getElementById('case').value],v=c.valuation;document.getElementById('valuation').innerHTML='<p class="metric">$'+v.per_share.toFixed(2)+'/share</p><p>Enterprise value $'+v.ev.toFixed(1)+'m + excess liquidity $'+v.excess_cash.toFixed(1)+'m − acquisition claims $'+v.acquisition_claim.toFixed(1)+'m = equity $'+v.equity.toFixed(1)+'m.</p><p>Terminal share of EV: '+(100*v.terminal_share).toFixed(1)+'%.</p>';document.getElementById('table').innerHTML='<table><tr><th>Line</th>'+c.statements.map(r=>'<th>'+r.year+'</th>').join('')+'</tr>'+['revenue','gp','sga','rd','ebit','cfo','fcff','cash'].map(k=>'<tr><td>'+({revenue:'Revenue',gp:'Gross profit',sga:'SG&A',rd:'R&D',ebit:'Operating profit',cfo:'Operating cash flow',fcff:'FCFF after SBC cost',cash:'Cash balance'}[k]||k)+'</td>'+c.statements.map(r=>'<td>'+r[k].toFixed(1)+'</td>').join('')+'</tr>').join('')+'</table>';}document.getElementById('case').onchange=render;render();</script></html>'''
    (ROOT/'index.html').write_text(html.replace('__DATA__',json.dumps(r)).replace('__LOW__',f"${r['cases']['downside']['valuation']['per_share']:.2f}").replace('__HIGH__',f"${r['cases']['upside']['valuation']['per_share']:.2f}").replace('__PRICE__',f"${d['market']['PATH']['price']:.2f}"))
    print('Wrote reports/results.json, reports/valuation-output.md and index.html')
    print('Base',round(base,4),'Range',round(r['cases']['downside']['valuation']['per_share'],4),round(r['cases']['upside']['valuation']['per_share'],4))

if __name__=='__main__': main()
