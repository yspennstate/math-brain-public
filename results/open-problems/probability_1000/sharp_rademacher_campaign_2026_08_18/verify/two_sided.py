"""The induction needs TWO bounds. Find whether a natural lower bound closes it.

F(G) = 2F(G-e) - F(G/e)  has a MINUS sign, so
    F(G) <= 2 B(G-e) - L(G/e)
requires an UPPER bound B on F(G-e) and a LOWER bound L on F(G/e). One-sided induction cannot work;
I checked the wrong inequality first and am correcting that here.

Target:  F(G) <= B(G) := 2^{E-V+2b} 3^{V-b}.
Needed:  2 B(G-e) - L(G/e) <= B(G)   for some valid lower bound L <= F.

Candidate lower bounds, all with a reason rather than fitted:
  L_jensen(G) = 2^V * 2^{E/2}          Jensen on the convex map t -> 2^t, since <cut> = E/2
  L_max(G)    = 2^{maxcut} * (#optimal cuts, >= 2)   the aligned configurations alone
  L_bip(G)    = 2 * 2^E for bipartite  (the two aligned configurations cut everything)

This measures, over all small connected graphs:
  - is each candidate actually a valid lower bound for F?      (a violation kills it outright)
  - does 2B(G-e) - L(G/e) <= B(G) hold?                        (this is the induction step)
and reports the worst case for each, so the failure mode is visible rather than just a verdict.
"""
import itertools
import math


def F(V, edges):
    tot = 0
    for bits in range(1 << V):
        c = 0
        for (a, b) in edges:
            if ((bits >> a) ^ (bits >> b)) & 1:
                c += 1
        tot += 1 << c
    return tot


def maxcut_and_count(V, edges):
    best = -1
    cnt = 0
    for bits in range(1 << V):
        c = 0
        for (a, b) in edges:
            if ((bits >> a) ^ (bits >> b)) & 1:
                c += 1
        if c > best:
            best, cnt = c, 1
        elif c == best:
            cnt += 1
    return best, cnt


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


def B(V, edges):
    E = len(edges)
    b = 1 if bipartite(V, edges) else 0
    return (2 ** (E - V + 2 * b)) * (3 ** (V - b))


def L_jensen(V, edges):
    return (2 ** V) * (2 ** (len(edges) / 2.0))


def L_max(V, edges):
    mc, cnt = maxcut_and_count(V, edges)
    return cnt * (2 ** mc)


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


cands = {"jensen": L_jensen, "maxcut": L_max}
valid = {k: [0, 0, None] for k in cands}       # ok, bad, worst
step = {k: [0, 0, None] for k in cands}

for V in range(3, 7):
    alledges = list(itertools.combinations(range(V), 2))
    for mask in range(1, 1 << len(alledges)):
        edges = [alledges[i] for i in range(len(alledges)) if (mask >> i) & 1]
        if len({v for e in edges for v in e}) != V or not connected(V, edges) or len(edges) < 2:
            continue
        f = F(V, edges)
        for name, Lf in cands.items():
            lv = Lf(V, edges)
            if lv <= f + 1e-9:
                valid[name][0] += 1
            else:
                valid[name][1] += 1
                if valid[name][2] is None:
                    valid[name][2] = (V, tuple(edges), f, lv)
        # induction step on the first edge
        Vd, ed = V, [e for i, e in enumerate(edges) if i != 0]
        Vc, ec = contract(V, edges, 0)
        if not ec or not connected(Vd, ed) or not connected(Vc, ec):
            continue
        for name, Lf in cands.items():
            need = 2 * B(Vd, ed) - Lf(Vc, ec)
            if need <= B(V, edges) + 1e-9:
                step[name][0] += 1
            else:
                step[name][1] += 1
                if step[name][2] is None:
                    step[name][2] = (V, tuple(edges), B(V, edges), need)

print("IS THE CANDIDATE A VALID LOWER BOUND (L <= F)?")
for name in cands:
    ok, bad, w = valid[name]
    print("   %-8s ok %6d   VIOLATIONS %5d   %s" % (name, ok, bad, ("first: %s" % (w,)) if w else ""))
print()
print("DOES THE INDUCTION STEP CLOSE:  2B(G-e) - L(G/e) <= B(G) ?")
for name in cands:
    ok, bad, w = step[name]
    print("   %-8s ok %6d   FAILS      %5d   %s" % (name, ok, bad, ("first: %s" % (w,)) if w else ""))
