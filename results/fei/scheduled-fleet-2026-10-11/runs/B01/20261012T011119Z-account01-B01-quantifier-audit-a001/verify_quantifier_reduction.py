#!/usr/bin/env python3
"""Finite audit of the A001 critical-prime reduction (not a proof)."""

from fractions import Fraction
from itertools import product
from math import log2


def spectrum(table, n):
    out = []
    for mask in range(1 << n):
        total = 0
        for x, fx in enumerate(table):
            parity = (x & mask).bit_count() & 1
            total += fx * (-1 if parity else 1)
        out.append(Fraction(total, 1 << n))
    return out


def hi(table, n):
    coeff = spectrum(table, n)
    mass = [c * c for c in coeff]
    influence = sum((m * mask.bit_count() for mask, m in enumerate(mass)), Fraction())
    entropy = sum(float(m) * log2(1.0 / float(m)) for m in mass if m)
    return entropy, influence, mass


def restrict(table, n, i, bit):
    out = []
    for y in range(1 << (n - 1)):
        low = y & ((1 << i) - 1)
        high = y >> i
        x = low | (bit << i) | (high << (i + 1))
        out.append(table[x])
    return tuple(out)


def ratio(table, n):
    h, i, _ = hi(table, n)
    return None if i == 0 else h / float(i)


def relevant(table, n, i):
    return restrict(table, n, i, 0) != restrict(table, n, i, 1)


def factor(table, n):
    """Return two nonconstant disjoint factors, if a proper split exists."""
    full = (1 << n) - 1
    for amask in range(1, full):
        bmask = full ^ amask
        if amask > bmask:
            continue
        apos = [i for i in range(n) if (amask >> i) & 1]
        bpos = [i for i in range(n) if (bmask >> i) & 1]
        na, nb = len(apos), len(bpos)
        u = []
        for a in range(1 << na):
            x = sum(((a >> k) & 1) << p for k, p in enumerate(apos))
            u.append(table[x])
        base = u[0]
        v = []
        for b in range(1 << nb):
            x = sum(((b >> k) & 1) << p for k, p in enumerate(bpos))
            v.append(table[x] * base)
        ok = True
        for a in range(1 << na):
            for b in range(1 << nb):
                x = sum(((a >> k) & 1) << p for k, p in enumerate(apos))
                x |= sum(((b >> k) & 1) << p for k, p in enumerate(bpos))
                if table[x] != u[a] * v[b]:
                    ok = False
        if ok and len(set(u)) > 1 and len(set(v)) > 1:
            return (tuple(u), na), (tuple(v), nb)
    return None


def critical_prime_descendant(table, n):
    start = ratio(table, n)
    steps = 0
    while True:
        r = ratio(table, n)
        moved = False
        for i in range(n):
            if not relevant(table, n, i):
                continue
            h, inf, mass = hi(table, n)
            ii = sum((m for mask, m in enumerate(mass) if (mask >> i) & 1), Fraction())
            children = [restrict(table, n, i, b) for b in (0, 1)]
            hbar = sum(hi(c, n - 1)[0] for c in children) / 2
            step = (h - hbar) / float(ii)
            if step + 1e-12 < r:
                candidates = [(ratio(c, n - 1), c) for c in children]
                candidates = [(q, c) for q, c in candidates if q is not None]
                q, table = max(candidates, key=lambda z: z[0])
                assert q > r - 1e-11
                n -= 1
                steps += 1
                moved = True
                break
        if moved:
            continue
        fac = factor(table, n)
        if fac:
            candidates = [(ratio(t, m), t, m) for t, m in fac]
            q, table, n = max(candidates, key=lambda z: z[0])
            assert q >= r - 1e-11
            steps += 1
            continue
        assert ratio(table, n) >= start - 1e-10
        return steps


def main():
    truth_tables = 0
    restriction_identities = 0
    descent_runs = 0
    descent_steps = 0
    max_identity_error = 0.0
    for n in range(1, 4):
        for values in product((-1, 1), repeat=1 << n):
            if len(set(values)) == 1:
                continue
            table = tuple(values)
            truth_tables += 1
            h, inf, mass = hi(table, n)
            r = h / float(inf)
            for i in range(n):
                ii = sum((m for mask, m in enumerate(mass) if (mask >> i) & 1), Fraction())
                if ii == 0:
                    continue
                children = [restrict(table, n, i, b) for b in (0, 1)]
                child_hi = [hi(c, n - 1)[:2] for c in children]
                hbar = sum(x[0] for x in child_hi) / 2
                ibar = sum(float(x[1]) for x in child_hi) / 2
                lhs = hbar - r * ibar
                rhs = r * float(ii) - (h - hbar)
                max_identity_error = max(max_identity_error, abs(lhs - rhs))
                assert abs(lhs - rhs) < 2e-12
                if rhs > 1e-12:
                    child_ratios = [ratio(c, n - 1) for c in children]
                    assert any(q is not None and q > r for q in child_ratios)
                restriction_identities += 1
            descent_steps += critical_prime_descendant(table, n)
            descent_runs += 1

    tensor_pairs = 0
    max_tensor_error = 0.0
    nonconstant = []
    for n in (1, 2):
        for values in product((-1, 1), repeat=1 << n):
            if len(set(values)) > 1:
                nonconstant.append((tuple(values), n))
    for (f, nf), (g, ng) in product(nonconstant, repeat=2):
        fg = tuple(f[x] * g[y] for y in range(1 << ng) for x in range(1 << nf))
        hf, inf, _ = hi(f, nf)
        hg, ing, _ = hi(g, ng)
        hp, inp, _ = hi(fg, nf + ng)
        max_tensor_error = max(max_tensor_error, abs(hp - hf - hg), abs(float(inp - inf - ing)))
        assert abs(hp - hf - hg) < 2e-12
        assert inp == inf + ing
        assert hp / float(inp) <= max(hf / float(inf), hg / float(ing)) + 1e-12
        tensor_pairs += 1

    print("A001 finite quantifier-reduction audit: PASS")
    print(f"nonconstant truth tables n<=3: {truth_tables}")
    print(f"relevant-coordinate restriction identities: {restriction_identities}")
    print(f"critical-prime descents: {descent_runs}; dimension-lowering steps: {descent_steps}")
    print(f"nonconstant tensor pairs (factor dimensions <=2): {tensor_pairs}")
    print(f"max restriction identity error: {max_identity_error:.3e}")
    print(f"max tensor identity error: {max_tensor_error:.3e}")


if __name__ == "__main__":
    main()
