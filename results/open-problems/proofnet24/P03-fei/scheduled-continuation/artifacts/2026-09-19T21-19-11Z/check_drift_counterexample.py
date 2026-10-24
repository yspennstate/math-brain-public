#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache
from dataclasses import dataclass
import hashlib, json, time

@dataclass(frozen=True)
class IV:
    lo:F; hi:F
    def __add__(self,o):
        o=asiv(o); return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asiv(o))
    def __rsub__(self,o): return asiv(o)-self
    def __mul__(self,o):
        o=asiv(o); z=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asiv(o)
        assert not (o.lo<=0<=o.hi)
        return self*IV(1/o.hi,1/o.lo)
def asiv(x): return x if isinstance(x,IV) else IV(F(x),F(x))
@lru_cache(None)
def slog(q):
    q=F(q); assert 1<=q<=2
    z=(q-1)/(q+1); p=z; s=F(0)
    for j in range(80):
        s += 2*p/(2*j+1); p*=z*z
    tail=2*p/(161*(1-z*z))
    return IV(s,s+tail)
LN2=slog(F(2))
@lru_cache(None)
def log2iv(q):
    q=F(q); assert q>0
    k=0
    while q<1:q*=2;k-=1
    while q>=2:q/=2;k+=1
    if q==1:return asiv(k)
    return asiv(k)+slog(q)/LN2
def ent(p):
    p=F(p)
    return asiv(0) if p in (0,1) else -p*log2iv(p)
def entropy(ps):
    s=asiv(0)
    for p in ps:s+=ent(p)
    return s
def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j]=x+y;a[j+h]=x-y
        h*=2
    return a
def canonical(f):
    f=tuple(f);return tuple(x*f[0] for x in f)
def derivative(f,z):
    f=tuple(f);return canonical(tuple(f[x]*f[x^z] for x in range(len(f))))
def probs(f):
    N=len(f);W=fwht(f)
    return tuple(F(w*w,N*N) for w in W)
def H(f): return entropy(probs(f))
def L(f):
    p=probs(f);N=len(f)
    q=[sum((p[s]*p[s^u] for s in range(N)),F(0)) for u in range(N)]
    return 2*entropy(p)-entropy(q)
def rank_add(B,v):
    x=v
    for hb in sorted(B,reverse=True):
        if (x>>hb)&1:x^=B[hb]
    if not x:return False,B
    b=dict(B);b[x.bit_length()-1]=x;return True,b
def dcost(f,v,fold):
    N=len(f);d=sum(f[x]!=f[x^v] for x in range(N));a=F(d,N)
    return min(a,1-a) if fold else a
@lru_cache(None)
def basis_min(f,fold):
    f=tuple(f);n=len(f).bit_length()-1
    items=sorted((dcost(f,v,fold),v) for v in range(1,len(f)))
    B={};s=F(0)
    for w,v in items:
        ok,B2=rank_add(B,v)
        if ok:
            B=B2;s+=w
            if len(B)==n:break
    return s
def M(f):return basis_min(canonical(f),True)
def M0(f):return basis_min(canonical(f),False)
def delta(f):
    f=canonical(f);N=len(f)
    return 2*M(f)-sum((M(derivative(f,z)) for z in range(N)),F(0))/N
def delta0(f):
    f=canonical(f);N=len(f)
    return 2*M0(f)-sum((M0(derivative(f,z)) for z in range(N)),F(0))/N
def Dcross(f):
    f=canonical(f);N=len(f)
    return 2*H(f)-sum((H(derivative(f,z)) for z in range(N)),asiv(0))/N
def gate(f,c):
    f=tuple(f);mask=(1<<c)-1
    return canonical(tuple(f[x>>c] if (x&mask)==0 else 1 for x in range(len(f)*(1<<c))))
def mean(f):return F(sum(f),len(f))
def dec(x,d=12,up=False):
    y=x*10**d;q,r=divmod(y.numerator,y.denominator)
    if up and r:q+=1
    s='-' if q<0 else '';q=abs(q);a,b=divmod(q,10**d)
    return f"{s}{a}.{b:0{d}d}"
def show(iv):
    return {"lower":dec(iv.lo,12,False),"upper":dec(iv.hi,12,True)}

def main():
    t=time.time()
    # Exact seven-bit obstruction to the former candidate L <= 3 Delta_aff.
    A=(0,7,9,12,28,51,56,61,75,84,88,91,106,116)
    f=tuple(-1 if x in A else 1 for x in range(128))
    m=M(f);da=delta(f);l=L(f);dc=Dcross(f)
    assert m==F(15,16) and da==F(1073,2048)
    assert l.lo>3*da
    assert l.lo>F(311,100)*da
    assert dc.lo>F(121,25)*da
    # New exact control-drift identity, exhaustive through three inner bits.
    checks=0
    for n in range(4):
        N=1<<n
        for mask in range(1<<(N-1)):
            f=(1,)+tuple(-1 if (mask>>(x-1))&1 else 1 for x in range(1,N))
            d=1-mean(f)
            d0=delta0(f)
            for c in (3,4):
                p=F(1,1<<c);g=gate(f,c)
                rhs=p*p*d0+2*p*(1-p)*d+c*p*p*d*d
                assert delta(g)==rhs
                checks+=1
    out={
      "full_FEI_proved":False,
      "universal_finite_drift_constant_proved":False,
      "former_candidate_L_le_3_Delta_aff":"REFUTED",
      "counterexample":{
        "variables":7,"negative_set":list(A),"M":str(m),"Delta_aff":str(da),
        "L":show(l),"L_over_Delta":show(l/da),
        "D_cross":show(dc),"D_cross_over_Delta":show(dc/da),
        "certified_lower_bounds":{"L_over_Delta":"> 3.11","D_cross_over_Delta":"> 4.84"}
      },
      "tensor_consequence":"By the previously proved exact tensor additivity of L, D_cross, and Delta_aff, tensor powers give counterexamples in every dimension 7q with the same ratios.",
      "control_drift_identity":{
        "statement":"Delta_aff(Gamma_c f)=p^2 Delta_0(f)+2p(1-p)d+c p^2 d^2 for c>=3, p=2^-c, d=1-Ef, Delta_0=2M_0-E M_0(f_v).",
        "exhaustive_inner_functions_through_bits":3,
        "gate_instances_checked":checks,
        "status":"PASS"
      },
      "arithmetic":"Fraction identities plus outward atanh-series logarithm intervals",
      "status":"PASS","elapsed_seconds":round(time.time()-t,3)
    }
    out["script_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    print(json.dumps(out,indent=2))
    open("/mnt/data/fei_drift_counterexample_checks.json","w").write(json.dumps(out,indent=2)+"\n")
if __name__=="__main__":main()
