#!/usr/bin/env python3
"""HARD10-01 exact checks for the 2026-09-15T22:27:05Z checkpoint.

Standard library only. These finite computations are adversarial checks, not
proof premises.

Checks:
  1. exact |R|=7 root-fiber partitions for representative adjacent/disjoint
     distinguished pairs on n=6,7;
  2. every observed (4,3) instance has the ear/star structure of L65 and
     suppressing the size-three ear gives exactly |R|=5 with partition (4,1);
  3. every observed (3,3,1) instance satisfies the common-ear/cross-ear
     dichotomy of L66 and the corresponding compression claim;
  4. exact unit Rayleigh-gap distributions quoted in the checkpoint.
"""

from collections import Counter
from itertools import combinations


def norm(e):
    return tuple(sorted(e))


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        if rank[ru] < rank[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        if rank[ru] == rank[rv]:
            rank[ru] += 1
    return True


def zeta(a, m):
    z = a[:]
    for i in range(m):
        bit = 1 << i
        for mask in range(1 << m):
            if mask & bit:
                z[mask] += z[mask ^ bit]
    return z


def fixed_arrays(n, e, f):
    """Precompute R indicators/roots and forest-state counts on the complete H."""
    e, f = norm(e), norm(f)
    H = [g for g in combinations(range(n), 2) if g not in (e, f)]
    m = len(H)
    N = 1 << m

    r = [0] * N
    root = [0] * N
    forest = [0] * N
    eadd = [0] * N
    fadd = [0] * N
    bothadd = [0] * N

    for mask in range(N):
        A = [H[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        forest[mask] = 1
        eo = is_forest(n, A + [e])
        fo = is_forest(n, A + [f])
        efo = is_forest(n, A + [e, f])
        eadd[mask] = int(eo)
        fadd[mask] = int(fo)
        bothadd[mask] = int(efo)
        if eo and fo and not efo:
            r[mask] = 1

    for mask in range(N):
        if not r[mask]:
            continue
        x = mask
        minimal = True
        while x:
            bit = x & -x
            if r[mask ^ bit]:
                minimal = False
                break
            x -= bit
        if minimal:
            root[mask] = 1

    return {
        "n": n,
        "e": e,
        "f": f,
        "H": H,
        "index": {g: i for i, g in enumerate(H)},
        "r": r,
        "root": root,
        "Rcount": zeta(r, m),
        "F00": zeta(forest, m),
        "F10": zeta(eadd, m),
        "F01": zeta(fadd, m),
        "F11": zeta(bothadd, m),
    }


def edge_set(H, mask):
    return {H[i] for i in range(len(H)) if (mask >> i) & 1}


def submasks_from_indicator(indicator, host):
    out = []
    s = host
    while True:
        if indicator[s]:
            out.append(s)
        if s == 0:
            break
        s = (s - 1) & host
    return out


def instance(data, host):
    Rs = submasks_from_indicator(data["r"], host)
    roots = submasks_from_indicator(data["root"], host)
    fibers = {P: [A for A in Rs if (P & ~A) == 0] for P in roots}
    part = tuple(sorted((len(v) for v in fibers.values()), reverse=True))
    return Rs, roots, fibers, part


def extension_edges(data, P, fiber):
    H = data["H"]
    out = []
    for A in fiber:
        if A == P:
            continue
        d = A ^ P
        assert d.bit_count() == 1
        out.append(H[(d & -d).bit_length() - 1])
    return out


def cycle_support(data, P):
    out = set()
    for g in edge_set(data["H"], P) | {data["e"], data["f"]}:
        out.update(g)
    return out


def ear_from_size3(data, P, fiber):
    ext = extension_edges(data, P, fiber)
    assert len(ext) == 2
    support = cycle_support(data, P)
    common = set(ext[0]) & set(ext[1])
    outside_common = common - support
    assert len(outside_common) == 1
    w = next(iter(outside_common))
    u = next(x for x in ext[0] if x != w)
    v = next(x for x in ext[1] if x != w)
    assert u in support and v in support and u != v
    return frozenset(ext), w, norm((u, v))


def star_from_size4(data, P, fiber):
    ext = extension_edges(data, P, fiber)
    assert len(ext) == 3
    support = cycle_support(data, P)
    common = set(ext[0]) & set(ext[1]) & set(ext[2])
    outside_common = common - support
    assert len(outside_common) == 1
    w = next(iter(outside_common))
    attachments = []
    for g in ext:
        x = next(v for v in g if v != w)
        assert x in support
        attachments.append(x)
    assert len(set(attachments)) == 3
    return frozenset(ext), w, tuple(sorted(attachments))


def has_edge(mask, data, g):
    i = data["index"][norm(g)]
    return bool(mask & (1 << i))


def remove_edges_add_edges(mask, data, remove, add):
    out = mask
    for g in remove:
        out &= ~(1 << data["index"][norm(g)])
    for g in add:
        out |= 1 << data["index"][norm(g)]
    return out


def delta(data, host):
    A = data["F00"][host]
    B = data["F10"][host]
    C = data["F01"][host]
    D = data["F11"][host]
    return B * C - A * D


def partition_counts(data, target):
    out = Counter()
    for host, value in enumerate(data["Rcount"]):
        if value != target:
            continue
        _, _, _, part = instance(data, host)
        out[part] += 1
    return out


def check_43(data):
    checked = 0
    gaps = Counter()
    for host, value in enumerate(data["Rcount"]):
        if value != 7:
            continue
        Rs, roots, fibers, part = instance(data, host)
        if part != (4, 3):
            continue
        checked += 1

        P3 = next(P for P in roots if len(fibers[P]) == 3)
        Q4 = next(P for P in roots if len(fibers[P]) == 4)
        ear, w, direct = ear_from_size3(data, P3, fibers[P3])
        star, sw, attachments = star_from_size4(data, Q4, fibers[Q4])

        Qset = edge_set(data["H"], Q4)
        assert set(ear) <= Qset

        Pset = edge_set(data["H"], P3)
        assert sum(g in Pset for g in star) == 2

        assert not has_edge(host, data, direct)

        compressed = remove_edges_add_edges(host, data, ear, [direct])
        assert data["Rcount"][compressed] == 5
        _, _, _, cpart = instance(data, compressed)
        assert cpart == (4, 1)

        gaps[delta(data, host)] += 1

    return checked, gaps


def check_331(data):
    checked = 0
    common_ear = 0
    cross_ear = 0
    gaps = Counter()

    for host, value in enumerate(data["Rcount"]):
        if value != 7:
            continue
        Rs, roots, fibers, part = instance(data, host)
        if part != (3, 3, 1):
            continue
        checked += 1

        big = [P for P in roots if len(fibers[P]) == 3]
        single = next(P for P in roots if len(fibers[P]) == 1)
        P, Q = big
        EP, wp, gp = ear_from_size3(data, P, fibers[P])
        EQ, wq, gq = ear_from_size3(data, Q, fibers[Q])
        Pset = edge_set(data["H"], P)
        Qset = edge_set(data["H"], Q)
        Sset = edge_set(data["H"], single)

        q_use = sum(g in Qset for g in EP)
        p_use = sum(g in Pset for g in EQ)
        assert q_use in (0, 2)
        assert p_use in (0, 2)

        if q_use == 0:
            common_ear += 1
            assert EP == EQ
            assert set(EP) <= Sset
            assert has_edge(host, data, gp)
            reduced = remove_edges_add_edges(host, data, EP, [])
            assert data["Rcount"][reduced] == 2
        else:
            cross_ear += 1
            assert p_use == 2
            assert set(EP) <= Sset and set(EQ) <= Sset
            assert not has_edge(host, data, gp)
            assert not has_edge(host, data, gq)
            reduced = remove_edges_add_edges(host, data, set(EP) | set(EQ), [gp, gq])
            assert data["Rcount"][reduced] == 3
            _, roots2, fibers2, part2 = instance(data, reduced)
            assert part2 == (1, 1, 1)
            assert len(roots2) == 3

        gaps[delta(data, host)] += 1

    return checked, common_ear, cross_ear, gaps


def main():
    cases = [
        ("n6-adj", fixed_arrays(6, (0, 1), (0, 2))),
        ("n6-dis", fixed_arrays(6, (0, 1), (2, 3))),
        ("n7-adj", fixed_arrays(7, (0, 1), (0, 2))),
        ("n7-dis", fixed_arrays(7, (0, 1), (2, 3))),
    ]

    expected_parts = {
        "n6-adj": Counter({(7,): 82, (4, 3): 30}),
        "n6-dis": Counter({(7,): 64, (3, 3, 1): 72, (5, 1, 1): 36, (4, 3): 32}),
        "n7-adj": Counter({(7,): 918, (4, 3): 396}),
        "n7-dis": Counter({(7,): 1542, (3, 3, 1): 1260, (4, 3): 864, (5, 1, 1): 630}),
    }
    expected_43 = {
        "n6-adj": (30, Counter({248: 24, 124: 6})),
        "n6-dis": (32, Counter({248: 32})),
        "n7-adj": (396, Counter({496: 288, 248: 96, 124: 12})),
        "n7-dis": (864, Counter({496: 768, 248: 96})),
    }
    expected_331 = {
        "n6-adj": (0, 0, 0, Counter()),
        "n6-dis": (72, 72, 0, Counter({136: 64, 68: 8})),
        "n7-adj": (0, 0, 0, Counter()),
        "n7-dis": (1260, 1260, 0, Counter({272: 1056, 136: 192, 68: 12})),
    }

    total_43 = total_331 = 0
    for name, data in cases:
        parts = partition_counts(data, 7)
        assert parts == expected_parts[name], (name, parts)
        print(name, "R=7 partitions:", dict(parts))

        got43 = check_43(data)
        assert got43 == expected_43[name], (name, "4+3", got43)
        total_43 += got43[0]
        print(name, "4+3:", got43)

        got331 = check_331(data)
        assert got331 == expected_331[name], (name, "3+3+1", got331)
        total_331 += got331[0]
        print(name, "3+3+1:", got331)

    assert total_43 == 1322
    assert total_331 == 1332
    print("ALL CHECKS PASSED")
    print("total 4+3 instances:", total_43)
    print("total 3+3+1 instances:", total_331)


if __name__ == "__main__":
    main()
