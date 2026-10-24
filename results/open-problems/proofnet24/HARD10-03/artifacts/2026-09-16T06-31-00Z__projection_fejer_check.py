#!/usr/bin/env python3
"""Finite-state sanity checker for HARD10-03 NEW-L61--NEW-L63.

This is not a proof. It enumerates interchange on C4, computes the exact
finite-state semigroup by matrix exponentiation, and checks:
  * divisor / Mobius inversion for root-cycle lengths;
  * direct finite-cycle projection kernel = cycle autocorrelation kernel;
  * Fourier transform = finite-cycle form factor;
  * the pathwise Fejer inequality on every permutation state.
"""

import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm

N = 4
T = 0.7
EDGES = [(0, 1), (1, 2), (2, 3), (3, 0)]
PERMS = list(itertools.permutations(range(N)))
INDEX = {p: i for i, p in enumerate(PERMS)}


def left_transpose(p, edge):
    u, v = edge
    return tuple(v if y == u else u if y == v else y for y in p)


def root_cycle(p, root=0):
    out = []
    x = root
    while True:
        out.append(x)
        x = p[x]
        if x == root:
            return out


def power_image(p, k, x=0):
    for _ in range(k):
        x = p[x]
    return x


def mobius(n):
    if n == 1:
        return 1
    m = n
    primes = 0
    q = 2
    while q * q <= m:
        if m % q == 0:
            m //= q
            primes += 1
            if m % q == 0:
                return 0
            while m % q == 0:
                m //= q
        q += 1
    if m > 1:
        primes += 1
    return -1 if primes % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def main():
    q = np.zeros((len(PERMS), len(PERMS)))
    for i, p in enumerate(PERMS):
        for edge in EDGES:
            j = INDEX[left_transpose(p, edge)]
            q[i, j] += 1.0
            q[i, i] -= 1.0

    identity = tuple(range(N))
    law = expm(T * q)[INDEX[identity]]

    # Cycle-length probabilities.
    p_len = np.zeros(N + 1)
    for prob, p in zip(law, PERMS):
        p_len[len(root_cycle(p))] += prob

    # Power returns and arithmetic Mobius inversion.
    a = np.zeros(N + 1)
    for k in range(1, N + 1):
        a[k] = sum(
            prob for prob, p in zip(law, PERMS) if power_image(p, k) == 0
        )
    p_mob = np.zeros(N + 1)
    for ell in range(1, N + 1):
        p_mob[ell] = sum(mobius(ell // d) * a[d] for d in divisors(ell))
    mobius_error = float(np.max(np.abs(p_mob[1:] - p_len[1:])))

    # Direct G(x) and point-shift autocorrelation version on the transitive C4.
    g_direct = np.zeros(N)
    g_auto = np.zeros(N)
    for prob, p in zip(law, PERMS):
        cyc = root_cycle(p)
        L = len(cyc)
        cycset = set(cyc)
        for x in range(N):
            if x in cycset:
                g_direct[x] += prob / L
            count = sum(1 for u in cyc if (u + x) % N in cycset)
            g_auto[x] += prob * count / (L * L)
    autocorr_error = float(np.max(np.abs(g_direct - g_auto)))

    # Fourier form factor.
    g_hat = np.zeros(N, dtype=complex)
    form_factor = np.zeros(N, dtype=complex)
    for k in range(N):
        theta = 2.0 * math.pi * k / N
        g_hat[k] = sum(g_direct[x] * np.exp(1j * theta * x) for x in range(N))
        for prob, p in zip(law, PERMS):
            cyc = root_cycle(p)
            L = len(cyc)
            amp = sum(np.exp(1j * theta * u) for u in cyc) / L
            form_factor[k] += prob * abs(amp) ** 2
    form_factor_error = float(np.max(np.abs(g_hat - form_factor)))
    min_form_factor = float(np.min(form_factor.real))

    # Pathwise Fejer inequality for all permutations, Fourier modes and H<=6.
    fejer_max_violation = 0.0
    fejer_cases = 0
    for p in PERMS:
        cyc = root_cycle(p)
        L = len(cyc)
        for k in range(N):
            theta = 2.0 * math.pi * k / N
            z = np.array([np.exp(1j * theta * u) for u in cyc])
            A = np.mean(z)
            lhs = abs(A) ** 2
            for H in range(1, 7):
                rhs = 1.0 / H
                for r in range(1, H):
                    B = np.mean(
                        [z[(j + r) % L] * np.conjugate(z[j]) for j in range(L)]
                    )
                    rhs += 2.0 * (H - r) * B.real / (H * H)
                fejer_max_violation = max(fejer_max_violation, float(lhs - rhs))
                fejer_cases += 1

    result = {
        "graph": "C4",
        "time": T,
        "number_of_permutations": len(PERMS),
        "law_mass_error": float(abs(np.sum(law) - 1.0)),
        "cycle_length_probabilities": {str(i): float(p_len[i]) for i in range(1, N + 1)},
        "power_return_probabilities": {str(i): float(a[i]) for i in range(1, N + 1)},
        "mobius_inversion_max_error": mobius_error,
        "projection_autocorrelation_max_error": autocorr_error,
        "form_factor_max_error": form_factor_error,
        "minimum_form_factor_value": min_form_factor,
        "fejer_cases_checked": fejer_cases,
        "fejer_max_positive_violation": max(0.0, fejer_max_violation),
        "pass": bool(
            mobius_error < 1e-12
            and autocorr_error < 1e-12
            and form_factor_error < 1e-12
            and min_form_factor > -1e-12
            and fejer_max_violation < 1e-12
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
