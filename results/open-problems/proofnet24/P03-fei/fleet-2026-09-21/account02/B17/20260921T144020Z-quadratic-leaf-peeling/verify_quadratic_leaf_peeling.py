#!/usr/bin/env python3
"""Exact small-scope checker for B17 quadratic-leaf peeling.

It verifies algebraic identities behind the theorem:
  G(t,x,z)=F(t,z)*(-1)^(t*x)
has
  H(G) = (H(F|t=0)+H(F|t=1))/2 + 2,
  alpha_x(G)=alpha_t(G)=1/2,
  alpha_j(G)=alpha_j(F) for residual j,
hence for folded influence J=sum min(alpha_i,1-alpha_i),
  J(G)=J(F)-j_t(F)+1.

The entropy identity is checked without floating logs: squared Walsh masses of G
are compared exactly against two copies of each child squared Walsh mass divided
by 4.  Exhaustive F have t plus <=2 residual bits.

It also checks the exact sharp C=4 witness and the k-arm tree family.
Finite checks do not prove FEI.
"""
from fractions import Fraction
from collections import Counter
import json

def fwht(a):
    a=list(map(int,a)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]
                a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def mass_multiset(vals):
    N=len(vals); den=N*N
    return Counter(Fraction(w*w,den) for w in fwht(vals) if w)

def influences(vals):
    N=len(vals); n=N.bit_length()-1
    out=[]
    for i in range(n):
        bit=1<<i; bad=0
        for x in range(N):
            if not (x & bit) and vals[x]!=vals[x|bit]:
                bad += 1
        out.append(Fraction(bad, N//2))
    return out

def folded_J(vals):
    return sum((min(p,1-p) for p in influences(vals)), Fraction(0))

def restrict_t(vals,t):
    return [vals[t+2*z] for z in range(len(vals)//2)]

def attach_leaf(F):
    # F index t + 2*z; output coordinates t,z...,x where x is newest bit.
    NF=len(F); nz=(NF.bit_length()-1)-1
    out=[]
    for s in range(1<<(nz+2)):
        t=s&1
        z=(s>>1)&((1<<nz)-1)
        x=(s>>(nz+1))&1
        q=-1 if (t and x) else 1
        out.append(F[t+2*z]*q)
    return out

def predicted_leaf_masses(F):
    # Each child squared Walsh mass p produces exactly two G masses p/4.
    out=Counter()
    for t in (0,1):
        child=restrict_t(F,t)
        N=len(child); den=N*N
        for w in fwht(child):
            if w:
                out[Fraction(w*w,4*den)] += 2
    return out

def phase_from_mask(mask,n):
    return [-1 if (mask>>x)&1 else 1 for x in range(1<<n)]

def anf_coeff(vals):
    c=[0 if v==1 else 1 for v in vals]
    n=len(vals).bit_length()-1
    for i in range(n):
        for m in range(1<<n):
            if m&(1<<i):
                c[m]^=c[m^(1<<i)]
    return c

def arm_phase(t,x,y):
    # P=t+x+t*y+x*y mod 2.
    return -1 if (t ^ x ^ (t&y) ^ (x&y)) else 1

def k_arm(k):
    # t plus pairs (x_l,y_l)
    n=1+2*k
    vals=[]
    for s in range(1<<n):
        t=s&1; v=1
        for ell in range(k):
            x=(s>>(1+2*ell))&1
            y=(s>>(2+2*ell))&1
            v *= arm_phase(t,x,y)
        vals.append(v)
    return vals

exhaustive=0
for nz in (0,1,2):
    nF=1+nz
    for mask in range(1<<(1<<nF)):
        F=phase_from_mask(mask,nF)
        G=attach_leaf(F)
        assert mass_multiset(G)==predicted_leaf_masses(F)
        infF=influences(F); infG=influences(G)
        jt=min(infF[0],1-infF[0])
        assert infG[0]==Fraction(1,2)
        assert infG[-1]==Fraction(1,2)
        assert infG[1:-1]==infF[1:]
        assert folded_J(G)==folded_J(F)-jt+1
        exhaustive += 1

# Sharp threshold witness F(t,x,y)=(-1)^(t+x+t*y+x*y), truth mask 6.
Fsharp=phase_from_mask(6,3)
assert anf_coeff(Fsharp)[1] == 1  # t
Gsharp=attach_leaf(Fsharp)
assert influences(Fsharp)==[Fraction(1,2)]*3
assert folded_J(Fsharp)==Fraction(3,2)
assert folded_J(Gsharp)==Fraction(2,1)
# Fsharp and both t-restrictions have flat four-point spectra: H=2, Delta_t=0.
assert mass_multiset(Fsharp)==Counter({Fraction(1,4):4})
for t in (0,1):
    assert mass_multiset(restrict_t(Fsharp,t))==Counter({Fraction(1,4):4})
# Gsharp has 16 equal atoms: H=4.
assert mass_multiset(Gsharp)==Counter({Fraction(1,16):16})

arms=[]
for k in range(1,6):
    F=k_arm(k)
    masses=mass_multiset(F)
    assert masses==Counter({Fraction(1,1<<(2*k)):1<<(2*k)})
    inf=influences(F)
    assert inf==[Fraction(1,2)]*(2*k+1)
    # Interaction polynomial should be quadratic; rank formula is proved in report.
    assert all(m.bit_count()<=2 for m,c in enumerate(anf_coeff(F)) if c)
    arms.append({
        "k":k,
        "variables":2*k+1,
        "spectral_atoms":1<<(2*k),
        "H_exact":2*k,
        "I_exact":f"{2*k+1}/2",
        "ratio_exact":f"{4*k}/{2*k+1}",
    })

# Cubic-leaf obstruction to extending the monotonicity theorem.
# Base B(t,u) is -1 only at (0,0), i.e. truth mask 1.
B=phase_from_mask(1,2)
Gc=[]
for s in range(8):
    t=s&1; u=(s>>1)&1; x=(s>>2)&1
    q=-1 if (x and t and u) else 1
    Gc.append(B[t+2*u]*q)
assert mass_multiset(B)==Counter({Fraction(1,4):4})
assert influences(B)==[Fraction(1,2),Fraction(1,2)]
assert mass_multiset(Gc)==Counter({Fraction(1,16):7,Fraction(9,16):1})
assert influences(Gc)==[Fraction(3,4),Fraction(3,4),Fraction(1,4)]
assert folded_J(B)==Fraction(1,1)
assert folded_J(Gc)==Fraction(3,4)

out={
    "status":"PASS",
    "scope":"exhaustive leaf identity for F with t plus <=2 residual bits; k-arm family k<=5",
    "exhaustive_base_functions":exhaustive,
    "sharp_C4_witness":{
        "truth_mask":6,
        "J_F":"3/2",
        "H_F":2,
        "Delta_t_H":0,
        "J_attached":2,
        "H_attached":4,
        "slack_increment_formula":"C/2 - 2"
    },
    "arm_family":arms,
    "cubic_leaf_obstruction":{"base_truth_mask":1,"base_H_exact":"2","base_J_exact":"1","attached_spectral_law":"one atom 9/16 and seven atoms 1/16","attached_J_exact":"3/4","attached_H_exact":"4-(9/8)log2(3)","slack_increment_exact":"(9/8)log2(3)-2-C/4 < 0 for every C>=0"},
    "full_FEI_status":"OPEN / NOT PROVED; finite checks only"
}
print(json.dumps(out,indent=2))
