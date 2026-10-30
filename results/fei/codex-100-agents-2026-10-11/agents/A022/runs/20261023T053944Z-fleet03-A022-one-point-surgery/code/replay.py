"""Separate representation: direct characters and degree influence, no helper imports."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]; N=0
def add(*xs):
    z={}
    for x in xs:
        for p,c in x.items(): z[p]=z.get(p,F(0))+c
    return {p:c for p,c in z.items() if c}
def scale(x,c): return {p:c*v for p,v in x.items() if c*v}
@lru_cache(None)
def log(x):
    x=F(x); out={}
    for n,sign in ((x.numerator,1),(x.denominator,-1)):
        p=2
        while p*p<=n:
            while n%p==0: out[p]=out.get(p,0)+sign; n//=p
            p+=1
        if n>1: out[n]=out.get(n,0)+sign
    return {p:F(c) for p,c in out.items() if c}
def number(x): return {2:F(x)} if x else {}
def h(ps): return add(*(scale(log(p),-p) for p in ps if p))
@lru_cache(None)
def spectrum(f):
    return tuple(F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(f))**2,len(f)**2) for s in range(len(f)))
def same(x,y):
    global N
    N+=1; assert not add(x,scale(y,-1)),(x,y)
@lru_cache(None)
def interval(p):
    def ln(q):
        z=(q-1)/(q+1); ans=F(0)
        for j in range(48): ans+=2*z**(2*j+1)/(2*j+1)
        return ans,ans+2*z**97/(97*(1-z*z))
    k=p.bit_length()-1; low,high=ln(F(p,2**k)); al,ah=ln(F(2))
    return k+low/ah,k+high/al
def nonnegative(x):
    global N
    N+=1; lo=F(0)
    for p,c in x.items(): lo+=c*interval(p)[0 if c>0 else 1]
    assert lo>=0,x
def sign(x): return -1 if x==0 else 1
@lru_cache(None)
def leaf(v,d,u,a):
    m=6-d; size=2**m
    table=tuple(sign((u+(x<<d))&7)*sign((u+(x<<d))>>3)*(a[z] if u+(x<<d)==v else 1) for z in range(len(a)) for x in range(size))
    P=spectrum(table); pa=spectrum(a); R=[p/64 for p in pa]; R[0]+=F(63,64)
    c={}
    for label,p in enumerate(P):
        if not p: continue
        s=label%size; T=label//size; prob=R[T]; offset=0
        for block in range(2):
            fixed=max(0,min(3,d-3*block)); rem=3-fixed
            local=s>>offset & ((1<<rem)-1); value=u>>(3*block)&((1<<fixed)-1); offset+=rem
            if fixed==0: prob*=F(9 if local==0 else 1,16)
            if fixed==1: prob*=F(1,4) if value==0 else F(13 if local==0 else 1,16)
            if fixed==2: prob*=F(15 if local==(1 if value==0 else 0) else 1,16)
        c=add(c,scale(log(prob),-p))
    influence=sum(p*(s%size).bit_count() for s,p in enumerate(P))
    return c,h(P),influence,h(pa)
def cut(v,d,nodes):
    C={}; H={}; L={}; I=F(0)
    for u,a,p,path in nodes:
        c,hh,ii,ha=leaf(v,d,u,a); w=p/F(2**d)
        C=add(C,scale(c,w)); H=add(H,scale(hh,w)); I+=w*ii
        if u==v%2**d: L=add(L,scale(ha,p/64))
    return add(number(4*I-F(1,32)),L,scale(C,-1)),add(C,scale(H,-1)),H,L
def phi(q): return scale(log(q),-q) if q else {}
def J(a,d):
    s=F(sum(a),len(a)); r=F(63,64)+s*s/64
    return add(phi(r),scale(phi(s*s),-F(1,64)),number(F(6,64)*(1-s*s)),scale(log(r),1-F(1,2**d)))
def run(v,a):
    nodes=[(0,a,F(1),())]; gamma={}; E={}; K={}; initial=cut(v,0,nodes)
    for d in range(6):
        pure=cut(v,d,[(u,a,F(1),()) for u in range(2**d)])
        current=cut(v,d,nodes)
        same(current[0],add(pure[0],gamma)); same(add(current[0],current[1],E),add(initial[0],initial[1])); same(add(current[3],K),initial[3])
        nonnegative(add(current[0],number(-F(26,576))))
        if d in (1,3):
            result=[]
            for u,aa,p,path in nodes:
                if u!=v%2**d or (d==3 and path!=(0,)):
                    result.append((u,aa,p,path)); continue
                kids=(aa[::2],aa[1::2]); old=leaf(v,d,u,aa); child=[leaf(v,d,u,k) for k in kids]
                g=add(J(aa,d),scale(add(*(J(k,d) for k in kids)),-F(1,2))); nonnegative(g); gamma=add(gamma,scale(g,p))
                dh=add(old[1],scale(add(*(c[1] for c in child)),-F(1,2)))
                dha=add(old[3],scale(add(*(c[3] for c in child)),-F(1,2)))
                E=add(E,scale(dha,p/64),scale(dh,-p/F(2**d))); K=add(K,scale(dha,p/64))
                result.extend((u,k,p/2,path+(b,)) for b,k in enumerate(kids))
            nodes=result
            current=cut(v,d,nodes); same(current[0],add(pure[0],gamma)); same(add(current[0],current[1],E),add(initial[0],initial[1]))
        if d==5: break
        result=[]; old=cut(v,d,nodes)
        for u,aa,p,path in nodes:
            parent=leaf(v,d,u,aa); child=[leaf(v,d+1,u+(b<<d),aa) for b in (0,1)]
            # Spectral-degree difference equals the queried physical pivot.
            pivot=parent[2]-sum(c[2] for c in child)/2
            dh=add(parent[1],scale(add(*(c[1] for c in child)),-F(1,2)))
            E=add(E,scale(add(number(4*pivot),scale(dh,-1)),p/F(2**d)))
            result.extend((u+(b<<d),aa,p,path) for b in (0,1))
        nodes=result; new=cut(v,d+1,nodes)
        nextpure=cut(v,d+1,[(u,a,F(1),()) for u in range(2**(d+1))])
        same(add(new[0],scale(old[0],-1)),add(nextpure[0],scale(pure[0],-1)))
    return
start=time.monotonic()
for v in (0,63):
    for mask in range(16):
        run(v,tuple(1 if mask>>z&1 else -1 for z in range(4)))
        assert time.monotonic()-start<120
# Literal control: inactive half-cube retains ORIGINAL R, with positive
# complete controller CE half*log2(64/63) after active control exhaustion.
witness=scale(log(F(64,63)),F(1,2)); nonnegative(witness)
assert witness
literal=(-1,1,-1,1)
inactive=tuple(sign((1+(x<<1))&7)*sign((1+(x<<1))>>3) for z in range(4) for x in range(32))
actual=spectrum(inactive); R=[p/64 for p in spectrum(literal)]; R[0]+=F(63,64)
physical_cost=add(*(scale(log(R[s//32]),-p/2) for s,p in enumerate(actual) if p))
same(physical_cost,witness)
out={'status':'PASS','cases':32,'assertions':N,'elapsed_seconds':time.monotonic()-start,'representation':'direct characters / degree influence / separate log algebra','inactive_frozen_CE_witness':{str(p):str(c) for p,c in witness.items()},'review':'author reproduction, not independent-person review'}
(ROOT/'out/replay.json').write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out))
