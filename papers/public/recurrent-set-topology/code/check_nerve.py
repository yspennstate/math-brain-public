"""Check: for random small S in Z^n, the nerve of the cover of R by the polytopes C_V
(V a plane spanned by steps, C_V nonempty) has the same Betti numbers b0, b1 (and b2 = 0)
as the line-plane incidence graph B. Intersections are tested by linear programming on the
defining constraints, independently of the combinatorial description.
Usage: python check_nerve.py [trials] [seed]
"""
import itertools, random, sys
import numpy as np
from scipy.optimize import linprog


def rank(vecs):
    if not vecs:
        return 0
    return int(np.linalg.matrix_rank(np.array(vecs, dtype=float)))


def feasible(v, allowed):
    """Is there a in the simplex with a_i = 0 off `allowed` and sum a_i v_i = 0?"""
    idx = sorted(allowed)
    if not idx:
        return False
    A_eq = [[v[i][k] for i in idx] for k in range(len(v[0]))] + [[1.0] * len(idx)]
    b_eq = [0.0] * len(v[0]) + [1.0]
    r = linprog(np.zeros(len(idx)), A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * len(idx), method="highs")
    return r.status == 0


def in_span(u, basis):
    return rank(basis + [u]) == rank(basis)


def betti_complex(simplices):
    """Betti numbers over Q (via float ranks) of a simplicial complex given by its maximal faces."""
    faces = set()
    for s in simplices:
        s = tuple(sorted(s))
        for k in range(1, len(s) + 1):
            for f in itertools.combinations(s, k):
                faces.add(f)
    by_dim = {}
    for f in faces:
        by_dim.setdefault(len(f) - 1, []).append(f)
    top = max(by_dim) if by_dim else -1
    index = {d: {f: i for i, f in enumerate(sorted(by_dim[d]))} for d in by_dim}
    ranks = {}
    for d in range(1, top + 1):
        M = np.zeros((len(by_dim[d - 1]), len(by_dim[d])))
        for f, j in index[d].items():
            for t in range(len(f)):
                g = f[:t] + f[t + 1:]
                M[index[d - 1][g], j] = (-1) ** t
        ranks[d] = int(np.linalg.matrix_rank(M)) if M.size else 0
    betti = []
    for d in range(0, top + 1):
        n = len(by_dim[d])
        betti.append(n - ranks.get(d, 0) - ranks.get(d + 1, 0))
    return betti


def trial(rng, n, m, box):
    v = [tuple(rng.randint(-box, box) for _ in range(n)) for _ in range(m)]
    if any(all(x == 0 for x in u) for u in v):
        return None
    if rank(list(v)) < 3:
        return None
    # planes spanned by steps: identify a plane by the set of indices whose steps lie in it
    planes = {}
    for i, j in itertools.combinations(range(m), 2):
        if rank([v[i], v[j]]) == 2:
            members = frozenset(k for k in range(m) if in_span(v[k], [v[i], v[j]]))
            planes[members] = True
    planes = [P for P in planes if feasible(v, P)]
    lines = {}
    for i in range(m):
        members = frozenset(k for k in range(m) if in_span(v[k], [v[i]]))
        lines[members] = True
    lines = [L for L in lines if feasible(v, L)]
    # nerve by LP: a family of planes is a simplex iff the intersection of the sets C_P is nonempty
    P = len(planes)
    maximal = []
    simplices = [frozenset([p]) for p in range(P)]
    frontier = list(simplices)
    allsimp = set(simplices)
    while frontier:
        new = []
        for s in frontier:
            for p in range(max(s) + 1, P):
                t = s | {p}
                allowed = frozenset.intersection(*[planes[q] for q in t])
                if feasible(v, allowed):
                    new.append(t)
                    allsimp.add(t)
        frontier = new
    bn = betti_complex([tuple(s) for s in allsimp]) if P else []
    # graph B
    edges = [(("L", a), ("P", b)) for a, L in enumerate(lines) for b, Pl in enumerate(planes) if L <= Pl]
    nodes = [("L", a) for a in range(len(lines))] + [("P", b) for b in range(P)]
    parent = {x: x for x in nodes}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        parent[find(a)] = find(b)
    # components of B that contain at least one plane (a line always lies in a plane when rank >= 3)
    comps = len({find(x) for x in nodes})
    b1_graph = len(edges) - len(nodes) + comps
    b0n = bn[0] if bn else 0
    b1n = bn[1] if len(bn) > 1 else 0
    higher = [b for b in bn[2:] if b != 0]
    ok = (b0n == comps) and (b1n == b1_graph) and not higher
    return ok, v, (b0n, b1n, bn[2:]), (comps, b1_graph), P, len(lines)


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    rng = random.Random(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    done = bad = 0
    stats = {}
    while done < trials:
        n = rng.choice([3, 3, 4])
        m = rng.randint(4, 8)
        r = trial(rng, n, m, rng.choice([1, 1, 2]))
        if r is None:
            continue
        done += 1
        ok, v, nerve, graph, P, L = r
        stats[graph] = stats.get(graph, 0) + 1
        if not ok:
            bad += 1
            print("MISMATCH", v, nerve, graph)
    print("trials", done, "mismatches", bad)
    print("(b0,b1) of B seen:", sorted(stats.items(), key=lambda kv: -kv[1])[:15])
    # the examples from the paper
    ex64 = [(0, 0, 1), (1, 0, 0), (-1, 1, 0), (-1, -1, 0), (0, 0, -1)]
    sym3 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    sym4 = [tuple(s * (1 if k == i else 0) for k in range(4)) for i in range(4) for s in (1, -1)]
    for name, S in [("Example 6.4", ex64), ("+-e_i in Z^3", sym3), ("+-e_i in Z^4", sym4)]:
        res = fixed(S)
        print(name, "nerve betti", res[2], "graph (b0,b1)", res[3])


def fixed(S):
    class Fixed:
        def __init__(self, S):
            self.flat = [x for u in S for x in u]
            self.k = 0

        def randint(self, a, b):
            x = self.flat[self.k]
            self.k += 1
            return x
    return trial(Fixed(S), len(S[0]), len(S), 0)


if __name__ == "__main__":
    main()
