#!/usr/bin/env python3
from itertools import combinations
from collections import Counter


def norm(e):
    return tuple(sorted(e))


def comps(n, edges, mask):
    p = list(range(n))
    r = [0] * n

    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for i, (a, b) in enumerate(edges):
        if not ((mask >> i) & 1):
            continue
        a, b = f(a), f(b)
        if a == b:
            return None
        if r[a] < r[b]:
            a, b = b, a
        p[b] = a
        if r[a] == r[b]:
            r[a] += 1
    return [f(i) for i in range(n)]


def fixed_R(n, e, f):
    e, f = norm(e), norm(f)
    H = [g for g in combinations(range(n), 2) if g not in (e, f)]
    N = 1 << len(H)
    R = bytearray(N)
    root = bytearray(N)
    a, b = e
    c, d = f

    for m in range(N):
        C = comps(n, H, m)
        if C is None:
            continue
        ra, rb, rc, rd = C[a], C[b], C[c], C[d]
        if ra != rb and rc != rd and {ra, rb} == {rc, rd}:
            R[m] = 1

    for m in range(N):
        if not R[m]:
            continue
        x = m
        while x:
            bit = x & -x
            if R[m ^ bit]:
                break
            x -= bit
        else:
            root[m] = 1

    cnt = list(R)
    for i in range(len(H)):
        bit = 1 << i
        for m in range(N):
            if m & bit:
                cnt[m] += cnt[m ^ bit]
    return H, R, root, cnt


def contained_partition(M, rlist, roots):
    rs = [a for a in rlist if not (a & ~M)]
    ro = [p for p in roots if not (p & ~M)]
    fs = tuple(sorted(
        (sum(1 for a in rs if not (p & ~a)) for p in ro), reverse=True
    ))
    return fs, rs, ro


def bit_edge(H, b):
    return H[b.bit_length() - 1]


def edges_of(H, m):
    return {H[i] for i in range(len(H)) if (m >> i) & 1}


def star_info(H, P, F):
    atoms = []
    for A in F:
        d = A ^ P
        if d and not (d & (d - 1)):
            atoms.append(d)
    if len(F) != 4 or len(atoms) != 3:
        return None
    E = [bit_edge(H, b) for b in atoms]
    common = set(E[0]) & set(E[1]) & set(E[2])
    if len(common) != 1:
        return None
    w = next(iter(common))
    at = []
    for a, b in E:
        at.append(b if a == w else a)
    return w, tuple(sorted(at))


def r10_counts_and_4411(n, e, f):
    H, R, root, cnt = fixed_R(n, e, f)
    rlist = [m for m, x in enumerate(R) if x]
    roots = [m for m, x in enumerate(root) if x]
    parts = Counter()
    regimes = Counter()

    for M, v in enumerate(cnt):
        if v != 10:
            continue
        part, rs, ro = contained_partition(M, rlist, roots)
        parts[part] += 1
        if part != (4, 4, 1, 1):
            continue

        fib = {p: [A for A in rs if not (p & ~A)] for p in ro}
        L = [p for p in ro if len(fib[p]) == 4]
        S = [p for p in ro if len(fib[p]) == 1]
        infos = [star_info(H, p, fib[p]) for p in L]
        if not all(infos):
            regimes[("nonstar",)] += 1
            continue

        (w, A), (x, B) = infos
        if w == x:
            pairs = []
            for s in S:
                cyc = edges_of(H, s) | {norm(e), norm(f)}
                pairs.append(tuple(sorted(
                    a for a in A if norm((w, a)) in cyc
                )))
            regimes[(
                "same-center",
                "same-pair" if pairs[0] == pairs[1] else "distinct-pairs",
            )] += 1
        else:
            P, Q = L
            CP = edges_of(H, P) | {norm(e), norm(f)}
            CQ = edges_of(H, Q) | {norm(e), norm(f)}
            tA = {a for a in A if norm((w, a)) in CQ}
            tB = {b for b in B if norm((x, b)) in CP}
            connector = norm((w, x)) in edges_of(H, M)
            regimes[(
                "distinct-centers",
                "connector" if connector else "no-connector",
                len(tA & tB),
                len(tA),
                len(tB),
            )] += 1

    return parts, regimes


def main():
    cases = [
        ("n6_adj", 6, (0, 1), (0, 2)),
        ("n6_dis", 6, (0, 1), (2, 3)),
        ("n7_adj", 7, (0, 1), (0, 2)),
        ("n7_dis", 7, (0, 1), (2, 3)),
    ]
    out = {}
    for name, n, e, f in cases:
        parts, reg = r10_counts_and_4411(n, e, f)
        out[name] = (parts, reg)
        print(name, dict(parts))
        assert parts.get((5, 4, 1), 0) == 0
        if reg:
            print("  4411 regimes", dict(reg))

    assert out["n7_dis"][0] == Counter({
        (8, 2): 5136,
        (4, 4, 1, 1): 2640,
        (10,): 1968,
        (4, 3, 3): 432,
        (7, 3): 120,
        (9, 1): 108,
    })
    assert out["n7_dis"][1] == Counter({
        ("same-center", "distinct-pairs"): 1260,
        ("same-center", "same-pair"): 624,
        ("distinct-centers", "connector", 2, 2, 2): 324,
        ("distinct-centers", "no-connector", 1, 2, 2): 216,
        ("distinct-centers", "connector", 1, 2, 2): 216,
    })

    print("No 5+4+1 examples through n=7 for representative adjacent/disjoint pairs.")
    print("OK")


if __name__ == "__main__":
    main()
