"""Two further checks.
1. Nerve versus graph B on step sets biased towards cycles (steps together with their negatives or
   multiples), n = 3, 4, 5; reports how many trials had b1 > 0 and a balanced line in three or more planes.
2. Components of the transient set R^c, counted on a rational grid of the simplex, against the predicted
   count (0 if every step projects to 0; 2 if the projected steps span a line and lie on both sides of 0;
   1 otherwise). Two grid points of R^c are joined when the open segment between them avoids R: on that
   segment the support is the union of the two supports and the drift moves linearly between the two drifts.
Usage: python check_more.py [nerve_trials] [grid_trials] [seed]
"""
import itertools, random, sys
from fractions import Fraction
import numpy as np
import check_nerve as cn


def biased_steps(rng):
    n = rng.choice([3, 4, 5])
    k = rng.randint(3, min(n + 1, 5))
    base = []
    while len(base) < k:
        u = tuple(rng.randint(-2, 2) for _ in range(n))
        if any(u):
            base.append(u)
    steps = []
    for u in base:
        steps.append(u)
        r = rng.random()
        if r < 0.6:
            steps.append(tuple(-x for x in u))
        elif r < 0.8:
            steps.append(tuple(-2 * x for x in u))
    target = rng.randint(min(len(steps), 9), 9)
    while len(steps) < target:
        u = tuple(rng.randint(-1, 1) for _ in range(n))
        if any(u):
            steps.append(u)
    return steps[:9]


def nerve_part(trials, rng):
    done = bad = cyc = big = 0
    while done < trials:
        S = biased_steps(rng)
        r = cn.fixed(S)
        if r is None:
            continue
        ok, v, nerve, graph, P, L = r
        done += 1
        if not ok:
            bad += 1
            print("MISMATCH", v, nerve, graph)
        if graph[1] > 0:
            cyc += 1
        # a balanced line lying in three or more balanced planes
        lines, planes = lines_planes(S)
        if any(sum(1 for Pl in planes if Lm <= Pl) >= 3 for Lm in lines):
            big += 1
    print(f"nerve: trials {done}, mismatches {bad}, with b1>0 {cyc}, with a line in >=3 planes {big}")


def lines_planes(S):
    m = len(S)
    planes = set()
    for i, j in itertools.combinations(range(m), 2):
        if cn.rank([S[i], S[j]]) == 2:
            planes.add(frozenset(k for k in range(m) if cn.in_span(S[k], [S[i], S[j]])))
    planes = [P for P in planes if cn.feasible(S, P)]
    lines = set(frozenset(k for k in range(m) if cn.in_span(S[k], [S[i]])) for i in range(m) if any(S[i]))
    lines = [L for L in lines if cn.feasible(S, L)]
    return lines, planes


def compositions(N, m):
    for c in itertools.combinations(range(N + m - 1), m - 1):
        prev = -1
        out = []
        for x in c + (N + m - 1,):
            out.append(x - prev - 1)
            prev = x
        yield tuple(out)


def drift(S, a):
    return tuple(sum(a[i] * S[i][k] for i in range(len(S))) for k in range(len(S[0])))


def span_dim(S, supp):
    vs = [S[i] for i in supp if any(S[i])]
    return cn.rank(vs)


def recurrent(S, a):
    supp = [i for i in range(len(S)) if a[i] > 0]
    return all(x == 0 for x in drift(S, a)) and span_dim(S, supp) <= 2


def zero_between(d1, d2):
    """Is 0 on the open segment between d1 and d2 (exact)?"""
    # 0 = (1-t) d1 + t d2 for some 0 < t < 1
    t = None
    for x, y in zip(d1, d2):
        if x == y:
            if x != 0:
                return False
            continue
        tt = Fraction(x, x - y)
        if t is None:
            t = tt
        elif tt != t:
            return False
    if t is None:
        return False  # d1 = d2 = 0 cannot happen for two transient points with the same support span <= 2
    return 0 < t < 1


def rc_components(S, N):
    m = len(S)
    pts = [a for a in compositions(N, m)]
    pts = [a for a in pts if not recurrent(S, a)]
    info = []
    for a in pts:
        supp = frozenset(i for i in range(m) if a[i] > 0)
        info.append((supp, drift(S, a)))
    parent = list(range(len(pts)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for x, y in itertools.combinations(range(len(pts)), 2):
        s = info[x][0] | info[y][0]
        if span_dim(S, s) <= 2 and zero_between(info[x][1], info[y][1]):
            continue
        if span_dim(S, s) <= 2 and all(c == 0 for c in info[x][1]) and all(c == 0 for c in info[y][1]):
            continue
        parent[find(x)] = find(y)
    return len({find(x) for x in range(len(pts))})


def predicted_rc(S):
    nz = [u for u in S if any(u)]
    if not nz:
        return 0
    if cn.rank(nz) == 1:
        # direction of the line; signs of the steps along it
        d = nz[0]
        k = next(i for i, x in enumerate(d) if x != 0)
        signs = {(u[k] > 0) == (d[k] > 0) for u in nz}
        if len(signs) == 2:
            return 2
    return 1


def grid_part(trials, rng):
    done = bad = 0
    seen = {}
    while done < trials:
        n = rng.choice([1, 1, 2, 2, 3])
        m = rng.randint(2, 5)
        S = [tuple(rng.randint(-2, 2) for _ in range(n)) for _ in range(m)]
        N = 6 if m >= 5 else 8
        got = rc_components(S, N)
        want = predicted_rc(S)
        seen[(want, got)] = seen.get((want, got), 0) + 1
        done += 1
        if got != want:
            bad += 1
            print("RC MISMATCH", S, "grid", got, "predicted", want)
    print(f"R^c grid: trials {done}, mismatches {bad}, (predicted, grid) counts {sorted(seen.items())}")


if __name__ == "__main__":
    nt = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    gt = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    rng = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 7)
    nerve_part(nt, rng)
    grid_part(gt, rng)
