# (1) the constants of the decision-tree theorem: 4.6355 + Psi(2L-2) <= log2 L + 7.85 and
#     max(8.80, 2(1.0615 + 2/ln2 + Psi(2L-2))) <= 2 log2 L + 14.33 for L >= 1 (grid to 1e9, log-spaced);
# (2) Proposition 6.3: R <= sum_v B_v <= min(H, R + log2(2e) I) for every Boolean function - all monotone functions of
#     at most five variables and 20,000 random (non-monotone) functions of 3..8 variables.
import math, numpy as np
from mono_enum import monotone_masks
C1 = 2 / math.log(2) + 2 * math.exp(-0.5) / math.log(2)
def Psi(r): return math.log2(math.e * (r + 2 * math.sqrt(max(r, 0.0)) + 2))
Ls = np.concatenate([np.linspace(1, 3, 20001), np.exp(np.linspace(math.log(3), math.log(1e9), 20001))])
g1 = max(C1 + Psi(2 * L - 2) - math.log2(L) for L in Ls)
g2 = max(max(8.80, 2 * (1.0615 + 2 / math.log(2) + Psi(2 * L - 2))) - 2 * math.log2(L) for L in Ls)
print('max over L of c(L) - log2 L = %.5f (claim <= 7.85); of C+(L) - 2 log2 L = %.5f (claim <= 14.33)' % (g1, g2))

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

worst = [0.0, 0.0, 0.0]   # violations: R - B, B - H, B - R - log2(2e) I  (all should be <= ~1e-12)
count = 0
for n in range(1, 6):
    masks = monotone_masks(n); N = 1 << n
    tt = ((masks[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(bool)
    H, I, B, R = quantities(tt, n)
    worst = [max(worst[0], (R - B).max()), max(worst[1], (B - H).max()), max(worst[2], (B - R - math.log2(2 * math.e) * I).max())]
    count += len(tt)
rng = np.random.default_rng(3)
ratios = []
for n in range(3, 9):
    tt = rng.random((20000 // 6, 1 << n)) < rng.random((20000 // 6, 1))
    H, I, B, R = quantities(tt, n)
    worst = [max(worst[0], (R - B).max()), max(worst[1], (B - H).max()), max(worst[2], (B - R - math.log2(2 * math.e) * I).max())]
    count += len(tt)
    ok = I > 1e-12
    ratios.append((n, (R[ok] / I[ok]).max(), (B[ok] / I[ok]).max(), (H[ok] / I[ok]).max()))
print('Proposition 6.3 on %d functions: max(R - sumB) = %.2e, max(sumB - H) = %.2e, max(sumB - R - log2(2e) I) = %.2e'
      % (count, worst[0], worst[1], worst[2]))
for r in ratios: print('random functions n=%d: max R/I %.3f, max sumB/I %.3f, max H/I %.3f' % r)
