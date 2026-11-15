# Independent float check of the Q2 report's lemma (4), the two-pair bound (6), formula (3) and the r=2 ratio,
# using direct hitting-time solves only. F_ij = E_i T_j - E_pi T_j, T = max F.
import numpy as np, itertools
rng = np.random.default_rng(7)

def hit(w):
    n = len(w); d = w.sum(1); P = w / d[:, None]; pi = d / d.sum()
    H = np.zeros((n, n))
    for j in range(n):
        idx = [k for k in range(n) if k != j]
        A = np.eye(n - 1) - P[np.ix_(idx, idx)]
        H[idx, j] = np.linalg.solve(A, np.ones(n - 1))
    return H - (pi @ H)[None, :], pi

def quot(w, blocks):
    m = len(blocks); q = np.zeros((m, m))
    for a, A in enumerate(blocks):
        for b, B in enumerate(blocks):
            q[a, b] = w[np.ix_(A, B)].sum()
    return q

def rand_w(n):
    w = np.zeros((n, n))
    for i in range(1, n):
        j = rng.integers(0, i); w[i, j] = w[j, i] = 10.0 ** rng.uniform(-3, 3)
    for _ in range(rng.integers(0, n)):
        i, j = rng.integers(0, n, 2); x = 10.0 ** rng.uniform(-3, 3); w[i, j] += x; w[j, i] += x if i != j else 0
    return w

worst = dict(lem4=-1e9, two_pair=-1e9, ratio=0, f3=0)
for trial in range(400):
    n = int(rng.integers(5, 8)); w = rand_w(n); F, pi = hit(w); t = F.max(1); T = F.max()
    perm = list(rng.permutation(n))
    # one triple
    B = sorted(perm[:3]); rest = perm[3:]; blocks = [B] + [[x] for x in rest]
    Fh, _ = hit(quot(w, blocks)); fb = {x: k + 1 for k, x in enumerate(rest)}
    for j in range(n):
        col = 0 if j in B else fb[j]
        worst['lem4'] = max(worst['lem4'], (Fh[0, col] - t[j]) / T)
    worst['ratio'] = max(worst['ratio'], Fh.max() / T)
    # formula (3) for this partition
    C = np.zeros((n, 2)); C[B[1], 0] = 1; C[B[0], 0] = -1; C[B[2], 1] = 1; C[B[0], 1] = -1
    G = F - F @ C @ np.linalg.solve(C.T @ F @ C, C.T @ F)
    f = {x: (0 if x in B else fb[x]) for x in range(n)}
    err = max(abs(G[i, j] - Fh[f[i], f[j]]) for i in range(n) for j in range(n)) / T
    worst['f3'] = max(worst['f3'], err)
    # two pairs
    A2 = sorted(perm[:2]); B2 = sorted(perm[2:4]); rest = perm[4:]
    blocks = [A2, B2] + [[x] for x in rest]
    Fh, _ = hit(quot(w, blocks))
    worst['two_pair'] = max(worst['two_pair'], max(Fh[0].max(), Fh[1].max()) / T - 2)
    worst['ratio'] = max(worst['ratio'], Fh.max() / T)
print({k: round(v, 9) for k, v in worst.items()})
print('lem4 <= 0, two_pair <= 0, ratio <= 3, f3 ~ 0 expected')
