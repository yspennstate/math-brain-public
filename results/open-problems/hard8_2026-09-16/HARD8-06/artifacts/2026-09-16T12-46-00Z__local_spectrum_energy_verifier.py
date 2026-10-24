#!/usr/bin/env python3
"""
Exact verifier for HARD8-06 all-depth local-field spectrum checkpoint.

Pure standard library. No randomness, floating point acceptance tests, external
solver, network access, or timeout inference.

Checks:
  1. balanced-box increment C_m(s+1)-C_m(s)=2 floor(s/m);
  2. affine hierarchical energy against the exact base-q digit-sum formula;
  3. projective increment and affine-branch recursion;
  4. superadditivity of affine/projective energies on a finite exhaustive grid;
  5. simultaneous balanced occupancy at every residue-tree depth;
  6. explicit Q_p affine sharpness using roots 0,...,s-1;
  7. explicit finite Q_p projective sharpness using rational representatives
     of the q+1 first branches;
  8. exact finite-family aggregation lower bound using Fraction arithmetic.
"""

from fractions import Fraction


def C(m, s):
    if m <= 0 or s < 0:
        raise ValueError
    a, r = divmod(s, m)
    return m * a * (a - 1) + 2 * r * a


def E(q, s):
    if q < 2 or s < 0:
        raise ValueError
    ans = 0
    m = q
    while m < s:
        ans += C(m, s)
        m *= q
    return ans


def P(q, s):
    if q < 2 or s < 0:
        raise ValueError
    ans = 0
    m = q + 1
    while m < s:
        ans += C(m, s)
        m *= q
    return ans


def digit_sum(n, q):
    ans = 0
    while n:
        ans += n % q
        n //= q
    return ans


def E_digit(q, s):
    num = s * (s - 1) - 2 * sum(digit_sum(t, q) for t in range(s))
    assert num % (q - 1) == 0
    return num // (q - 1)


def ceil_log2(s):
    if s <= 1:
        return 0
    return (s - 1).bit_length()


def vp_int(n, p):
    if n == 0:
        raise ValueError("v_p(0)")
    n = abs(n)
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def vp_frac(x, p):
    x = Fraction(x)
    if x == 0:
        raise ValueError("v_p(0)")
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)


def chordal_delta(u, v, p):
    u = Fraction(u)
    v = Fraction(v)
    hu = 0 if u == 0 else max(0, -vp_frac(u, p))
    hv = 0 if v == 0 else max(0, -vp_frac(v, p))
    return vp_frac(u - v, p) + hu + hv


def affine_balanced_level_energy(q, s, ell):
    m = q ** ell
    occ = [0] * m
    for t in range(s):
        occ[t % m] += 1
    return sum(n * (n - 1) for n in occ)


def projective_balanced_level_energy(q, s, ell):
    m = (q + 1) * (q ** (ell - 1))
    occ = [0] * m
    for t in range(s):
        occ[t % m] += 1
    return sum(n * (n - 1) for n in occ)


def projective_points_Qp(p, s):
    """Explicit finite rational points realizing balanced mixed-radix leaves.

    Pick L minimal with (p+1)p^(L-1) >= s. A leaf index j is encoded by
      b = j mod (p+1), t = floor(j/(p+1)).
    For b<p use x=b+p*t.
    For the infinity branch b=p use reciprocal coordinate
      w=1/x=p*(t+p^(L-1)),
    which is nonzero and has the requested residue prefix.
    """
    if s == 0:
        return []
    L = 1
    m = p + 1
    while m < s:
        L += 1
        m *= p
    pts = []
    for j in range(s):
        b = j % (p + 1)
        t = j // (p + 1)
        if b < p:
            x = Fraction(b + p * t, 1)
        else:
            w = p * (t + p ** (L - 1))
            x = Fraction(1, w)
        pts.append(x)
    assert len(set(pts)) == s
    return pts


counts = {
    "C_increment": 0,
    "E_digit": 0,
    "P_increment": 0,
    "P_recursion": 0,
    "superadditivity": 0,
    "balanced_tree_levels": 0,
    "affine_Qp_sharpness": 0,
    "projective_Qp_sharpness": 0,
    "family_aggregation": 0,
}

# 1. C increments.
for m in range(1, 41):
    for s in range(0, 501):
        assert C(m, s + 1) - C(m, s) == 2 * (s // m)
        counts["C_increment"] += 1

# 2-3. Exact energy formulas.
for q in range(2, 13):
    for s in range(0, 1001):
        assert E(q, s) == E_digit(q, s)
        counts["E_digit"] += 1

        a = s // (q + 1)
        inc = 2 * (q * a - digit_sum(a, q)) // (q - 1)
        assert P(q, s + 1) - P(q, s) == inc
        counts["P_increment"] += 1

        a0, r = divmod(s, q + 1)
        rhs = C(q + 1, s) + (q + 1 - r) * E(q, a0) + r * E(q, a0 + 1)
        assert P(q, s) == rhs
        counts["P_recursion"] += 1

# 4. Superadditivity.
for q in range(2, 9):
    for a in range(0, 81):
        for b in range(0, 81):
            assert E(q, a + b) >= E(q, a) + E(q, b)
            assert P(q, a + b) >= P(q, a) + P(q, b)
            counts["superadditivity"] += 2

# 5. Simultaneous balanced occupancy.
for q in range(2, 8):
    for s in range(1, 201):
        ell = 1
        while q ** ell < s:
            assert affine_balanced_level_energy(q, s, ell) == C(q ** ell, s)
            counts["balanced_tree_levels"] += 1
            ell += 1

        ell = 1
        m = q + 1
        while m < s:
            assert projective_balanced_level_energy(q, s, ell) == C(m, s)
            counts["balanced_tree_levels"] += 1
            ell += 1
            m *= q

# 6. Actual Q_p affine sharpness.
for p in (2, 3, 5, 7):
    for s in range(2, 101):
        energy = 0
        for i in range(s):
            for j in range(i + 1, s):
                energy += 2 * vp_int(j - i, p)
        assert energy == E(p, s)
        counts["affine_Qp_sharpness"] += 1

# 7. Actual finite Q_p projective sharpness.
for p in (2, 3, 5):
    for s in range(2, 61):
        pts = projective_points_Qp(p, s)
        energy = 0
        for i in range(s):
            for j in range(i + 1, s):
                d = chordal_delta(pts[i], pts[j], p)
                assert d >= 0
                energy += 2 * d
        assert energy == P(p, s), (p, s, energy, P(p, s), pts)
        counts["projective_Qp_sharpness"] += 1

# 8. Exact finite-family aggregation inequality.
# Synthetic exact-field spectra; once local parameters and class sizes are fixed,
# the inequality is purely arithmetic.
for H in range(1, 5):
    for seed in range(0, 800):
        ss = [((seed * (j + 3) + 7 * j * j + 5) % 37) for j in range(H)]
        qs = [2 + ((seed + 2 * j) % 7) for j in range(H)]
        es = [1 + ((3 * seed + j) % 4) for j in range(H)]
        S = sum(ss)
        if S == 0:
            continue
        Emax = max(es)
        Qmax = max(qs)
        lhs = sum(Fraction(E(q, s), e) for q, s, e in zip(qs, ss, es))
        rhs = Fraction(1, Emax) * (
            Fraction(S * S, H * (Qmax - 1))
            - S * ceil_log2(S)
            - 2 * S
        )
        assert lhs >= rhs, (H, seed, ss, qs, es, lhs, rhs)
        counts["family_aggregation"] += 1

print("ALL_CHECKS_PASSED")
for key in counts:
    print(f"{key} = {counts[key]}")
