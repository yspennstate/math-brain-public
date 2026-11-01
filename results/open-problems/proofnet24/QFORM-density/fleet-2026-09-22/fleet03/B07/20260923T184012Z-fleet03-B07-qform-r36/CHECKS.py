import math
import random


def e2(xs):
    s = sum(xs)
    return (s*s - sum(x*x for x in xs))/2.0


# Regression only: verify the E2 heavy-marginal algebra on random positive spectra.
random.seed(3607)
cases = 0
rank2_cases = 0
min_margin = float("inf")
for n in range(2, 20):
    for _ in range(1000):
        xs = [10.0**random.uniform(-8.0, 8.0) for __ in range(n)]
        Z = e2(xs)
        if Z <= 0.0:
            continue
        S = sum(xs)
        alpha = [x*(S-x)/Z for x in xs]
        heavy = [i for i, a in enumerate(alpha) if a > 2.0/3.0]
        assert len(heavy) <= 2
        if len(heavy) == 2:
            p, q = heavy
            ratio = xs[p]*xs[q]/(Z/3.0)
            min_margin = min(min_margin, ratio)
            assert ratio > 1.0 - 1e-12
            rank2_cases += 1
        cases += 1

Zc = 854675.100194511
h = (2.0*math.sqrt(2.0)-1.0)/1572864.0
product_constant = math.sqrt(Zc/3.0)
flat_side_density_bound = 2.0*math.sqrt(math.pi/(product_constant*h*h))
nonzero_entry_lower_bound = math.floor(128.0*product_constant)+1

assert nonzero_entry_lower_bound == 68321

print(f"cases={cases}")
print(f"rank2_cases={rank2_cases}")
print(f"min_ratio_xpxq_over_Zthird={min_margin:.12f}")
print(f"h={h:.16e}")
print(f"sqrt_Zc_over_3={product_constant:.15f}")
print(f"flat_side_density_bound={flat_side_density_bound:.12f}")
print(f"partner_cap_nonzero_entry_lower_bound={nonzero_entry_lower_bound}")
print("STATUS=PASS")
