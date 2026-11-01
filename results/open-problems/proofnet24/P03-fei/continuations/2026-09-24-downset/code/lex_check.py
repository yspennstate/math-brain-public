# R/I, sum_v B_v / I and H/I for lexicographic threshold functions f(x) = [x read as a binary number >= t]
# (monotone; Hod's family for lower bounds on the FEI constant), over many thresholds t.
import sys, numpy as np
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

def lex_tt(n, t):
    N = 1 << n; x = np.arange(N)
    val = np.zeros(N, dtype=np.int64)
    for j in range(n): val = val * 2 + ((x >> j) & 1)      # coordinate 0 is the most significant bit
    return val >= t
rng = np.random.default_rng(5)
for n in (10, 12, 14, 16):
    N = 1 << n
    ts = sorted(set([int(v) for v in rng.integers(1, N, size=400 if n < 16 else 150)] +
                    [int(round(N * a)) for a in (1/3, 2/3, 1/5, 2/5, 3/7, 0.2927, 0.618, 0.382)]))
    best = {'R': (0, 0), 'B': (0, 0), 'H': (0, 0)}
    for c in range(0, len(ts), 50):
        chunk = ts[c:c + 50]
        tt = np.array([lex_tt(n, t) for t in chunk])
        H, I, B, R = quantities(tt, n)
        for k, arr in (('R', R / I), ('B', B / I), ('H', H / I)):
            i = int(np.argmax(arr))
            if arr[i] > best[k][0]: best[k] = (float(arr[i]), chunk[i])
    print('n=%2d, %d thresholds: max R/I %.3f (t/N=%.4f), max sumB/I %.3f, max H/I %.3f (t/N=%.4f)'
          % (n, len(ts), best['R'][0], best['R'][1] / N, best['B'][0], best['H'][0], best['H'][1] / N), flush=True)
