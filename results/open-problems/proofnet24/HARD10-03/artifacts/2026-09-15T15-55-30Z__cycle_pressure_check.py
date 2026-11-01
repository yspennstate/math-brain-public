#!/usr/bin/env python3
"""Numerical sanity checks for HARD10-03 NEW-L8--NEW-L10.

This script is not a proof.  It builds the principal matrix of the exact
continuous-time SRW heat kernel on finite cubes in Z^3 using

    p_t(x,y) = prod_j exp(-2t) I_{|x_j-y_j|}(2t),

and checks the exact determinant sandwich

    1-exp(-tau) <= 1-det(I-K) <= tau,
    tau = |S| p_t(0,0),

as well as the q-fugacity determinant and the normalized pressure scale.
The analytic proof is in the matching run report.
"""

import math
import itertools
import numpy as np
from scipy.special import ive, zeta


def heat_1d(t, n):
    # ive(n,2t) = exp(-2t) I_n(2t) for t>0.
    return float(ive(abs(int(n)), 2.0 * t))


def heat_3d(t, x, y):
    out = 1.0
    for a, b in zip(x, y):
        out *= heat_1d(t, a - b)
    return out


def cube(radius):
    return list(itertools.product(range(-radius, radius + 1), repeat=3))


def kernel_matrix(t, pts):
    n = len(pts)
    K = np.empty((n, n), dtype=float)
    for i, x in enumerate(pts):
        for j, y in enumerate(pts):
            K[i, j] = heat_3d(t, x, y)
    return K


def logdet_I_minus_qK(K, q):
    sign, logabs = np.linalg.slogdet(np.eye(K.shape[0]) - q * K)
    if sign <= 0:
        raise RuntimeError("I-qK did not have positive determinant")
    return logabs


def check(t=8.0, radius=2, qs=(0.25, 0.5, 1.0)):
    pts = cube(radius)
    K = kernel_matrix(t, pts)
    eig = np.linalg.eigvalsh(K)
    p0 = heat_3d(t, (0, 0, 0), (0, 0, 0))
    tau = len(pts) * p0

    logdet = logdet_I_minus_qK(K, 1.0)
    event_prob = 1.0 - math.exp(logdet)
    lower = 1.0 - math.exp(-tau)
    upper = min(1.0, tau)

    assert eig.min() > -1e-12
    assert eig.max() < 1.0 + 1e-12
    assert lower - 2e-12 <= event_prob <= upper + 2e-12

    kappa = float(zeta(2.5, 1.0)) / (4.0 * math.pi) ** 1.5
    rows = []
    for q in qs:
        pressure = -logdet_I_minus_qK(K, q)
        normalized = (t ** 1.5 / len(pts)) * pressure
        rows.append((q, pressure, normalized))

    return {
        "t": t,
        "radius": radius,
        "vertices": len(pts),
        "p_t_00": p0,
        "tau": tau,
        "event_probability_from_determinant": event_prob,
        "sandwich_lower": lower,
        "sandwich_upper": upper,
        "min_eigenvalue": float(eig.min()),
        "max_eigenvalue": float(eig.max()),
        "kappa_3_zeta_5_2_over_4pi_3_2": kappa,
        "q_pressure_rows": rows,
    }


if __name__ == "__main__":
    for t, radius in [(4.0, 1), (8.0, 2), (16.0, 2)]:
        print(check(t=t, radius=radius))
