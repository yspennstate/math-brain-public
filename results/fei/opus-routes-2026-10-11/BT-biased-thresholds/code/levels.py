"""Exact-structure (high precision) spectra of functions of group counts.

Coordinates are split into groups g = 0..G-1 of sizes m_g with a common bias q_g inside a group.
A function tau(n_0, ..., n_{G-1}) of the group counts (0/1 valued) gives f = 2 tau - 1.
By symmetry inside groups, g_S depends only on k = (|S cap group_g|)_g; it is

    u(k) = prod_g 2^{-k_g} E[ Delta^{k} f (R) ],  R_g ~ Bin(m_g - k_g, q_g)  independent,

and the multiplicity of k is prod_g C(m_g, k_g), with sigma_S^2 = prod_g sigma_g^{2 k_g}.
Everything is computed with mpmath at mp.dps digits.
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 50


def group_matrix(m, q):
    q = mp.mpf(q)
    M = mp.matrix(m + 1, m + 1)
    for k in range(m + 1):
        probs = [mp.binomial(m - k, r) * q ** r * (1 - q) ** (m - k - r) for r in range(m - k + 1)]
        scale = mp.mpf(2) ** (-k)
        coef = [(-1) ** (k - l) * mp.binomial(k, l) * scale for l in range(k + 1)]
        for r in range(m - k + 1):
            pr = probs[r]
            if pr == 0:
                continue
            for l in range(k + 1):
                M[k, r + l] += pr * coef[l]
    return M


def spectrum_2groups(tau, m0, q0, m1, q1):
    """tau: callable (n0, n1) -> 0/1. Returns dict of E (nats), I, V, J, Delta, Hplus, ratio."""
    # work with the 0/1 function tau: for k != 0, u(k) = 2 (M tau)(k); u(0) = 2 E tau - 1.
    F = mp.matrix(m0 + 1, m1 + 1)
    for a in range(m0 + 1):
        for b in range(m1 + 1):
            F[a, b] = tau(a, b)
    M0 = group_matrix(m0, q0)
    M1 = group_matrix(m1, q1)
    U = 2 * (M0 * F * M1.T)
    U[0, 0] = U[0, 0] - 1
    s0 = 4 * mp.mpf(q0) * (1 - mp.mpf(q0))
    s1 = 4 * mp.mpf(q1) * (1 - mp.mpf(q1))
    E = I = V = J = mp.mpf(0)
    rho0 = rho1 = None
    for k0 in range(m0 + 1):
        for k1 in range(m1 + 1):
            if k0 + k1 == 0:
                continue
            u = U[k0, k1]
            if u == 0:
                continue
            mult = mp.binomial(m0, k0) * mp.binomial(m1, k1) * s0 ** k0 * s1 ** k1
            P = mult * u * u
            E += P * mp.log(1 / (u * u))
            I += (k0 + k1) * P
            V += P
            if k0 + k1 >= 2:
                J += (k0 + k1) * P
    Delta = I - V
    out = dict(E=float(E), I=float(I), V=float(V), J=float(J), Delta=float(Delta),
               Hplus=float(E / mp.log(2)))
    out['ratio_HD'] = float(E / mp.log(2) / Delta) if Delta > 0 else float('nan')
    out['ratio_EJ'] = float(E / J) if J > 0 else float('nan')
    out['parseval_err'] = float(abs(V + U[0, 0] ** 2 - 1))
    if m0 >= 1:
        out['rho0'] = float(U[1, 0]) if m0 >= 1 else None
    if m1 >= 1:
        out['rho1'] = float(U[0, 1])
    return out


def spectrum_1group(tau, m, q):
    return spectrum_2groups(lambda a, b: tau(a), m, q, 0, mp.mpf('0.5'))
