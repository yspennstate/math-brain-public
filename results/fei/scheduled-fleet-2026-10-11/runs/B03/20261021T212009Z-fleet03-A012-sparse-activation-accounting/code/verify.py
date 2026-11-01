"""Separate Fraction logarithms, direct character sums, exact octree coverage."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1];N=32;S=1<<60;checks=0
def ck(x):
    global checks
    assert x;checks+=1
@lru_cache(None)
def ln(z):
    u=(z-1)/(z+1);ck(0<=u<=F(1,3));power=u;sm=F(0)
    for j in range(N):sm+=2*power/(2*j+1);power*=u*u
    return sm,sm+2*power/((2*N+1)*(1-u*u))
ll,lh=ln(F(2))
@lru_cache(None)
def loghi(n,d):
    z=F(n,d);k=0
    while z>=2:z/=2;k+=1
    lo,hi=ln(z)
    q=(k+hi/ll)*S
    return -(-q.numerator//q.denominator)
def chars(t,s):return (-1)**((t&s).bit_count()%2)
def verify(job):
    global checks
    t0=time.perf_counter();data=json.loads((R/'out'/f'CONTINUUM_{job}.json').read_text(encoding='utf-8'))
    ck(data['status']=='PASS');ck(not data['unresolved']);m=data['mask'];c=[(-1)**((m>>s)&1) for s in range(8)]
    P=[(sum(c[s]*chars(t,s) for s in range(8)),[c[s]*chars(t,s) for s in range(3)]) for t in range(8)]
    occupied=set();volume=F(0);minimum=None
    for rec in data['leaves']+data['pruned']:
        ix,dep=rec[:2];key=(tuple(ix),dep);ck(key not in occupied);occupied.add(key);volume+=F(1,1<<(3*dep))
        den=1<<dep
        if rec[2]=='rare':ck(4*(sum(ix)+3)<=den);continue
        if rec[2]=='moderate':ck(3*sum(ix)>=4*den);continue
        mid=[F(2*x+1,2*den) for x in ix];sl=[]
        for a,v in P:
            if a==0:continue
            b=sum(v[j]*mid[j] for j in range(3));A=(a-b)**2;B=b*b
            r=F(1,1024) if not B else F(1023,1024) if not A else B/(A+B)
            lam=loghi(r.denominator,r.denominator-r.numerator);mu=loghi(r.denominator,r.numerator)
            ck(lam+mu>=2*S);sl.append((a,v,lam,mu))
        mx=None
        for bits in product((0,1),repeat=3):
            p=[ix[j]+bits[j] for j in range(3)];val=-16*den*S*sum(p)
            for a,v,lam,mu in sl:
                k=sum(v[j]*p[j] for j in range(3));val+=lam*(a*den-k)**2+(mu-2*S)*k*k
            mx=val if mx is None else max(mx,val)
        ck(mx<0);margin=F(-mx,64*den*den*S)
        minimum=margin if minimum is None else min(minimum,margin)
        if time.perf_counter()-t0>52:raise RuntimeError('52-second verification cap; incomplete, not PASS')
    ck(volume==1)
    for ix,dep in occupied:
        for d in range(2,dep):ck((tuple(x>>(dep-d) for x in ix),d) not in occupied)
    out={'job':job,'status':'PASS','exact_assertions':checks,'leaves':len(data['leaves']),'pruned':len(data['pruned']),'minimum_gap':str(minimum),'seconds':time.perf_counter()-t0,'arithmetic':'Fraction32-term atanh, actual rational tail; independent60-bit rounding; direct Walsh; exact octree coverage'}
    (R/'out'/f'VERIFY_{job}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out));checks=0;loghi.cache_clear();ln.cache_clear()
if __name__=='__main__':
    for job in map(int,sys.argv[1:]):verify(job)
