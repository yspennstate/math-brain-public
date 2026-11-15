"""Small independent numerical check of PROOF.md (15) and (17).

Uses only scalar arithmetic and the standard library. This is a floating-point
diagnostic; the analytic proof is in PROOF.md.
"""

import csv
import math
import os
from pathlib import Path
import resource
import sys
import time


def main():
    if os.environ.get("OMP_NUM_THREADS") != "1":
        raise SystemExit("Run with OMP_NUM_THREADS=1")
    # The launcher may already be at nice 20. Never try to raise its priority.
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 15:
        raise SystemExit(f"Priority is {priority}; need nice >= 15")
    started = time.monotonic()
    n = 100_000
    images = 8
    a = 8 * math.pi**2
    fourier_tail_bound = 2 / (a * n)
    rows = []
    for t in (0.1, 0.01, 0.001, 0.0001, 0.00001):
        # Stochastic isometry in the real sine/cosine Fourier basis.
        fourier = t + 2 * math.fsum(
            -math.expm1(-a * k * k * t) / (a * k * k)
            for k in range(1, n + 1)
        )
        # Integrate each periodized Gaussian image analytically.
        base = math.sqrt(t / (2 * math.pi))
        terms = []
        for m in range(1, images + 1):
            q = m / math.sqrt(8 * t)
            terms.append(math.exp(-q * q) - math.sqrt(math.pi) * q * math.erfc(q))
        image_value = base * (1 + 2 * math.fsum(terms))
        image_tail_bound = 2 * t * math.erfc(images / math.sqrt(8 * t))
        gap = image_value - fourier
        passed = -5e-13 <= gap <= fourier_tail_bound + image_tail_bound + 5e-13
        if not passed:
            raise AssertionError((t, gap, fourier_tail_bound, image_tail_bound))
        rows.append({
            "t": t,
            "fourier_partial": fourier,
            "image_partial": image_value,
            "image_minus_fourier": gap,
            "fourier_tail_bound": fourier_tail_bound,
            "image_tail_bound": image_tail_bound,
            "image_over_sqrt_t": image_value / math.sqrt(t),
            "passed": passed,
        })
        if time.monotonic() - started > 30:
            raise SystemExit("Unexpectedly slow: stopped after 30 seconds")
    output = Path(__file__).resolve().parent / "heat_check.csv"
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print("N=100000; images=8; five Fourier/image comparisons passed")
    print(f"predicted small-time constant = {1 / math.sqrt(2 * math.pi):.12f}")
    for row in rows:
        print(f"t={row['t']:.5g}  variance/sqrt(t)={row['image_over_sqrt_t']:.12f}"
              f"  image-Fourier={row['image_minus_fourier']:.6e}")
    print(f"Fourier tail bound = {fourier_tail_bound:.6e}")
    print("data: heat_check.csv")
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == "darwin" else peak * 1024
    print(f"nice={priority}; peak RSS={peak_bytes / 1024**2:.2f} MiB")
    if peak_bytes >= 1024**3:
        raise AssertionError("Memory limit exceeded")


if __name__ == "__main__":
    main()
