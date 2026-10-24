#!/usr/bin/env python3
"""
P10/F0119 outward-rounded certificate: arbitrary-orbit KS contraction
on max(|m|,|n|) <= 167/400 via exact angular Bernstein enclosure.

Inputs already proved path-scoped:
  * corrected exact H4-H6;
  * exact H7-H14 D3-invariant identities;
  * analytic absolute remainder beginning at degree 15.

New step here:
for fixed radial variables r,t, the retained normalized polynomial is of
degree <=4 separately in x=Re(m^3)/|m|^3 and y=Re(n^3)/|n|^3.
Convert the exact angular power basis on [-1,1]^2 to degree-4 tensor
Bernstein form on [0,1]^2. The convex-hull property removes angular
interval dependency exactly. Only (r,t) are adaptively subdivided.
"""
from fractions import Fraction
from math import comb
import mpmath as mp

mp.mp.dps = 60
iv = mp.iv
SQ2 = iv.sqrt(2)

RMAX = Fraction(167, 400)  # 0.4175 exactly
TARGET = mp.mpf("0.00002")

def I(q):
    if isinstance(q, Fraction):
        return iv.mpf(q.numerator) / q.denominator
    if isinstance(q, int):
        return iv.mpf(q)
    if isinstance(q, mp.mpf):
        return iv.mpf(q)
    raise TypeError(type(q))

# Exact coefficients from corrected path-scoped H4-H14.
am = -iv.mpf(1)/4 + SQ2/16
bm = 13*SQ2/36
a7 = -iv.mpf(1)/2 + SQ2/16
b7 = -7*SQ2/24
g7 = -19*SQ2/48
c1 = -iv.mpf(9)/8 + 9*SQ2/128
c2 = -iv.mpf(1)/18 + SQ2/288
c4 = SQ2/6
c5 = SQ2/12
c6 = 83*SQ2/96
alpha11 = -iv.mpf(2)/5 + SQ2/80
beta11 = -iv.mpf(27)/10 + 27*SQ2/320
delta11 = -125*SQ2/288
eps11 = -51*SQ2/64
zeta11 = -55*SQ2/96
v1 = -2 + SQ2/32
v2 = 27*(-64 + SQ2)/256
v3 = 83*SQ2/192
v4 = 35*SQ2/96
v5 = 5*SQ2/16
v6 = 517*SQ2/384

def addterm(d, ij, c):
    d[ij] = d.get(ij, iv.mpf(0)) + c

