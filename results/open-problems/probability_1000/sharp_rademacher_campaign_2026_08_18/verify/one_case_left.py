"""The induction reduces to ONE case. Test its one inequality exhaustively.

Setting: B(H) = 2^{E-V+2b} 3^{V-b}, b = 1 iff bipartite. Recursion F(G) = 2F(G-e) - F(G/e).
Induction hypothesis F <= B on smaller graphs. Then

    F(G) = 2F(G-e) - F(G/e) <= 2B(G-e) - F(G/e),

so the step closes iff  F(G/e) >= 2B(G-e) - B(G).  Computing the right side by cases:

  (i)  G bipartite               -> G-e bipartite, B(G-e) = B(G)/2, RHS = 0.        TRIVIAL
  (ii) G and G-e non-bipartite   -> B(G-e) = B(G)/2, RHS = 0.                        TRIVIAL
  (iii) G non-bipartite, G-e BIPARTITE (e is in every odd cycle):
            B(G-e) = (2/3) B(G),  RHS = (4/3 - 1) B(G) = B(G)/3 = 2^{E-V} 3^{V-1}.

So everything rests on case (iii):

        ***  F(G/e)  >=  2^{E-V} 3^{V-1}   whenever G is non-bipartite and G-e is bipartite  ***

with V, E the parameters of G. Note G/e has V-1 vertices and E-1 edges (self-loops from the
contraction are never cut and are dropped).

Also recorded here, because it is free and proved: for a BIPARTITE graph every even subgraph has an
even number of edges (all cycles even), so every term (-1/3)^{|S|} is positive and Z >= 1, i.e.
F >= I = 2^V (3/2)^E. That is a proved lower bound on the bipartite side.

This enumerates all connected graphs to V<=7, finds every (G, e) in case (iii), and checks the
inequality exactly in integers. Reports the worst margin and any failure.
"""
import itertools
import sys

VMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7


def F(V, edges):
    tot = 0
    for bits in range(1 << V):
        c = 0
        for (a, b) in edges:
            if ((bits >> a) ^ (bits >> b)) & 1:
                c += 1
        tot += 1 << c
    return tot


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
    seen, st = {0}, [0]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    return len(seen) == V


def contract(V, edges, ei):
    a, b = edges[ei]
    keep, gone = min(a, b), max(a, b)
    m, nxt = {}, 0
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
        if nx != ny:
            ne.append((nx, ny))
    return V - 1, ne


cases = 0
fails = []
worst = None
for V in range(3, VMAX + 1):
    alledges = list(itertools.combinations(range(V), 2))
    for mask in range(1, 1 << len(alledges)):
        edges = [alledges[i] for i in range(len(alledges)) if (mask >> i) & 1]
        if len({v for e in edges for v in e}) != V or not connected(V, edges):
            continue
        if bipartite(V, edges):
            continue                       # case (i)
        E = len(edges)
        for ei in range(E):
            ed = [e for i, e in enumerate(edges) if i != ei]
            if not ed or not connected(V, ed):
                continue
            if not bipartite(V, ed):
                continue                   # case (ii)
            # case (iii)
            Vc, ec = contract(V, edges, ei)
            if not connected(Vc, ec):
                continue
            cases += 1
            lhs = F(Vc, ec)
            rhs = (2 ** (E - V)) * (3 ** (V - 1))
            margin = lhs / rhs
            if worst is None or margin < worst[0]:
                worst = (margin, V, E, tuple(edges), edges[ei], lhs, rhs)
            if lhs < rhs:
                fails.append((V, E, tuple(edges), edges[ei], lhs, rhs))

print("case (iii) instances found (G non-bipartite, G-e bipartite, both connected): %d" % cases)
print()
if fails:
    print("*** FAILURES: %d" % len(fails))
    for V, E, edges, e, lhs, rhs in fails[:8]:
        print("   V=%d E=%d  e=%s  F(G/e)=%d < %d   %s" % (V, E, e, lhs, rhs, edges))
else:
    print("NO FAILURE. F(G/e) >= 2^{E-V} 3^{V-1} held in every case (iii) instance.")
print()
if worst:
    m, V, E, edges, e, lhs, rhs = worst
    print("tightest instance: margin F(G/e)/RHS = %.9f" % m)
    print("   V=%d E=%d contracted edge %s   F(G/e)=%d  RHS=%d" % (V, E, e, lhs, rhs))
    print("   G = %s" % (edges,))
