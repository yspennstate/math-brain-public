#!/usr/bin/env python3
"""Exact-algebra checker for account04/B12 unequal-MUX cross-deficit reduction.

No FEI claim is inferred from the finite grid. Exact Fraction checks verify the
six spectral weights, biased influences, Poincare currency split, and the
quadratic-lift/block-currency identities. Floating checks verify the displayed
block-slack formulas for an arbitrary smooth symmetric toy potential.
"""
from fractions import Fraction as F
import math

GRID=[F(1,8),F(1,4),F(3,8),F(1,2),F(5,8),F(3,4),F(7,8)]

def V(x): return 4*x*(1-x)
def phi(x): return x*(1-x)
def h2(x):
    x=float(x)
    if x<=0.0 or x>=1.0: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)
def H(ws):
    out=0.0
    for z in ws:
        z=float(z)
        if z>0.0: out -= z*math.log2(z)
    return out

def mux_data(p,q0,q1):
    r=(1-p)*q0+p*q1
    d=q0+q1-2*q0*q1
    ws=[
        (1-2*r)**2,
        (1-p)**2*V(q0),
        p*p*V(q1),
        V(p)*(q1-q0)**2,
        p*(1-p)*V(q0),
        p*(1-p)*V(q1),
    ]
    IA=ws[3]+ws[4]+ws[5]
    I0=ws[1]+ws[4]
    I1=ws[2]+ws[5]
    Itot=IA+I0+I1
    P=Itot/F(4,1)-r*(1-r)
    Q0=V(p)*V(q0)/F(16,1)
    Q1=V(p)*V(q1)/F(16,1)
    return r,d,ws,IA,I0,I1,P,Q0,Q1

def and_weights(a,b):
    return [(1-2*a*b)**2, V(a)*b*b, V(b)*a*a, V(a)*V(b)/F(4,1)]

def toy_gamma(x):
    # symmetric, nonnegative, deliberately not just quadratic
    y=float(x)*(1.0-float(x))
    return 3.0*y+2.0*y*y

def Ag(x,gamma): return gamma(x)+h2(V(x))

def D_and(a,b,gamma):
    return float(b)*Ag(a,gamma)+float(a)*Ag(b,gamma)-gamma(a*b)-H(and_weights(a,b))

def D_mux(p,q0,q1,gamma):
    r,d,ws,*_=mux_data(p,q0,q1)
    return float(d)*Ag(p,gamma)+float(1-p)*Ag(q0,gamma)+float(p)*Ag(q1,gamma)-gamma(r)-H(ws)

def R0_explicit(p,q0,q1,gamma):
    r,_,ws,*_=mux_data(p,q0,q1)
    return (float(1-p)*Ag(q0,gamma)
            +float(1-q0)*gamma(p*q1)+float(q0)*gamma(p*(1-q1))-gamma(r)
            -H(ws)+float(1-q0)*H(and_weights(p,q1))+float(q0)*H(and_weights(p,1-q1)))

def R1_explicit(p,q0,q1,gamma):
    r,_,ws,*_=mux_data(p,q0,q1)
    return (float(p)*Ag(q1,gamma)
            +float(1-q1)*gamma((1-p)*q0)+float(q1)*gamma((1-p)*(1-q0))-gamma(r)
            -H(ws)+float(1-q1)*H(and_weights(1-p,q0))+float(q1)*H(and_weights(1-p,1-q0)))

def lifted(gamma,a):
    return lambda x: gamma(x)+a*float(x)*(1.0-float(x))

checks=0
max_float_err=0.0
for p in GRID:
  for q0 in GRID:
    for q1 in GRID:
      r,d,ws,IA,I0,I1,P,Q0,Q1=mux_data(p,q0,q1)
      assert sum(ws,F(0,1))==1
      assert IA==V(p)*d
      assert I0==(1-p)*V(q0)
      assert I1==p*V(q1)
      assert P==p*(1-p)*(q0*(1-q0)+q1*(1-q1))
      assert P==Q0+Q1
      # AND Poincare currencies of either branch after revealing data 0/1.
      Pand_01=V(p)*V(q1)/F(16,1)
      Pand_10=V(1-p)*V(q0)/F(16,1)
      assert Pand_01==Q1 and Pand_10==Q0

      D=D_mux(p,q0,q1,toy_gamma)
      L0=float(1-q0)*D_and(p,q1,toy_gamma)+float(q0)*D_and(p,1-q1,toy_gamma)
      L1=float(1-q1)*D_and(1-p,q0,toy_gamma)+float(q1)*D_and(1-p,1-q0,toy_gamma)
      e0=abs((D-L0)-R0_explicit(p,q0,q1,toy_gamma))
      e1=abs((D-L1)-R1_explicit(p,q0,q1,toy_gamma))
      max_float_err=max(max_float_err,e0,e1)
      assert e0<2e-12 and e1<2e-12

      aa=0.173
      gl=lifted(toy_gamma,aa)
      Dl=D_mux(p,q0,q1,gl)
      assert abs((Dl-D)-aa*float(P))<3e-12
      r0=R0_explicit(p,q0,q1,toy_gamma)
      r1=R1_explicit(p,q0,q1,toy_gamma)
      r0l=R0_explicit(p,q0,q1,gl)
      r1l=R1_explicit(p,q0,q1,gl)
      assert abs((r0l-r0)-aa*float(Q0))<3e-12
      assert abs((r1l-r1)-aa*float(Q1))<3e-12
      checks += 1

# Candidate constants used only for exact arithmetic in the conditional theorem.
a_dag=F(268204856,10**9)
c_ro=F(1,100)
kappa=a_dag-c_ro
assert kappa==F(258204856,10**9)
print('PASS')
print('grid_triples',checks)
print('exact_fraction_identities_per_triple',8)
print('max_block_formula_float_error',format(max_float_err,'.3e'))
print('a_dagger',float(a_dag))
print('certified_AND_base_margin_c0',float(c_ro))
print('cross_deficit_kappa',float(kappa))
print('closure_target','R0_dagger + R1_dagger >= -0.258204856 * P_MUX')
