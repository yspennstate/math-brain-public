"""Exact rational enclosures for a Boolean FEI drift obstruction.
No floating point is used for acceptance. Logs are enclosed by an atanh series.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import json, math, pathlib, hashlib

@dataclass(frozen=True)
class IV:
    lo: F
    hi: F
    def __post_init__(self):
        assert self.lo <= self.hi
    @staticmethod
    def point(x):
        return IV(F(x),F(x))
    def __add__(self,other):
        b=other if isinstance(other,IV) else IV.point(other)
        return IV(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,other): return self+-asiv(other)
    def __rsub__(self,other): return asiv(other)+-self
    def __mul__(self,other):
        b=asiv(other); c=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return IV(min(c),max(c))
    __rmul__=__mul__
    def __truediv__(self,other):
        b=asiv(other); assert not b.lo<=0<=b.hi
        return self*IV(1/b.hi,1/b.lo)
    def __rtruediv__(self,other): return asiv(other)/self

def asiv(x): return x if isinstance(x,IV) else IV.point(x)

@lru_cache(None)
def small_log(q:F) -> IV:
    assert 1<=q<=2
    z=(q-1)/(q+1); z2=z*z; power=z; value=F(0)
    terms=64
    for j in range(terms):
        value+=2*power/(2*j+1); power*=z2
    tail=2*power/((2*terms+1)*(1-z2))
    return IV(value,value+tail)

LN2=small_log(F(2))
@lru_cache(None)
def log_iv(q:F)->IV:
    q=F(q); assert q>0
    e=0
    while q<1: q*=2;e-=1
    while q>=2: q/=2;e+=1
    return e*LN2+small_log(q)

def log2_iv(q): return log_iv(F(q))/LN2

def fwht(v):
    a=list(v); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a

def truth_from_anf(n, masks):
    return tuple((-1)**sum((x&s)==s for s in masks) for x in range(1<<n))

def restrict_truth(f,i):
    return tuple(y for x,y in enumerate(f) if not x&(1<<i))

def entropy_from_spectrum(f):
    N=len(f); w=fwht(f); p=[F(c*c,N*N) for c in w]
    assert sum(p)==1
    return sum((-q*log2_iv(q) for q in p if q),IV.point(0)),p

def psi(j):
    if not j: return IV.point(0)
    if j<=F(1,8): return j-j*j*log_iv(1/j)
    u=F(1,8); slope=F(9,8)-log_iv(F(8))/4
    return u-u*u*log_iv(F(8))+slope*(j-u)

def row_potential(j,t):
    P=sum((psi(x) for x in j),IV.point(0))
    L=sum((x*x*log2_iv(1/x)/(x+sum(row)) for x,row in zip(j,t) if x),IV.point(0))
    R=sum((x*x/(x+sum(row)) for x,row in zip(j,t) if x),F(0))
    return P,L,R

@lru_cache(None)
def metrics(f):
    N=len(f);n=N.bit_length()-1; assert N==1<<n and set(f)<=set((-1,1))
    H,p=entropy_from_spectrum(f)
    inf=[F(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N) for i in range(n)]
    for i in range(n): assert inf[i]==sum(p[s] for s in range(N) if s&(1<<i))
    j=[min(v,1-v) for v in inf]
    t=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(i):
            bad=sum(f[x]*f[x^(1<<i)]*f[x^(1<<k)]*f[x^(1<<i)^(1<<k)]<0 for x in range(N))
            t[i][k]=t[k][i]=F(bad,4*N)
    P,L,R=row_potential(j,t)
    return H,P,L,R,j,t,p

def show(q:IV,places=12):
    scale=10**places
    lo=(q.lo*scale).__floor__(); hi=(q.hi*scale).__ceil__()
    return {'lower':str(F(lo,scale)),'upper':str(F(hi,scale)),
            'decimal_lower':str(lo/scale),'decimal_upper':str(hi/scale)}

def main():
    n=5; masks=[7,11,13,19,21,25]; f=truth_from_anf(n,masks);N=len(f)
    H,P,L,R,j,t,p=metrics(f)
    Hg=[];Pg=[];Lg=[];gains=[];shift_rows=[]
    for z in range(N):
        g=tuple(f[x]*f[x^z] for x in range(N)); h,pp,ll,rr,jj,tt,pr=metrics(g)
        Hg.append(h);Pg.append(pp);Lg.append(ll)
        gs=[]
        for i in range(n):
            if not z&(1<<i): continue
            hq,pq,lq,rq,jq,tq,prq=metrics(restrict_truth(g,i))
            # Check entropy-preserving label bijection by exact coefficient masses.
            assert sorted(v for v in pr if v)==sorted(v for v in prq if v)
            rem=[v for v in range(n) if v!=i]
            assert jq==[jj[v] for v in rem]
            assert tq==[[tt[v][w] for w in rem] for v in rem]
            pq2,lq2,rq2=row_potential(jq,tq)
            assert pq==pq2 and lq==lq2 and rq==rq2
            gs.append((i,4*(pp-pq)+2*(ll-lq)))
        if not gs: gs=[(-1,IV.point(0))]
        mx=IV(max(v.lo for _,v in gs),max(v.hi for _,v in gs));gains.append(mx)
        shift_rows.append({'shift':z,'j':[str(a) for a in jj],
                           't':[[str(a) for a in row] for row in tt],
                           'max_admissible_gain':show(mx)})
    D=2*H-sum(Hg,IV.point(0))/N
    dP=2*P-sum(Pg,IV.point(0))/N
    dL=2*L-sum(Lg,IV.point(0))/N
    delta=D-4*dP-2*dL
    M=IV(max(v.lo for v in gains),max(v.hi for v in gains))
    four_residual=4*delta-M
    assert delta.lo>F(5415,10000)
    assert M.hi<F(18778,10000)
    assert four_residual.lo>F(2884,10000)
    assert dP.lo>0 and (2*dP-dL).lo>0
    lower_bound=4+(D-2*dL)/dP
    assert lower_bound.lo>F(447,50) # 8.94
    # Independent exact cubic degree / square identities.
    assert max(s.bit_count() for s in masks)==3
    w=fwht(f)
    for u in range(N): assert sum(w[s]*w[s^u] for s in range(N))==(N*N if u==0 else 0)
    out={
      'status':'ALL_EXACT_CHECKS_PASS',
      'method':'Fractions only for accepted comparisons; 64-term atanh log intervals',
      'float_values_are_display_only':True,'independent_audit':False,'full_FEI_proof':False,
      'base':{'variables':n,'ANF_masks':masks,'negative_inputs':[i for i,v in enumerate(f) if v<0],
              'Walsh_integer_numerators':w,'Walsh_denominator':N,'J':str(sum(j)),
              'j':[str(a) for a in j], 't':[[str(a) for a in row] for row in t],
              'H_bits':show(H),'P':show(P),'L_bits':show(L),'R':str(R)},
      'derivative':{'D_cross_bits':show(D),'delta_P':show(dP),'delta_L_bits':show(dL),
                    'quotient_free_residual':show(delta), 'max_single_block_quotient_gain':show(M)},
      'tensor_counterexample':{'copies':4,'variables':20,'lower_bound_on_residual_for_every_pivot_rule':show(four_residual),
                  'scope':'Analytic tensor amplification using an exact base certificate; no 2^20-shift enumeration claimed'},
      'two_potential_family':{'necessary_b_lower_bound':2,'necessary_advertised_a_plus_2b_lower_bound':show(lower_bound),
                  'scope':'Combined with the written rare-point asymptotic; NOT a lower bound on the optimal FEI constant'},
      'shifts':shift_rows}
    path=pathlib.Path(__file__).with_name('exact_drift_certificate.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='shifts'},indent=2))
    print('ALL_EXACT_CHECKS_PASS')
if __name__=='__main__':main()
