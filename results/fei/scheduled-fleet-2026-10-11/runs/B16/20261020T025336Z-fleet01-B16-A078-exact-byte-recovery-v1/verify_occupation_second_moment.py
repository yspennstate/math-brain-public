#!/usr/bin/env python3
"""Exact finite checks for B16/A078 occupation-time second-moment proof."""
from fractions import Fraction
from math import comb, log, log2, sqrt
from decimal import Decimal, getcontext
import json, sys

getcontext().prec = 60
failures = []

# Central-binomial inequalities for all even s in a finite range, checked exactly.
central_checked = 0
for s in range(2, 4098, 2):
    c = comb(s, s//2)
    if 4*s*c*c < 2**(2*s):
        failures.append(f"central lower bound fails at s={s}")
    if s*c*c > 2**(2*s):
        failures.append(f"central upper bound fails at s={s}")
    central_checked += 1

# Geometry and exact first/second moments for a finite set of n,l.
geometry_checked = 0
moment_checked = 0
min_hit_lower = None
max_ex2_over_n = Fraction(0,1)
for n in range(42, 257):
    for ell in range((n+2)//3, n//2 + 1):
        m = n-ell
        times = [s for s in range(m, n-1) if s % 2 == 0]
        M = len(times)
        if 7*M < n or 4*M > n:
            failures.append(f"M geometry fails at n={n}, ell={ell}, M={M}")
        geometry_checked += 1
        p = {s: Fraction(comb(s, s//2), 2**s) for s in times}
        EX = sum(p.values(), Fraction(0,1))
        pair = Fraction(0,1)
        for idx,s in enumerate(times):
            for t in times[idx+1:]:
                pair += p[s] * Fraction(comb(t-s, (t-s)//2), 2**(t-s))
        EX2 = EX + 2*pair
        if EX*EX < Fraction(n,196):
            failures.append(f"EX lower bound fails at n={n}, ell={ell}")
        if EX2 > n:
            failures.append(f"EX2 upper bound fails at n={n}, ell={ell}")
        if EX2/n > max_ex2_over_n:
            max_ex2_over_n = EX2/n
        if EX*EX/EX2 < Fraction(1,196):
            failures.append(f"Paley/Cauchy probability bound fails at n={n}, ell={ell}")
        moment_checked += 1

# Exact probability bookkeeping.
p_band_hit = Fraction(1,196) - Fraction(1,6144)
if p_band_hit <= Fraction(1,204):
    failures.append("P(A cap B) lower bound is not > 1/204")
if Fraction(1,4)*Fraction(1,204) != Fraction(1,816):
    failures.append("base-label event probability arithmetic failed")
C = 1_142_400
if Fraction(1,196)-Fraction(1,6144) != Fraction(1487,301056):
    failures.append("exact P(A cap B) fraction mismatch")
if Fraction(1487,301056) <= Fraction(1,204):
    failures.append("exact P(A cap B) does not exceed 1/204")

# Analytic constants, with numerical evaluation as a sanity check only.
Dnat = (Decimal(32)/Decimal(27)).ln()/Decimal(3)
Dbits = Decimal(5)/Decimal(3) - Decimal(3).ln()/Decimal(2).ln()
# Evaluate C50 = 1/(1-2^(-1/50)) in high-precision decimal arithmetic.
C50 = Decimal(1)/(Decimal(1)-(-Decimal(2).ln()/Decimal(50)).exp())
if not Dnat > Decimal(1)/Decimal(20): failures.append("natural KL divergence not > 1/20")
if not Dbits > Decimal(1)/Decimal(15): failures.append("bit KL divergence not > 1/15")
if not C50 < Decimal(128): failures.append("C50 not < 128")
if not (C50.ln()/Decimal(2).ln()) < Decimal(7): failures.append("log2 C50 not < 7")

# All-parameter exact rational witnesses.
def witness(a: Fraction, b: Fraction):
    n0 = 131072
    x = C*(a+b+2)
    N = max(n0, x.numerator//x.denominator + 1)
    residual = Fraction(1,1) + Fraction(N,C) - a - b
    return {"a": str(a), "b": str(b), "N": N, "physical_dimension": 2*N,
            "residual_exact_lower": str(residual), "residual_gt_3": residual > 3}

witnesses = [witness(Fraction(0),Fraction(0)),
             witness(Fraction(4),Fraction(3,4)),
             witness(Fraction(17,3),Fraction(9,10)),
             witness(Fraction(100),Fraction(0))]
for w in witnesses:
    if not w["residual_gt_3"]:
        failures.append(f"all-parameter witness failed: {w}")

result = {
  "schema": "b16-occupation-second-moment-check/1",
  "run_id": "20261020T014205Z-fleet01-B16-A078-occupation-second-moment-v1",
  "status": "PASS" if not failures else "FAIL",
  "command": "python3 -S verify_occupation_second_moment.py",
  "python": sys.version.split()[0],
  "random_seed": None,
  "central_binomial_exact_inequalities": {"even_s_range": [2,4096], "count": central_checked, "status": "PASS" if central_checked==2048 and not any("central " in x for x in failures) else "FAIL"},
  "finite_geometry_and_moment_checks": {"n_range": [42,256], "selected_pairs": geometry_checked, "exact_moment_pairs": moment_checked, "max_EX2_over_n_decimal": float(max_ex2_over_n), "status": "PASS" if not any("geometry" in x or "EX " in x or "EX2" in x or "probability bound" in x for x in failures) else "FAIL"},
  "probability_bookkeeping": {"P_AcapB_lower_exact": str(p_band_hit), "strictly_gt_1_over_204": p_band_hit>Fraction(1,204), "base_label_event_lower": "1/816", "status": "PASS" if not any("P(A cap B)" in x or "probability arithmetic" in x or "fraction mismatch" in x for x in failures) else "FAIL"},
  "analytic_constants_decimal_sanity": {"D_natural": str(Dnat), "D_bits": str(Dbits), "C50": str(C50), "log2_C50": str(C50.ln()/Decimal(2).ln()), "status": "PASS" if not any("KL divergence" in x or "C50" in x or "log2 C50" in x for x in failures) else "FAIL"},
  "all_parameter_witnesses": witnesses,
  "failures": failures,
  "interpretation": "PASS checks finite exact arithmetic and constants only. It does not prove the all-dimensional analytic estimates or replace A092/A088 end-to-end review."
}
print(json.dumps(result, indent=2))
if failures: sys.exit(1)
