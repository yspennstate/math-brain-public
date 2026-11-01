"""Numerical checks for 'Quadratic forms with nine large eigenvalues have bounded densities'.

Every test is labelled by the statement it exercises. Exact arithmetic and high-precision evaluation are used for
constants; Monte Carlo and quadrature are used for the analytic statements, with explicit error allowances.
Numerical checks are evidence, not proofs.

usage: python verify.py [--quick] [--skip-t1] [--out results.json]
"""
import argparse
import itertools
import json
import math
import sys
import time

import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, pi as mpi, e as me, log as mlog, gamma as mgamma
from mpmath import asinh as masinh, acosh as macosh, quad as mquad, inf as minf, factorial as mfact

mp.dps = 50
RESULTS = []


def record(test_id, label, ok, detail):
    RESULTS.append({"id": test_id, "statement": label, "pass": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + test_id + " [" + label + "] " + str(detail), flush=True)


# ---------------------------------------------------------------- constants
def omega(m):
    return mpf(1) if m == 0 else mpf(m) ** m / mfact(m)


def beta(ell):
    return ((msqrt(2) * mpi * me) ** ell * msqrt(omega(ell))) ** mpf("0.5")


def check_constants():
    eta = mpf(3) / 40
    zeta = mpf(1) / 400
    kappa = mpf(4) / 625
    C3 = 3 * msqrt(2) * me * (mpf(9) / 2) ** (mpf(1) / 6)
    C2 = 8 * msqrt(me) * 2 ** (-mpf(1) / 8)
    C1 = 2 * me ** mpf("0.25") * msqrt(msqrt(2) * mpi * me) * mgamma(mpf("0.25")) / msqrt(mpi)
    L0 = 2 + 2 * mlog(19)
    J0 = mpi + 4 * mlog(2)
    delta = mpf(1) / 64
    nopiv = 25 * C3
    diag_half = eta ** mpf("-0.5") * (J0 + 2 * L0)
    pair_half = 16 * zeta ** mpf("-0.25")
    indef = zeta ** mpf("-0.5") * (6 + mlog(16) + L0) + 1 / me
    items = [
        ("cor:decay(a) C3 = 3 beta3^(2/3)/pi", abs(3 * beta(3) ** (mpf(2) / 3) / mpi - C3) < mpf(10) ** -40),
        ("cor:decay(a) C3 < 14.82", C3 < mpf("14.82")),
        ("cor:decay(b) C2 = 8 sqrt(beta2/(2pi))", abs(8 * msqrt(beta(2) / (2 * mpi)) - C2) < mpf(10) ** -40),
        ("cor:decay(b) beta2 = 2^(3/4) pi e", abs(beta(2) - 2 ** (mpf(3) / 4) * mpi * me) < mpf(10) ** -40),
        ("cor:decay(b) C2 < 12.1", C2 < mpf("12.1")),
        ("lem:concentration constant < 18.3", C1 < mpf("18.3")),
        ("lem:concentration 18.3 < 19", mpf("18.3") < 19),
        ("lem:concentration L0 < 7.9", L0 < mpf("7.9")),
        ("lem:concentration integral of min(1,19e^{-u/2}) = 2+2log19",
         abs(mquad(lambda u: min(1, 19 * mp.e ** (-u / 2)), [0, 2 * mlog(19), minf]) - L0) < mpf(10) ** -20),
        ("lem:kernels (1+sqrt(1+d))(1+sqrt(1-d)) <= 4 on 2001 points of [0,1]",
         all((1 + msqrt(1 + d)) * (1 + msqrt(1 - d)) <= 4 for d in [mpf(i) / 2000 for i in range(2001)])),
        ("lem:kernels J(1) = pi + 2 log(1+sqrt2) < pi + 4 log 2", mpi + 2 * mlog(1 + msqrt(2)) < J0),
        ("lem:pairhalf int_0^inf min(1, 2M/s^2) ds = 2 sqrt(2M) (M = 0.3, 1, 7)",
         all(abs(mquad(lambda s: min(1, 2 * M / s ** 2), [0, msqrt(2 * M), minf]) - 2 * msqrt(2 * M)) < mpf(10) ** -20
             for M in (mpf("0.3"), mpf(1), mpf(7)))),
        ("lem:pairhalf definite 2 sqrt(2 pi) < 6", 2 * msqrt(2 * mpi) < 6),
        ("lem:pairhalf near integral = 4 sqrt(delta)(8 + log(16/delta)) (quadrature, delta = 1/64)",
         abs(2 * mquad(lambda y: (6 + mlog(16 / y)) * y ** mpf("-0.5"), [0, delta]) - 4 * msqrt(delta) * (8 + mlog(16 / delta)))
         < mpf(10) ** -20),
        ("lem:pairhalf 4 sqrt(delta)(8+log(16/delta)) = 4 + 5 log 2", abs(4 * msqrt(delta) * (8 + mlog(16 / delta)) - (4 + 5 * mlog(2))) < mpf(10) ** -40),
        ("lem:pairhalf 8 + 4 + 5 log 2 < 16", 12 + 5 * mlog(2) < 16),
        ("eq:small eta^2 + zeta = 13/1600", eta ** 2 + zeta == mpf(13) / 1600),
        ("eq:small sqrt(13/1600) < 1/11", msqrt(mpf(13) / 1600) < mpf(1) / 11),
        ("prop:volume r=0: eta + sqrt(kappa) < 1", eta + msqrt(kappa) < 1),
        ("prop:volume eps < 3 sqrt(kappa) = 6/25", abs(3 * msqrt(kappa) - mpf(6) / 25) < mpf(10) ** -45),
        ("prop:volume 1 - 6/25 - 3/40 = 137/200", 1 - mpf(6) / 25 - mpf(3) / 40 == mpf(137) / 200),
        ("prop:volume 1/11 + 6/25 < 1/3", mpf(1) / 11 + mpf(6) / 25 < mpf(1) / 3),
        ("prop:volume 2/3 < 137/200", mpf(2) / 3 < mpf(137) / 200),
        ("prop:nopivot(a) (kappa^3/64)^{-1/6} = 25", abs((kappa ** 3 / 64) ** (-mpf(1) / 6) - 25) < mpf(10) ** -30),
        ("prop:nopivot(a) 25 C3 < 371", nopiv < 371),
        ("prop:nopivot(b) (kappa^2/16)^{-1/8} = 5", abs((kappa ** 2 / 16) ** (-mpf(1) / 8) - 5) < mpf(10) ** -30),
        ("prop:nopivot(b) 5 C2 < 60.5", 5 * C2 < mpf("60.5")),
        ("prop:halfpotential pair 16 zeta^{-1/4} = 16 sqrt 20 < 72", abs(pair_half - 16 * msqrt(20)) < mpf(10) ** -40 and pair_half < 72),
        ("prop:halfpotential diagonal eta^{-1/2}(pi + 4 log 2 + 2 L0) < 79.3", diag_half < mpf("79.3")),
        ("prop:halfpotential diagonal with L0 < 8: sqrt(40/3)(pi + 4 log 2 + 16) < 81", msqrt(mpf(40) / 3) * (J0 + 16) < 81),
        ("prop:halfpotential 81 + 1 = 82 dominates 61 and 72", mpf(81) + 1 == 82 and 61 < 82 and 72 < 82),
        ("thm:main diagonal pivot sqrt(40/3) * 82 < 300", msqrt(mpf(40) / 3) * 82 < 300),
        ("thm:main definite pair pi zeta^{-1/2} = 20 pi < 63", abs(mpi * zeta ** mpf("-0.5") - 20 * mpi) < mpf(10) ** -40 and 20 * mpi < 63),
        ("thm:main indefinite pair 20(6+log16+L0)+1/e < 334", indef < 334),
        ("thm:main indefinite pair with L0 < 8: 20(6+log16+8)+1/e < 337", 20 * (6 + mlog(16) + 8) + 1 / me < 337),
        ("thm:main every case < 375 <= 400", max(nopiv, 300, 63, 337) < 375 and 375 <= 400),
        ("lem:hyperbola (15/2) log 2 < 6", mpf(15) / 2 * mlog(2) < 6),
        ("lem:hyperbola T1 = (3/4) log 2 gives e^{2T1} = 2 sqrt2", abs(mp.e ** (mpf(3) / 2 * mlog(2)) - 2 * msqrt(2)) < mpf(10) ** -40),
        ("lem:halfmoment 4^{1/4}/(2 sqrt pi) = 1/sqrt(2 pi)", abs(4 ** mpf("0.25") / (2 * msqrt(mpi)) - 1 / msqrt(2 * mpi)) < mpf(10) ** -40),
        ("thm:main sup_D D^{-1/2} log D = 2/e", abs(mp.findroot(lambda D: mp.diff(lambda x: mlog(x) / msqrt(x), D), 7) - me ** 2) < mpf(10) ** -20
         and abs(mlog(me ** 2) / me - 2 / me) < mpf(10) ** -40),
        ("thm:decay a_k decreasing in k (ell<=12)", all(
            (2 * me) ** (mpf(ell - k - 1) / 2) * msqrt(omega(ell - k - 1)) * 2 ** (mpf(k + 1) / 2)
            <= (2 * me) ** (mpf(ell - k) / 2) * msqrt(omega(ell - k)) * 2 ** (mpf(k) / 2) * me ** mpf("-0.5") * (1 + mpf(10) ** -30)
            for ell in range(1, 13) for k in range(0, ell))),
        ("thm:decay pi^l e^{l/2}(2e)^{l/2} = (sqrt2 pi e)^l", all(
            abs(mpi ** l * me ** (mpf(l) / 2) * (2 * me) ** (mpf(l) / 2) - (msqrt(2) * mpi * me) ** l) < mpf(10) ** -30 for l in range(1, 8))),
        ("lem:fpower m=floor(p/2) >= p/4 for p>=2", all(math.floor(p / 2) >= p / 4 for p in np.linspace(2, 50, 4801))),
    ]
    for name, ok in items:
        record("C", name, ok, "")
    return {"C3": str(C3)[:22], "C2": str(C2)[:22], "C1": str(C1)[:22], "L0": str(L0)[:22],
            "no_pivot_25C3": str(nopiv)[:10], "diagonal_pivot_bound": "sqrt(40/3)*82 = " + str(msqrt(mpf(40) / 3) * 82)[:8],
            "indefinite_pair": str(indef)[:10], "definite_pair": str(20 * mpi)[:8],
            "final": "every case < 375 <= 400"}


# ---------------------------------------------------------------- analytic identities
def check_identities():
    for t in [0.3, 1.0, 7.5]:
        lhs = mquad(lambda v: v ** mpf("-1.25") * mp.e ** (-mpf(t) ** 2 / (4 * v)), [0, 1, minf])
        rhs = 4 ** mpf("0.25") * mgamma(mpf("0.25")) * mpf(t) ** mpf("-0.5")
        record("I1", "lem:halfmoment inner integral t=%g" % t, abs(lhs - rhs) < mpf(10) ** -10 * abs(rhs), float(lhs - rhs))
    for w in [0.2, 3.0]:
        lhs = 2 * mquad(lambda t: mp.e ** (-w * t * t) * t ** mpf("-0.5"), [0, 1, minf])
        rhs = mgamma(mpf("0.25")) * mpf(w) ** mpf("-0.25")
        record("I2", "lem:concentration Gamma integral w=%g" % w, abs(lhs - rhs) < mpf(10) ** -15, float(lhs - rhs))
    for z in [0.1, 2.0]:
        lhs = mquad(lambda v: v ** mpf("-0.75") * mp.e ** (-v * mpf(z) ** 2), [0, 1, minf]) / mgamma(mpf("0.25"))
        record("I3", "lem:halfmoment |z|^{-1/2} representation z=%g" % z, abs(lhs - mpf(z) ** mpf("-0.5")) < mpf(10) ** -10, float(lhs - mpf(z) ** mpf("-0.5")))
    for v, a in [(0.5, 0.2), (2.0, -1.0)]:
        # Z uniform on [0,1]: E exp(-v(Z-a)^2) against the Fourier formula of lem:fourier(c)
        lhs = mquad(lambda z: mp.e ** (-v * (z - a) ** 2), [0, 1])
        phi = lambda t: (mp.e ** (1j * t) - 1) / (1j * t) if t != 0 else 1
        rhs = mquad(lambda t: mp.re(mp.e ** (-t * t / (4 * v)) * mp.e ** (-1j * t * a) * phi(t)), [-minf, 0, minf]) / (2 * msqrt(mpi * v))
        record("I4", "lem:fourier(c) Gaussian identity v=%g a=%g" % (v, a), abs(lhs - rhs) < mpf(10) ** -10, float(lhs - rhs))
    # lem:kernels: J(d) on a grid, and the log kernel
    worst_J, worst_log, worst_formula = -1e9, -1e9, 0.0
    for d in list(np.logspace(-6, 1.5, 60)) + [1.0]:
        J = mquad(lambda x: abs(x) ** mpf("-0.5") * abs(x - d) ** mpf("-0.5"), [-1, 0, min(d, 1), 1] if d < 1 else [-1, 0, 1])
        worst_J = max(worst_J, float(J) - (math.pi + 4 * math.log(2) + 2 * max(0.0, math.log(1 / d))))
        if d <= 1:
            dd = mpf(d)
            exact = mpi + 2 * mlog((1 + msqrt(1 + dd)) * (1 + msqrt(1 - dd))) + 2 * mlog(1 / dd)
            worst_formula = max(worst_formula, float(abs(J - exact) / exact))
    for a in list(np.linspace(-1.5, 1.5, 61)):
        pts = sorted(set([-1, 0, 1] + ([a] if -1 < a < 1 else [])))
        L = float(mquad(lambda x: abs(x) ** mpf("-0.5") * max(0, -mlog(abs(x - a))) if x != a else 0, pts))
        worst_log = max(worst_log, L - 8)
    record("I5", "lem:kernels J(d) <= pi + 4 log 2 + 2 log+(1/d), 61 values of d", worst_J < 0, "max excess %.4f" % worst_J)
    record("I7", "lem:kernels exact formula J(d) = pi + 2 log((1+sqrt(1+d))(1+sqrt(1-d))) + 2 log(1/d), d <= 1",
           worst_formula < 1e-8, "max relative difference %.2e" % worst_formula)
    record("I6", "lem:kernels log kernel <= 8, 61 centres", worst_log < 1e-9, "max excess %.2e" % worst_log)


# ---------------------------------------------------------------- linear algebra
def sv(T):
    return np.linalg.svd(T, compute_uv=False)


def check_linear_algebra(rng):
    bad = 0
    for _ in range(300):
        m, n = rng.integers(2, 9), rng.integers(2, 9)
        T, U = rng.normal(size=(m, n)), rng.normal(size=(m, n))
        sT, sU = sv(T), sv(U)
        bad += np.any(np.abs(sT - sU) > np.linalg.norm(T - U, 2) + 1e-9)
        q = rng.integers(0, min(m, n) + 1)
        R = rng.normal(size=(m, q)) @ rng.normal(size=(q, n))
        sTR = np.concatenate([sv(T + R), np.zeros(20)])
        sTp = np.concatenate([sT, np.zeros(20)])
        for j in range(1, min(m, n) + 1):
            bad += sTR[j + q - 1] > sTp[j - 1] + 1e-9
    record("L1", "lem:weyl Weyl and rank inequalities, 300 random pairs", bad == 0, "violations %d" % bad)

    bad = 0
    for trial in range(400):
        n = rng.integers(3, 10)
        k = rng.integers(1, min(3, n - 1) + 1)
        A = rng.normal(size=(n, n)); A = (A + A.T) / 2
        if trial % 3 == 0:  # make A singular and with repeated eigenvalue moduli
            w, V = np.linalg.eigh(A); w[: n // 3] = 0.0; w[-1] = -w[-2]; A = V @ np.diag(w) @ V.T
        B, C, D = A[:k, :k], A[:k, k:], A[k:, k:]
        if abs(np.linalg.det(B)) < 1e-6:
            continue
        S = D - C.T @ np.linalg.solve(B, C)
        la, ls = np.abs(np.linalg.eigvalsh(A)), np.abs(np.linalg.eigvalsh(S))
        for t in np.concatenate([np.linspace(0.05, 3, 25), la[la > 1e-9] * (1 - 1e-12)]):
            bad += (ls >= t).sum() < (la >= t).sum() - k
    record("L2", "lem:schur N_S(t) >= N_A(t) - k, 400 random matrices incl. singular", bad == 0, "violations %d" % bad)

    bad = 0
    for _ in range(300):
        n = rng.integers(2, 8)
        T = rng.normal(size=(n, n))
        T[np.diag_indices(n)] = np.abs(T).sum(1) + rng.uniform(0.01, 1, n)
        bad += abs(np.linalg.det(T)) < 1e-12
    record("L3", "lem:dd strictly diagonally dominant matrices are invertible, 300 cases", bad == 0, "violations %d" % bad)

    bad = 0
    for _ in range(100):
        nI, nJ = rng.integers(2, 7), rng.integers(2, 7)
        M = rng.normal(size=(nI, nJ))
        ev = np.linalg.eigvalsh(M @ M.T)
        for ell in range(1, min(nI, nJ) + 1):
            e_ell = sum(np.prod(c) for c in itertools.combinations(ev, ell))
            gram = sum(np.linalg.det(M[list(T)] @ M[list(T)].T) for T in itertools.combinations(range(nI), ell))
            minors = sum(np.linalg.det(M[np.ix_(S, T)]) ** 2 for S in itertools.combinations(range(nI), ell)
                         for T in itertools.combinations(range(nJ), ell))
            bad += not (abs(e_ell - gram) < 1e-8 * max(1, abs(e_ell)) and abs(gram - minors) < 1e-8 * max(1, abs(gram)))
        H = list(range(rng.integers(1, min(nI - 1, nJ) + 1)))
        MH = M[H]
        Pi = MH.T @ np.linalg.solve(MH @ MH.T, MH)
        C = M @ (np.eye(nJ) - Pi)
        rest = [i for i in range(nI) if i not in H]
        for s in range(1, len(rest) + 1):
            for T in itertools.combinations(rest, s):
                lhs = np.linalg.det(M[H + list(T)] @ M[H + list(T)].T)
                rhs = np.linalg.det(MH @ MH.T) * np.linalg.det(C[list(T)] @ C[list(T)].T)
                bad += abs(lhs - rhs) > 1e-8 * max(1, abs(lhs))
    record("L4", "lem:gram Cauchy-Binet and Gram factorization, 100 random M", bad == 0, "violations %d" % bad)


# ---------------------------------------------------------------- Brascamp-Lieb and projections
def check_bl(rng):
    worst = -1.0
    g = np.linspace(-12, 12, 1201)
    X, Y = np.meshgrid(g, g, indexing="ij")
    dx = g[1] - g[0]
    for trial in range(40):
        N = rng.integers(3, 6)
        W = rng.normal(size=(N, 2))
        G = W.T @ W
        w_, V_ = np.linalg.eigh(G)
        Gm = V_ @ np.diag(w_ ** -0.5) @ V_.T
        Wt = W @ Gm.T  # rows G^{-1/2} w_i
        c = (Wt ** 2).sum(1)
        u = Wt / np.sqrt(c)[:, None]
        assert np.allclose((c[:, None, None] * u[:, :, None] * u[:, None, :]).sum(0), np.eye(2))
        lhs = np.ones_like(X)
        masses = []
        for i in range(N):
            ctr = rng.normal(size=3) * 2
            wid = rng.uniform(0.2, 1.5, 3)
            amp = rng.uniform(0.2, 2.0, 3)
            if trial % 2:
                h = lambda s, ctr=ctr, wid=wid, amp=amp: sum(a * (np.abs(s - m) < w) for a, m, w in zip(amp, ctr, wid))
                mass = float(sum(a * 2 * w for a, w in zip(amp, wid)))
            else:
                h = lambda s, ctr=ctr, wid=wid, amp=amp: sum(a * np.exp(-((s - m) / w) ** 2) for a, m, w in zip(amp, ctr, wid))
                mass = float(sum(a * w * math.sqrt(math.pi) for a, w in zip(amp, wid)))
            lhs = lhs * h(u[i, 0] * X + u[i, 1] * Y) ** c[i]
            masses.append(mass)
        L = lhs.sum() * dx * dx
        Rr = float(np.prod([m ** ci for m, ci in zip(masses, c)]))
        worst = max(worst, L / Rr)
    record("B1", "thm:bl geometric Brascamp-Lieb in R^2, 40 random frames and functions (grid quadrature)",
           worst <= 1 + 2e-2, "max LHS/RHS %.4f" % worst)

    worst = 0.0
    for trial in range(60):
        n = rng.integers(2, 9)
        a = rng.normal(size=n); a /= np.linalg.norm(a)
        # exact density of a.X for X_i uniform on [0,1]: convolution on a fine grid
        h = 1e-3
        dens = None
        for ai in a:
            L_ = abs(ai)
            k = max(1, int(round(L_ / h)))
            piece = np.full(k, 1.0 / (k * h))
            dens = piece if dens is None else np.convolve(dens, piece) * h
        worst = max(worst, dens.max())
    record("B2", "lem:projection d=1: density of a.X for uniform coordinates <= sqrt(e) (sharp sqrt2)",
           worst <= math.sqrt(math.e) and worst <= math.sqrt(2) + 1e-2, "max density %.4f" % worst)

    worst = 0.0
    for trial in range(12):
        n = rng.integers(3, 7)
        U, _ = np.linalg.qr(rng.normal(size=(n, 2)))
        Xs = rng.uniform(0, 1, size=(4_000_000, n))
        P = Xs @ U
        H2, xe, ye = np.histogram2d(P[:, 0], P[:, 1], bins=120)
        area = (xe[1] - xe[0]) * (ye[1] - ye[0])
        worst = max(worst, H2.max() / (len(P) * area))
    record("B3", "lem:projection d=2 Monte Carlo max density of U^T X (uniform coordinates) <= e",
           worst <= math.e, "max histogram density %.3f (sharp bound 2)" % worst)

    worst = -1.0
    ts = np.linspace(-400, 400, 800001)
    dt = ts[1] - ts[0]
    laws = {
        "uniform": lambda t: np.where(t == 0, 1.0 + 0j, (np.exp(1j * t) - 1) / (1j * np.where(t == 0, 1, t))),
        "two-halves": lambda t: 0.5 * (np.where(t == 0, 1.0 + 0j, (np.exp(0.5j * t) - 1) / (0.5j * np.where(t == 0, 1, t))) * (1 + np.exp(10j * t))),
        "comb4": lambda t: sum(0.25 * np.exp(1j * t * 3 * k) * np.where(t == 0, 1.0 + 0j, (np.exp(0.25j * t) - 1) / (0.25j * np.where(t == 0, 1, t))) for k in range(4)),
        "triangle": lambda t: np.where(t == 0, 1.0 + 0j, (np.sin(t / 2) / np.where(t == 0, 1, t / 2)) ** 2),
    }
    for name, ph in laws.items():
        vals = np.abs(ph(ts))
        for p in [2, 2.5, 3, 4, 6, 10, 20]:
            I = (vals ** p).sum() * dt
            worst = max(worst, I / (2 * math.pi * math.sqrt(2 * math.e) / math.sqrt(p)))
    record("B4", "lem:fpower int |f^|^p <= 2 pi sqrt(2e)/sqrt p for four laws, p in [2,20]", worst <= 1.0,
           "max ratio %.4f" % worst)


# ---------------------------------------------------------------- entropy lemma
def check_entropy(rng):
    worst = -1e9
    for trial in range(2000):
        N = rng.integers(2, 9)
        m = rng.integers(1, min(4, N) + 1)
        subs = list(itertools.combinations(range(N), m))
        w = rng.dirichlet(np.full(len(subs), rng.choice([0.05, 0.3, 1.0, 5.0])))
        alpha = np.zeros(N)
        for wt, T in zip(w, subs):
            alpha[list(T)] += wt
        H = -sum(x * math.log(x) for x in w if x > 0)
        A = sum(a * math.log(a) for a in alpha if a > 0)
        worst = max(worst, H + A - math.log(m ** m / math.factorial(m)))
    record("E1", "lem:entropy H(w) + sum alpha log alpha <= log(m^m/m!), 2000 random w", worst <= 1e-12,
           "max excess %.3e" % worst)


# ---------------------------------------------------------------- samplers with density <= 1
def sampler(name, rng, size):
    if name == "uniform":
        return rng.uniform(0, 1, size)
    if name == "comb":
        k = rng.integers(0, 4, size)
        return 3.0 * k + rng.uniform(0, 0.25, size)
    if name == "halves":
        return rng.uniform(0, 0.5, size) + 10.0 * rng.integers(0, 2, size)
    if name == "triangle":
        return rng.uniform(0, 1, size) + rng.uniform(0, 1, size)
    if name == "centred":
        return rng.uniform(-0.5, 0.5, size)
    raise ValueError(name)


LAWS = ["uniform", "comb", "halves", "triangle"]


def draw(n, N, rng, laws):
    return np.stack([sampler(laws[i % len(laws)], rng, N) for i in range(n)], axis=1)


def qvals(Xs, A, b, c):
    return ((Xs @ A) * Xs).sum(axis=1) + Xs @ b + c


# ---------------------------------------------------------------- Fourier decay theorem
def e_ell(M, ell):
    """ell-th elementary symmetric function of the squared singular values (recursion, exact up to rounding)."""
    s2 = sv(M) ** 2
    e = np.zeros(ell + 1); e[0] = 1.0
    for x in s2:
        e[1:] = e[1:] + x * e[:-1]
    return float(e[ell])


def check_decay(rng, quick):
    N = 400_000 if quick else 2_000_000
    worst = -1.0
    tested = 0
    for trial in range(10 if quick else 24):
        n = rng.integers(4, 8)
        A = rng.normal(size=(n, n)) * rng.uniform(0.3, 2.0)
        A = (A + A.T) / 2
        if trial % 4 == 1:  # a heavy row: forces the hub branch
            A[0, :] *= 6; A[:, 0] *= 6
        b = rng.normal(size=n) * 3
        c = rng.normal()
        I = list(range(n // 2)); J = list(range(n // 2, n))
        M = A[np.ix_(I, J)]
        laws = [LAWS[(trial + i) % 4] for i in range(n)]
        Xs = draw(n, N, rng, laws)
        Q = qvals(Xs, A, b, c)
        for ell in range(1, min(len(I), len(J)) + 1):
            E = e_ell(M, ell)
            if E <= 0:
                continue
            for t in [0.5, 1.0, 2.0, 4.0, 8.0]:
                bound = (math.sqrt(2) * math.pi * math.e) ** ell * math.sqrt(ell ** ell / math.factorial(ell)) / (math.sqrt(E) * t ** ell)
                if bound >= 1:
                    continue
                ph = np.exp(1j * t * Q).mean()
                err = 4.0 / math.sqrt(N)
                worst = max(worst, (abs(ph) - err) ** 2 / bound if abs(ph) > err else 0.0)
                tested += 1
    record("D1", "thm:decay |phi_Q(t)|^2 <= (sqrt2 pi e)^l w(l)^{1/2} E_l^{-1/2} |t|^{-l} (Monte Carlo, 4 laws)",
           worst <= 1.0, "cases where bound < 1: %d; max (|phi|-4sd)^2/bound %.3e" % (tested, worst))


def check_decoupling(rng, quick):
    """Inequality (4.4): |phi_Q(t)|^2 <= E prod_{i in I} |psi_i(2t<m_i,D>)| for uniform[0,1] coordinates,
    where |psi(s)| = |sin(s/2)/(s/2)| exactly; both sides estimated by Monte Carlo."""
    N = 400_000 if quick else 2_000_000
    worst = -1.0
    cases = 0
    for trial in range(12 if quick else 30):
        n = int(rng.integers(3, 8))
        A = rng.normal(size=(n, n)) * rng.uniform(0.2, 1.5); A = (A + A.T) / 2
        b = rng.normal(size=n); c = rng.normal()
        k = int(rng.integers(1, n))
        I, J = list(range(k)), list(range(k, n))
        M = A[np.ix_(I, J)]
        Xs = rng.uniform(0, 1, size=(N, n))
        Q = qvals(Xs, A, b, c)
        Dm = rng.uniform(0, 1, size=(N, len(J))) - rng.uniform(0, 1, size=(N, len(J)))
        MD = Dm @ M.T
        for t in [0.25, 0.5, 1.0, 2.0, 4.0]:
            lhs = abs(np.exp(1j * t * Q).mean()) ** 2
            arg = t * MD  # s/2 with s = 2t<m_i,D>
            rhs = np.prod(np.abs(np.sinc(arg / np.pi)), axis=1).mean()
            err = 8.0 / math.sqrt(N)
            if rhs > 20 * err:
                cases += 1
                worst = max(worst, (lhs - err) / (rhs + err))
    record("D2", "eq:step1 decoupling |phi_Q|^2 <= E prod |psi_i(2t<m_i,D>)| (uniform laws, Monte Carlo both sides)",
           worst <= 1.0, "cases %d, max (lhs-err)/(rhs+err) %.4f" % (cases, worst))


# ---------------------------------------------------------------- one and two coordinates
def check_pivots(rng, quick):
    N = 1_000_000 if quick else 4_000_000
    worst_sq = worst_def = worst_hyp = 0.0
    for trial in range(8):
        a = rng.uniform(0.05, 5) * rng.choice([-1, 1]); m = rng.normal(); v = rng.normal()
        Y = sampler(LAWS[trial % 4], rng, N)
        T = a * (Y - m) ** 2 + v
        h = 0.01
        edges = v + np.sign(a) * np.arange(h, 3, h)
        edges.sort()
        cnt, _ = np.histogram(T, bins=edges)
        centers = (edges[:-1] + edges[1:]) / 2
        # compare with the bound integrated over each bin
        d1, d2 = np.abs(edges[:-1] - v), np.abs(edges[1:] - v)
        bnd = 2 * np.abs(np.sqrt(d2) - np.sqrt(d1)) / math.sqrt(abs(a))
        dens = cnt / N
        worst_sq = max(worst_sq, float(np.max(dens / (bnd + 1e-300))))
    record("P1", "lem:square bin masses of a(Y-m)^2+v below the integrated 1/sqrt(|a||z-v|) envelope",
           worst_sq <= 1.02, "max ratio %.4f" % worst_sq)
    for trial in range(8):
        B = rng.normal(size=(2, 2)); B = B @ B.T + 0.1 * np.eye(2)
        if trial % 2: B = -B
        W = np.stack([sampler(LAWS[trial % 4], rng, N), sampler(LAWS[(trial + 1) % 4], rng, N)], 1)
        l = rng.normal(size=2) * 2
        q = np.einsum("ni,ij,nj->n", W, B, W) + W @ l
        cnt, ed = np.histogram(q, bins=4000)
        d = cnt.max() / (N * (ed[1] - ed[0]))
        worst_def = max(worst_def, d * math.sqrt(abs(np.linalg.det(B))) / math.pi)
    record("P2", "lem:definite density of a definite pair <= pi/sqrt(det B)", worst_def <= 1.05,
           "max density*sqrt(det)/pi %.4f" % worst_def)
    for trial in range(8):
        B = rng.normal(size=(2, 2)); B = (B + B.T) / 2
        if np.linalg.det(B) >= 0:
            B[0, 1] = B[1, 0] = math.sqrt(abs(B[0, 0] * B[1, 1])) + 0.5
        D = abs(np.linalg.det(B))
        W = np.stack([sampler(LAWS[trial % 4], rng, N), sampler(LAWS[(trial + 2) % 4], rng, N)], 1)
        w0 = rng.normal(size=2); v = rng.normal()
        q = np.einsum("ni,ij,nj->n", W - w0, B, W - w0) + v
        h = 0.002
        edges = np.arange(v - 4, v + 4 + h, h)
        cnt, _ = np.histogram(q, bins=edges)
        cen = (edges[:-1] + edges[1:]) / 2
        env = (6 + np.maximum(0, np.log(16 * math.sqrt(D) / np.maximum(np.abs(cen - v) - h, 1e-12)))) / math.sqrt(D)
        worst_hyp = max(worst_hyp, float(np.max(cnt / (N * h) / env)))
    record("P3", "lem:hyperbola density of an indefinite pair below D^{-1/2}(6+log+(16 sqrt D/|z-v|))",
           worst_hyp <= 1.0, "max density/envelope %.4f" % worst_hyp)


def check_concentration(rng, quick):
    N = 400_000 if quick else 2_000_000
    worst = 0.0
    worst_log = 0.0
    for trial in range(16):
        n = rng.integers(2, 7)
        S = rng.normal(size=(n, n)); S = (S + S.T) / 2
        if trial % 2:
            S[np.diag_indices(n)] = 0.01
        L = np.linalg.norm(S, 2)
        b = rng.normal(size=n) * 2; c = rng.normal()
        Xs = draw(n, N, rng, [LAWS[(trial + i) % 4] for i in range(n)])
        R = qvals(Xs, S, b, c)
        Rs = np.sort(R)
        for rho in [1e-3, 1e-2, 1e-1] :
            # worst window of half-width rho: max over centres of the count
            lo = np.searchsorted(Rs, Rs - 2 * rho, side="left")
            cnt = np.arange(len(Rs)) - lo + 1
            p = cnt.max() / N
            worst = max(worst, p / min(1.0, 19 * math.sqrt(rho / L)))
        if L >= 1:
            for a in np.quantile(R, [0.1, 0.5, 0.9]):
                worst_log = max(worst_log, float(np.mean(np.maximum(0, -np.log(np.abs(R - a) + 1e-300)))))
    record("P4", "lem:concentration P(|R-a|<rho) <= 19 sqrt(rho/||S||) (worst window, Monte Carlo)",
           worst <= 1.0, "max ratio %.4f" % worst)
    record("P5", "lem:concentration E log+(1/|R-a|) <= L0 when ||S|| >= 1", worst_log <= 2 + 2 * math.log(19),
           "max %.3f vs L0 %.3f" % (worst_log, 2 + 2 * math.log(19)))


def check_pairhalf(rng, quick):
    """lem:pairhalf: E|q(W)-a|^{-1/2} <= 16 D^{-1/4} for a quadratic polynomial in two independent coordinates."""
    N = 1_000_000 if quick else 4_000_000
    worst = 0.0
    for trial in range(12):
        B = rng.normal(size=(2, 2)); B = (B + B.T) / 2
        if trial % 3 == 0:  # nearly degenerate quadratic part
            w, Vv = np.linalg.eigh(B)
            w[np.argmin(np.abs(w))] = rng.choice([-1.0, 1.0]) * 1e-3
            B = Vv @ np.diag(w) @ Vv.T
        if trial % 4 == 1:  # force definite
            w, Vv = np.linalg.eigh(B); B = Vv @ np.diag(np.abs(w) + 0.05) @ Vv.T
        D = abs(np.linalg.det(B))
        W = np.stack([sampler(LAWS[trial % 4], rng, N), sampler(LAWS[(trial + 1) % 4], rng, N)], 1)
        l = rng.normal(size=2); c = rng.normal()
        q = np.einsum("ni,ij,nj->n", W, B, W) + W @ l + c
        w0 = -np.linalg.solve(B, l) / 2
        v = float(w0 @ B @ w0 + l @ w0 + c)
        for a in [v] + list(np.quantile(q, [0.05, 0.25, 0.5, 0.75, 0.95])):
            hp = float(np.mean(np.abs(q - a) ** -0.5))
            worst = max(worst, hp * D ** 0.25 / 16)
    record("P6", "lem:pairhalf E|q(W)-a|^{-1/2} <= 16 D^{-1/4} (definite, indefinite, nearly degenerate; centre at the critical value and at quantiles)",
           worst <= 1.0, "max E|q-a|^{-1/2} D^{1/4}/16 = %.4f" % worst)


def lowrank_sign(rng, n, rank, s_index):
    """Symmetric, zero diagonal, U diag(lam) U^T with sign vectors; scaled so that s_{s_index} = 1.0001."""
    U = rng.choice([-1.0, 1.0], size=(n, rank)) / math.sqrt(n)
    lam = rng.choice([-1.0, 1.0], size=rank) * rng.uniform(1.0, 1.6, rank)
    A = (U * lam) @ U.T
    np.fill_diagonal(A, 0.0)
    ev = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
    return A / ev[s_index - 1] * 1.0001


def check_halfpotential(rng, quick):
    """prop:halfpotential: s_5(A) >= 1 gives sup_a E|Q-a|^{-1/2} <= 82, with a pivot of the smallest allowed size."""
    N = 250_000 if quick else 1_000_000
    worst = 0.0
    rows = []
    for trial in range(12):
        n = 120
        A = lowrank_sign(rng, n, 6, 5)
        kind = trial % 4
        if kind == 0:    # a diagonal pivot of size exactly eta
            A[0, 0] = 3 / 40
        elif kind == 1:  # a definite pair with determinant exactly zeta
            A[0, 0] = A[1, 1] = 0.05; A[0, 1] = A[1, 0] = 0.0
        elif kind == 2:  # an indefinite pair with determinant exactly -zeta
            A[0, 0] = A[1, 1] = 0.0; A[0, 1] = A[1, 0] = 0.05
        ev = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
        if ev[4] < 1:
            A = A / ev[4]
        laws = ["centred"] if trial % 2 == 0 else ["uniform"]
        Xs = draw(n, N, rng, laws)
        Q = qvals(Xs, A, np.zeros(n), 0.0)
        cnt, ed = np.histogram(Q, bins=400)
        mode = float((ed[np.argmax(cnt)] + ed[np.argmax(cnt) + 1]) / 2)
        for a in [mode] + list(np.quantile(Q, [0.1, 0.5, 0.9])):
            hp = float(np.mean(np.abs(Q - a) ** -0.5))
            worst = max(worst, hp)
        rows.append(kind)
    record("P7", "prop:halfpotential sup_a E|Q-a|^{-1/2} <= 82 when s_5(A) >= 1 (diagonal pivot of size eta, pairs of determinant +-zeta, no pivot)",
           worst <= 82, "max %.3f" % worst)


# ---------------------------------------------------------------- disjoint minors
def ordered_disjoint_pairs(n, r):
    for S in itertools.combinations(range(n), r):
        rest = [i for i in range(n) if i not in S]
        for T in itertools.combinations(rest, r):
            yield S, T


def V(A, r):
    if r == 0:
        return 1.0
    n = A.shape[0]
    return sum(np.linalg.det(A[np.ix_(S, T)]) ** 2 for S, T in ordered_disjoint_pairs(n, r))


def check_minors(rng):
    bad_samp = bad_dec = 0
    worst_ratio = 0.0
    for trial in range(60):
        n = rng.integers(5, 9)
        A = rng.normal(size=(n, n)); A = (A + A.T) / 2
        if trial % 3 == 0:  # near low rank: small ratios V_{r+1}/V_r
            w, Vv = np.linalg.eigh(A); w[np.argsort(np.abs(w))[: n - 3]] *= 1e-3; A = Vv @ np.diag(w) @ Vv.T
        for r in (1, 2):
            if 2 * (r + 1) > n:
                continue
            Vr, Vr1 = V(A, r), V(A, r + 1)
            tot = 0.0
            for S, T in ordered_disjoint_pairs(n, r):
                B = A[np.ix_(S, T)]
                dB = np.linalg.det(B)
                if abs(dB) < 1e-14:
                    continue
                P = A[:, list(T)] @ np.linalg.solve(B, A[list(S), :])
                Lset = [i for i in range(n) if i not in S and i not in T]
                F = sum((A[i, j] - P[i, j]) ** 2 for i in Lset for j in Lset if i != j)
                tot += dB ** 2 / Vr * F
                # decomposition of lem:completion
                D = np.zeros((n, n)); E = np.zeros((n, n))
                for i in Lset:
                    D[i, i] = A[i, i] - P[i, i]
                    for j in Lset:
                        if i != j:
                            E[i, j] = A[i, j] - P[i, j]
                R = A - D - E
                ok = (np.linalg.matrix_rank(R, tol=1e-8 * max(1, np.abs(R).max())) <= 3 * r
                      and np.allclose(R[np.ix_(Lset, Lset)], P[np.ix_(Lset, Lset)])
                      and np.linalg.matrix_rank(P[np.ix_(Lset, Lset)], tol=1e-8 * max(1, np.abs(P).max())) <= r
                      and np.allclose(P[list(S), :], A[list(S), :]) and np.allclose(P[:, list(T)], A[:, list(T)]))
                bad_dec += not ok
            bound = (r + 1) ** 2 * Vr1 / Vr
            bad_samp += tot > bound * (1 + 1e-9) + 1e-12
            if bound > 0:
                worst_ratio = max(worst_ratio, tot / bound)
    record("M1", "lem:sampling E_w sum (a_ij-P_ij)^2 <= (r+1)^2 V_{r+1}/V_r (exact enumeration, r=1,2)",
           bad_samp == 0, "violations %d, max ratio %.4f" % (bad_samp, worst_ratio))
    record("M2", "lem:completion rank R <= 3r, R_LL = P_LL, rank P_LL <= r, interpolation (every seed)",
           bad_dec == 0, "violations %d" % bad_dec)

    bad = 0
    for trial in range(40):
        n = rng.integers(4, 11)
        A = rng.normal(size=(n, n)); A = (A + A.T) / 2
        for k in (1, 2, 3):
            if 2 * k > n:
                continue
            Vk = V(A, k)
            tot = 0.0
            for mask in range(2 ** n):
                I = [i for i in range(n) if mask >> i & 1]
                J = [i for i in range(n) if not mask >> i & 1]
                if len(I) >= k and len(J) >= k:
                    tot += e_ell(A[np.ix_(I, J)], k)
            bad += abs(tot / 2 ** n - Vk / 4 ** k) > 1e-7 * max(1, Vk)
    record("M3", "lem:cut average of E_k(A_IJ) over all 2^n partitions equals 4^-k V_k(A)", bad == 0,
           "violations %d" % bad)


def no_pivot(A):
    """No diagonal entry of modulus >= 3/40 and no principal 2x2 minor of modulus >= 1/400."""
    d = np.diag(A)
    dets = np.abs(np.outer(d, d) - A ** 2)
    np.fill_diagonal(dets, 0)
    return np.abs(d).max() < 3 / 40 and dets.max() < 1 / 400


def nopivot_matrix(rng, n, target, rank=None, diag=0.0):
    """Symmetric, no pivot (eta = 3/40, zeta = 1/400), with s_target(A) = 1.0001 (None if not found).

    rank=None: bounded-entry sign matrix, entries 0 or +-0.045 with density 0.45 (a Wigner matrix whose entries stay
    below sqrt(zeta)); otherwise a sign-vector matrix of the given rank. `diag` is a constant diagonal or "mixed"
    (uniform on [-0.02, 0.02]); it is added before the final scaling."""
    for _ in range(200):
        if rank is None:
            G = rng.choice([-0.045, 0.045], size=(n, n)) * (rng.random((n, n)) < 0.45)
            A = np.triu(G, 1); A = A + A.T
        else:
            U = rng.choice([-1.0, 1.0], size=(n, rank)) / math.sqrt(n)
            lam = rng.choice([-1.0, 1.0], size=rank) * rng.uniform(1.0, 1.6, rank)
            A = (U * lam) @ U.T
            np.fill_diagonal(A, 0.0)
        ev = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
        if ev[target - 1] <= 0:
            continue
        if rank is not None:
            A = A / ev[target - 1]
        np.fill_diagonal(A, rng.uniform(-0.02, 0.02, n) if diag == "mixed" else float(diag))
        ev = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
        A = A / ev[target - 1] * 1.0001
        if no_pivot(A):
            return A
    return None


def check_volume(rng, quick):
    kappa = 4 / 625
    worst = {2: math.inf, 3: math.inf}
    made = {2: 0, 3: 0}
    for trial in range(8 if quick else 20):
        for k, target in ((2, 5), (3, 9)):
            wigner = bool(trial % 2)
            n = 400 if wigner else int(rng.choice([400, 500, 600]))
            diag = [0.0, 0.04, -0.04, "mixed"][(trial // 2) % 4]
            A = nopivot_matrix(rng, n, target, rank=None if wigner else target + int(rng.integers(0, 4)), diag=diag)
            if A is None:
                continue
            assert no_pivot(A)
            assert np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1][target - 1] >= 1
            est = np.mean([e_ell(A[np.ix_(I, J)], k) for I, J in
                           ((np.where(m)[0], np.where(~m)[0]) for m in (rng.random(n) < 0.5 for _ in range(40)))])
            Vk_est = 4 ** k * est
            worst[k] = min(worst[k], Vk_est / kappa ** k)
            made[k] += 1
    record("V1", "prop:volume V_k(A) >= kappa^k = (4/625)^k for no-pivot matrices with s_{4k-3} >= 1 (k=2,3; unbiased cut estimator)",
           all(worst[k] >= 1 for k in (2, 3)) and made[2] > 0 and made[3] > 0,
           "matrices %s, min V_k/kappa^k: k=2 %.3g, k=3 %.3g" % (made, worst[2], worst[3]))


# ---------------------------------------------------------------- the theorem end to end
def check_theorem(rng, quick):
    N = 1_000_000 if quick else 4_000_000
    worst = 0.0
    rows = []
    for trial in range(16 if quick else 40):
        n = int(rng.integers(9, 16))
        kind = trial % 8
        tight = trial % 2 == 0 or kind >= 4
        if kind == 0:   # random eigenbasis, nine unit eigenvalues of random signs
            Qm, _ = np.linalg.qr(rng.normal(size=(n, n)))
            lam = np.zeros(n); lam[:9] = rng.choice([-1, 1], 9); lam[9:] = rng.normal(size=n - 9) * 0.3
            A = (Qm * lam) @ Qm.T
        elif kind == 1:  # diagonal
            A = np.diag(np.concatenate([rng.choice([-1, 1], 9), rng.normal(size=n - 9) * 0.1]))
        elif kind == 2:  # hyperbolic pairs x_i y_i, the logarithmic building block
            n = max(n, 12)
            A = np.zeros((n, n))
            for i in range(0, 18 if n >= 18 else n - 1, 2):
                A[i, i + 1] = A[i + 1, i] = 1.0
            for _guard in range(500):
                if (np.abs(np.linalg.eigvalsh(A)) >= 1 - 1e-12).sum() >= 9:
                    break
                i, j = rng.integers(0, n, 2)
                if i != j:
                    A[i, j] = A[j, i] = 1.0
        elif kind == 3:  # spread, no pivot: small entries, rank nine
            A = nopivot_matrix(rng, 200, 9, rank=9)
            n = A.shape[0]
        elif kind == 4:  # nine unit squares
            A = np.diag(np.concatenate([np.ones(9), np.zeros(n - 9)]))
        elif kind == 5:  # five positive and four negative squares: the level set through 0 is a cone
            A = np.diag(np.concatenate([np.ones(5), -np.ones(4), np.zeros(n - 9)]))
        elif kind == 6:  # nine hyperbolic pairs in 18 variables
            n = 18
            A = np.zeros((n, n))
            for i in range(0, 18, 2):
                A[i, i + 1] = A[i + 1, i] = 1.0
        else:            # one heavy coordinate coupled to all others plus nine unit directions
            Qm, _ = np.linalg.qr(rng.normal(size=(n, n)))
            lam = np.zeros(n); lam[:9] = rng.choice([-1, 1], 9)
            A = (Qm * lam) @ Qm.T
            A[0, 1:] += 3.0; A[1:, 0] += 3.0
        ev = np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]
        s = ev[8]
        b = rng.normal(size=n) * rng.choice([0, 1, 5]) if not tight else np.zeros(n)
        c = rng.normal()
        chunks = []
        per = max(10_000, min(N, 20_000_000 // n))
        for start in range(0, N, per):
            laws = (["centred"] if trial % 4 in (0, 1) else ["uniform"]) if tight else [LAWS[(trial + i) % 4] for i in range(n)]
            Xs = draw(n, min(per, N - start), rng, laws)
            chunks.append(qvals(Xs, A, b, c))
        Q = np.concatenate(chunks)
        h = max(0.005 * np.std(Q), 1e-3)
        cnt, ed = np.histogram(Q, bins=np.arange(Q.min(), Q.max() + h, h))
        d = cnt.max() / (N * h)
        worst = max(worst, d * s)
        rows.append({"n": n, "kind": kind, "tight_laws": bool(tight), "s9": float(s), "max_density": float(d),
                     "max_density_times_s9": float(d * s)})
    record("T1", "thm:main Monte Carlo density of Q times s_9 far below 400 (structured and adversarial instances)",
           worst < 400, "max density*s_9 = %.3f" % worst)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--out", default="results.json")
    ap.add_argument("--skip-t1", action="store_true", help="skip T1 (the end-to-end test also run by t1_tight.py)")
    args = ap.parse_args()
    rng = np.random.default_rng(20260924)
    t0 = time.time()
    summary = {"constants": check_constants()}
    check_identities()
    check_linear_algebra(rng)
    check_bl(rng)
    check_entropy(rng)
    check_decay(rng, args.quick)
    check_decoupling(rng, args.quick)
    check_pivots(rng, args.quick)
    check_concentration(rng, args.quick)
    check_pairhalf(rng, args.quick)
    check_halfpotential(rng, args.quick)
    check_minors(rng)
    check_volume(rng, args.quick)
    if not args.skip_t1:
        summary["theorem_rows"] = check_theorem(rng, args.quick)
    summary["results"] = RESULTS
    summary["all_pass"] = all(r["pass"] for r in RESULTS)
    summary["seconds"] = round(time.time() - t0, 1)
    json.dump(summary, open(args.out, "w", encoding="utf-8"), indent=1)
    print("ALL PASS" if summary["all_pass"] else "SOME FAILED", "in", summary["seconds"], "s", flush=True)
    return 0 if summary["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
