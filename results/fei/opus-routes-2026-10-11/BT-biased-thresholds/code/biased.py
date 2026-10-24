"""Biased (product-measure) Fourier tools for the corrected FEI+ inequality.

Conventions (see NOTES.md section 0):
  y in {0,1}^n, index of a configuration = sum_i y_i 2^i, q[i] = P(y_i = 1).
  f = 2T - 1 in {-1,1}.  g_S = 2^{-|S|} E[d_S f] (butterfly), P(S) = sigma_S^2 g_S^2.
  E = sum_{S != 0} sigma_S^2 g_S^2 ln(1/g_S^2)   (nats);  H+ = E / ln 2 (bits).
"""
from fractions import Fraction
import math
import numpy as np


def ltf_table(w, theta):
    """0/1 truth table of T(y) = 1[sum w_i y_i >= theta], index bit i = y_i."""
    n = len(w)
    idx = np.arange(2 ** n)
    W = np.zeros(2 ** n)
    for i in range(n):
        W += w[i] * ((idx >> i) & 1)
    return (W >= theta - 1e-12).astype(np.int64)


def g_transform(T, q):
    """Float butterfly. T: 0/1 array of length 2^n. Returns g (length 2^n)."""
    n = len(q)
    g = (2.0 * np.asarray(T, dtype=float) - 1.0).copy()
    for i in range(n):
        g = g.reshape(-1, 2, 2 ** i)
        a = g[:, 0, :].copy()
        b = g[:, 1, :].copy()
        g[:, 0, :] = (1 - q[i]) * a + q[i] * b
        g[:, 1, :] = (b - a) / 2.0
        g = g.reshape(-1)
    return g


def sigma2_vector(q):
    n = len(q)
    s = np.ones(1)
    for i in range(n):
        s2 = 4 * q[i] * (1 - q[i])
        s = np.concatenate([s, s * s2])
    return s


def popcount_vector(n):
    c = np.zeros(1, dtype=np.int64)
    for i in range(n):
        c = np.concatenate([c, c + 1])
    return c


def metrics(T, q, with_rho=True):
    """Return dict with E (nats), Hplus (bits), I, V, Delta, J, rho, ratios."""
    q = np.asarray(q, dtype=float)
    n = len(q)
    g = g_transform(T, q)
    s2 = sigma2_vector(q)
    k = popcount_vector(n)
    g2 = g * g
    P = s2 * g2
    nz = (k > 0)
    with np.errstate(divide='ignore', invalid='ignore'):
        lg = np.where(g2 > 0, np.log(1.0 / np.where(g2 > 0, g2, 1.0)), 0.0)
    E = float(np.sum(P[nz] * lg[nz]))
    I = float(np.sum(k * P))
    V = float(np.sum(P[nz]))
    J = float(np.sum((k * P)[k >= 2]))
    Delta = I - V
    out = dict(E=E, Hplus=E / math.log(2), I=I, V=V, Delta=Delta, J=J,
               E2=float(np.sum((P * lg)[k >= 2])))
    if with_rho:
        out['rho'] = np.array([g[1 << i] for i in range(n)])
    out['ratio_HD'] = out['Hplus'] / Delta if Delta > 0 else float('nan')
    out['ratio_EJ'] = E / J if J > 0 else float('nan')
    return out


# ---------------- exact versions -----------------

def g_transform_exact(T, q):
    """Exact butterfly with Fractions. T: list of 0/1 of length 2^n, q: list of Fractions."""
    n = len(q)
    g = [Fraction(2 * t - 1) for t in T]
    half = Fraction(1, 2)
    for i in range(n):
        step = 1 << i
        for base in range(0, len(g), step << 1):
            for c in range(step):
                a = g[base + c]
                b = g[base + c + step]
                g[base + c] = (1 - q[i]) * a + q[i] * b
                g[base + c + step] = (b - a) * half
    return g


def exact_spectrum(T, q):
    """Return list of (S_index, sigma_S^2, g_S) with exact Fractions."""
    n = len(q)
    g = g_transform_exact(T, q)
    s2 = [Fraction(1)]
    for i in range(n):
        si = 4 * q[i] * (1 - q[i])
        s2 = s2 + [x * si for x in s2]
    return [(S, s2[S], g[S]) for S in range(1 << n)]


def exact_checks(T, q):
    """Exact Parseval, Booleanity (convolution) and the monotone identities. Returns dict."""
    n = len(q)
    spec = exact_spectrum(T, q)
    P = [s * g * g for (_, s, g) in spec]
    tot = sum(P)
    I = sum(bin(S).count('1') * P[S] for S in range(1 << n))
    V = tot - P[0]
    return dict(parseval=tot, I=I, V=V, Delta=I - V)


# ---------------- events, TC and the normalization credit -----------------

def law_vector(q):
    """Product probability of every configuration (float)."""
    p = np.ones(1)
    for i in range(len(q)):
        p = np.concatenate([p * (1 - q[i]), p * q[i]])
    return p


def tc_conditional(A, q):
    """Total correlation (nats) of mu conditioned on the 0/1 indicator array A."""
    n = len(q)
    p = law_vector(q) * A
    a = p.sum()
    if a <= 0:
        return 0.0, 0.0
    pc = p / a
    nzm = pc > 0
    H = -np.sum(pc[nzm] * np.log(pc[nzm]))
    idx = np.arange(2 ** n)
    Hm = 0.0
    for i in range(n):
        m1 = pc[((idx >> i) & 1) == 1].sum()
        for x in (m1, 1 - m1):
            if x > 0:
                Hm -= x * math.log(x)
    return Hm - H, a


def credit_terms(T, q):
    """Normalization-credit quantities of paper Lemma bias:credit for monotone T.

    Returns V ln(1/V), sum_i I_i ln^+(4 rho_i / V), I, alpha, alpha*TC(mu_A) for the minority side A.
    """
    m = metrics(T, q)
    V, I, rho = m['V'], m['I'], m['rho']
    q = np.asarray(q, dtype=float)
    s2 = 4 * q * (1 - q)
    Ii = s2 * rho
    with np.errstate(divide='ignore'):
        cr = float(np.sum(Ii * np.maximum(0.0, np.log(np.where(rho > 0, 4 * rho / V, 1.0)))))
    VlnV = V * math.log(1.0 / V) if V > 0 else 0.0
    T = np.asarray(T)
    tc1, a1 = tc_conditional(T, q)
    tc0, a0 = tc_conditional(1 - T, q)
    if a1 <= a0:
        alpha, tc = a1, tc1
    else:
        alpha, tc = a0, tc0
    return dict(VlnV=VlnV, credit=cr, I=I, V=V, alpha=alpha, aTC=alpha * tc, TC=tc,
                excess=VlnV - cr)
