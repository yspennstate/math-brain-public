"""Fresh exact check of the round-4 response criterion; no earlier imports."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product, combinations
import os
import resource
import signal
import time

signal.alarm(120)
start = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"


def component(edges, sources):
    seen = set(sources)
    while True:
        enlarged = seen | {v for u, v in edges if u in seen} | {
            u for u, v in edges if v in seen}
        if enlarged == seen:
            return seen
        seen = enlarged


def blocks(edges, terminals):
    return tuple(sorted({tuple(sorted(component(edges, (v,)) & set(terminals)))
                         for v in terminals}))


def open_edges(edges, mask):
    return [edge for i, edge in enumerate(edges) if mask & (1 << i)]


def weight(mask, n, p):
    return p**mask.bit_count() * (1-p)**(n-mask.bit_count())


S = (1, 2, 3)
inside = ((0, 1), (0, 3), (1, 2), (2, 3))
outside = ((1, 4), (4, 5), (5, 2), (3, 6), (6, 7), (5, 6))
pis = {i: blocks(open_edges(inside, i), (0,)+S)
       for i in range(1 << len(inside))}
reference = ((0, 1, 2, 3),)
comparisons = atoms = states = inversions = 0
for p in (Q(1, 4), Q(1, 2), Q(3, 4)):
    a = defaultdict(Q)
    base = {}
    for i, pi in pis.items():
        base[i] = weight(i, len(inside), p)
        a[pi] += base[i]
    runs = []
    for T in ((7,), (5,), (5, 7)):
        h = {}
        direct = defaultdict(Q)
        b = Q(0)
        for j in range(1 << len(outside)):
            oe = open_edges(outside, j)
            w = weight(j, len(outside), p)
            b += w * bool(component(oe, S) & set(T))
            for i, pi in pis.items():
                ie = open_edges(inside, i)
                success = bool(component(ie+oe, (0,)) & set(T))
                # A separate contraction calculation, using only the partition.
                contracted = oe + [(B[0], v) for B in pi for v in B[1:]]
                assert success == bool(component(contracted, (0,)) & set(T))
                direct[i] += base[i]*w*success
                states += 1
        q = sum(direct.values())
        for i, pi in pis.items():
            value = direct[i]/base[i]
            assert pi not in h or h[pi] == value
            h[pi] = value
        r = {pi: value/b for pi, value in h.items()}
        assert r[reference] == 1 and all(0 <= x <= 1 for x in r.values())
        Z = sum(a[pi]*r[pi] for pi in a)
        assert q == b*Z and a[reference] <= Z <= 1
        mu = {i: direct[i]/q for i in pis}
        lam = defaultdict(Q)
        for i, pi in pis.items():
            assert mu[i] == base[i]*r[pi]/Z
            lam[pi] += mu[i]
            atoms += 1
        for pi in a:
            assert r[pi] == a[reference]/a[pi]*lam[pi]/lam[reference]
            inversions += 1
        runs.append((r, mu, lam))
    for (r, mu, lam), (s, nu, gam) in combinations(runs, 2):
        D = sum(a[pi]*abs(r[pi]-s[pi]) for pi in a)
        tv = sum(abs(mu[i]-nu[i]) for i in pis)/2
        assert tv == sum(abs(lam[pi]-gam[pi]) for pi in a)/2
        assert D/(2+1/a[reference]) <= tv <= D/a[reference]
        comparisons += 1

# Check the cubic witness with a degree count, separate from the displayed formula.
def cubic_edges(m):
    V = set(product(range(-m, m+1), repeat=3))
    result = set()
    degree_sum = 0
    for v in V:
        for axis in range(3):
            for step in (-1, 1):
                u = tuple(v[k]+(step if k == axis else 0) for k in range(3))
                if u in V:
                    degree_sum += 1
                    result.add(frozenset((u, v)))
    assert len(result)*2 == degree_sum
    return result

F1, F3 = cubic_edges(1), cubic_edges(3)
assert len(F1) == 54 and len(F3) == 882
assert len(F3-F1)-5 == 823
o, a, b, c = (0,0,0), (1,0,0), (1,1,0), (0,1,0)
oe = [(a,(2,0,0)), ((2,0,0),(2,1,0)), ((2,1,0),b),
      (c,(0,2,0)), ((0,2,0),(0,3,0))]
assert all(frozenset(e) in F3-F1 for e in oe)
assert (0,3,0) not in component([(o,a)]+oe, (o,))
assert (0,3,0) in component([(o,a),(b,c)]+oe, (o,))

print(f"PASS: {states} full-connectivity versus contracted-partition comparisons")
print(f"PASS: {atoms} exact conditional atom laws; {inversions} partition inversions")
print(f"PASS: {comparisons} exact two-sided TV comparisons")
print("PASS: independent cubic degree counts and return-path witness; exponent 823")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
print(f"Priority: {os.getpriority(os.PRIO_PROCESS, 0)}; OMP_NUM_THREADS=1")
print(f"Elapsed seconds: {time.monotonic()-start:.3f}")
print(f"Peak RSS bytes (macOS): {rss}")
print("PASS: round-4 result holds")
