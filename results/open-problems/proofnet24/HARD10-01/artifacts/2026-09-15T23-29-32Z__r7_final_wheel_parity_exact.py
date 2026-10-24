#!/usr/bin/env python3
"""HARD10-01 exact checks for the 2026-09-15T23:29:32Z checkpoint.

Standard library only.  These are finite adversarial checks, NOT proof
premises.  The script verifies:
  * the bare opposite-rim W4 coefficient (49,33,33,19), gap 158;
  * all observed |R|=7, partition (5,1,1) instances through n=7 have
    the four-spoke/disjoint-pair/decorated-W4 structure;
  * Delta = 158*alpha_X*alpha_Y exactly for every such instance;
  * the all-minimal |R|=4 edge-incidence parity 0/2/4 through n=7;
  * no (6,1) or (4,1,1,1) |R|=7 partition occurs in the same census.

Representative adjacent/disjoint edge pairs suffice by vertex relabeling.
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


def connected(edges, s, t):
    if s == t:
        return True
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    stack = [s]
    seen = {s}
    while stack:
        u = stack.pop()
        for v in adj.get(u, ()):
            if v == t:
                return True
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return False


def zeta(a, m):
    z = a[:]
    for i in range(m):
        bit = 1 << i
        for mask in range(1 << m):
            if mask & bit:
                z[mask] += z[mask ^ bit]
    return z


def fixed_arrays(n, e, f):
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


def submasks(indicator, host):
    out = []
    s = host
    while True:
        if indicator[s]:
            out.append(s)
        if s == 0:
            break
        s = (s - 1) & host
    return out


def edge_set(data, mask):
    return {data["H"][i] for i in range(len(data["H"])) if (mask >> i) & 1}


def instance(data, host):
    Rs = submasks(data["r"], host)
    roots = submasks(data["root"], host)
    fibers = {P: [A for A in Rs if (P & ~A) == 0] for P in roots}
    part = tuple(sorted((len(v) for v in fibers.values()), reverse=True))
    return Rs, roots, fibers, part


def extension_edges(data, P, fiber):
    out = []
    for A in fiber:
        if A == P:
            continue
        d = A ^ P
        assert d.bit_count() == 1
        out.append(data["H"][(d & -d).bit_length() - 1])
    return out


def cycle_support(data, P):
    out = set()
    for g in edge_set(data, P) | {data["e"], data["f"]}:
        out.update(g)
    return out


def star_from_size5(data, P, fiber):
    ext = extension_edges(data, P, fiber)
    assert len(ext) == 4
    support = cycle_support(data, P)
    common = set(ext[0])
    for g in ext[1:]:
        common &= set(g)
    outside = common - support
    assert len(outside) == 1
    w = next(iter(outside))
    attachments = []
    for g in ext:
        x = next(v for v in g if v != w)
        assert x in support
        attachments.append(x)
    assert len(set(attachments)) == 4
    return ext, w, attachments


def components_of_edges(edges):
    adj = {}
    for u, v in edges:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    seen = set()
    comps = []
    for s in adj:
        if s in seen:
            continue
        stack = [s]
        seen.add(s)
        vs, es = set(), set()
        while stack:
            u = stack.pop()
            vs.add(u)
            for v in adj[u]:
                es.add(norm((u, v)))
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        comps.append((vs, es))
    return comps


def alpha_network(n, edges, terminals, q):
    edges = sorted(set(map(norm, edges)))
    q = norm(q)
    assert q in edges
    D = C = Dq = Cq = 0
    for mask in range(1 << len(edges)):
        A = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        conn = connected(A, *terminals)
        contains = q in A
        if conn:
            C += 1
            if contains:
                Cq += 1
        else:
            D += 1
            if contains:
                Dq += 1
    return D * Cq - C * Dq


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


def wheel_core_check():
    # rim u=0,v=1,z=2,t=3; hub w=4
    E = norm((1, 2))
    F = norm((3, 0))
    H = sorted({
        norm((0, 1)), norm((2, 3)),
        norm((4, 0)), norm((4, 1)), norm((4, 2)), norm((4, 3)),
    })
    A = B = C = D = 0
    for mask in range(1 << len(H)):
        S = [H[i] for i in range(len(H)) if (mask >> i) & 1]
        if not is_forest(5, S):
            continue
        A += 1
        B += int(is_forest(5, S + [E]))
        C += int(is_forest(5, S + [F]))
        D += int(is_forest(5, S + [E, F]))
    assert (A, B, C, D) == (49, 33, 33, 19)
    assert B * C - A * D == 158
    return (A, B, C, D), 158


def check_511(data):
    checked = 0
    triples = Counter()

    for host, value in enumerate(data["Rcount"]):
        if value != 7:
            continue
        Rs, roots, fibers, part = instance(data, host)
        if part != (5, 1, 1):
            continue
        checked += 1

        P = next(P for P in roots if len(fibers[P]) == 5)
        ext, w, attachments = star_from_size5(data, P, fibers[P])
        extset = set(ext)
        Pset = edge_set(data, P)

        singles = [Q for Q in roots if len(fibers[Q]) == 1]
        assert len(singles) == 2
        pairs = []
        directs = []

        for Q in singles:
            Qset = edge_set(data, Q)
            used = [g for g in ext if g in Qset]
            assert len(used) == 2
            aa = [next(v for v in g if v != w) for g in used]
            pair = frozenset(aa)
            pairs.append(pair)
            direct = norm(tuple(pair))
            directs.append(direct)
            assert direct in data["index"]
            assert (host >> data["index"][direct]) & 1
            assert direct in Pset

        assert not (pairs[0] & pairs[1])

        Croot = Pset | {data["e"], data["f"]}
        comps = components_of_edges(Croot - set(directs))
        assert len(comps) == 2

        ecomp = [i for i, (_, es) in enumerate(comps) if data["e"] in es]
        fcomp = [i for i, (_, es) in enumerate(comps) if data["f"] in es]
        assert len(ecomp) == len(fcomp) == 1
        assert ecomp[0] != fcomp[0]

        # Confinement: every nonspoke, nondirect H-edge lies in one branch.
        V0, V1 = comps[0][0], comps[1][0]
        for i, g in enumerate(data["H"]):
            if not ((host >> i) & 1):
                continue
            if g in extset or g in set(directs):
                continue
            assert set(g) <= V0 or set(g) <= V1

        alphas = {}
        for vs, path_edges in comps:
            if data["e"] in path_edges:
                q = data["e"]
            elif data["f"] in path_edges:
                q = data["f"]
            else:
                raise AssertionError("branch has no distinguished edge")

            deg = Counter()
            for a, b in path_edges:
                deg[a] += 1
                deg[b] += 1
            terminals = [v for v, d in deg.items() if d == 1]
            assert len(terminals) == 2

            network_edges = [q] + [
                g for i, g in enumerate(data["H"])
                if ((host >> i) & 1) and set(g) <= vs
            ]
            alphas[q] = alpha_network(
                data["n"], network_edges, tuple(terminals), q
            )

        dg = delta(data, host)
        assert dg == 158 * alphas[data["e"]] * alphas[data["f"]]
        triples[(dg, alphas[data["e"]], alphas[data["f"]])] += 1

    return checked, triples


def check_four_root_incidence(data):
    checked = 0
    incidence = Counter()

    for host, value in enumerate(data["Rcount"]):
        if value != 4:
            continue
        Rs, roots, fibers, part = instance(data, host)
        if part != (1, 1, 1, 1):
            continue
        checked += 1
        for i, g in enumerate(data["H"]):
            if not ((host >> i) & 1):
                continue
            c = sum(bool((P >> i) & 1) for P in roots)
            assert c in (0, 2, 4)
            incidence[c] += 1

    return checked, incidence


def main():
    print("W4:", wheel_core_check())

    cases = [
        ("n6-adj", fixed_arrays(6, (0, 1), (0, 2))),
        ("n6-dis", fixed_arrays(6, (0, 1), (2, 3))),
        ("n7-adj", fixed_arrays(7, (0, 1), (0, 2))),
        ("n7-dis", fixed_arrays(7, (0, 1), (2, 3))),
    ]

    expected_parts = {
        "n6-adj": Counter({(7,): 82, (4, 3): 30}),
        "n6-dis": Counter({(7,): 64, (3, 3, 1): 72,
                           (5, 1, 1): 36, (4, 3): 32}),
        "n7-adj": Counter({(7,): 918, (4, 3): 396}),
        "n7-dis": Counter({(7,): 1542, (3, 3, 1): 1260,
                           (4, 3): 864, (5, 1, 1): 630}),
    }

    expected_511 = {
        "n6-adj": (0, Counter()),
        "n6-dis": (
            36,
            Counter({
                (158, 1, 1): 4,
                (316, 1, 2): 16,
                (316, 2, 1): 16,
            }),
        ),
        "n7-adj": (0, Counter()),
        "n7-dis": (
            630,
            Counter({
                (158, 1, 1): 6,
                (316, 1, 2): 48,
                (316, 2, 1): 48,
                (632, 2, 2): 192,
                (632, 4, 1): 168,
                (632, 1, 4): 168,
            }),
        ),
    }

    expected_four = {
        "n6-adj": (0, Counter()),
        "n6-dis": (2, Counter({2: 16, 0: 1})),
        "n7-adj": (0, Counter()),
        "n7-dis": (78, Counter({2: 624, 0: 75, 4: 72})),
    }

    for name, data in cases:
        parts = partition_counts(data, 7)
        assert parts == expected_parts[name], (name, parts)
        assert (6, 1) not in parts
        assert (4, 1, 1, 1) not in parts

        got511 = check_511(data)
        assert got511 == expected_511[name], (name, got511)

        got4 = check_four_root_incidence(data)
        assert got4 == expected_four[name], (name, got4)

        print(name, "R=7 partitions:", dict(parts))
        print(name, "5+1+1 factor triples:", got511)
        print(name, "all-minimal R=4 incidence:", got4)

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
