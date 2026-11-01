#!/usr/bin/env python3
"""Finite checks for B16 oriented-cut / fractional noisy-square payment.

Support code only. The all-dimensional positive and negative statements are
proved in REPORT.md; this script is for falsification/sanity checks.
Standard library only.
"""
from itertools import product
from math import exp, log
import json
import random


def pc(x):
    return x.bit_count()


def walsh(f):
    a = [float(v) for v in f]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]


def inv_walsh(a):
    b = a[:]
    n = len(b)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = b[j], b[j+h]
                b[j], b[j+h] = x+y, x-y
        h *= 2
    return b


def influence(a):
    return sum(pc(s)*v*v for s, v in enumerate(a))


def cfield(a, rho):
    nbits = (len(a)).bit_length()-1
    ghat = [(rho**pc(s))*v for s, v in enumerate(a)]
    g = inv_walsh(ghat)
    g2 = [x*x for x in g]
    return walsh(g2), g


def flux_fourier(a, C):
    return sum(pc(u)*a[u]*C[u] for u in range(1, len(a)))


def flux_physical(f, g):
    N = len(f)
    n = N.bit_length()-1
    total = 0.0
    for i in range(n):
        bit = 1 << i
        # Every undirected i-edge is visited once, at x with bit i = 0.
        for x in range(N):
            if x & bit:
                continue
            y = x ^ bit
            if f[x] == f[y]:
                continue
            xp, xm = (x, y) if f[x] == 1 else (y, x)
            total += g[xp]*g[xp] - g[xm]*g[xm]
    return total/N


def check_function(f, rho):
    a = walsh(f)
    I = influence(a)
    C, g = cfield(a, rho)
    A0 = sum(v*v for u, v in enumerate(C) if u)
    A1 = sum(pc(u)*v*v for u, v in enumerate(C) if u)
    assert A0 <= (1-rho*rho)*I + 2e-11
    assert A1 <= 4*rho*rho*I + 2e-11

    ff = flux_fourier(a, C)
    fp = flux_physical(f, g)
    assert abs(ff-fp) <= 2e-10
    assert abs(ff) <= 2*rho*I + 2e-11

    # Pointwise interpolation behind Theorem 3.1.
    for theta in (0.25, 0.5, 0.75):
        lhs = sum((pc(u)**theta)*v*v for u, v in enumerate(C) if u)
        rhs = (4**theta)*(rho**(2*theta))*((1-rho*rho)**(1-theta))*I
        assert lhs <= rhs + 3e-11
    return I, A1, ff


def parity_switch_row(m):
    # For f_m(y,z)=A(y)+z B(y), Inf_z=1/2 and
    # sum_{U contains z} C_U(rho)^2 = rho^2(1-rho^(2m))^2/4.
    rho = 1 - 1/m
    Infz = 0.5
    energy = rho*rho*(1-rho**(2*m))**2/4
    point_ratio = energy/((1-rho*rho)*Infz)
    critical = 0.25*sum(
        1/(2*j+3) - 1/(2*(j+m)+3)
        for j in range(m)
    )
    integral_ratio = critical/Infz
    return {
        "m": m,
        "rho": rho,
        "pointwise_coordinate_ratio": point_ratio,
        "critical_integral_over_Inf_z": integral_ratio,
        "asymptotic_point_ratio_over_m": (1-exp(-2))**2/4,
        "asymptotic_integral_ratio_over_log_m": 0.25,
    }


def main():
    rhos = (0.1, 0.25, 0.5, 0.75, 0.9, 0.97)
    rng = random.Random(316021)
    cases = 0
    max_a1 = 0.0
    max_flux = 0.0

    families = []
    for n in range(1, 4):
        N = 1 << n
        families.append([
            [1 if (mask >> x) & 1 else -1 for x in range(N)]
            for mask in range(1 << N)
        ])
    for n in range(4, 7):
        N = 1 << n
        families.append([
            [rng.choice((-1, 1)) for _ in range(N)]
            for _ in range(40)
        ])

    for funcs in families:
        for f in funcs:
            for rho in rhos:
                I, A1, flux = check_function(f, rho)
                if I and rho:
                    max_a1 = max(max_a1, A1/(4*rho*rho*I))
                    max_flux = max(max_flux, abs(flux)/(2*rho*I))
                cases += 1

    rows = [parity_switch_row(m) for m in (8, 16, 32, 64, 128, 256)]
    assert rows[-1]["pointwise_coordinate_ratio"] > 40
    assert rows[-1]["critical_integral_over_Inf_z"] > 1

    out = {
        "status": "PASS",
        "checked_function_noise_cases": cases,
        "max_A1_over_4rho2I": max_a1,
        "max_abs_flux_over_2rhoI": max_flux,
        "parity_switch_rows": rows,
        "claims_checked": [
            "A0 <= (1-rho^2) I",
            "A1 <= 4 rho^2 I",
            "|oriented cut flux| <= 2 rho I",
            "pointwise fractional interpolation theta=1/4,1/2,3/4",
            "parity-switch coordinatewise endpoint-payment obstruction",
        ],
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
