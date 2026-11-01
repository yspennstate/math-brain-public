from sympy import Matrix, sqrt, eye, ones, Rational, E, log, N, kronecker_product


def kron_pow(M, k):
    out = Matrix([[1]])
    for _ in range(k):
        out = kronecker_product(out, M)
    return out


H = Matrix([[1, 1], [1, -1]]) / sqrt(2)
for k in (4, 5):
    A = kron_pow(H, k)
    n = 2**k
    m = n // 2
    assert A.T == A
    assert A.T * A == eye(n)
    B = A[:m, m:]
    assert B * B.T == Rational(1, 2) * eye(m)
    bound = E * Rational(1, 2) * Rational(m, m - 4)
    print("hadamard", n, "cross_sigma_sq=1/2", "density_bound", N(bound, 16))

# Exact maximum leverage of the selected three +1 tensor eigenvectors.
a = (2 + sqrt(2)) / 4
base = Rational(7, 16) + 5 * sqrt(2) / 32
kappa = -log(a) / log(2)
print("selected_frame_max_row_leverage_formula = a^(k-3)*base")
print("a", a, "base", base, "kappa", N(kappa, 16))
for k in (4, 8, 16, 32):
    delta = a ** (k - 3) * base
    print("selected_frame_max_row_leverage", 2**k, N(delta, 16))

# Named-partner witness: O is a 3x3 Householder reflection.
O = eye(3) - Rational(2, 3) * ones(3)
assert O.T * O == eye(3)
K = O * O.T * (eye(3) + O * O.T).inv()
assert K == Rational(1, 2) * eye(3)
theta = K.trace()
D = (eye(3) + O * O.T).det()
assert theta == Rational(3, 2)
assert D == 8
s = Rational(3, 2)
beta = Rational(3, 4)
ratio = beta * s / (beta * s - 1)
assert ratio == 9
partner_bound = 6 * sqrt(E * sqrt(2))
print("partner_theta", theta, "D", D, "beta_s_ratio", ratio)
print("partner_density_bound", N(partner_bound, 16))
print("QFORM_B08_HADAMARD_GLOBAL_RIDGE_CHECK_PASS")
