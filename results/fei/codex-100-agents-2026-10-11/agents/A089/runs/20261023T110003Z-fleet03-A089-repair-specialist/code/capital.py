"""Marked-point local-admission capital, exact interval formula pilot."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
import json,time,sys
from arithmetic import Q,log2,scale,plus
ROOT=Path(__file__).resolve().parents[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def maximum(v):return max(x[0] for x in v),max(x[1] for x in v)
@lru_cache(None)
def entropy(m):
    if m<2:return (0,0)
    u=F(2,2**m);a=(1-u)**2;b=u*u
    return plus(scale(log2(1/a),a),scale(log2(1/b),(2**m-1)*b))
def influence(r,t):
    m=r+t
    return F(0) if not m else F(r)+F(2*(m-2*r),2**m)
@lru_cache(None)
def deficit(r,t):
    s=sub(entropy(r+t),scale((Q,Q),influence(r,t)));return max(0,s[0]),max(0,s[1])
@lru_cache(None)
def local(r,t,p,q):
    return maximum([scale(deficit(r-a,t-b),F(1,2**(a+b))) for a in range(p+1) for b in range(q+1)])
@lru_cache(None)
def capital(r,t,p,q):
    candidates=[deficit(r,t)]
    if p<r:candidates.append(capital(r,t,p+1,q))
    if q<t:candidates.append(capital(r,t,p,q+1))
    for flag,nn in [(p,(r-1,t,p-1,q)),(q,(r,t-1,p,q-1))]:
        if flag:
            delta=scale(local(*nn),F(1,2))
            candidates.extend([sub(capital(*nn),delta),delta])
    return maximum(candidates)
def witness(state):
    r,t,p,q=state;candidates=[('stop',deficit(r,t),None,None)]
    if p<r:candidates.append(('admit_parity',capital(r,t,p+1,q),(r,t,p+1,q),None))
    if q<t:candidates.append(('admit_selector',capital(r,t,p,q+1),(r,t,p,q+1),None))
    for flag,nn,name in [(p,(r-1,t,p-1,q),'parity'),(q,(r,t-1,p,q-1),'selector')]:
        if flag:
            delta=scale(local(*nn),F(1,2))
            candidates.extend([('query_'+name+'_zero',sub(capital(*nn),delta),nn,delta),('query_'+name+'_one',delta,None,delta)])
    name,iv,nn,delta=max(candidates,key=lambda x:x[1][0]);step={'state':state,'action':name,'capital_requirement':iv,'delta_zero':delta}
    return [step]+(witness(nn) if nn else [])
def main():
    start=time.perf_counter();ds=range(3) if '--pilot' in sys.argv else range(7);out=[]
    for d in ds:
        R=local(3,d,3,d);T=capital(3,d,0,0)
        out.append({'d':d,'global_hull':R,'robust_capital':T,'capital_minus_half':sub(T,(Q//2,Q//2)),'I':str(influence(3,d))})
        assert time.perf_counter()-start<55
    summary={'cases':len(out),'states':capital.cache_info().currsize,'runtime_seconds':time.perf_counter()-start,'results':out}
    if '--pilot' not in sys.argv:
        assert capital(3,3,0,0)[0]*10000>5078*Q
        summary['counterexample_to_half_bit_conjecture']=witness((3,3,0,0))
    tag='PILOT' if '--pilot' in sys.argv else 'CAPITAL'
    (ROOT/'out'/f'{tag}.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'cases':len(out),'states':summary['states'],'runtime_seconds':summary['runtime_seconds'],'display':[{'d':r['d'],'R':float(F(r['global_hull'][0],Q)),'T':float(F(r['robust_capital'][0],Q)),'T_minus_half_upper_units':r['capital_minus_half'][1]} for r in out]}))
if __name__=='__main__':main()
