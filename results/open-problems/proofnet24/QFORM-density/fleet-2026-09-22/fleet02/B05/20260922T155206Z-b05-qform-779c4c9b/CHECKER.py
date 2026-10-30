import math

E = math.e

# No-leakage aggregate constant: 3*2^(2/3)*e^(2/3)*c^(-1/3), c>1/2,
# and (B^2 |tau|)^(-1/3)<=1. Its supremum is 6 e^(2/3).
no_leak = 6 * E ** (2 / 3)
assert no_leak < 11.687
assert math.sqrt(2 * E) < E

# Elementary Hausdorff--Young factor used in the diffuse 2D projection proof.
for p in [2, 3, 4, 10, 100, 1000]:
    lhs = (p / (p - 1)) ** ((p - 1) / 2) / math.sqrt(p)
    rhs = math.sqrt(E / p)
    assert lhs <= rhs * (1 + 1e-14)

# For U,V iid Uniform[-1/2,1/2], W=2UV has
# p_W(w)=log(1/(2|w|)) on 0<|w|<1/2.
points = [0.25, 0.1, 1e-3, 1e-6]
densities = [math.log(1 / (2 * abs(w))) for w in points]
assert all(densities[k + 1] > densities[k] for k in range(len(densities) - 1))

print("NO_LEAK_CONSTANT", repr(no_leak))
for w, d in zip(points, densities):
    print("PRODUCT_DENSITY", repr(w), repr(d))
print("QFORM_B05_AGGREGATE_PAIR_CAP_PASS")
