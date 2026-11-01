# Direct check: g = [w.x >= 921] with the 14 weights below; f_l = AND of l fresh variables with g (a threshold function).
# Compute H(f_l), I(f_l) from an exact integer Walsh transform and mpmath logs; no use of the recursion.
import numpy as np, mpmath as mp, psutil
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); psutil.Process().cpu_affinity(list(range(2, psutil.cpu_count())))
mp.mp.dps = 30
w = [1000, 595, 354, 211, 125, 75, 44, 26, 15, 9, 5, 3, 1, 1]; theta = 921
def walsh_int(F):
    a = F.astype(np.int64).copy(); h = 1
    while h < len(a):
        a = a.reshape(-1, 2*h); a = np.concatenate([a[:, :h]+a[:, h:], a[:, :h]-a[:, h:]], axis=1).reshape(-1); h *= 2
    return a
def HI_exact(f, n):
    N = 1 << n
    a = walsh_int(np.where(f, -1, 1))          # a = N * Fhat, integers
    pc = np.array([bin(i).count("1") for i in range(N)], dtype=np.int64) if n <= 16 else None
    vals, counts = np.unique(np.abs(a[a != 0]), return_counts=True)
    H = mp.mpf(0)
    for v, c in zip(vals.tolist(), counts.tolist()):
        p = mp.mpf(v)**2 / mp.mpf(N)**2
        H += c * p * mp.log(1/p, 2)
    # I = sum |S| a_S^2 / N^2 ; compute popcount weights blockwise to save memory
    I_num = 0
    idx = np.arange(N, dtype=np.int64)
    pcs = np.zeros(N, dtype=np.int64)
    for b in range(n): pcs += (idx >> b) & 1
    I_num = int((pcs * (a.astype(np.int64)**2)).sum())
    return H, mp.mpf(I_num) / mp.mpf(N)**2
n0 = len(w)
X = ((np.arange(1 << n0)[:, None] >> np.arange(n0)) & 1)
g = (X @ np.array(w)) >= theta
H0, I0 = HI_exact(g, n0)
print("g: n=14 P =", g.mean(), " H =", mp.nstr(H0, 15), " I =", mp.nstr(I0, 15), " D = 4I-H =", mp.nstr(4*I0 - H0, 15))
for l in range(1, 9):
    n = n0 + l; N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    low = idx & ((1 << n0) - 1); high = idx >> n0
    f = g[low] & (high == (1 << l) - 1)          # AND of the l new variables with g
    H, I = HI_exact(f, n)
    print(f"l={l} n={n} P={f.mean():.3e}  H/I = {mp.nstr(H/I, 12)}   4I - H = {mp.nstr(4*I - H, 12)}")
