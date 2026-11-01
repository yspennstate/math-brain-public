"""Randomized checks of Proposition 6.4, Remark 8.2 and Theorem 1.1 of the five-eigenvalue paper.

P64: for no-pivot matrices with s_{2m-1}(A) >= 1 (m = 2, 3), a sign vector with ||Q_eps||_F^2 below the
     exact mean exists, and its partition has s_m(A_IJ) > gamma_m and E_m(A_IJ) > gamma_m^(2m).
R82: the two-star matrix has no pivot, rank-two cut blocks for every sampled partition, and the density
     of Q = X^T A X stays below 4 sqrt(e).
T11: Monte Carlo density of Q for matrices with s_5(A) = 1 stays far below 270.
"""
import math
import sys
import functools
print = functools.partial(print, flush=True)

import numpy as np

rng = np.random.default_rng(20260925)
ETA, ZETA = 1 / 12, 1 / 256
GAMMA = {m: (44 - 5 * math.sqrt(2) * (2 * m - 1)) / 96 for m in (1, 2, 3)}


def no_pivot(A):
    d = np.diag(A)
    if np.max(np.abs(d)) >= ETA:
        return False
    M = np.outer(d, d) - A * A
    np.fill_diagonal(M, 0)
    return np.max(np.abs(M)) < ZETA


def elem_sym(vals, m):
    e = np.zeros(m + 1)
    e[0] = 1
    for v in vals:
        for j in range(m, 0, -1):
            e[j] += e[j - 1] * v
    return e[m]


def best_cut(A, k, trials=300):
    w, V = np.linalg.eigh(A)
    idx = np.argsort(-np.abs(w))[:k]
    lam, Phi = w[idx], V[:, idx]
    O = A - np.diag(np.diag(A))
    nrm2 = np.sum(Phi ** 2, axis=1)
    G = Phi @ Phi.T
    EQ = float(np.sum((O ** 2) * (np.outer(nrm2, nrm2) + G ** 2)))
    best = None
    for _ in range(trials):
        eps = rng.choice([-1.0, 1.0], size=A.shape[0])
        Q = (Phi * eps[:, None]).T @ O @ (Phi * eps[:, None])
        q = float(np.sum(Q * Q))
        if best is None or q < best[0]:
            best = (q, eps)
    return lam, EQ, best


def check_p64(A, name, ms=(2, 3)):
    assert no_pivot(A), name
    s = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
    out = []
    for m in ms:
        k = 2 * m - 1
        if s[k - 1] < 1 - 1e-12:
            continue
        lam, EQ, (q, eps) = best_cut(A, k)
        a = np.max(np.abs(A - np.diag(np.diag(A))))
        assert EQ <= 2 * a * a * k * k + 1e-12
        assert q <= EQ + 1e-12, (name, q, EQ)
        I = eps > 0
        M = A[np.ix_(I, ~I)]
        sv = np.linalg.svd(M, compute_uv=False)
        sm = sv[m - 1] if len(sv) >= m else 0.0
        Em = elem_sym(sv ** 2, m)
        ok = sm > GAMMA[m] and Em > GAMMA[m] ** (2 * m)
        out.append(ok)
        print(f"  {name:34s} n={A.shape[0]:4d} m={m} s_k(A)={s[k-1]:.3f} max|a_ij|={a:.4f} "
              f"E||Q||^2={EQ:.4f} chosen={q:.4f} s_m(A_IJ)={sm:.4f} > {GAMMA[m]:.4f}  E_m={Em:.3e} "
              f"> {GAMMA[m]**(2*m):.3e}  {'PASS' if ok else 'FAIL'}")
    return out


def scale_to(A, k):
    s = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
    return A / s[k - 1]


results = []
print('P64 random spread matrices (no pivot enforced):')
for trial in range(12):
    n = int(rng.choice([400, 600, 900]))
    r = int(rng.integers(5, 12))
    U = np.linalg.qr(rng.standard_normal((n, r)))[0]
    lam = rng.choice([-1, 1], r) * rng.uniform(1, 2.5, r)
    A = U @ np.diag(lam) @ U.T
    A = scale_to(A, 5)
    A = A - np.diag(np.diag(A)) + np.diag(rng.uniform(-0.02, 0.02, n))
    A = scale_to(A, 5)
    if no_pivot(A):
        results += check_p64(A, f'spread r={r}')
    else:
        print(f'  spread n={n} r={r}: skipped (has a pivot after scaling)')
print('P64 structured matrices:')


def stars(nh, N, extra=None):
    # equal-magnitude weights +-N^(-1/2): every 2x2 principal minor is at most 1/N < zeta when N > 256
    n = nh * (N + 1)
    A = np.zeros((n, n))
    for h in range(nh):
        c = h * (N + 1)
        w = rng.choice([-1.0, 1.0], size=N) / math.sqrt(N)
        A[c, c + 1:c + 1 + N] = w
        A[c + 1:c + 1 + N, c] = w
    return A


A = stars(3, 700)
results += check_p64(A, 'three stars (s_6 = 1)')
# two stars plus a spread rank-one piece
n = 2 * 701
A = stars(2, 700)
u = rng.standard_normal(n)
u /= np.linalg.norm(u)
A = A + 1.2 * np.outer(u, u)
A = A - np.diag(np.diag(A))
A = scale_to(A, 5)
if no_pivot(A):
    results += check_p64(A, 'two stars + rank one')
