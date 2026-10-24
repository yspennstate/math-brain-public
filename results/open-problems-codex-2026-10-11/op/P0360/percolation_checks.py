"""Small exact and numerical checks of the ordinary-percolation obstruction.

No simulation of a frozen solution is claimed. Working memory is negligible.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
import json
from pathlib import Path

rows = []
for t in [Fraction(0), Fraction(1, 100), Fraction(1, 4),
          Fraction(1, 2), Fraction(3, 4), Fraction(1)]:
    q = 1 - t
    f_q = (1 - t) / 2 + t * q / 2 + q * q / 2
    assert f_q == q
    assert (1 - t) / 2 + t / 2 + Fraction(1, 2) == 1
    with localcontext() as context:
        context.prec = 60
        dt = Decimal(t.numerator) / Decimal(t.denominator)
        qn = Decimal(0)
        for _ in range(2000):
            qn = (1 - dt) / 2 + dt * qn / 2 + qn * qn / 2
        rows.append({"time": str(t), "exact_extinction_probability": str(q),
                     "fixed_point_identity_checked_with_fractions": True,
                     "extinction_by_generation_2000": str(qn)})

frontier = []
for delta in [Fraction(1, 10), Fraction(1, 100)]:
    for size in [100, 1000]:
        bound = (1 - delta) ** size
        frontier.append({"delta": str(delta), "frontier_size": size,
                         "failure_bound_float": float(bound),
                         "bound_computed_as_exact_fraction": True})

result = {"offspring_checks": rows, "frontier_checks": frontier,
          "limitation": "These checks concern ordinary percolation only; "
                        "they do not test uniqueness of frozen solutions."}
Path(__file__).with_name('percolation_checks.json').write_text(
    json.dumps(result, indent=2), encoding='utf8')
print(json.dumps(result, indent=2))
