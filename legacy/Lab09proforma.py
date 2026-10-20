"""Lab 09 ABG five-year three-statement engine; Python standard library only.

Amounts: USD millions, except per-share value. Course inputs, not independently
researched ABG estimates. Sources and student explanations: lab09-proforma.md.
Run: python3 proforma.py
"""

from math import isfinite


OPENING = dict(revenue=17999.0, inventory=2135.8, ppe=3070.4,
               other_assets=6371.6, cash=40.4, floor_plan=2027.0,
               debt=3572.0, other_liabilities=2127.5, equity=3891.7,
               revolver=0.0)
ASSUMPTIONS = dict(
    growth=0.018,                       # judgment
    gross_margin=0.1705,                # judgment
    sga_ratios=(0.665, 0.655, 0.645, 0.645, 0.645),  # judgment
    depreciation_ratio=82.4 / 3070.4,    # history
    impairment=120.0,                   # judgment
    capex=250.0,                        # guidance
    tax_rate=0.255,                     # judgment
    inventory_days=2135.8 / (17999.0 - 3071.7) * 365,  # history
    floor_plan_ratio=2027.0 / 2135.8,    # history
    other_wc_ratio=0.008,               # judgment
    minimum_cash=25.0,                  # history
    revolver_limit=850.0,               # judgment
    revolver_rate=0.06,                 # judgment
    repayment=150.0, buyback=150.0,      # judgment
    floor_plan_rate=0.0467, debt_rate=0.0544,  # history
    cost_of_equity=0.10, terminal_growth=0.025,  # judgment
    shares=17.951349,                   # fact; June 30, 2026 10-Q
)
TOLERANCE = 1e-7  # USD millions; check full precision, not printed rounding.


def checks(row, assumptions):
    assets = row['cash'] + row['inventory'] + row['ppe'] + row['other_assets']
    liabilities = (row['floor_plan'] + row['debt'] + row['revolver']
                   + row['other_liabilities'])
    return {
        'balance gap': assets - liabilities - row['equity'],
        'cash-flow reconciliation gap': row['cash'] - row['cf_closing_cash'],
        'cash above minimum': row['cash'] - assumptions['minimum_cash'],
        'revolver headroom': assumptions['revolver_limit'] - row['revolver'],
    }


def assert_balanced(rows, assumptions=ASSUMPTIONS):
    """Recompute checks from statements; never trust a cached balance gap."""
    for row in rows:
        year = f"FY{row['year']}E"
        if any(not isfinite(value) for value in row.values()):
            raise ValueError(f'{year}: non-finite statement value')
        for name, gap in checks(row, assumptions).items():
            failed = abs(gap) > TOLERANCE if 'gap' in name else gap < -TOLERANCE
            if failed:
                raise ValueError(f'{year}: {name} {gap:+.1f} USD million')
        if row['debt'] < -TOLERANCE or row['revolver'] < -TOLERANCE:
            raise ValueError(f'{year}: negative debt or revolver balance')


