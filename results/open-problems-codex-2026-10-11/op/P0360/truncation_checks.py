"""Exact rational checks of Proposition F's finite-cutoff law bound."""
from fractions import Fraction as Q
from pathlib import Path
import json

rows = []
for theta in [Q(1, 4), Q(1, 2), Q(3, 5), Q(3, 4), Q(9, 10)]:
    for n in [0, 1, 2, 5, 10, 25, 50]:
        cdf = {}
        previous = Q(0)
        for k in reversed(range(n+1)):
            t = theta**k
            previous = max(previous, t-previous)
            cdf[k] = previous
        delta = theta**(n+1)/(1+theta)
        assert all(abs(cdf[k]-theta**k/(1+theta)) <= delta
                   for k in range(n+1))
        total_abs = Q(0)
        vanished_atoms = 0
        for k in range(n+1):
            finite_mass = cdf[k]-(cdf[k+1] if k < n else Q(0))
            full_mass = (1-theta)*theta**k/(1+theta)
            assert finite_mass >= 0
            vanished_atoms += finite_mass == 0
            total_abs += abs(finite_mass-full_mass)
        # Omitted full-law tail and the atom at infinity.
        total_abs += delta
        total_abs += abs((1-cdf[0])-theta/(1+theta))
        tv = total_abs / 2
        assert tv <= (n+2)*delta
        rows.append({"theta": str(theta), "N": n,
                     "cdf_error_bound": str(delta),
                     "tv_exact": str(tv), "tv_upper_bound": str((n+2)*delta),
                     "tv_float": float(tv),
                     "vanished_finite_atoms": vanished_atoms})

output = {"number_of_exact_cases": len(rows), "cases": rows,
          "limitation": "Checks marginal finite-cutoff laws and their "
                        "TV bound. It does not test stability of arbitrary "
                        "full-time frozen solutions."}
Path(__file__).with_name('truncation_checks.json').write_text(
    json.dumps(output, indent=2), encoding='utf8')
print(json.dumps({"number_of_exact_cases":len(rows),
                  "largest_cutoff_cases":[r for r in rows if r['N']==50]},indent=2))