else:
    print('  two stars + rank one: skipped (pivot)')
# hub plus trigonometric leaves (rank five), t = 1
m_ = 1601
th = 2 * np.pi * np.arange(m_) / m_
l = np.ones(m_) / math.sqrt(m_)
v, p = math.sqrt(2 / m_) * np.cos(2 * th), math.sqrt(2 / m_) * np.sin(2 * th)
w, z = math.sqrt(2 / m_) * np.cos(th), math.sqrt(2 / m_) * np.sin(th)
n = m_ + 1
E = lambda x: np.concatenate([[0.0], x])
h = np.zeros(n)
h[0] = 1
L_, V_, P_, W_, Z_ = map(E, (l, v, p, w, z))
A = (np.outer(h, L_) + np.outer(L_, h) + 1e-3 * (np.outer(L_, P_) + np.outer(P_, L_))
     + np.outer(V_, V_) + np.outer(W_, W_) - np.outer(Z_, Z_))
A = A - np.diag(np.diag(A)) + np.diag(np.diag(A)).clip(-0.05, 0.05)
A = scale_to(A, 5)
results += check_p64(A, 'hub + trigonometric leaves')
# a hub, a large-diagonal coordinate and a spread rank-two part
n = 900
u1, u2 = np.linalg.qr(rng.standard_normal((n, 2)))[0].T
A = 2.0 * np.outer(u1, u1) - 1.5 * np.outer(u2, u2)
wv = rng.standard_normal(n)
wv[0] = 0
wv /= np.linalg.norm(wv)
A[0, :] += 1.3 * wv
A[:, 0] += 1.3 * wv
q = rng.standard_normal(n)
q /= np.linalg.norm(q)
A += 1.1 * np.outer(q, q)
A = A - np.diag(np.diag(A))
A = scale_to(A, 5)
if no_pivot(A):
    results += check_p64(A, 'hub + rank three')
else:
    print('  hub + rank three: skipped (pivot)')

print('R82 two stars:')
N = 400
w = np.ones(N) / math.sqrt(N)
n = 2 * (N + 1)
A = np.zeros((n, n))
for c in (0, N + 1):
    A[c, c + 1:c + 1 + N] = w
    A[c + 1:c + 1 + N, c] = w
ev = np.sort(np.linalg.eigvalsh(A))
ok_spec = np.allclose(ev[[0, 1, -2, -1]], [-1, -1, 1, 1]) and np.max(np.abs(ev[2:-2])) < 1e-9
ok_np = no_pivot(A)
ranks = []
for _ in range(200):
    eps = rng.choice([-1.0, 1.0], size=n)
    I = eps > 0
    ranks.append(np.linalg.matrix_rank(A[np.ix_(I, ~I)], tol=1e-10))
ok_rank = max(ranks) <= 2
# density of Q = 2 U1 L1 + 2 U2 L2 with uniform[0,1] coordinates
S = 2_000_000
X = rng.uniform(0, 1, size=(S, 2))
Lk = rng.uniform(0, 1, size=(S, 2, N)) if False else None
# L_k = w . V_k with V_k uniform on [0,1]^N: exact law is the Irwin-Hall sum scaled by 1/sqrt(N); simulate by the
# sum of N uniforms in chunks
Lsum = np.zeros((S, 2))
for _ in range(N):
    Lsum += rng.uniform(0, 1, size=(S, 2))
L = Lsum / math.sqrt(N)
Qs = 2 * X[:, 0] * L[:, 0] + 2 * X[:, 1] * L[:, 1]
hist, edges = np.histogram(Qs, bins=4000)
dens = hist / (S * (edges[1] - edges[0]))
ok_dens = dens.max() < 4 * math.sqrt(math.e)
print(f"  spectrum +-1 twice: {ok_spec}; no pivot: {ok_np}; max cut rank over 200 partitions: {max(ranks)}; "
      f"max empirical density {dens.max():.4f} < 4 sqrt(e) = {4*math.sqrt(math.e):.4f}: {ok_dens}")
results += [ok_spec, ok_np, ok_rank, ok_dens]

print('T11 Monte Carlo densities with s_5(A) = 1:')
for name, gen in [('no pivot spread', 'spread'), ('diagonal pivot', 'diag'), ('pair pivot', 'pair')]:
    n = 12
    U = np.linalg.qr(rng.standard_normal((n, 5)))[0]
    A = U @ np.diag(rng.choice([-1, 1], 5)) @ U.T
    if gen == 'diag':
        A[0, 0] += 0.5
    if gen == 'pair':
        A[0, 1] += 0.4
        A[1, 0] += 0.4
    A = scale_to(A, 5)
    S = 2_000_000
    Xs = rng.uniform(0, 1, size=(S, n))
    b = rng.standard_normal(n)
    Qs = np.einsum('si,ij,sj->s', Xs, A, Xs, optimize=True) + Xs @ b
    hist, edges = np.histogram(Qs, bins=2000)
    dens = hist / (S * (edges[1] - edges[0]))
    ok = dens.max() < 270
    results.append(ok)
    print(f"  {name:18s} max empirical density {dens.max():.3f} < 270: {ok}")
print('ALL PASS' if all(results) else 'SOME FAIL', f'({sum(map(bool, results))}/{len(results)})')
sys.exit(0 if all(results) else 1)
