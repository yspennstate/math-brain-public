from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent

def upper(L,p,M=2):
    size=L-1
    values={}
    counts=sorted(product(range(M+1),repeat=size),key=sum,reverse=True)
    for c in counts:
        low=[F(0)]*size
        diag=[F(1)]*size
        high=[F(0)]*size
        rhs=[F(0)]*size
        for i in range(size):
            if c[i]<M:
                nxt=list(c); nxt[i]+=1
                v=values[tuple(nxt)]
                rhs[i]=p*(F(1) if i==size-1 else v[i+1])+(1-p)*(F(0) if i==0 else v[i-1])
            else:
                if i:
                    low[i]=-F(1,2)
                if i<size-1:
                    high[i]=-F(1,2)
                else:
                    rhs[i]=F(1,2)
        # Thomas elimination; row structure follows the exact boundary equation.
        for i in range(1,size):
            factor=low[i]/diag[i-1]
            diag[i]-=factor*high[i-1]
            rhs[i]-=factor*rhs[i-1]
        v=[F(0)]*size
        for i in range(size-1,-1,-1):
            v[i]=(rhs[i]-(high[i]*v[i+1] if i+1<size else 0))/diag[i]
        assert all(0<=x<=1 for x in v)
        values[c]=v
    return values[(0,)*size][0],len(values)*size

def main():
    start=time.perf_counter()
    rows=[]
    last=F(1)
    for L in range(2,9):
        q,states=upper(L,F(4,5))
        fair,_=upper(L,F(1,2))
        assert fair==F(1,L)
        assert q<=last
        last=q
        rows.append({'L':L,'finite_interval_q_exact':str(q),'finite_interval_q_float':float(q),
                     'escape_from_zero_upper_if_right_transient_exact':str(F(4,5)*q),
                     'transient_state_upper_bound':states,'fair_q_exact':str(fair)})
    result={'command':'python -X utf8 c0130_check.py','label':'exact rational upper bounds only',
            'cookie_strength':'4/5','cookies_per_site':2,'cases':rows,
            'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'measurements').mkdir(exist_ok=True)
    (ROOT/'measurements'/'c0130.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
