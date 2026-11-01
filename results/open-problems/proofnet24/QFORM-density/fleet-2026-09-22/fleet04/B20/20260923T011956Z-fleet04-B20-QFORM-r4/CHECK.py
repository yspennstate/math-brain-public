from fractions import Fraction
from math import e, sqrt

C = 103680 ** (1 / 3)
print("Cstar", C)
print("example_bound", C * (4 / (3 ** 0.5)) ** (2 / 3))
print("uniform_near_null", C * 2 ** (7 / 6))
base = 6 * 2 ** 0.25 * e ** 0.5 * (Fraction(1, 4)) ** (-0.5) * (Fraction(1, 256)) ** (-1 / 12)
print("outer_square_cap1", base)
print("outer_square_bank", base * 2 ** 0.5)

# Coordinates are in the orthonormal basis (e,f,g).
rows = [
    (sqrt(3) / 2, 0, 0),
    (1 / 2, 0, 0),
    (0, 1 / sqrt(2), 0),
    (0, 1 / sqrt(2), 0),
    (0, 0, 1 / sqrt(2)),
    (0, 0, 1 / sqrt(2)),
]
frame = [[sum(u[i] * u[j] for u in rows) for j in range(3)] for i in range(3)]
leverages = [sum(x*x for x in u) for u in rows]
print("frame_operator", frame)
print("leverages", leverages)
print("effective_eigenvalues", [-1, 1, 1])
for i in range(3):
    for j in range(3):
        assert abs(frame[i][j] - (1 if i == j else 0)) < 1e-12
assert max(leverages) < 1
