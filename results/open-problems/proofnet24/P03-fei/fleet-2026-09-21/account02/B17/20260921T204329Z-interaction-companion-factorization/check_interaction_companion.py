#!/usr/bin/env python3
"""Finite checks for B17 interaction-component / companion-Riesz mechanism.

Analytic proofs are in REPORT.md.  This checks only finite implementations:
  * exact plaquette/support-boundary identity p_ik=p_ki;
  * p_ik <= 2 min(Inf_i,1-Inf_i);
  * interaction-graph components contain every nonlinear ANF monomial;
  * maximum spanning-tree plaquette weight <= 2J;
  * character-fold invariance of p_ik for all n<=3;
  * exact addressing p-weights for m<=3, plus formula diagnostics.

No finite check is promoted to FEI.
"""
from fractions import Fraction
from math import comb, log2
import json

def values_from_mask(n, mask):
    N=1<<n
    return [-1 if (mask>>x)&1 else 1 for x in range(N)]

def inf_count(vals,i):
    N=len(vals)
    return sum(vals[x]!=vals[x^(1<<i)] for x in range(N))

def p_count(vals,i,k):
    N=len(vals)
    c=0
    for x in range(N):
        ai=(vals[x]!=vals[x^(1<<i)])
        y=x^(1<<k)
        bi=(vals[y]!=vals[y^(1<<i)])
        c += (ai!=bi)
    return c

def plaquette_count(vals,i,k):
    N=len(vals)
    c=0
    for x in range(N):
        prod=vals[x]*vals[x^(1<<i)]*vals[x^(1<<k)]*vals[x^(1<<i)^(1<<k)]
        c += (prod==-1)
    return c

def anf_coeffs(vals):
    a=[1 if v==-1 else 0 for v in vals]
    n=(len(vals)).bit_length()-1
    for i in range(n):
        for mask in range(1<<n):
            if mask&(1<<i):
                a[mask] ^= a[mask^(1<<i)]
    return a

def components_from_p(P):
    n=len(P)
    seen=set(); comps=[]
    for s in range(n):
        if s in seen: continue
        st=[s]; seen.add(s); C=[]
        while st:
            u=st.pop(); C.append(u)
            for v in range(n):
                if v not in seen and P[u][v]>0:
                    seen.add(v); st.append(v)
        comps.append(sorted(C))
    return comps

def max_tree_weight(P, C):
    if len(C)<=1: return 0
    used={C[0]}; total=0
    while len(used)<len(C):
        best=(-1,None)
        for u in used:
            for v in C:
                if v not in used and P[u][v]>best[0]:
                    best=(P[u][v],v)
        assert best[0]>0
        total += best[0]
        used.add(best[1])
    return total

def char_multiply(vals,A):
    return [v*(-1 if ((x&A).bit_count()&1) else 1) for x,v in enumerate(vals)]

total=0
pair_checks=0
tree_checks=0
anf_checks=0
char_checks=0
for n in range(1,5):
    N=1<<n
    for mask in range(1<<N):
        vals=values_from_mask(n,mask)
        q=[inf_count(vals,i) for i in range(n)]
        P=[[0]*n for _ in range(n)]
        for i in range(n):
            for k in range(i+1,n):
                pc=p_count(vals,i,k)
                assert pc==p_count(vals,k,i)==plaquette_count(vals,i,k)
                assert pc <= 2*min(q[i],N-q[i])
                assert pc <= 2*min(q[k],N-q[k])
                P[i][k]=P[k][i]=pc
                pair_checks += 1
        comps=components_from_p(P)
        cid={}
        for a,C in enumerate(comps):
            for i in C: cid[i]=a
            tw=max_tree_weight(P,C)
            assert tw <= 2*sum(min(q[i],N-q[i]) for i in C)
            tree_checks += 1
        anf=anf_coeffs(vals)
        for mon,c in enumerate(anf):
            if c and mon.bit_count()>=2:
                inds=[i for i in range(n) if mon>>i&1]
                assert len({cid[i] for i in inds})==1
                anf_checks += 1
        if n<=3:
            for A in range(1<<n):
                vv=char_multiply(vals,A)
                for i in range(n):
                    for k in range(i+1,n):
                        assert p_count(vals,i,k)==p_count(vv,i,k)
                        char_checks += 1
        total += 1

def address_vals(m):
    N=1<<m
    n=m+N
    vals=[]
    for x in range(1<<n):
        a=x & (N-1)
        bit=(x>>(m+a))&1
        vals.append(-1 if bit else 1)
    return vals

address_exact=[]
for m in range(1,4):
    vals=address_vals(m); N=1<<m; n=m+N
    P=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(i+1,n):
            P[i][k]=P[k][i]=p_count(vals,i,k)
    den=len(vals)
    for i in range(m):
        for k in range(i+1,m):
            assert Fraction(P[i][k],den)==Fraction(1,2)
    for i in range(m):
        for t in range(N):
            assert Fraction(P[i][m+t],den)==Fraction(2,N)
    for s in range(N):
        for t in range(s+1,N):
            assert P[m+s][m+t]==0
    C=list(range(n))
    W=Fraction(max_tree_weight(P,C),den)
    assert W==Fraction(m+3,2)
    address_exact.append({"m":m,"n":n,"W":str(W)})

def h2(p):
    if p<=0 or p>=1: return 0.0
    return -p*log2(p)-(1-p)*log2(1-p)

def address_rinc(m):
    z=0.0
    for r in range(m+1):
        pr=comb(m,r)/(2**m)
        hm=h2(1/(r+1)) + m/(r+1) + (r/(r+1))*log2(m)
        z += pr*(m + log2(comb(m,r)) - hm)
    return z

address_diag=[]
for m in [1,2,3,5,10,20,50,100]:
    R=address_rinc(m)
    W=(m+3)/2
    address_diag.append({"m":m,"R_inc":R,"W":W,"ratio":R/W})

out={
  "status":"PASS",
  "scope":{
    "all_boolean_functions_n_le_4":total,
    "pair_identity_checks":pair_checks,
    "component_tree_checks":tree_checks,
    "nonlinear_anf_monomial_checks":anf_checks,
    "character_invariance_pair_checks_n_le_3":char_checks,
    "address_exact_small":address_exact
  },
  "addressing_diagnostics":address_diag,
  "warning":"Finite checks validate implementations only; full FEI and the proposed interaction-skeleton entropy bridge remain open."
}
print(json.dumps(out,indent=2,sort_keys=True))
