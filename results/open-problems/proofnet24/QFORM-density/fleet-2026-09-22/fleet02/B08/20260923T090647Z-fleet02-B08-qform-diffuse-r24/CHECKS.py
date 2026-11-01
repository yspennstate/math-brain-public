from fractions import Fraction
import math

tau = Fraction(1, 4_000_000)
m = 2**24

# Tiny-N3 exclusion: every off-diagonal entry obeys |A_ij|^2 < tau+tau^2.
assert tau + tau*tau < Fraction(1, 600**2 * 3)

# Explicit Hadamard hybrid lies in N3(tau).
assert Fraction(3, m) < tau
assert Fraction(18, m*m) < tau

# Actual spectral-gate locations.
c2 = Fraction(3, 20)       # [(1/2)sqrt(3/5)]^2
beta2 = Fraction(27, 1280) # [(3/16)sqrt(3/5)]^2
assert Fraction(1, 5)**2 < c2 < Fraction(9, 10)**2
assert Fraction(1, 10)**2 < beta2 < Fraction(4, 5)**2

# Whole-range Theorem-F bounds for delta<=1/10.
def fbound(k):
    prod = (4/5)**k * (3/5)**(3-k)
    return 6 * prod**(-1/6)

x = float(tau + tau*tau)
entry_cap = math.sqrt(x)
r31_floor = 1/(600*math.sqrt(3))
tau_root = (-1 + math.sqrt(1 + 4/(600**2*3)))/2
G_floor = 1/(300*math.sqrt(3)*x)
vol_bound = (27*math.e/2)/G_floor
E2_floor = 3*G_floor**4/16
match_floor = 3*G_floor**4/256
bicore_floor = math.sqrt(2/27)*G_floor

print("QFORM_B08_R24_CHECK_PASS")
print(f"tau={float(tau):.12g}")
print(f"no_pivot_entry_cap={entry_cap:.15g}")
print(f"r31_scalar_floor={r31_floor:.15g}")
print(f"critical_tau_root={tau_root:.15g}")
print(f"m={m}")
print(f"3/m={3/m:.15g}")
print(f"18/m^2={18/m**2:.15g}")
print(f"actual_child_gate_c={0.5*math.sqrt(3/5):.15g}")
print(f"actual_cross_gate_beta={(3/16)*math.sqrt(3/5):.15g}")
print(f"r30_branchA_residual_floor={G_floor:.15g}")
print(f"r30_VOL_bound_after_tiny_gate={vol_bound:.15g}")
print(f"r30_E2_floor={E2_floor:.15g}")
print(f"r30_matching_floor={match_floor:.15g}")
print(f"r30_BICORE_star_floor={bicore_floor:.15g}")
print(f"hybrid_F_bound_k1={fbound(1):.15g}")
print(f"hybrid_F_bound_k2={fbound(2):.15g}")
