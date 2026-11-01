from math import e


def K_general(r, pdet=1.0):
    assert r >= 3 and pdet > 0
    return e * r / (r - 2) * pdet ** (-1.0 / r)


def K_one_physical(r, pdet=1.0):
    assert r >= 3 and pdet > 0
    return e ** 0.5 * r / (r - 2) * pdet ** (-1.0 / r)


def K_square(r, det=1.0):
    assert r >= 3 and det != 0
    return r / (r - 2) * abs(det) ** (-1.0 / r)


def integral_formula(r, A):
    # Exact integral of min(1, A |t|^{-r/2}) over R, evaluated by
    # splitting at t0=A^{2/r}.
    assert r > 2 and A > 0
    alpha = r / 2.0
    t0 = A ** (1.0 / alpha)
    return 2.0 * (t0 + A * t0 ** (1.0 - alpha) / (alpha - 1.0))


print("r general one_physical square")
for r in range(3, 9):
    print(r, f"{K_general(r):.12f}", f"{K_one_physical(r):.12f}", f"{K_square(r):.12f}")

rank3_o0 = K_general(3, 1.0 / 16.0)
print("rank3_o0", f"{rank3_o0:.12f}")
assert rank3_o0 < 20.549
assert K_square(3, 1.0) == 3.0
print("physical_3x3_det1", K_square(3, 1.0))

for r, A in [(3, 2.7), (4, 1.3), (7, 9.1)]:
    lhs = integral_formula(r, A)
    rhs = 2.0 * r / (r - 2) * A ** (2.0 / r)
    print("integral", r, A, lhs, rhs, abs(lhs - rhs))
    assert abs(lhs - rhs) < 1e-12

print("STATUS=QFORM_B19_EXACT_CROSS_L2_CHECK_PASS")
