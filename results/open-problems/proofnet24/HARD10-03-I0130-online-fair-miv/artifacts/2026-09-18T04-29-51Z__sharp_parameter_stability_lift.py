#!/usr/bin/env python3
from fractions import Fraction as F

# Exact arithmetic receipt for I0130's sharpened parameter-stability lift.
# The theorem proved in the accompanying report is continuous and on-page:
#   |G_h^delta(D)-G_h^delta'(D)| <= h |delta-delta'|.
# This script verifies only the rational arithmetic that converts the already
# certified Q=24, delta=1/10, h=145 Bellman margin into the new source bound.

delta0 = F(1, 10)
alpha0 = 1 - delta0
h = 145
root = F(319, 240)          # pinned exact artifact from prior run
start0 = 1 + 3*delta0       # 13/10
margin = root - start0
assert margin == F(7, 240)

# New stability loss is h*eps, and the starting target rises by 3*eps.
eps = margin / (h + 3)
assert eps == F(7, 35520)

delta1 = delta0 + eps
alpha1 = 1 - delta1
assert delta1 == F(3559, 35520)
assert alpha1 == F(31961, 35520)

# Exact boundary inequality at equality.
assert root - h*eps == 1 + 3*delta1

L = F(19, 30)
W = alpha1 - L
assert W == F(631, 2368)

prevU = F(63281, 70320)
improvement = prevU - alpha1
assert improvement == F(203, 2081472)
assert improvement > 0

# Compare with the previous 2h-stability lift to make sure this is strictly stronger.
old_eps = F(7, 70320)
assert eps > old_eps

print('I0130_SHARP_PARAMETER_STABILITY_LIFT_PASS')
print(f'baseline_delta={delta0}')
print(f'baseline_alpha={alpha0}')
print(f'horizon={h}')
print(f'pinned_root={root}')
print(f'baseline_start_target={start0}')
print(f'margin={margin}')
print(f'sharp_stability_coefficient={h}')
print(f'epsilon={eps}')
print(f'lifted_delta={delta1}')
print(f'source_valid_upper_bound={alpha1}')
print(f'current_lower_bound={L}')
print(f'metric_width={W}')
print(f'improvement_over_63281_70320={improvement}')
