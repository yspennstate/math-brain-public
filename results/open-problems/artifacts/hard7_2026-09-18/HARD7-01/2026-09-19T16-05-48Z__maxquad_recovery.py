#!/usr/bin/env python3
"""
HARD7-01 run 20 support artifact.

Two roles only:
(1) exact symbolic algebra for the one-cell max-of-quadratics family;
(2) deterministic sphere-quadrature sanity check showing that a coarse apparent
    violation can disappear under refinement.

The quadrature section is EXPLORATORY NUMERICS, not a proof of a continuous
sphere inequality and not an exhaustive search.
"""
import math
import numpy as np
import sympy as sp

# ---------- exact symbolic algebra ----------
A, b, c = sp.symbols("A b c", positive=True)
m = (A + b*(1 + 2*c)) / (3*(A+b))
s2 = (3*A + b*(3 + 2*c + 8*c**2)) / (15*(A+b))
var = sp.expand(s2 - m**2)
defect = sp.factor(sp.Rational(2,5)*m*(1-m) - var)

print("EXACT_SYMBOLIC_DEFECT")
print(defect)
expected = 2*b*c*((3-4*c)*A + (3-2*c)*b)/(15*(A+b)**2)
print("IDENTITY_OK =", sp.simplify(defect-expected) == 0)

def one_cell(a):
    A = math.atan(1.0/math.sqrt(a))
    b = math.sqrt(a)/(1.0+a)
    c = a/(1.0+a)
    m = (A+b*(1+2*c))/(3*(A+b))
    s2 = (3*A+b*(3+2*c+8*c*c))/(15*(A+b))
    v = s2-m*m
    R = v/(m*(1-m))
    D = 0.4*m*(1-m)-v
    return m, v, R, D

print("\nONE_CELL_VALUES")
for a0 in (1e-4,1e-2,1e-1,1.0,10.0,100.0,1e4):
    print(f"a={a0:g} m={one_cell(a0)[0]:.15g} R={one_cell(a0)[2]:.15g} defect={one_cell(a0)[3]:.15g}")

# ---------- deterministic exploratory quadrature ----------
def fib_sphere(n):
    i = np.arange(n, dtype=float)
    z = 1.0 - 2.0*(i+0.5)/n
    ga = math.pi*(3.0-math.sqrt(5.0))
    th = ga*i
    r = np.sqrt(np.maximum(0.0,1.0-z*z))
    return np.column_stack((r*np.cos(th), r*np.sin(th), z))

def eval_general(As, Bs, n):
    X = fib_sphere(n)
    phi = np.stack([np.einsum("ni,ij,nj->n",X,M,X) for M in As],axis=1).max(axis=1)
    psi = np.stack([np.einsum("ni,ij,nj->n",X,M,X) for M in Bs],axis=1).max(axis=1)
    H = phi+psi
    w = H**(-1.5)
    U = phi/H
    Z = w.sum()
    m = (w*U).sum()/Z
    v = (w*(U-m)**2).sum()/Z
    R = v/(m*(1-m))
    return m,v,R

# A fixed candidate found by a coarse random max-of-rank-one scan.
# It looked > 2/5 at N=20,000 but does not survive refinement.
As = [
np.array([[24.4327060304,6.9740913608,0.8880452797],
          [6.9740913608,1.9906902759,0.2534843625],
          [0.8880452797,0.2534843625,0.0322774079]]),
np.array([[6.8748793075,9.7425084724,8.1604221010],
          [9.7425084724,13.8062745671,11.5642730441],
          [8.1604221010,11.5642730441,9.6863502452]]),
0.0005097442*np.eye(3)
]
Bs = [
np.array([[0.0754505981,0.1915033160,0.1044620470],
          [0.1915033160,0.4860600303,0.2651381021],
          [0.1044620470,0.2651381021,0.1446286648]]),
np.array([[0.0927191683,-0.0327204118,-0.0013981163],
          [-0.0327204118,0.0115469689,0.0004933925],
          [-0.0013981163,0.0004933925,0.0000210823]]),
0.0005097442*np.eye(3)
]
print("\nEXPLORATORY_FIXED_CANDIDATE")
for n in (20000,80000,200000,600000):
    mm,vv,rr = eval_general(As,Bs,n)
    print(f"N={n} m={mm:.15g} var={vv:.15g} R={rr:.15g} threshold_gap={0.4-rr:.15g}")
print("NUMERICS_ARE_NOT_A_CERTIFICATE = True")
