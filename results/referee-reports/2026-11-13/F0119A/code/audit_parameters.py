#!/usr/bin/env python3
"""Check the parameter translation and tabulate the cited exact thresholds.

The output is algebraic bookkeeping, not population-dynamics evidence.
"""
import csv
from decimal import Decimal, localcontext
from fractions import Fraction
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    checks = 0
    for epsilon in [Fraction(i, 200) for i in range(101)]:
        lam = 1 - 3 * epsilon
        diagonal = 1 - 2 * epsilon
        assert diagonal + 2 * epsilon == 1
        assert diagonal == (1 + 2 * lam) / 3
        assert epsilon == (1 - lam) / 3
        # Action on the independent mean-zero vectors (1,-1,0),(1,0,-1).
        for v in [(1, -1, 0), (1, 0, -1)]:
            out = [diagonal * v[i] + epsilon * sum(v[j] for j in range(3) if j != i)
                   for i in range(3)]
            assert out == [lam * x for x in v]
        for b in range(2, 7):
            # Independent polynomial expansion of b lambda^2 - 1.
            assert b * lam**2 - 1 == 9*b*epsilon**2 - 6*b*epsilon + b - 1
            # Mossel--Peres revealing-color ratio, in both conventions.
            assert b * lam**2 / (1-epsilon) == 3*b*lam**2 / (2+lam)
        checks += 1
    rows = []
    with localcontext() as c:
        c.prec = 60
        for b in range(2, 7):
            t = Decimal(1) / Decimal(b).sqrt()
            lo, hi = (1-t)/3, (1+t)/3
            assert abs(Decimal(b)*(1-3*lo)**2-1) < Decimal('1e-57')
            assert abs(Decimal(b)*(1-3*hi)**2-1) < Decimal('1e-57')
            rows.append(dict(b=b, lambda_abs_KS=str(t),
                             epsilon_ferro_boundary=str(lo),
                             epsilon_anti_algebraic_boundary=str(hi),
                             anti_reconstruction_nonempty=b>4,
                             classification_source='OpenAI 2026 Theorem 1.1, PDF p. 3'))
    dest = ROOT / 'data' / 'thresholds.csv'
    with dest.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    result = dict(rational_parameter_points_checked=checks,
                  b_values=[2,3,4,5,6], decimal_precision=60,
                  nice=os.getpriority(os.PRIO_PROCESS,0),
                  note='Thresholds copied from a cited theorem; not simulations or a new proof.')
    (ROOT / 'data' / 'parameter_audit.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
