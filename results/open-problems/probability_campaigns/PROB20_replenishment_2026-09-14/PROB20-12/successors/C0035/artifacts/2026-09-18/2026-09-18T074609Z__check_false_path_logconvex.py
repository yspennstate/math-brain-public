from fractions import Fraction
from itertools import product

# Explicit binary 3-block factor h(y_i,y_{i+1},y_{i+2}).
H = {
    (0, 0, 0): 0,
    (0, 0, 1): 1,
    (0, 1, 0): 0,
    (0, 1, 1): 0,
    (1, 0, 0): 1,
    (1, 0, 1): 0,
    (1, 1, 0): 1,
    (1, 1, 1): 0,
}

def all_ones_run_probability(n):
    good = 0
    total = 2 ** (n + 2)
    for y in product((0, 1), repeat=n + 2):
        x = [H[tuple(y[i:i+3])] for i in range(n)]
        good += int(all(v == 1 for v in x))
    return Fraction(good, total), good, total

q2, c2, t2 = all_ones_run_probability(2)
q3, c3, t3 = all_ones_run_probability(3)
q4, c4, t4 = all_ones_run_probability(4)

assert q2 == Fraction(1, 8)
assert q3 == Fraction(1, 32)
assert q4 == 0
gap = q3*q3 - q2*q4
assert gap == Fraction(1, 1024) and gap > 0

print(f"q2 = {q2} ({c2}/{t2})")
print(f"q3 = {q3} ({c3}/{t3})")
print(f"q4 = {q4} ({c4}/{t4})")
print(f"q3^2 - q2*q4 = {gap} > 0")
print("PASS: the proposed log-convex inequality q3^2 <= q2*q4 is NOT a valid universal constraint for binary 3-block factors.")
