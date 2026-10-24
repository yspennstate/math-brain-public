#!/usr/bin/env python3
"""Exact/self-contained checks for the FEI affine-drift route.

Main tested candidate (NOT claimed universally proved by this script):
    L(f) = H(S | S xor T) <= 3 * Delta_aff(f),
where M=Ifrak is minimum affine influence and
    Delta_aff(f)=2M(f)-E_z M(f f^z).

All acceptance decisions use Fraction arithmetic and outward rational
logarithm intervals. The script also certifies the finite n<=7 part of the
all-dimensional one-point-defect theorem proved in the companion report.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import hashlib, json, sys, time
from pathlib import Path

@dataclass(frozen=True)
class IV:
    lo:F; hi:F
    def __post_init__(self):
        if self.lo > self.hi: raise ValueError("reversed")
    @staticmethod
    def point(x): return IV(F(x),F(x))
    def __add__(self,o):
        o=asiv(o); return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asiv(o))
    def __rsub__(self,o): return asiv(o)-self
    def __mul__(self,o):
        o=asiv(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asiv(o)
        if o.lo <= 0 <= o.hi: raise ZeroDivisionError
        return self*IV(1/o.hi,1/o.lo)
def asiv(x): return x if isinstance(x,IV) else IV.point(x)

@lru_cache(None)
def small_log(q:F)->IV:
    if not F(1) <= q <= F(2): raise ValueError(q)
    z=(q-1)/(q+1); p=z; total=F(0)
    for j in range(64):
        total += 2*p/(2*j+1)
        p *= z*z
    tail=2*p/(129*(1-z*z))
    return IV(total,total+tail)
LN2=small_log(F(2))

@lru_cache(None)
def log2_iv(q:F)->IV:
    q=F(q)
    if q<=0: raise ValueError(q)
    k=0
    while q<1: q*=2; k-=1
    while q>=2: q/=2; k+=1
    if q==1: return IV.point(k)
    return IV.point(k)+small_log(q)/LN2

@lru_cache(None)
def ent_term(p:F)->IV:
    if p==0 or p==1: return IV.point(0)
    return -p*log2_iv(p)

def entropy_iv(probs):
    out=IV.point(0)
    for p in probs:
        out += ent_term(F(p))
    return out

def dec(x:F, digits=12, upper=False):
    y=x*10**digits
    q,r=divmod(y.numerator,y.denominator)
    if upper and r: q+=1
    s='-' if q<0 else ''; q=abs(q)
    a,b=divmod(q,10**digits)
    return f"{s}{a}.{b:0{digits}d}"

def show(v:IV,d=12):
    return {"lower":dec(v.lo,d,False),"upper":dec(v.hi,d,True)}

def fwht(a):
    a=list(a); w=1
    while w<len(a):
        for s in range(0,len(a),2*w):
            for j in range(s,s+w):
                x,y=a[j],a[j+w]; a[j]=x+y; a[j+w]=x-y
        w*=2
    return a

def canonical(f):
    f=tuple(f)
    return tuple(v*f[0] for v in f)

def derivative(f,z):
    return canonical(tuple(f[x]*f[x^z] for x in range(len(f))))

def spectral_probs(f):
    N=len(f)
    W=fwht(f)
    den=N*N
    return tuple(F(w*w,den) for w in W)

def L_iv(f):
    p=spectral_probs(f); N=len(p)
    q=[F(0) for _ in range(N)]
    for u in range(N):
        q[u]=sum((p[s]*p[s^u] for s in range(N)),F(0))
    return 2*entropy_iv(p)-entropy_iv(tuple(q))

def direction_cost(f,v):
    N=len(f)
    diff=sum(1 for x in range(N) if f[x]!=f[x^v])
    a=F(diff,N)
    return min(a,1-a)

def rank_insert(basis,v):
    # basis is a dict pivot_bit -> row, maintained as an upper-triangular GF(2) basis.
    x=v
    for hb in sorted(basis, reverse=True):
        if (x>>hb)&1:
            x ^= basis[hb]
    if x==0:
        return False,basis
    hb=x.bit_length()-1
    b2=dict(basis); b2[hb]=x
    return True,b2

@lru_cache(None)
def M_cached(f):
    f=tuple(f); n=(len(f)).bit_length()-1
    items=sorted((direction_cost(f,v),v) for v in range(1,1<<n))
    basis={}; cost=F(0)
    for w,v in items:
        ok,b2=rank_insert(basis,v)
        if ok:
            basis=b2; cost+=w
            if len(basis)==n: break
    assert len(basis)==n
    return cost

def delta_M(f):
    f=canonical(f); N=len(f)
    m=M_cached(f)
    av=sum((M_cached(derivative(f,z)) for z in range(N)),F(0))/N
    return 2*m-av

def onepoint(n, points=(0,)):
    N=1<<n; A=set(points)
    return canonical(tuple(-1 if x in A else 1 for x in range(N)))

def ratio_iv(num:IV, den:F):
    return num/den

def check_function(f):
    d=delta_M(f)
    L=L_iv(f)
    if d==0:
        ok=(L.hi==0); r=IV.point(0)
    else:
        ok=L.hi <= 3*d
        r=L/d
    return ok,L,d,r,M_cached(canonical(f))

def quadratic_phase(n):
    assert n%2==0
    vals=[]
    for x in range(1<<n):
        bit=0
        for i in range(0,n,2):
            bit ^= ((x>>i)&1)&((x>>(i+1))&1)
        vals.append(-1 if bit else 1)
    return canonical(tuple(vals))

def addressing_m2():
    # f(z,x1,x2,y00,y01,y10,y11): z bit 0 means +1 branch g(x), z bit 1 data y_x.
    # g(x)=(-1)^(x1*x2), all variables encoded as bits with sign (-1)^bit for y.
    n=7; vals=[]
    for t in range(1<<n):
        z=t&1; x=(t>>1)&3
        if z==0:
            bit=((x&1)&((x>>1)&1))
        else:
            a=x
            bit=(t>>(3+a))&1
        vals.append(-1 if bit else 1)
    return canonical(tuple(vals))

def main():
    t0=time.time()
    out={"full_FEI_proved":False,"candidate_universal_L_le_3_delta_proved":False,
         "arithmetic":"Fraction plus outward 64-term atanh logarithm intervals"}
    # Exhaustive canonical functions through n=4.
    ex={}
    for n in range(1,5):
        N=1<<n; total=1<<(N-1)
        max_hi=F(-1); max_rec=None; violations=0
        for mask in range(total):
            f=(1,)+tuple(-1 if (mask>>(x-1))&1 else 1 for x in range(1,N))
            ok,L,d,r,M=check_function(f)
            if not ok: violations+=1
            if d and r.hi>max_hi:
                max_hi=r.hi
                neg=[i for i,v in enumerate(f) if v==-1]
                max_rec=(neg,show(r),show(L),str(d),str(M))
        ex[str(n)]={"canonical_functions":total,"violations":violations,
                    "max_L_over_delta": max_rec}
        assert violations==0
    out["exhaustive_n_le_4"]=ex

    # One-point finite core n=2..7; report proof handles n>=8 analytically.
    ops=[]
    for n in range(2,8):
        f=onepoint(n)
        ok,L,d,r,M=check_function(f); assert ok
        a=F(1,1<<(n-1))
        expected_delta=(F(2) if n==2 else 2*a+(n-1)*a*a)
        assert d==expected_delta
        ops.append({"n":n,"M":str(M),"delta":str(d),"L":show(L),
                    "L_over_delta":show(r)})
    out["onepoint_finite_core"]=ops
    out["onepoint_tail_analytic_start_n"]=8

    # Quadratic phases: exact structural benchmark.
    qs=[]
    for n in (2,4,6):
        f=quadratic_phase(n)
        ok,L,d,r,M=check_function(f); assert ok
        qs.append({"n":n,"M":str(M),"delta":str(d),"L":show(L),"ratio":show(r)})
    out["quadratic_phases"]=qs

    # Structured adversarial examples, exact.
    fixed=[
        ("n5_three_point",(1,10,26),5),
        ("n6_seven_point",(57,52,51,44,28,43,9),6),
    ]
    fs=[]
    for name,A,n in fixed:
        f=onepoint(n,A)
        ok,L,d,r,M=check_function(f); assert ok
        fs.append({"name":name,"minority_set":list(A),"M":str(M),"delta":str(d),
                   "L":show(L),"L_over_delta":show(r)})
    out["fixed_sparse_stress"]=fs

    f=addressing_m2()
    ok,L,d,r,M=check_function(f); assert ok
    out["addressing_m2"]={"M":str(M),"delta":str(d),"L":show(L),"ratio":show(r)}

    script=Path(__file__).read_bytes()
    out["script_sha256"]=hashlib.sha256(script).hexdigest()
    out["elapsed_seconds"]=round(time.time()-t0,3)
    out["status"]="PASS"
    dest=Path(sys.argv[1] if len(sys.argv)>1 else "affine_drift_checks.json")
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
