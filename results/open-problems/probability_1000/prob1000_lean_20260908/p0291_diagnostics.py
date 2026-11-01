"""P0291 proof-route diagnostics for the symmetric star chain (see p0291_star_sm_lp.py).
(A) single-gap monotonicity: is (X_0, X_g, X_{g+h}) >=_sm (X_0, X_{g'}, X_{g'+h}) for g < g' (h fixed)?  and the
    same with the LAST gap varied.  If yes, the proof can go gap by gap.
(B) does conditioning on two interior coordinates preserve supermodularity?  For n = 3 and Phi(x,y) =
    sum_z P_h(y,z) phi(x,y,z): search (LP) for a supermodular phi on {1,2,3}^3 with Phi NOT supermodular.
(C) the same for the 4-state lift (Y, W): center-with-last-coin states, to see whether a monotone lift exists.
"""
import itertools
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog
from p0291_star_sm_lp import star, fdd, sm_gap, stationary

def test_single_gap(Q, name):
    print(f"== (A) single-gap monotonicity, {name}")
    worst = -1
    for h in (0.3, 1.0, 3.0):
        for g1, g2 in ((0.2, 0.4), (0.4, 0.8), (0.8, 1.6), (1.6, 3.2)):
            for which in ("first", "last"):
                t1 = [0.0, g1, g1 + h] if which == "first" else [0.0, h, h + g1]
                t2 = [0.0, g2, g2 + h] if which == "first" else [0.0, h, h + g2]
                gap, _, _ = sm_gap(fdd(Q, t1, 1.0), fdd(Q, t2, 1.0))
                worst = max(worst, gap)
                if gap > 1e-9: print(f"   VIOLATION h={h} {which} gap {g1}->{g2}: {gap:+.3e}")
    print(f"   worst max(E2-E1) over all cases: {worst:+.3e}")
    # four points, vary one interior gap
    for h in (0.5, 2.0):
        for g1, g2 in ((0.3, 0.6), (1.0, 2.0)):
            t1 = [0.0, h, h + g1, h + g1 + h]; t2 = [0.0, h, h + g2, h + g2 + h]
            gap, _, _ = sm_gap(fdd(Q, t1, 1.0), fdd(Q, t2, 1.0))
            print(f"   n=4 middle gap {g1}->{g2}, h={h}: max(E2-E1)={gap:+.3e} {'VIOLATION' if gap>1e-9 else 'OK'}")

def test_phi_preservation(Q, h, name):
    """maximize the worst violation of increasing differences of Phi over supermodular phi, |phi|<=1."""
    m = 3; P = expm(Q * h)
    pts = list(itertools.product(range(m), repeat=3)); idx = {x: i for i, x in enumerate(pts)}; N = len(pts)
    rows = []
    for x in pts:
        for i in range(3):
            for j in range(i+1, 3):
                if x[i] + 1 < m and x[j] + 1 < m:
                    xi = list(x); xi[i] += 1; xj = list(x); xj[j] += 1; xij = list(x); xij[i] += 1; xij[j] += 1
                    r = np.zeros(N); r[idx[tuple(xij)]] += 1; r[idx[x]] += 1; r[idx[tuple(xi)]] -= 1; r[idx[tuple(xj)]] -= 1
                    rows.append(-r)
    A = np.array(rows)
    worst = 0.0; arg = None
    # Phi(x,y) = sum_z P(y,z) phi(x,y,z); violation: Phi(x+1,y+1)+Phi(x,y)-Phi(x+1,y)-Phi(x,y+1) < 0
    for x in range(m-1):
        for y in range(m-1):
            c = np.zeros(N)
            for z in range(m):
                c[idx[(x+1, y+1, z)]] += P[y+1, z]; c[idx[(x, y, z)]] += P[y, z]
                c[idx[(x+1, y, z)]] -= P[y, z];     c[idx[(x, y+1, z)]] -= P[y+1, z]
            res = linprog(c, A_ub=A, b_ub=np.zeros(len(rows)), bounds=[(-1, 1)]*N, method="highs")
            if res.fun < worst - 1e-12: worst, arg = res.fun, (x+1, y+1)
    print(f"== (B) {name}, h={h}: most negative increasing-difference of Phi over supermodular phi: {worst:+.4f} at (x,y)={arg}")

if __name__ == "__main__":
    Q = star(1.0, 1.0)
    test_single_gap(Q, "star a=b=1")
    test_single_gap(star(1.0, 3.0), "star a=1 b=3")
    for h in (0.2, 1.0, 3.0):
        test_phi_preservation(Q, h, "star a=b=1")
    from p0291_star_sm_lp import birth_death
    test_phi_preservation(birth_death(1.0, 2.0), 1.0, "birth-death control (must be >= 0)")
