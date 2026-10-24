#!/usr/bin/env python3
"""Exact finite self-check for R06 BENJ-2026-FS3.

The excess-coordinate change (da,db,dc) changes the three landmark-distance
coordinates by
    dr1 = -da + db + dc,
    dr2 =  da - db + dc,
    dr3 =  da + db - dc.
Among the 26 nonzero {-1,0,1}^3 moves, classify exactly those for which every
landmark distance changes by at most one.  No floating point arithmetic is used.
"""
from itertools import product

expected = {
    (-1, -1, -1),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
}

allowed = {}
for da, db, dc in product((-1, 0, 1), repeat=3):
    if (da, db, dc) == (0, 0, 0):
        continue
    dr = (-da + db + dc, da - db + dc, da + db - dc)
    if max(abs(t) for t in dr) <= 1:
        allowed[(da, db, dc)] = dr

assert set(allowed) == expected
assert len(allowed) == 8

# Check the exact inverse linear identities used on the report page.
# If r1=b+c-a+s1, r2=a+c-b+s2, r3=a+b-c+s3, then each expected
# move gives exactly the distance increment printed below.
for move in sorted(allowed):
    print(f"{move} -> {allowed[move]}")
print("allowed_count=8")
print("EXACT_STEP_CLASSIFICATION_PASS")
