#!/usr/bin/env python3
"""Diagnostic for the one-point-defect obstruction to fixed global packet escorts.

This is a numerical companion only.  The all-n asymptotic theorem is proved
analytically in REPORT.md.  Standard library only.
"""
from decimal import Decimal, getcontext
import json

getcontext().prec = 180
LN2 = Decimal(2).ln()

def powd(x: Decimal, y: Decimal) -> Decimal:
    if y == 0:
        return Decimal(1)
    return (y * x.ln()).exp()

def row(n: int, theta: Decimal):
    j = Decimal(2) ** Decimal(1 - n)
    influence = Decimal(n) * j
    beta0 = (Decimal(1) - j) ** n
    beta1 = Decimal(1) - beta0
    N1 = Decimal(2) ** n - 1
    Z = powd(beta0, Decimal(1) - theta) + powd(N1, theta) * powd(beta1, Decimal(1) - theta)
    log2Z = Z.ln() / LN2
    return {
        "n": n,
        "theta": str(theta),
        "influence": str(influence),
        "beta1": str(beta1),
        "Z_theta": str(Z),
        "log2_Z_theta": str(log2Z),
        "log2_Z_over_I": str(log2Z / influence),
    }

fixed = [Decimal(1)/4, Decimal(1)/2, Decimal(3)/4, Decimal(1)]
ns = [8, 16, 32, 64, 128]
rows = []
for n in ns:
    for theta in fixed:
        rows.append(row(n, theta))
    rows.append(row(n, Decimal(1)/Decimal(n)))

# Sanity checks visible in exact/high precision arithmetic.
for theta in fixed:
    seq = [Decimal(r["log2_Z_over_I"]) for r in rows if r["theta"] == str(theta)]
    assert all(seq[i+1] > seq[i] for i in range(len(seq)-1))
# At the critical theta=1/n scale, the ratio should approach (4-1)/ln 2.
critical = [r for r in rows if Decimal(r["theta"]) == Decimal(1)/Decimal(r["n"])]
limit_c1 = (Decimal(4) - 1) / LN2
assert Decimal(critical[-1]["log2_Z_over_I"]) < limit_c1
assert Decimal(critical[-1]["log2_Z_over_I"]) > Decimal(4)

out = {
    "status": "PASS",
    "scope": "closed-form one-point-defect packet data; high-precision diagnostic, not theorem certificate",
    "fixed_theta_values": ["1/4", "1/2", "3/4", "1"],
    "n_values": ns,
    "critical_scaling_limit_c_equals_1": str(limit_c1),
    "rows": rows,
}
print(json.dumps(out, indent=2, sort_keys=True))
