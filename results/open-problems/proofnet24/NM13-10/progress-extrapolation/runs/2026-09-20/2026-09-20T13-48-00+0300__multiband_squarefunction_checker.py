import math
import mpmath as mp

mp.mp.dps = 50

# Exact numerical value of the rearrangement-square-function integral.
C0 = mp.quad(lambda x: mp.e**(-x/3) * (1+x)**(mp.mpf(4)/3), [0, mp.inf])

# The analytic proof uses C0 < 33. Constants below use that rigorous envelope.
base_rig = 65 * math.sqrt(66)  # 65*sqrt(2)*sqrt(33)
two_rig = base_rig * 2**(1/6)

# Numerical best constant from the same square-function integral, sanity only.
base_num = 65 * mp.sqrt(2*C0)
two_num = base_num * 2**(mp.mpf(1)/6)

print(f"C0_numeric={mp.nstr(C0, 18)}")
print(f"C0_lt_33={bool(C0 < 33)}")
print(f"rigorous_base=65*sqrt(66)={base_rig:.12f}")
print(f"rigorous_base_lt_529={base_rig < 529}")
print(f"two_band_rigorous={two_rig:.12f}")
print(f"two_band_lt_594={two_rig < 594}")
print(f"numerical_base_same_argument={mp.nstr(base_num, 18)}")
print(f"numerical_two_band_same_argument={mp.nstr(two_num, 18)}")

# Compare the predecessor wide-band loss 65*sqrt(K) with the new N-block
# gluing loss 529*N^(1/6), for a spectral ratio K=2^N.
first = None
for N in range(1, 25):
    old = 65 * 2**(N/2)
    new = 529 * N**(1/6)
    if first is None and new < old:
        first = N
    if N in (1, 2, 4, 7, 8, 12, 16, 24):
        print(f"N={N:2d} old_65sqrtK={old:.9f} new_529N16={new:.9f} improved={new<old}")
print(f"first_integer_N_with_new_better={first}")

# Elementary gamma bound used in the written proof:
# Gamma(1/3) < 21/8 + exp(-1) < 3.
gamma_bound = 21/8 + math.exp(-1)
print(f"gamma_one_third_upper={gamma_bound:.12f}")
print(f"gamma_upper_lt_3={gamma_bound < 3}")

assert C0 < 33
assert base_rig < 529
assert two_rig < 594
assert gamma_bound < 3
assert first == 7
print("CHECK_PASS")
