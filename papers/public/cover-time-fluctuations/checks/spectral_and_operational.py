"""Checks for Sections 7-8 that do not reduce to rational arithmetic.

  1. The perturbation identities of Lemma 8.1, lambda'(0) = 0 and
     lambda''(0) = (2/q) f^T L^+ f, checked numerically to high precision (mpmath,
     50 digits, central differences) for every core in a list and several centred
     vectors f; and exactly for the two-vertex core, where the top eigenvalue of
     -L + z diag(a, -a) is -1 + sqrt(1 + a^2 z^2).
  2. The occupation-time covariance (2/q) L^+ of (8.1), checked against a long
     simulation of the rate-one-per-edge chain on the two-vertex core and on the
     triangle.
  3. An exact-in-law Monte Carlo of the physical cover time of the double star D_k
     through the operational construction of Section 7.1 (thresholds are maxima of
     k exponentials, marks are Poisson in local time), compared with the
     half-normal limit (10.2). This is a diagnostic of the limit theorem and of
     the transfer identity (7.9), not a proof.
"""
import math
import numpy as np
import mpmath as mp

from decorated_cores import CORES, laplacian, pseudoinverse
from fractions import Fraction as Fr

mp.mp.dps = 50


def top_eig(q, edges, f, z):
    L = laplacian(q, edges)
    M = mp.matrix(q, q)
    for i in range(q):
        for j in range(q):
            M[i, j] = -mp.mpf(L[i][j].numerator) / L[i][j].denominator + (z * f[i] if i == j else 0)
    ev = mp.eigsy(M)[0]
    return max(ev)


def check_perturbation():
    rng = np.random.default_rng(7)
    print("== 1. lambda'(0) = 0 and lambda''(0) = (2/q) f^T L^+ f (mpmath central differences, h = 1e-8)")
    for name, (q, edges) in CORES.items():
        Lp = pseudoinverse(laplacian(q, edges))
        worst = 0
        for trial in range(3):
            f = rng.standard_normal(q); f -= f.mean()
            f = [mp.mpf(float(x)) for x in f]
            h = mp.mpf('1e-8')
            l0 = top_eig(q, edges, f, mp.mpf(0)); lp = top_eig(q, edges, f, h); lm = top_eig(q, edges, f, -h)
            d1 = (lp - lm) / (2 * h)
            d2 = (lp - 2 * l0 + lm) / h**2
            pred = 2 / mp.mpf(q) * sum(f[i] * sum(mp.mpf(Lp[i][j].numerator) / Lp[i][j].denominator * f[j] for j in range(q)) for i in range(q))
            worst = max(worst, abs(d1), abs(d2 - pred))
            assert abs(l0) < mp.mpf('1e-40') and abs(d1) < mp.mpf('1e-12') and abs(d2 - pred) < mp.mpf('1e-10'), (name, d1, d2, pred)
        print(f"   {name}: max |lambda'(0)|, |lambda''(0) - (2/q) f L+ f| = {mp.nstr(worst, 3)}  ok")
    # exact two-vertex case
    a, z = mp.mpf('0.7'), mp.mpf('0.3')
    lam = top_eig(2, [(0, 1)], [a, -a], z)
    assert abs(lam - (-1 + mp.sqrt(1 + a * a * z * z))) < mp.mpf('1e-45')
    print("   two-vertex core: top eigenvalue of -L + z diag(a,-a) is -1 + sqrt(1 + a^2 z^2); lambda''(0) = a^2 = (2/q) f L+ f  ok")


