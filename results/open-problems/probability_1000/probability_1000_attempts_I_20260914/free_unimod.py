"""I0086 (Hasebe and Ueda, Problem 3.3): the optimal constant C with mu box+ S(0,t) unimodal for
every t >= C D^2, D the diameter of the support of mu.

Their Lemma 3.1: mu box+ S(0,t) is unimodal iff for every R > 0 the equation

    xi_R(u) = int dmu(x) / ((x-u)^2 + R^2) = 1/t

has at most two solutions in u.  A level c has three or more solutions exactly when two disjoint
excursions of xi_R rise above it, so the times at which unimodality fails are those with 1/t above some
separating local minimum of some xi_R.  Hence, writing m for the value of a local minimum of xi_R that
has a local maximum on each side,

    t*(mu) = 1 / inf { m : over R > 0 and over separating local minima },

and mu box+ S(0,t) is unimodal exactly for t >= t*(mu).  With the support normalised to diameter one,
C = sup over mu of t*(mu).  Control: the symmetric Bernoulli on {-1,1} must give t* = 4 (their
Example 2.1), and on {-1/2,1/2} must give t* = 1.
"""
import numpy as np

def xi(u, x, w, R):
    u = np.atleast_1d(u)[:, None]
    return (w[None, :] / ((x[None, :] - u) ** 2 + R * R)).sum(axis=1)

def valleys(x, w, R, n=4001):
    """values of the separating local minima of xi_R (those with a local max on each side)"""
    lo, hi = x.min() - 1e-9, x.max() + 1e-9
    u = np.linspace(lo, hi, n)
    y = xi(u, x, w, R)
    out = []
    for i in range(1, n - 1):
        if y[i] <= y[i - 1] and y[i] <= y[i + 1] and (y[i] < y[i-1] or y[i] < y[i+1]):
            if y[:i].max(initial=-1) > y[i] and y[i + 1:].max(initial=-1) > y[i]:
                a, b = u[i - 1], u[i + 1]           # golden refinement of the local min
                for _ in range(80):
                    m1, m2 = a + (b - a) / 3, b - (b - a) / 3
                    if xi(m1, x, w, R)[0] < xi(m2, x, w, R)[0]: b = m2
                    else: a = m1
                out.append(float(xi(0.5 * (a + b), x, w, R)[0]))
    return out

def tstar(x, w, nR=400, Rmax=None):
    x = np.asarray(x, float); w = np.asarray(w, float); w = w / w.sum()
    D = x.max() - x.min()
    if Rmax is None: Rmax = np.sqrt(3) * D
    best = np.inf
    for R in np.linspace(1e-4, Rmax, nR):
        for m in valleys(x, w, R):
            best = min(best, m)
    return np.inf if best == np.inf else 1.0 / best

if __name__ == '__main__':
    print("control, symmetric Bernoulli")
    print("  on {-1,1}     t* =", round(tstar([-1, 1], [.5, .5]), 5), " (paper: 4)")
    print("  on {-1/2,1/2} t* =", round(tstar([-.5, .5], [.5, .5]), 5), " (scaling: 1)")
    print("\ntwo atoms at -1/2, +1/2 with weight p on the left, diameter 1")
    print(f"{'p':>6} {'t*':>9}")
    for p in (0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05):
        print(f"{p:>6.2f} {tstar([-.5, .5], [p, 1 - p]):>9.5f}")
