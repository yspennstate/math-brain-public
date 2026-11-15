"""Exact finite audits for PROOF.md; no inference about large Z^3 boxes.

Run: nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py
Uses only the standard library, one thread, and a 120-second alarm.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
import os
import resource
import signal
import time

signal.alarm(120)
started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
STAR = -1


def reached(edges, sources):
    """Breadth-first reachability, independent of the partition implementation."""
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    found = set(sources)
    queue = list(sources)
    for v in queue:
        for w in adj[v]:
            if w not in found:
                found.add(w)
                queue.append(w)
    return found


class Union:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def join(self, u, v):
        self.parent[self.find(u)] = self.find(v)


def partition(edges, terminals, targets=()):
    vertices = set(terminals) | set(targets)
    vertices.update(v for e in edges for v in e)
    uf = Union(vertices)
    for u, v in edges:
        uf.join(u, v)
    for t in targets:
        uf.join(t, STAR)
    names = {}
    code = []
    for t in terminals:
        block = uf.find(t)
        if block not in names:
            names[block] = len(names)
        code.append(names[block])
    return tuple(code)


def kernel(pi, xi, boundary):
    vertices = (0,) + boundary + (STAR,)
    uf = Union(vertices)
    for terminals, code in (((0,) + boundary, pi), (boundary + (STAR,), xi)):
        first = {}
        for v, block in zip(terminals, code):
            if block in first:
                uf.join(first[block], v)
            else:
                first[block] = v
    return int(uf.find(0) == uf.find(STAR))


def mask_edges(edges, mask):
    return tuple(e for j, e in enumerate(edges) if mask & (1 << j))


def mass(mask, count, p):
    k = mask.bit_count()
    return p**k * (1-p)**(count-k)


def tv(left, right):
    return sum(abs(left.get(k, 0)-right.get(k, 0)) for k in left.keys() | right.keys())/2


cases = [
    dict(name="return_square", boundary=(1, 2, 3),
         inside=((0, 1), (0, 3), (1, 2), (2, 3)),
         outside=((1, 4), (4, 5), (5, 2), (3, 6), (6, 7)),
         targets=((7,), (5,), (5, 7))),
    dict(name="two_returns", boundary=(1, 2, 3, 4, 5),
         inside=((0, 1), (0, 3), (2, 3), (0, 5), (4, 5)),
         outside=((1, 6), (6, 2), (3, 7), (7, 4), (5, 8), (8, 9)),
         targets=((9,), (7,), (7, 9))),
    dict(name="hidden_interior_and_multiple_targets", boundary=(1, 3, 4),
         inside=((0, 1), (1, 2), (2, 3), (3, 0), (0, 4)),
         outside=((1, 5), (5, 6), (3, 7), (7, 8), (4, 5), (5, 7)),
         targets=((6,), (8,), (6, 8))),
    dict(name="single_boundary_cycle", boundary=(2,),
         inside=((0, 1), (1, 2)),
         outside=((2, 3), (3, 4), (2, 4)),
         targets=((4,), (3,), (3, 4))),
]

connectivity_checks = atom_checks = partition_checks = comparisons = 0
rows = []


def audit_graph(case, p, target):
    global connectivity_checks, atom_checks, partition_checks
    inside, outside, S = case["inside"], case["outside"], case["boundary"]
    ivertices = {v for edge in inside for v in edge}
    overts = {v for edge in outside for v in edge}
    assert ivertices & overts <= set(S)
    assert not ivertices & set(target)
    assert ivertices <= reached(inside, (0,))
    pis = {i: partition(mask_edges(inside, i), (0,)+S) for i in range(2**len(inside))}
    a_atom = {i: mass(i, len(inside), p) for i in pis}
    a_part = defaultdict(Q)
    for i, pi in pis.items():
        a_part[pi] += a_atom[i]
    reference = (0,)*(len(S)+1)
    astar = a_part[reference]
    assert astar >= p**(len(ivertices)-1)
    h_atom = defaultdict(Q)
    joint_atom = defaultdict(Q)
    rho = defaultdict(Q)
    Hprob = Q(0)
    for e in range(2**len(outside)):
        eedges = mask_edges(outside, e)
        weight = mass(e, len(outside), p)
        xi = partition(eedges, S+(STAR,), target)
        H = bool(reached(eedges, S) & set(target))
        assert H == any(xi[j] == xi[-1] for j in range(len(S)))
        Hprob += weight * H
        if H:
            rho[xi] += weight
        for i, pi in pis.items():
            iedges = mask_edges(inside, i)
            by_bfs = bool(reached(iedges+eedges, (0,)) & set(target))
            by_join = kernel(pi, xi, S)
            assert by_bfs == bool(by_join)
            assert not by_join or H
            h_atom[i] += weight*by_join
            joint_atom[i] += a_atom[i]*weight*by_bfs
            connectivity_checks += 1
    assert Hprob > 0
    rho = {k: v/Hprob for k, v in rho.items()}
    assert sum(rho.values()) == 1
    r_part = {}
    for i, pi in pis.items():
        r = h_atom[i]/Hprob
        assert 0 <= r <= 1
        assert r == sum(kernel(pi, xi, S)*weight for xi, weight in rho.items())
        if pi in r_part:
            assert r_part[pi] == r
        r_part[pi] = r
    assert r_part[reference] == 1
    Z = sum(a_part[pi]*r for pi, r in r_part.items())
    assert astar <= Z <= 1
    q = sum(joint_atom.values())
    assert q == Hprob*Z
    mu_atom = {i: joint_atom[i]/q for i in pis}
    mu_part = defaultdict(Q)
    for i, pi in pis.items():
        assert mu_atom[i] == a_atom[i]*r_part[pi]/Z
        mu_part[pi] += mu_atom[i]
        atom_checks += 1
    assert mu_part[reference] >= astar
    for pi in a_part:
        assert mu_part[pi] == a_part[pi]*r_part[pi]/Z
        assert r_part[pi] == astar/a_part[pi] * mu_part[pi]/mu_part[reference]
        for i in pis:
            if pis[i] == pi and mu_part[pi]:
                assert mu_atom[i]/mu_part[pi] == a_atom[i]/a_part[pi]
        partition_checks += 1
    rows.append((case["name"], str(p), str(target), len(a_part), Hprob, Z, astar))
    return dict(a=a_part, r=r_part, mu=mu_part, atom=mu_atom, rho=rho, astar=astar)


for case in cases:
    for p in (Q(1, 3), Q(1, 2), Q(2, 3)):
        runs = [audit_graph(case, p, target) for target in case["targets"]]
        for left, right in combinations(runs, 2):
            D = sum(left["a"][pi]*abs(left["r"][pi]-right["r"][pi]) for pi in left["a"])
            delta = tv(left["mu"], right["mu"])
            astar = left["astar"]
            assert delta == tv(left["atom"], right["atom"])
            assert D/(2+1/astar) <= delta <= D/astar
            assert D <= tv(left["rho"], right["rho"])
            comparisons += 1

print(f"PASS: {len(rows)} exact graph/parameter/target models")
print(f"PASS: {connectivity_checks} BFS versus partition-join configurations")
print(f"PASS: {atom_checks} conditional atom formulas; {partition_checks} partition mixture/inverse formulas")
print(f"PASS: {comparisons} TV comparisons, disjoint-support equalities and exterior-law bounds")

# Independent stress check of the two normalizations over abstract response
# vectors, including zero coordinates and a small reference weight.
abstract_checks = 0
responses = [(Q(1), x, y) for x, y in product((Q(0), Q(1, 4), Q(1, 2), Q(1)), repeat=2)]
for a in ((Q(1, 100), Q(9, 100), Q(9, 10)), (Q(1, 2), Q(1, 4), Q(1, 4)), (Q(1, 8), Q(3, 8), Q(1, 2))):
    for r, s in product(responses, repeat=2):
        Z = sum(x*y for x, y in zip(a, r))
        W = sum(x*y for x, y in zip(a, s))
        lam = {i: a[i]*r[i]/Z for i in range(3)}
        gam = {i: a[i]*s[i]/W for i in range(3)}
        D = sum(a[i]*abs(r[i]-s[i]) for i in range(3))
        delta = tv(lam, gam)
        assert D/(2+1/a[0]) <= delta <= D/a[0]
        assert abs(Z-W) <= delta/a[0]
        for i in range(3):
            assert r[i] == a[0]/a[i]*lam[i]/lam[0]
        abstract_checks += 1
print(f"PASS: {abstract_checks} independent exact normalization and inverse stress checks")

# The finite lattice witness in PROOF.md, checked in coordinates.
o, a, b, c = (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)
u, v, w, t = (2, 0, 0), (2, 1, 0), (0, 2, 0), (0, 3, 0)
ie0 = ((o, a),)
ie1 = ie0 + ((b, c),)
oe = ((a, u), (u, v), (v, b), (c, w), (w, t))


def radius(vertex):
    return max(abs(x) for x in vertex)


def lattice_box(m):
    vertices = set(product(range(-m, m+1), repeat=3))
    edges = []
    for x in sorted(vertices):
        for j in range(3):
            y = tuple(x[k] + int(j == k) for k in range(3))
            if y in vertices:
                edges.append((x, y))
    return vertices, edges


def edge_key(edge):
    return frozenset(edge)


V1, F1 = lattice_box(1)
V3, F3 = lattice_box(3)
G13 = {edge_key(e) for e in F3} - {edge_key(e) for e in F1}
assert len(F1) == 54 and len(F3) == 882 and len(G13) == 828
assert all(edge_key(e) in G13 for e in oe)
assert all(edge_key(e) in {edge_key(f) for f in F1} for e in ie1)
S1 = {x for x in V1 if radius(x) == 1}
T3 = {x for x in V3 if radius(x) == 3}
assert reached(ie0, (o,)) & S1 == reached(ie1, (o,)) & S1 == {a}
assert not reached(ie0+oe, (o,)) & T3
assert reached(ie1+oe, (o,)) & T3
assert len(oe) == 5
for p in (Q(1, 3), Q(1, 2), Q(2, 3)):
    gap = Q(0)
    for mask in range(2**len(oe)):
        opened = mask_edges(oe, mask)
        e0 = bool(reached(ie0+opened, (o,)) & T3)
        e1 = bool(reached(ie1+opened, (o,)) & T3)
        assert e1 >= e0
        gap += mass(mask, len(oe), p)*(e1-e0)
    # This is conditional on all unlisted exterior edges being closed.
    assert gap == p**5
    # A certified lower bound for the unconditional response gap in B_3.
    assert gap*(1-p)**(len(G13)-5) == p**5*(1-p)**823 > 0
print("PASS: cubic witness: 54 interior edges, 828 exterior edges, 5-edge return pattern")
print("PASS: sparse-witness conditional response gap p^5; full-box lower bound p^5(1-p)^823 > 0")

# Check edge counts and the spanning-tree exponent independently of the
# displayed counting formulas, for several actual cubic boxes.
for m in range(1, 5):
    vertices, edges = lattice_box(m)
    degrees = sum(sum(tuple(x[k]+(step if k == j else 0) for k in range(3)) in vertices
                      for j in range(3) for step in (-1, 1)) for x in vertices)
    assert len(edges) == degrees//2 == 6*m*(2*m+1)**2
    visited = {o}
    tree = []
    adj = defaultdict(list)
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    todo = [o]
    for x in todo:
        for y in adj[x]:
            if y not in visited:
                tree.append((x, y))
                visited.add(y)
                todo.append(y)
    assert visited == vertices
    assert len(tree) == len(vertices)-1 == (2*m+1)**3-1
print("PASS: four cubic edge counts by degree sum; four explicit spanning trees and exponents")

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
print(f"Priority: {os.getpriority(os.PRIO_PROCESS, 0)}; OMP_NUM_THREADS={os.environ['OMP_NUM_THREADS']}")
print(f"Elapsed seconds: {time.monotonic()-started:.3f}")
print(f"Peak RSS bytes (macOS): {rss}")
print("PASS: all exact checks")
