from fractions import Fraction as F
from math import comb,exp
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent

def main():
    start=time.perf_counter()
    P=[F(1,4)]*4
    Q=[F(v,24) for v in (5,9,3,7)]
    momentsP=[sum((P[x]*x**r for x in range(4)),F(0)) for r in range(4)]
    momentsQ=[sum((Q[x]*x**r for x in range(4)),F(0)) for r in range(4)]
    assert momentsP[:3]==momentsQ[:3]
    assert momentsQ[3]-momentsP[3]==F(1,4)
    assert all(v>0 for v in P+Q)
    tv=sum((abs(p-q) for p,q in zip(P,Q)),F(0))/2
    assert tv==F(1,6)
    rows=[]
    for j in range(1,9):
        n=16*j
        errP=sum((F(comb(n,k)*3**(n-k),4**n) for k in range(n//2,n+1)),F(0))
        errQ=sum((F(comb(n,k)*3**k,4**n) for k in range(n//2)),F(0))
        assert float(errP)<=exp(-2*j)
        assert float(errQ)<=exp(-2*j)
        rows.append({'j':j,'coins':n,'P_wrong_side':float(errP),'Q_wrong_side':float(errQ),
                     'error_sum_exact':str(errP+errQ),'individual_hoeffding_bound':exp(-2*j)})
    result={'command':'python -X utf8 c0022_check.py','moments_P_exact':list(map(str,momentsP)),
            'moments_Q_exact':list(map(str,momentsQ)),'mutually_absolutely_continuous':True,
            'moment_example_tv_exact':str(tv),'separator_error_cases':rows,
            'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'c0022.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='separator_error_cases'},indent=2))

if __name__=='__main__':
    main()
