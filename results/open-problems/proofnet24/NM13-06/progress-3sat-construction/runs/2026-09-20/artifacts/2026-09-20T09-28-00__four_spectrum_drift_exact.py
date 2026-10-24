#!/usr/bin/env python3
"""
Exact rational verifier for the T04 four-spectrum random-3-SAT drift.

State:
  x[a,b,c,d] = density of unset variables with
    a positive 2-clause occurrences,
    b negative 2-clause occurrences,
    c positive 3-clause occurrences,
    d negative 3-clause occurrences.

At unit-free macroscopic checkpoints:
  T2 = sum (a+b)x = 2 m2,
  T3 = sum (c+d)x = 3 m3,
  S  = sum ab x,
  rho = 2S/T2.

D2  = deletion of one uniformly random 2-occurrence from its variable.
D3  = deletion of one uniformly random 3-occurrence.
M32 = migration of one uniformly random 3-occurrence into a 2-occurrence,
      preserving literal sign.

For a free TRUE move from class s=(a,b,c,d):
  F_T = -e_s + a D2 + 2c D3 + 2d M32,  u_T=b.
For FALSE:
  F_F = -e_s + b D2 + 2d D3 + 2c M32,  u_F=a.

An average forced unit event has x-drift
  G = -((a+b)x/T2)
      + K2 D2 + K3 D3 + K32 M32
with
  K2  = sum[a(a-1)+b(b-1)]x/T2,
  K3  = 2 sum[ac+bd]x/T2,
  K32 = 2 sum[ad+bc]x/T2.

The two-type unit branching matrix has Perron root rho=2S/T2.
When rho<1 and initial unit signs have the ambient 2-occurrence mixture,
the expected full cascade drift is
  F_o + u_o/(1-rho) G.

This script checks the operator identities and gives an exact witness that
the 4-spectrum barrier controller distinguishes two classes with the same
total positive/negative degrees, including opposite optimal polarities.
"""
from fractions import Fraction
from collections import defaultdict

Q = Fraction

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

def signed_2_mass(x):
    A = sum(Q(a)*v for (a,b,c,d),v in x.items())
    B = sum(Q(b)*v for (a,b,c,d),v in x.items())
    return A,B

def D2(x):
    T2,_,_ = moments(x)
    out=defaultdict(Q)
    for (a,b,c,d),v in x.items():
        if a:
            w=Q(a)*v/T2
            out[(a,b,c,d)] -= w
            out[(a-1,b,c,d)] += w
        if b:
            w=Q(b)*v/T2
            out[(a,b,c,d)] -= w
            out[(a,b-1,c,d)] += w
    return dict(out)

def D3(x):
    _,T3,_ = moments(x)
    out=defaultdict(Q)
    for (a,b,c,d),v in x.items():
        if c:
            w=Q(c)*v/T3
            out[(a,b,c,d)] -= w
            out[(a,b,c-1,d)] += w
        if d:
            w=Q(d)*v/T3
            out[(a,b,c,d)] -= w
            out[(a,b,c,d-1)] += w
    return dict(out)

def M32(x):
    _,T3,_ = moments(x)
    out=defaultdict(Q)
    for (a,b,c,d),v in x.items():
        if c:
            w=Q(c)*v/T3
            out[(a,b,c,d)] -= w
            out[(a+1,b,c-1,d)] += w
        if d:
            w=Q(d)*v/T3
            out[(a,b,c,d)] -= w
            out[(a,b+1,c,d-1)] += w
    return dict(out)

def forced_G(x):
    T2,_,_=moments(x)
    out=defaultdict(Q)
    for k,v in x.items():
        a,b,c,d=k
        out[k] -= Q(a+b)*v/T2
    K2=sum(Q(a*(a-1)+b*(b-1))*v for (a,b,c,d),v in x.items())/T2
    K3=2*sum(Q(a*c+b*d)*v for (a,b,c,d),v in x.items())/T2
    K32=2*sum(Q(a*d+b*c)*v for (a,b,c,d),v in x.items())/T2
    add_scaled(out,D2(x),K2)
    add_scaled(out,D3(x),K3)
    add_scaled(out,M32(x),K32)
    return dict(out),(K2,K3,K32)

def free_F(x,s,orient):
    a,b,c,d=s
    out=defaultdict(Q)
    out[s] -= 1
    if orient=="T":
        add_scaled(out,D2(x),Q(a))
        add_scaled(out,D3(x),Q(2*c))
        add_scaled(out,M32(x),Q(2*d))
        u=Q(b)
    else:
        add_scaled(out,D2(x),Q(b))
        add_scaled(out,D3(x),Q(2*d))
        add_scaled(out,M32(x),Q(2*c))
        u=Q(a)
    return dict(out),u

def full_drift(x,s,orient):
    T2,_,S=moments(x)
    rho=2*S/T2
    assert rho < 1
    F,u=free_F(x,s,orient)
    G,K=forced_G(x)
    lam=u/(1-rho)
    out=defaultdict(Q,F)
    add_scaled(out,G,lam)
    return dict(out),rho,lam,K

