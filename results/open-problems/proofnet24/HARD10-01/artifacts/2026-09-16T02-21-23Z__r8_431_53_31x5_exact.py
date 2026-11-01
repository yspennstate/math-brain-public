#!/usr/bin/env python3
"""HARD10-01 exact checks for the 2026-09-16 02Z checkpoint.

Standard-library only. Finite checks are adversarial evidence, not universal proof premises.

Checks:
  * the marked W4 core polynomial for the 4+3+1 reduction is
      Delta(t)=4(11 t^2+8 t+2),
    hence Delta(1/3)=212/9;
  * every representative |R|=8, partition (4,3,1) instance through n=7
    has the claimed ear suppression to a (4,1,1) graph, the new edge occurs
    in 5 of 6 R-forests and is the marked exact-two exchange edge, and
      Delta_G = 212 alpha_e alpha_f;
  * no (5,3) or (3,1,1,1,1,1) instances occur in the same exhaustive ranges.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations


def norm(e):
    return tuple(sorted(e))


def forest_components(n, edges, mask):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, (a, b) in enumerate(edges):
        if not ((mask >> i) & 1):
            continue
        a, b = find(a), find(b)
        if a == b:
            return None
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

    for i in range(n):
        parent[i] = find(i)
    return parent


def fixed_R_arrays(n, e, f):
    e, f = norm(e), norm(f)
    H = [g for g in combinations(range(n), 2) if g not in (e, f)]
    N = 1 << len(H)
    r = bytearray(N)

    a, b = e
    c, d = f
    for mask in range(N):
        comp = forest_components(n, H, mask)
        if comp is None:
            continue
        ra, rb, rc, rd = comp[a], comp[b], comp[c], comp[d]
        if ra == rb or rc == rd:
            continue
        if rc in (ra, rb) and rd in (ra, rb) and rc != rd:
            r[mask] = 1

    root = bytearray(N)
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

    counts = list(r)
    for i in range(len(H)):
        bit = 1 << i
        for mask in range(N):
            if mask & bit:
                counts[mask] += counts[mask ^ bit]

    return H, r, root, counts


def edge_set(H, mask):
    return {H[i] for i in range(len(H)) if (mask >> i) & 1}


def root_fibers(Rs, roots):
    return {P: [A for A in Rs if (P & ~A) == 0] for P in roots}


def classify_from_lists(M, r_masks, root_masks):
    Rs = [A for A in r_masks if (A & ~M) == 0]
    roots = [P for P in root_masks if (P & ~M) == 0]
    fibers = root_fibers(Rs, roots)
    part = tuple(sorted((len(v) for v in fibers.values()), reverse=True))
    return part, Rs, roots, fibers


def extension_single_edges(H, P, fiber):
    out = []
    for A in fiber:
        if A == P:
            continue
        d = A ^ P
        if d.bit_count() != 1:
            return None
        out.append(H[(d & -d).bit_length() - 1])
    return out


def ear_info(H, P, fiber):
    atoms = extension_single_edges(H, P, fiber)
    if atoms is None or len(atoms) != 2:
        return None
    common = set(atoms[0]) & set(atoms[1])
    if len(common) != 1:
        return None
    w = next(iter(common))
    ends = tuple(sorted(next(v for v in ed if v != w) for ed in atoms))
    return w, ends, atoms


def component_edges(E, target):
    adj = defaultdict(set)
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    seen = set()
    stack = [target[0]]
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        stack.extend(adj[x] - seen)
    return {g for g in E if g[0] in seen and g[1] in seen}, seen


def alpha_unit(n, K, terminals, distinguished):
    K = sorted(set(map(norm, K)))
    s, t = terminals
    q = norm(distinguished)
    iq = K.index(q)
    D = C = Dq = Cq = 0
    for mask in range(1 << len(K)):
        comp = forest_components(n, K, mask)
        if comp is None:
            continue
        conn = comp[s] == comp[t]
        has_q = (mask >> iq) & 1
        if conn:
            C += 1
            Cq += has_q
        else:
            D += 1
            Dq += has_q
    return D * Cq - C * Dq


def direct_delta(n, E, e, f):
    E = sorted(set(map(norm, E)))
    e, f = norm(e), norm(f)
    ie, jf = E.index(e), E.index(f)
    A = B = C = D = 0
    for mask in range(1 << len(E)):
        if forest_components(n, E, mask) is None:
            continue
        he = (mask >> ie) & 1
        hf = (mask >> jf) & 1
        if not he and not hf:
            A += 1
        elif he and not hf:
            B += 1
        elif hf and not he:
            C += 1
        else:
            D += 1
    return B * C - A * D, (A, B, C, D)


def marked_wheel_core_certificate():
    # K5 minus {03,24}; distinguished E=01,F=23; marked incidence-5 edge r=02.
    n = 5
    e, f, r = (0, 1), (2, 3), (0, 2)
    E = [e, f, (0, 4), (1, 2), (1, 3), (1, 4), (3, 4), r]
    ie, jf, ir = E.index(e), E.index(f), E.index(r)

    # Each count is a0 + a1 t because only r is weighted by t.
    counts = {"Z": [0, 0], "Ze": [0, 0], "Zf": [0, 0], "Zef": [0, 0]}
    for mask in range(1 << len(E)):
        if forest_components(n, E, mask) is None:
            continue
        k = (mask >> ir) & 1
        counts["Z"][k] += 1
        if (mask >> ie) & 1:
            counts["Ze"][k] += 1
        if (mask >> jf) & 1:
            counts["Zf"][k] += 1
        if ((mask >> ie) & 1) and ((mask >> jf) & 1):
            counts["Zef"][k] += 1

    assert counts == {
        "Z": [82, 52],
        "Ze": [34, 14],
        "Zf": [34, 18],
        "Zef": [14, 4],
    }

    # Polynomial coefficients low-to-high.
    # (34+14t)(34+18t) - (82+52t)(14+4t) = 8+32t+44t^2.
    delta = [8, 32, 44]
    assert delta == [4 * 2, 4 * 8, 4 * 11]
    val = Fraction(delta[0], 1) + Fraction(delta[1], 3) + Fraction(delta[2], 9)
    assert val == Fraction(212, 9)
    return counts, delta, val


def analyze_411(n, e, f, H, r_masks, root_masks, MB):
    part, Rs, roots, fibers = classify_from_lists(MB, r_masks, root_masks)
    assert part == (4, 1, 1)
    P = next(P for P in roots if len(fibers[P]) == 4)
    singles = [Q for Q in roots if len(fibers[Q]) == 1]
    spokes = extension_single_edges(H, P, fibers[P])
    assert spokes is not None and len(spokes) == 3
    common = set(spokes[0]) & set(spokes[1]) & set(spokes[2])
    assert len(common) == 1
    w = next(iter(common))

    def attachment(ed):
        return next(x for x in ed if x != w)

    def singleton_pair(Q):
        Qset = edge_set(H, Q)
        return frozenset(attachment(ed) for ed in spokes if ed in Qset)

    pairs = [singleton_pair(Q) for Q in singles]
    assert all(len(p) == 2 for p in pairs)
    shared = set(pairs[0]) & set(pairs[1])
    assert len(shared) == 1
    u = next(iter(shared))

    E = edge_set(H, MB) | {norm(e), norm(f)}
    flags = [norm(tuple(p)) in E for p in pairs]
    assert sum(flags) == 1
    present = pairs[flags.index(True)]
    absent = pairs[flags.index(False)]
    v = next(iter(set(present) - {u}))
    z = next(iter(set(absent) - {u}))
    uv, uz = norm((u, v)), norm((u, z))

    # Exact-two compression of the absent-direct singleton.
    MB2 = MB
    for s in spokes:
        MB2 &= ~(1 << H.index(s))
    MB2 |= 1 << H.index(uz)
    part2, Rs2, roots2, fibers2 = classify_from_lists(MB2, r_masks, root_masks)
    assert part2 == (1, 1) and len(Rs2) == 2 and len(roots2) == 2
    Qp = next(R for R in roots2 if R != P)
    Pset, Qpset = edge_set(H, P), edge_set(H, Qp)
    exchange = (Pset - Qpset) | (Qpset - Pset)
    assert len(exchange) == 4

    B_edges = E - set(spokes) | {uz}
    remainder = B_edges - exchange
    Ke, Ve = component_edges(remainder, norm(e))
    Kf, Vf = component_edges(remainder, norm(f))
    assert not (Ve & Vf)
    Te = {x for x in Ve if any(x in g for g in exchange)}
    Tf = {x for x in Vf if any(x in g for g in exchange)}
    assert len(Te) == len(Tf) == 2
    ae = alpha_unit(n, Ke, tuple(Te), e)
    af = alpha_unit(n, Kf, tuple(Tf), f)

    return {
        "Rs": Rs,
        "roots": roots,
        "fibers": fibers,
        "exchange": exchange,
        "Ke": Ke,
        "Kf": Kf,
        "alpha_e": ae,
        "alpha_f": af,
    }


def check_pair(n, e, f):
    H, r, root, counts = fixed_R_arrays(n, e, f)
    r_masks = [m for m, x in enumerate(r) if x]
    root_masks = [m for m, x in enumerate(root) if x]

    part_counts = Counter()
    checked_431 = 0
    triples = Counter()

    for M, total in enumerate(counts):
        if total != 8:
            continue
        part, Rs, roots, fibers = classify_from_lists(M, r_masks, root_masks)
        part_counts[part] += 1
        if part != (4, 3, 1):
            continue

        checked_431 += 1
        p3 = next(P for P in roots if len(fibers[P]) == 3)
        ear = ear_info(H, p3, fibers[p3])
        assert ear is not None
        w, (u, v), ear_edges = ear
        g = norm((u, v))
        E = edge_set(H, M) | {norm(e), norm(f)}

        # Universal structural claims used in the report.
        assert g not in E
        other_roots = [P for P in roots if P != p3]
        assert all(set(ear_edges) <= edge_set(H, Q) for Q in other_roots)

        MB = M
        for ed in ear_edges:
            MB &= ~(1 << H.index(ed))
        MB |= 1 << H.index(g)

        partB, RsB, rootsB, fibersB = classify_from_lists(MB, r_masks, root_masks)
        assert partB == (4, 1, 1)
        assert sum(g in edge_set(H, A) for A in RsB) == 5

        info = analyze_411(n, e, f, H, r_masks, root_masks, MB)
        assert g in info["exchange"]

        gap, _ = direct_delta(n, E, e, f)
        ae, af = info["alpha_e"], info["alpha_f"]
        assert gap == 212 * ae * af
        triples[(ae, af, gap)] += 1

    return part_counts, checked_431, triples


def main():
    counts, poly, val = marked_wheel_core_certificate()
    print("MARKED_W4_COUNTS", counts)
    print("MARKED_W4_DELTA_COEFFS", poly, "Delta(1/3)=", val)

    configs = [
        (6, (0, 1), (0, 2), "n6_adjacent"),
        (6, (0, 1), (2, 3), "n6_disjoint"),
        (7, (0, 1), (0, 2), "n7_adjacent"),
        (7, (0, 1), (2, 3), "n7_disjoint"),
    ]
    for n, e, f, label in configs:
        parts, checked, triples = check_pair(n, e, f)
        print(label)
        print("  R8_partitions", dict(parts))
        print("  4+3+1_checked", checked)
        print("  4+3+1_factor_triples", dict(triples))
        print("  count_5+3", parts.get((5, 3), 0))
        print("  count_3+1^5", parts.get((3, 1, 1, 1, 1, 1), 0))


if __name__ == "__main__":
    main()
