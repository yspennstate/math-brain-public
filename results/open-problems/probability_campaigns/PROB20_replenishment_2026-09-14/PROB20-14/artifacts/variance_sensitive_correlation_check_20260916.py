#!/usr/bin/env python3
"""Finite numerical consistency checks for the 2026-09-16 variance-sensitive
correlation-tax report.

This uses a genuine critical infinite-support law with finite q-moment and
infinite variance:

    q = 3/2,
    P(xi=2^j) = c / (j^2 2^(q j)), j>=1,

with masses at 0 and 1 chosen so E xi = 1 and total mass is one.

For each tested n, coefficients above n-1 cannot participate in the event
S_n=n-1, so exact central-conditioning probabilities are computable from the
finite relevant part of the infinite law. Floating arithmetic is used; this
is a reproducibility/algebra diagnostic, not proof evidence.
"""

import math
import numpy as np

Q = 1.5
C = 0.25
GAMMA = 0.20
SERIES_CUTOFF = 240

A = C * sum(2.0 ** ((1.0 - Q) * j) / (j * j) for j in range(1, SERIES_CUTOFF + 1))
B = C * sum(2.0 ** (-Q * j) / (j * j) for j in range(1, SERIES_CUTOFF + 1))
P1 = 1.0 - A
P0 = A - B

assert P0 > 0.0 and P1 > 0.0
assert abs(P0 + P1 + B - 1.0) < 1e-14


def prob_at(d: int) -> float:
    if d == 0:
        return P0
    if d == 1:
        return P1
    if d > 0 and (d & (d - 1)) == 0:
        j = int(round(math.log2(d)))
        if j >= 1:
            return C / (j * j * (2.0 ** (Q * j)))
    return 0.0


def offspring_pmf(max_d: int) -> np.ndarray:
    p = np.zeros(max_d + 1, dtype=float)
    p[0] = P0
    if max_d >= 1:
        p[1] = P1
    j = 1
    while 2**j <= max_d:
        p[2**j] = prob_at(2**j)
        j += 1
    return p


def truncated_power(base: np.ndarray, exponent: int, max_degree: int) -> np.ndarray:
    """Polynomial base**exponent, retaining only coefficients <= max_degree."""
    result = np.array([1.0])
    cur = base.copy()
    e = exponent
    while e:
        if e & 1:
            result = np.convolve(result, cur)[: max_degree + 1]
        e >>= 1
        if e:
            cur = np.convolve(cur, cur)[: max_degree + 1]
    if len(result) < max_degree + 1:
        result = np.pad(result, (0, max_degree + 1 - len(result)))
    return result


def full_power_pmf(base: np.ndarray, exponent: int) -> np.ndarray:
    """Full convolution via zero-padded FFT."""
    max_d = len(base) - 1
    need = exponent * max_d + 1
    fft_len = 1
    while fft_len < need:
        fft_len *= 2
    padded = np.pad(base, (0, fft_len - len(base)))
    spectrum = np.fft.rfft(padded)
    out = np.fft.irfft(spectrum**exponent, n=fft_len)[:need]
    return np.maximum(out, 0.0)


def truncated_second_moment_pi(R: float) -> float:
    total = 0.0
    for d in range(int(math.floor(R)) + 1):
        total += d * d * prob_at(d)
    return total


def check_n(n: int) -> None:
    base = offspring_pmf(n - 1)
    pn = truncated_power(base, n, n - 1)
    pnm1 = truncated_power(base, n - 1, n - 1)
    a_n = float(pn[n - 1])
    assert a_n > 0.0

    mu = np.zeros(n, dtype=float)
    for d, p in enumerate(base):
        if p > 0.0:
            mu[d] = p * pnm1[n - 1 - d] / a_n

    assert abs(float(mu.sum()) - 1.0) < 2e-10
    mean_mu = float(mu @ np.arange(n, dtype=float))
    assert abs(mean_mu - (1.0 - 1.0 / n)) < 2e-9

    kl = 0.0
    for d, mass in enumerate(mu):
        if mass > 0.0:
            kl += mass * math.log(mass / base[d])

    x_n = n * kl
    lam = -math.log(a_n)
    total_correlation = lam - x_n
    assert total_correlation >= -1e-10

    R_n = (n / (x_n + 1.0)) ** GAMMA
    V = truncated_second_moment_pi(R_n)

    mu_sum_pmf = full_power_pmf(mu, n)
    max_atom = float(mu_sum_pmf.max())
    target_atom = float(mu_sum_pmf[n - 1])

    # Data processing: TC >= -log P_{mu^n}(sum=n-1).
    assert total_correlation + 1e-8 >= -math.log(target_atom)

    # Pinsker/truncation comparison used in the proof.
    tv_upper = math.sqrt(max(kl, 0.0) / 2.0)
    V_mu = sum(d * d * mu[d] for d in range(min(n, int(math.floor(R_n)) + 1)))
    assert V_mu + R_n * R_n * tv_upper + 1e-9 >= V

    scaled_max = max_atom * math.sqrt(n * V) if V > 0.0 else float("nan")
    tax_without_constant = 0.5 * math.log(n) + 0.5 * math.log(V) if V > 0 else float("-inf")

    print(
        f"n={n:4d}  lambda={lam:.9f}  x=nKL={x_n:.9f}  "
        f"TC={total_correlation:.9f}  R={R_n:.6f}  V(R)={V:.9f}"
    )
    print(
        f"          target_atom={target_atom:.9g}  max_atom={max_atom:.9g}  "
        f"max*sqrt(nV)={scaled_max:.6f}  0.5log(nV)={tax_without_constant:.6f}"
    )


if __name__ == "__main__":
    print("critical infinite-support test law")
    print(f"q={Q}, c={C}, P0={P0:.12f}, P1={P1:.12f}, tail_prob={B:.12f}, tail_mean={A:.12f}")
    print("q-moment tail is finite because sum_j j^-2 < infinity; second moment diverges because sum_j 2^((2-q)j)/j^2 diverges.")
    for n_value in (32, 64, 128, 256):
        check_n(n_value)
    print("ALL ASSERTIONS PASSED")
