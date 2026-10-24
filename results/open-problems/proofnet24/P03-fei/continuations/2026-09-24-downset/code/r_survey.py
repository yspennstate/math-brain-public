# The local form of the conjecture (Proposition 6.3) on monotone functions: R/I, (sum_v B_v)/I and H/I for all monotone
# functions of at most five variables (and six, in chunks) and for families up to 20 variables.
import math, itertools, numpy as np
from mono_enum import monotone_masks
from gdnf import truth_table

def fwht(G):
    N = G.shape[1]; h = 1
    while h < N:
        G = G.reshape(G.shape[0], N // (2 * h), 2, h)
        a = G[:, :, 0, :].copy(); b = G[:, :, 1, :]
        G[:, :, 0, :] = a + b; G[:, :, 1, :] = a - b
        G = G.reshape(G.shape[0], N); h *= 2
    return G / N

def quantities(tt, n):
    N = 1 << n
    P = fwht(np.where(tt, -1.0, 1.0)) ** 2
    x = np.arange(N); pc = np.array([bin(t).count('1') for t in range(N)])
    def phi(p): return np.where(p > 1e-300, -p * np.log2(np.where(p > 1e-300, p, 1)), 0.0)
    H = phi(P).sum(1); I = (P * pc).sum(1)
    B = np.zeros(len(tt)); R = np.zeros(len(tt))
    for v in range(n):
        low = x[((x >> v) & 1) == 0]; up = low | (1 << v)
        X = P[:, low]; Y = P[:, up]
        B += (phi(X) + phi(Y) - phi(X + Y)).sum(1)
        with np.errstate(divide='ignore', invalid='ignore'):
            lr = np.where((Y > 1e-300) & (X > 1e-300), np.log2(np.where(X > 1e-300, X, 1) / np.where(Y > 1e-300, Y, 1)), 0.0)
        R += (Y * np.maximum(lr, 0.0)).sum(1)
    return H, I, B, R

def show(name, n, f):
    H, I, B, R = quantities(f[None, :], n)
    print('%-28s n=%2d  R/I %.3f  sumB/I %.3f  H/I %.3f' % (name, n, R[0] / I[0], B[0] / I[0], H[0] / I[0]), flush=True)
    return R[0] / I[0]

best = 0.0
for n in range(1, 7):
    masks = monotone_masks(n); N = 1 << n
    mx = [0.0, 0.0, 0.0]
    for c in range(0, len(masks), 200000):
        tt = ((masks[c:c + 200000, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(bool)
        H, I, B, R = quantities(tt, n)
        ok = I > 1e-12
        mx = [max(mx[0], (R[ok] / I[ok]).max()), max(mx[1], (B[ok] / I[ok]).max()), max(mx[2], (H[ok] / I[ok]).max())]
    best = max(best, mx[0])
    print('all monotone n=%d (%d fns): max R/I %.3f, max sumB/I %.3f, max H/I %.3f' % (n, len(masks), *mx), flush=True)

def maj(n):
    x = np.arange(1 << n); return np.array([bin(t).count('1') for t in x]) > n // 2
def thr(n, t):
    x = np.arange(1 << n); return np.array([bin(t2).count('1') for t2 in x]) >= t
def g_example(n):   # Maj_n(y) or (z and y = y*), y* with (n-1)/2 ones; z is coordinate n
    N = 1 << (n + 1); x = np.arange(N); y = x & ((1 << n) - 1); z = (x >> n) & 1
    pcy = np.array([bin(t).count('1') for t in y]); ystar = (1 << ((n - 1) // 2)) - 1
    return (pcy > n // 2) | ((z == 1) & (y == ystar))
fam = []
for m in (4, 6, 8, 10): fam.append(('matching%d' % m, 2 * m, truth_table(2 * m, [(2 * i, 2 * i + 1) for i in range(m)])))
for k in (3, 4):
    for t in (3, 4):
        fam.append(('tribes %dx%d' % (k, t), k * t, truth_table(k * t, [tuple(range(i * t, (i + 1) * t)) for i in range(k)])))
for n in (7, 11, 15, 19): fam.append(('majority%d' % n, n, maj(n)))
for n in (12, 16): fam.append(('threshold%d>=%d' % (n, n // 2 + 2), n, thr(n, n // 2 + 2)))
for n in (7, 11, 15): fam.append(('Remark6.1 g_%d' % n, n + 1, g_example(n)))
E6 = list(itertools.combinations(range(6), 2))
tri = [tuple(E6.index(e) for e in itertools.combinations(T, 2)) for T in itertools.combinations(range(6), 3)]
fam.append(('K6 contains triangle', 15, truth_table(15, tri)))
E5 = list(itertools.combinations(range(5), 2))
fam.append(('K5 contains triangle', 10, truth_table(10, [tuple(E5.index(e) for e in itertools.combinations(T, 2)) for T in itertools.combinations(range(5), 3)])))
fam.append(('K16 2-DNF (K_16 edges)', 16, truth_table(16, list(itertools.combinations(range(16), 2)))))
for name, n, f in fam: best = max(best, show(name, n, f))
print('largest R/I: %.3f' % best)
