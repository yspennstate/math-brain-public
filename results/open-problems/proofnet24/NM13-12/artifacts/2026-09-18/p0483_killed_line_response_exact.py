from fractions import Fraction

# Exact self-check for NM13-12 / P0483 finite-box response theorem.
#
# Family (d=2): at each site, independently,
#   p^+ = (1/4+t, 1/4-t, 1/4, 1/4)
#   p^- = (1/4-t, 1/4+t, 1/4, 1/4)
# with P(type +)=1/2+2t.
#
# B_L = {(-L,0),...,(L,0)} is killed on first exit.
# Delta_L(t) is the annealed probability of horizontal exit at +(L+1,0)
# minus the annealed probability of horizontal exit at -(L+1,0).
#
# The report proves:
#   Delta_L(t) = [16(L+1)/T_{L+1}(2)] t^2 + O_L(t^4)
# where T_n is the Chebyshev polynomial of the first kind.
#
# This checker verifies, using exact Fraction arithmetic, the finite linear-
# algebra identity underlying the coefficient for L=0,...,8:
#   derivative at t=0 in the homogeneous "+" environment
#     = 4(L+1)/T_{L+1}(2),
# hence the annealed t^2 coefficient is four times this derivative.

def solve_fraction(A, b):
    n = len(A)
    M = [[Fraction(x) for x in A[i]] + [Fraction(b[i])] for i in range(n)]
    for c in range(n):
        pivot = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[pivot] = M[pivot], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r == c:
                continue
            f = M[r][c]
            if f != 0:
                M[r] = [M[r][j] - f * M[c][j] for j in range(n + 1)]
    return [M[i][-1] for i in range(n)]

def T_at_2(n):
    # T_0(2)=1, T_1(2)=2, T_{n+1}(2)=4 T_n(2)-T_{n-1}(2).
    if n == 0:
        return 1
    if n == 1:
        return 2
    a, b = 1, 2
    for _ in range(1, n):
        a, b = b, 4 * b - a
    return b

def baseline_and_uniform_derivative(L):
    N = 2 * L + 1
    A = [[Fraction(int(i == j)) for j in range(N)] for i in range(N)]
    rhs = [Fraction(0) for _ in range(N)]

    # Baseline t=0 equation:
    # u_i = (1/4) u_{i+1} + (1/4) u_{i-1},
    # with horizontal boundary values +1 and -1 and vertical exits valued 0.
    for i in range(N):
        if i + 1 < N:
            A[i][i + 1] -= Fraction(1, 4)
        else:
            rhs[i] += Fraction(1, 4)
        if i - 1 >= 0:
            A[i][i - 1] -= Fraction(1, 4)
        else:
            rhs[i] -= Fraction(1, 4)

    u = solve_fraction(A, rhs)

    # Differentiate the homogeneous "+" equation at t=0:
    # v_i = (1/4)(v_{i+1}+v_{i-1}) + u_{i+1}-u_{i-1},
    # with v on the fixed boundary equal to 0.
    drhs = []
    for i in range(N):
        u_right = u[i + 1] if i + 1 < N else Fraction(1)
        u_left = u[i - 1] if i - 1 >= 0 else Fraction(-1)
        drhs.append(u_right - u_left)

    v = solve_fraction(A, drhs)
    return u[L], v[L]

print("P0483 exact killed-line response self-check")
print("L n T_n(2) baseline_center direct_derivative expected_derivative annealed_t2_coeff")

for L in range(9):
    n = L + 1
    Tn = T_at_2(n)
    u0, deriv = baseline_and_uniform_derivative(L)
    expected = Fraction(4 * n, Tn)
    coeff = 4 * deriv

    assert u0 == 0
    assert deriv == expected

    print(L, n, Tn, u0, deriv, expected, coeff)

expected_coeffs = [
    Fraction(8, 1),
    Fraction(32, 7),
    Fraction(24, 13),
    Fraction(64, 97),
    Fraction(40, 181),
    Fraction(96, 1351),
    Fraction(56, 2521),
    Fraction(128, 18817),
    Fraction(72, 35113),
]
got_coeffs = [
    Fraction(16 * (L + 1), T_at_2(L + 1))
    for L in range(9)
]
assert got_coeffs == expected_coeffs

print("coefficient_sequence =", ",".join(str(x) for x in got_coeffs))
print("ALL_EXACT_CHECKS_PASS")
