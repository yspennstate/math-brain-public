from decimal import Decimal, getcontext
getcontext().prec = 80

R6_LO = Decimal("6.5218509495504481848401605388605")
C0 = Decimal("6.4548")
C_AND = Decimal("0.0043974201")
TEST_C = Decimal("0.2682037982")

margin = Decimal(4) * (R6_LO - C0)
expected = Decimal("0.2682037982017927393606421554420")

assert margin == expected
assert margin > TEST_C
assert C0 + TEST_C / Decimal(4) == Decimal("6.52185094955")
assert margin / C_AND > Decimal("60.99")

print("PASS")
print("R6_lower=" + str(R6_LO))
print("C0=" + str(C0))
print("margin_lower=" + str(margin))
print("test_c=" + str(TEST_C))
print("test_center=" + str(C0 + TEST_C / Decimal(4)))
print("margin_over_AND_floor=" + str(margin / C_AND))
print("full_FEI_status=OPEN")
