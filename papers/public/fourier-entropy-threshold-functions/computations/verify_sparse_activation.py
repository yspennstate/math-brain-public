#!/usr/bin/env python3
"""Exact Walsh coefficient checks for the balanced rare-activation identities.

Integer spectra and rational influences are compared exactly. Entropy
identities are separately checked in double precision and do not prove
the all-dimensional results in the manuscript. Uses the standard library.
"""
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def walsh(values):
    out = list(values)
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2 * step):
            for j in range(base, base + step):
                a, b = out[j], out[j + step]
                out[j], out[j + step] = a + b, a - b
        step *= 2
    return out


def entropy(spec):
    norm = len(spec) ** 2
    return math.fsum(-(v * v / norm) * math.log2(v * v / norm)
                     for v in spec if v)


def influence(spec):
    return Fraction(sum(s.bit_count() * v * v
                        for s, v in enumerate(spec)), len(spec) ** 2)


def main():
    cases = 0
    coefficient_checks = 0
    max_error = 0.0
    for n in range(1, 4):
        size = 1 << n
        for positives in itertools.combinations(range(size), size // 2):
            pos = set(positives)
            g = [1 if x in pos else -1 for x in range(size)]
            gs = walsh(g)
            assert gs[0] == 0
            for r in range(1, 5):
                controls = 1 << r
                # Lower bits are the data coordinates; control point is zero.
                f = [g[x] if z == 0 else 1
                     for z in range(controls) for x in range(size)]
                fs = walsh(f)
                full_size = size * controls
                for u in range(controls):
                    for t in range(size):
                        index = t + size * u
                        expected = gs[t] if t else (-size if u else full_size-size)
                        assert fs[index] == expected, (n, r, positives, t, u)
                        coefficient_checks += 1
                assert sum(x*x for x in fs) == full_size**2
                p = Fraction(1, controls)
                assert influence(fs) == p * (influence(gs) + r)
                assert Fraction(sum(x == -1 for x in f), full_size) == p / 2
                pf = float(p)
                expected_h = (pf * entropy(gs) + 2*r*pf*(2-pf)
                              -(1-pf)**2 * math.log2((1-pf)**2))
                error = abs(entropy(fs) - expected_h)
                max_error = max(max_error, error)
                assert error < 1e-12, (n, r, positives, error)
                cases += 1
    # Exact-rational certificates for the sparse bent-point-flip obstruction.
    bent_cases = []
    for k in range(4, 42, 2):
        r = 2 * k
        delta, p = Fraction(1, 2**k), Fraction(1, 2**r)
        root_delta = Fraction(1, 2**(k//2))
        i_g = p * (Fraction(k, 2) + r * (1-root_delta))
        i_h = p * (Fraction(k, 2) + 2*k*delta + r*(1-root_delta+2*delta))
        assert 0 < i_g <= 5*k*p and 0 < i_h <= 5*k*p
        lower = (1-delta)*(k-2)
        bent_cases.append({"k": k, "selector_influence": str(p*delta),
                           "child_influences": [str(i_g), str(i_h)],
                           "entropy_charge_ratio_lower_bound": str(lower)})
    result = {"status": "PASS", "balanced_activation_cases": cases,
              "exact_coefficient_checks": coefficient_checks,
              "maximum_entropy_identity_error": max_error,
              "bent_point_flip_rational_certificates": bent_cases,
              "scope": "Finite exact identities and stated rational formulas; not a proof of full FEI."}
    path = Path(__file__).with_name("verify_sparse_activation.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k:v for k,v in result.items() if k != "bent_point_flip_rational_certificates"}))


if __name__ == "__main__":
    main()
