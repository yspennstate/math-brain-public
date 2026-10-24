"""The hardest piece, confirmed with my own eyes: S3 and the theorem on MULTIGRAPHS.

Every check so far enumerated with itertools.combinations, i.e. SIMPLE graphs only. The theorem as
I wrote it says "parallel edges allowed", and contraction produces parallel edges, so that claim is
untested. This tests it.

Checks, on multigraphs with edge multiplicities up to 3:
  T   the theorem itself:  F(G) <= B(G) = 2^{E-V+2b} 3^{V-b}
  S3  a non-critical edge exists for connected, bridgeless, non-bipartite, non-odd-cycle G
  S2  bridge multiplicativity 2F(G) = 3F(G-bridge)
  REC the recursion F(G) = 2F(G-e) - F(G/e)

Note on parallel edges and bipartiteness: two parallel edges form a cycle of LENGTH 2, which is
even, so parallel edges never destroy bipartiteness. A multigraph is bipartite iff its underlying
simple graph is.

A failure in any of these narrows the theorem's scope, which is the useful outcome. The RC
application only needs SIMPLE graphs (linearity forbids two triangles sharing two coordinates), so a
multigraph failure would restrict the statement without touching the application.
"""
import itertools
import sys

VMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5
MAXMULT = 3


def F(V, edges):
    tot = 0
    for bits in range(1 << V):
        c = 0
        for (a, b) in edges:
            if ((bits >> a) ^ (bits >> b)) & 1:
                c += 1
        tot += 1 << c
    return tot


def comps_bip(V, edges):
    adj = {v: [] for v in range(V)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    col, comps, bip = {}, 0, 0
    for s in range(V):
        if s in col:
            continue
        comps += 1
        col[s] = 0
        st, ok = [s], True
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in col:
                    col[v] = 1 - col[u]
                    st.append(v)
                elif col[v] == col[u]:
                    ok = False
        if ok:
            bip += 1
    return comps, bip


def B(V, edges):
    E = len(edges)
    comps, b = comps_bip(V, edges)
    return (2 ** (E - V + 2 * b)) * (3 ** (V - b))


def connected(V, edges):
    return comps_bip(V, edges)[0] == 1


def is_bip(V, edges):
    c, b = comps_bip(V, edges)
    return b == c


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


t_ok = t_bad = 0
s3_ok = s3_bad = 0
s2_ok = s2_bad = 0
rec_ok = rec_bad = 0
t_fail, s3_fail = [], []
para_seen = 0

for V in range(2, VMAX + 1):
    pairs = list(itertools.combinations(range(V), 2))
    for mults in itertools.product(range(MAXMULT + 1), repeat=len(pairs)):
        if sum(mults) == 0 or sum(mults) > 9:
            continue
        edges = []
        for p, m in zip(pairs, mults):
            edges.extend([p] * m)
        if len({v for e in edges for v in e}) != V or not connected(V, edges):
            continue
        if max(mults) >= 2:
            para_seen += 1
        E = len(edges)

        # T: the theorem
        if F(V, edges) <= B(V, edges):
            t_ok += 1
        else:
            t_bad += 1
            if len(t_fail) < 5:
                t_fail.append((V, tuple(edges), F(V, edges), B(V, edges)))

        # REC on the first edge
        ed = [e for i, e in enumerate(edges) if i != 0]
        Vc, ec = contract(V, edges, 0)
        if ed:
            if F(V, edges) == 2 * F(V, ed) - F(Vc, ec):
                rec_ok += 1
            else:
                rec_bad += 1

        # bridges
        br = []
        for i in range(E):
            e2 = [e for j, e in enumerate(edges) if j != i]
            if comps_bip(V, e2)[0] > 1:
                br.append(i)
        if br:
            i = br[0]
            e2 = [e for j, e in enumerate(edges) if j != i]
            if 2 * F(V, edges) == 3 * F(V, e2):
                s2_ok += 1
            else:
                s2_bad += 1

        # S3
        if not br and not is_bip(V, edges):
            deg = {v: 0 for v in range(V)}
            for a, b in edges:
                deg[a] += 1
                deg[b] += 1
            is_odd_cycle = (E == V) and all(deg[v] == 2 for v in range(V)) and max(mults) == 1
            if not is_odd_cycle:
                found = any(connected(V, [e for j, e in enumerate(edges) if j != i])
                            and not is_bip(V, [e for j, e in enumerate(edges) if j != i])
                            for i in range(E))
                if found:
                    s3_ok += 1
                else:
                    s3_bad += 1
                    if len(s3_fail) < 5:
                        s3_fail.append((V, tuple(edges)))

print("multigraphs examined (with at least one parallel pair): %d" % para_seen)
print()
print("T   theorem  F <= B                 : %7d ok, %5d FAIL" % (t_ok, t_bad))
for x in t_fail:
    print("       V=%d %s  F=%d B=%d" % x)
print("REC F(G) = 2F(G-e) - F(G/e)          : %7d ok, %5d FAIL" % (rec_ok, rec_bad))
print("S2  bridge 2F(G) = 3F(G-e)           : %7d ok, %5d FAIL" % (s2_ok, s2_bad))
print("S3  non-critical edge exists         : %7d ok, %5d FAIL" % (s3_ok, s3_bad))
for x in s3_fail:
    print("       V=%d %s" % x)
