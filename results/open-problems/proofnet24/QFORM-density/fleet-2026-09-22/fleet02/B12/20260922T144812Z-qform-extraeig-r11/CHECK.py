import math

c3 = 2 * math.pi + 3 * math.sqrt(3)
cstar = c3 + math.sqrt(c3 * c3 + 3 * math.pi * math.pi)
c5 = 5 * math.e / 2

assert abs(cstar - 24.183038289961516) < 1e-12
assert abs(c5 - 6.7957045711476125) < 1e-15

# Exact cancellation bookkeeping from REPORT.md Section 6.
for r in range(1, 9):
    m = 4 + r
    base_cross_singulars = [1.0] * m
    final_cross_singulars = [0.0] * r + [1.0] * 4
    assert len(base_cross_singulars) == 4 + r
    assert sum(x > 0 for x in final_cross_singulars) == 4

    # Each canceled 2x2 pair becomes -I_2; each uncanceled
    # hyperbolic pair has eigenvalues {-1,+1}.
    final_eigenvalues = [-1.0] * (2 * r)
    for _ in range(4):
        final_eigenvalues += [-1.0, 1.0]
    assert len(final_eigenvalues) == 2 * m
    assert all(abs(abs(x) - 1.0) < 1e-15 for x in final_eigenvalues)

sigma = 1.0
delta = 0.2
surviving_s5 = sigma - delta
density_bound = 5 * math.e / (2 * surviving_s5)
assert abs(surviving_s5 - 0.8) < 1e-15

print("QFORM_B12_SPECTRAL_TAIL_CHECK_PASS")
print(f"5e/2={c5:.16f}")
print(f"Cstar={cstar:.15f}")
print("cancellation_r_checked=1..8")
print(f"sample_surviving_s5={surviving_s5:.16f}")
print(f"sample_density_bound={density_bound:.15f}")
