"""Close the last caveat: does the pair-sum residual space actually satisfy the campaign's valid_R?

My RC chain uses  d_cb <= rank{e_x + e_y : xy in E} = |V| - b.  I established that as a RANK
computation. It is only a bound on d_cb if the span of those pair-sums is an ADMISSIBLE residual
space under the campaign's own definition - `valid_R` in rc_deep_box.py.

Earlier I treated this as blocked because `fast_dcb` searches over C(|cand|, d) subspaces and never
terminates. That framing was wrong: I do not need the SEARCH. `valid_R(D, Rvecs, dim)` tests ONE
candidate space. Checking my construction is a single call per system.

For each test system: build the fibre A, the dual D via the campaign's own full_dual, the pair-sum
space R, and call the campaign's own valid_R. If it returns True then d_cb <= dim R, which is all
the RC chain needs.

Also reports dim R against |V| - b so the rank formula is re-confirmed on the actual objects rather
than on abstract graphs.
"""
import itertools
import math
import sys

SRC = "/srv/aiwork/rc_deep_box.py"
src = open(SRC, encoding="utf-8").read()
cut = src.index('print("dmax = %d"')
ns = {"__name__": "rc_lib", "sys": sys}
exec(compile(src[:cut], SRC, "exec"), ns)
full_dual = ns["full_dual"]
valid_R = ns["valid_R"]
rank_of = ns["rank_of"]
fib = ns["fib"]

BETA = math.log2(4.0 / 3.0)


def cycle_sys(m):
    """m-cycle: shared 0..m-1, private m..2m-1"""
    return [(i, (i + 1) % m, m + i) for i in range(m)], 2 * m


def path_sys(m):
    """tree: a path of m triangles, shared 0..m-1"""
    T = []
    for i in range(m):
        T.append((i, i + 1, m + 1 + i))
    return T, 2 * m + 1


def knn_sys(n):
    """sharing graph K_{n,n}: triangle per edge, one private each"""
    T = []
    p = 2 * n
    for i in range(n):
        for j in range(n):
            T.append((i, n + j, p))
            p += 1
    return T, p


def theta_sys(a, b, c):
    T = []
    nxt = [2]
    def path(L, tag):
        prev = 0
        for i in range(L):
            nx = 1 if i == L - 1 else nxt[0] + 0
            if i != L - 1:
                nxt[0] += 1
            T.append((prev, nx, None))
            prev = nx
    path(a, "a"); path(b, "b"); path(c, "c")
    # assign privates
    base = nxt[0] + 1
    out = []
    for i, (x, y, _) in enumerate(T):
        out.append((x, y, base + i))
    return out, base + len(T)


def pairsum_space(T, r):
    """one pair-sum per triangle: prefer its two SHARED coordinates, else any pair."""
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = {x for x in cnt if cnt[x] >= 2}
    vs = []
    for t in T:
        s = [x for x in t if x in sh]
        pick = (s[0], s[1]) if len(s) >= 2 else (t[0], t[1])
        v = [0] * r
        v[pick[0]] += 1
        v[pick[1]] += 1
        vs.append(v)
    return vs


def bipartite_components_of_sharing_graph(T):
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = {x for x in cnt if cnt[x] >= 2}
    edges = []
    for t in T:
        s = [x for x in t if x in sh]
        if len(s) == 2:
            edges.append(tuple(s))
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    col, comps, bip = {}, 0, 0
    for s0 in adj:
        if s0 in col:
            continue
        comps += 1
        col[s0] = 0
        st, ok = [s0], True
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
    return len(adj), comps, bip


TESTS = []
for m in (3, 4, 5, 6):
    T, r = cycle_sys(m)
    TESTS.append(("%d-cycle" % m, T, r))
for m in (2, 3, 4):
    T, r = path_sys(m)
    TESTS.append(("path of %d triangles" % m, T, r))
for n in (2, 3):
    T, r = knn_sys(n)
    TESTS.append(("K_%d,%d sharing graph" % (n, n), T, r))

print("  system                       r   k   |A|     dimR   |V|-b   valid_R?   d_cb <=")
for name, T, r in TESTS:
    if r > 17:
        print("  %-27s r=%d too big for full_dual" % (name, r))
        continue
    A = fib(r, T)
    D = full_dual(A, r)
    vs = pairsum_space(T, r)
    dimR = rank_of(vs, r)
    V, comps, bip = bipartite_components_of_sharing_graph(T)
    ok = valid_R(D, vs, r)
    print("  %-27s %3d %3d %6d   %4d   %5s   %-8s   %s"
          % (name, r, len(T), len(A), dimR, (V - bip) if V else 0, ok, dimR if ok else "NOT BOUNDED"))
