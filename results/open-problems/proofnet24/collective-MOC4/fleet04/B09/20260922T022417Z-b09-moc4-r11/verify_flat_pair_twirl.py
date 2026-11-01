from fractions import Fraction as F
from itertools import combinations, permutations, product

U = [
    [F(0),       -F(9,25),     F(12,25),    -F(4,5)],
    [F(12,25),    F(492,625), -F(31,625),   -F(48,125)],
    [F(4,5),     -F(36,125),   F(48,125),    F(9,25)],
    [F(9,25),    -F(256,625), -F(492,625),  -F(36,125)],
]
pairs = list(combinations(range(4), 2))

def dotrow(i, j):
    return sum(U[i][k] * U[j][k] for k in range(4))
assert all(dotrow(i, j) == (1 if i == j else 0) for i in range(4) for j in range(4))

p = [[U[i][j] ** 2 for j in range(4)] for i in range(4)]
def det2(S, T):
    i, j = S; k, ell = T
    return U[i][k] * U[j][ell] - U[i][ell] * U[j][k]
q = {(S, T): det2(S, T) ** 2 for S in pairs for T in pairs}

def swap01(S):
    d = {0: 1, 1: 0, 2: 2, 3: 3}
    return tuple(sorted(d[i] for i in S))

pbar = [row[:] for row in p]
pbar[0] = [(p[0][j] + p[1][j]) / 2 for j in range(4)]
pbar[1] = pbar[0][:]
qbar = {}
for S in pairs:
    Ss = swap01(S)
    for T in pairs:
        qbar[S, T] = q[S, T] if Ss == S else (q[S, T] + q[Ss, T]) / 2

top = (0, 1); bottom = (2, 3)
qtop = {T: qbar[top, T] for T in pairs}
r = {T: qbar[bottom, T] for T in pairs}
x = {(j, k): qtop[tuple(sorted((j, k)))] / 2
     for j in range(4) for k in range(4) if j != k}
for j in range(4):
    assert sum(x[j, k] for k in range(4) if k != j) == pbar[0][j]

edges = pairs
d = {j: pbar[2][j] for j in range(4)}
A = []; rhs = []
for j in range(3):
    row = []; const = F(0)
    for a, b in edges:
        if j == a: row.append(F(1))
        elif j == b: row.append(F(-1)); const += r[(a, b)]
        else: row.append(F(0))
    A.append(row); rhs.append(d[j] - const)

def solve_square(M, b):
    n = len(b); aug = [list(M[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        piv = next((rr for rr in range(c, n) if aug[rr][c]), None)
        if piv is None: return None
        aug[c], aug[piv] = aug[piv], aug[c]
        pv = aug[c][c]; aug[c] = [v / pv for v in aug[c]]
        for rr in range(n):
            if rr != c and aug[rr][c]:
                fac = aug[rr][c]
                aug[rr] = [aug[rr][k] - fac * aug[c][k] for k in range(n + 1)]
    return [aug[i][-1] for i in range(n)]

sol = None
for fixed_idx in combinations(range(6), 3):
    free = [i for i in range(6) if i not in fixed_idx]
    for bits in product((0, 1), repeat=3):
        fixed = {idx: (r[edges[idx]] if bit else F(0)) for idx, bit in zip(fixed_idx, bits)}
        M = []; b = []
        for rr in range(3):
            M.append([A[rr][idx] for idx in free])
            b.append(rhs[rr] - sum(A[rr][idx] * fixed[idx] for idx in fixed))
        vals = solve_square(M, b)
        if vals is None: continue
        cand = [None] * 6
        for idx, val in fixed.items(): cand[idx] = val
        for idx, val in zip(free, vals): cand[idx] = val
        if not all(F(0) <= cand[i] <= r[edges[i]] for i in range(6)): continue
        out = []
        for j in range(4):
            s = F(0)
            for ii, (a, b0) in enumerate(edges):
                if j == a: s += cand[ii]
                elif j == b0: s += r[(a, b0)] - cand[ii]
            out.append(s)
        if all(out[j] == d[j] for j in range(4)):
            sol = cand; break
    if sol is not None: break
assert sol is not None

z = {}
for val, (j, k) in zip(sol, edges):
    z[j, k] = val; z[k, j] = r[(j, k)] - val

mu = {}
for sig in permutations(range(4)):
    J = tuple(sorted(sig[:2])); qJ = qtop[J]
    mu[sig] = F(0) if qJ == 0 else x[sig[0], sig[1]] * z[sig[2], sig[3]] / qJ
assert sum(mu.values()) == 1 and all(w >= 0 for w in mu.values())

Pmu = [[sum(w for sig, w in mu.items() if sig[i] == j) for j in range(4)] for i in range(4)]
assert Pmu == pbar
Qmu = {}
for S in pairs:
    for T in pairs:
        Qmu[S, T] = sum(w for sig, w in mu.items()
                            if tuple(sorted(sig[i] for i in S)) == T)
assert Qmu == qbar

a = [-F(2), F(1, 2), F(3), F(5, 2)]
b = [F(4), -F(1), F(2), F(7, 3)]
allset = set(range(4))
def prodvals(v, S):
    ans = F(1)
    for i in S: ans *= v[i]
    return ans

def qbar_k(S, T):
    S = tuple(sorted(S)); T = tuple(sorted(T)); k = len(S)
    if k in (0, 4): return F(1)
    if k == 1: return pbar[S[0]][T[0]]
    if k == 2: return qbar[S, T]
    i = next(iter(allset - set(S))); j = next(iter(allset - set(T)))
    return pbar[i][j]

lhs = F(0)
for k in range(5):
    for S in combinations(range(4), k):
        Sc = tuple(sorted(allset - set(S)))
        for T in combinations(range(4), k):
            lhs += prodvals(a, Sc) * prodvals(b, T) * qbar_k(S, T)

def vertex(sig):
    ans = F(1)
    for i in range(4): ans *= a[i] + b[sig[i]]
    return ans
rhs = sum(w * vertex(sig) for sig, w in mu.items())
assert lhs == rhs

print('PASS exact orthogonality')
print('PASS twirled one-point marginals')
print('PASS all 36 twirled two-set marginals')
print('PASS 24-state probability law, total =', sum(mu.values()))
print('bottom_orientation =', sol)
print('positive_mu_count =', sum(w > 0 for w in mu.values()))
print('exterior_average =', lhs)
print('permutation_mixture =', rhs)
print('PASS full exterior-power twirl lift')
