#!/usr/bin/env python3
"""Independent 32-left-label elimination check of the two-state C4 proof."""
from collections import Counter,defaultdict
from itertools import product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
def multiply(P,Q):
    R=Counter()
    for a,c in P.items():
        for b,d in Q.items():R[tuple(x+y for x,y in zip(a,b))]+=c*d
    return {a:c for a,c in R.items()if c}
def decode(P):return {tuple(map(int,n.split(','))):c for n,c in P.items()}
def main():
    F=Counter();zero=(0,)*6
    for left in product(range(2),repeat=5):
        polynomial={zero:1}
        for j in range(5):
            local=Counter()
            for right in range(2):
                exponent=[0]*6
                for i in range(5):
                    if (i-j)%5 not in (0,1,4):continue
                    h=left[i]+right # 00->0,01/10->1,11->2
                    if i in (0,1) and j in (0,1):h+=3
                    exponent[h]+=1
                local[tuple(exponent)]+=1
            polynomial=multiply(polynomial,local)
        F.update(polynomial)
    assert sum(F.values())==1024
    author=json.loads((HERE/'continuation_20261003_C4_twostate_discriminant.json').read_text())
    assert dict(F)==decode(author['raw_polynomial'])
    Q=defaultdict(Counter)
    for n,c in F.items():Q[n[3:]][n[:3]]+=c
    allowed={(4,0,0),(0,0,4),(0,4,0),(2,2,0),(0,2,2),(1,2,1)}
    assert set(Q)==allowed
    assert {k:dict(v)for k,v in Q.items()}=={
        tuple(map(int,k.split(','))):decode(v)for k,v in author['quartic_coefficients'].items()}
    C,D,E=Q[2,2,0],Q[0,2,2],Q[1,2,1]
    discriminant=Counter({n:4*c for n,c in multiply(C,D).items()})
    discriminant.subtract(multiply(E,E));discriminant={n:c for n,c in discriminant.items()if c}
    assert discriminant==decode(author['four_cd_minus_e_squared'])
    assert len(discriminant)==66 and min(discriminant.values())==24
    assert max(discriminant.values())==16008
    assert all(sum(n)==22 and n[1]>=2 and c>0 for n,c in discriminant.items())
    report={'status':'PASS exact independent elimination and quartic PSD certificate',
            'left_assignments':32,'independent_target_sums_per_left':5,
            'represented_source_assignments':sum(F.values()),
            'quartic_term_counts':{','.join(map(str,k)):len(v)for k,v in Q.items()},
            'full_quartic_and_all_six_grouped_polynomials_match':True,
            'determinant_terms':len(discriminant),'determinant_coefficients_strictly_positive':True,
            'determinant_minimum_coefficient':min(discriminant.values()),
            'determinant_maximum_coefficient':max(discriminant.values()),
            'all_determinant_monomials_have_degree22_and_c_squared_factor':True,
            'scope':'arbitrary symmetric entrywise nonnegative 2x2 A and real symmetric 2x2 B'}
    (HERE/'C4_twostate_ant_independent_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
