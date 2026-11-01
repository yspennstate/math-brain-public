#!/usr/bin/env python3
"""
R16 / I0112 exact self-check for the synchronous direct-product cutoff run.

This checker certifies only finite/algebraic subclaims:
1. the exact algebraic inequality showing that the Bordenave--Lacoin
   Theorem-B right-hand side is < 1/2 at u=rho_d for D=d^2;
2. the d=6 trace threshold N>=16 forcing the direct square to be
   non-Ramanujan as a 36-regular graph;
3. exact comparison of the local growth bases (d-1)^2 < d^2-1;
4. exact spectral tensor identities on a small rational stochastic example.

The asymptotic cutoff theorem is proved analytically in the run report.
"""
from fractions import Fraction
import itertools

print("R16 I0112 synchronous-tensor exact checker")

# 1. Exact algebraic certificate:
# rho_d/rho_D = d/sqrt(d+1), D=d^2.
# F_D(rho_d)<1/2 is equivalent to
#   arcosh(d/sqrt(d+1)) > (1/4) log(d^2-1).
# Squaring the equivalent positive cosh inequality reduces to:
#   4(2d+1)^2(d-1)^3 > d^4(d+1).
def edge_certificate(d):
    return 4*(2*d+1)**2*(d-1)**3 - d**4*(d+1)

for d in range(3,10001):
    assert edge_certificate(d) > 0
print("BL_EDGE_HALF_BARRIER_PASS d=3..10000")
print("BL_EDGE_d6_integer_margin", edge_certificate(6))

# 2. Previous trace certificate, rechecked exactly:
# some nontrivial adjacency eigenvalue obeys
# lambda^2 >= d(N-d)/(N-1).
# The direct square has eigenvalue d lambda and fails D=d^2 Ramanujan if
# d^3 (N-d)/(N-1) > 4(d^2-1).
def nonram_margin(d,N):
    return d**3*(N-d) - 4*(d*d-1)*(N-1)

d=6
vals=[]
for N in range(7,31):
    vals.append((N, nonram_margin(d,N)))
first=min(N for N,m in vals if m>0)
assert first==16
assert all(nonram_margin(d,N)>0 for N in range(16,10000))
print("D6_NONRAM_FIRST_N", first)
print("D6_NONRAM_MARGIN_N16", nonram_margin(6,16))

# 3. Direct product local growth base is strictly smaller than D-tree base.
for d in range(3,10001):
    assert (d-1)**2 < d*d-1
    assert Fraction((d-1)**2, d*d-1) == Fraction(d-1,d+1)
print("LOCAL_GROWTH_BASE_RATIO_PASS d=3..10000")

# 4. Exact tensor-spectrum sanity check on a rational reversible kernel.
P = [
    [Fraction(7,12), Fraction(1,6), Fraction(1,4)],
    [Fraction(1,6), Fraction(7,12), Fraction(1,4)],
    [Fraction(1,4), Fraction(1,4), Fraction(1,2)],
]
vecs=[
    (Fraction(1),Fraction(1),Fraction(1)),
    (Fraction(1),Fraction(-1),Fraction(0)),
    (Fraction(1),Fraction(1),Fraction(-2)),
]
def mv(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M)))
evals=[]
for v in vecs:
    w=mv(P,v)
    lam=None
    for vi,wi in zip(v,w):
        if vi:
            lam=wi/vi; break
    assert lam is not None
    assert all(wi==lam*vi for wi,vi in zip(w,v))
    evals.append(lam)
assert evals[0]==1

def kron_mv(P,u,v):
    Pu=mv(P,u); Pv=mv(P,v)
    lhs=[]
    for i in range(3):
        for k in range(3):
            s=Fraction(0)
            for j in range(3):
                for l in range(3):
                    s += P[i][j]*P[k][l]*u[j]*v[l]
            lhs.append(s)
    rhs=[Pu[i]*Pv[k] for i in range(3) for k in range(3)]
    assert lhs==rhs
for u,v in itertools.product(vecs, repeat=2):
    kron_mv(P,u,v)
print("TENSOR_SPECTRUM_EXACT_IDENTITY_PASS")
print("EXACT_EIGENVALUES", [str(x) for x in evals])

print("ALL_EXACT_CHECKS_PASS")
