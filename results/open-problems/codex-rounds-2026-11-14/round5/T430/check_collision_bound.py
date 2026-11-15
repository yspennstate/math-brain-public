"""Small exact-arithmetic audits; no simulation or external dependencies."""

import itertools
import math
import os
import resource
import time
from fractions import Fraction as F


def main():
    start = time.monotonic()
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    print(f"priority={priority}; OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS')}")
    assert priority >= 15
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    print("CPU limit = 30 seconds")

    # Independently enumerate original d-subset routing and per-tag proposals.
    configs = rates = 0
    for n in range(2, 6):
        for lengths in itertools.product(range(3), repeat=n):
            for d in range(2, min(n, 4) + 1):
                original = [F(0)] * n
                for sample in itertools.combinations(range(n), d):
                    minimum = min(lengths[i] for i in sample)
                    winners = [i for i in sample if lengths[i] == minimum]
                    for i in winners:
                        original[i] += F(n, math.comb(n, d) * len(winners))
                proposal = []
                for tag in range(n):
                    total = F(0)
                    others = [i for i in range(n) if i != tag]
                    for rivals in itertools.combinations(others, d - 1):
                        if all(lengths[j] >= lengths[tag] for j in rivals):
                            total += F(1, 1 + sum(lengths[j] == lengths[tag] for j in rivals))
                    proposal.append(F(d, math.comb(n - 1, d - 1)) * total)
                assert original == proposal
                assert sum(proposal) == n
                configs += 1
                rates += n
    print(f"exact proposal representation: {configs} configurations/choice counts, {rates} tagged rates passed")

    # Enumerate every iid label tuple. Compare exact no-collision counts with
    # falling factorials, and the collision probability with the pair bound.
    tuple_count = birthday_cases = 0
    for n in range(2, 7):
        for m in range(0, 8):
            distinct = 0
            total = n**m
            for labels in itertools.product(range(n), repeat=m):
                distinct += len(set(labels)) == m
                tuple_count += 1
            falling = math.prod(n - j for j in range(m)) if m <= n else 0
            assert distinct == falling
            collision = 1 - F(distinct, total)
            assert collision <= F(m * (m - 1), 2 * n)
            birthday_cases += 1
    print(f"birthday bound: {birthday_cases} cases, {tuple_count} explicit label tuples passed")

    # Recover moments from a second-order expansion of the branching PGF,
    # independently of solving the moment differential equations.
    moment_cases = 0
    derivative_cases = 0
    for a in range(1, 9):
        for k in range(1, 13):
            for p in (F(1), F(1, 2), F(2, 3), F(3, 4), F(1, 5)):
                q = 1 - p
                r = F(k, a)
                v = q * a / p
                w = q * a * (a - 1) / (2 * p)
                # z=1+h: z^k times (1-v*h-w*h^2+O(h^3))^(-r).
                linear = k + r * v
                quadratic = F(k * (k - 1), 2) + k * r * v + r * w + r * (r + 1) * v**2 / 2
                pgf_factorial_second = 2 * quadratic
                A = 1 / p
                ode_first = k * A
                ode_second = k**2 * A**2 + a * k * (A**2 - A)
                assert linear == ode_first
                assert pgf_factorial_second == ode_second - ode_first
                assert pgf_factorial_second == k * (k + a) * A**2 - k * (a + 1) * A
                moment_cases += 1
            # Divide the time derivative by C. A proposal changes choose(M,2)
            # by a*k+a*(a-1)/2 and has rate beta*k=C*k/a.
            generator_derivative = F(k, a) * (a * k + F(a * (a - 1), 2))
            formula_derivative = F(k * (2 * k + a - 1), 2)
            assert generator_derivative == formula_derivative
            derivative_cases += 1
    print(f"branching moments: {moment_cases} exact PGF expansions and {derivative_cases} initial generator derivatives passed")

    # The centered-product test in (12) has oscillation at most one,
    # so TV, with sup-event convention, introduces no factor two.
    for j in range(101):
        m = F(j, 100)
        oscillation = max(m**2, (1 - m)**2) + m * (1 - m)
        assert oscillation == max(m, 1 - m) <= 1
    print("centered-product oscillation: 101 exact cases passed")
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak < 1024**3
    print(f"peak RSS = {peak} bytes (macOS); elapsed = {time.monotonic() - start:.3f} seconds")
    print("All checks passed. Enumeration supplements the all-parameter proof.")


if __name__ == "__main__":
    main()
