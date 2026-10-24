from fractions import Fraction
from itertools import product

# Graph: direct edge e1 from o to b in parallel with a two-edge path e2,e3.
# C = {o <-> b} = {e1 open} union {e2,e3 both open}.
# A = {e1 open}.  Both A and C are increasing.
# We verify exactly that P_p(A | C) is not monotone in p.

def conditional_probability(p: Fraction):
    pC = Fraction(0)
    pAC = Fraction(0)
    for e1, e2, e3 in product((0, 1), repeat=3):
        k = e1 + e2 + e3
        prob = p**k * (1 - p)**(3 - k)
        C = bool(e1 or (e2 and e3))
        A = bool(e1)
        if C:
            pC += prob
        if A and C:
            pAC += prob
    return pAC / pC, pC, pAC

rows = []
for p in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
    ratio, pC, pAC = conditional_probability(p)
    formula = Fraction(1, 1) / (1 + p - p*p)
    assert ratio == formula
    rows.append((p, pC, pAC, ratio))

assert rows[0][3] == Fraction(16, 19)
assert rows[1][3] == Fraction(4, 5)
assert rows[2][3] == Fraction(16, 19)
assert rows[0][3] > rows[1][3] < rows[2][3]

for p, pC, pAC, ratio in rows:
    print(f"p={p}: P(C)={pC}, P(A cap C)={pAC}, P(A|C)={ratio}")
print("closed form: P_p(A|C)=1/(1+p-p^2)")
print("EXACT_SPRINKLING_MONOTONICITY_COUNTEREXAMPLE_PASS")
