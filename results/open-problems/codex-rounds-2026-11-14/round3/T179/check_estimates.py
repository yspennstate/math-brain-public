"""Exact-arithmetic diagnostics for the estimates in PROOF.md.

These check exponents and deterministic identities, not SPDE uniqueness.
Only the Python standard library is used; storage is constant and small.
"""

from fractions import Fraction as Q
import math
import os
import resource
import sys
import time


def main():
    started = time.monotonic()
    if os.environ.get("OMP_NUM_THREADS") != "1":
        raise SystemExit("Set OMP_NUM_THREADS=1")
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 15:
        raise SystemExit(f"nice={priority}; expected at least 15")

    for beta in (Q(1, 100), Q(1, 2), Q(2, 3), Q(3, 4), Q(99, 100), Q(999, 1000)):
        eta = (1 - beta) / 8
        p = math.floor(12 / (1 - beta)) + 2
        p += p % 2
        inner = 2 * eta + (1 + beta) / 2
        outer_gap = eta - Q(3, 2 * p)
        conjugate = Q(p, p - 1)
        # Direct L^q integration of the outer time kernel, independently
        # compared with eta > 3/(2p).
        outer_integral_gap = conjugate * (eta - 1 - Q(1, 2 * p)) + 1
        assert inner == (3 + beta) / 4 < 1
        assert outer_integral_gap == conjugate * outer_gap > 0
        print(f"beta={beta}; eta={eta}; p={p}; inner={inner}; outer_gap={outer_gap}")

    pairs = (
        ([1, -1], [0, 0]),
        ([-2, 1, 0, 5], [3, -1, 0, -2]),
        ([Q(1, 3), Q(-7, 5)], [Q(1, 3), Q(2, 5)]),
    )
    for v, w in pairs:
        l1 = sum((abs(Q(a) - Q(b)) for a, b in zip(v, w)), Q(0)) / len(v)
        gap = sum((max(Q(a), Q(b)) - min(Q(a), Q(b))
                   for a, b in zip(v, w)), Q(0)) / len(v)
        assert gap == l1
    print("three crossing/signed envelope-mass identities: exact")

    for height in (2, 10, 1000):
        support = Q(1, height * height)
        assert height * height * support == 1
        assert height * support == Q(1, height)
    print("three unit-L2 spike identities with growing supremum: exact")

    # Squared initial error delta^(1/2), followed by Jensen with powers
    # 1/4 and 1/2, gives the two independently available closure rates.
    assert Q(1, 2) * Q(1, 4) == Q(1, 8)
    assert Q(1, 2) * Q(1, 2) == Q(1, 4)
    print("restart exponents: H modulus 1/8; L1 tests 1/4")

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == "darwin" else peak * 1024
    assert peak_bytes < 1024**3
    assert time.monotonic() - started < 30
    print(f"nice={priority}; peak RSS={peak_bytes / 1024**2:.2f} MiB")


if __name__ == "__main__":
    main()
