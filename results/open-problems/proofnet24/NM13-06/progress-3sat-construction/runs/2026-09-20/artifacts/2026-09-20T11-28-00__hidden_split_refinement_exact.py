#!/usr/bin/env python3
"""Exact rational checks for NM13-06 T04 hidden 2/3-degree split refinement.

This is not a threshold certificate.  It checks the exact algebra in the
exchangeable-split/adjoint refinement lemma and a rational product-Poisson
benchmark used in the accompanying report.

Notation at a unit-free checkpoint:
  x[a,b,c,d] = density with positive/negative 2-degrees a,b and
               positive/negative 3-degrees c,d.
  i=a+c, j=b+d are the coarse Hajiaghayi--Sorkin total signed degrees.

For a linear first-variation functional L, define
  A = L(D2) - L(G)/(1-rho),
  B = 2 L(D3-M32),
  Theta = A-B.
The exact polarity gap in coarse cell (i,j) is
  Delta = (i-j) B + (a-b) Theta.

Under the source conditional-uniformity model, if theta is the fraction of
surviving occurrences that are in 2-clauses, then for bounded i,j the hidden
split is asymptotically a~Bin(i,theta), b~Bin(j,theta), independently up to
the standard without-replacement O(1/n) correction.  The best coarse-vs-fine
first-variation gain is
  (E|Delta|-|E Delta|)/2.
"""
from fractions import Fraction as Q
from math import comb


def fmt(x):
    if isinstance(x, Q):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    return str(x)


def binom_prob(n, k, p):
    return Q(comb(n, k)) * p**k * (1-p)**(n-k)


def exact_cell_gain(i, j, theta, A, B):
    """Return Jensen refinement gain, E Delta, E|Delta| exactly."""
    Th = A-B
    ed = Q(0)
    ea = Q(0)
    prob = Q(0)
    signs = set()
    for a in range(i+1):
        pa = binom_prob(i, a, theta)
        for b in range(j+1):
            pb = binom_prob(j, b, theta)
            w = pa*pb
            d = Q(i-j)*B + Q(a-b)*Th
            prob += w
            ed += w*d
            ea += w*abs(d)
            if w and d:
                signs.add(1 if d > 0 else -1)
    assert prob == 1
    gain = (ea-abs(ed))/2
    return gain, ed, ea, signs


# Product-Poisson benchmark parameters.  If a,b~Pois(lambda2) and
# c,d~Pois(lambda3), all independent with total variable mass u, then
# rho=lambda2.  For Phi=m2+eta*m3-beta*log(1-rho), elementary factorial
# moments give the closed operator derivatives below.
lambda2 = Q(1,4)
lambda3 = Q(4,1)
u = Q(4,5)
eta = Q(2,1)
beta = Q(1,1)
assert lambda2 < 1

rho = lambda2
LD2 = -Q(1,2) - beta/(2*u*(1-lambda2))
LD3 = -eta/Q(3)
LM32 = Q(1,2) - eta/Q(3) + beta/(2*u*(1-lambda2))
LG = ((1-2*eta)*lambda3 - (3*lambda2+1)/2
      + beta*(2*lambda3-lambda2-1)/(2*u*(1-lambda2)))
A = LD2 - LG/(1-rho)
B = 2*(LD3-LM32)
Theta = A-B

# Closed-form simplification proved in the report.
Theta_closed = ((1+lambda2+(2*eta-1)*lambda3)/(1-lambda2)
                + beta*(1-lambda3)/(u*(1-lambda2)**2))
assert Theta == Theta_closed

# In this product-Poisson benchmark the fraction of occurrences that live in
# 2-clauses is theta=lambda2/(lambda2+lambda3).
theta = lambda2/(lambda2+lambda3)

print("T04 HIDDEN-SPLIT REFINEMENT EXACT CHECK")
print("lambda2 =", fmt(lambda2), "lambda3 =", fmt(lambda3), "u =", fmt(u))
print("rho =", fmt(rho), "theta_occurrence_2 =", fmt(theta))
print("L(D2) =", fmt(LD2))
print("L(D3) =", fmt(LD3))
print("L(M32) =", fmt(LM32))
print("L(G) =", fmt(LG))
print("A =", fmt(A), "B =", fmt(B), "Theta =", fmt(Theta))
print("Theta_closed_match =", Theta == Theta_closed)
assert (LD2,LD3,LM32,LG,A,B,Theta,theta) == (
    Q(-4,3), Q(-2,3), Q(2,3), Q(-29,4), Q(25,3), Q(-8,3), Q(11), Q(1,17))

# Balanced (1,1): Delta=(a-b)Theta.  Exact strict gain equals
# |Theta| theta(1-theta).
g11, ed11, ea11, signs11 = exact_cell_gain(1,1,theta,A,B)
closed11 = abs(Theta)*theta*(1-theta)
assert g11 == closed11 == Q(176,289)
assert ed11 == 0 and signs11 == {-1,1}
print("cell(1,1): EDelta =", fmt(ed11), "EabsDelta =", fmt(ea11),
      "gain =", fmt(g11), "float = %.12f" % float(g11), "STRICT =", g11>0)

# Non-balanced cells: the hidden split can also reverse polarity preference.
for i,j in [(1,2),(2,3),(3,4),(1,3),(2,4),(3,5)]:
    g,ed,ea,signs = exact_cell_gain(i,j,theta,A,B)
    print(f"cell({i},{j}): EDelta={fmt(ed)} EabsDelta={fmt(ea)} "
          f"gain={fmt(g)} float={float(g):.12f} signs={sorted(signs)}")
    assert g > 0 and signs == {-1,1}

# Algebraic mean check under Bin(i,theta), Bin(j,theta):
# E Delta = (i-j)(B + theta Theta).
for i in range(0,6):
    for j in range(0,6):
        g,ed,ea,signs = exact_cell_gain(i,j,theta,A,B)
        assert ed == Q(i-j)*(B+theta*Theta)
print("binomial_mean_identity_for_0<=i,j<=5 = PASS")

# A simple finite-population correction used in the proof: coupling an
# ordered k-sample without replacement from N labelled occurrence slots to a
# with-replacement sample fails only if the latter repeats a slot.  Union
# bound <= k(k-1)/(2N).  We record the symbolic coefficient for h=31 used by
# Hajiaghayi--Sorkin, i+j<=62.
kmax = 62
collision_numerator = kmax*(kmax-1)//2
print("without_replacement_to_iid_TV_bound <=", collision_numerator, "/ N")
assert collision_numerator == 1891

print("ALL_EXACT_CHECKS_PASS")