def project(opening=OPENING, assumptions=ASSUMPTIONS):
    a = assumptions
    if len(a['sga_ratios']) != 5:
        raise ValueError('Provide exactly five SG&A ratios')
    opening_gap = (opening['cash'] + opening['inventory'] + opening['ppe']
                   + opening['other_assets'] - opening['floor_plan']
                   - opening['debt'] - opening['revolver']
                   - opening['other_liabilities'] - opening['equity'])
    if not isfinite(opening_gap) or abs(opening_gap) > TOLERANCE:
        raise ValueError(f'FY2025: opening balance gap {opening_gap:+.1f}')
    prior = dict(opening)
    rows = []
    for year, sga_ratio in zip(range(2026, 2031), a['sga_ratios']):
        r = dict(year=year)
        r['revenue'] = prior['revenue'] * (1 + a['growth'])
        r['gross_profit'] = r['revenue'] * a['gross_margin']
        r['cost_of_sales'] = r['revenue'] - r['gross_profit']
        r['sga'] = r['gross_profit'] * sga_ratio
        r['depreciation'] = prior['ppe'] * a['depreciation_ratio']
        r['impairment'] = a['impairment']
        r['operating_income'] = (r['gross_profit'] - r['sga']
                                 - r['depreciation'] - r['impairment'])
        r['interest'] = (prior['floor_plan'] * a['floor_plan_rate']
                         + prior['debt'] * a['debt_rate']
                         + prior['revolver'] * a['revolver_rate'])
        r['pretax'] = r['operating_income'] - r['interest']
        r['tax'] = max(0.0, r['pretax']) * a['tax_rate']
        r['net_income'] = r['pretax'] - r['tax']

        r['inventory'] = r['cost_of_sales'] * a['inventory_days'] / 365
        r['floor_plan'] = r['inventory'] * a['floor_plan_ratio']
        r['capex'] = a['capex']
        r['ppe'] = prior['ppe'] + r['capex'] - r['depreciation']
        r['delta_other_wc'] = a['other_wc_ratio'] * (r['revenue'] - prior['revenue'])
        r['other_assets'] = prior['other_assets'] + r['delta_other_wc'] - r['impairment']
        r['repayment'] = a['repayment']
        if not 0 <= r['repayment'] <= prior['debt']:
            raise ValueError(f'FY{year}E: repayment exceeds opening debt or is negative')
        r['debt'] = prior['debt'] - r['repayment']
        r['other_liabilities'] = prior['other_liabilities']
        r['buyback'] = a['buyback']
        r['equity'] = prior['equity'] + r['net_income'] - r['buyback']
        r['delta_inventory'] = r['inventory'] - prior['inventory']
        r['delta_floor_plan'] = r['floor_plan'] - prior['floor_plan']
        r['operating_cf'] = (r['net_income'] + r['depreciation'] + r['impairment']
                             - r['delta_inventory'] - r['delta_other_wc']
                             + r['delta_floor_plan'])
        r['investing_cf'] = -r['capex']
        r['fcfe'] = r['operating_cf'] - r['capex'] - r['repayment']
        r['opening_cash'] = prior['cash']
        cash_before_revolver = prior['cash'] + r['fcfe'] - r['buyback']
        if cash_before_revolver < a['minimum_cash']:
            r['revolver_change'] = min(a['minimum_cash'] - cash_before_revolver,
                                       max(0.0, a['revolver_limit'] - prior['revolver']))
        else:
            r['revolver_change'] = -min(prior['revolver'],
                                        cash_before_revolver - a['minimum_cash'])
        r['revolver'] = prior['revolver'] + r['revolver_change']
        r['financing_cf'] = -r['repayment'] - r['buyback'] + r['revolver_change']
        r['cash_change'] = r['operating_cf'] + r['investing_cf'] + r['financing_cf']
        r['cf_closing_cash'] = r['opening_cash'] + r['cash_change']
        r['cash'] = cash_before_revolver + r['revolver_change']
        r['assets'] = r['cash'] + r['inventory'] + r['ppe'] + r['other_assets']
        r['liabilities_equity'] = (r['floor_plan'] + r['debt'] + r['revolver']
                                   + r['other_liabilities'] + r['equity'])
        assert_balanced([r], a)
        rows.append(r)
        prior = r
    return rows


