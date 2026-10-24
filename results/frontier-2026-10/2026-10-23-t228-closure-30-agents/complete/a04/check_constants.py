"""Reproducible arithmetic checks; analytic inequalities are in REPORT.md."""
import math
delta = 1e-3
q1 = 4 / math.sqrt(2 * math.pi * math.e)
remainder = delta * (4 + 2 * math.sqrt(2 / math.pi)) + 3 * delta**2
uniform_lipschitz = q1 + .01 + 1.01 * remainder
print(f"E|1-a^2| = {q1:.15f}")
print(f"uniform E Lipschitz upper bound = {uniform_lipschitz:.15f}")
print(f"uniform lower bound E A^2 = {1-2*.99+3*.99**2:.15f}")
assert uniform_lipschitz < 1
assert q1 + .01 < 1
assert 1 - 2*.99 + 3*.99**2 > 1

