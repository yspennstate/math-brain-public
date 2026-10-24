"""Checks for 'A Levy random drift destroys compactness for every confining power'.

C1  the energy identity of Lemma 3.2 (energy of the scale profile = 1/(2 Delta s)) on random step potentials;
C2  the deterministic benchmark V = 0: the Dirichlet bottom eigenvalue on [x, 2x] grows for delta = 2, tends to 1/8
    for delta = 1 and to 0 for delta = 1/2 (compact iff delta > 1, as recalled in Section 2 of the source);
C3  a planted downward jump of size m at tau in u = y^delta + V: the Dirichlet bottom eigenvalue near tau is below
    the Rayleigh quotient of the explicit test function and decays like e^{-m}; a jump of the other sign does not
    lower it;
C4  the same for w2 = -|y|^delta with an upward jump (mirror of C3);
C5  illustration on simulated symmetric alpha-stable environments (alpha = 0.5, 1.5; delta = 3 > 1/alpha): the first
    term of the bound at the largest downward jump in the blocks [2^n, 2^(n+1)] goes to 0.
Every printed PASS is an assertion in this file.
"""
from math import gamma, sin, pi

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from scipy.special import logsumexp
from scipy.stats import levy_stable

rng = np.random.default_rng(20261020)
ok = True


def check(name, cond, info=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (" | " + info if info else ""))


# ---------- C1: energy identity for the scale profile on a step potential ----------
for trial in range(5):
    n = 50
    dx = np.diff(np.linspace(0.0, 1.0, n + 1))
    uval = rng.normal(0, 3, n)                        # u constant on each cell
    Ds = np.sum(np.exp(uval) * dx)                    # s(tau) - s(a)
    fprime = np.exp(uval) / Ds                        # f' on each cell, f = (s - s(a)) / Ds
    energy = 0.5 * np.sum(fprime ** 2 * np.exp(-uval) * dx)
    check(f"C1 energy identity, trial {trial}", abs(energy - 0.5 / Ds) <= 1e-12 * (0.5 / Ds),
          f"E={energy:.6e}, 1/(2 Ds)={0.5 / Ds:.6e}")


# ---------- P1 finite elements: E(f,f) = 1/2 int f'^2 e^{-u}, mass int f^2 e^{-u}, Dirichlet ends ----------
def weights(u_mid):
    return np.exp(-(u_mid - u_mid.min()))            # a constant rescaling of the weight leaves eigenvalues fixed


def bottom_eig(nodes, u_mid):
    """Smallest eigenvalue of the P1 pencil (K, M) with Dirichlet ends, by shift-invert at 0 on sparse matrices."""
    w = weights(u_mid)
    h = np.diff(nodes)
    k = 0.5 * w / h                    # element stiffness coefficient
    mm = w * h / 6                     # element mass coefficient
    Kd = k[:-1] + k[1:]
    Ko = -k[1:-1]
    Md = 2 * (mm[:-1] + mm[1:])
    Mo = mm[1:-1]
    K = diags([Ko, Kd, Ko], [-1, 0, 1], format="csc")
    M = diags([Mo, Md, Mo], [-1, 0, 1], format="csc")
    vals = eigsh(K, k=1, M=M, sigma=0.0, which="LM", return_eigenvectors=False)
    return float(vals[0])


def rayleigh(nodes, u_mid, f):
    w = weights(u_mid)
    h = np.diff(nodes)
    fp = np.diff(f) / h
    fm2 = (f[:-1] ** 2 + f[:-1] * f[1:] + f[1:] ** 2) / 3   # exact cell mean of f^2 for linear f
    return 0.5 * np.sum(fp ** 2 * w * h) / np.sum(fm2 * w * h)


# ---------- C2: deterministic benchmark ----------
# For smooth u the substitution g = f e^{-u/2} turns E(f,f)/||f||^2 into the Schrodinger form
# (1/2) int g'^2 + int Phi g^2 over int g^2, Phi = u'^2/8 - u''/4 (Dirichlet ends kill the boundary terms),
# which avoids the weight's dynamic range (e^{-77000} on [160, 320] for delta = 2).
def bottom_schrodinger(x0, x1, delta, n=4000):
    y = np.linspace(x0, x1, n + 2)[1:-1]
    hh = (x1 - x0) / (n + 1)
    phi = delta ** 2 * y ** (2 * delta - 2) / 8 - delta * (delta - 1) * y ** (delta - 2) / 4
    main = 1.0 / hh ** 2 + phi
    off = -0.5 / hh ** 2 * np.ones(n - 1)
    from scipy.linalg import eigh_tridiagonal
    return eigh_tridiagonal(main, off, select="i", select_range=(0, 0), eigvals_only=True)[0]


res = {}
for delta in (2.0, 1.0, 0.5):
    vals = []
    for x in (10.0, 40.0, 160.0):
        vals.append(bottom_schrodinger(x, 2 * x, delta))
    res[delta] = vals
    print(f"     C2 delta={delta}: Dirichlet bottom on [x,2x], x=10,40,160: " + ", ".join(f"{v:.5f}" for v in vals))
check("C2 delta=2 grows", res[2.0][0] < res[2.0][1] < res[2.0][2] and res[2.0][2] > 100)
check("C2 delta=1 near 1/8", all(abs(v - 0.125) < 0.01 for v in res[1.0][1:]))
check("C2 delta=1/2 decreases to 0", res[0.5][0] > res[0.5][1] > res[0.5][2] and res[0.5][2] < 0.01)


