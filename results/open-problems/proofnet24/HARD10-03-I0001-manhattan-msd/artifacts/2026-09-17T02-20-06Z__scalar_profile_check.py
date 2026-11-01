from fractions import Fraction


def T(theta):
    return Fraction(1, 1) - theta / 2


fixed = Fraction(2, 3)
theta = Fraction(0, 1)
rows = []
for n in range(7):
    invariant = ((-2) ** n) * (theta - fixed)
    rows.append((n, theta, invariant))
    assert invariant == Fraction(-2, 3)
    theta = T(theta)

assert T(fixed) == fixed
rho_star = Fraction(1, 4) + fixed / 8
assert rho_star == Fraction(1, 3)

p_outer = Fraction(3, 4) - fixed / 8
q_inner = Fraction(1, 2) + fixed / 4
assert p_outer == q_inner == Fraction(2, 3)

# Solve the scale-matching equation:
# 3/4 - theta/8 = 1/2 + theta/4.
theta_match = (Fraction(3, 4) - Fraction(1, 2)) / (Fraction(1, 8) + Fraction(1, 4))
assert theta_match == Fraction(2, 3)

# Finite-dimensional counterexample to automatic scalar/diagonal Schur closure.
# C = I, B = [[1,1],[0,1]], so B C^{-1} B^T has a nonzero off-diagonal.
B = [[Fraction(1), Fraction(1)],
     [Fraction(0), Fraction(1)]]
M = [[sum(B[i][k] * B[j][k] for k in range(2)) for j in range(2)] for i in range(2)]
assert M == [[Fraction(2), Fraction(1)],
             [Fraction(1), Fraction(1)]]
assert M[0][1] != 0

print("scalar exponent recursion theta_{n+1}=1-theta_n/2, theta_0=0")
for n, th, inv in rows:
    print(f"n={n}: theta={th}; invariant=(-2)^n(theta-2/3)={inv}")
print(f"fixed_point={fixed}")
print(f"target_resolvent_exponent=1/4+theta*/8={rho_star}")
print(f"outer_scale_exponent={p_outer}")
print(f"inner_transition_exponent={q_inner}")
print(f"scale_matching_theta={theta_match}")
print(f"BC^-1B^T={M}")
print("OFF_DIAGONAL_SCHUR_COUNTEREXAMPLE_PASS")
print("ALL_EXACT_CHECKS_PASS")
