"""Small exact-arithmetic audits of the constants in PROOF.md; no simulation."""

import itertools
import math
import os
import resource
from fractions import Fraction as F


def choose(n, k):
    return math.comb(n, k) if n >= k >= 0 else 0


def main():
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    print(f"priority={priority}; OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS')}")
    assert priority >= 15
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    # The sandbox rejects lowering AS/DATA limits. This finite streamed audit
    # stores tiny fractions and one tuple at a time; observe its RSS explicitly.
    try:
        resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
        print("CPU limit = 30 seconds")
    except (OSError, ValueError) as error:
        print(f"CPU limit unavailable: {error}")
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1024**3

    cases = 0
    subset_cases = 0
    largest_ratio = F(0)
    for n in range(2, 17):
        for d in range(2, min(n, 7) + 1):
            c = d * (d - 1)  # lambda=1, which cancels in the comparisons
            epsilon = F(d * d * (d - 1), 2 * n)
            assert epsilon / c == F(d, 2 * n)
            for equal in range(1, n + 1):
                for higher in range(n - equal + 1):
                    u = F(equal + higher, n)
                    v = F(higher, n)
                    b = sum(u ** (d - 1 - j) * v**j for j in range(d))
                    exact = F(n, equal) * F(
                        choose(equal + higher, d) - choose(higher, d),
                        choose(n, d),
                    )
                    assert 0 <= exact <= d and 0 <= b <= d
                    assert abs(exact - b) <= epsilon
                    largest_ratio = max(largest_ratio, abs(exact - b) / epsilon)
                    cases += 1
                    if n <= 7:
                        # Independent enumeration: label zero is the tag, of length 1.
                        lengths = [1] * equal + [2] * higher + [0] * (n - equal - higher)
                        weight = F(0)
                        for subset in itertools.combinations(range(n), d):
                            if 0 in subset and min(lengths[j] for j in subset) == 1:
                                weight += F(1, sum(lengths[j] == 1 for j in subset))
                        enumeration = F(n, choose(n, d)) * weight
                        assert exact == enumeration
                        subset_cases += 1
    print(f"routing rate bound: {cases} exact count cases passed (2<=N<=16, 2<=d<=7)")
    print(f"independent subset enumeration: {subset_cases} cases passed (N<=7)")
    print(f"largest observed error / stated bound = {largest_ratio}")

    walks = 0
    for n in range(1, 13):
        sum_max_squared = 0
        for signs in itertools.product((-1, 1), repeat=n):
            position = 0
            maximum = 0
            for step in signs:
                position += step
                maximum = max(maximum, abs(position))
            sum_max_squared += maximum**2
            walks += 1
        assert F(sum_max_squared, 2**n) <= 4 * n
    print(f"sign-walk maximal second-moment bound: {walks} walks passed (1<=N<=12)")

    # The prior periodic witness, independently computed from class counts.
    for d in range(2, 8):
        for m in range(d - 1, d + 5):
            n = 3 * m + 2
            equal = higher = m + 1
            numerator = choose(equal + higher, d) - choose(higher, d)
            old = F(n * numerator, equal * choose(n, d))
            new = F((n + 1) * numerator, equal * choose(n + 1, d))
            assert new == F(n + 1 - d, n) * old < old
    print("prior append-shorter witness: 36 exact cases passed")
    print(f"peak RSS = {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes (macOS)")
    print("All checks passed. Finite enumeration supplements the symbolic proof.")


if __name__ == "__main__":
    main()