def value_equity(rows, assumptions=ASSUMPTIONS):
    assert_balanced(rows, assumptions)  # Mandatory gate before any valuation.
    a = assumptions
    ke, g = a['cost_of_equity'], a['terminal_growth']
    if len(rows) != 5 or [r['year'] for r in rows] != list(range(2026, 2031)):
        raise ValueError('Valuation requires FY2026E through FY2030E')
    if not all(isfinite(x) for x in (ke, g, a['shares'])):
        raise ValueError('Valuation assumptions must be finite')
    if not -1 < g < ke or ke <= -1 or a['shares'] <= 0:
        raise ValueError('Require cost of equity > terminal growth > -100%, and positive shares')
    pv_fcfe = sum(r['fcfe'] / (1 + ke) ** i for i, r in enumerate(rows, 1))
    # Course terminal convention: scheduled term-debt repayments cease after 2030.
    terminal = (rows[-1]['fcfe'] + rows[-1]['repayment']) * (1 + g) / (ke - g)
    pv_terminal = terminal / (1 + ke) ** 5
    equity = pv_fcfe + pv_terminal
    return dict(equity_value=equity, value_per_share=equity / a['shares'],
                terminal_share=pv_terminal / equity if equity else float('nan'))


def print_table(title, rows, fields):
    print(f'\n{title} (USD millions)')
    print('Line'.ljust(34) + ''.join(f"FY{r['year']}E".rjust(13) for r in rows))
    for label, key, sign in fields:
        print(label.ljust(34) + ''.join(f"{sign*r[key]:13,.1f}" for r in rows))


def main():
    rows = project()
    print('Asbury (ABG) — Lab 09 course base case')
    print_table('Income statement', rows, [
        ('Revenue', 'revenue', 1), ('Cost of sales', 'cost_of_sales', -1),
        ('Gross profit', 'gross_profit', 1), ('SG&A', 'sga', -1),
        ('Depreciation', 'depreciation', -1), ('Impairment', 'impairment', -1),
        ('Operating income', 'operating_income', 1), ('Interest', 'interest', -1),
        ('Pretax income', 'pretax', 1), ('Tax', 'tax', -1), ('Net income', 'net_income', 1)])
    print_table('Balance sheet', rows, [
        ('Cash', 'cash', 1), ('Inventory', 'inventory', 1), ('PP&E', 'ppe', 1),
        ('Other assets', 'other_assets', 1), ('Total assets', 'assets', 1),
        ('Floor plan', 'floor_plan', 1), ('Term debt', 'debt', 1),
        ('Revolver', 'revolver', 1), ('Other liabilities', 'other_liabilities', 1),
        ('Equity', 'equity', 1), ('Liabilities + equity', 'liabilities_equity', 1)])
    print_table('Cash flow', rows, [
        ('Opening cash', 'opening_cash', 1), ('Net income', 'net_income', 1),
        ('Depreciation add-back', 'depreciation', 1), ('Impairment add-back', 'impairment', 1),
        ('Inventory investment', 'delta_inventory', -1), ('Other WC investment', 'delta_other_wc', -1),
        ('Change in floor plan', 'delta_floor_plan', 1), ('Operating cash flow', 'operating_cf', 1),
        ('Capex / investing cash flow', 'investing_cf', 1), ('Debt repayment', 'repayment', -1),
        ('FCFE before buybacks/revolver', 'fcfe', 1), ('Buybacks', 'buyback', -1),
        ('Revolver draw / (repayment)', 'revolver_change', 1),
        ('Financing cash flow', 'financing_cf', 1), ('Change in cash', 'cash_change', 1),
        ('Closing cash', 'cf_closing_cash', 1)])
    print('\nChecks (USD millions; full-precision validation)')
    for r in rows:
        values = checks(r, ASSUMPTIONS)
        print(f"FY{r['year']}E: " + '; '.join(
            f'{name} = {0.0 if abs(gap) < TOLERANCE else gap:.1f}'
            for name, gap in values.items()) + '; PASS')
    result = value_equity(rows)
    print(f"\nEquity value: ${result['equity_value']:,.2f} million")
    print(f"Share of value after 2030: {result['terminal_share']:.2%}")
    print(f"Value per share: ${result['value_per_share']:.2f}")


if __name__ == '__main__':
    try:
        main()
    except ValueError as error:
        raise SystemExit(f'VALUATION REFUSED: {error}') from error
