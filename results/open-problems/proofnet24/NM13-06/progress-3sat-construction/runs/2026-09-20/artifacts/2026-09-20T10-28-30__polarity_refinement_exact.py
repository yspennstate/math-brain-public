#!/usr/bin/env python3
"""
Exact rational verifier for T04 polarity-refinement theorem.

We use the closed four-spectrum cascade drift established in the preceding run.
For a unit-free state x[a,b,c,d], define Phi=m2+2 m3-log(1-rho),
rho=2*sum(ab x)/sum((a+b)x), and let ell_s,o = D Phi[F_{s,o}]
for one free choice from class s followed by its complete expected subcritical
unit cascade.

The script verifies:
  (1) the exact polarity-gap factorization
      ell_T-ell_F=(a-b) A + (c-d) B
      where A=L(D2)-L(G)/(1-rho), B=2 L(D3-M32);
  (2) the exact Jensen/refinement gap in a coarse total-degree cell;
  (3) a sign-symmetric rational witness with rho=8/17 in the balanced
      coarse cell (3,3), where every coarse uniform-polarity choice makes
      Phi increase, but the four-spectrum polarity split makes Phi decrease.
"""
from fractions import Fraction as Q
from collections import defaultdict

def add_scaled(dst, src, scale=Q(1)):
    for k,v in src.items():
        dst[k] += scale*v
        if dst[k] == 0:
            del dst[k]

def mass(y):
    return sum(y.values(), Q(0))

def moments(x):
    T2 = sum(Q(a+b)*v for (a,b,c,d),v in x.items())
    T3 = sum(Q(c+d)*v for (a,b,c,d),v in x.items())
    S  = sum(Q(a*b)*v for (a,b,c,d),v in x.items())
    return T2,T3,S

def D2(x):
    T2,_,_ = moments(x)
    out = defaultdict(Q)
    for (a,b,c,d),v in x.items():
        if a:
            w = Q(a)*v/T2
            out[(a,b,c,d)] -= w
            out[(a-1,b,c,d)] += w
        if b:
            w = Q(b)*v/T2
            out[(a,b,c,d)] -= w
            out[(a,b-1,c,d)] += w
    return dict(out)

def D3(x):
    _,T3,_ = moments(x)
    out = defaultdict(Q)
    for (a,b,c,d),v in x.items():
        if c:
            w = Q(c)*v/T3
            out[(a,b,c,d)] -= w
            out[(a,b,c-1,d)] += w
        if d:
            w = Q(d)*v/T3
            out[(a,b,c,d)] -= w
            out[(a,b,c,d-1)] += w
    return dict(out)

def M32(x):
    _,T3,_ = moments(x)
    out = defaultdict(Q)
    for (a,b,c,d),v in x.items():
        if c:
            w = Q(c)*v/T3
            out[(a,b,c,d)] -= w
            out[(a+1,b,c-1,d)] += w
        if d:
            w = Q(d)*v/T3
            out[(a,b,c,d)] -= w
            out[(a,b+1,c,d-1)] += w
    return dict(out)

def forced_G(x):
    T2,_,_ = moments(x)
    out = defaultdict(Q)
    for k,v in x.items():
        a,b,c,d = k
        out[k] -= Q(a+b)*v/T2
    K2 = sum(Q(a*(a-1)+b*(b-1))*v for (a,b,c,d),v in x.items())/T2
    K3 = 2*sum(Q(a*c+b*d)*v for (a,b,c,d),v in x.items())/T2
    K32 = 2*sum(Q(a*d+b*c)*v for (a,b,c,d),v in x.items())/T2
    add_scaled(out,D2(x),K2)
    add_scaled(out,D3(x),K3)
    add_scaled(out,M32(x),K32)
    return dict(out)

def free_F(x,s,o):
    a,b,c,d = s
    out = defaultdict(Q)
    out[s] -= 1
    if o == "T":
        add_scaled(out,D2(x),Q(a))
        add_scaled(out,D3(x),Q(2*c))
        add_scaled(out,M32(x),Q(2*d))
        u = Q(b)
    else:
        add_scaled(out,D2(x),Q(b))
        add_scaled(out,D3(x),Q(2*d))
        add_scaled(out,M32(x),Q(2*c))
        u = Q(a)
    return dict(out),u

def full_drift(x,s,o):
    T2,_,S = moments(x)
    rho = 2*S/T2
    assert rho < 1
    F,u = free_F(x,s,o)
    G = forced_G(x)
    out = defaultdict(Q,F)
    add_scaled(out,G,u/(1-rho))
    return dict(out),rho

def delta_rho(x,dx):
    T2,_,S = moments(x)
    dT2,_,dS = moments(dx)
    return 2*(dS*T2-S*dT2)/(T2*T2)

def Lphi(x,dx,eta=Q(2),beta=Q(1)):
    T2,_,S = moments(x)
    rho = 2*S/T2
    dT2,dT3,_ = moments(dx)
    dr = delta_rho(x,dx)
    return dT2/2 + eta*dT3/3 + beta*dr/(1-rho)

def ell(x,s,o):
    dx,_ = full_drift(x,s,o)
    return Lphi(x,dx)

