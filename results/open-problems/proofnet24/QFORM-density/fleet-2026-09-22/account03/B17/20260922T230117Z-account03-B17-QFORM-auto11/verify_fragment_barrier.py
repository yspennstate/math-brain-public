from fractions import Fraction as F
import math


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


O = [
    [F(6, 7), F(-2, 7), F(-3, 7)],
    [F(-2, 7), F(3, 7), F(-6, 7)],
    [F(-3, 7), F(-6, 7), F(-2, 7)],
]
J = [
    [F(1), F(0), F(0)],
    [F(0), F(1), F(0)],
    [F(0), F(0), F(-1)],
]
I3 = [[F(int(i == j)) for j in range(3)] for i in range(3)]
assert matmul(transpose(O), O) == I3

B = matmul(matmul(transpose(O), J), O)
B_expected = [
    [F(31, 49), F(-36, 49), F(-12, 49)],
    [F(-36, 49), F(-23, 49), F(-24, 49)],
    [F(-12, 49), F(-24, 49), F(41, 49)],
]
assert B == B_expected

u = [O[2][j] ** 2 for j in range(3)]
assert u == [F(9, 49), F(36, 49), F(4, 49)]
assert sum(u) == 1

partner_deficit = F(5295, 21952)
assert partner_deficit > F(69, 320)


def rkl(k, l):
    return math.exp(
        math.lgamma(k + l + 0.5)
        - math.lgamma(l + 0.5)
        - math.lgamma(k + 1)
        - (k + l) * math.log(2.0)
    )


# Finite diagnostic for the analytically proved bound
# r_00=1 and sup_(k,l)!=(0,0) r_kl = 1/2, attained at (0,1).
mx = 0.0
arg = None
for k in range(80):
    for l in range(80):
        if k == 0 and l == 0:
            continue
        value = rkl(k, l)
        if value > mx:
            mx = value
            arg = (k, l)
assert abs(mx - 0.5) < 1e-12
assert arg == (0, 1)


def poisson_pmf(mu, N=120):
    p = [math.exp(-mu)]
    for k in range(1, N):
        p.append(p[-1] * mu / k)
    return p


def Rj(a, uj, N=120):
    alpha = 12.0 * a * a * (1.0 - float(uj))
    beta = 12.0 * a * a * float(uj)
    pk = poisson_pmf(alpha / 2.0, N)
    pl = poisson_pmf(beta / 2.0, N)
    total = 0.0
    for k, p in enumerate(pk):
        for l, q in enumerate(pl):
            total += p * q * rkl(k, l)
    return total


print("O^T O = I: PASS")
print("B = O^T J O exact: PASS")
print("u =", [str(x) for x in u])
print("partner deficit =", float(partner_deficit))
print("finite-grid nonzero max r_kl =", mx, "at", arg)

for a in (0.25, 0.5, 1.0, 2.0):
    values = [Rj(a, uj) for uj in u]
    common_bound = (1.0 + math.exp(-6.0 * a * a)) / 2.0
    assert all(value <= common_bound + 1e-12 for value in values)
    deficit_c1 = float(partner_deficit) + sum(1.0 - value for value in values)
    print(
        "a=", a,
        "R=", [round(value, 14) for value in values],
        "bound=", round(common_bound, 14),
        "first-order deficit c=1=", round(deficit_c1, 14),
    )

print("PASS QFORM-RARE-FRAGMENT-FIRST-ORDER-BARRIER-v1")
