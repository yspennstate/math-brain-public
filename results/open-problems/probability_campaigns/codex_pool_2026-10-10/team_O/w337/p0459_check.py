from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent

def exact_mean(n,k):
    if k==n-1:
        return F(k)
    N=n-2
    return (n-1)*sum((F(comb(N,i)*comb(N,j)*factorial(i+j)*factorial(2*N-i-j),factorial(2*N+1))
                      for i in range(k) for j in range(k)),F(0))

def main():
    start=time.perf_counter()
    cases=[]
    for n in range(2,14):
        for k in range(1,n):
            mu=exact_mean(n,k)
            assert 0<=mu<=k
            assert (k-mu)**2<=F(k*(n-1-k),2*n)
            cases.append({'n':n,'k':k,'mean_exact':str(mu),'mean_deficit_squared':str((k-mu)**2)})
    edges=[(i,j) for i in range(4) for j in range(i+1,4)]
    sums={k:F(0) for k in (1,2,3)}
    inclusion_checks=0
    for ordering in permutations(edges):
        incident={v:[e for e in ordering if v in e] for v in range(4)}
        for k in (1,2,3):
            choices={v:set(incident[v][:k]) for v in range(4)}
            bilateral={e for e in edges if e in choices[e[0]] and e in choices[e[1]]}
            sums[k]+=len([e for e in bilateral if 0 in e])
            for cutoff in range(7):
                threshold=set(ordering[:cutoff])
                degrees={v:sum(v in e for e in threshold) for v in range(4)}
                if max(degrees.values())<=k:
                    assert threshold<=bilateral
                inclusion_checks+=1
    assert all(sums[k]/720==exact_mean(4,k) for k in (1,2,3))
    result={'command':'python -X utf8 p0459_check.py','exact_mean_bound_cases':len(cases),
            'exhaustive_edge_orders':720,'threshold_rank_cases':inclusion_checks,
            'exhaustive_means':{str(k):str(sums[k]/720) for k in (1,2,3)},
            'elapsed_seconds':time.perf_counter()-start,'cases':cases}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'p0459.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))

if __name__=='__main__':
    main()
