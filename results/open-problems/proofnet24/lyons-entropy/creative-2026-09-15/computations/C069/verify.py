"""Exact checks for C069. Analytic proofs are in agents/C069.md.

All reported signs use Fraction arithmetic and rational logarithm enclosures.
Sympy is used only for exact Gaussian-rational determinants.
"""
from fractions import Fraction as F
from itertools import combinations, product
from decimal import Decimal, localcontext
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent

def log_unit_interval(x, terms=45):
    assert 1 <= x <= 2
    z = (x-1)/(x+1)
    lo = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lo, lo+tail

def scale_interval(iv, c):
    return (iv[0]*c,iv[1]*c) if c >= 0 else (iv[1]*c,iv[0]*c)

def log_interval(x):
    x=F(x); assert x>0
    k=0
    while x<1: x*=2; k-=1
    while x>2: x/=2; k+=1
    a=log_unit_interval(x); b=scale_interval(log_unit_interval(F(2)),F(k))
    return a[0]+b[0],a[1]+b[1]

def linlog(items):
    out=(F(0),F(0))
    for c,x in items:
        if not c: continue
        iv=scale_interval(log_interval(x),c)
        out=out[0]+iv[0],out[1]+iv[1]
    return out

def entropy(law):
    return linlog([(-p,p) for p in law if p])

def add_iv(a,b):return a[0]+b[0],a[1]+b[1]
def sub_iv(a,b):return a[0]-b[1],a[1]-b[0]
def dec(x):
    with localcontext() as ctx:
        ctx.prec=45
        return str(Decimal(x.numerator)/Decimal(x.denominator))
def record(iv):
    return {'lower_decimal':dec(iv[0]),'upper_decimal':dec(iv[1]),
            'positive_certified':iv[0]>0,'width_less_than_1e_minus_38':iv[1]-iv[0]<F(1,10**38)}

def sf(x):return sp.Rational(x.numerator,x.denominator)
def ff(x):
    assert sp.im(x)==0
    return F(int(sp.numer(x)),int(sp.denom(x)))

results={}
examples=[('three_site',[6,-2,-3],[-2,3,-6],7),
          ('four_site',[14,-2,-3,-4],[-2,11,-6,-8],15)]
for name,xx,yy,d in examples:
    x=[F(z,d) for z in xx];y=[F(z,d) for z in yy];n=len(x)
    assert sum(z*z for z in x)==sum(z*z for z in y)==1
    assert sum(a*b for a,b in zip(x,y))==0
    m=[(a*a+b*b)/2 for a,b in zip(x,y)]
    pairs=list(combinations(range(n),2))
    r={(i,j):(x[i]*y[j]-x[j]*y[i])**2 for i,j in pairs}
    assert sum(m)==sum(r.values())==1
    for i in range(n):
        assert sum(v for ij,v in r.items() if i in ij)==2*m[i]
    for (i,j),p in r.items():assert p<=4*m[i]*m[j]
    hm=entropy(m);hr=entropy(r.values())
    beta=sub_iv(scale_interval(hm,F(2)),hr)
    theta=(beta[0]/(2*log_interval(F(2))[1]),beta[1]/(2*log_interval(F(2))[0]))
    assert beta[0]>log_interval(F(2))[1]
    assert beta[1]<2*log_interval(F(2))[0]
    law_checks=[]
    for p,q in [(F(1,5),F(1,3)),(F(3,4),F(4,5)),(F(19,40),F(17,30))]:
        f=[(1-p)*(1-q),p*(1-q)+q*(1-p),p*q]
        law={st:F(0) for st in product([0,1],repeat=n)}
        law[(0,)*n]=f[0]
        for i in range(n):
            st=tuple(int(j==i) for j in range(n));law[st]=f[1]*m[i]
        for ij,rr in r.items():
            st=tuple(int(j in ij) for j in range(n));law[st]=f[2]*rr
        K=sp.Matrix(n,n,lambda i,j:sf((p+q)*(x[i]*x[j]+y[i]*y[j])/2)
                      +sp.I*sf((p-q)*(y[i]*x[j]-x[i]*y[j])/2))
        for st,prob in law.items():
            M=sp.Matrix(n,n,lambda i,j:K[i,j] if st[j] else int(i==j)-K[i,j])
            assert ff(sp.simplify(M.det()))==prob
        hv=entropy(law.values())
        formula=add_iv(entropy(f),add_iv(scale_interval(hm,f[1]),scale_interval(hr,f[2])))
        assert max(hv[0],formula[0])<=min(hv[1],formula[1])
        law_checks.append(hv)
    gap=sub_iv(law_checks[2],scale_interval(add_iv(law_checks[0],law_checks[1]),F(1,2)))
    assert gap[0]>0
    results[name]={'m':[str(z) for z in m],
                   'r':{str(tuple(i+1 for i in ij)):str(v) for ij,v in r.items()},
                   'beta':record(beta),'theta':record(theta),
                   'sample_Jensen_gap':record(gap),
                   'exact_atom_determinant_checks':3*(2**n)}

