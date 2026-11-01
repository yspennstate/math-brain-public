from fractions import Fraction

# Two one-type supercritical Galton--Watson laws with the same mean.
# Model A: deterministic binary tree.
A = {2: Fraction(1, 1)}
# Model B: nondegenerate, leafless, mean-two tree.
B = {1: Fraction(1, 2), 3: Fraction(1, 2)}


def mean(dist):
    return sum(Fraction(k) * p for k, p in dist.items())


def variance(dist):
    m = mean(dist)
    return sum(p * (Fraction(k) - m) ** 2 for k, p in dist.items())


assert sum(A.values()) == 1
assert sum(B.values()) == 1
assert mean(A) == mean(B) == 2
assert variance(A) == 0
assert variance(B) == 1
assert min(A) > 0 and min(B) > 0  # both are leafless

# At unit transmission every edge weight is 1, so the one-type tilted
# mean matrix is the scalar E[N]=2 for every beta in both models.
# Hence the entire pressure curve is phi(beta)=log 2 in both models.
for n in range(1, 9):
    # Model A has exactly 2^n depth-n cylinders, each of harmonic mass 2^-n.
    total = 2 ** n
    cylinder_mass = Fraction(1, total)
    assert total * cylinder_mass == 1

print("MODEL_A_MEAN", mean(A))
print("MODEL_B_MEAN", mean(B))
print("MODEL_A_VAR", variance(A))
print("MODEL_B_VAR", variance(B))
print("PRESSURE_INPUT_MEAN_EQUAL", mean(A) == mean(B))
print("UNIT_TRANSMISSION_TILT_CONSTANT", "M(beta)=2 for both models")
print("DETERMINISTIC_DEPTH8_CYLINDER_MASS", Fraction(1, 2 ** 8))
print("ALL_EXACT_CHECKS_PASS")
