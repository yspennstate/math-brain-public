from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent

def formula(bs,bias):
    if not bs or bias<=0 or bias>=min(bs):
        raise ValueError('Outside proven range: 0<lambda<min b_i')
    B=sum(bs); m=len(bs)
    return F(B-m*bias,B+m*bias)

def main():
    start=time.perf_counter()
    families=[[3]*m for m in range(1,6)]+[[3,5],[3,5,7]]
    biases=[F(1,2),F(1),F(2),F(29,10)]
    rows=[]; pattern_cases=0
    for bs in families:
        for bias in biases:
            eventual=formula(bs,bias)
            for at_root in product((False,True),repeat=len(bs)):
                outward=sum(b+1 if root else b for b,root in zip(bs,at_root))
                inward=sum(not root for root in at_root)
                drift=(outward-bias*inward)/(outward+bias*inward)
                assert drift>=eventual
                if not any(at_root):
                    assert drift==eventual
                pattern_cases+=1
            if all(b==3 for b in bs) and bias==2:
                assert eventual==F(1,5)
            if all(b==3 for b in bs) and bias==F(29,10):
                assert eventual==F(1,59)
            rows.append({'branching_numbers':bs,'lambda_exact':str(bias),'speed_exact':str(eventual),
                         'coordinate_return_probabilities_exact':[str(bias/b) for b in bs]})
    rejected=0
    for bs,bias in [([3],F(3)),([3,5],F(4)),([3],F(0))]:
        try:
            formula(bs,bias)
        except ValueError:
            rejected+=1
        else:
            raise AssertionError('Unproved boundary admitted')
    result={'command':'python -X utf8 p0035_check.py','tree_product_bias_cases':len(rows),
            'root_coordinate_patterns_checked':pattern_cases,'out_of_range_cases_rejected':rejected,
            'cases':rows,'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'p0035.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))

if __name__=='__main__':
    main()
