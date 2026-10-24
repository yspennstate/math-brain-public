try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
from scipy.integrate import quad
# density of |W|^2, W uniform on [-1/2,1/2]^2, at r2 (exact): (1/2) * angular measure of circle radius rho inside square
def p2(r2):
    if r2 <= 0: return 0.0
    rho = np.sqrt(r2)
    if rho <= 0.5: return np.pi
    if rho >= np.sqrt(0.5): return 0.0
    return 0.5*(2*np.pi - 8*np.arccos(0.5/rho))
s = 0.3
g = lambda t: p2(s - t*t)          # partial density of X_1^2 + X_2^2 + X_3^2 at s given X_1 = t
I_int = quad(g, -0.5, 0.5, points=[-np.sqrt(0.05), np.sqrt(0.05)], limit=200)[0]
# top measure-one superlevel set: g is even, equals pi on sqrt(.05) <= |t| <= sqrt(.3), smaller near 0, zero beyond sqrt(.3)
tmax = np.sqrt(0.3); excess = 2*tmax - 1.0          # measure to remove, from the lowest part (around t = 0)
cut = excess/2
I_top = 2*quad(g, cut, tmax, points=[np.sqrt(0.05)], limit=200)[0]
print(f"s = {s}: g(0) = {g(0):.4f}, g(0.3) = {g(0.3):.4f} (= pi on {np.sqrt(0.05):.4f} <= |t| <= {tmax:.4f})")
print(f"  centred interval: {I_int:.5f};  best set [-{tmax:.4f},-{cut:.4f}] u [{cut:.4f},{tmax:.4f}]: {I_top:.5f}")
# best interval at this s (shift c)
best = max((quad(g, c-0.5, c+0.5, points=[x for x in (-tmax,-np.sqrt(.05),np.sqrt(.05),tmax) if c-0.5<x<c+0.5], limit=200)[0], c) for c in np.linspace(0,0.1,101))
print(f"  best shifted interval at this s: {best[0]:.5f} (shift {best[1]:.3f});  sup over s of the density is pi = {np.pi:.5f} at s = 1/4")
