import json
from pathlib import Path
from fractions import Fraction
from itertools import product
from phase_exact import affine_admit, direct_walsh
ROOT=Path(__file__).resolve().parents[1]
cases=[]
for n,basis,shift in [(3,[1,2],4),(4,[3,5],8),(4,[1,2,4,8],0),(5,[3,5,9,17],7),(5,[1,2,4],8),(30,[3,5],1<<29)]:
    labels=[]
    for mask in range(1<<len(basis)):
        s=shift
        for j,v in enumerate(basis):
            if mask>>j&1: s^=v
        labels.append(s)
    result=affine_admit({s:Fraction(1,len(labels)) for s in labels},n)
    expected='REALIZABLE' if len(basis)%2==0 else 'IMPOSSIBLE'
    assert result['status']==expected
    if expected=='REALIZABLE' and n<=5:
        truth=[]
        for x in range(1<<n):
            y=sum(((v&x).bit_count()%2)<<j for j,v in enumerate(result['basis']))
            truth.append((-1 if (result['affine_shift']&x).bit_count()%2 else 1)*result['truth_table'][y])
        coefficients=direct_walsh(truth)
        assert {s:Fraction(a*a,(1<<n)**2) for s,a in enumerate(coefficients) if a}=={s:Fraction(1,len(labels)) for s in labels}
        result['lifted_truth_table']=truth
    cases.append(result)
out={'status':'PASS','cases':cases,'arithmetic':'integers and Fraction; lifted transforms use direct character sums'}
(ROOT/'out'/'lift_checks.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
