"""Evaluate Theorem 4.1's closed form for G(r) (Malrieu survey / Benaim-Le Borgne-Malrieu-Zitt) directly."""
import numpy as np
from scipy.integrate import quad
from e0018 import G_of_r
def H(th, r):   # theta in (-pi/2, 0)
    val, _ = quad(lambda y: np.exp(2*r/np.tan(2*y)) / np.cos(y)**2, th, 0.0, limit=200)
    return np.exp(-2*r/np.tan(2*th)) * val
def G_closed(r):
    def integrand_C(x):
        return 1/np.cos(x)**2 + (1/np.sin(x)**2 - 1/np.cos(x)**2) * r * H(x, r)
    Cinv, _ = quad(integrand_C, -np.pi/2, 0.0, limit=200)
    C = 1.0/(4*Cinv)
    def p0(th): return C / np.sin(th)**2 * r * H(th, r)
    def p1(th): return C / np.cos(th)**2 * (1 - r*H(th, r))
    # G = int_0^{2pi} (p0-p1) cos sin ; use the symmetries p_i(th+pi)=p_i(th), p_i(th)=p_{1-i}(th+pi/2)
    # integrate over one quarter (-pi/2,0) and use symmetries: total = 4 * int_{-pi/2}^0 (p0-p1) cos sin   [check numerically vs pi-periodicity]
    val, _ = quad(lambda th: (p0(th)-p1(th))*np.cos(th)*np.sin(th), -np.pi/2+1e-9, -1e-9, limit=200)
    return 4*val
B0 = np.array([[0.,1.],[0.,0.]]); B1 = np.array([[0.,0.],[-1.,0.]])
for r in [0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 4.6, 10.0]:
    try: gc = G_closed(r)
    except Exception as e: gc = float('nan')
    print(f"r={r:5.2f}  closed-form G={gc:+.4f}   finite-volume G={G_of_r(B0,B1,r,1200):+.4f}")
