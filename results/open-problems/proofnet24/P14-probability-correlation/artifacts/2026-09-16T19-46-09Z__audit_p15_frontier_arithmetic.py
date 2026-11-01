#!/usr/bin/env python3
"""Independent arithmetic-only audit of P15's 2092 frontier checkpoint.

Scope: verify the 2-adic/odd-part decomposition for the multiples of four
2060..2092 quoted in P15's 2026-09-16_19-23-52 report, and verify the
d=6,d=9 row-sum profiles quoted there satisfy the necessary four-square
equation.  This deliberately does NOT independently certify the literature
status of H(2092).
"""

vals = [2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092]
expected = {
    2060: (2, 515),
    2064: (4, 129),
    2068: (2, 517),
    2072: (3, 259),
    2076: (2, 519),
    2080: (5, 65),
    2084: (2, 521),
    2088: (3, 261),
    2092: (2, 523),
}

for n in vals:
    k = 0
    m = n
    while m % 2 == 0:
        k += 1
        m //= 2
    assert (k, m) == expected[n]
    print(f"N={n} v2={k} oddpart={m}")

profiles = {
    6: [(5, 5, 19, 41), (7, 19, 29, 29)],
    9: [(1, 19, 19, 37), (17, 17, 17, 35)],
}
for d, rows in profiles.items():
    for p in rows:
        s = sum(x * x for x in p)
        assert s == 2092
        print(f"d={d} profile={p} sumsq={s}")

print("AUDIT_SCOPE=arithmetic only; does not independently certify literature status of H(2092)")
print("AUDIT_EXACT_PASS")
