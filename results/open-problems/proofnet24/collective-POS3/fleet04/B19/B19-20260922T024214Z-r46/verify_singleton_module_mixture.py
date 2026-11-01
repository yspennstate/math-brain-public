from itertools import combinations
from collections import defaultdict
from fractions import Fraction


def closure(n, edges):
    rel = [[False] * n for _ in range(n)]
    for a, b in edges:
        rel[a][b] = True
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]:
                        rel[i][j] = True
    assert not any(rel[i][i] for i in range(n))
    return rel


def linext(rel):
    n = len(rel)
    pred = [{i for i in range(n) if rel[i][j]} for j in range(n)]
    out = []
    def rec(prefix, remaining):
        if not remaining:
            out.append(tuple(prefix)); return
        remset = set(remaining)
        for x in remaining:
            if not (pred[x] & remset):
                rec(prefix + [x], [y for y in remaining if y != x])
    rec([], list(range(n)))
    return out


def generated_cases():
    for d in range(3):
        for u in range(3):
            for m in range(1, 4):
                D = list(range(d)); n = d
                C = list(range(d + 1, d + 1 + m))
                U = list(range(d + 1 + m, d + 1 + m + u))
                size = d + 1 + m + u
                D_edges = list(combinations(D, 2)); U_edges = list(combinations(U, 2))
                for dmask in range(1 << len(D_edges)):
                    for umask in range(1 << len(U_edges)):
                        base = [e for i, e in enumerate(D_edges) if dmask >> i & 1]
                        base += [e for i, e in enumerate(U_edges) if umask >> i & 1]
                        base += [(C[i], C[i + 1]) for i in range(m - 1)]
                        base += [(x, c) for x in D for c in C]
                        base += [(x, y) for x in D for y in U]
                        base += [(c, y) for c in C for y in U]
                        for lowmask in range(1 << d):
                            for upmask in range(1 << u):
                                edges = list(base)
                                edges += [(x, n) for i, x in enumerate(D) if lowmask >> i & 1]
                                edges += [(n, y) for i, y in enumerate(U) if upmask >> i & 1]
                                rel = closure(size, edges)
                                if any(rel[n][c] or rel[c][n] for c in C):
                                    continue
                                yield rel, D, n, C, U

case_count = fiber_checks = pair_checks = nc_checks = 0
max_extensions = 0
for rel, D, n, C, U in generated_cases():
    case_count += 1
    extensions = linext(rel); E = len(extensions)
    max_extensions = max(max_extensions, E)
    labels = list(range(len(rel)))
    Q = [x for x in labels if x not in C]
    qrel = [[rel[a][b] for b in Q] for a in Q]
    q_extensions = [tuple(Q[i] for i in tau) for tau in linext(qrel)]
    fibers = defaultdict(int)
    for word in extensions:
        fibers[tuple(x for x in word if x not in C)] += 1
    central = {}
    for tau in q_extensions:
        pos = {x: i for i, x in enumerate(tau)}
        central[tau] = all(pos[d] < pos[n] for d in D) and all(pos[n] < pos[u] for u in U)
        assert fibers[tau] == 1 + len(C) * int(central[tau])
        fiber_checks += 1
    T = len(q_extensions); B = sum(central.values()); m = len(C)
    assert E == T + m * B
    A = sum(any(tau.index(n) < tau.index(d) for d in D) for tau in q_extensions)
    R = sum(any(tau.index(u) < tau.index(n) for u in U) for tau in q_extensions)
    assert A + B + R == T
    full_pos = [{x: i for i, x in enumerate(word)} for word in extensions]
    for s, c in enumerate(C, 1):
        assert sum(pos[n] < pos[c] for pos in full_pos) == A + s * B
        nc_checks += 1
    for x, y in combinations(Q, 2):
        numerator = sum(pos[x] < pos[y] for pos in full_pos)
        X = sum(tau.index(x) < tau.index(y) for tau in q_extensions)
        Y = sum(central[tau] and tau.index(x) < tau.index(y) for tau in q_extensions)
        assert numerator == X + m * Y
        pair_checks += 1

# Shortcut adversary: c1<c2<u and n incomparable with all three.
rel = closure(4, [(1, 2), (2, 3)])
extensions = linext(rel); E = len(extensions)
p_nu = Fraction(sum(word.index(0) < word.index(3) for word in extensions), E)
p_nc2 = Fraction(sum(word.index(0) < word.index(2) for word in extensions), E)
assert E == 4 and p_nu == Fraction(3, 4) and p_nc2 == Fraction(1, 2)

print("cases", case_count)
print("fiber_checks", fiber_checks)
print("pair_mixture_checks", pair_checks)
print("nC_arithmetic_checks", nc_checks)
print("max_extensions", max_extensions)
print("shortcut_example E=4 weighted_Q_Pr(n<u)=3/4 ambient_Pr(n<c2)=1/2")
print("POS3_SINGLETON_MODULE_MIXTURE_CHECK_PASS")
