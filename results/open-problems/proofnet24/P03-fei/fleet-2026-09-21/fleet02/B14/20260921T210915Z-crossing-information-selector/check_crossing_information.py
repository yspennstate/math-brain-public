#!/usr/bin/env python3
"""Diagnostic checks for B14 posterior-crossing information inequalities.

The analytic proof in REPORT.md is authoritative.  These finite checks use
floating Shannon entropy only as regression diagnostics; they are not an
all-dimensional certificate.
"""
import math


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def event_stats(bits, m):
    N = 1 << m
    p = sum(bits) / N
    infl = []
    for i in range(m):
        mask = 1 << i
        infl.append(sum(bits[x] != bits[x ^ mask] for x in range(N)) / N)
    return p, infl


def posterior(bits, m, A):
    N = 1 << m
    p = sum(bits) / N
    if not A:
        us = [p]
    else:
        groups = {}
        for x in range(N):
            key = tuple((x >> i) & 1 for i in A)
            s, n = groups.get(key, (0, 0))
            groups[key] = (s + bits[x], n + 1)
        us = [s / n for s, n in groups.values()]
    c = sum(max(2.0 * u - 1.0, 0.0) for u in us) / len(us)
    mi = h2(p) - sum(h2(u) for u in us) / len(us)
    return p, c, mi


def f_influences(vals, n):
    N = 1 << n
    return [sum(vals[x] != vals[x ^ (1 << i)] for x in range(N)) / N for i in range(n)]


def pivotal_event(vals, n, j):
    others = [i for i in range(n) if i != j]
    bits = []
    for y in range(1 << (n - 1)):
        x = 0
        for k, i in enumerate(others):
            if (y >> k) & 1:
                x |= 1 << i
        bits.append(int(vals[x] != vals[x ^ (1 << j)]))
    return bits, others


def main():
    event_block_cases = 0
    positive_crossing_cases = 0
    max_kl_lower_violation = 0.0
    max_mi_upper_violation = 0.0

    # Exhaust all events through m=4 and all coordinate blocks.
    for m in range(1, 5):
        N = 1 << m
        for maskfun in range(1 << N):
            bits = [(maskfun >> x) & 1 for x in range(N)]
            p, infl = event_stats(bits, m)
            if not (0.0 < p <= 0.5):
                continue
            for amask in range(1 << m):
                A = [i for i in range(m) if (amask >> i) & 1]
                _, c, mi = posterior(bits, m, A)
                if p < 0.5:
                    L = math.log2((1.0 - p) / p)
                    max_kl_lower_violation = max(max_kl_lower_violation, L * c - mi)
                    if c > 0.0:
                        positive_crossing_cases += 1
                max_mi_upper_violation = max(max_mi_upper_violation, mi - sum(infl[i] for i in A))
                event_block_cases += 1

    local_square_checks = 0
    combined_block_cases = 0
    max_square_violation = 0.0
    max_combined_violation = 0.0

    # Exhaust all Boolean functions through n=3 for the pivotality specialization.
    for n in range(1, 4):
        N = 1 << n
        for fmask in range(1 << N):
            vals = [1 if (fmask >> x) & 1 else -1 for x in range(N)]
            pinf = f_influences(vals, n)
            for j in range(n):
                bits, others = pivotal_event(vals, n, j)
                p, eta_infl = event_stats(bits, n - 1)
                assert abs(p - pinf[j]) < 1e-15
                for k, i in enumerate(others):
                    max_square_violation = max(max_square_violation, eta_infl[k] - 2.0 * pinf[i])
                    local_square_checks += 1
                if not (0.0 < p < 0.5):
                    continue
                L = math.log2((1.0 - p) / p)
                for amask in range(1 << (n - 1)):
                    Aidx = [k for k in range(n - 1) if (amask >> k) & 1]
                    _, c, _ = posterior(bits, n - 1, Aidx)
                    IA = sum(pinf[others[k]] for k in Aidx)
                    max_combined_violation = max(max_combined_violation, 0.5 * L * c - IA)
                    combined_block_cases += 1

    print("event_block_cases", event_block_cases)
    print("positive_crossing_cases", positive_crossing_cases)
    print("max_kl_lower_violation", max_kl_lower_violation)
    print("max_mi_upper_violation", max_mi_upper_violation)
    print("local_square_checks", local_square_checks)
    print("combined_block_cases", combined_block_cases)
    print("max_square_violation", max_square_violation)
    print("max_combined_violation", max_combined_violation)


if __name__ == "__main__":
    main()
