"""Quadrature engine, general form:  p_hub2 with independent anisotropic sigmas, and a Gauss-Hermite outer layer
for extra Gaussian directions Y3.. entering R (couplings to Y1, Y2, own diagonal, linear)."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
from scipy.special import ndtr
from gq import _prob_quad_in_window
SIG = np.sqrt(1/12)
def gl(nq):
    x, w = np.polynomial.legendre.leggauss(nq); return x, w
_GL = {}
def p_hub2g(svals, mu, kap, lam, beta, b1, b2, r0=0.0, s1=SIG, s2=SIG, nq=200):
    """Q = 2 X_h (Y1 + beta) + mu Y1^2 + 2 kap Y1 Y2 + lam Y2^2 + b1 Y1 + b2 Y2 + r0; Y1~N(0,s1^2), Y2~N(0,s2^2);
    X_h uniform[-1/2,1/2].  r0 may be an array (then svals must be scalar-compatible: returns (len(r0), S))."""
    if nq not in _GL: _GL[nq] = gl(nq)
    gx, gw = _GL[nq]
    svals = np.atleast_1d(np.asarray(svals, float))
    umax = np.sqrt(8*s1 + abs(beta))
    u = (gx + 1)/2*umax; wq = gw/2*umax
    r0 = np.atleast_1d(np.asarray(r0, float)); b1 = np.atleast_1d(np.asarray(b1, float)); b2 = np.atleast_1d(np.asarray(b2, float))
    J = max(len(r0), len(b1), len(b2))
    r0 = np.broadcast_to(r0, (J,)); b1 = np.broadcast_to(b1, (J,)); b2 = np.broadcast_to(b2, (J,))
    out = np.zeros((J, len(svals)))
    for sgn in (+1, -1):
        t = sgn*u*u; y1 = t - beta
        phi = np.exp(-0.5*(y1/s1)**2)/(s1*np.sqrt(2*np.pi))
        p = kap*y1[None, :] + b2[:, None]/2                       # (J, U)
        q = mu*y1[None, :]**2 + b1[:, None]*y1[None, :] + r0[:, None]
        at = np.abs(t)
        lo = svals[None, :, None] - at[None, None, :]; hi = svals[None, :, None] + at[None, None, :]
        P = _prob_quad_in_window(lam, p[:, None, :], q[:, None, :], lo, hi, s2)   # (J,S,U)
        with np.errstate(divide='ignore', invalid='ignore'):
            integ = np.where(u > 0, phi/u, 0.0)
        out += (P*(integ*wq)[None, None, :]).sum(2)
    return out

_GH = {}
def gh(m):
    if m not in _GH:
        x, w = np.polynomial.hermite_e.hermegauss(m); _GH[m] = (x, w/np.sqrt(2*np.pi))
    return _GH[m]

def p_hub3(svals, mu, kap, lam, beta, b1, b2, k13, k23, nu, b3, s1=SIG, s2=SIG, s3=SIG, m=24, nq=160):
    """Adds Y3 ~ N(0,s3^2): R += 2 k13 Y1 Y3 + 2 k23 Y2 Y3 + nu Y3^2 + b3 Y3.  Exact in (X_h, Y1, Y2), GH in Y3."""
    x, w = gh(m); y3 = s3*x
    vals = p_hub2g(svals, mu, kap, lam, beta, b1 + 2*k13*y3, b2 + 2*k23*y3, nu*y3*y3 + b3*y3, s1, s2, nq)
    return (w[:, None]*vals).sum(0)

if __name__ == "__main__":
    import time
    t0 = time.time()
    for nq in (60, 120, 200, 400):
        print(nq, p_hub2g([0.0, 0.05, 0.2], 0, 0, 1, 0, 0, 0, nq=nq)[0], flush=True)
    print("k3 pure (k13=k23=nu=0):", p_hub3([0.0, 0.05], 0, 0, 1, 0, 0, 0, 0, 0, 0, 0), time.time()-t0)
    print("k3 nu=.1:", p_hub3([0.0, 0.05], 0, 0, 1, 0, 0, 0, 0, 0, 0.1, 0), time.time()-t0)
