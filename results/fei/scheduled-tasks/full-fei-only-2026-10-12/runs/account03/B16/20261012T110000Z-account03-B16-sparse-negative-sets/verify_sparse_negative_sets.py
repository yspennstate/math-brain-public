#!/usr/bin/env python3
"""Exact finite checks for a candidate sparse-negative-set FEI class lemma.

Only non-protected, generated Boolean truth tables; no evaluation-bank data.
Bounded d<=10 with fixed radius-0/1/2 balls and spectator/overlap controls.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, log2, isclose
import json


def walsh(values):
    w = list(values)
    step = 1
    while step < len(w):
        for base in range(0, len(w), 2 * step):
            for j in range(base, base + step):
                a, b = w[j], w[j + step]
                w[j], w[j + step] = a + b, a - b
        step *= 2
    return w


def analyze(d, negative):
    assert 2 <= d <= 10 and 1 <= len(negative) < (1 << d)
    N = 1 << d
    a = len(negative)
    f = [-1 if mask in negative else 1 for mask in range(N)]
    sums = walsh(f)
    p = [Fraction(z*z, N*N) for z in sums]
    assert sum(p) == 1
    alpha = Fraction(a, N)
    p0 = (1 - 2 * alpha) ** 2
    m = 4 * alpha * (1 - alpha)
    assert p[0] == p0 and sum(p[1:]) == m
    boundary = sum(1 for x in negative for i in range(d) if (x ^ (1 << i)) not in negative)
    inside = (d * a - boundary) // 2
    assert boundary == d*a - 2*inside
    assert 2 * inside <= a * log2(a) + 1e-10
    influence = sum(s.bit_count() * p[s] for s in range(N))
    assert influence == Fraction(2 * boundary, N)
    assert Fraction(2 * a * d, N) >= influence
    assert float(influence) + 1e-12 >= float(Fraction(2 * a, N) * (d-log2(a)))
    zeta = p[:]
    for i in range(d):
        for s in range(N):
            if (s & (1 << i)) == 0:
                zeta[s] += zeta[s | (1 << i)]
    assert zeta[0] == 1
    error = 0.0
    for s in range(1, N):
        if not p[s]:
            continue
        k = s.bit_count()
        F = sum((-1 if ((x & s).bit_count() & 1) else 1) for x in negative)
        assert sums[s] == -2 * F
        assert 1 <= abs(F) <= a
        R = sum((sum((-1 if ((x & s).bit_count() & 1) else 1)
                         for x in negative if (x & ~s) == y))**2
                for y in set(x & ~s for x in negative))
        assert R >= 1 and R <= a*a
        assert zeta[s] == Fraction(4 * (2**(d-k)) * R, N*N)
        assert zeta[s] / p[s] == Fraction(2**(d-k) * R, F*F)
        error += float(p[s]) * log2(Fraction(R,F*F))
    empty_entropy = 0.0 if p0 == 0 else float(p0) * log2(1/float(p0))
    H = sum(float(x) * log2(1/float(x)) for x in p if x)
    U = sum(float(p[s]) * log2(float(zeta[s]/p[s])) for s in range(N) if p[s])
    assert isclose(U, empty_entropy + d*float(m)-float(influence)+error, rel_tol=2e-12, abs_tol=3e-12)
    assert abs(error) <= 2 * float(m) * log2(a) + 1e-10
    assert H <= 2 * d * float(m) + 1e-10
    return dict(d=d,a=a,boundary=boundary,inside=inside,H_over_I=round(H/float(influence),8),U_over_I=round(U/float(influence),8),m=str(m),I=str(influence),U=round(U,12),H=round(H,12))


def ball(d, r):
    return {mask for mask in range(1 << d) if mask.bit_count() <= r}


def main():
    outputs=[]
    # Freely generated cases, not test/evaluation-bank questions.
    for d in range(2,11):
        for r in [0,1,2]:
            A=ball(d,r)
            if len(A) < 1 << d:
                outputs.append(analyze(d,A))
    # Non-product shared-input overlap, spectator padding and sign-complement controls.
    fixtures = [
      (6, {0, 1, 2, 4, 8}),
      (7, {0, 1, 3, 7, 15, 31}),
      (8, {x for x in range(1 << 8) if x % 8 == 0}),
      (8, set(range((1 << 8) - 1))),
    ]
    for d, A in fixtures:
        outputs.append(analyze(d, A))
    print(json.dumps({'schema':'fei-sparse-set-check/1','python_arithmetic':'exact Fraction and integer for all identities; float only for logarithms, error and induced-edge inequality','case_count':len(outputs),'cases':outputs,'all_exact_identities':'PASS','logarithmic_formulas':'PASS_numerical_only'},indent=2))

if __name__=='__main__':
    main()
