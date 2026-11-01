"""Exact finite self-checks for the FEI affine one-step continuation.

The universal theorem D_x(f) <= 6 Ifrak(f) is proved in the matching run report.
This file checks finite truth tables, the scalar entropy lemma on rational grids,
and the exact one-point discounted-Ifrak obstruction. Stronger potential tests are
explicitly finite evidence only. Standard library only; not Lean/independent review.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib, json, time

@lru_cache(None)
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d=3 if d==2 else d+2
    if n>1: out[n]=out.get(n,0)+1
    return tuple(out.items())

@lru_cache(None)
def ln_unit(q):
    z=(q-1)/(q+1); z2=z*z; power=z; val=F(0)
    for k in range(64): val+=2*power/(2*k+1); power*=z2
    err=2*power/(129*(1-z2)); return val,val+err
LN2=ln_unit(F(2))
@lru_cache(None)
def log2_prime(p):
    if p==2:return F(1),F(1)
    k=p.bit_length()-1; lo,hi=ln_unit(F(p,1<<k)); return k+lo/LN2[1],k+hi/LN2[0]
class LogExpr:
    def __init__(self,t=None):self.t={p:F(c) for p,c in (t or {}).items() if c}
    def __add__(self,o):
        if not isinstance(o,LogExpr):o=LogExpr({2:F(o)})
        d=self.t.copy()
        for p,c in o.t.items():d[p]=d.get(p,F(0))+c
        return LogExpr(d)
    __radd__=__add__
    def __neg__(self):return LogExpr({p:-c for p,c in self.t.items()})
    def __sub__(self,o):return self+(-o if isinstance(o,LogExpr) else -F(o))
    def __mul__(self,c):return LogExpr({p:F(c)*v for p,v in self.t.items()})
    __rmul__=__mul__
    def __truediv__(self,c):return self*(1/F(c))
    def interval(self):
        lo=hi=F(0)
        for p,c in self.t.items():
            a,b=log2_prime(p)
            if c>=0:lo+=c*a;hi+=c*b
            else:lo+=c*b;hi+=c*a
        return lo,hi
    def nonnegative(self):
        lo,hi=self.interval(); assert lo>=0,(lo,hi)

def log_rat(q):
    d={}
    for p,e in factors(q.numerator):d[p]=d.get(p,F(0))+e
    for p,e in factors(q.denominator):d[p]=d.get(p,F(0))-e
    return LogExpr(d)
def entropy_weights(ws,den):
    z=LogExpr()
    for w in ws:
        if w:
            p=F(w,den); z+=(-p)*log_rat(p)
    return z
def hrat(q):return entropy_weights((q.numerator,q.denominator-q.numerator),q.denominator)
def fwht(a):
    a=list(a);w=1
    while w<len(a):
        for i in range(0,len(a),2*w):
            for j in range(i,i+w):a[j],a[j+w]=a[j]+a[j+w],a[j]-a[j+w]
        w*=2
    return a
def canonical(f):return tuple(x*f[0] for x in f)
def derivative(f,z):return canonical(tuple(f[x]*f[x^z] for x in range(len(f))))
def rank(vs):
    p={}
    for v in vs:
        while v:
            b=v.bit_length()-1
            if b not in p:p[b]=v;break
            v^=p[b]
    return len(p)
@lru_cache(None)
def basic(f):
    N=len(f);w=fwht(f); masses=tuple(x*x for x in w);den=N*N
    return {'H':entropy_weights(masses,den),'masses':masses,'den':den}
@lru_cache(None)
def Dcross(f):
    return 2*basic(f)['H']-sum((basic(derivative(f,z))['H'] for z in range(len(f))),LogExpr())/len(f)
@lru_cache(None)
def affine(f):
    N=len(f);n=N.bit_length()-1;w=fwht(f); num=fwht([x*x for x in w]);corr=[x//N for x in num]
    alpha=tuple(F(N-x,2*N) for x in corr); weight=tuple(min(x,1-x) for x in alpha)
    chosen=[]
    for v in sorted(range(1,N),key=lambda v:(weight[v],v)):
        if rank(chosen+[v])>len(chosen):chosen.append(v)
        if len(chosen)==n:break
    return {'M':sum((weight[v] for v in chosen),F(0)),'max_mass':F(max(x*x for x in w),N*N)}
def pointwise(f):
    f=canonical(f);a=affine(f);N=len(f); ch=Counter(derivative(f,z) for z in range(N))
    EM=sum((c*affine(g)['M'] for g,c in ch.items()),F(0))/N
    return a['M'],1-a['max_mass'],Dcross(f),2*a['M']-EM

def finite():
    funcs=set();raw=0;maxratio=F(0)
    for n in range(4):
        N=1<<n
        for bits in range(1<<N):
            raw+=1;funcs.add(canonical(tuple(1 if bits&(1<<x) else -1 for x in range(N))))
    for f in funcs:
        M,v,D,delta=pointwise(f);(LogExpr({2:6*M})-D).nonnegative()
        (LogExpr({2:4*(v+delta)})-D).nonnegative();assert M<=v+delta
        if M:maxratio=max(maxratio,D.interval()[1]/M)
    return {'status':'PASS','raw_truth_tables':raw,'canonical':len(funcs),'max_D_over_M_upper':str(maxratio),
            'warning':'D<=4(v+delta_M) and M<=v+delta_M are finite evidence only.'}
def scalar():
    for den in (64,128,256,512):
        for num in range(den//2+1):
            q=F(num,den);u=2*q*(1-q);phi=2*hrat(q)-hrat(u);(LogExpr({2:3*q})-phi).nonnegative()
    assert LN2[0]>F(2,3)
    x=F(9,5);term=F(1);s=F(1)
    for k in range(1,7):term*=x/k;s+=term
    assert s>6
    return {'status':'PASS','denominators':[64,128,256,512],'exp_9_5_taylor6':str(s)}
def onepoint(n):
    P=F(1);total=F(0)
    for k in range(n-1):
        if k:P*=1-F(2**(k-1),2**n)
        total+=F(1,2**k)*P*F((n-k)*2**(k+1),2**n)
    M0=F(2*n,2**n);return total/M0
def main():
    t=time.monotonic();vals={n:str(onepoint(n)) for n in (4,8,16,32,64)}
    out={'full_FEI_proved':False,'independent_audit':False,'lean_used':False,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'finite':finite(),'scalar_phi':scalar(),'one_point_discounted_M_over_M':vals,
         'status':'ALL_REQUESTED_CHECKS_PASS','elapsed_seconds':round(time.monotonic()-t,3)}
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
