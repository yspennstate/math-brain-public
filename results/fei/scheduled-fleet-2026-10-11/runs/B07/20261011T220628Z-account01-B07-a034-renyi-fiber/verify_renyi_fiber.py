#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def walsh(values):
    a = [Fraction(v) for v in values]
    n = len(a)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return [v / n for v in a]


def fiber_data(coeffs, nx, ny):
    out = []
    for r in range(1 << nx):
        col = [coeffs[r | (t << nx)] for t in range(1 << ny)]
        mass = sum(c * c for c in col)
        if not mass:
            continue
        l1 = sum(abs(c) for c in col)
        support = sum(c != 0 for c in col)
        khalf = l1 * l1 / mass
        out.append((r, mass, khalf, support))
    return out


assertions = 0
positive_fibers = 0
for bits in product((-1, 1), repeat=8):
    coeffs = walsh(bits)
    fibers = fiber_data(coeffs, 2, 1)
    assert sum(m for _, m, _, _ in fibers) == 1
    assertions += 1
    for _, mass, khalf, support in fibers:
        assert mass > 0
        assert Fraction(1) <= khalf <= support
        assertions += 3
        positive_fibers += 1

# Exact tensor multiplicativity for all small rational coefficient vectors.
vectors = [
    [Fraction(1)],
    [Fraction(1, 2), Fraction(1, 2)],
    [Fraction(3, 4), Fraction(1, 4)],
    [Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)],
]
tensor_checks = 0
for a in vectors:
    for b in vectors:
        ma = sum(x*x for x in a); mb = sum(x*x for x in b)
        ka = sum(abs(x) for x in a)**2 / ma
        kb = sum(abs(x) for x in b)**2 / mb
        c = [x*y for x in a for y in b]
        mc = sum(x*x for x in c)
        kc = sum(abs(x) for x in c)**2 / mc
        assert mc == ma*mb
        assert kc == ka*kb
        assertions += 2
        tensor_checks += 1

# Genuine Boolean AND signs: support grows as 2^k but K_{1/2}<9.
and_rows = []
for k in range(1, 11):
    vals = [(-1 if x == (1 << k)-1 else 1) for x in range(1 << k)]
    coeffs = walsh(vals)
    support = sum(c != 0 for c in coeffs)
    l1 = sum(abs(c) for c in coeffs)
    expected = Fraction(3) - Fraction(4, 1 << k)
    assert support == (1 if k == 1 else (1 << k))
    assert l1 == expected
    assert l1*l1 < 9
    assertions += 3
    and_rows.append((k, support, str(l1), str(l1*l1)))

print('PASS')
print('exhaustive_boolean_functions=256')
print(f'positive_fibers={positive_fibers}')
print(f'tensor_pairs={tensor_checks}')
print(f'and_family_rows={len(and_rows)}')
print(f'exact_assertions={assertions}')
for k,s,l1,kh in and_rows:
    print(f'and_k={k} support={s} l1={l1} Khalf={kh}')
print('arithmetic=exact Fraction')
print('random_seed=None')

