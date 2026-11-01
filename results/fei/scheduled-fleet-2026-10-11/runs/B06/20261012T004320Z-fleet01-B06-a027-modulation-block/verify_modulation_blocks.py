#!/usr/bin/env python3
"""Exact finite audit for the A027 proper-block modulation theorem.

Walsh coefficients, squared spectral laws, influences, and physical block
telescope costs are Fractions.  Floating point is used only to display
entropy residuals after the underlying probability identities have passed.
"""

from fractions import Fraction
from itertools import product
from math import log2


def fwht(v):
    a = list(v)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def coeffs(vals):
    den = len(vals)
    return [Fraction(x, den) for x in fwht(vals)]


def law(vals):
    return [x * x for x in coeffs(vals)]


def entropy(p):
    return -sum(float(x) * log2(float(x)) for x in p if x)


def influence_from_law(p):
    return sum(x * s.bit_count() for s, x in enumerate(p))


def direct_influence(vals, bit):
    return Fraction(sum(vals[x] != vals[x ^ (1 << bit)] for x in range(len(vals))), len(vals))


def all_boolean(n):
    for mask in range(1 << (1 << n)):
        yield [1 if ((mask >> x) & 1) == 0 else -1 for x in range(1 << n)]


def sign(bit):
    return 1 if bit == 0 else -1


def compose(g, n, hs, m):
    out = []
    for u in range(1 << (n + m)):
        x = u & ((1 << n) - 1)
        z = u >> n
        gx = 0
        for i in range(n):
            value = sign((x >> i) & 1) * hs[i][z]
            if value == -1:
                gx |= 1 << i
        out.append(g[gx])
    return out


def product_table(hs, subset, m):
    return [prod(hs[i][z] for i in range(len(hs)) if (subset >> i) & 1) for z in range(1 << m)]


def prod(xs):
    ans = 1
    for x in xs:
        ans *= x
    return ans


def restrict(vals, n, fixed):
    """Restrict listed bit positions to 0/1; retain remaining bit order."""
    free = [i for i in range(n) if i not in fixed]
    out = []
    for y in range(1 << len(free)):
        x = 0
        for i, b in fixed.items():
            x |= b << i
        for j, i in enumerate(free):
            x |= ((y >> j) & 1) << i
        out.append(vals[x])
    return out


def audit_case(g, n, hs, m):
    global assertions, max_entropy_residual
    f = compose(g, n, hs, m)
    cg = coeffs(g)
    cf = coeffs(f)
    # Exact factorization \hat F(S,T)=\hat g(S)\widehat{h_S}(T).
    for S in range(1 << n):
        ch = coeffs(product_table(hs, S, m))
        for T in range(1 << m):
            assert cf[S | (T << n)] == cg[S] * ch[T]
            assertions += 1

    pg, pf = law(g), law(f)
    products = [law(product_table(hs, S, m)) for S in range(1 << n)]
    # Exact mass, entropy-chain input, and influence decomposition.
    predicted = [Fraction(0) for _ in pf]
    for S, mass in enumerate(pg):
        for T, q in enumerate(products[S]):
            predicted[S | (T << n)] = mass * q
    assert predicted == pf
    assertions += len(pf)

    ix = sum(pf[A] * (A & ((1 << n) - 1)).bit_count() for A in range(len(pf)))
    iz = sum(pf[A] * (A >> n).bit_count() for A in range(len(pf)))
    expected_iz = sum(pg[S] * influence_from_law(products[S]) for S in range(1 << n))
    assert ix == influence_from_law(pg)
    assert iz == expected_iz
    assertions += 2

    # Every physical Z-child is a sign-flipped copy of g and has the same
    # squared spectrum; hence M_Z=0 and terminal entropy is exactly H(g).
    for z in range(1 << m):
        child = [f[x | (z << n)] for x in range(1 << n)]
        assert law(child) == pg
        assertions += 1

    block_entropy = sum(float(pg[S]) * entropy(products[S]) for S in range(1 << n))
    residual = abs(entropy(pf) - entropy(pg) - block_entropy)
    max_entropy_residual = max(max_entropy_residual, residual)
    assert residual < 2e-12
    assertions += 1

    # Queried-influence telescope for the physical order z_0,...,z_{m-1}.
    telescope = Fraction(0)
    for j in range(m):
        for prefix in range(1 << j):
            fixed = {n + r: (prefix >> r) & 1 for r in range(j)}
            node = restrict(f, n + m, fixed)
            # In node coordinates z_j is position n.
            telescope += Fraction(1, 1 << j) * direct_influence(node, n)
    assert telescope == iz
    assertions += 1
    return f


assertions = 0
max_entropy_residual = 0.0
cases = 0

for n, m in [(1, 1), (2, 1), (2, 2)]:
    gs = list(all_boolean(n))
    hpool = list(all_boolean(m))
    # Full enumeration is 16*16^2=4096 at (2,2), still a bounded pilot.
    for g in gs:
        for hs in product(hpool, repeat=n):
            audit_case(g, n, hs, m)
            cases += 1

# Explicit two-level hierarchy audit: all one-bit base/modulator choices.
hierarchies = 0
for g0 in all_boolean(1):
    for h1 in all_boolean(1):
        g1 = compose(g0, 1, [h1], 1)
        for hs2 in product(list(all_boolean(1)), repeat=2):
            g2 = audit_case(g1, 2, hs2, 1)
            assert len(g2) == 8
            assertions += 1
            hierarchies += 1

# Coded plateau: character modulators on a two-bit block.  Every partial
# physical restriction has exactly the base squared spectrum.
plateau_checks = 0
chars = []
for mask in range(4):
    chars.append([prod(sign((z >> j) & 1) for j in range(2) if (mask >> j) & 1) for z in range(4)])
for g in all_boolean(2):
    for hs in product(chars, repeat=2):
        f = compose(g, 2, hs, 2)
        target = law(g)
        for fixed_count in range(3):
            for prefix in range(1 << fixed_count):
                fixed = {2 + r: (prefix >> r) & 1 for r in range(fixed_count)}
                node = restrict(f, 4, fixed)
                # Residual padding characters add zero entropy, so entropy
                # (not necessarily the literal law dimension) equals H(g).
                assert abs(entropy(law(node)) - entropy(target)) < 2e-12
                assertions += 1
                plateau_checks += 1

print("one_step_cases", cases)
print("two_level_hierarchies", hierarchies)
print("coded_plateau_nodes", plateau_checks)
print("assertions", assertions)
print("max_entropy_residual", f"{max_entropy_residual:.3e}")
print("PASS: exact block factorization, physical children, influence telescope, and hierarchy controls")
