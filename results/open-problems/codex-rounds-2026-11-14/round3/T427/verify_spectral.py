#!/usr/bin/env python3
"""Check the square spectral formula; requires mpmath and niceness >= 15.

Run from this directory:
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
    nice -n 15 python3 -B verify_spectral.py

No files are written. The calculation uses one Python thread, small finite
lists, and a 90-second CPU limit. Printed intervals omit floating-point
rounding; their analytic truncation bounds are proved in PROOF.md.
"""

import os
import sys


def main():
    if os.environ.get("OMP_NUM_THREADS") != "1":
        print("REFUSED: set OMP_NUM_THREADS=1.", file=sys.stderr)
        return 77
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 15:
        print(
            f"REFUSED: niceness is {priority}; at least 15 is required. "
            "No mathematical computation was run.",
            file=sys.stderr,
        )
        return 77

    import resource

    resource.setrlimit(resource.RLIMIT_CPU, (90, 95))
    try:
        import mpmath as mp
    except ImportError:
        print("REFUSED: mpmath is unavailable; no installation attempted.", file=sys.stderr)
        return 77

    mp.mp.dps = 85
    pi = mp.pi

    def truncation_bound(cutoff):
        r = cutoff + 1
        return (
            4 * mp.exp(-pi * r * r)
            / (pi**2 * r**2 * (1 - mp.exp(-pi))
               * (1 - mp.exp(-pi * (2 * cutoff + 3))))
        )

    def h_partial(cutoff):
        lattice = []
        for k in range(-cutoff, cutoff + 1):
            for ell in range(-cutoff, cutoff + 1):
                if k == 0 and ell == 0:
                    continue
                a = pi * (k * k + ell * ell)
                lattice.append(mp.e1(a) + mp.exp(-a) / a)
        axes = []
        for m in range(1, cutoff + 1):
            a = pi * m * m
            # 85 working digits control cancellation for these small cutoffs.
            aa = 2 * mp.exp(-a) - 2 * mp.sqrt(pi * a) * mp.erfc(mp.sqrt(a))
            axes.append(aa + mp.exp(-a) / a)
        return (1 - mp.log(pi) + mp.fsum(lattice) + 4 * mp.fsum(axes)) / (4 * pi)

    def direct_heat(cutoff, time):
        terms = []
        for k in range(cutoff + 1):
            for ell in range(cutoff + 1):
                if k == 0 and ell == 0:
                    continue
                eigenvalue = pi**2 * (k * k + ell * ell)
                terms.append(mp.exp(-time * eigenvalue) / eigenvalue)
        corrected = (
            mp.fsum(terms) - mp.log(1 / time) / (4 * pi)
            + mp.sqrt(time / pi) - 3 * time / 4
        )
        r = cutoff + 1
        alpha = pi**2 * time
        lattice_tail = (
            (2 / (pi**2 * r) + 1 / (pi**2 * r**2))
            * mp.exp(-alpha * r**2) / (1 - mp.exp(-alpha * (2 * r + 1)))
        )
        qtime = mp.exp(-1 / time)
        heat_correction = qtime * (
            time / (pi * (1 - qtime)**2)
            + time**mp.mpf("1.5") / (mp.sqrt(pi) * (1 - qtime))
        )
        return corrected, lattice_tail + heat_correction

    # Independent heat sum uses the quadrant spectrum directly, without E1.
    h3, h5 = h_partial(3), h_partial(5)
    b3, b5 = truncation_bound(3), truncation_bound(5)
    heat, heat_error = direct_heat(40, mp.mpf(1) / 100)
    rounding_allowance = mp.mpf("1e-75")
    assert h3 <= h5 + rounding_allowance
    assert h5 - h3 <= b3 + rounding_allowance
    assert abs(h5 - heat) <= b5 + heat_error + rounding_allowance
    assert b3 < mp.mpf("1e-21")
    print(f"niceness={priority}; working precision={mp.mp.dps} decimal digits")
    print("H_3 =", mp.nstr(h3, 60))
    print("H_3 analytic tail bound =", mp.nstr(b3, 12))
    print("H_5 =", mp.nstr(h5, 60))
    print("H_5 analytic tail bound =", mp.nstr(b5, 12))
    print("Corrected direct heat sum =", mp.nstr(heat, 60))
    print("Direct heat analytic error bound =", mp.nstr(heat_error, 12))
    print("PASS: positive-series formula and direct heat sum agree.")
    print("This is a numerical check, not interval-arithmetic certification.")
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak_rss if sys.platform == "darwin" else 1024 * peak_rss
    assert peak_bytes < 1024**3, "The 1 GB memory limit was exceeded."
    print(f"Peak resident memory: {peak_bytes} bytes (below 1 GB).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
