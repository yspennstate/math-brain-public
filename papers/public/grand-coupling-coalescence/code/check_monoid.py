"""End-to-end check of the argument for Grimmett-Holmes Open Problem 3.8, without the hypergraph.

For a finite set Sigma of maps S -> S (the support of a grand coupling), let M be the monoid it generates and r the
least image size in M (= k(mu) a.s.). If r >= 2, take an idempotent e in M of rank r, W = e(S). Check that for every
g in Sigma, x -> e(g(x)) is a bijection of W, so that sum_{x in W} 1[g(x) in e^{-1}(z0)] = 1 for every z0 in W.
Also check |W| >= 2 and that e^{-1}(z0) is a proper subset.

Usage: python check_monoid.py   (all Sigma of size <= 3 for n = 3; 100000 random Sigma of size 1..4 for n = 4, 5)
"""
import itertools, random


def monoid(gens, n):
    idt = tuple(range(n))
    seen = {idt}
    frontier = [idt]
    while frontier:
        new = []
        for h in frontier:
            for g in gens:
                c = tuple(g[h[x]] for x in range(n))
                if c not in seen:
                    seen.add(c)
                    new.append(c)
        frontier = new
    return seen


def check(gens, n):
    M = monoid(gens, n)
    r = min(len(set(f)) for f in M)
    if r < 2:
        return 0
    e = next(f for f in M if len(set(f)) == r and all(f[f[x]] == f[x] for x in range(n)))
    W = sorted(set(e))
    assert len(W) >= 2
    for g in gens:
        assert len({e[g[x]] for x in W}) == len(W), (gens, e, g)
        for z0 in W:
            Z = {z for z in range(n) if e[z] == z0}
            assert 0 < len(Z) < n
            assert sum(1 for x in W if g[x] in Z) == 1
    return 1


random.seed(1)
n = 3
maps = list(itertools.product(range(n), repeat=n))
hits = tot = 0
for s in range(1, 4):
    for gens in itertools.combinations(maps, s):
        hits += check(gens, n)
        tot += 1
print(f"n=3: {tot} generator sets, {hits} with rank >= 2, all pass")
for n in (4, 5):
    maps = list(itertools.product(range(n), repeat=n))
    hits = 0
    for _ in range(100000):
        gens = random.sample(maps, random.randint(1, 4))
        hits += check(gens, n)
    print(f"n={n}: 100000 random generator sets, {hits} with rank >= 2, all pass")
