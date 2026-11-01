import math

C = 3 * 2 ** (8 / 3)
C_time = math.sqrt(2 * math.pi) * C

assert abs(C - 19.048812623618392) < 1e-12
assert abs(C_time - 47.74829232050979) < 1e-12

# Verify the optimizer and closed form for several positive D,kappa.
for D, kappa in [(1.0, 1.0), (4.0, 0.25), (1e-6, 3.0), (17.0, 2e-3)]:
    r = 2 ** (-5 / 6) * (D * kappa) ** (1 / 3)
    rhs = 2 ** (13 / 4) * r ** (-0.5) + 2 ** (7 / 2) * r / math.sqrt(D * kappa)
    closed = C * (D * kappa) ** (-1 / 6)
    assert abs(rhs / closed - 1.0) < 1e-12

# Homogeneity: B -> cB sends D -> c^2 D, kappa -> c kappa,
# and the half-Riesz certificate must scale as c^{-1/2}.
for c in [0.01, 0.3, 2.0, 100.0]:
    D, kappa = 5.0, 0.7
    old = (D * kappa) ** (-1 / 6)
    new = ((c * c * D) * (c * kappa)) ** (-1 / 6)
    assert abs(new / old - c ** (-0.5)) < 1e-12

print(f"C_ind={C:.15f}")
print(f"C_time={C_time:.15f}")
print("QFORM_B03_R20B_CHECK_PASS")
