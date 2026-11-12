"""Search small Cayley graphs (simple, unweighted) for an edge x~xg with H_t(e,g)/H_t(e,e) not monotone in t.
Groups as permutation groups; generating sets = unions of up to 3 inverse classes {g, g^-1}."""
import itertools, sys
import numpy as np

def compose(p, q):  # (p*q)(i) = p(q(i))
    return tuple(p[i] for i in q)

def closure(gens):
    n = len(gens[0]); e = tuple(range(n))
    G = {e}; frontier = [e]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = compose(x, g)
                if y not in G:
                    G.add(y); nf.append(y)
        frontier = nf
    return sorted(G)

def inv(p):
    q = [0]*len(p)
    for i, v in enumerate(p): q[v] = i
    return tuple(q)

def cyc(n, *cycles):
    p = list(range(n))
    for c in cycles:
        for a, b in zip(c, c[1:] + c[:1]): p[a] = b
    return tuple(p)

def dihedral(n):
    r = tuple((i+1) % n for i in range(n)); s = tuple((-i) % n for i in range(n))
    return closure([r, s])

def direct(G1, G2):
    n1 = len(G1[0]); n2 = len(G2[0])
    return sorted(tuple(list(a) + [n1 + v for v in b]) for a in G1 for b in G2)

groups = {}
groups['S3'] = closure([cyc(3, [0, 1]), cyc(3, [0, 1, 2])])
for n in range(4, 13): groups[f'D{n}'] = dihedral(n)
groups['A4'] = closure([cyc(4, [0, 1, 2]), cyc(4, [0, 1], [2, 3])])
groups['S4'] = closure([cyc(4, [0, 1]), cyc(4, [0, 1, 2, 3])])
groups['Q8'] = closure([cyc(8, [0, 1, 2, 3], [4, 5, 6, 7]), cyc(8, [0, 4, 2, 6], [1, 7, 3, 5])])
groups['S3xZ2'] = direct(groups['S3'], closure([cyc(2, [0, 1])]))
groups['S3xZ3'] = direct(groups['S3'], closure([cyc(3, [0, 1, 2])]))
groups['S3xZ4'] = direct(groups['S3'], closure([cyc(4, [0, 1, 2, 3])]))
groups['D4xZ2'] = direct(groups['D4'], closure([cyc(2, [0, 1])]))
groups['Q8xZ3'] = direct(groups['Q8'], closure([cyc(3, [0, 1, 2])]))

ts = np.linspace(0.0, 12.0, 2401)
found = []
for name, G in groups.items():
    idx = {g: i for i, g in enumerate(G)}; N = len(G); e = tuple(range(len(G[0])))
    classes = []
    seen = set()
    for g in G:
        if g == e or g in seen: continue
        c = {g, inv(g)}; seen |= c; classes.append(tuple(sorted(c)))
    for k in (1, 2, 3):
        for combo in itertools.combinations(classes, k):
            S = sorted(set().union(*combo))
            if len(closure(S)) != N: continue
            d = len(S)
            A = np.zeros((N, N))
            for x in G:
                for s in S:
                    A[idx[x], idx[compose(x, s)]] += 1
            L = np.eye(N) - A / d
            w, V = np.linalg.eigh(L)
            ie = idx[e]
            E = np.exp(-np.outer(ts, w))           # T x N
            a = E @ (V[ie] * V[ie])
            worst = 0.0; worst_s = None
            for cl in combo:
                g = cl[0]; ig = idx[g]
                b = E @ (V[ie] * V[ig])
                r = b / a
                dr = np.diff(r).min()
                if dr < worst: worst = dr; worst_s = g
            if worst < -1e-10:
                found.append((name, N, d, [list(c[0]) for c in combo], worst, list(worst_s)))
                print(name, N, d, 'gens', [c[0] for c in combo], 'min step', worst, 'at gen', worst_s, flush=True)
print('done; found', len(found))
