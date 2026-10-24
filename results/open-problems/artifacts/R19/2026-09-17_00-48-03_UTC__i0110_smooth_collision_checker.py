#!/usr/bin/env python3
"""Exact self-check for R19 / I0110 smooth-entropic-extraction lemmas.

All arithmetic is Fraction-exact. The finite atlas uses Omega=F_2^3,
X=F_2^2, q=Bernoulli(1/4)^3, and E={Hamming weight 1 or 2}.
We enumerate all 2^(2*3)=64 linear maps A: F_2^3 -> F_2^2 and check:

(1) the deterministic truncated-TV upper bound
    TV(P_A,U) <= (1-m) + (1/2)*sqrt(D_A),
    D_A = 4*sum_y r_A(y)^2 - m^2,
    using exact squaring (no floating point);
(2) the deterministic pre-mixing image bound
    TV(P_A,U) >= m - |A(E)|/4;
(3) the exact 2-universal averaged collision identity
    E_A[D_A] = (4-1)*sum_{w in E} q(w)^2.
"""
from fractions import Fraction
from itertools import product

K = 3
D = 2
N = 2**D
P = Fraction(1, 4)
OMEGAS = list(product((0, 1), repeat=K))
YS = list(product((0, 1), repeat=D))


def wt(x):
    return sum(x)


def qprob(x):
    w = wt(x)
    return (P**w) * ((1-P)**(K-w))


Q = {x: qprob(x) for x in OMEGAS}
E = [x for x in OMEGAS if wt(x) in (1, 2)]
M = sum((Q[x] for x in E), Fraction(0))
SUMQ2 = sum((Q[x] * Q[x] for x in E), Fraction(0))
TARGET = (N-1) * SUMQ2


def apply(A, x):
    out = []
    for i in range(D):
        s = 0
        for j in range(K):
            s ^= (A[i*K+j] & x[j])
        out.append(s)
    return tuple(out)


def tv(mu):
    u = Fraction(1, N)
    return Fraction(1, 2) * sum(abs(mu[y]-u) for y in YS)


Ds = []
upper_checks = 0
lower_checks = 0
all_As = list(product((0, 1), repeat=D*K))
for A in all_As:
    mu = {y: Fraction(0) for y in YS}
    r = {y: Fraction(0) for y in YS}
    image_E = set()
    for x in OMEGAS:
        y = apply(A, x)
        mu[y] += Q[x]
        if x in E:
            r[y] += Q[x]
            image_E.add(y)

    D_A = N * sum((v*v for v in r.values()), Fraction(0)) - M*M
    assert D_A >= 0
    Ds.append(D_A)

    # TV <= (1-M) + (1/2)*sqrt(D_A), checked without irrational arithmetic.
    residual = max(Fraction(0), 2*(tv(mu)-(1-M)))
    assert residual*residual <= D_A
    upper_checks += 1

    # TV >= M - |A(E)|/N.
    lower = M - Fraction(len(image_E), N)
    assert tv(mu) >= lower
    lower_checks += 1

AVG_D = sum(Ds, Fraction(0)) / len(Ds)
assert AVG_D == TARGET
assert M == Fraction(9, 16)
assert SUMQ2 == Fraction(135, 2048)
assert TARGET == Fraction(405, 2048)
assert min(Ds) == Fraction(27, 512)
assert max(Ds) == Fraction(243, 256)

# Exact 2-universality of all linear maps A: for every distinct x,x',
# exactly 1/N of the maps collide.
for x in OMEGAS:
    for xp in OMEGAS:
        if x == xp:
            continue
        collisions = sum(1 for A in all_As if apply(A, x) == apply(A, xp))
        assert Fraction(collisions, len(all_As)) == Fraction(1, N)

print("PASS")
print(f"maps={len(all_As)} upper_checks={upper_checks} lower_checks={lower_checks}")
print(f"m={M} sum_E_q2={SUMQ2}")
print(f"average_D={AVG_D} target={(N-1)}*sum_E_q2={TARGET}")
print(f"D_range=[{min(Ds)},{max(Ds)}]")
print("2-universality: PASS for every ordered distinct pair in F_2^3")