def simulate_occupation(q, edges, T, n, rng):
    """Occupation vector A(T) of the rate-one-per-edge chain, n independent runs, vectorised."""
    nbrs = [[b for a, b in edges if a == v] + [a for a, b in edges if b == v] for v in range(q)]
    deg = np.array([len(x) for x in nbrs])
    state = rng.integers(0, q, size=n)
    tnow = np.zeros(n)
    A = np.zeros((n, q))
    active = np.ones(n, dtype=bool)
    while active.any():
        idx = np.nonzero(active)[0]
        hold = rng.exponential(1.0 / deg[state[idx]])
        end = np.minimum(tnow[idx] + hold, T)
        A[idx, state[idx]] += end - tnow[idx]
        tnow[idx] = end
        done = end >= T
        active[idx[done]] = False
        move = idx[~done]
        if move.size:
            choice = rng.integers(0, 10**9, size=move.size)
            new = np.array([nbrs[s][c % deg[s]] for s, c in zip(state[move], choice)])
            state[move] = new
    return A


def check_occupation_cov():
    print("== 2. covariance of (A(T) - T/q)/sqrt(T) against (2/q) L^+  (simulation, T = 400, 20000 runs)")
    rng = np.random.default_rng(11)
    for name in ('edge', 'triangle', 'path3'):
        q, edges = CORES[name]
        Lp = pseudoinverse(laplacian(q, edges))
        target = np.array([[2.0 / q * float(Lp[i][j]) for j in range(q)] for i in range(q)])
        T, n = 400.0, 20000
        A = simulate_occupation(q, edges, T, n, rng)
        X = (A - T / q) / math.sqrt(T)
        C = np.cov(X.T)
        err = np.abs(C - target).max()
        se = 3 * np.abs(target).max() * math.sqrt(2.0 / n) + 0.02
        print(f"   {name}: max |cov - (2/q)L+| = {err:.4f} (target entries {np.round(target, 3).tolist()})")
        assert err < se, (name, C, target)


def double_star_operational_mc(k, n, rng):
    """Exact-in-law samples of tau_cov(D_k) from a centre start."""
    taus = np.empty(n)
    for s in range(n):
        # thresholds and sums of the k first-arrival times at each centre
        E1 = rng.exponential(1.0, k); E2 = rng.exponential(1.0, k)
        B = np.array([E1.max(), E2.max()]); Esum = np.array([E1.sum(), E2.sum()])
        A = np.zeros(2); pos = 0; t = 0.0; J = 0
        while True:
            hold = rng.exponential(1.0)
            need = B[pos] - A[pos]
            other_done = A[1 - pos] >= B[1 - pos]
            if other_done and need <= hold:
                A[pos] += max(need, 0.0)
                break
            A[pos] += hold; t += hold; pos = 1 - pos; J += 1
        # marks: k + Poisson(k A_v - sum E_v) at each centre
        P = 2 * k + rng.poisson(max(k * A[0] - Esum[0], 0.0)) + rng.poisson(max(k * A[1] - Esum[1], 0.0))
        taus[s] = 2 * P + J - 1
    return taus


def check_half_normal():
    print("== 3. operational Monte Carlo of tau_cov(D_k): standardised by (10.2), compared with |Z|")
    rng = np.random.default_rng(2026)
    print("   k       n     mean [->0.798]   sd [->0.603]   P(W<=0.5) [->0.383]   KS distance to |Z|")
    for k, n in ((1000, 20000), (10000, 20000)):
        taus = double_star_operational_mc(k, n, rng)
        L = math.log(k)
        W = (taus - 4 * k * L) / (2 * math.sqrt(2) * k * math.sqrt(L))
        W.sort()
        cdf = lambda w: math.erf(max(w, 0.0) / math.sqrt(2))
        ks = max(abs(cdf(w) - (i + 1) / n) for i, w in enumerate(W))
        print(f"   {k:5d}  {n:6d}   {W.mean():7.3f}         {W.std():6.3f}       {np.mean(W <= 0.5):6.3f}              {ks:.3f}")
    print("   (the leading-order standardisation carries O(1/sqrt(log k)) corrections; the shape is the half-normal)")


if __name__ == '__main__':
    check_perturbation()
    check_occupation_cov()
    check_half_normal()
    print("SPECTRAL_AND_OPERATIONAL_CHECKS_DONE")
