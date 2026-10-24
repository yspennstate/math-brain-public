from fractions import Fraction
from math import sqrt

# Edgeworth polynomial coefficients.
a = Fraction(57, 32)
b = Fraction(15, 4)
c = Fraction(3, 4)
A = Fraction(57, 8)
B = Fraction(3, 4)

assert a + c - b == Fraction(-39, 32)


def discrete_min(r):
    vals = []
    for k in range(1, r):
        val = A / k + B / (r - k)
        vals.append((val, k))
    return min(vals)

# Positive-definite Hessian for the one-mixed-row reduced problem occurs
# iff H=31pq-19p-19q-19<0.  For positive integers this forces one
# coordinate to equal 1 and the other <=3.
pd_cases = []
for p in range(1, 40):
    for q in range(1, 40):
        H = 31*p*q - 19*p - 19*q - 19
        if H < 0:
            vstar = Fraction(-19*(p - 5*q + 1), H)
            pd_cases.append((p, q, H, vstar))
            assert vstar < 0

assert [(p, q) for p, q, _, _ in pd_cases] == [
    (1, 1), (1, 2), (1, 3), (2, 1), (3, 1)
]

expected = {
    3: (2, Fraction(69,16)),
    4: (3, Fraction(25,8)),
    5: (4, Fraction(81,32)),
    6: (4, Fraction(69,32)),
    7: (5, Fraction(9,5)),
    8: (6, Fraction(25,16)),
    9: (7, Fraction(39,28)),
    12: (9, Fraction(25,24)),
}
for r, (k_expected, m_expected) in expected.items():
    m, k = discrete_min(r)
    assert k == k_expected
    assert m == m_expected

m4, k4 = discrete_min(4)
assert k4 == 3 and m4 == Fraction(25, 8)
assert Fraction(4,20) * m4 == Fraction(5,8)

# Exact r=4 physical matrix: top-left block is P=I-(1/3)11^T,
# hence P^2=P, P 1=0 and tr(P)=2; the last eigenvalue is -1.
P = [
    [Fraction(2,3), Fraction(-1,3), Fraction(-1,3)],
    [Fraction(-1,3), Fraction(2,3), Fraction(-1,3)],
    [Fraction(-1,3), Fraction(-1,3), Fraction(2,3)],
]

def mmul(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))]
            for i in range(len(X))]

assert mmul(P, P) == P
assert [sum(row) for row in P] == [0, 0, 0]
assert sum(P[i][i] for i in range(3)) == 2

rho = sqrt(float(A))/(sqrt(float(A))+sqrt(float(B)))
kappa = (sqrt(float(A))+sqrt(float(B)))**2
beta_star = kappa/20
beta4 = float(Fraction(5,8))
assert beta4 > beta_star

print("PASS QFORM-FINITE-PERIOD-EDGEWORTH-OPT-v1")
print("a+c-b =", a+c-b)
print("positive-definite one-mixed cases =", [(p,q) for p,q,_,_ in pd_cases])
print("rho = %.15f" % rho)
print("kappa* = %.15f" % kappa)
print("beta* = %.15f" % beta_star)
print("r=4: M_4 = %s, beta_4 = %s, gap = %.15g" % (m4, Fraction(5,8), beta4-beta_star))
