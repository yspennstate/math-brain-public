"""T354 eps > 0 next-order term: an exact x* by a route with no Laplace kernel (agent C, 20 Oct 2026, audit).
Under iid sampling the lag-i term of D is E[g_{k-i} phi(v_k)], v_k = d b2^i g_{k-i}^2 + W_i with W_i independent of g_{k-i}
and cumulants kappa_m(W_i) = d^m kappa_m(g^2) (1/(1 - b2^m) - b2^(i m)). phi(v) = 1/(sqrt(v) + eps) is expanded in Y = v/V - 1
to order J with exact moments of Y given g (from those cumulants). y <= max g^2 / V keeps the truncation error negligible
(J = 10, 14, 18 agree). Root by brentq.  usage: python eps_moment_route.py"""
import math
import sys
import numpy as np
from scipy.optimize import brentq


def series_phi(s, eps, J):
    # coefficients of 1/(s sqrt(1+Y) + eps) in powers of Y
    a = np.array([math.comb(1, 0) if j == 0 else 0 for j in range(J + 1)], float)
    c = 1.0
    sq = np.zeros(J + 1)
    for j in range(J + 1):  # binom(1/2, j)
        sq[j] = c
        c *= (0.5 - j) / (j + 1)
    den = s * sq
    den[0] += eps
    inv = np.zeros(J + 1)
    inv[0] = 1 / den[0]
    for j in range(1, J + 1):
        inv[j] = -sum(den[k] * inv[j - k] for k in range(1, j + 1)) / den[0]
    return inv


def cumulants(vals, p, M):
    mu = float(np.dot(p, vals))
    cm = [float(np.dot(p, (vals - mu) ** m)) for m in range(M + 1)]  # central moments
    k = [0.0] * (M + 1)
    k[1] = mu
    for m in range(2, M + 1):  # cumulants from central moments (kappa_1 dropped)
        k[m] = cm[m] - sum(math.comb(m - 1, j - 1) * k[j] * cm[m - j] for j in range(2, m - 1))
    return k


def D(x, b, d, b1, eps, J=14):
    b2 = 1 - d
    n = len(b)
    g = x + b
    p = np.full(n, 1.0 / n)
    V = float(np.mean(g ** 2))
    s = math.sqrt(V)
    cphi = series_phi(s, eps, J) * 1.0  # phi(V(1+Y)) = 1/(s sqrt(1+Y) + eps)
    kg = cumulants(g ** 2, p, J)
    if b1 == 0:
        lags = np.array([0])
        w = np.array([1.0])
    else:
        L = int(40 / (1 - b1)) + 10
        lags = np.arange(L)
        w = (1 - b1) * b1 ** lags
    tot = np.zeros(len(lags))
    # cumulants of W_i, i = lag: shape (L, J+1)
    kW = np.zeros((len(lags), J + 1))
    for m in range(1, J + 1):
        kW[:, m] = d ** m * kg[m] * (1 / (1 - b2 ** m) - b2 ** (lags * m))
    # central moments of W_i from cumulants (kappa_1 = 0 for the centred part)
    mw = np.zeros((len(lags), J + 1))
    mw[:, 0] = 1
    for m in range(1, J + 1):
        acc = np.zeros(len(lags))
        for k in range(2, m + 1):
            acc += math.comb(m - 1, k - 1) * kW[:, k] * mw[:, m - k]
        mw[:, m] = acc
    mwV = mw / V ** np.arange(J + 1)
    for gv, pv in zip(g, p):
        c = (d * b2 ** lags * gv ** 2 + kW[:, 1]) / V - 1  # mean part of Y given g
        EY = np.zeros((len(lags), J + 1))
        for j in range(J + 1):
            EY[:, j] = sum(math.comb(j, l) * c ** (j - l) * mwV[:, l] for l in range(j + 1))
        tot += pv * gv * (EY @ cphi)
    return float(np.dot(w, tot))


def pred(b, d, b1, eps):
    b2 = 1 - d
    B2, B3 = np.mean(b ** 2), np.mean(b ** 3)
    Z = b ** 2 - B2
    S = np.mean(Z ** 2)
    EbZ2 = np.mean(b * Z ** 2)
    s = math.sqrt(B2)
    r = s / (s + eps)
    K = (1 - b1) / (1 - b1 * b2)
    K2 = (1 - b1) / (1 - b1 * b2 ** 2)
    p2 = s * (eps + 3 * s) / (4 * (eps + s) ** 2)
    p3 = -3 * s * (eps ** 2 + 4 * eps * s + 5 * s ** 2) / (8 * (eps + s) ** 3)
    br = r * K - (p2 / 4) * S / B2 ** 2 - (p2 / r) * (K2 / K) * EbZ2 / (B2 * B3) - (p3 / (2 * r)) * S / B2 ** 2
    x0 = r * d * K * B3 / (2 * B2)
    return x0, br


if __name__ == "__main__":
    models = {"test": np.array([9.0] + [-1.0] * 9), "three": np.array([6.0, 2.0] + [-1.0] * 8)}
    cases = [("test", e, fam) for e in (1, 3, 10) for fam in ("b1_0", "r0.1")] + [("three", 3, "b1_0"), ("three", 3, "r0.1")]
    if "--J" in sys.argv:  # truncation check
        b = models["test"]
        for J in (10, 14, 18):
            x = brentq(lambda t: D(t, b, 0.002, 0, 3, J), 1e-6, 0.1, xtol=1e-16, rtol=1e-15)
            print("J", J, repr(x))
        sys.exit()
    for mname, eps, fam in cases:
        b = models[mname]
        row = []
        for d in (0.002, 0.001, 0.0005):
            b1 = 0.0 if fam == "b1_0" else 1 - d / 0.1
            x0, br = pred(b, d, b1, eps)
            xs = brentq(lambda t: D(t, b, d, b1, eps), 0.3 * x0, 2 * x0, xtol=1e-17, rtol=1e-15)
            row.append((d, (xs / x0 - 1) / d, br))
        rich = 2 * row[2][1] - row[1][1]
        print("%-5s eps %-2s %-4s " % (mname, eps, fam) + "  ".join("d %g exact %.4f pred %.4f" % t for t in row)
              + "  Richardson(1e-3,5e-4) %.4f" % rich, flush=True)
