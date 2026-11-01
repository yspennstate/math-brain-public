#!/usr/bin/env python3
"""
P26 independent exact audit for R20/I0100, p=41.

Claim audited:
    theta(complement G_{41,1}) = 2*sqrt(5),
where G_{p,1} is the Paley 1-localization on the nonzero quadratic
residues modulo p.

This checker independently:
  1. reconstructs the cyclic localized graph from F_41;
  2. recovers the complement difference classes modulo +/-;
  3. verifies the exact symmetry-reduced theta primal;
  4. verifies the exact LP dual at every Fourier frequency;
  5. verifies exact objective equality.

All certificate checks are symbolic exact arithmetic in SymPy.
"""
import sympy as sp

p = 41
n = (p - 1) // 2

# 6 is a primitive root mod 41; alpha=6^2 generates the nonzero squares.
g = 6
assert pow(g, 40, p) == 1
for q in (2, 5):
    assert pow(g, 40 // q, p) != 1
alpha = pow(g, 2, p)

Q = {pow(x, 2, p) for x in range(1, p)}
assert len(Q) == n
assert {pow(alpha, j, p) for j in range(n)} == Q

S = []
N = []
for d in range(1, n):
    val = (pow(alpha, d, p) - 1) % p
    (S if val in Q else N).append(d)

assert len(S) == 9
assert len(N) == 10
assert set(S) == {4,5,7,9,10,11,13,15,16}
assert set(N) == {1,2,3,6,8,12,14,17,18,19}

Nred = sorted(d for d in N if d <= n-d)
assert Nred == [1,2,3,6,8]

r5 = sp.sqrt(5)
rA = sp.sqrt(10 + 2*r5)
rB = sp.sqrt(50 + 10*r5)

# Paired Fourier masses for m=0,...,10; omitted masses are zero.
w = {m: sp.Integer(0) for m in range(n//2 + 1)}
w[0] = r5/10
w[1] = sp.Rational(1,4) - r5/20 - rA/16 + rB/80
w[4] = sp.Rational(1,8) + r5/40
w[5] = r5/10
w[6] = sp.Rational(3,8) - r5/8
w[9] = sp.Rational(1,4) - r5/20 + rA/16 - rB/80

assert sp.simplify(sum(w.values()) - 1) == 0
for m, val in w.items():
    assert sp.ask(sp.Q.nonnegative(val)) is True, (m, sp.simplify(val))

for d in Nred:
    moment = sum(w[m] * sp.cos(2*sp.pi*m*d/n) for m in w)
    assert sp.simplify(sp.trigsimp(moment)) == 0, (d, sp.simplify(moment))

primal_obj = sp.simplify(n*w[0])
assert primal_obj == 2*r5

a = r5/10
lam = {
    2: (5-r5)/20,
    6: (5+r5)/20,
    8: (5-r5)/10,
}
slacks = []
for m in range(n):
    lhs = a + sum(lam[d]*sp.cos(2*sp.pi*m*d/n) for d in lam)
    slack = sp.simplify(sp.trigsimp(lhs - (1 if m == 0 else 0)))
    assert sp.ask(sp.Q.nonnegative(slack)) is True, (m, slack)
    slacks.append(slack)

dual_obj = sp.simplify(n*a)
assert dual_obj == primal_obj == 2*r5
assert set(map(str, slacks)) == {
    "0",
    "sqrt(5)/4",
    "1",
    "-1/2 + sqrt(5)/4",
}

print("P26-I0100-P41-INDEPENDENT-EXACT-AUDIT: PASS")
print("p =", p, "n =", n, "alpha =", alpha)
print("localized_degree =", len(S))
print("complement_degree =", len(N))
print("complement_reduced_classes =", Nred)
print("positive_primal_support =", [m for m in w if w[m] != 0])
print("dual_slack_set =", sorted(set(map(str, slacks))))
print("theta_exact = 2*sqrt(5)")
print("theta_decimal =", sp.N(primal_obj, 30))
print("sqrt(p/2)_decimal =", sp.N(sp.sqrt(sp.Rational(p,2)), 30))
print("ratio =", sp.N(primal_obj/sp.sqrt(sp.Rational(p,2)), 30))
