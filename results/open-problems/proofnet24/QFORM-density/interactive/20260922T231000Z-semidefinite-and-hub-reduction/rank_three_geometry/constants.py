try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from scipy.integrate import quad
F1 = (np.sin(0.5) / 0.5) ** 2
ess = 1 / F1
print(f"Esseen: F(1) = {F1:.6f}, constant 1/F(1) = {ess:.5f}")
a1_light = 4 * ess * np.sqrt(4 * np.pi)
print(f"Lemma A1 light constant (times sqrt(v/A)): {a1_light:.4f}; heavy: 4")
A = 0.5
a1 = a1_light / np.sqrt(A)
print(f"alpha_1(D') <= {a1:.3f} for A >= 1/2")
k_light = 2 * ess * 4 * np.pi
print(f"Lemma X' light: alpha_2 <= {k_light:.3f};  heavy: alpha_2 <= 4*alpha_1 = {4*a1:.3f}")
def Ebound(K):
    # E|Z - s|^{-1/2} <= int_0^inf min(1, phi(v^-2)) dv, phi(u) <= K u (1 + log(1/u)) for u <= 1, <= 1 otherwise
    f = lambda v: min(1.0, K * v ** -2 * (1 + 2 * np.log(v)))
    val = 1.0 + quad(f, 1, 50, limit=400)[0] + quad(f, 50, np.inf, limit=400)[0]
    return val
for K in [k_light, 4 * a1]:
    print(f"K = {K:7.3f}: sup_s E|Z-s|^(-1/2) <= {Ebound(K):.3f};  times sqrt 2 = {np.sqrt(2)*Ebound(K):.2f}")
print(f"definite, linear part in range: 4 sqrt(pi) = {4*np.sqrt(np.pi):.4f}, times sqrt2 = {4*np.sqrt(2*np.pi):.4f}")
print(f"sup_w0 E|W - w0|^-1 for rho_W <= 2: 2 sqrt(2 pi) = {2*np.sqrt(2*np.pi):.4f}")
print(f"Theorem F constant with det G = 1: 12; spherical-mean constant 12/(2 pi) = {12/(2*np.pi):.4f}")
