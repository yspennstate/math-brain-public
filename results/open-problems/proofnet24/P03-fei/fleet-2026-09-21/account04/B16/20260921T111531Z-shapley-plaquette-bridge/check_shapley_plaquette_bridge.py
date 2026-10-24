#!/usr/bin/env python3
"""Exact/self-checks for account04/B16 Shapley--plaquette / q-flip bridge.
Finite checks only; universal claims in the report are proved algebraically.
No external packages.
"""
from fractions import Fraction
from itertools import combinations
import json, math

def pc(x): return x.bit_count()

def fwht_float(vals):
    a=[float(x) for x in vals]; N=len(a); h=1
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/N for x in a]

def fwht_frac(vals):
    a=list(vals); N=len(a); h=1
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/N for x in a]

def H_bits(vals):
    out=0.0
    for a in fwht_float(vals):
        p=a*a
        if p: out-=p*math.log2(p)
    return out

def pivot(v): return (v & -v).bit_length()-1
def parent(v): return v ^ (1<<pivot(v))
def basis(n): return [v for v in range(1,1<<n) if pc(v)>=2]

def B_vertices(v):
    i=pivot(v); return (0,1<<i,v,v^(1<<i))

def B_bitmask(v):
    out=0
    for x in B_vertices(v): out ^= 1<<x
    return out

def is_descendant(u,x):
    if pc(x)<2: return False
    y=x
    while pc(y)>=2:
        if y==u: return True
        y=parent(y)
    return False

def dual_phase(n,u): return [-1 if is_descendant(u,x) else 1 for x in range(1<<n)]

def syndrome(vals,v):
    z=1
    for x in B_vertices(v): z*=vals[x]
    return z

def phase_subset(n,bs,mask):
    out=[1]*(1<<n)
    for j,u in enumerate(bs):
        if (mask>>j)&1:
            g=dual_phase(n,u); out=[a*b for a,b in zip(out,g)]
    return out

def entropy_values(n,bs,M):
    G={}; S=M
    while True:
        G[S]=H_bits(phase_subset(n,bs,S))
        if S==0: break
        S=(S-1)&M
    return G

def shapley_float(G,M,vbit):
    m=pc(M); others=M&~vbit; ans=0.0; S=others
    while True:
        k=pc(S); w=math.factorial(k)*math.factorial(m-k-1)/math.factorial(m)
        ans += w*(G[S|vbit]-G[S])
        if S==0: break
        S=(S-1)&others
    return ans

def kappa(G,S,vbit,hbit):
    return G[S|vbit]+G[S|hbit]-G[S]-G[S|vbit|hbit]

def curvature_bank(G,M,vbit):
    m=pc(M); total=0.0; hs=M&~vbit
    while hs:
        hbit=hs & -hs; others=M&~vbit&~hbit; S=others
        while True:
            k=pc(S)
            w=math.factorial(k)*math.factorial(m-k-1)/math.factorial(m)
            total += w*kappa(G,S,vbit,hbit)
            if S==0: break
            S=(S-1)&others
        hs-=hbit
    return total

def relation_vertex_mask(bs,rmask):
    out=0
    for j,v in enumerate(bs):
        if (rmask>>j)&1: out ^= B_bitmask(v)
    return out

