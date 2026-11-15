# structure test for ev_<g>, ec_<g> and eh_k<a>x<b>.
# The group is found here apart from the script's generators: every vertex permutation that keeps the edge set (and,
# for eh, keeps the first side) is listed by brute force and made to act on the edges and the further inputs.
# Checks: every generator is a permutation and lies in that group, the closure of the generators has the same order,
# the class sizes sum to 2^m, the class count equals the Burnside count over every element.  No transform.
import sys
import signal
import itertools
sys.path.insert(0, sys.argv[1])
import sym_search as S

if hasattr(signal, "alarm"):
    signal.alarm(1500)


def cycles(p):
    seen = [False] * len(p); c = 0
    for i in range(len(p)):
        if not seen[i]:
            c += 1; j = i
            while not seen[j]:
                seen[j] = True; j = p[j]
    return c


def graph(g):
    """vertices, edge list, size of the first side (None unless bipartite)"""
    if g == "octa":
        anti = {frozenset((0, 3)), frozenset((1, 4)), frozenset((2, 5))}
        return 6, [e for e in itertools.combinations(range(6), 2) if frozenset(e) not in anti], None
    if "x" in g:
        a, b = (int(t) for t in g[1:].split("x"))
        return a + b, [(i, a + j) for i in range(a) for j in range(b)], a
    n = int(g[1:])
    return n, list(itertools.combinations(range(n), 2)), None


def check(name):
    fam, g = name.split("_")[:2]
    nv, edges, a = graph(g)
    E = len(edges)
    eid = {frozenset(e): i for i, e in enumerate(edges)}
    elems = set()
    for vp in itertools.permutations(range(nv)):
        if any(frozenset((vp[u], vp[v])) not in eid for u, v in edges):
            continue
        if fam == "eh" and any(vp[u] >= a for u in range(a)):
            continue
        ep = [eid[frozenset((vp[u], vp[v]))] for u, v in edges]
        if fam == "ec":
            full = ep + [E + q for q in ep]
        elif fam == "ev":
            full = ep + [E + vp[u] for u in range(nv)]
        else:
            full = ep + [E + vp[u] for u in range(a)]
        elems.add(tuple(full))
    m, gens, sedges = S.struct(name)
    perms = all(sorted(gp) == list(range(m)) for gp in gens)
    ingroup = all(tuple(gp) in elems for gp in gens)
    idt = tuple(range(m)); seen = {idt}; stack = [idt]
    while stack:
        x = stack.pop()
        for gp in gens:
            y = tuple(gp[x[i]] for i in range(m))
            if y not in seen:
                seen.add(y); stack.append(y)
    burn = sum(1 << cycles(p) for p in elems)
    exact = burn % len(elems) == 0
    reps, cls, sizes = S.orbits(m, gens)
    edges_same = {frozenset(e) for e in sedges} == set(eid)
    print("%s m %d classes %d order %d closure %d burnside %d edges %s match %s sum %s perms %s ingroup %s" % (
        name, m, len(reps), len(elems), len(seen), burn // len(elems), edges_same,
        exact and len(reps) == burn // len(elems) and len(seen) == len(elems) and edges_same,
        int(sizes.sum()) == 1 << m, perms, ingroup), flush=True)


for nm in sys.argv[2:]:
    check(nm)
