from fractions import Fraction
import json

# Exact multipliers for the genuine half-band charged mode (q,k)=(3,1).
epsilon = 2 * (Fraction(1, 2**3) / 3) * (Fraction(1, 2) - Fraction(1, 2**3) / 3)
e_full = 2 * (Fraction(1, 3) - Fraction(1, 9))
W = 1 - Fraction(1, 3)
a_star = Fraction(11, 192)

assert epsilon == Fraction(11, 288)
assert e_full == Fraction(4, 9)
assert W == Fraction(2, 3)
assert epsilon == a_star * W
assert epsilon / e_full == Fraction(11, 128)

# Source theorem: full-current live-window lower bound
#   7 / (3145728 n^3).
# Scale by epsilon/e_full for the central current, then use C=(11/192)W.
full_lb_coeff = Fraction(7, 3145728)
central_lb_coeff = full_lb_coeff * epsilon / e_full
ward_lb_coeff = central_lb_coeff / a_star
assert central_lb_coeff == Fraction(77, 402653184)
assert ward_lb_coeff == Fraction(7, 2097152)

# Since J=8n/2^D, a coefficient gap delta gives
# residual/J >= delta * [7*2^D/(2^24 n^4)].
ratio_delta_coeff = ward_lb_coeff / 8
assert ratio_delta_coeff == Fraction(7, 2**24)

# Leading asymptotic from I_R ~ 1/(12 n^3), four charged modes.
central_asymptotic_coeff = 4 * epsilon * Fraction(1, 12)
ward_asymptotic_coeff = 4 * W * Fraction(1, 12)
assert central_asymptotic_coeff == Fraction(11, 864)
assert ward_asymptotic_coeff == Fraction(2, 9)
assert central_asymptotic_coeff == a_star * ward_asymptotic_coeff

sample_a = Fraction(1, 20)
delta = a_star - sample_a
assert delta > 0
rows = []
for D in (128, 160, 192, 256):
    n = D - 1
    lower = delta * ratio_delta_coeff * Fraction(2**D, n**4)
    rows.append({"D": D, "n": n, "residual_over_J_lower_bound_for_a_1_over_20": float(lower)})

out = {
    "status": "PASS",
    "epsilon_q3k1": str(epsilon),
    "full_current_multiplier_q3k1": str(e_full),
    "ward_multiplier_q3": str(W),
    "sharp_ward_coefficient": str(a_star),
    "central_lower_bound_coefficient": str(central_lb_coeff),
    "ward_lower_bound_coefficient": str(ward_lb_coeff),
    "ratio_gap_coefficient": str(ratio_delta_coeff),
    "central_asymptotic_coefficient": str(central_asymptotic_coeff),
    "ward_asymptotic_coefficient": str(ward_asymptotic_coeff),
    "sample_rows": rows,
}
print(json.dumps(out, indent=2, sort_keys=True))
