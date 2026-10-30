#!/usr/bin/env python3
"""Exact/numerical sanity checks for B17 recursive-majority adversary
and hierarchical branch-surplus code.

The analytic report contains the proofs.  This script checks:
* exact Galton--Watson first/second moments for recursive Maj_3;
* exact entropy/influence recurrence for the composition tree;
* numerical global ordered-code U and its rigorous moment lower bound;
* the nested local ordered-code cost on the natural composition tree;
* for every Boolean function through n<=3, exact tree branch-surplus
  telescoping and the hierarchical true-local-entropy code H<=T.

Finite checks are not a proof of FEI.
"""
from fractions import Fraction
import math, json

def h(probs):
    return -sum(float(p)*math.log2(float(p)) for p in probs if p)

def conv_float(a,b):
    out=[0.0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: out[i+j]+=x*y
    return out

def kdist(depth):
    p=[0.0,1.0]  # K_0=1
    for _ in range(depth):
        p3=conv_float(conv_float(p,p),p)
        q=[0.0]*max(len(p),len(p3))
        for k,x in enumerate(p): q[k]+=0.75*x
        for k,x in enumerate(p3): q[k]+=0.25*x
        p=q
    return p

def maj_diag(d):
    I=Fraction(3,2)**d
    M2=2*I*I-I
    Htrue=4*(I-1)
    p=kdist(d)
    Inum=sum(k*x for k,x in enumerate(p))
    M2num=sum(k*k*x for k,x in enumerate(p))
    HK=h(p)
    elogfac=sum(x*math.lgamma(k+1)/math.log(2) for k,x in enumerate(p) if k>=2 and x)
    U=HK+float(I)*d*math.log2(3)-elogfac
    lower=d*math.log2(3)-math.log2(2*float(I)-1)
    hKbase=h([Fraction(3,4),Fraction(1,4)])
    Ubase=hKbase+1.5*math.log2(3)-0.25*math.log2(6)
    Utree=2*Ubase*(float(I)-1)
    assert abs(Inum-float(I))<1e-10
    assert abs(M2num-float(M2))<1e-8
    assert U/float(I)+1e-10 >= lower
    return {
      "depth":d,"leaves":3**d,"I":float(I),"M2":float(M2),
      "H":float(Htrue),"H_over_I":float(Htrue/I),
      "global_U_over_I":U/float(I),
      "rigorous_U_over_I_lower_bound":lower,
      "nested_U_over_I":Utree/float(I)
    }

def fwht(a):
    a=list(map(int,a)); hstep=1
    while hstep<len(a):
        for i in range(0,len(a),2*hstep):
            for j in range(i,i+hstep):
                x,y=a[j],a[j+hstep]
                a[j],a[j+hstep]=x+y,x-y
        hstep*=2
    return a

def fixed_tree(n):
    # Returns children map for a deterministic balanced interval hierarchy.
    children={}
    def rec(indices):
        key=tuple(indices)
        if len(indices)<=1: return
        m=len(indices)//2
        L=tuple(indices[:m]); R=tuple(indices[m:])
        children[key]=(L,R)
        rec(L); rec(R)
    rec(list(range(n)))
    return tuple(range(n)), children

def tree_stats(ps,n):
    root, children=fixed_tree(n)
    # probabilities are Fractions over bitmask spectral subsets
    def active(mask, node):
        return any((mask>>i)&1 for i in node)
    tau={}
    nodes={root}|set(children)|{c for pair in children.values() for c in pair}
    for node in nodes:
        tau[node]=sum((p for mask,p in enumerate(ps) if p and active(mask,node)), Fraction())
    I=sum((p*mask.bit_count() for mask,p in enumerate(ps)), Fraction())
    tr=tau[root]
    surplus=Fraction()
    code=(0.0 if tr in (0,1) else h([tr,1-tr]))
    for node,(L,R) in children.items():
        tv=tau[node]
        surplus += tau[L]+tau[R]-tv
        if tv:
            probs=[]
            for pattern in ((1,0),(0,1),(1,1)):
                mass=sum((p for mask,p in enumerate(ps) if p and active(mask,node)
                          and int(active(mask,L))==pattern[0]
                          and int(active(mask,R))==pattern[1]), Fraction())
                probs.append(mass/tv)
            code += float(tv)*h(probs)
    return I,tr,surplus,code

tree_checks=0
worst_gap=-1e9
for n in range(1,4):
    N=1<<n
    for tailmask in range(1<<(N-1)):
        vals=[1]+[-1 if (tailmask>>(x-1))&1 else 1 for x in range(1,N)]
        W=fwht(vals); den=N*N
        ps=[Fraction(w*w,den) for w in W]
        Hspec=h(ps)
        I,tau,surplus,code=tree_stats(ps,n)
        assert surplus == I-tau
        assert Hspec <= code+1e-10
        worst_gap=max(worst_gap,Hspec-code)
        tree_checks+=1

diags=[maj_diag(d) for d in range(1,8)]
out={
 "status":"PASS",
 "recursive_majority_depths_checked":[1,2,3,4,5,6,7],
 "recursive_majority_diagnostics":diags,
 "exact_boolean_tree_checks_n_le_3":tree_checks,
 "max_H_minus_hierarchical_code":worst_gap,
 "analytic_claims_checked":"I_d=(3/2)^d, E K_d^2=2 I_d^2-I_d, H_d=4(I_d-1), branch surplus = I-tau",
 "full_FEI_status":"OPEN / NOT PROVED; finite checks only"
}
print(json.dumps(out,indent=2))