def fmt(q):
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)

# A sign-symmetric exact state obtained by symmetrizing a rational search witness.
x = {
    (0,0,2,2): Q(7,52),
    (0,1,1,3): Q(5,104),
    (0,1,2,3): Q(5,52),
    (0,2,2,0): Q(7,104),
    (0,2,3,1): Q(1,8),
    (1,0,3,1): Q(5,104),
    (1,0,3,2): Q(5,52),
    (1,2,2,3): Q(1,104),
    (1,2,3,3): Q(9,104),
    (2,0,0,2): Q(7,104),
    (2,0,1,3): Q(1,8),
    (2,1,3,2): Q(1,104),
    (2,1,3,3): Q(9,104),
}
assert mass(x) == 1
for (a,b,c,d),v in x.items():
    assert x.get((b,a,d,c),Q(0)) == v

T2,T3,S = moments(x)
rho = 2*S/T2
assert (T2,T3,S,rho) == (Q(85,52),Q(223,52),Q(5,13),Q(8,17))

G = forced_G(x)
LD2 = Lphi(x,D2(x))
LD3 = Lphi(x,D3(x))
LM32 = Lphi(x,M32(x))
LG = Lphi(x,G)
A = LD2 - LG/(1-rho)
B = 2*(LD3-LM32)
Theta = A-B

print("T04 FOUR-SPECTRUM POLARITY-REFINEMENT EXACT VERIFIER")
print("state_mass =", fmt(mass(x)))
print("sign_symmetric = PASS")
print("T2 =",fmt(T2),"T3 =",fmt(T3),"S =",fmt(S),"rho =",fmt(rho))
print("L(D2) =",fmt(LD2),"L(D3) =",fmt(LD3),"L(M32) =",fmt(LM32),"L(G) =",fmt(LG))
print("A =",fmt(A),"B =",fmt(B),"Theta=A-B =",fmt(Theta),"float=%.12f"%float(Theta))

# Verify gap factorization for every selectable class in the state.
for s in sorted(x):
    a,b,c,d = s
    lhs = ell(x,s,"T")-ell(x,s,"F")
    rhs = Q(a-b)*A + Q(c-d)*B
    assert lhs == rhs
print("polarity_gap_factorization_all_support_classes = PASS")

# Balanced-cell simplification and decisive pair.
U = (2,0,1,3)
V = (0,2,3,1)
assert (U[0]+U[2],U[1]+U[3]) == (3,3)
assert (V[0]+V[2],V[1]+V[3]) == (3,3)
assert V == (U[1],U[0],U[3],U[2])

uT,uF = ell(x,U,"T"),ell(x,U,"F")
vT,vF = ell(x,V,"T"),ell(x,V,"F")
assert uT == vF and uF == vT
assert uF < uT and vT < vF

print("balanced_cell = (3,3)")
print("U =",U,"weight =",fmt(x[U]),"ell_T =",fmt(uT),"ell_F =",fmt(uF))
print("V =",V,"weight =",fmt(x[V]),"ell_T =",fmt(vT),"ell_F =",fmt(vF))
print("U_gap =",fmt(uT-uF),"expected =",fmt(Q(U[0]-U[1])*Theta))
assert uT-uF == Q(U[0]-U[1])*Theta

# Coarse total-degree policy must use one polarity on the whole cell.
cell = [s for s in x if (s[0]+s[2],s[1]+s[3]) == (3,3)]
W = sum(x[s] for s in cell)
coarse_T = sum(x[s]*ell(x,s,"T") for s in cell)/W
coarse_F = sum(x[s]*ell(x,s,"F") for s in cell)/W
fine = sum(x[s]*min(ell(x,s,"T"),ell(x,s,"F")) for s in cell)/W
coarse_best = min(coarse_T,coarse_F)

# Jensen identity:
# min(E X,E Y)-E min(X,Y) = (E|X-Y|-|E(X-Y)|)/2.
Eabs = sum(x[s]*abs(ell(x,s,"T")-ell(x,s,"F")) for s in cell)/W
Egap = sum(x[s]*(ell(x,s,"T")-ell(x,s,"F")) for s in cell)/W
jensen_gap = (Eabs-abs(Egap))/2
assert coarse_best-fine == jensen_gap

print("coarse_T_dPhi_per_free_choice =",fmt(coarse_T),"float=%.12f"%float(coarse_T))
print("coarse_F_dPhi_per_free_choice =",fmt(coarse_F),"float=%.12f"%float(coarse_F))
print("coarse_best =",fmt(coarse_best),"float=%.12f"%float(coarse_best))
print("four_spectrum_refined =",fmt(fine),"float=%.12f"%float(fine))
print("refinement_gain =",fmt(coarse_best-fine),"float=%.12f"%float(coarse_best-fine))
print("jensen_gap_identity =",fmt(jensen_gap),"PASS")
assert coarse_T > 0 and coarse_F > 0 and fine < 0
print("SIGN_FLIP_CERTIFICATE: coarse_uniform_polarity_worsens_Phi_but_refined_polarity_improves_Phi = PASS")
print("ALL_EXACT_CHECKS_PASS")
