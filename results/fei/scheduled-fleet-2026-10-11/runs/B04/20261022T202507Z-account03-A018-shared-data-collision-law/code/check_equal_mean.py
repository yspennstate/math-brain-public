"""A018 v1. Exact, bounded reconstruction; no external checker imports."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, sys, hashlib
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(b):
    global checks
    checks+=1
    assert b
def add(*vs):
    r={}
    for v in vs:
        for p,c in v.items(): r[p]=r.get(p,F(0))+c
    return {p:c for p,c in r.items() if c}
def sc(a,v): return {p:a*c for p,c in v.items() if a*c}
@lru_cache(None)
def factors(n):
    r={}; p=2
    while p*p<=n:
        while n%p==0: r[p]=r.get(p,0)+1; n//=p
        p+=1
    if n>1:r[n]=r.get(n,0)+1
    return r
@lru_cache(None)
def lg(x):
    x=F(x); assert x>0
    return add(factors(x.numerator),sc(-1,factors(x.denominator)))
def ent(P): return add(*(sc(-p,lg(p)) for p in P if p))
def ce(P,Q):
    ck(sum(Q)==1)
    return add(*(sc(-p,lg(q)) for p,q in zip(P,Q) if p))
def kl(P,Q): return add(ce(P,Q),sc(-1,ent(P)))
@lru_cache(None)
def lnint(p):
    k=p.bit_length()-1; x=F(p,2**k); z=(x-1)/(x+1)
    def atanh(z):
        v=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0))
        return v,v+2*z**73/(73*(1-z*z))
    lo,hi=atanh(z); a,b=atanh(F(1,3))
    return lo+k*a,hi+k*b
def interval(v):
    lo=hi=F(0)
    for p,c in v.items():
        a,b=lnint(p)
        lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    return lo,hi
def nonneg(v):
    if not v:return True
    return interval(v)[0]>=0
def walsh(t):
    a=list(t); n=len(a);step=1
    while step<n:
        for i in range(0,n,2*step):
            for j in range(i,i+step):a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
        step*=2
    a=tuple(F(x,n) for x in a)
    direct=tuple(F(sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(n)),n) for s in range(n))
    ck(a==direct)
    return a
def probs(a):return tuple(x*x for x in a)
def refs(P):
    n=len(P)
    return (P,tuple((p+int(i==0))/2 for i,p in enumerate(P)),tuple(F(i+1,n*(n+1)//2) for i in range(n)))
def lift(a0,a1,Q0,Q1):
    a=[];Q=[]
    for u,(x,y) in enumerate(zip(a0,a1)):
        v,w=(x+y)/2,(x-y)/2;r=v*v+w*w;q=(Q0[u]+Q1[u])/2
        # q is the least significant Fourier coordinate. Fix absent on zero true rows.
        nu=v*v/r if r else F(1)
        a.extend((v,w));Q.extend((nu*q,(1-nu)*q))
    return tuple(a),tuple(Q)
def refund(p,t):
    # Bits represented as exact rational combinations of log_2(primes).
    r={}
    if p:r=add(r,sc(p/2,lg(p/t)))
    return add(r,sc((1+p)/2,lg((1+t)/(1+p))))
def psi(mu):
    return add(ent(((1+mu)**2/4,(1-mu)**2/4)),sc(1-mu*mu,lg(F(2))),sc(-F(1,2),ent((mu*mu,))))
def activation(a,Q,s,Qs):
    n=len(a);G=tuple(x*y for y in s for x in a);QG=tuple(x*y for y in Qs for x in Q)
    out=[];ref=[]
    for u,(g,q) in enumerate(zip(G,QG)):
        v,w=(1+g)/2,(1-g)/2 if u==0 else (None,None)
        if u:
            v=w=g/2
        row=v*v+w*w;qr=(q+int(u==0))/2
        nu=v*v/row if row else F(1)
        out.extend((v,w));ref.extend((nu*qr,(1-nu)*qr))
    P=probs(out);ck(sum(P)==1)
    cost=ce(P,ref);p=(a[0]*s[0])**2;t=Q[0]*Qs[0]
    D=refund(p,t)
    ck(cost==add(sc(F(1,2),add(ce(probs(a),Q),ce(probs(s),Qs))),psi(a[0]*s[0]),sc(-1,D)))
    return cost,D
def run(pilot=False):
    started=time.perf_counter();cases=nonbalanced=balanced=0;witness=None
    masks=[walsh((1,-1)),walsh((-1,1,1,1)),walsh((1,-1,-1,-1))]
    for m in ([1] if pilot else [1,2]):
        N=2**m
        for t0 in range(2**N):
            tt0=tuple(1-2*((t0>>x)&1) for x in range(N));a0=walsh(tt0);P0=probs(a0)
            for t1 in range(2**N):
                tt1=tuple(1-2*((t1>>x)&1) for x in range(N));a1=walsh(tt1)
                if a0[0]!=a1[0]:continue
                P1=probs(a1);beta=a0[0]
                actual=tuple(v for pair in zip(tt0,tt1) for v in pair)
                d=F(sum(x!=y for x,y in zip(tt0,tt1)),N)
                for Q0 in refs(P0):
                    for Q1 in refs(P1):
                        ah,Qh=lift(a0,a1,Q0,Q1);ck(ah==walsh(actual));Ph=probs(ah)
                        dc=add(sc(F(1,2),add(kl(P0,Q0),kl(P1,Q1))),sc(-1,kl(Ph,Qh)))
                        ch=ce(Ph,Qh);DH=add(ent(Ph),sc(-F(1,2),add(ent(P0),ent(P1))))
                        ck(ch==add(sc(F(1,2),add(ce(P0,Q0),ce(P1,Q1))),DH,sc(-1,dc)))
                        ck(Qh[0]==(Q0[0]+Q1[0])/2)
                        de={}
                        if beta:de=sc(beta*beta,add(lg((Q0[0]+Q1[0])/2),sc(-F(1,2),add(lg(Q0[0]),lg(Q1[0])))))
                        ck(nonneg(de));ck(nonneg(add(dc,sc(-1,de))))
                        for s in masks:
                            Ps=probs(s)
                            for Qs in (Ps,tuple(F(1,len(Ps)) for _ in Ps)):
                                c,D=activation(ah,Qh,s,Qs);c0,D0=activation(a0,Q0,s,Qs);c1,D1=activation(a1,Q1,s,Qs)
                                lam=add(sc(F(1,2),add(D0,D1)),sc(-1,D),sc(-F(1,2),dc))
                                a=Qs[0];m2=s[0]*s[0];p=beta*beta*m2
                                J=add(lg(1+a*(Q0[0]+Q1[0])/2),sc(-F(1,2),add(lg(1+a*Q0[0]),lg(1+a*Q1[0]))))
                                exact=sc(-F(1,2),add(dc,sc(-m2,de),sc(1+p,J)))
                                ck(lam==exact);ck(nonneg(J));ck(nonneg(sc(-1,lam)))
                                ck(add(c,sc(-F(1,2),add(c0,c1)))==add(sc(F(1,2),DH),lam))
                                ck(nonneg(add(sc(F(1,2),DH),sc(-1,add(c,sc(-F(1,2),add(c0,c1)))))))
                                # Direct parent spectrum checked against actual activation truth table once per case.
                                infq=sum(Ph[j] for j in range(len(Ph)) if j&1);ck(infq==d)
                                cases+=1
                                if beta:nonbalanced+=1
                                else:balanced+=1
                                if witness is None and beta and d and Q0!=Q1:
                                    witness={'m':m,'tables':[t0,t1],'beta':str(beta),'d':str(d),'Lambda':{str(k):str(v) for k,v in lam.items()}}
        (ROOT/'out'/'CHECKPOINT.json').write_text(json.dumps({'m_completed':m,'cases':cases,'checks':checks}),encoding='utf-8')
    result={'helper':'A018-equal-mean-v1','pilot':pilot,'cases':cases,'balanced':balanced,'nonbalanced':nonbalanced,'assertions':checks,'seconds':time.perf_counter()-started,'witness':witness,'arithmetic':'Fraction spectra; exact prime-log identities; 36-term outward rational atanh signs','status':'PASS'}
    (ROOT/'out'/('PILOT.json' if pilot else 'CHECKS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
