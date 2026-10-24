from sympy import Matrix, symbols, I, conjugate, expand, simplify, zeros, eye

# Exact algebraic self-check for the representation-theoretic reduction used
# in the accompanying LYAP6 report.  The proof is written on the report page;
# this script checks the canonical identities without floating point arithmetic.


def frob_sq(M):
    return expand(sum(z * conjugate(z) for z in M))


# ----------------------------------------------------------------------
# 1. Exact symbolic 3x3 complex canonical skew-vs-symmetric identity.
# ----------------------------------------------------------------------
names = "ar ai br bi cr ci dr di pr pi qr qi rr ri sr si tr ti"
(ar, ai, br, bi, cr, ci, dr, di,
 pr, pi_, qr, qi, rr, ri, sr, si, tr, ti) = symbols(names, real=True)
a = ar + I*ai
b = br + I*bi
c = cr + I*ci
d = dr + I*di
p = pr + I*pi_
q = qr + I*qi
r = rr + I*ri
s = sr + I*si
t = tr + I*ti
B = Matrix([[a, b, p], [c, d, q], [r, s, t]])

K0 = Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 0]])
D0 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])

Yk = B*K0 + K0*B.T
Ys = B*D0 + D0*B.T

expected_Yk = Matrix([
    [0, a+d, s],
    [-(a+d), 0, -r],
    [-s, r, 0],
])
expected_Ys = Matrix([
    [2*a, b+c, r],
    [b+c, 2*d, s],
    [r, s, 0],
])
assert simplify(Yk - expected_Yk) == zeros(3)
assert simplify(Ys - expected_Ys) == zeros(3)

diff = simplify(expand(frob_sq(Ys) - frob_sq(Yk)))
target = simplify(expand(
    2*(a-d)*conjugate(a-d) + 2*(b+c)*conjugate(b+c)
))
assert simplify(expand(diff - target)) == 0

print("CANONICAL_3X3_IDENTITY_PASS")
print("||M_B(D0)||_F^2-||M_B(K0)||_F^2 = 2|a-d|^2+2|b+c|^2")


# ----------------------------------------------------------------------
# 2. Exact realification identities for the complex-linear / antilinear split.
# ----------------------------------------------------------------------
def split_re_im(M):
    P = M.applyfunc(lambda z: expand(z.as_real_imag()[0]))
    Q = M.applyfunc(lambda z: expand(z.as_real_imag()[1]))
    return P, Q


def realify_linear(M):
    P, Q = split_re_im(M)
    return P.row_join(-Q).col_join(Q.row_join(P))


def realify_antilinear(M):
    P, Q = split_re_im(M)
    return P.row_join(Q).col_join(Q.row_join(-P))


B0 = Matrix([
    [1+2*I, 3-I, 2],
    [4+I, -2+3*I, 5-2*I],
    [1-I, 2+4*I, 3-I],
])
C0 = Matrix([
    [0, 2+I, -1+3*I],
    [-2-I, 0, 4-2*I],
    [1-3*I, -4+2*I, 0],
])
Z0 = Matrix([
    [2, 1+I, 3-I],
    [1-I, -1, 2+2*I],
    [3+I, 2-2*I, 4],
])  # Hermitian

A = realify_linear(B0)
TA = realify_antilinear(C0)
RZ = realify_linear(Z0)
J = zeros(6)
J[:3, 3:] = -eye(3)
J[3:, :3] = eye(3)

assert A*J == J*A
assert TA*J == -J*TA
assert RZ.T == RZ
assert realify_antilinear(C0.T) == TA.T

lhs_anti = A*TA + TA*A.T
rhs_anti = realify_antilinear(B0*C0 + C0*B0.T)
assert lhs_anti == rhs_anti

lhs_lin = A*RZ + RZ*A.T
rhs_lin = realify_linear(B0*Z0 + Z0*B0.conjugate().T)
assert lhs_lin == rhs_lin

print("REALIFICATION_INTERTWINING_PASS")


# ----------------------------------------------------------------------
# 3. Exact direct-sum cross-sector identity in a symbolic 2+1 model.
#    This is only an algebraic self-check of the block formula used in proof.
# ----------------------------------------------------------------------
x1, x2, bb11, bb12, bb21, bb22, cc = symbols(
    "x1 x2 bb11 bb12 bb21 bb22 cc", real=True
)
BB = Matrix([[bb11, bb12], [bb21, bb22]])
xx = Matrix([[x1], [x2]])
CC = Matrix([[cc]])
A3 = zeros(3)
A3[:2, :2] = BB
A3[2, 2] = cc

Xs = zeros(3)
Xs[:2, 2] = xx
Xs[2, :2] = xx.T
Xk = zeros(3)
Xk[:2, 2] = xx
Xk[2, :2] = -xx.T
Ys3 = A3*Xs + Xs*A3.T
Yk3 = A3*Xk + Xk*A3.T

cross = BB*xx + xx*CC.T
assert Ys3[:2, 2] == cross
assert Yk3[:2, 2] == cross
assert simplify(frob_sq(Xs) - frob_sq(Xk)) == 0
assert simplify(frob_sq(Ys3) - frob_sq(Yk3)) == 0
print("DIRECT_SUM_CROSS_SECTOR_PASS")

print("ALL_EXACT_CHECKS_PASS")
