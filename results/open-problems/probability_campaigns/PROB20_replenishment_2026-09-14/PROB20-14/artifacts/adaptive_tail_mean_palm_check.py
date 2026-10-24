#!/usr/bin/env python3
"""
Consistency checker for PROB20-14 adaptive tail-mean Palm truncation.

This is NOT proof of the infinite-variance theorem. It checks, on finite
critical lattice laws and with exact rational convolution probabilities, the
algebra behind Lemma 3.1 / Theorem 4.1 in the 2026-09-15T21:03:00Z report:

  * E[(xi-1)_+] = P(xi=0) under criticality;
  * the least-support adaptive threshold T satisfying
        N M_Y(T) <= eta*d/2
    has nonincreasing V_Y(T) as d grows;
  * the exact lower-deviation probability is below the elementary truncated
    negative-mgf Chernoff bound
        exp(-eta^2*d^2/(8*N*V_Y(T))).

Only Python's standard library is used.
"""

from fractions import Fraction
from collections import defaultdict
import math


def y_law(pi):
    out = defaultdict(Fraction)
    for x, p in pi.items():
        out[max(x - 1, 0)] += p
    return dict(out)


def check_critical(pi):
    assert sum(pi.values(), Fraction(0)) == 1
    assert sum(Fraction(x) * p for x, p in pi.items()) == 1
    py = y_law(pi)
    mu = sum(Fraction(y) * p for y, p in py.items())
    assert mu == pi[0]
    return py, mu


def convolve(base, n):
    dist = {0: Fraction(1)}
    for _ in range(n):
        nxt = defaultdict(Fraction)
        for s, p in dist.items():
            for y, q in base.items():
                nxt[s + y] += p * q
        dist = dict(nxt)
    return dist


def tail_mean(py, T):
    return sum(Fraction(y) * p for y, p in py.items() if y > T)


def truncated_second(py, T):
    return sum(Fraction(y * y) * p for y, p in py.items() if y <= T)


def adaptive_threshold(py, N, d, eta):
    support = sorted(py)
    for T in support:
        if N * tail_mean(py, T) <= eta * d / 2:
            return T
    return support[-1]


def exact_bad_probability(dist, N, mu, d, eta):
    cutoff = Fraction(N) * mu - eta * d
    return sum(p for s, p in dist.items() if Fraction(s) < cutoff)


def run_case(name, pi, N, ds, eta=Fraction(1, 2)):
    py, mu = check_critical(pi)
    dist = convolve(py, N)
    rows = []
    previous_v = None
    for d in ds:
        T = adaptive_threshold(py, N, d, eta)
        M = tail_mean(py, T)
        V = truncated_second(py, T)
        assert N * M <= eta * d / 2
        bad = exact_bad_probability(dist, N, mu, d, eta)
        if V == 0:
            bound = 0.0
            assert bad == 0
        else:
            bound = math.exp(
                -(float(eta) ** 2) * (d ** 2) / (8.0 * N * float(V))
            )
            assert float(bad) <= bound + 1e-15
        if previous_v is not None:
            # As d increases the admissible threshold set expands, so the
            # optimized truncated second moment cannot increase.
            assert V <= previous_v
        previous_v = V
        rows.append((d, T, float(M), float(V), float(bad), bound))
    print(name)
    print("Y law:", {k: str(v) for k, v in sorted(py.items())})
    print("E Y =", mu, "= pi_0")
    for row in rows:
        print(
            "d=%d T=%d M=%.9g V=%.9g exact_bad=%.9g chernoff=%.9g"
            % row
        )
    print()


if __name__ == "__main__":
    # Earlier campaign test law.
    pi_a = {
        0: Fraction(11, 20),
        1: Fraction(1, 5),
        2: Fraction(3, 20),
        5: Fraction(1, 10),
    }
    run_case("case A", pi_a, N=30, ds=[5, 8, 10, 12, 15, 20])

    # A rare high atom. The adaptive criterion is able to truncate before
    # Y=19 once d is large enough; this illustrates why tail mean rather than
    # the entire q-tail is the right centering quantity.
    pi_b = {
        0: Fraction(219, 1000),
        1: Fraction(580, 1000),
        2: Fraction(200, 1000),
        20: Fraction(1, 1000),
    }
    run_case("case B", pi_b, N=100, ds=[8, 10, 15, 20, 30, 40])
