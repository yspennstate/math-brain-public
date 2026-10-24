from fractions import Fraction
from itertools import product


def pmf(weights, p):
    q = 1 - p
    out = {}
    for bits in product((0, 1), repeat=len(weights)):
        s = sum(w * b for w, b in zip(weights, bits))
        k = sum(bits)
        out[s] = out.get(s, Fraction(0)) + p**k * q**(len(weights) - k)
    return out


p = Fraction(1, 4)

# The simplest positive-weight numerical support already leaves the ordinary
# one-dimensional log-concave class used by the Bernoulli-count transport.
q12 = pmf((1, 2), p)
lc_minor = q12[1] ** 2 - q12[0] * q12[2]

# On the Boolean-quotient graph the natural local objects are weighted
# four-corner/rhombus ratios.  Even at one fixed source-valid law their signs
# are mixed, so a uniform local log-concavity sign is not available.
q123 = pmf((1, 2, 3), p)
ratio_neg = q123[1] * q123[2] / (q123[0] * q123[3])
ratio_pos = q123[1] * q123[3] / (q123[0] * q123[4])

print("EXACT_WEIGHTED_TRANSPORT_OBSTRUCTION")
print(f"p={p}")
print(f"weights_1_2_pmf={[str(q12[k]) for k in sorted(q12)]}")
print(f"log_concavity_minor_f1^2-f0*f2={lc_minor}")
print(f"rhombus_ratio_weights_1_2_3_pair_1_2_base0={ratio_neg}")
print(f"rhombus_ratio_weights_1_2_3_pair_1_3_base0={ratio_pos}")

assert lc_minor < 0
assert ratio_neg < 1
assert ratio_pos > 1
print(
    "PASS: exact weighted pmf is not 1D log-concave, and weighted rhombus "
    "log-ratios have both signs."
)
