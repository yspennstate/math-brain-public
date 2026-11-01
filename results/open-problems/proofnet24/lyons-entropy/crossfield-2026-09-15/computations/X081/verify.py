"""Exact checks for X081. Run from the campaign root with Python + SymPy.
The theorem is analytic; these checks certify a two-block example and identities.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import sympy as sp

OUT=Path(__file__).resolve().parent
COUNTS=defaultdict(int)

def subsets(E):
    E=tuple(E)
    for k in range(len(E)+1):
        for S in combinations(E,k): yield frozenset(S)

def H_form(p):
    d=defaultdict(F)
    for v in p:
        if not v: continue
        for prime,power in log_form(v): d[prime]-=v*power
    return {k:v for k,v in d.items() if v}

@lru_cache(None)
def log_form(v):
    d=defaultdict(int)
    for p,e in sp.factorint(v.numerator).items(): d[int(p)]+=e
    for p,e in sp.factorint(v.denominator).items(): d[int(p)]-=e
    return tuple((p,e) for p,e in d.items() if e)

def linear(*terms):
    d=defaultdict(F)
    for coefficient,form in terms:
        for p,v in form.items(): d[p]+=coefficient*v
    return {k:v for k,v in d.items() if v}

def form_float(form):
    import math
    return sum(float(c)*math.log(p) for p,c in form.items())

def gap(forms,I,p,q):
    return linear((1,forms[I|{p}]),(1,forms[I|{q}]),(-1,forms[I]),(-1,forms[I|{p,q}]))

def factor(n,vals):
    # vals are exact unnormalized Gaussian integers at their nonzero coordinates.
    v=sp.Matrix([vals.get(i,0) for i in range(n)])
    norm=sp.expand((v.conjugate().T*v)[0])
    Q=sp.eye(n)-2*v*v.conjugate().T/norm
    weights={i:F(int(sp.expand(sp.conjugate(x)*x)),int(norm)) for i,x in vals.items()}
    return Q,weights

def channel(I,s):
    x=sum((s.get(i,F(0)) for i in I),F(0))
    out={I:1-4*x*(1-x)}
    for i in I:
        for j in s.keys()-I:
            if s.get(i,F(0)):
                out[(I-{i})|{j}]=4*s[i]*s[j]
    out={k:v for k,v in out.items() if v}
    assert all(v>0 for v in out.values()) and sum(out.values())==1
    return out

def evolve(law,s):
    out=defaultdict(F)
    for I,v in law.items():
        for J,w in channel(I,s).items(): out[J]+=v*w
    return dict(out)

def minor_law(U,I):
    out={}
    for Y in combinations(range(U.rows),len(I)):
        d=sp.expand(U.extract(Y,sorted(I)).det(method='domain-ge'))
        value=sp.cancel(d*sp.conjugate(d))
        assert value.is_Rational
        p=F(int(value.p),int(value.q))
        if p: out[frozenset(Y)]=p
        COUNTS['exact_physical_minors']+=1
    assert sum(out.values())==1
    return out

def check_pair(Q1,s1,Q2,s2):
    V=Q2*Q1
    E=range(V.rows)
    Fs,Gs,ells={},{},{}
    firstFs,secondFs={},{}
    maxfiber=0
    for I in subsets(E):
        first=channel(I,s1)
        firstFs[I]=H_form(first.values())
        secondFs[I]=H_form(channel(I,s2).values())
        joint={}
        final=defaultdict(F)
        fiber=defaultdict(set)
        for R,x in first.items():
            for Y,y in channel(R,s2).items():
                joint[R,Y]=x*y
                final[Y]+=x*y
                fiber[Y].add(R)
        assert dict(final)==minor_law(V,I)
        local_max=max(map(len,fiber.values()))
        maxfiber=max(maxfiber,local_max)
        assert local_max<=2
        COUNTS['posterior_fibers_checked']+=len(fiber)
        Fs[I]=H_form(final.values())
        Gs[I]=H_form(joint.values())
        ells[I]=linear((1,Gs[I]),(-1,Fs[I]))
        expected=linear((1,firstFs[I]),*[(x,H_form(channel(R,s2).values())) for R,x in first.items()])
        assert Gs[I]==expected
        COUNTS['exact_joint_entropy_identities']+=1
    min_joint_gap=100.
    min_beta=100.
    for I in subsets(E):
        for p,q in combinations(set(E)-I,2):
            gG=gap(Gs,I,p,q)
            gF=gap(Fs,I,p,q)
            gell=gap(ells,I,p,q)
            assert gF==linear((1,gG),(-1,gell))
            assert form_float(gG)>-1e-11
            min_joint_gap=min(min_joint_gap,form_float(gG))
            min_beta=min(min_beta,form_float(gF))
            COUNTS['exact_square_entropy_balances']+=1
    return {'sites':V.rows,'maximum_complete_posterior_fiber':maxfiber,
            'minimum_joint_gap_diagnostic':min_joint_gap,'minimum_beta_diagnostic':min_beta}

def diamond_step(S,T,s):
    P=T-S
    C=set(s)-T
    R=S
    alpha=sum((s.get(i,F(0)) for i in R),F(0))
    beta=sum((s.get(i,F(0)) for i in P),F(0))
    chi=sum((s.get(i,F(0)) for i in C),F(0))
    c0=1-4*(alpha*beta+alpha*chi+beta*chi)
    tau=max(-c0,F(0))
    out=defaultdict(F)
    out[S,T]+=c0+tau
    def coeff(x,y): return 4-(tau/(x*y) if tau else 0)
    for a in R:
        for k in P:
            out[(R-{a})|{k},T]+=s.get(a,F(0))*s.get(k,F(0))*coeff(alpha,beta)
    for k in P:
        for c in C:
            out[R,(T-{k})|{c}]+=s.get(k,F(0))*s[c]*coeff(beta,chi)
    for a in R:
        for c in C:
            out[(R-{a})|{c},(T-{a})|{c}]+=s.get(a,F(0))*s[c]*coeff(alpha,chi)
    if tau:
        for a in R:
            for k in P:
                for c in C:
                    w=tau*s.get(a,F(0))*s.get(k,F(0))*s[c]/(alpha*beta*chi)
                    out[(R-{a})|{c},(T-{k})|{c}]+=w
                    out[(R-{a})|{k},(T-{a})|{c}]+=w
    out={d:v for d,v in out.items() if v}
    assert all(v>0 and S0<T0 and len(T0-S0)==2 for (S0,T0),v in out.items())
    assert sum(out.values())==1
    return out

@lru_cache(None)
def log_bounds(v):
    k=0
    while v<1: v*=2; k-=1
    while v>=2: v/=2; k+=1
    def base(x):
        z=(x-1)/(x+1)
        N=28
        lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
        return lo,lo+2*z**(2*N+1)/((2*N+1)*(1-z*z))
    lo,hi=base(v)
    l2,h2=base(F(2))
    return (lo+k*l2,hi+k*h2) if k>=0 else (lo+k*h2,hi+k*l2)

def H_bounds(law):
    lo=hi=F(0)
    for p in law.values():
        if p:
            a,b=log_bounds(p)
            lo-=p*b; hi-=p*a
    return lo,hi

# Exhaustive single-pair checks use local coordinates.
A1,sA1=factor(6,{0:1,1:1,2:1,3:1})
A2,sA2=factor(6,{2:1,3:sp.I,4:1,5:1})
B1,sB1=factor(5,{0:1,1:1,2:1})
B2,sB2=factor(5,{1:1,2:sp.I,3:1,4:1})
local_results=[check_pair(A1,sA1,A2,sA2),check_pair(B1,sB1,B2,sB2)]

n=10
Q1,s1=factor(n,{0:1,1:1,2:1,3:1})
Q2,s2=factor(n,{2:1,3:sp.I,4:1,5:1})
Q3,s3=factor(n,{5:1,6:1,7:1})
Q4,s4=factor(n,{6:1,7:sp.I,8:1,9:1})
Vleft=Q2*Q1
Vright=Q4*Q3
V=Vright*Vleft
assert sp.simplify(V.conjugate().T*V)==sp.eye(n)
I=frozenset({0,2,5,8}); p=1; q=6
inputs=[I,I|{p},I|{q},I|{p,q}]
laws=[]
for J in inputs:
    law={J:F(1)}
    for s in (s1,s2,s3,s4): law=evolve(law,s)
    assert law==minor_law(V,J)
    laws.append(law)
    # Exact root gluing entropy formula with A=0..5, B=5..9.
    Jleft=J&set(range(6)); K=J&set(range(6,10))
    left=evolve(evolve({Jleft:F(1)},s1),s2)
    sk=sum((abs(Vleft[5,j])**2 for j in Jleft),sp.Rational(0))
    sk=F(int(sk.p),int(sk.q))
    right0=evolve(evolve({frozenset(K):F(1)},s3),s4)
    right1=evolve(evolve({frozenset(K|{5}):F(1)},s3),s4)
    rhs=linear((1,H_form(left.values())),(1-sk,H_form(right0.values())),(sk,H_form(right1.values())))
    assert rhs==H_form(law.values())
    COUNTS['exact_tree_gluing_identities']+=1

# Independently compose the credited local diamonds and check final marginals.
dlaw={(I,I|{p,q}):F(1)}
for s in (s1,s2,s3,s4):
    new=defaultdict(F)
    for (S,T),v in dlaw.items():
        for d,w in diamond_step(S,T,s).items(): new[d]+=v*w
    dlaw=dict(new)
a,b,twom=defaultdict(F),defaultdict(F),defaultdict(F)
for (S,T),v in dlaw.items():
    a[S]+=v; b[T]+=v
    for z in T-S: twom[S|{z}]+=v
assert dict(a)==laws[0] and dict(b)==laws[3]
expectedmid=defaultdict(F)
for law in laws[1:3]:
    for S,v in law.items(): expectedmid[S]+=v
assert dict(twom)==dict(expectedmid)
m={S:v/2 for S,v in twom.items()}
ha=H_bounds(laws[0]); hb=H_bounds(laws[3]); hm=H_bounds(m)
beta_interval=(2*hm[0]-ha[1]-hb[1],2*hm[1]-ha[0]-hb[0])
l2,h2=log_bounds(F(2))
assert beta_interval[0]>2*h2-4 and beta_interval[1]<2*l2

result={'status':'PASS','checks':dict(COUNTS),'local_pairs':local_results,
        'example':{'sites':n,'bottom_columns':sorted(I),'active_columns':[p,q],
                   'top_codimension':n-len(I)-2,'quadrature_blocks':2,
                   'positive_final_diamond_atoms':len(dlaw),
                   'probability_support_sizes':[len(x) for x in laws],
                   'beta_star_rigorous_interval':[str(v) for v in beta_interval],
                   'beta_star_interval_display':[float(v) for v in beta_interval]},
        'analytic_uniform_definite_coefficient':'8 - 8 log 2'}
(OUT/'verified_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({**result,'example':{k:v for k,v in result['example'].items() if k!='beta_star_rigorous_interval'}},indent=2))
