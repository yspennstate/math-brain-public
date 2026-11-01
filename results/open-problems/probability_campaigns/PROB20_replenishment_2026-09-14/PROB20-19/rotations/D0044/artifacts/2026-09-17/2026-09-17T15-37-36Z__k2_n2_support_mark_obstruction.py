from fractions import Fraction


def gamma0_two_atom(p, z1, z2):
    """First modified Verblunsky coefficient for p*delta_z1+(1-p)*delta_z2
    in the real witness z1=1,z2=-1, using gamma_0 = p z1 + (1-p) z2.
    """
    return p * z1 + (1 - p) * z2


z1 = Fraction(1)
z2 = Fraction(-1)
p1 = Fraction(1, 4)
p2 = Fraction(3, 4)
g1 = gamma0_two_atom(p1, z1, z2)
g2 = gamma0_two_atom(p2, z1, z2)

print(f"support={{1,-1}} p={p1} gamma0={g1}")
print(f"support={{1,-1}} p={p2} gamma0={g2}")

assert g1 == Fraction(-1, 2)
assert g2 == Fraction(1, 2)
assert g1 != g2
print("ALL_EXACT_CHECKS_PASS")
