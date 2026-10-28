"""A076 activation repair v1. Exact Walsh and prime-log checks; bounded pilot."""
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json, time, hashlib
ROOT=Path(__file__).resolve().parents[1]

@lru_cache(None)
def factors(n):
    ans=[]; p=2
    while p*p<=n:
        e=0
        while n%p==0: n//=p; e+=1
        if e: ans.append((p,e))
        p=3 if p==2 else p+2
    if n>1: ans.append((n,1))
    return tuple(ans)

def add(*terms):
    d=defaultdict(Q)
    for expr,c in terms:
        for p,v in expr.items(): d[p]+=c*v
    return {p:v for p,v in d.items() if v}

@lru_cache(None)
def phi(x):
    x=Q(x)
    if not x:return {}
    d=defaultdict(Q)
    for p,e in factors(x.numerator):d[p]-=x*e
    for p,e in factors(x.denominator):d[p]+=x*e
    return {p:v for p,v in d.items() if v}

@lru_cache(None)
def walsh(t):
    z=list(t); h=1
    while h<len(z):
        for b in range(0,len(z),2*h):
            for j in range(b,b+h):z[j],z[j+h]=z[j]+z[j+h],z[j]-z[j+h]
        h*=2
    return tuple(Q(x,len(z)) for x in z)

def ent(c):return add(*[(phi(x*x),Q(1)) for x in c])
def inf(c,indices):return sum((sum((s>>i)&1 for i in indices)*v*v for s,v in enumerate(c)),Q(0))

def ln_unit(x):
    z=(x-1)/(x+1); terms=24
    lo=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
    return lo,lo+2*z**(2*terms+1)/((2*terms+1)*(1-z*z))

LN2=ln_unit(Q(2))
@lru_cache(None)
def logprime(p):
    if p==2:return Q(1),Q(1)
    k=p.bit_length()-1; lo,hi=ln_unit(Q(p,2**k))
    return k+lo/LN2[1],k+hi/LN2[0]

def bounds(expr):
    lo=hi=Q(0)
    for p,v in expr.items():
        a,b=logprime(p);lo+=v*(a if v>=0 else b);hi+=v*(b if v>=0 else a)
    return lo,hi

def leq(expr,rhs):
    # An exact zero in the prime-log representation needs no interval decision.
    residual=add((expr,1),({2:Q(rhs)},-1))
    if not residual:return
    assert bounds(residual)[1]<=0,('not certified',expr,rhs,bounds(residual))

def main():
    begin=time.perf_counter(); checks=0; cases=0; cancellation=0; rare=0
    for nx in (1,2,3):
        ny=2; size=2**nx
        for mask in range(2**size):
            a=tuple((mask>>x)&1 for x in range(size));p=Q(sum(a),size)
            if p>Q(1,2):continue
            ac=walsh(a);J=ent(ac);D=inf(ac,range(nx))
            for vm in range(16):
                V=tuple(1-2*((vm>>y)&1) for y in range(4));vc=walsh(V)
                mu=vc[0];q=1-mu
                ft=tuple(1+a[x]*(V[y]-1) for y in range(4) for x in range(size))
                fc=walsh(ft);H=ent(fc);N=add((H,1),(ent(vc),-p))
                rhs=add((J,2*q),(phi((1-p*q)**2),1),(phi(p*p),-q*q),
                        (phi(q*q),p*(1-p)),(phi(mu*mu),-p))
                assert N==rhs;checks+=1
                assert inf(fc,range(nx))==2*q*D;checks+=1
                assert inf(fc,range(nx,nx+ny))==p*inf(vc,range(ny));checks+=1
                leq(add((N,-1)),0);checks+=1
                leq(add((N,1),(J,-2*q)),5*p*q);checks+=1
                if p:
                    assert D>=p/2;checks+=1
                    leq(add((N,1),(J,-2*q)),5*2*q*D);checks+=1;rare+=1
                if q==0:
                    assert N=={} and inf(fc,range(nx))==0;checks+=1;cancellation+=1
                cases+=1
                assert time.perf_counter()-begin<55,'pilot exceeded 55 seconds'
    bent=[]
    for k in (4,6,8,12,16,24,32):
        delta=Q(1,2**k);r=Q(1,2**(k//2));np=(2**k+2**(k//2))//2;nm=2**k-np
        N={2:2*k*delta}
        for height,count in ((r,np),(-r,nm)):
            N=add((N,1),(phi((height-delta)**2),count),
                  (phi(height**2),Q(-count,2)),(phi((height-2*delta)**2),Q(-count,2)))
        leq(add((N,-1)),-(k-2)*delta);checks+=1
        if k in (4,6):
            G=tuple((-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(k//2)) for y in range(2**k))
            V=tuple(v-2*(y==0) for y,v in enumerate(G))
            F=tuple(G[y] if z==0 else V[y] for y in range(2**k) for z in range(2))
            full=add((ent(walsh(F)),1),(ent(walsh(G)),Q(-1,2)),(ent(walsh(V)),Q(-1,2)))
            assert full==N;checks+=1
            assert inf(walsh(F),(0,))==delta;checks+=1
            assert inf(walsh(F),range(1,k+1))==Q(k,2)+k*delta;checks+=1
        lo,hi=bounds(N)
        bent.append({'k':k,'disagreement':str(delta),'N_over_delta_interval':[str(lo/delta),str(hi/delta)],'lower_bound':k-2})
    result={'status':'PASS','helper_version':'activation-v1','cases':cases,'rare_nonempty_cases':rare,
            'constant_profile_cancellation_cases':cancellation,'exact_assertions':checks,
            'bent_grouped_cases':bent,'elapsed_seconds':time.perf_counter()-begin,
            'arithmetic':'Fraction Walsh coefficients; exact rational prime-exponent entropy identities; 24-term atanh rational log enclosures',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'out'/'VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='bent_grouped_cases'},indent=2))

if __name__=='__main__': main()
