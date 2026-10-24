#!/usr/bin/env python3
"""Finite exact-arithmetic-style diagnostic for the PROB20-20 smoothing lemma.

This is supplementary numerical evidence, not a proof.  For several fixed span-one
lattice laws it computes convolution powers exactly in the sense of ordinary
floating-point coefficient convolution and reports the two scale-normalized
quantities predicted by the proved Fourier bounds:

    sqrt(n) * max_s P(S_n=s),
    n * max_s |P(S_n=s+1)-P(S_n=s)|.

It also constructs a 75% LLN window, finds its largest atom, and verifies a
small deterministic plateau using the empirically certified gradient constant
across all powers n=10,...,NMAX.  The mathematical report proves the bounds
analytically from a fixed finite aperiodic smoothing component; this script is
only a reproducible sanity check on finite examples.
"""

from __future__ import annotations

from math import floor, sqrt

NMAX = 160
CHECK_NS = (20, 40, 80, 160)

LAWS = {
    "irregular_A": {0: 0.55, 1: 0.20, 4: 0.10, 13: 0.10, 37: 0.05},
    "irregular_B": {
        0: 0.68,
        1: 0.08,
        2: 0.04,
        7: 0.07,
        19: 0.06,
        53: 0.04,
        101: 0.03,
    },
}


def convolve(p: list[float], q: list[float]) -> list[float]:
    out = [0.0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a == 0.0:
            continue
        for j, b in enumerate(q):
            if b != 0.0:
                out[i + j] += a * b
    return out


def convolution_powers(base: list[float], nmax: int) -> dict[int, list[float]]:
    cur = [1.0]
    powers: dict[int, list[float]] = {}
    for n in range(1, nmax + 1):
        cur = convolve(cur, base)
        powers[n] = cur
    return powers


def max_gradient(p: list[float]) -> float:
    # Include the zero extension at the two edges.
    vals = [0.0] + p + [0.0]
    return max(abs(vals[i + 1] - vals[i]) for i in range(len(vals) - 1))


def llw_halfwidth(p: list[float], center: float, target_mass: float = 0.75) -> tuple[int, float]:
    w = 0
    while True:
        mass = sum(v for s, v in enumerate(p) if abs(s - center) <= w)
        if mass >= target_mass:
            return w, mass
        w += 1


def main() -> None:
    print("PROB20-20 convolution-smoothing finite diagnostic")
    print(f"NMAX={NMAX}; CHECK_NS={CHECK_NS}")
    print()

    for name, law in LAWS.items():
        total = sum(law.values())
        assert abs(total - 1.0) < 1e-12
        assert law.get(0, 0.0) > 0.0 and law.get(1, 0.0) > 0.0, "span-one check"

        max_k = max(law)
        base = [law.get(k, 0.0) for k in range(max_k + 1)]
        mean = sum(k * prob for k, prob in law.items())
        powers = convolution_powers(base, NMAX)

        # A finite-range certificate for the numerical first-difference constant.
        c_grad_emp = max(n * max_gradient(powers[n]) for n in range(10, NMAX + 1))

        print(f"LAW {name}: mean={mean:.12g}; empirical_Cgrad={c_grad_emp:.12g}")
        print(" n   sqrt(n)*maxatom      n*maxdiff       W75    mass75       H    minplateau/pstar")

        for n in CHECK_NS:
            p = powers[n]
            max_atom = max(p)
            grad = max_gradient(p)
            w75, mass75 = llw_halfwidth(p, n * mean)
            candidates = [s for s in range(len(p)) if abs(s - n * mean) <= w75]
            s_star = max(candidates, key=p.__getitem__)
            p_star = p[s_star]

            # Use the empirically certified Cgrad across n=10,...,NMAX.
            # A factor 1/4 matches the analytic plateau proof.
            h = max(0, floor(n * p_star / (4.0 * c_grad_emp)))
            lo = max(0, s_star - h)
            hi = min(len(p) - 1, s_star + h)
            min_plateau = min(p[lo : hi + 1])
            ratio = min_plateau / p_star
            assert ratio >= 0.75 - 1e-12

            print(
                f"{n:3d}  {sqrt(n)*max_atom:18.12g}  {n*grad:14.12g}"
                f"  {w75:6d}  {mass75:10.8f}  {h:6d}  {ratio:18.12g}"
            )

        print()

    print("PASS: all tested plateau ratios are >= 3/4.")
    print("NOTE: bounded scaled quantities are diagnostics only; the report contains the proof.")


if __name__ == "__main__":
    main()
