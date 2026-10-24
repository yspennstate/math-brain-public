"""Counterexample-backed applicability controls, not a production benchmark."""
from pathlib import Path
import json,time
from hypothesis_guard import check

ROOT=Path(__file__).resolve().parent

def main():
    start=time.perf_counter()
    records=[
        ('Z3-ambient-exp-theorem', ['quasi_transitive','exponential_growth'], {'quasi_transitive':True,'exponential_growth':False}, False, 'Z^3 has polynomial volume growth, so Hutchcroft exponential-growth theorem does not apply.'),
        ('decorated-ray-transfer', ['quasi_transitive','exponential_growth'], {'quasi_transitive':False,'exponential_growth':True}, False, 'Written L005: maximum degree 3, exponential growth >=sqrt(2), p_c=1; quasi-transitivity is missing.'),
        ('subexponential-cluster-peierls', ['bounded_degree','positive_anchored_expansion','fresh_q_bits'], {'bounded_degree':True,'positive_anchored_expansion':False,'fresh_q_bits':True}, False, 'w442 deterministic ball-growth obstruction proves the needed positive expansion cannot hold.'),
        ('regular-tree-exp-control', ['quasi_transitive','exponential_growth'], {'quasi_transitive':True,'exponential_growth':True}, True, 'Regular degree-3 tree meets both graph hypotheses.'),
        ('peierls-tree-control', ['bounded_degree','positive_anchored_expansion','fresh_q_bits'], {'bounded_degree':True,'positive_anchored_expansion':True,'fresh_q_bits':True}, True, 'Regular degree-3 tree has anchored expansion 1; choose fresh q=19/20 for L004, checked exactly in MATH_CHECKS.json.')
    ]
    rows=[]
    for name,required,facts,expected,evidence in records:
        result=check(required,facts)
        assert result['applicable']==expected
        rows.append({'case':name,'required':required,'established':facts,'expected_applicable':expected,'result':result,'evidence':evidence})
    unknown=check(['quasi_transitive','exponential_growth'],{'exponential_growth':True})
    assert not unknown['applicable'] and unknown['unknown_hypotheses']==['quasi_transitive']
    report={'command':'python -X utf8 validate_guard.py','seconds':time.perf_counter()-start,'scope':'Controlled local applicability fixture, not production recall accuracy. Ungated baseline means accepting every candidate; it is not an observation of the live engine.','before':{'invalid_candidates_allowed':3,'valid_controls_allowed':2},'after':{'invalid_candidates_allowed':0,'valid_controls_allowed':2},'unknown_property_control':unknown,'rows':rows}
    (ROOT/'GUARD_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2))

if __name__=='__main__':main()
