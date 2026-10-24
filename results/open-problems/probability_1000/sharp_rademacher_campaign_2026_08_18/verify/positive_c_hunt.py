"""RC only has content where c > 0. So find every linear triangle system with c > 0.

Recall: RC  <=>  c <= beta*(k - d_cb),  c := k*beta - ell,  ell = r - log2|A|.
Since the campaign PROVED d_cb <= k for linear systems, every object with c <= 0 satisfies RC
automatically. The conjecture's entire content lives on {c > 0}.

First sweep (28,200 objects, k<=4): exactly ONE positive value, c/beta = +0.042652, at k=4, r=8 -
the tri-cycle. And |A| = 82 against the independence prediction 2^r (3/4)^k = 81. Trees hit the
prediction EXACTLY (6*3^(k-1) = 2*3^k), which is why c = 0 there.

Working hypothesis to test, not to confirm: c > 0 comes from EVEN cycles in the true sharing
structure, c < 0 from odd ones, and hub-stars (which look like cycles in the intersection graph)
contribute nothing.

So this reports, for every connected linear system it can reach:
    |A| vs the independence prediction, exactly, as an integer difference
    the girth and the parity profile of the TRUE cycle structure
and prints every c > 0 object it finds, with its shape, rather than aggregating them away.

The invariant used for "true cycle structure" is the cycle rank of the BIPARTITE incidence graph
(triangles on one side, shared coordinates on the other), which does NOT create a cycle for a hub
shared by three triangles the way the intersection graph does.
"""
import itertools
import math
import sys
from collections import defaultdict

BETA = math.log2(4.0 / 3.0)
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5
RMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 12


def fibre_size(r, T):
    n = 0
    for s in itertools.product((0, 1), repeat=r):
        ok = True
        for (a, b, c) in T:
            if s[a] == s[b] == s[c]:
                ok = False
                break
        if ok:
            n += 1
    return n


def is_linear(T):
    return all(len(set(t) & set(u)) < 2 for t, u in itertools.combinations(T, 2))


def connected(T):
    seen, frontier = {0}, [0]
    while frontier:
        i = frontier.pop()
        for j in range(len(T)):
            if j not in seen and set(T[i]) & set(T[j]):
                seen.add(j)
                frontier.append(j)
    return len(seen) == len(T)


def bipartite_cycle_rank(T):
    """triangles <-> shared coordinates. A hub in 3 triangles gives a STAR here, not a cycle."""
    cnt = defaultdict(int)
    for t in T:
        for x in t:
            cnt[x] += 1
    shared = [x for x in cnt if cnt[x] >= 2]
    V = len(T) + len(shared)
    E = sum(cnt[x] for x in shared)
    # components of the bipartite graph
    adj = defaultdict(list)
    for i, t in enumerate(T):
        for x in t:
            if cnt[x] >= 2:
                adj[("t", i)].append(("c", x))
                adj[("c", x)].append(("t", i))
    seen, comps = set(), 0
    for node in list(adj):
        if node in seen:
            continue
        comps += 1
        st = [node]
        seen.add(node)
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    st.append(v)
    touched_t = {n[1] for n in seen if n[0] == "t"}
    comps += len(T) - len(touched_t)
    return E - V + comps if V else 0


print("# hunting c > 0.  beta = %.6f" % BETA)
print("# |A|_pred = 2^r (3/4)^k  (independence);  c>0 <=> |A| > |A|_pred")
print()
found = []
examined = 0
for k in range(2, KMAX + 1):
    for r in range(3 * 1, RMAX + 1):
        allt = list(itertools.combinations(range(r), 3))
        if len(allt) > 300:
            continue
        for T in itertools.combinations(allt, k):
            used = {x for t in T for x in t}
            if len(used) != r or not is_linear(T) or not connected(T):
                continue
            examined += 1
            n = fibre_size(r, T)
            pred = (2 ** r) * (3.0 / 4.0) ** k
            if n > pred + 1e-9:
                ell = r - math.log2(n)
                c = k * BETA - ell
                found.append((c / BETA, k, r, n, pred, bipartite_cycle_rank(T), T))

print("objects examined: %d" % examined)
print("objects with c > 0: %d" % len(found))
print()
if found:
    found.sort(reverse=True)
    print("  c/beta      k   r   |A|   pred    bipcyc   shape")
    for cb, k, r, n, pred, bc, T in found[:25]:
        print("  %+.6f  %2d %3d %5d %7.2f %6d   %s" % (cb, k, r, n, pred, bc, T))
    print()
    by = defaultdict(set)
    for cb, k, r, n, pred, bc, T in found:
        by[(k, r)].add(round(cb, 6))
    print("  distinct c/beta by (k, r):")
    for key in sorted(by):
        print("    k=%d r=%d : %s" % (key[0], key[1], sorted(by[key])))