def terms_k(k, t):
    """Power coefficients {(i,j): c_ij(t)} of P_k(t,x,y)."""
    d = {}
    if k == 4:
        addterm(d, (0,0), (5 - 2*t*t + 5*t**4)/72)
    elif k == 5:
        addterm(d, (1,0), am + bm*t**2)
        addterm(d, (0,1), am*t**5 + bm*t**3)
    elif k == 6:
        addterm(d, (0,0), iv.mpf(9)/40*(1+t**6) + iv.mpf(1)/36*(t**2+t**4))
        addterm(d, (2,0), iv.mpf(1)/20)
        addterm(d, (0,2), iv.mpf(1)/20*t**6)
        addterm(d, (1,1), -iv.mpf(5)/36*t**3)
    elif k == 7:
        addterm(d, (1,0), a7 + b7*t**2 + g7*t**4)
        addterm(d, (0,1), a7*t**7 + b7*t**5 + g7*t**3)
    elif k == 8:
        addterm(d, (0,0), iv.mpf(27)/64*(1+t**8) + iv.mpf(1)/6*(t**6+t**2) - iv.mpf(59)/288*t**4)
        addterm(d, (2,0), iv.mpf(1)/4)
        addterm(d, (0,2), iv.mpf(1)/4*t**8)
        addterm(d, (1,1), iv.mpf(1)/16*t**3*(1+t**2))
    elif k == 9:
        addterm(d, (1,0), c1 + c4*t**6 + c6*t**4)
        addterm(d, (0,1), c1*t**9 + c4*t**3 + c6*t**5)
        addterm(d, (3,0), c2)
        addterm(d, (0,3), c2*t**9)
        addterm(d, (1,2), c5*t**6)
        addterm(d, (2,1), c5*t**3)
    elif k == 10:
        addterm(d, (0,0), iv.mpf(27)/32*(1+t**10) - iv.mpf(5)/24*t**4*(1+t**2))
        addterm(d, (2,0), iv.mpf(15)/16 + iv.mpf(1)/6*t**4)
        addterm(d, (0,2), iv.mpf(15)/16*t**10 + iv.mpf(1)/6*t**6)
        addterm(d, (1,1), -iv.mpf(5)/36*t**3*(1+t**4) + iv.mpf(67)/576*t**5)
    elif k == 11:
        addterm(d, (3,0), alpha11)
        addterm(d, (0,3), alpha11*t**11)
        addterm(d, (1,0), beta11 + eps11*t**6 + zeta11*t**4)
        addterm(d, (0,1), beta11*t**11 + eps11*t**5 + zeta11*t**7)
        addterm(d, (2,1), delta11*t**5)
        addterm(d, (1,2), delta11*t**6)
    elif k == 12:
        addterm(d, (4,0), iv.mpf(31)/528)
        addterm(d, (0,4), iv.mpf(31)/528*t**12)
        addterm(d, (2,0), iv.mpf(279)/88 - iv.mpf(643)/1440*t**6)
        addterm(d, (0,2), iv.mpf(279)/88*t**12 - iv.mpf(643)/1440*t**6)
        addterm(d, (0,0), iv.mpf(2511)/1408*(1+t**12) + iv.mpf(5)/16*(t**8+t**4) + iv.mpf(833)/2880*t**6)
        addterm(d, (2,2), iv.mpf(101)/240*t**6)
        addterm(d, (1,1), iv.mpf(95)/576*(t**5+t**7))
    elif k == 13:
        addterm(d, (3,0), v1)
        addterm(d, (0,3), v1*t**13)
        addterm(d, (1,0), v2 + v5*t**8 + v6*t**6)
        addterm(d, (0,1), v2*t**13 + v5*t**5 + v6*t**7)
        addterm(d, (2,1), v3*t**7 + v4*t**5)
        addterm(d, (1,2), v3*t**6 + v4*t**8)
    elif k == 14:
        addterm(d, (4,0), iv.mpf(63)/104)
        addterm(d, (0,4), iv.mpf(63)/104*t**14)
        addterm(d, (2,2), -iv.mpf(19)/48*(t**8+t**6))
        addterm(d, (2,0), iv.mpf(8505)/832 + iv.mpf(29)/96*t**8 + iv.mpf(59)/96*t**6)
        addterm(d, (0,2), iv.mpf(8505)/832*t**14 + iv.mpf(29)/96*t**6 + iv.mpf(59)/96*t**8)
        addterm(d, (1,1), -iv.mpf(35)/96*(t**9+t**5) + iv.mpf(257)/1152*t**7)
        addterm(d, (0,0), iv.mpf(6561)/1664*(1+t**14) - iv.mpf(139)/192*(t**8+t**6))
    else:
        raise ValueError(k)
    return d

# Degree-4 Bernstein coefficients for x^i after x=2u-1, u in [0,1].
BETA = [[Fraction(0) for _ in range(5)] for __ in range(5)]
for i in range(5):
    for J in range(5):
        s = Fraction(0)
        for a in range(min(i, J)+1):
            s += Fraction(comb(i,a) * (2**a) * ((-1)**(i-a)) * comb(J,a), comb(4,a))
        BETA[i][J] = s

assert BETA[0] == [Fraction(1)]*5
assert BETA[1] == [Fraction(-1),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(1)]
assert BETA[2] == [Fraction(1),Fraction(0),Fraction(-1,3),Fraction(0),Fraction(1)]
assert BETA[3] == [Fraction(-1),Fraction(1,2),Fraction(0),Fraction(-1,2),Fraction(1)]
assert BETA[4] == [Fraction(1),Fraction(-1),Fraction(1),Fraction(-1),Fraction(1)]

