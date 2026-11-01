"""End-to-end test of the theorem C = 1: for a measure of diameter D, mu box+ S(0,t) is unimodal for
every t >= D^2.

This does not use the level-set criterion at all.  For each random measure of diameter 1 it builds the
density of mu box+ S(0,t) from Biane's description - v_t(u) solves int dmu/((x-u)^2+v^2) = 1/t and the
density at psi_t(u) is v_t(u)/(pi t), with psi_t increasing - counts its modes, and bisects on t for the
least time from which it is unimodal.  Every answer must come out at most 1.
"""
import numpy as np, sys
from scipy.optimize import brentq

def vt(u, x, w, t):
    f = lambda v: (w / ((x - u) ** 2 + v * v)).sum() - 1.0 / t
    if f(1e-12) <= 0: return 0.0
    hi = 1.0
    while f(hi) > 0: hi *= 2
    return brentq(f, 1e-12, hi, xtol=1e-14)

def modes(x, w, t, n=6001):
    u = np.linspace(x.min() - 8, x.max() + 8, n)
    v = np.array([vt(uu, x, w, t) for uu in u])
    k = 0
    for i in range(1, n - 1):
        if v[i] > v[i - 1] and v[i] >= v[i + 1] and v[i] > 1e-9: k += 1
    return k

def tstar(x, w, lo=1e-3, hi=4.0):
    for _ in range(28):
        mid = 0.5 * (lo + hi)
        if modes(x, w, mid) <= 1: hi = mid
        else: lo = mid
    return hi

if __name__ == '__main__':
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 2)
    print("each measure has support of diameter exactly 1, so the theorem says t* <= 1")
    print(f"{'atoms':>6} {'t*':>9} {'<= 1?':>7}   weights")
    worst = 0.0
    for _ in range(trials):
        k = int(rng.integers(2, 6))
        inner = rng.uniform(-0.5, 0.5, max(0, k - 2))
        x = np.concatenate(([-0.5, 0.5], inner))
        w = rng.dirichlet(np.ones(k) * rng.choice([0.4, 1.0, 2.5]))
        t = tstar(x, w)
        worst = max(worst, t)
        print(f"{k:>6} {t:>9.5f} {'yes' if t <= 1.0 + 1e-6 else 'NO':>7}   {np.round(w,3)}", flush=True)
    print(f"\nlargest t* over {trials} random measures of diameter one: {worst:.5f}")
    t = tstar(np.array([-0.5, 0.5]), np.array([0.5, 0.5]))
    print(f"control, the symmetric pair, must be 1: {t:.5f}")
