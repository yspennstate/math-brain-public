#!/usr/bin/env python3
from fractions import Fraction


def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j+1:]
        for M in matchings(rest):
            yield ((a, b),) + M


def stats(degrees, low):
    half = tuple((v, h) for v, d in enumerate(degrees) for h in range(d))
    total = 0
    first = {}
    joint = {}
    for M in matchings(half):
        total += 1
        adj = {v: [] for v in range(len(degrees))}
        for ha, hb in M:
            a, b = ha[0], hb[0]
            adj[a].append(b)
            adj[b].append(a)
        seen = set()
        c = {}
        for v, d in enumerate(degrees):
            if d == 0 or v in seen:
                continue
            stack = [v]
            seen.add(v)
            V = []
            degsum = 0
            while stack:
                x = stack.pop()
                V.append(x)
                degsum += len(adj[x])
                for y in adj[x]:
                    if y not in seen:
                        seen.add(y)
                        stack.append(y)
            tree = (degsum // 2 == len(V) - 1)
            if tree and set(V).issubset(low):
                c[len(V)] = c.get(len(V), 0) + 1
        for k, x in c.items():
            first[k] = first.get(k, 0) + x
        for k in (2, 3):
            for l in (2, 3):
                x = c.get(k, 0) * c.get(l, 0)
                if k == l:
                    x -= c.get(k, 0)
                joint[(k, l)] = joint.get((k, l), 0) + x
    return (
        total,
        {k: Fraction(v, total) for k, v in first.items()},
        {kl: Fraction(v, total) for kl, v in joint.items()},
    )


def r(ell, ell_L, k):
    out = Fraction(1, 1)
    for j in range(k - 1):
        out *= Fraction(ell_L - (2 * j + 1), ell - (2 * j + 1))
    return out


d_full = [1, 1, 1, 1, 2, 2, 4]  # ell=12
d_core = d_full[:6]                 # ell_L=8
low = set(range(6))
Tf, Ef, Jf = stats(d_full, low)
Tc, Ec, Jc = stats(d_core, set(range(6)))
ell = sum(d_full)
ell_L = sum(d_core)

print("full_matchings", Tf)
print("core_matchings", Tc)
for k in (2, 3, 4):
    lhs = Ef.get(k, Fraction(0, 1))
    rhs = r(ell, ell_L, k) * Ec.get(k, Fraction(0, 1))
    print("first", k, lhs, rhs, "PASS" if lhs == rhs else "FAIL")
    assert lhs == rhs
for k in (2, 3):
    for l in (2, 3):
        lhs = Jf[(k, l)]
        rhs = r(ell, ell_L, k + l - 1) * Jc[(k, l)]
        print("joint", k, l, lhs, rhs, "PASS" if lhs == rhs else "FAIL")
        assert lhs == rhs
print("ALL_EXACT_CHECKS_PASS")
