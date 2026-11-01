from fractions import Fraction

seed = Fraction(6521851214, 10**9)
d0 = Fraction(38023734, 10**9)

M2 = Fraction(62098577, 239075328)
r2 = 4 * M2

L4 = Fraction(211575825297187673, 1628974855061766144)
r4 = 8 * L4

eps = Fraction(453773, 20000000)
Lstar = Fraction(
    14089027843865471581106016370764179,
    13874074233328574665473392640000000,
)
cstar = 1 - eps
rstar = Lstar / cstar

R6 = Fraction(
    117399595402058107229743783687,
    112981776538836095856994516992,
)
Rsingle = Fraction(279387, 261632)

assert r2 < r4 < rstar < R6 < Rsingle

def barrier(r):
    inc = d0 / r
    return inc, seed + inc

for name, r in [
    ("quadratic", r2),
    ("quartic", r4),
    ("three_ray_cone", rstar),
    ("degree6_necessary_cone", R6),
    ("singleton_safe_cone", Rsingle),
]:
    inc, total = barrier(r)
    print(name)
    print("eff=", r, float(r))
    print("inc=", inc, float(inc))
    print("center=", total, float(total))

candidate = Fraction(6558445288811087, 10**15)
gap = candidate - barrier(rstar)[1]
assert gap > 0
print("candidate_gap=", gap, float(gap))

epsmax = Fraction(10625, 468288)
A = r4
B = (A - Lstar) / eps
assert A - B > 0
r_family = (A - B * epsmax) / (1 - epsmax)
assert rstar < r_family
_, center_family = barrier(r_family)
print("shape_family_eff_ceiling=", r_family, float(r_family))
print("shape_family_center_barrier=", center_family, float(center_family))
print("PASS")
