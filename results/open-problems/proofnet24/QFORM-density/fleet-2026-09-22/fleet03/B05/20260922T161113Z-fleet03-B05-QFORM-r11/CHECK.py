"""Regression-only arithmetic checks for fleet03/B05 run 20260922T161113Z.

The proof is in REPORT.md.  This script only checks constants and representative
regular-polygon Cauchy--Binet identities; it is not numerical evidence for QFORM.
"""
import math

C = 6.0 * math.e ** (2.0 / 3.0)
print("6 e^(2/3) =", C)
assert abs(C - 11.6864042463) < 1e-9

for m in [5, 7, 11, 29, 101]:
    y = [math.sqrt(2.0/m) * math.cos(2*math.pi*j/m) for j in range(m)]
    z = [math.sqrt(2.0/m) * math.sin(2*math.pi*j/m) for j in range(m)]
    yy = sum(v*v for v in y)
    zz = sum(v*v for v in z)
    yz = sum(a*b for a,b in zip(y,z))
    deltas = []
    for j in range(m):
        for k in range(j+1,m):
            deltas.append(y[j]*z[k]-y[k]*z[j])
    mass = sum(d*d for d in deltas)
    maxd = max(abs(d) for d in deltas)
    print(m, yy, zz, yz, mass, maxd, 2.0/m)
    assert abs(yy-1.0) < 1e-12
    assert abs(zz-1.0) < 1e-12
    assert abs(yz) < 1e-12
    assert abs(mass-1.0) < 1e-12
    assert maxd <= 2.0/m + 1e-12

print("PASS: representative arithmetic identities")