def synthetic_c(bs,rmask):
    A=relation_vertex_mask(bs,rmask); w=pc(A)
    if not w: return Fraction(0)
    return Fraction((-1)**(w//2),w+1)

def P_game(bs,M):
    return sum((synthetic_c(bs,r) for r in range(1,1<<len(bs)) if pc(r&M)%2),Fraction(0))

def shapley_P(bs,M,j):
    vb=1<<j; m=pc(M); others=M&~vb; ans=Fraction(0); S=others
    while True:
        k=pc(S); w=Fraction(math.factorial(k)*math.factorial(m-k-1),math.factorial(m))
        ans += w*(P_game(bs,S|vb)-P_game(bs,S))
        if S==0: break
        S=(S-1)&others
    return ans

def L_direct(bs,M,j):
    vb=1<<j
    if not (M&vb): return Fraction(0)
    ans=Fraction(0)
    for r in range(1,1<<len(bs)):
        q=pc(r&M)
        if q%2 and (r&vb): ans += synthetic_c(bs,r)/q
    return ans

def eta(n,f,i): return [Fraction(1-f[x]*f[x^(1<<i)],2) for x in range(1<<n)]

dual_checks=0; entropy_formula_checks=0; max_entropy_err=0.0; max_dual_entropy=(0,0.0)
for n in range(2,6):
    bs=basis(n)
    for u in bs:
        g=dual_phase(n,u)
        for v in bs:
            assert syndrome(g,v)==(-1 if u==v else 1); dual_checks+=1
        c=n-pivot(u); q=2.0**(-c); p0=(1-2*q)**2; p1=4*q*q
        Hform=-(p0*math.log2(p0) if p0 else 0.0)-(2**c-1)*p1*math.log2(p1)
        Hg=H_bits(g); max_entropy_err=max(max_entropy_err,abs(Hg-Hform)); assert abs(Hg-Hform)<1e-12
        entropy_formula_checks+=1
        if Hg>max_dual_entropy[1]: max_dual_entropy=(c,Hg)

shapley_curvature_checks=0; max_shapley_error=0.0
for n in (3,4):
    bs=basis(n); L=len(bs); masks=[]
    for k in range(1,min(5,L)+1):
        for comb in list(combinations(range(L),k))[:min(10,math.comb(L,k))]:
            masks.append(sum(1<<j for j in comb))
    for M in masks:
        G=entropy_values(n,bs,M)
        for j in range(L):
            vb=1<<j
            if not (M&vb): continue
            phi=shapley_float(G,M,vb); C=curvature_bank(G,M,vb); err=abs(phi-(G[vb]-C))
            max_shapley_error=max(max_shapley_error,err); assert err<1e-11; shapley_curvature_checks+=1
        lhs=sum(curvature_bank(G,M,1<<j) for j in range(L) if M&(1<<j))
        rhs=sum(G[1<<j] for j in range(L) if M&(1<<j))-G[M]
        assert abs(lhs-rhs)<1e-10

aumann_shapley_checks=0
for n in (2,3):
    bs=basis(n)
    for M in range(1,1<<len(bs)):
        for j in range(len(bs)):
            if M&(1<<j):
                assert shapley_P(bs,M,j)==L_direct(bs,M,j); aumann_shapley_checks+=1

cut_radon_checks=0; cut_average_checks=0
for n in (2,3):
    N=1<<n
    for truth in range(1<<N):
        f=[-1 if (truth>>x)&1 else 1 for x in range(N)]
        for i in range(n):
            e=eta(n,f,i); eh=fwht_frac(e); mu=sum(e,Fraction(0))/N
            assert all(eh[U]==0 for U in range(N) if U&(1<<i))
            ws=[w for w in range(1,N) if not (w&(1<<i))]; probs=[]
            for w in ws:
                bad=0
                for a in range(N):
                    z=f[a]*f[a^(1<<i)]*f[a^w]*f[a^w^(1<<i)]; bad += (z==-1)
                p=Fraction(bad,N)
                rhs=4*sum((x*x for U,x in enumerate(eh) if pc(U&w)%2),Fraction(0))
                assert p==rhs; probs.append(p); cut_radon_checks+=1
            av=sum(probs,Fraction(0))/len(probs)
            rhsav=Fraction(2**n,2**(n-1)-1)*mu*(1-mu)
            assert av==rhsav; cut_average_checks+=1

def Hc(c):
    q=2.0**(-c); p0=(1-2*q)**2; p1=4*q*q
    return -(p0*math.log2(p0) if p0 else 0.0)-(2**c-1)*p1*math.log2(p1)

hc_table={str(c):Hc(c) for c in range(2,21)}
baseline={str(n):sum((2**(c-1)-1)*Hc(c) for c in range(2,n+1))/(2*n) for n in (3,4,5,8,10,20)}

out={
  "status":"PASS",
  "scope":"finite self-checks for universal algebraic identities; not FEI closure",
  "dual_basis_syndrome_checks":dual_checks,
  "dual_entropy_formula_checks":entropy_formula_checks,
  "max_dual_entropy_formula_abs_error":max_entropy_err,
  "max_dual_entropy_seen_bits":{"c":max_dual_entropy[0],"H_bits":max_dual_entropy[1]},
  "shapley_curvature_checks":shapley_curvature_checks,
  "max_shapley_curvature_abs_error":max_shapley_error,
  "aumann_shapley_exact_checks":aumann_shapley_checks,
  "cut_radon_exact_checks":cut_radon_checks,
  "cut_average_exact_checks":cut_average_checks,
  "dual_entropy_Hc_bits_c2_to20":hc_table,
  "expected_raw_baseline_relation_load_per_edge_bits_selected_n":baseline,
  "notes":[
    "The q-flip dual basis is checked through n=5.",
    "The Shapley--plaquette bridge is checked on deterministic active sets through n=4.",
    "Aumann--Shapley relation allocation is exact-rational through n=3 with synthetic signed relation weights.",
    "The cut-spectrum Radon identity is exact-rational for every Boolean function through n=3.",
    "Finite checks are not used as proofs of the all-dimensional statements."
  ]
}
print(json.dumps(out,indent=2,sort_keys=True))
