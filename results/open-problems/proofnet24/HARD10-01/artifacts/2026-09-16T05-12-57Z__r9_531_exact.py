#!/usr/bin/env python3
"""HARD10-01 exact checks for the 2026-09-16 05Z checkpoint.

Finite enumeration is adversarial self-checking only, except the displayed
five-vertex W4 marked-edge polynomial and six-vertex prism core, which are
finite exact identities.

Checks representative adjacent/disjoint distinguished pairs through n=7 for:
  * |R|=9 partition 5+3+1;
  * size-three ear compression to exact 5+1+1;
  * identification of the compressed edge as a literal direct-pair rim edge;
  * marked W4 polynomial Delta(t)=8+86 t+64 t^2;
  * exact unit factorization Delta_G=394 alpha_1 alpha_2;
  * finite reconnaissance for 4+4+1, including the observed decorated-prism
    factorization Delta_G=304 alpha_1 alpha_2;
  * all |R|=9 partition counts in the same search ranges.
"""
from collections import Counter, defaultdict
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


def classify(M, r_masks, root_masks):
    Rs = [A for A in r_masks if (A & ~M) == 0]
    roots = [P for P in root_masks if (P & ~M) == 0]
    fib = root_fibers(Rs, roots)
    part = tuple(sorted((len(v) for v in fib.values()), reverse=True))
    return part, Rs, roots, fib


def fiber_atoms(H, P, fiber):
    out = []
    for A in fiber:
        if A == P:
            continue
        d = A ^ P
        if d.bit_count() == 1:
            out.append(H[(d & -d).bit_length() - 1])
    return out


def pure_star(H, P, fiber, atom_count):
    ats = fiber_atoms(H, P, fiber)
    if len(fiber) != atom_count + 1 or len(ats) != atom_count:
        return None
    common = set(ats[0])
    for a in ats[1:]:
        common &= set(a)
    if len(common) != 1:
        return None
    w = next(iter(common))
    attachments = tuple(sorted(next(v for v in a if v != w) for a in ats))
    return w, attachments, tuple(ats)


def direct_delta(n, E, e, f):
    E = sorted(set(map(norm, E)))
    e, f = norm(e), norm(f)
    ie, jf = E.index(e), E.index(f)
    A = B = C = D = 0
    for m in range(1 << len(E)):
        if forest_components(n, E, m) is None:
            continue
        he, hf = (m >> ie) & 1, (m >> jf) & 1
        if not he and not hf:
            A += 1
        elif he and not hf:
            B += 1
        elif hf and not he:
            C += 1
        else:
            D += 1
    return B * C - A * D, (A, B, C, D)


def alpha_terminal(n, edges, q, s, t):
    edges = sorted(set(map(norm, edges)))
    q = norm(q)
    iq = edges.index(q)
    D = C = Dq = Cq = 0
    for m in range(1 << len(edges)):
        comp = forest_components(n, edges, m)
        if comp is None:
            continue
        conn = comp[s] == comp[t]
        hasq = (m >> iq) & 1
        if conn:
            C += 1
            if hasq:
                Cq += 1
        else:
            D += 1
            if hasq:
                Dq += 1
    return D * Cq - C * Dq


