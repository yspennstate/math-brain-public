# Does an i-compression lose at most K times the influence it removes?  H(f)-H(C_i f) <= K (I(f)-I(C_i f)) ?
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3])
import numpy as np, math
n = 4; N = 1 << n
def wht_batch(T):  # T: (M, N) +-1 float
    a = T.astype(np.float64).copy(); h = 1
    while h < N:
        a = a.reshape(a.shape[0], -1, 2*h)
        x = a[:, :, :h].copy(); y = a[:, :, h:].copy()
        a[:, :, :h] = x + y; a[:, :, h:] = x - y
        a = a.reshape(a.shape[0], N); h *= 2
    return a / N
pc = np.array([bin(s).count('1') for s in range(N)])
def HI(T):
    F = wht_batch(T); P = F*F
    with np.errstate(divide='ignore', invalid='ignore'):
        L = np.where(P > 0, -P*np.log2(P), 0.0)
    return L.sum(1), (P*pc).sum(1)
idx = np.arange(1 << N)
T = 1 - 2*((idx[:, None] >> np.arange(N)) & 1)        # all 65536 functions, entry x -> f(x); -1 = TRUE
H0, I0 = HI(T)
worst = -1e9; worst_zero = -1e9; examples = []
for i in range(n):
    lo = np.array([x for x in range(N) if not (x >> i) & 1]); hi = lo | (1 << i)
    C = T.copy()
    a = C[:, lo].copy(); b = C[:, hi].copy()
    # monotone in TRUE: TRUE (-1) must not sit at x_i = FALSE while FALSE (+1) sits at x_i = TRUE
    bad = (a == -1) & (b == 1)
    C[:, lo] = np.where(bad, 1, a); C[:, hi] = np.where(bad, -1, b)
    H1, I1 = HI(C)
    dH = H0 - H1; dI = I0 - I1
    assert np.all(dI >= -1e-12), "compression raised influence?"
    zero = dI < 1e-12
    if np.any(zero): worst_zero = max(worst_zero, dH[zero].max())
    ratio = np.where(~zero, dH/np.where(zero, 1, dI), -np.inf)
    k = int(np.argmax(ratio)); 
    if ratio[k] > worst: worst = ratio[k]; examples.append((i, k, dH[k], dI[k], H0[k], I0[k]))
print(f"n={n}: max over f,i with dI>0 of (H(f)-H(Cf))/(I(f)-I(Cf)) = {worst:.4f}")
print(f"       max dH when dI = 0: {worst_zero:.3e}")
print("worst example (i, f-index, dH, dI, H(f), I(f)):", examples[-1])
