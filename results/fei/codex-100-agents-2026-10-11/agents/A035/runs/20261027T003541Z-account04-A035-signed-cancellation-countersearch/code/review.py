"""Independent exact review; standard library, no imported campaign helper."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools, json, time, sys

ROOT = Path(__file__).resolve().parents[1]

@lru_cache(None)
def factors(n):
    out = {}; d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0)+1; n //= d
        d += 1
    if n > 1: out[n] = out.get(n, 0)+1
    return out

def addlog(out, coefficient, q):
    if not coefficient: return
    assert q > 0
    for n, sign in [(q.numerator,1),(q.denominator,-1)]:
        for p,e in factors(n).items():
            out[p] = out.get(p,F(0))+coefficient*sign*e

def combine(*terms):
    out = {}
    for c, form in terms:
        for p,v in form.items(): out[p] = out.get(p,F(0))+c*v
    return {p:v for p,v in out.items() if v}

def kl(p,q):
    out = {}
    for a,b in zip(p,q):
        if a: addlog(out,a,a/b)
    return out

@lru_cache(None)
def ln_interval(n):
    # Reduce to [1,2], then atanh series with an explicit geometric tail.
    k = n.bit_length()-1; x = F(n,2**k); t = (x-1)/(x+1)
    def series(z):
        s = sum((2*z**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
        err = 2*z**41/(41*(1-z*z))
        return s,s+err
    a,b = series(t); c,d = series(F(1,3))
    return a+k*c,b+k*d

def bounds(form):
    lo=hi=F(0)
    for p,c in form.items():
        a,b=ln_interval(p)
        lo += c*(a if c>=0 else b); hi += c*(b if c>=0 else a)
    return lo,hi

def walsh(table):
    a=list(table); h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return [F(x,len(table)) for x in a]

def partitions(n):
    def rec(a):
        if len(a)==n:
            yield [[j for j,v in enumerate(a) if v==k] for k in range(max(a)+1)]
        else:
            for k in range(max(a)+2): yield from rec(a+[k])
    yield from rec([0])

def run(pilot=False):
    start=time.monotonic(); cases=checks=strict=single=ghost=zero=0
    parts=list(partitions(4)); assert len(parts)==15
    for mask in range(16 if pilot else 256):
        table=[1-2*((mask>>j)&1) for j in range(8)]
        h=walsh(table); hp=walsh(table[::2]); hm=walsh(table[1::2])
        # Different representation: direct characters and full signed autocorrelation.
        direct=[sum(F(table[x]*(-1)**((s&x).bit_count()),8) for x in range(8)) for s in range(8)]
        assert h==direct; checks+=1
        for shift in range(8):
            assert sum(h[s]*h[s^shift] for s in range(8)) == (1 if shift==0 else 0)
            checks+=1
        for j in range(4):
            assert hp[j]==h[2*j]+h[2*j+1] and hm[j]==h[2*j]-h[2*j+1]; checks+=1
        p=[x*x for x in hp]; q=[x*x for x in hm]; a=[(x+y)/2 for x,y in zip(p,q)]
        candidates=[]
        for t in [F(1,4),F(1,2)]:
            candidates.append(([(1-t)*x+t*y for x,y in zip(p,q)], [t*x+(1-t)*y for x,y in zip(p,q)]))
        candidates.append(([F(j,10) for j in [1,2,3,4]], [F(j,10) for j in [4,3,2,1]]))
        for rp,rm in candidates:
            m=[(x+y)/2 for x,y in zip(rp,rm)]
            fine=combine((F(1,2),kl(p,rp)),(F(1,2),kl(q,rm)))
            js=combine((F(1,2),kl(p,a)),(F(1,2),kl(q,a)))
            # Full transaction at Q with true parent occupancy and prescribed marginal m.
            parent=[x*x for x in h]; ref=[]
            for j in range(4):
                ref.extend([m[j]*parent[2*j]/a[j],m[j]*parent[2*j+1]/a[j]] if a[j] else [m[j]/2,m[j]/2])
            assert sum(ref)==1
            old=kl(parent,ref); assert combine((1,old),(-1,kl(a,m)))=={}; checks+=2
            # Exact formal-log cancellation includes conditional occupancy (zero here).
            ce_parent={}; ce_children={}; erasure={}
            for x,y in zip(parent,ref):
                if x: addlog(ce_parent,-x,y)
            for j in range(4):
                for x in parent[2*j:2*j+2]:
                    if x: addlog(erasure,-x,x/a[j])
                if p[j]: addlog(ce_children,-p[j]/2,rp[j])
                if q[j]: addlog(ce_children,-q[j]/2,rm[j])
            assert combine((1,erasure),(1,ce_children),(-1,ce_parent),(-1,fine),(1,js),(1,old))=={}; checks+=1
            for blocks in parts:
                coarse={}; phi=F(0)
                for block in blocks:
                    ap=sum(p[j] for j in block); am=sum(q[j] for j in block)
                    u=sum(rp[j] for j in block); v=sum(rm[j] for j in block)
                    if ap: addlog(coarse,ap/2,ap/u)
                    if am: addlog(coarse,am/2,am/v)
                    ghost += any(a[j]==0 and m[j]>0 for j in block)
                    if ap and am:
                        e=[u*p[j]/ap+v*q[j]/am-2*m[j] for j in block]
                        ep=[rp[j]-u*p[j]/ap for j in block]; em=[rm[j]-v*q[j]/am for j in block]
                        assert all(x+y==-z for x,y,z in zip(ep,em,e))
                        W=u*u/ap+v*v/am
                        E=sum(abs(x) for x in e); X=sum(abs(x) for x in ep); Y=sum(abs(x) for x in em)
                        # Cleared-denominator Cauchy certificate, including the lost-sign guard.
                        assert E<=X+Y
                        assert W*(ap*X*X/(u*u)+am*Y*Y/(v*v))-(X+Y)**2 == (ap*v*X/(u*u) - am*Y/v)**2*u*u/(ap*am)
                        phi+=E*E/(4*W); checks+=3
                    elif ap or am:
                        single+=1; z,weight,r,R=(p,ap,u,rp) if ap else (q,am,v,rm)
                        overflow=sum(max(F(0),r*z[j]/weight-2*m[j]) for j in block)
                        assert sum(abs(R[j]-r*z[j]/weight) for j in block)>=2*overflow
                        phi+=weight*overflow*overflow/(r*r); checks+=1
                    else: zero+=1
                gap=combine((1,fine),(-1,coarse)); lo,hi=bounds(gap)
                assert lo>=phi or (not gap and phi==0), (mask,blocks,str(lo),str(phi))
                strict+=phi>0; cases+=1; checks+=1
        assert time.monotonic()-start < (55 if pilot else 180), 'frozen runtime cap'
    result={'status':'PASS','cases':cases,'checks':checks,'positive_phi_cases':strict,'singly_occupied_blocks':single,'ghost_blocks':ghost,'empty_actual_blocks':zero,'seconds':round(time.monotonic()-start,6),'ln_series_terms':20,'pilot':pilot}
    (ROOT/'out'/('PILOT.json' if pilot else 'REVIEW_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8'); print(json.dumps(result))

if __name__=='__main__': run('--pilot' in sys.argv)