def endpoint15_coeff(r):
    return (iv.mpf(1)/2*iv.mpf(2)**15/(15*14)/(1-2*r)
            + iv.mpf(2)**15/(15*14)*iv.mpf(2)**(-iv.mpf(15)/2)/(1-SQ2*r))

def tail15_coeff(r, t):
    den = 1+t**4
    z = r**2*t
    Ce = (endpoint15_coeff(r) + t**15*endpoint15_coeff(t*r))/den
    Cjd = r*t**8/(56*(1-z)*den)
    ell = (1+t)/SQ2
    q = t/2
    C26 = (7-6*z)/(1-z)**2
    C25 = (6-5*z)/(1-z)**2
    Ccub = iv.mpf(1)/3/den * (
        ell**3*t**6*C26
        + 3*r*ell**2*q*t**6*C26
        + 3*ell*q**2*t**5*C25
        + r*q**3*t**5*C25
    )
    C36 = (28-48*z+21*z**2)/(1-z)**3
    C35 = (21-35*z+15*z**2)/(1-z)**3
    C34 = (15-24*z+10*z**2)/(1-z)**3
    Cquart = iv.mpf(2)/9/den * (
        r*ell**4*t**6*C36
        + 4*ell**3*q*t**5*C35
        + 6*r*ell**2*q**2*t**5*C35
        + 4*ell*q**3*t**4*C34
        + r*q**4*t**4*C34
    )
    return Ce + Cjd + Ccub + Cquart

def bernstein_lower(box):
    (r0,r1),(t0,t1) = box
    r = iv.mpf([I(r0).a, I(r1).b])
    t = iv.mpf([I(t0).a, I(t1).b])
    den = 1+t**4

    coeff = {}
    for k in range(4,15):
        scale = r**(k-4)/den
        for ij,c in terms_k(k,t).items():
            coeff[ij] = coeff.get(ij, iv.mpf(0)) + c*scale

    lower = mp.inf
    for J in range(5):
        for K in range(5):
            bc = iv.mpf(0)
            for (i,j),c in coeff.items():
                bc += c * I(BETA[i][J]) * I(BETA[j][K])
            lower = min(lower, mp.mpf(bc.a))

    tail = tail15_coeff(r,t)*r**11
    return lower - mp.mpf(tail.b)

def split(box, depth):
    (r0,r1),(t0,t1) = box
    wr = (r1-r0)/RMAX
    wt = t1-t0
    if wr >= wt:
        m = (r0+r1)/2
        return [(((r0,m),(t0,t1)),depth+1), (((m,r1),(t0,t1)),depth+1)]
    m = (t0+t1)/2
    return [(((r0,r1),(t0,m)),depth+1), (((r0,r1),(m,t1)),depth+1)]

stack = [((((Fraction(0),RMAX),(Fraction(0),Fraction(1)))),0)]
evaluated = leaves = max_depth = 0
min_leaf = mp.inf
worst_leaf = None
while stack:
    box, depth = stack.pop()
    lo = bernstein_lower(box)
    evaluated += 1
    if lo > TARGET:
        leaves += 1
        if lo < min_leaf:
            min_leaf = lo
            worst_leaf = box
        max_depth = max(max_depth, depth)
        continue
    if depth >= 30:
        raise RuntimeError(("DEPTH_FAIL", box, lo, evaluated))
    stack.extend(split(box, depth))

print("RMAX =", f"{RMAX.numerator}/{RMAX.denominator}", "=", mp.mpf(RMAX.numerator)/RMAX.denominator)
print("TARGET_NORMALIZED_GAP =", TARGET)
print("evaluated_radial_boxes =", evaluated)
print("certified_radial_leaves =", leaves)
print("max_depth =", max_depth)
print("minimum_certified_leaf_lower =", min_leaf)
print("worst_leaf_box =", worst_leaf)
assert min_leaf > TARGET
print("ANGULAR_BERNSTEIN_RADIUS_04175_PASS")
print("OVERALL_PASS")
