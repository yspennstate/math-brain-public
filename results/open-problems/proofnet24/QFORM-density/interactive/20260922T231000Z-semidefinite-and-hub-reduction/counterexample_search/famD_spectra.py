"""Family (d), Gaussian (spread) limit: Q = sum_k lam_k sig^2 (Z_k + m_k)^2, Z iid N(0,1), sig^2 = 1/12.
Exact bin masses of each term (erf), FFT convolution, density = mass / h.  Multi-scale spectra.
Also the 3-term reduction: for independent terms sup p_{Q1+Q2} <= sup p_{Q1}; we maximise the 3-term
noncentral density over (ratio lam2, lam3, signs, m) to check that (1,1,-1), m = 0, s = 0 is the maximiser."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, time
from scipy.special import ndtr
from scipy.optimize import minimize
SIG2 = 1/12


def term_mass(edges, th, m=0.0):
    """P(th (Z+m)^2 in [e_i, e_{i+1}))"""
    def cdf(y):
        y = np.asarray(y, float)
        if th > 0:
            r = np.sqrt(np.maximum(y, 0)/th)
            return np.where(y > 0, ndtr(r - m) - ndtr(-r - m), 0.0)
        r = np.sqrt(np.maximum(-y, 0)/(-th))
        return np.where(y < 0, 1 - (ndtr(r - m) - ndtr(-r - m)), 1.0)
    c = cdf(edges)
    return np.diff(c)


def density_spectrum(lams, ms=None, h=2e-4, lo=-12.0, hi=12.0):
    ms = np.zeros(len(lams)) if ms is None else ms
    edges = np.arange(lo, hi + h/2, h); nb = len(edges) - 1
    tot = None; off = 0.0
    L = 1
    while L < nb*len(lams): L *= 2
    F = np.ones(L, complex); shift = 0
    for lam, m in zip(lams, ms):
        pm = term_mass(edges, lam*SIG2, m)
        F *= np.fft.fft(pm, L)
        shift += lo
    conv = np.real(np.fft.ifft(F))
    # the convolution of k terms each on [lo, hi] lives on [k lo, k hi]; bin j <-> start k*lo + j*h
    k = len(lams)
    start = k*lo
    centers = start + (np.arange(L) + 0.5*k)*h
    dens = conv/h
    return centers, dens


if __name__ == "__main__":
    t0 = time.time()
    cases = {
        '(1,1,-1)': [1, 1, -1],
        '(1,1,-1)+(.5,-.5,.25,-.25,.125,-.125)': [1, 1, -1, .5, -.5, .25, -.25, .125, -.125],
        '(1,1,-1)+(2,-2,4,-4)': [1, 1, -1, 2, -2, 4, -4],
        '(1,-1,2,-2,4,-4,8,-8)': [1, -1, 2, -2, 4, -4, 8, -8],
        '(1,1,-1)+40 x (+-.1)': [1, 1, -1] + [0.1, -0.1]*20,
        '(1,1,1)': [1, 1, 1],
        '(1,1,1)+(-.5,-.25,-.125)': [1, 1, 1, -.5, -.25, -.125],
        '(1,1,-1,-1)': [1, 1, -1, -1],
        '(1,1,-2)': [1, 1, -2],
        '(1,2,-1)': [1, 2, -1],
    }
    for name, lams in cases.items():
        c, d = density_spectrum(lams, h=4e-4, lo=-8, hi=8)
        j = int(np.argmax(d))
        print(f"{name:40s} max p = {d[j]:.4f} at s = {c[j]:+.4f}   t={time.time()-t0:.1f}", flush=True)
    print("3 sqrt 2 =", 3*np.sqrt(2), flush=True)
