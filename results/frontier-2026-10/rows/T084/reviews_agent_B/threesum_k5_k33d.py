# T084, agent B: the 3-sum M(K5) (+)3 M*(K3,3) over GF(2) (glue along a triangle, delete it): 13 elements, rank 6.
# M(K5) is a minor (so not cographic), M*(K3,3) is a minor (so not graphic). Then regularity by a TU signing and the adversarial search.
import itertools, numpy as np
def rref2(M):
    M = M.copy() % 2; r = 0; piv = []
    for c in range(M.shape[1]):
        p = next((i for i in range(r, M.shape[0]) if M[i, c]), None)
        if p is None: continue
        M[[r, p]] = M[[p, r]]
        for i in range(M.shape[0]):
            if i != r and M[i, c]: M[i] ^= M[r]
        piv.append(c); r += 1
    return M[:r], piv
def incidence(n_v, edges):
    M = np.zeros((n_v, len(edges)), dtype=np.int64)
    for k, (u, v) in enumerate(edges): M[u, k] = M[v, k] = 1
    return rref2(M)[0]
def dual(M):  # M full row rank r x n -> representation of the dual, (n - r) x n
    R, piv = rref2(M); n = M.shape[1]; free = [c for c in range(n) if c not in piv]
    D = np.zeros((len(free), n), dtype=np.int64)
    for i, f in enumerate(free):
        D[i, f] = 1
        for k, pc in enumerate(piv): D[i, pc] = R[k, f]
    return D
def put_first(M, a, b):  # change basis so columns a, b become e0, e1
    r = M.shape[0]; basis = [M[:, a], M[:, b]]
    for i in range(r):
        e = np.zeros(r, dtype=np.int64); e[i] = 1; T = np.array(basis + [e]).T
        if rref2(T)[0].shape[0] == len(basis) + 1: basis.append(e)
        if len(basis) == r: break
    P = np.array(basis).T  # columns of P = new basis; solve P x = col over GF(2)
    aug = np.concatenate([P, M], axis=1); R, _ = rref2(aug)
    return R[:, r:] % 2
K5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]
M1 = incidence(5, K5); t = [K5.index((0, 1)), K5.index((1, 2)), K5.index((0, 2))]
K33 = [(i, 3 + j) for i in range(3) for j in range(3)]
M2 = dual(incidence(6, K33)); s = [K33.index((0, 3)), K33.index((0, 4)), K33.index((0, 5))]  # vertex star = triangle of the dual
M1 = put_first(M1, t[0], t[1]); M2 = put_first(M2, s[0], s[1])
assert (M1[:, t[2]] == [1, 1, 0, 0]).all() and (M2[:, s[2]] == [1, 1, 0, 0]).all(), (M1[:, t[2]], M2[:, s[2]])
r1, r2 = M1.shape[0], M2.shape[0]; R = r1 + r2 - 2; cols = []
for k in range(M1.shape[1]):
    if k not in t: cols.append(np.concatenate([M1[:, k], np.zeros(r2 - 2, dtype=np.int64)]))
for k in range(M2.shape[1]):
    if k not in s: cols.append(np.concatenate([M2[:2, k], np.zeros(r1 - 2, dtype=np.int64), M2[2:, k]]))
C = np.array(cols).T; n = C.shape[1]; print("elements", n, "rank", rref2(C)[0].shape[0])
# regularity: TU signing of the reduced matrix
Rr, piv = rref2(C); A = Rr[:, [c for c in range(n) if c not in piv]]; ones = [tuple(x) for x in np.argwhere(A)]
def tu(S):
    for k in range(1, min(S.shape) + 1):
        for rr in itertools.combinations(range(S.shape[0]), k):
            for cc in itertools.combinations(range(S.shape[1]), k):
                if abs(round(np.linalg.det(S[np.ix_(rr, cc)]))) > 1: return False
    return True
nr, nc = A.shape; par = list(range(nr + nc)); f = lambda x: x if par[x] == x else f(par[x]); tree = []
for (i, j) in ones:
    a, b = f(i), f(nr + j)
    if a != b: par[a] = b; tree.append((i, j))
free = [e for e in ones if e not in tree]; ok = False
for sg in itertools.product((1, -1), repeat=len(free)):
    S = A.astype(float).copy()
    for e, sgn in zip(free, sg): S[e] = sgn
    if tu(S): ok = True; break
print("free signs", len(free), "TU signing found:", ok, flush=True)
src = open('adversarial_weights.py').read(); exec(src.split("\nK5 = ")[0])
ints = [int(sum(int(C[i, j]) << i for i in range(R))) for j in range(n)]
rk = ranks(ints, n); print("bases", sum(1 for x in range(1 << n) if bin(x).count('1') == R and rk[x] == R), flush=True)
search('K5 (+)3 K33*', rk, n, starts=10)
