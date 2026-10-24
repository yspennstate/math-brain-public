from fractions import Fraction

print("PROB10-09 lift-uniform central-extension exact checker")
print("All arithmetic is exact rational/integer arithmetic.")

# Full-Z fibre strict branching at the smallest possible free rank k=2.
b = 3
branch_num = b**3 - b**2 - b - 1
assert branch_num == 14 and branch_num > 0
print(f"k=2 full-Z branching numerator = {branch_num} > 0")
assert (3*b + 1)*(b - 1) > 0
print("b^3-b^2-b-1 is strictly increasing for b>=3 because f'(b)=(3b+1)(b-1)>0")

# Coarse all-r>=2 surface-amalgam inequality used in the written proof.
radical_margin = 289 - 288
assert radical_margin == 1
print("global radical check: 289-288 = 1 > 0, hence 9-6*sqrt(2)>1/2")
G = 4
coarse_floor = Fraction(1, 2)*G*G - 2*G + 1
assert coarse_floor == 1 and coarse_floor > 0
print(f"global coarse polynomial floor at minimal G=4 = {coarse_floor} > 0")

# Pell upper bound sqrt(2)<577/408.
s2 = Fraction(577, 408)
pell = s2*s2 - 2
assert pell == Fraction(1, 166464) and pell > 0
print(f"(577/408)^2-2 = {pell} > 0")

# Tight r=2, g1=g2=2 nonbacktracking root certificate.
zeta = Fraction(20000, 1683)
q = 17
zsq = zeta*zeta - q
assert zsq == Fraction(351847687, 2832489) and zsq > 0
print(f"zeta^2-17 = {zsq} > 0")
R_upper = 2 + 8*s2
assert R_upper == Fraction(679, 51)
print(f"2+8*(577/408) = {R_upper}")
root_margin = zeta + Fraction(q, 1)/zeta - R_upper
assert root_margin == Fraction(12313, 33660000) and root_margin > 0
print(f"zeta+17/zeta-R_upper = {root_margin} > 0")

p_u_floor = Fraction(1683, 20000)
p_c_ceiling = Fraction(1, 12)
gap = p_u_floor - p_c_ceiling
assert gap == Fraction(49, 60000) and gap > 0
print(f"new certified gap = 1683/20000 - 1/12 = {gap} = {float(gap):.16f}")
old = Fraction(1, 1500)
improvement = gap - old
assert improvement == Fraction(3, 20000) and improvement > 0
print(f"improvement over predecessor 1/1500 = {improvement} = {float(improvement):.16f}")
print(f"new p_u floor = {p_u_floor} = {float(p_u_floor):.8f}")
print("ALL_EXACT_CHECKS_PASS")
