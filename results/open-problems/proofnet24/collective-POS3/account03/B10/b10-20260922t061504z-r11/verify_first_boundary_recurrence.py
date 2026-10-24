from fractions import Fraction


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def R_extensions(n):
    if n == 7:
        return 168
    if n >= 8:
        return 8 * fib(n + 1) - 13 * fib(n - 7)
    raise ValueError(n)


# Algebraic regression for the one-step boundary identity.  A current
# exact-two state reached from a preceding exact-two state has
#   Z=K-A, X=A_prev+A-K, C=A.
# The actual next fringe count is B=Y+Z+W; keeping W in the check makes
# the cancellation explicit even before specializing to the inherited
# W=0 exact-to-exact state.
algebra_tuples = 0
for A_prev in range(15):
    for A in range(15):
        for K in range(A, 25):
            Z = K - A
            X = A_prev + A - K
            if X < 0:
                continue
            for Y in range(15):
                for W in range(15):
                    C = A
                    E = A + C + X + Y + Z + W
                    B = Y + Z + W
                    assert E + K - A_prev - 3 * A == B
                    algebra_tuples += 1


# Exact calibration on the account04/B11 R_N family.  For the last
# exact-two state, A=E_{N-3}; for its predecessor,
# A_prev=2 E_{N-4}; and the far boundary count is B=E_{N-2}.
# Fibonacci recurrence gives A_prev+3A=E_N, hence B=K exactly.
partner_checks = 0
for N in range(11, 201):
    E = R_extensions(N)
    A_prev = 2 * R_extensions(N - 4)
    A = R_extensions(N - 3)
    B = R_extensions(N - 2)
    assert A_prev + 3 * A == E
    K = A_prev + 3 * A + B - E
    assert K == B
    q = Fraction(B, E)
    assert Fraction(1, 3) < q < Fraction(2, 5)
    partner_checks += 1

N = 30
E = R_extensions(N)
A_prev = 2 * R_extensions(N - 4)
A = R_extensions(N - 3)
B = R_extensions(N - 2)
K = A_prev + 3 * A + B - E

print("POS3_FIRST_BOUNDARY_RECURRENCE_PASS")
print("algebra_tuples_checked", algebra_tuples)
print("partner_RN_boundary_checks", partner_checks)
print(
    "R30",
    {
        "E": E,
        "A_prev": A_prev,
        "A": A,
        "B": B,
        "K": K,
        "B_over_E": str(Fraction(B, E)),
    },
)