def delta_rho(x,dx):
    T2,_,S=moments(x)
    dT2,_,dS=moments(dx)
    return 2*(dS*T2-S*dT2)/(T2*T2)

def phi_rate_per_removed_variable(x,s,orient,eta=Q(2),beta=Q(1)):
    dx,rho,lam,K=full_drift(x,s,orient)
    dT2,dT3,_=moments(dx)
    dm2=dT2/2
    dm3=dT3/3
    dr=delta_rho(x,dx)
    dphi=dm2+eta*dm3+beta*dr/(1-rho)
    removed=-mass(dx)
    return dphi/removed,(dm2,dm3,dr,removed,rho,lam)

def fmt(q):
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)

# Exact finite state. U and V have the same total signed degrees:
# U: positive total 2, negative total 3; V: positive total 2, negative total 3.
U=(2,1,0,2)
V=(0,0,2,3)
x={
    U: Q(1,10),
    V: Q(1,10),
    (1,0,1,0): Q(1,5),
    (0,1,0,1): Q(1,5),
    (1,1,1,1): Q(1,5),
    (0,0,0,0): Q(1,5),
}
assert mass(x)==1

T2,T3,S=moments(x)
A,B=signed_2_mass(x)
rho=2*S/T2
print("T04 FOUR-SPECTRUM EXACT RATIONAL DRIFT VERIFIER")
print("state_mass =",fmt(mass(x)))
print("T2 =",fmt(T2),"T3 =",fmt(T3),"S =",fmt(S),"rho =",fmt(rho))
print("signed_2_masses A,B =",fmt(A),fmt(B))

# Operator identities.
op_expected={
    "D2": (Q(0),Q(-1),Q(0)),
    "D3": (Q(0),Q(0),Q(-1)),
    "M32":(Q(0),Q(1),Q(-1)),
}
for name,op in (("D2",D2(x)),("D3",D3(x)),("M32",M32(x))):
    dm=mass(op); dT2,dT3,_=moments(op)
    got=(dm,dT2,dT3)
    exp=op_expected[name]
    print(name,"mass,dT2,dT3 =",tuple(fmt(z) for z in got),
          "PASS" if got==exp else "FAIL")
    assert got==exp

# Branching matrix, row = parent unit sign (+,-), col = child sign (+,-).
Mpp=S/T2
Mpm=S*B/(A*T2)
Mmp=S*A/(B*T2)
Mmm=S/T2
trace=Mpp+Mmm
det=Mpp*Mmm-Mpm*Mmp
print("branch_matrix = [[%s,%s],[%s,%s]]" %
      (fmt(Mpp),fmt(Mpm),fmt(Mmp),fmt(Mmm)))
print("branch_trace =",fmt(trace),"branch_det =",fmt(det),
      "rho_match =", trace==rho and det==0)
assert trace==rho and det==0

G,K=forced_G(x)
print("K2,K3,K32 =",tuple(fmt(z) for z in K))
print("forced_G_mass =",fmt(mass(G)),"PASS" if mass(G)==-1 else "FAIL")
assert mass(G)==-1

# Full-cascade mass identity: one free variable plus expected forced variables.
for s in (U,V):
    for orient in ("T","F"):
        dx,r,lam,K=full_drift(x,s,orient)
        expected=-(1+lam)
        print("full",s,orient,
              "lambda =",fmt(lam),
              "mass =",fmt(mass(dx)),
              "expected =",fmt(expected),
              "PASS" if mass(dx)==expected else "FAIL")
        assert mass(dx)==expected

# Barrier potential Phi = m2 + 2 m3 - log(1-rho), derivative only.
print("barrier: Phi=m2+2*m3-log(1-rho); report dPhi per expected variable removed")
for s,label in ((U,"U"),(V,"V")):
    vals={}
    for orient in ("T","F"):
        sc,detail=phi_rate_per_removed_variable(x,s,orient)
        vals[orient]=sc
        dm2,dm3,dr,removed,r,lam=detail
        print(label,orient,
              "score =",fmt(sc),
              "float=%.12f"%float(sc),
              "dm2 =",fmt(dm2),"dm3 =",fmt(dm3),
              "drho =",fmt(dr),
              "removed =",fmt(removed))
    best="T" if vals["T"]<vals["F"] else "F"
    print(label,"best_orientation =",best)

assert (U[0]+U[2],U[1]+U[3])==(V[0]+V[2],V[1]+V[3])==(2,3)
uT,_=phi_rate_per_removed_variable(x,U,"T")
uF,_=phi_rate_per_removed_variable(x,U,"F")
vT,_=phi_rate_per_removed_variable(x,V,"T")
vF,_=phi_rate_per_removed_variable(x,V,"F")
assert uT<uF and vF<vT
print("same_total_degree_pair =", (2,3))
print("opposite_4D_optimal_polarities = PASS")
print("ALL_EXACT_CHECKS_PASS")
