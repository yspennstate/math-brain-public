#!/usr/bin/env python3
import json
import math

CSTAR = 8.45302122552817687470491804598

def c_m(m):
    return math.factorial(m) ** (3.0/m) / 6.0

def hadamard(n):
    H = [[1]]
    while len(H) < n:
        H = [row + row for row in H] + [row + [-x for x in row] for row in H]
    if len(H) != n:
        raise ValueError("n must be a power of two")
    return H

# Rank-free combinatorial constant checks for several m and many finite ranks.
for m in range(4, 11):
    cm = c_m(m)
    for r in range(m, 1000):
        finite = math.comb(r, 3) / (math.comb(r, m) ** (3.0/m))
        assert finite + 1e-12 >= cm

c4 = c_m(4)
assert abs(c4 - (32.0/3.0)**0.25) < 1e-14
C4DOWN = CSTAR * c4 ** (-1.0/6.0)

# Dense rotated-indefinite Hadamard test.
N = 64
H = hadamard(N)
for i in range(N):
    for j in range(N):
        dot = sum(H[i][k]*H[j][k] for k in range(N))
        assert dot == (N if i == j else 0)

E3 = math.comb(N, 3)
E4 = math.comb(N, 4)
assert E3 >= c4 * (E4 ** 0.75) - 1e-10

bound_from_E4 = C4DOWN * E4 ** (-1.0/8.0)
bound_from_E3 = CSTAR * E3 ** (-1.0/6.0)
rank64_crossing = 2.0*N/(N-2.0)

result = {
    "marker": "QFORM_B04_R47_HIGHER_COMPOUND_DOWNSHIFT_CHECK_PASS",
    "C_star": CSTAR,
    "c4": c4,
    "C_down_4": C4DOWN,
    "N": N,
    "E3": E3,
    "E4": E4,
    "bound_from_E4": bound_from_E4,
    "bound_from_exact_E3": bound_from_E3,
    "rank64_exact_crossing_comparison": rank64_crossing,
}
print(json.dumps(result, indent=2, sort_keys=True))
