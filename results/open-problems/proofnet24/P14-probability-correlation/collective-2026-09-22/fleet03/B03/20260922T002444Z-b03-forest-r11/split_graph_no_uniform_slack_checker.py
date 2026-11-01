#!/usr/bin/env python3
"""Exact checker for FOREST split-graph no-uniform-slack report.

For S_{r,m}=K_r join independent_m, marks
    e={0,1}, f={s_1,2}, g={s_1,0},
this script:
  * counts all joint forest events exactly by terminal-partition DP,
  * interpolates the normalized counts as exact polynomials in n=m-1,
  * verifies the deletion/contraction identity,
  * verifies the analytic leading coefficients from the report, and
  * verifies lim R=(r^2+r+2)/((r+1)(r+2))
for r=3,...,7.

Only Python standard library is used.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import factorial


def canon(labels):
    mp = {}
    out = []
    nxt = 0
    for x in labels:
        if x not in mp:
            mp[x] = nxt
            nxt += 1
        out.append(mp[x])
    return tuple(out)


def add_edge(part, u, v):
    if part[u] == part[v]:
        return None
    a, b = part[u], part[v]
    return canon(tuple(a if x == b else x for x in part))


def add_star(part, verts):
    comps = [part[v] for v in verts]
    if len(set(comps)) != len(comps):
        return None
    if len(verts) <= 1:
        return part
    merged = set(comps)
    target = comps[0]
    return canon(tuple(target if x in merged else x for x in part))


def joint_counts(r, m):
    """Return Z_S for S subset of mark bits e=1,f=2,g=4."""
    assert r >= 3 and m >= 1
    initial = tuple(range(r))
    states = {(initial, 0): 1}

    # Clique K_r. e={0,1} is the marked clique edge.
    for u, v in combinations(range(r), 2):
        bit = 1 if (u, v) == (0, 1) else 0
        nxt = defaultdict(int)
        for (part, mask), count in states.items():
            nxt[(part, mask)] += count
            part2 = add_edge(part, u, v)
            if part2 is not None:
                nxt[(part2, mask | bit)] += count
        states = nxt

    # Special star center s_1; f=s_1--2, g=s_1--0.
    nxt = defaultdict(int)
    for (part, mask), count in states.items():
        for size in range(r + 1):
            for verts in combinations(range(r), size):
                part2 = add_star(part, verts)
                if part2 is None:
                    continue
                mask2 = mask
                if 2 in verts:
                    mask2 |= 2
                if 0 in verts:
                    mask2 |= 4
                nxt[(part2, mask2)] += count
    states = nxt

    # Remaining m-1 unmarked star centers.
    for _ in range(m - 1):
        nxt = defaultdict(int)
        for (part, mask), count in states.items():
            for size in range(r + 1):
                for verts in combinations(range(r), size):
                    part2 = add_star(part, verts)
                    if part2 is not None:
                        nxt[(part2, mask)] += count
        states = nxt

    exact = [0] * 8
    for (_part, mask), count in states.items():
        exact[mask] += count

    z = []
    for required in range(8):
        z.append(
            sum(
                exact[mask]
                for mask in range(8)
                if (mask & required) == required
            )
        )
    return tuple(z)


# Polynomial helpers, low coefficient first.

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a, b, sign=1):
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += sign * value
    return trim(out)


def pmul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pscale(a, scalar):
    return trim([scalar * value for value in a])


def peval(a, x):
    out = Fraction(0)
    power = Fraction(1)
    for value in a:
        out += value * power
        power *= x
    return out


def binomial_poly(k):
    out = [Fraction(1)]
    for j in range(k):
        out = pmul(out, [Fraction(-j), Fraction(1)])
    return pscale(out, Fraction(1, factorial(k)))


def interpolate_consecutive(values):
    """Exact polynomial p with p(0),...,p(d) equal to values."""
    diffs = [Fraction(v) for v in values]
    out = [Fraction(0)]
    for k in range(len(values)):
        out = padd(out, pscale(binomial_poly(k), diffs[0]))
        diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        if not diffs:
            break
    return trim(out)


def quantity_polynomials(z):
    Z, Ze, Zf, Zef, Zg, Zeg, Zfg, Zefg = z

    A = padd(Z, Zg, -1)
    B = Zg
    Ae = padd(Ze, Zeg, -1)
    Be = Zeg
    Af = padd(Zf, Zfg, -1)
    Bf = Zfg
    Aef = padd(Zef, Zefg, -1)
    Bef = Zefg

    D0 = padd(pmul(Ae, Af), pmul(A, Aef), -1)
    D1 = padd(pmul(Be, Bf), pmul(B, Bef), -1)

    Delta_ge = padd(pmul(Zg, Ze), pmul(Z, Zeg), -1)
    Delta_gf = padd(pmul(Zg, Zf), pmul(Z, Zfg), -1)
    Delta_ef = padd(pmul(Ze, Zf), pmul(Z, Zef), -1)

    denominator = pmul(Z, padd(pmul(B, D0), pmul(A, D1)))
    numerator = pmul(Delta_ge, Delta_gf)

    # Identity: denominator - numerator = A B Delta_ef.
    identity_residual = padd(
        padd(denominator, numerator, -1),
        pmul(pmul(A, B), Delta_ef),
        -1,
    )

    return {
        "Z": Z,
        "A": A,
        "B": B,
        "D0": D0,
        "D1": D1,
        "Delta_ge": Delta_ge,
        "Delta_gf": Delta_gf,
        "Delta_ef": Delta_ef,
        "denominator": denominator,
        "numerator": numerator,
        "identity_residual": identity_residual,
    }


def main():
    print("FOREST split-graph exact polynomial check")
    print("marks: e={0,1}, f={s1,2}, g={s1,0}")
    for r in range(3, 8):
        q = r + 1

        # Every normalized joint count has degree at most r-1 in n=m-1,
        # so r exact samples n=0,...,r-1 suffice.
        samples = [[] for _ in range(8)]
        for n in range(r):
            z = joint_counts(r, n + 1)
            for required in range(8):
                samples[required].append(Fraction(z[required], q ** n))

        zpoly = [interpolate_consecutive(values) for values in samples]
        Q = quantity_polynomials(zpoly)

        assert Q["identity_residual"] == [Fraction(0)]

        c = Fraction(r, q) ** (r - 2)
        expected = {
            "D0": 2 * c * c / (r * r),
            "D1": c * c / (r * r),
            "Delta_ge": c * c * Fraction(r * r + r + 2, r * r),
            "Delta_gf": c * c / (q * q),
            "Delta_ef": 2 * c * c / (r * r),
        }

        for name, target in expected.items():
            actual = Q[name][-1]
            assert actual == target, (r, name, actual, target)

        limit = Q["numerator"][-1] / Q["denominator"][-1]
        expected_limit = Fraction(r * r + r + 2, (r + 1) * (r + 2))
        assert limit == expected_limit, (r, limit, expected_limit)

        # Exact polynomial evaluation far out in the family, no re-enumeration.
        n = 99  # m=100
        num = peval(Q["numerator"], n)
        den = peval(Q["denominator"], n)
        assert den > 0
        rho_100 = num / den

        print(
            f"r={r} "
            f"limit={limit} "
            f"one_minus_limit={1-limit} "
            f"R_m100={float(rho_100):.12f}"
        )

    print("ALL_EXACT_SPLIT_GRAPH_CHECKS_PASSED")


if __name__ == "__main__":
    main()
