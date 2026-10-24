"""Verify the deletion-contraction recursion, and locate where an induction would have to work.

F(G) := SUM over x in {+-1}^V of 2^{cut(x)}.  Then Z = (2/3)^E * F(G) / 2^V, and the RC-sufficient
inequality established today is

    F(G)  <=  B(G) := 2^{E-V+2b} 3^{V-b},      b = 1 if G bipartite else 0   (G connected)

tight in the limit on odd cycles: F(C_m odd) = 3^m - 1 against B = 3^m.

RECURSION (derived): splitting the sum on whether e's endpoints agree,
    F(G) = F_same(G-e) + 2 F_diff(G-e),  F(G-e) = F_same + F_diff,  F(G/e) = F_same(G-e)
    =>   F(G) = 2 F(G-e) - F(G/e).
Hand-checked on C3: 2*18 - 10 = 26.

This verifies the recursion on many graphs (including multigraphs, which contraction produces), and
then checks whether B satisfies the SAME recursion as an inequality - i.e. whether
    2 B(G-e) - B(G/e)  <=  B(G)
which is what a straight induction would need. Where that FAILS is exactly where the induction needs
a better invariant, and naming that is more useful than a blind search.
"""
import itertools
import sys


def F(V, edges):
    """edges may repeat (multigraph). V = number of vertices."""
    tot = 0
    for bits in range(1 << V):
        c = 0
        for (a, b) in edges:
            if ((bits >> a) ^ (bits >> b)) & 1:
                c += 1
        tot += 1 << c
    return tot


def contract(V, edges, ei):
    """contract edge index ei; relabel; drop self-loops (a self-loop is never cut, factor 1)."""
    a, b = edges[ei]
    if a == b:
        return V, [e for i, e in enumerate(edges) if i != ei]
    keep, gone = min(a, b), max(a, b)
    m = {}
    nxt = 0
    for v in range(V):
        if v == gone:
            continue
        m[v] = nxt
        nxt += 1
    m[gone] = m[keep]
    ne = []
    for i, (x, y) in enumerate(edges):
        if i == ei:
            continue
        nx, ny = m[x], m[y]
        if nx == ny:
            continue          # self-loop: never cut, contributes factor 1
        ne.append((nx, ny))
    return V - 1, ne


def bipartite(V, edges):
    adj = {v: [] for v in range(V)}
    for a, b in edges:
        if a == b:
            return False
        adj[a].append(b)
        adj[b].append(a)
    col = {}
    for s in range(V):
        if s in col:
            continue
        col[s] = 0
        st = [s]
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in col:
                    col[v] = 1 - col[u]
                    st.append(v)
                elif col[v] == col[u]:
                    return False
    return True


def connected(V, edges):
    if V == 0:
        return True
    adj = {v: [] for v in range(V)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    st = [0]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    return len(seen) == V


def B(V, edges):
    E = len(edges)
    b = 1 if bipartite(V, edges) else 0
    return (2 ** (E - V + 2 * b)) * (3 ** (V - b))


rec_ok = rec_bad = 0
ind_ok = ind_bad = 0
ind_failures = []
for V in range(3, 7):
    alledges = list(itertools.combinations(range(V), 2))
    for mask in range(1, 1 << len(alledges)):
        edges = [alledges[i] for i in range(len(alledges)) if (mask >> i) & 1]
        if len({v for e in edges for v in e}) != V or not connected(V, edges):
            continue
        if len(edges) < 1:
            continue
        ei = 0
        lhs = F(V, edges)
        Vd, ed = V, [e for i, e in enumerate(edges) if i != ei]
        Vc, ec = contract(V, edges, ei)
        if not ed:
            continue
        rhs = 2 * F(Vd, ed) - F(Vc, ec)
        if lhs == rhs:
            rec_ok += 1
        else:
            rec_bad += 1

        # would a straight induction on B close?
        if connected(Vd, ed) and connected(Vc, ec) and ec:
            cand = 2 * B(Vd, ed) - B(Vc, ec)
            if cand <= B(V, edges):
                ind_ok += 1
            else:
                ind_bad += 1
                if len(ind_failures) < 6:
                    ind_failures.append((V, tuple(edges), B(V, edges), cand,
                                         bipartite(V, edges), bipartite(Vd, ed), bipartite(Vc, ec)))

print("deletion-contraction  F(G) = 2F(G-e) - F(G/e)")
print("   verified on %d connected graphs, mismatches %d" % (rec_ok, rec_bad))
print()
print("would a straight induction close?  need 2B(G-e) - B(G/e) <= B(G)")
print("   holds %d,  FAILS %d" % (ind_ok, ind_bad))
if ind_failures:
    print()
    print("   where it fails (bip flags: G, G-e, G/e):")
    for V, edges, bg, cand, b1, b2, b3 in ind_failures:
        print("     V=%d E=%d  B(G)=%d  2B(G-e)-B(G/e)=%d   bip %s %s %s   %s"
              % (V, len(edges), bg, cand, b1, b2, b3, edges))
