from math import sqrt, e, pi

# fleet02/B08 r32 deterministic algebra/constant regression checks.
# These checks support, but do not replace, the analytic proofs in REPORT.md.

a0 = 4031 / 8192
s20 = 1 / 8
C_sing = 2 ** (11 / 4) / sqrt(a0 * s20)
assert abs(C_sing - 27.124769373386016) < 1e-12

# Newest fleet03/B08 r48 tangent-shear currency needed to match the
# inherited 619/L benchmark. r49 supersedes the deletion-loss branch but
# retains r48 as its immediate predecessor.
c48 = 8.653498
xi_619 = (c48 / 619) ** 3
assert 2.732e-6 < xi_619 < 2.733e-6

# Remaining nonzero Schur-hub quadratic coefficient after the inherited
# physical-pair gate and large-pivot selection.
delta_hub_max = 8190 / (4031 * 64)
assert abs(delta_hub_max - 0.031746154800297695) < 1e-15

# fleet03/B08 r49 diffuse-deletion spill specialization.
spill = 185 / 192
C_R = 288 * sqrt(3 * e) / 13
spill_payment = C_R / spill
assert abs(spill_payment - 65.65782681369896) < 1e-12

# Target-valid punctured-singular stress family at L=1.
delta = 1 / 128
m = 16384
n = 128
assert delta < 1 / 64
assert m > 64 / delta
assert n > 64

# Exact three nonzero eigenvalues, because the three rank-one vectors have
# disjoint supports.
eigs = (1.0, delta + 1 / delta, 1.0)
assert min(eigs) >= 1

# Every non-singular physical pair has its smaller diagonal entry below 1/64;
# pairs within either rank-one support are singular.
pair_scales = (delta, 1 / (delta * m), 1 / n)
assert max(pair_scales) < 1 / 64
assert all(abs(x - 1 / 128) < 1e-15 for x in pair_scales)

# Uniform full-density certificate from the independent Z^2 and U^2 blocks.
full_density_bound = pi * sqrt(2)
assert full_density_bound < 4.443

print(f"C_sing={C_sing:.15f}")
print(f"xi_619={xi_619:.15e}")
print(f"delta_hub_max={delta_hub_max:.15f}")
print(f"r49_spill={spill:.15f}")
print(f"r49_spill_payment={spill_payment:.15f}")
print(f"stress_eigs={eigs}")
print(f"stress_pair_scales={pair_scales}")
print(f"stress_full_density_bound={full_density_bound:.15f}")
print("QFORM_B08_R32_CHECK_PASS")
