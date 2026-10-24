"""Exact quadrature for the Gaussian (spread-leaf) model of a hub with zero diagonal and uniform law on [-1/2,1/2]:
   Q = 2 X_h (Y1 + beta) + R,  R = mu Y1^2 + 2 kap Y1 Y2 + lam Y2^2 + b1 Y1 + b2 Y2 + r0,   Y ~ N(0, sig^2 I_2).
   p(s) = int phi(y1) / (2|y1+beta|) P_{Y2}( |s - R(y1, Y2)| <= |y1 + beta| ) dy1   (exact).
The y1-integral is split at -beta and substituted y1 = -beta +- u^2 (removes the 1/sqrt singularity),
then Gauss-Legendre in u.  Vectorised over s."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
from scipy.special import ndtr
SIG = np.sqrt(1/12)

def _prob_quad_in_window(lam, p, q, lo, hi, sig):
    """P(lo <= lam Y^2 + 2 p Y + q <= hi), Y ~ N(0, sig^2); all arrays broadcast; lam scalar."""
    if abs(lam) < 1e-14:
        # linear: 2 p Y + q in [lo, hi]
        with np.errstate(divide='ignore', invalid='ignore'):
            a = (lo - q)/(2*p); b = (hi - q)/(2*p)
        l = np.minimum(a, b); u = np.maximum(a, b)
        return np.where(p != 0, ndtr(u/sig) - ndtr(l/sig), ((lo <= q) & (q <= hi)).astype(float))
    c = -p/lam; qs = q - p*p/lam              # lam (Y - c)^2 + qs
    L1 = (lo - qs)/lam; L2 = (hi - qs)/lam
    if lam < 0:
        L1, L2 = L2, L1
    r1 = np.sqrt(np.maximum(L1, 0.0)); r2 = np.sqrt(np.maximum(L2, 0.0))
    # Y - c in [r1, r2] or [-r2, -r1]
    P = (ndtr((c + r2)/sig) - ndtr((c + r1)/sig)) + (ndtr((c - r1)/sig) - ndtr((c - r2)/sig))
    return np.where(L2 > 0, P, 0.0)

_gl_x, _gl_w = np.polynomial.legendre.leggauss(400)

def p_hub2(svals, mu, kap, lam, beta, b1, b2, r0=0.0, sig=SIG, umax=None):
    svals = np.atleast_1d(np.asarray(svals, float))
    if umax is None:
        umax = np.sqrt(8*sig + abs(beta))
    u = (_gl_x + 1)/2*umax; wq = _gl_w/2*umax
    out = np.zeros(len(svals))
    for sgn in (+1, -1):
        t = sgn*u*u                      # t = y1 + beta
        y1 = t - beta
        phi = np.exp(-0.5*(y1/sig)**2)/(sig*np.sqrt(2*np.pi))
        p = kap*y1 + b2/2; q = mu*y1*y1 + b1*y1 + r0
        at = np.abs(t)
        lo = svals[:, None] - at[None, :]; hi = svals[:, None] + at[None, :]
        P = _prob_quad_in_window(lam, p[None, :], q[None, :], lo, hi, sig)
        # integrand phi/(2|t|) P dy1, dy1 = 2u du, |t| = u^2 -> phi P / u
        with np.errstate(divide='ignore', invalid='ignore'):
            integ = np.where(u[None, :] > 0, phi[None, :]*P/u[None, :], 0.0)
        out += (integ*wq[None, :]).sum(1)
    return out

if __name__ == "__main__":
    import time
    t0 = time.time()
    sv = np.linspace(-0.3, 0.3, 61)
    v = p_hub2(sv, 0, 0, 1.0, 0, 0, 0)
    print("pure star+rank1: max", v.max(), "at", sv[np.argmax(v)], " p(0)=", p_hub2([0.0], 0, 0, 1, 0, 0, 0)[0], " t", time.time()-t0)
    print("beta=.1:", p_hub2([0.0], 0, 0, 1, 0.1, 0, 0)[0], " lam=2:", p_hub2([0.0], 0, 0, 2, 0, 0, 0)[0])
    for umax in [1.5, 2.0, 3.0]:
        print("umax", umax, p_hub2([0.0, 0.05], 0, 0, 1, 0, 0, 0, umax=umax))