# ---------- C3/C4: planted jump ----------
def planted(delta, m, tau, sign_w, jump_up, nper=4000):
    """u = sign_w * y^delta + V with V = +-m 1{y >= tau}, on the window [tau-1, tau+1].
    Returns (Dirichlet bottom on the window, Rayleigh quotient of the explicit test function, h)."""
    h = min(0.5, (2 * tau) ** (1 - delta)) if delta > 1 else 0.5
    A, B = tau - 1.0, tau + 1.0
    nodes = np.unique(np.concatenate([np.linspace(A, B, nper + 1), [tau - h, tau, tau + h]]))
    mid = 0.5 * (nodes[1:] + nodes[:-1])
    V = np.where(mid >= tau, (m if jump_up else -m), 0.0)
    u = sign_w * mid ** delta + V
    lam = bottom_eig(nodes, u)
    s = np.concatenate([[0.0], np.cumsum(np.exp(u - u.max()) * np.diff(nodes))])   # rescaled scale function
    f = np.zeros_like(nodes)
    if sign_w > 0:   # w1: rise along the scale on [tau-h, tau], plateau, linear cutoff on [tau+0.5, tau+0.75]
        i0, i1 = np.searchsorted(nodes, tau - h), np.searchsorted(nodes, tau)
        f[i0:i1 + 1] = (s[i0:i1 + 1] - s[i0]) / (s[i1] - s[i0])
        f[(nodes >= tau) & (nodes <= tau + 0.5)] = 1.0
        sel = (nodes > tau + 0.5) & (nodes <= tau + 0.75)
        f[sel] = 1.0 - (nodes[sel] - tau - 0.5) / 0.25
    else:            # w2: linear rise on [tau-0.75, tau-0.5], plateau, fall along the scale on [tau, tau+h]
        sel = (nodes >= tau - 0.75) & (nodes < tau - 0.5)
        f[sel] = (nodes[sel] - tau + 0.75) / 0.25
        f[(nodes >= tau - 0.5) & (nodes <= tau)] = 1.0
        i0, i1 = np.searchsorted(nodes, tau), np.searchsorted(nodes, tau + h)
        f[i0:i1 + 1] = (s[i1] - s[i0:i1 + 1]) / (s[i1] - s[i0])
    return lam, rayleigh(nodes, u, f), h


for label, sign_w, up in (("C3 w1 downward jump", +1, False), ("C4 w2 upward jump", -1, True)):
    prev = None
    for m in (4.0, 8.0, 12.0):
        lam, R, h = planted(2.0, m, 6.0, sign_w, up)
        print(f"     {label}, delta=2, tau=6, h={h:.4f}, m={m}: lambda_D={lam:.3e}, Rayleigh={R:.3e}")
        check(f"{label} m={m}: lambda_D <= Rayleigh", lam <= R * (1 + 1e-9))
        if prev is not None:
            check(f"{label} m={m}: lambda_D drops by at least e^-2 per +4 in m", lam <= prev * np.exp(-2.0),
                  f"ratio {lam / prev:.3e}")
        prev = lam
    lam_wrong = planted(2.0, 12.0, 6.0, sign_w, not up)[0]
    lam_none = planted(2.0, 0.0, 6.0, sign_w, up)[0]
    print(f"     {label}: other-sign jump m=12 lambda_D={lam_wrong:.3e}; no jump lambda_D={lam_none:.3e}")
    check(f"{label}: a jump of the other sign does not lower the bottom", lam_wrong >= 0.5 * lam_none)

# ---------- C5: illustration on simulated symmetric alpha-stable environments ----------
# levy_stable(alpha, 0, scale 1) has P(X_1 < -t) ~ Ca t^-alpha with Ca = Gamma(alpha) sin(pi alpha/2)/pi, so the
# downward jumps below -x in a block of length L form a Poisson number with mean ~ L Ca x^-alpha. We draw the largest
# downward jump in [2^n, 2^(n+1)], simulate the environment's increments on [tau-h, tau+h] at resolution h/400, and
# evaluate log10 of the first term 1/(2 Ds mu(tau, tau+h)) of Lemma 3.2 by quadrature.
delta = 3.0
for alpha in (0.5, 1.5):
    Ca = gamma(alpha) * sin(pi * alpha / 2) / pi
    logs = []
    for n in range(2, 21, 3):
        L = 2.0 ** n
        m = (L * Ca / (-np.log(rng.random()))) ** (1 / alpha)
        tau = L + rng.random() * L
        h = min(1.0, (2 * tau) ** (1 - delta))
        k = 400
        dt = h / k
        incL = levy_stable.rvs(alpha, 0.0, scale=dt ** (1 / alpha), size=k, random_state=rng)
        incR = levy_stable.rvs(alpha, 0.0, scale=dt ** (1 / alpha), size=k, random_state=rng)
        VL = -np.cumsum(incL[::-1])[::-1]          # V(y) - V(tau-) on the left window, V(tau-) := 0
        VR = -m + np.concatenate([[0.0], np.cumsum(incR[:-1])])
        yL = tau - h + dt * (np.arange(k) + 0.5)
        yR = tau + dt * (np.arange(k) + 0.5)
        c0 = tau ** delta
        # y^delta - tau^delta without cancellation: tau^delta * expm1(delta * log1p((y - tau)/tau))
        uL = c0 * np.expm1(delta * np.log1p((yL - tau) / tau)) + VL
        uR = c0 * np.expm1(delta * np.log1p((yR - tau) / tau)) + VR
        logDs = np.log(dt) + logsumexp(uL)
        logmu = np.log(dt) + logsumexp(-uR)
        lb = (np.log(0.5) - logDs - logmu) / np.log(10)
        logs.append(lb)
        print(f"     C5 alpha={alpha} n={n:2d} tau={tau:.3e} jump={m:.3e} h={h:.2e} log10 first term={lb:.1f}")
    check(f"C5 alpha={alpha}: first term below 1e-3 in the last three blocks", max(logs[-3:]) < -3)

print("ALL PASS" if ok else "SOME CHECK FAILED")
