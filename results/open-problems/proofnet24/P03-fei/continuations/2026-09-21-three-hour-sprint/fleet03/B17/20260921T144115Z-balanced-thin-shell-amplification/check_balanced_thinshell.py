from fractions import Fraction
from collections import defaultdict
from math import log2


def walsh_law(vals, n):
    N = 1 << n
    assert len(vals) == N and all(v in (-1, 1) for v in vals)
    p = {}
    for s in range(N):
        A = sum(vals[x] * (-1 if ((s & x).bit_count() & 1) else 1)
                for x in range(N))
        if A:
            p[s] = Fraction(A * A, N * N)
    assert sum(p.values()) == 1
    return p


def entropy_bits(p):
    return sum(float(q) * (-log2(float(q))) for q in p.values())


def size_moments(p):
    e1 = sum(q * s.bit_count() for s, q in p.items())
    e2 = sum(q * (s.bit_count() ** 2) for s, q in p.items())
    return e1, e2 - e1 * e1


def level_entropy(p):
    lev = defaultdict(Fraction)
    for s, q in p.items():
        lev[s.bit_count()] += q
    return entropy_bits(lev)


def amplify_with_balancing_bit(vals, n, m):
    N = 1 << (1 + m * n)
    out = []
    for x in range(N):
        z = -1 if (x & 1) else 1
        y = z
        for j in range(m):
            block = (x >> (1 + j * n)) & ((1 << n) - 1)
            y *= vals[block]
        out.append(y)
    return out, 1 + m * n


def product_without_balancing_bit(vals, n, m):
    N = 1 << (m * n)
    out = []
    for x in range(N):
        y = 1
        for j in range(m):
            block = (x >> (j * n)) & ((1 << n) - 1)
            y *= vals[block]
        out.append(y)
    return out, m * n


def expected_amplified_law(p, n, m, balancing_bit=True):
    out = {1 if balancing_bit else 0: Fraction(1)}
    offset0 = 1 if balancing_bit else 0
    for j in range(m):
        nxt = {}
        for mask, q in out.items():
            for s, r in p.items():
                smask = mask | (s << (offset0 + j * n))
                nxt[smask] = nxt.get(smask, Fraction()) + q * r
        out = nxt
    return out


def show(name, vals, n):
    p = walsh_law(vals, n)
    H = entropy_bits(p)
    I, var = size_moments(p)
    print(name, "base", "H=", H, "I=", I, "VarK=", var,
          "pmax=", max(p.values()))

    amp_vals, N = amplify_with_balancing_bit(vals, n, 2)
    pa = walsh_law(amp_vals, N)
    expected = expected_amplified_law(p, n, 2, True)
    Ia, vara = size_moments(pa)
    assert pa == expected
    assert Ia == 1 + 2 * I
    assert vara == 2 * var
    assert max(pa.values()) == max(p.values()) ** 2
    print(name, "balanced_m2", "law_exact=PASS", "H=", entropy_bits(pa),
          "I=", Ia, "VarK=", vara, "pmax=", max(pa.values()),
          "Hlevel=", level_entropy(pa))

    if sum(vals) == 0:
        prod_vals, Np = product_without_balancing_bit(vals, n, 2)
        pp = walsh_law(prod_vals, Np)
        expectedp = expected_amplified_law(p, n, 2, False)
        Ip, varp = size_moments(pp)
        assert pp == expectedp
        assert Ip == 2 * I
        assert varp == 2 * var
        assert max(pp.values()) == max(p.values()) ** 2
        print(name, "already_balanced_m2", "law_exact=PASS", "H=", entropy_bits(pp),
              "I=", Ip, "VarK=", varp, "pmax=", max(pp.values()),
              "Hlevel=", level_entropy(pp))


# Exact admissible Boolean stress cases.
onepoint2 = [-1, 1, 1, 1]
majority3 = [1 if x.bit_count() <= 1 else -1 for x in range(8)]
character3 = [1 if ((x & 3).bit_count() % 2 == 0) else -1 for x in range(8)]
constant2 = [1] * 4

show("onepoint2", onepoint2, 2)
show("majority3", majority3, 3)
show("character3", character3, 3)

pc = walsh_law(constant2, 2)
Ic, varc = size_moments(pc)
assert entropy_bits(pc) == 0.0 and Ic == 0 and varc == 0
print("constant2 boundary", "H=0 I=0 VarK=0 pmax=1", "FEI_trivial=PASS")
