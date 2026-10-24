from fractions import Fraction

# Exact self-check of the scalar identities used in the proof report.
# This is falsification/self-check only; the report contains the all-dimensional proof.

bad = []
max_full = (Fraction(0), None)
max_central = (Fraction(0), None)
count = 0

for q in range(1, 402, 2):
    for k in range(1, q + 1, 2):
        if (q - k) % 2:
            continue

        x = Fraction(1, q)
        y = Fraction(1, k)
        lhs = 2*x*y - 2*x*x
        rhs = Fraction(1, 2)*y*y - 2*(x - Fraction(1, 2)*y)**2
        if lhs != rhs:
            bad.append(("full", q, k, lhs, rhs))
        ratio = lhs/(y*y)
        if ratio > max_full[0]:
            max_full = (ratio, (q, k))

        aq = Fraction(1, (2**q)*q)
        ak = Fraction(1, (2**k)*k)
        lhs_c = 2*aq*(ak-aq)
        rhs_c = Fraction(1, 2)*ak*ak - 2*(aq-Fraction(1, 2)*ak)**2
        if lhs_c != rhs_c:
            bad.append(("central", q, k, lhs_c, rhs_c))
        ratio_c = lhs_c/(ak*ak)
        if ratio_c > max_central[0]:
            max_central = (ratio_c, (q, k))

        if q >= k + 2:
            rem = Fraction(3, 8)*ak*ak - lhs_c
            fac = 2*(ak/Fraction(4)-aq)*(Fraction(3, 4)*ak-aq)
            if rem != fac or rem < 0:
                bad.append(("central_3_8", q, k, rem, fac))

        count += 1

# Clone-pair projector truth table.  P0=(1-e0)/2, P1=(1-e1)/2,
# Pg=(1-e0*e1)/2, P01=P0*P1.  Check Pg=P0+P1-2P01 and
# 16 P01 = 8(P0+P1-Pg), the normalized quadratic identity modewise.
projector_rows = []
for e0 in (-1, 1):
    for e1 in (-1, 1):
        P0 = Fraction(1-e0, 2)
        P1 = Fraction(1-e1, 2)
        Pg = Fraction(1-e0*e1, 2)
        P01 = P0*P1
        assert Pg == P0 + P1 - 2*P01
        assert 16*P01 == 8*(P0 + P1 - Pg)
        projector_rows.append((e0, e1, P0, P1, Pg, P01))

assert not bad
print("exact_pairs_checked", count)
print("max_full_ratio", max_full[0], "at", max_full[1], "float", float(max_full[0]))
print("max_central_ratio", max_central[0], "at", max_central[1], "float", float(max_central[0]))
print("projector_rows", projector_rows)
print("status PASS")
