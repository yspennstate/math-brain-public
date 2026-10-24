#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 90

def dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)

def A(p):
    m = 1 - 2*p
    return 1 - m**4

def B(p):
    v = 4*p*(1-p)
    return v**3

# Strong Numaro source, source-pinned in REPORT.md.
p1 = Fraction(223, 456)
pout = Fraction(1019, 2048)
alpha1 = Fraction(57, 256)
alpharest = Fraction(465, 256)

LA = alpha1*A(p1) + alpharest*A(Fraction(1,2)) - A(pout)
LB = alpha1*B(p1) + alpharest*B(Fraction(1,2)) - B(pout)

assert LA == Fraction(211575825297187673, 203621856882720768)
assert LB == Fraction(720628392668455225196366177, 693703711666428733273669632)
assert LA > LB > 0

# Latest exact genuine two-input AND-line obstruction E(r) from
# account01/B18 SHAPED-SAFE-FRONTIER-v1 at r=8004417/20000000.
N = 87063976298056383004191692840000000000000000000000000000
D = 3837334674058112811005758660502687481768624593225620567041
E = Fraction(N, D)
assert 0 < E < 1

# For repairs F=x A-y B, universal singleton-restriction safety forces
# T := N*x-D*y >= 0. The strong witness requires
# S := LA*x-LB*y > d0 because D_Gamma^dagger < -d0.
d0 = Fraction(38023734, 10**9)

# Exact nonnegative Farkas multipliers:
# (1,-1) = kappa*(LA,-LB) + beta*(N,-D).
den = D*LA - N*LB
kappa = Fraction(D-N, 1) / den
beta = (LA-LB) / den
assert den > 0 and kappa > 0 and beta > 0
assert kappa*LA + beta*N == 1
assert -kappa*LB - beta*D == -1

# Hence x-y = kappa*S + beta*T > kappa*d0.
Cdagger = Fraction(3260925607, 500000000)
center_floor = Cdagger + kappa*d0

# Prior source-reported family floor using the looser
# epsilon <= 10625/468288 obstruction.
prior_floor = Fraction(
    1081769658721394171434893539602395784124729,
    164943002829173802494551020191375500000000,
)

# Current source candidate SHAPED-SAFE-FRONTIER-v1.
current_candidate = Fraction(
    8198056603839780478193093835089,
    1250000000000000000000000000000,
)

assert center_floor > prior_floor
assert current_candidate > center_floor

epsilon_star = Fraction(56721646463783, 2500000000000000)
assert epsilon_star < E

eff_ceiling = (LA - E*LB) / (1-E)
assert eff_ceiling == 1/kappa

print("STATUS=PASS")
print("LA=", LA)
print("LB=", LB)
print("epsilon_two_input_ceiling=", E)
print("epsilon_two_input_ceiling_decimal=", dec(E))
print("efficiency_ceiling=", eff_ceiling)
print("efficiency_ceiling_decimal=", dec(eff_ceiling))
print("dual_kappa=", kappa)
print("dual_beta=", beta)
print("center_floor=", center_floor)
print("center_floor_decimal=", dec(center_floor))
print("prior_floor_decimal=", dec(prior_floor))
print("floor_improvement=", center_floor-prior_floor)
print("floor_improvement_decimal=", dec(center_floor-prior_floor))
print("current_candidate_decimal=", dec(current_candidate))
print("remaining_family_gap=", current_candidate-center_floor)
print("remaining_family_gap_decimal=", dec(current_candidate-center_floor))
