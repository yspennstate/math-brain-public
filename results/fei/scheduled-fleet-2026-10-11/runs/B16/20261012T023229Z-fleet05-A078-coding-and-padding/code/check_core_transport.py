"""Actual Boolean arbitrary-core transport; exact fourth-root normal forms."""
import argparse, json, time
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict

START=time.monotonic(); COUNT=0
def check(ok):
    global COUNT
    COUNT+=1
    assert ok
    if time.monotonic()-START>55: raise TimeoutError('frozen 55 second guard')

def walsh(table):
    n=len(table)
    return [sum(table[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(n)) for s in range(n)]

def pair(table,i):
    out=[[],[]]
    for x in range(len(table)//2):
        low=x&((1<<i)-1); high=x>>i
        a=low+(high<<(i+1)); b=a+(1<<i)
        out[0].append(F(table[a]+table[b],2)); out[1].append(F(table[a]-table[b],2))
    return walsh(out[0]),walsh(out[1]),len(table)//2

def factors(n):
    result={}; p=2
    while p*p<=n:
        while n%p==0: result[p]=result.get(p,0)+1; n//=p
        p+=1
    if n>1: result[n]=result.get(n,0)+1
    return result

def root4(q):
    q=F(q)
    if not q: return 1,F(0)
    e=defaultdict(int)
    for p,v in factors(q.numerator).items(): e[p]+=v
    for p,v in factors(q.denominator).items(): e[p]-=v
    rad=1; coeff=F(1)
    for p,v in e.items():
        a,b=divmod(v,4); coeff*=F(p)**a; rad*=p**b
    return rad,coeff

def add(dst,rad,coeff):
    dst[rad]=dst.get(rad,F(0))+coeff
    if not dst[rad]: del dst[rad]

def term(a,b): return root4(F(a)**2*F(b)**6)
def plus_scaled(dst,src,q):
    for rad,c in src.items(): add(dst,rad,c*q)
def profile(u,v,D):
    out={}
    for a,b in zip(u,v):
        rad,c=term(F(a,D),F(b,D)); add(out,rad,c)
    return out

def influence(v,D): return sum(F(b,D)**2 for b in v)

def run(pilot):
    mixed=activation=free=0; cores=0
    for k in ([1,2] if pilot else [1,2,3]):
        masks=range(1<<(1<<k)) if k<3 else [0,1,7,15,23,105,150,255]
        for mask in masks:
            g=[1-2*((mask>>x)&1) for x in range(1<<k)]; cores+=1
            for i in range(k):
                u,v,D=pair(g,i); P=profile(u,v,D); alpha=influence(v,D)
                mu=F(u[0],D); nu=F(v[0],D)
                check(abs(nu)<=alpha); check(all(a*b==0 for a,b in zip(u,v))==(not P))
                if not P: free+=1
                for m in [2,4]:
                    table=[]
                    for x in range(1<<(m+k)):
                        ordinary=x&((1<<m)-1); core=x>>m
                        s=m-2*ordinary.bit_count()+g[core]
                        table.append(1 if s>0 else -1)
                    U,V,DD=pair(table,m+i)
                    from math import comb
                    a=F(comb(m,m//2),1<<m); expected={}
                    plus_scaled(expected,P,a)
                    check(profile(U,V,DD)==expected); check(influence(V,DD)==a*alpha)
                    mixed+=1
                for s in [1,2]:
                    table=[g[x>>s] if (x&((1<<s)-1))==0 else 1 for x in range(1<<(s+k))]
                    U,V,DD=pair(table,s+i); p=F(1,1<<s)
                    expected={}; plus_scaled(expected,P,p)
                    rad,c=term(mu,nu); add(expected,rad,-p*c)
                    rad,c=term(1-mu,nu); add(expected,rad,p*(1-p)*c)
                    rad,c=root4(p**6*(1-p+p*mu)**2*nu**6); add(expected,rad,c)
                    check(profile(U,V,DD)==expected); check(influence(V,DD)==p*alpha)
                    # Full physical influence identity, all coordinates separately.
                    total=F(0)
                    for j in range(s+k):
                        _,vv,ddd=pair(table,j); total+=influence(vv,ddd)
                    coreI=sum(influence(pair(g,j)[1],D) for j in range(k))
                    mean=F(sum(g),1<<k)
                    check(total==p*coreI+s*p*(1-mean))
                    activation+=1
    return {'status':'PASS','helper_version':'core-quarter-transport-v1','pilot':pilot,
            'assertions':COUNT,'core_truth_tables':cores,'mixed_pairs':mixed,'activation_pairs':activation,
            'zero_profile_core_pairs':free,'seconds':time.monotonic()-START,
            'arithmetic':'Exact Walsh/Fraction; coefficientwise fourth-root identities',
            'universal_claim':'Analytic proof in CORE_TRANSPORT_PROOF.md; finite checks alone do not extrapolate'}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
    result=run(args.pilot); out=Path(__file__).resolve().parents[1]/'out'
    (out/('core_transport_pilot.json' if args.pilot else 'core_transport_full.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
