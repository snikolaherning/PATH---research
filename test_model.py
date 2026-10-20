"""Ordinary AI-assisted technical tests, NOT the student's AI-closed exercise."""
from copy import deepcopy
from datetime import datetime, timezone
import importlib.util
import unittest
import model

class FinanceTests(unittest.TestCase):
    def setUp(self): self.d=model.load()

    def test_filing_reconciliation(self):
        o=self.d['opening']
        self.assertAlmostEqual(model.total(o,model.ASSETS),2907.367,places=6)
        self.assertAlmostEqual(model.total(o,model.LIABS),958.816,places=6)
        self.assertAlmostEqual(o['equity'],1948.551,places=6)
        self.assertAlmostEqual(o['revenue'],1610.572+828.638-718.352,places=6)
        # Reported cash statement includes restricted cash and FX.
        self.assertAlmostEqual(871.595+162.627-128.565-287.124-9.644,608.889,places=6)
        self.assertAlmostEqual(608.889-1.475,o['cash'],places=6)

    def test_all_cases_articulate(self):
        for case in self.d['scenarios']:
            a,rows,v=model.run(self.d,case)
            self.assertEqual(len(rows),5)
            self.assertAlmostEqual(v['equity'],v['ev']+v['excess_cash']-v['acquisition_claim'],places=6)
            self.assertAlmostEqual(v['per_share']*a['shares'],v['equity'],places=6)

    def test_highest_risk_corruption_is_refused(self):
        a,rows,_=model.run(self.d)
        for field in ('cash','equity','ppe','cfo','fcff','deferred_revenue'):
            broken=deepcopy(rows); broken[2][field]+=1
            with self.subTest(field=field), self.assertRaises(ValueError):
                model.value(broken,a,self.d['opening'],self.d['history'])

    def test_boundary(self):
        for override in ({'g':.11},{'shares':0},{'growth':[-1]*5},{'gm':[float('nan')]*5}):
            with self.assertRaises(ValueError): model.run(self.d,override=override)

    def test_monotonicity(self):
        values=[model.run(self.d,override={'wacc':w})[2]['per_share'] for w in (.09,.10,.11,.12,.13)]
        self.assertTrue(all(a>b for a,b in zip(values,values[1:])))
        values=[model.run(self.d,override={'g':g})[2]['per_share'] for g in (.02,.03,.04)]
        self.assertTrue(all(a<b for a,b in zip(values,values[1:])))

    def test_preregistered_tax_direction(self):
        # See reports/directional-test-plan.md written before this test's first run.
        base=model.run(self.d)[2]['per_share']
        changed=model.run(self.d,override={'tax':.26})[2]['per_share']
        self.assertLess(changed,base)
        self.assertLess(changed,self.d['market']['PATH']['price'])

    def test_sbc_not_double_counted(self):
        a,rows,_=model.run(self.d)
        for r in rows:
            self.assertAlmostEqual(r['sbc'],r['offset_buybacks'],places=6)
            direct=r['ebit']-r['tax']+r['dep']+r['amort']-r['capex']-r['delta_nwc']-r['reserve_investment']
            self.assertAlmostEqual(r['fcff'],direct,places=6)

    def test_comps_definitions(self):
        c=model.comps(self.d); t=self.d['market']['PATH']; p=self.d['market']['PEGA']
        self.assertEqual(t['price_date'],p['price_date'])
        self.assertAlmostEqual(c['peer_pe'],34.37/2.13,places=8)
        self.assertAlmostEqual(c['peer_ev_sales'],(34.37*164.404945-361.907)/1736.356,places=8)

    def test_reverse_dcf(self):
        r=model.reverse_sga(self.d)
        self.assertEqual(r['status'],'solved')
        self.assertAlmostEqual(r['price'],13.03,places=6)

    def test_classroom_known_answer(self):
        path=model.ROOT/'legacy/Lab09proforma.py'
        spec=importlib.util.spec_from_file_location('training',path)
        training=importlib.util.module_from_spec(spec); spec.loader.exec_module(training)
        rows=training.project(); v=training.value_equity(rows)
        self.assertEqual(round(v['value_per_share'],2),291.75)
        self.assertEqual(round(v['equity_value'],2),5237.34)

if __name__=='__main__': unittest.main(verbosity=2)
