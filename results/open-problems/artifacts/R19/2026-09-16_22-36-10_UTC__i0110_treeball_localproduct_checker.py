#!/usr/bin/env python3
"""R19 / I0110 exact finite self-check.

This checker does NOT prove the asymptotic random-graph theorem.  It checks
only the finite algebra used in the report:
  1. Salez Problem 2.1's nine reference labels are nine distinct labels;
  2. the exact tree-ball Poincare quotient normalization
       (1/2)/(r/32) = 16/r
     when t=r/8 and Var >= t/4;
  3. the Poisson exponential-moment identity
       E[N^2 z^N]=(tz+t^2 z^2) exp(t(z-1));
  4. on a rational three-state example, the direct variance/energy equal
     the quadratic forms B_mu=Diag(mu)-mu mu^T and
     A_mu=(1/2) sum mu_x K_xy (e_y-e_x)(e_y-e_x)^T.

All equality checks are exact (fractions / symbolic algebra).
"""
from fractions import Fraction
import sympy as sp

refs = (80, 16, 14, 21, 13, 61, 22, 52, 62)
assert len(refs) == 9
assert len(set(refs)) == 9
print("reference list exact:", refs)

for r in (8, 16, 24, 40, 80, 160):
    t = Fraction(r, 8)
    energy = Fraction(1, 2)
    var_lower = t / 4
    quotient = energy / var_lower
    assert quotient == Fraction(16, r)
print("tree-ball quotient identity PASS: (1/2)/(r/32)=16/r")

t, z = sp.symbols("t z", positive=True)
M = sp.exp(t * (z - 1))
expr = sp.simplify(z * sp.diff(z * sp.diff(M, z), z))
target = (t * z + t**2 * z**2) * sp.exp(t * (z - 1))
assert sp.simplify(expr - target) == 0
print("Poisson E[N^2 z^N] identity PASS")

mu = [Fraction(1, 5), Fraction(3, 10), Fraction(1, 2)]
K = [
    [Fraction(0), Fraction(1, 2), Fraction(1, 2)],
    [Fraction(1, 3), Fraction(0), Fraction(2, 3)],
    [Fraction(1, 4), Fraction(3, 4), Fraction(0)],
]
f = [Fraction(2), Fraction(-1), Fraction(3, 2)]
mean = sum(mu[i] * f[i] for i in range(3))
var = sum(mu[i] * (f[i] - mean) ** 2 for i in range(3))
energy = Fraction(0)
for i in range(3):
    for j in range(3):
        energy += Fraction(1, 2) * mu[i] * K[i][j] * (f[j] - f[i]) ** 2

B = [[(mu[i] if i == j else Fraction(0)) - mu[i] * mu[j]
      for j in range(3)] for i in range(3)]
A = [[Fraction(0) for _ in range(3)] for _ in range(3)]
for x in range(3):
    for y in range(3):
        w = Fraction(1, 2) * mu[x] * K[x][y]
        v = [Fraction(0)] * 3
        v[y] += 1
        v[x] -= 1
        for i in range(3):
            for j in range(3):
                A[i][j] += w * v[i] * v[j]
qB = sum(f[i] * B[i][j] * f[j] for i in range(3) for j in range(3))
qA = sum(f[i] * A[i][j] * f[j] for i in range(3) for j in range(3))
assert var == qB == Fraction(601, 400)
assert energy == qA == Fraction(109, 40)
print("Var direct/matrix:", var, qB)
print("Energy direct/matrix:", energy, qA)
print("generalized Rayleigh finite identity PASS")
print("PASS")