# V4 shuffle: evaluate every rational atom, then verify polynomial derivatives.
G=[(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)]
states=list(product([0,1],repeat=4))
base=[F(3,4),F(3,4),F(1,4),F(1,4)];v=[1,-1,1,-1]

def prod(xs):
    ans=F(1)
    for x in xs:ans*=x
    return ans

def shuffle(tt):
    pars=[p+tt*vv for p,vv in zip(base,v)]
    raw={st:prod(p if bit else 1-p for bit,p in zip(st,pars)) for st in states}
    return {st:sum(raw[tuple(st[j] for j in g)] for g in G)/4 for st in states}

def second_atom(st):
    out=F(0)
    for g in G:
        zz=tuple(st[j] for j in g)
        factors=[base[i] if zz[i] else 1-base[i] for i in range(4)]
        signs=[v[i] if zz[i] else -v[i] for i in range(4)]
        out+=sum(F(2)*signs[i]*signs[j]*prod(factors[k] for k in range(4) if k not in (i,j))
                 for i,j in combinations(range(4),2))/4
    return out

law0=shuffle(F(0));lawp=shuffle(F(1,8));lawm=shuffle(F(-1,8))
assert lawp==lawm
assert sum(law0.values())==sum(lawp.values())==1
second={st:second_atom(st) for st in states}
assert sum(second.values())==0
assert sorted(law0.values())==sorted([F(9,256)]*6+[F(15,256)]*8+[F(41,256)]*2)
assert sorted(lawp.values())==sorted([F(105,4096)]*4+[F(247,4096)]*8+[F(617,4096)]*2+[F(233,4096)]*2)
curvature=linlog([(-second[st],law0[st]) for st in states])
formula=scale_interval(log_interval(F(41**5,9*15**4)),F(1,2))
assert max(curvature[0],formula[0])<=min(curvature[1],formula[1])
assert curvature[0]>0
gap=sub_iv(entropy(lawp.values()),entropy(law0.values()))
assert gap[0]>0
marginal=[sum(p for st,p in law0.items() if st[i]) for i in range(4)]
cov12=sum(p for st,p in law0.items() if st[0] and st[1])-marginal[0]*marginal[1]
assert marginal==[F(1,2)]*4 and cov12==F(1,16)
count0=[sum(p for st,p in law0.items() if sum(st)==k) for k in range(5)]
count_second=[sum(p for st,p in second.items() if sum(st)==k) for k in range(5)]
count_curvature=linlog([(-d,p) for d,p in zip(count_second,count0)])
assert count_curvature[1]<0
results['V4_obstruction']={'curvature':record(curvature),'finite_Jensen_violation':record(gap),
                           'count_entropy_curvature':record(count_curvature),
                           'covariance_12':str(cov12),
                           'p_minus':['5/8','7/8','1/8','3/8'],
                           'p_zero':['3/4','3/4','1/4','1/4'],
                           'p_plus':['7/8','5/8','3/8','1/8'],
                           'law0':{''.join(map(str,st)):str(p) for st,p in law0.items()},
                           'law_plus':{''.join(map(str,st)):str(p) for st,p in lawp.items()},
                           'atom_second_derivatives':{''.join(map(str,st)):str(p) for st,p in second.items()}}
(ROOT/'verification_results.json').write_text(json.dumps(results,indent=2)+'\n')
print('PASS: 72 exact physical atom checks, pair entropy coefficient certificates,')
print('      and exact V4 curvature, finite Jensen, and physical-exclusion checks.')
for name,r in results.items():
    print(name)
    for key in ('beta','theta','sample_Jensen_gap','curvature','finite_Jensen_violation','count_entropy_curvature'):
        if key in r: print(' ',key,r[key]['lower_decimal'],r[key]['upper_decimal'])
