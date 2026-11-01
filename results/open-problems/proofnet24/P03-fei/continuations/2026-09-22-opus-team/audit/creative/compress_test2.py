import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3])
import numpy as np
n = 4; N = 1 << n
def wht_batch(T):
    a = T.astype(np.float64).copy(); h = 1
    while h < N:
        a = a.reshape(a.shape[0], -1, 2*h); x = a[:, :, :h].copy(); y = a[:, :, h:].copy()
        a[:, :, :h] = x + y; a[:, :, h:] = x - y; a = a.reshape(a.shape[0], N); h *= 2
    return a / N
pc = np.array([bin(s).count('1') for s in range(N)])
def HI(T):
    F = wht_batch(T); P = F*F
    with np.errstate(divide='ignore', invalid='ignore'):
        L = np.where(P > 0, -P*np.log2(P), 0.0)
    return L.sum(1), (P*pc).sum(1)
idx = np.arange(1 << N)
T = 1 - 2*((idx[:, None] >> np.arange(N)) & 1)
H0, I0 = HI(T)
def compress(T, i, up=True):
    lo = np.array([x for x in range(N) if not (x >> i) & 1]); hi = lo | (1 << i)
    C = T.copy(); a = C[:, lo].copy(); b = C[:, hi].copy()
    bad = (a == -1) & (b == 1) if up else (a == 1) & (b == -1)
    C[:, lo] = np.where(bad, -a, a); C[:, hi] = np.where(bad, -b, b)
    return C
for K in (4.0, 6.0, 8.0):
    fails = 0; worst_excess = -1e9
    for i in range(n):
        Hu, Iu = HI(compress(T, i, True)); Hd, Id = HI(compress(T, i, False))
        ex_u = (H0 - Hu) - K*(I0 - Iu); ex_d = (H0 - Hd) - K*(I0 - Id)
        best = np.minimum(ex_u, ex_d)
        # functions already unate in i (both compressions trivial or one trivial) are fine
        fails += int((best > 1e-9).sum()); worst_excess = max(worst_excess, best.max())
    print(f"K={K}: (f,i) pairs where BOTH directions lose more than K*dI: {fails}; worst excess {worst_excess:.4f}")
