#!/usr/bin/env python3
"""Checks for agent 043; numerical checks supplement the proofs, never replace them.

Run from the research-session root:
  python computations/043_constants.py

No random-frame simulation is attempted at the deliberately large sufficient N.
"""
from fractions import Fraction
import json
import math
from pathlib import Path
import random

def gaussian_quadratic_moments(eigenvalues, field):
    """Exact moments up to order four by independent-variable convolution."""
    alpha, scale = ((Fraction(1), 1) if field == "complex" else (Fraction(1, 2), 2))
    egf = [Fraction(1)] + [Fraction(0)] * 4
    for lam in eigenvalues:
        factors = [Fraction(1)]
        rising = Fraction(1)
        for k in range(1, 5):
            rising *= alpha + k - 1
            factors.append(rising * (scale * lam) ** k / math.factorial(k))
        egf = [sum(egf[j] * factors[k-j] for j in range(k+1)) for k in range(5)]
    return [egf[k] * math.factorial(k) for k in range(5)]


def main():
    rng = random.Random(43)
    checked = 0
    for field, nu, b in [("complex", 1, 11), ("real", 2, 17)]:
        for d in range(1, 9):
            for _ in range(100):
                lam = [rng.randint(-6, 6) for _ in range(d)]
                t, s2, s3, s4 = (sum(x ** k for x in lam) for k in range(1, 5))
                moments = gaussian_quadratic_moments(lam, field)
                m2 = t*t + nu*s2
                if field == "complex":
                    m4 = t**4 + 6*t*t*s2 + 8*t*s3 + 3*s2*s2 + 6*s4
                else:
                    m4 = t**4 + 12*t*t*s2 + 32*t*s3 + 12*s2*s2 + 48*s4
                assert moments[2] == m2
                assert moments[4] == m4
                assert m4 <= b*m2*m2
                checked += 1

    beta_checks = []
    for a in [0.5, 1, 1.5, 2, 4, 8, 16, 32]:
        # x=(1+sin(theta))/2 removes the endpoint singularity at a=1/2.
        panels = 20000
        step = (math.pi/2)/panels
        values = [math.sin(k*step)*math.cos(k*step)**int(2*a-1) for k in range(panels+1)]
        simpson = step/3 * (values[0]+values[-1]+4*math.fsum(values[1:-1:2])+2*math.fsum(values[2:-1:2]))
        integral = math.exp((1-a)*math.log(4)-2*math.lgamma(a)+math.lgamma(2*a))*simpson
        gamma_value = math.exp(math.lgamma(a+0.5)-0.5*math.log(math.pi)-math.lgamma(a+1))
        err = abs(integral-gamma_value)
        assert err < 1e-10
        beta_checks.append({"a": a, "absolute_error": err})

    table = []
    for d in [2, 3, 4, 5, 8, 16, 32, 64]:
        m = d//2
        complex_exact = Fraction(4**m, math.comb(2*m, m))
        real_lower = math.exp(0.5*math.log(math.pi)+math.lgamma(m/2+1)-math.lgamma((m+1)/2))
        table.append({
            "d": d,
            "complex_lower_exact": str(complex_exact),
            "complex_lower": float(complex_exact),
            "real_lower": real_lower,
            "complex_constructive_upper": 2*math.sqrt(11*d),
            "real_constructive_upper": math.sqrt(34*d),
        })

    output = {
        "seed": 43,
        "exact_gaussian_moment_and_bound_cases": checked,
        "beta_integral_checks": beta_checks,
        "constant_table": table,
        "limitations": [
            "Moment formulas and inequalities are proved in agents/043.md; finite checks are supplementary.",
            "No construction at the large explicit sufficient frame size was simulated.",
            "Balanced-reflection bounds are not asserted to give the exact optimal lift coefficient.",
        ],
    }
    target = Path(__file__).with_name("043_constants_output.json")
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"output": str(target), "exact_cases": checked, "beta_cases": len(beta_checks), "table": table}, indent=2))


if __name__ == "__main__":
    main()