def path_components(edges):
    adj = defaultdict(list)
    verts = set()
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        verts |= {u, v}
    seen = set()
    out = []
    for v in verts:
        if v in seen:
            continue
        stack = [v]
        seen.add(v)
        comp = set()
        while stack:
            x = stack.pop()
            comp.add(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        out.append(comp)
    return out


def marked_wheel_certificate():
    # Rim u-v-z-t-u, hub w. Distinguished opposite rim edges v-z,t-u.
    # Mark the direct-pair rim edge u-v with weight s.
    u, v, z, t, w = 0, 1, 2, 3, 4
    E = {
        norm((u, v)), norm((v, z)), norm((z, t)), norm((t, u)),
        norm((w, u)), norm((w, v)), norm((w, z)), norm((w, t)),
    }
    e, f, g = norm((v, z)), norm((t, u)), norm((u, v))
    edges = sorted(E)
    ie, jf, kg = edges.index(e), edges.index(f), edges.index(g)
    coeff = {k: [0, 0] for k in "ABCD"}
    for m in range(1 << len(edges)):
        if forest_components(5, edges, m) is None:
            continue
        he, hf, hg = (m >> ie) & 1, (m >> jf) & 1, (m >> kg) & 1
        key = "D" if he and hf else "B" if he else "C" if hf else "A"
        coeff[key][hg] += 1
    assert coeff == {
        "A": [28, 21], "B": [20, 13], "C": [20, 13], "D": [14, 5]
    }
    # (20+13s)^2 - (28+21s)(14+5s) = 8+86s+64s^2.
    delta = [
        coeff["B"][0] * coeff["C"][0] - coeff["A"][0] * coeff["D"][0],
        coeff["B"][0] * coeff["C"][1] + coeff["B"][1] * coeff["C"][0]
        - coeff["A"][0] * coeff["D"][1] - coeff["A"][1] * coeff["D"][0],
        coeff["B"][1] * coeff["C"][1] - coeff["A"][1] * coeff["D"][1],
    ]
    assert delta == [8, 86, 64]
    # At s=1/3, 9 Delta(s)=394.
    assert 9 * delta[0] + 3 * delta[1] + delta[2] == 394
    return coeff, delta


def prism_certificate():
    # Candidate 4+4+1 torso from finite reconnaissance.
    u, a, b, v, w, x = range(6)
    E = {
        norm((u, a)), norm((a, b)), norm((b, v)),
        norm((w, u)), norm((w, v)), norm((w, a)),
        norm((x, u)), norm((x, v)), norm((x, b)),
    }
    gap, cells = direct_delta(6, E, (u, a), (b, v))
    assert cells == (114, 76, 76, 48)
    assert gap == 304
    return cells, gap


def check_pair(n, e, f):
    H, r, root, counts = fixed_R_arrays(n, e, f)
    r_masks = [m for m, x in enumerate(r) if x]
    root_masks = [m for m, x in enumerate(root) if x]
    part9 = Counter()
    f531 = Counter()
    f441 = Counter()
    c531 = c441 = 0

    for M, total in enumerate(counts):
        if total != 9:
            continue
        part, Rs, roots, fib = classify(M, r_masks, root_masks)
        part9[part] += 1
        E = edge_set(H, M) | {norm(e), norm(f)}

        if part == (5, 3, 1):
            c531 += 1
            P5 = next(P for P in roots if len(fib[P]) == 5)
            P3 = next(P for P in roots if len(fib[P]) == 3)
            S = next(P for P in roots if len(fib[P]) == 1)

            ats3 = fiber_atoms(H, P3, fib[P3])
            assert len(ats3) == 2 and len(fib[P3]) == 3
            common = set(ats3[0]) & set(ats3[1])
            assert len(common) == 1
            x = next(iter(common))
            ends = [next(v for v in a if v != x) for a in ats3]
            g = norm(ends)

            assert set(ats3) <= edge_set(H, P5)
            assert set(ats3) <= edge_set(H, S)
            assert g not in E

            MB = M
            for a in ats3:
                MB &= ~(1 << H.index(a))
            MB |= 1 << H.index(g)
            partB, RsB, rootsB, fibB = classify(MB, r_masks, root_masks)
            assert partB == (5, 1, 1) and len(RsB) == 7
            assert sum(g in edge_set(H, A) for A in RsB) == 6

            PL = next(P for P in rootsB if len(fibB[P]) == 5)
            star = pure_star(H, PL, fibB[PL], 4)
            assert star is not None
            hub, attachments, spokes = star
            singles = [Q for Q in rootsB if len(fibB[Q]) == 1]
            pairs = []
            for Q in singles:
                Qe = edge_set(H, Q)
                pair = tuple(sorted(next(v for v in a if v != hub)
                                    for a in spokes if a in Qe))
                assert len(pair) == 2
                pairs.append(pair)
            assert len(set(pairs)) == 2 and set(pairs[0]).isdisjoint(pairs[1])
            directs = [norm(p) for p in pairs]
            assert all(d in edge_set(H, PL) for d in directs)
            assert g in directs

            cyc = (edge_set(H, PL) | {norm(e), norm(f)}) - set(directs)
            comps = path_components(cyc)
            assert len(comps) == 2
            assert sum(set(e) <= C for C in comps) == 1
            assert sum(set(f) <= C for C in comps) == 1
            assert not any(set(e) <= C and set(f) <= C for C in comps)

            EB = edge_set(H, MB) | {norm(e), norm(f)}
            for ed in EB:
                if ed in set(spokes) or ed in set(directs):
                    continue
                assert any(set(ed) <= C for C in comps)

            alphas = []
            for C in comps:
                KE = {ed for ed in EB if set(ed) <= C}
                q = norm(e) if set(e) <= C else norm(f)
                terminals = tuple(C & set(attachments))
                assert len(terminals) == 2
                alphas.append(alpha_terminal(n, KE, q, *terminals))
            gap, _ = direct_delta(n, E, e, f)
            assert gap == 394 * alphas[0] * alphas[1]
            f531[(alphas[0], alphas[1], gap)] += 1

        if part == (4, 4, 1):
            # Finite reconnaissance only: every checked instance is the
            # decorated triangular-prism geometry described in the report.
            c441 += 1
            R4 = [P for P in roots if len(fib[P]) == 4]
            st = [pure_star(H, P, fib[P], 3) for P in R4]
            assert all(st)
            (w, A, SW), (x, B, SX) = st
            inter = set(A) & set(B)
            assert len(inter) == 2
            u, v = sorted(inter)
            a = next(iter(set(A) - inter))
            b = next(iter(set(B) - inter))
            PE = [edge_set(H, P) for P in R4]
            assert {norm((x, u)), norm((x, v))} <= PE[0]
            assert {norm((w, u)), norm((w, v))} <= PE[1]

            singleton = next(P for P in roots if len(fib[P]) == 1)
            SE = edge_set(H, singleton)
            usew = {next(z for z in at if z != w) for at in SW if at in SE}
            usex = {next(z for z in at if z != x) for at in SX if at in SE}

            common_path = (PE[0] & PE[1]) | {norm(e), norm(f)}
            adj = defaultdict(list)
            for p, q in common_path:
                adj[p].append(q)
                adj[q].append(p)
            assert len(adj[u]) == len(adj[v]) == 1
            order = [u]
            prev = None
            cur = u
            while cur != v:
                nxt = next(z for z in adj[cur] if z != prev)
                order.append(nxt)
                prev, cur = cur, nxt
            ia, ib = order.index(a), order.index(b)
            if ia > ib:
                order.reverse()
                u, v = v, u
                ia, ib = order.index(a), order.index(b)
            assert ib == ia + 1 and norm((a, b)) in E
            assert usew == {a, v} and usex == {u, b}

            L = set(order[:ia + 1])
            R = set(order[ib:])
            assert ({"L" if set(q) <= L else "R" if set(q) <= R else "?"
                     for q in (norm(e), norm(f))} == {"L", "R"})
            for ed in E:
                if ed in set(SW) | set(SX) | {norm((a, b))}:
                    continue
                assert set(ed) <= L or set(ed) <= R

            alphas = []
            for C in (L, R):
                KE = {ed for ed in E if set(ed) <= C}
                q = norm(e) if set(e) <= C else norm(f)
                terminals = tuple(C & {u, v, a, b})
                assert len(terminals) == 2
                alphas.append(alpha_terminal(n, KE, q, *terminals))
            gap, _ = direct_delta(n, E, e, f)
            assert gap == 304 * alphas[0] * alphas[1]
            f441[(alphas[0], alphas[1], gap)] += 1

    return part9, c531, f531, c441, f441


def main():
    coeff, poly = marked_wheel_certificate()
    print("marked_W4_cells_by_g_absent_present", coeff)
    print("marked_W4_Delta_coeff_low_to_high", poly)
    print("marked_W4_reexpanded_two_edge_ear_factor", 394)
    print("prism_core", prism_certificate())

    configs = [
        (6, (0, 1), (0, 2), "n6_adjacent"),
        (6, (0, 1), (2, 3), "n6_disjoint"),
        (7, (0, 1), (0, 2), "n7_adjacent"),
        (7, (0, 1), (2, 3), "n7_disjoint"),
    ]
    for n, e, f, label in configs:
        part9, c531, f531, c441, f441 = check_pair(n, e, f)
        print(label)
        print(" R9_partitions", dict(part9))
        print(" 5+3+1_count", c531)
        print(" 5+3+1_factor_triples", dict(f531))
        print(" 4+4+1_count", c441)
        print(" 4+4+1_candidate_prism_factor_triples", dict(f441))


if __name__ == "__main__":
    main()
