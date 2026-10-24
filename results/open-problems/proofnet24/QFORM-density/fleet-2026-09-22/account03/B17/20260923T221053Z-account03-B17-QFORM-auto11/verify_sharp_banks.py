from fractions import Fraction as F
from math import sqrt


def h4(u):
    return (F(57) + F(6)*u - F(39)*u*u) / F(32)


def h6(u):
    return -F(15)*(F(19)*u**3 - F(111)*u**2 + F(45)*u + F(63)) / F(128)


def h8(u):
    return F(105)*(F(611)*u**4 - F(492)*u**3 - F(1902)*u**2 + F(1044)*u + F(867)) / F(2048)


def k44(u, v):
    p = (F(21385)*u*u*v*v - F(3690)*u*u*v - F(951)*u*u
         - F(3690)*u*v*v - F(11412)*u*v + F(1566)*u
         - F(951)*v*v + F(1566)*v + F(2601))
    return F(3)*p/F(2048)


def second(vals):
    ans = sum((h6(x)/F(105) + h8(x)/F(800) for x in vals), F(0))
    for i in range(3):
        for j in range(i+1, 3):
            ans += k44(vals[i], vals[j])/F(400)
    return ans


# Single-bank controls.
assert h4(F(0)) == F(57, 32)
assert h4(F(1)) == F(3, 4)
assert h4(F(1, 3)) == F(41, 24)
assert h6(F(0))/F(105) + h8(F(0))/F(800) == F(-4833, 327680)
assert h6(F(1))/F(105) + h8(F(1))/F(800) == F(-173, 17920)

# Partner account04/B17 rational rotation.
u_partner = [F(9, 49), F(36, 49), F(4, 49)]
d1_partner = sum((h4(x)/F(20) for x in u_partner), F(0))
d2_partner = second(u_partner)
assert d1_partner == F(5295, 21952)
assert d2_partner == F(-3257268323, 337323212800)

# Aligned and balanced second-order controls.
assert sum((h4(x)/F(20) for x in [F(1), F(0), F(0)]), F(0)) == F(69, 320)
assert second([F(1), F(0), F(0)]) == F(-17411, 2867200)
assert sum((h4(x)/F(20) for x in [F(1,3)]*3), F(0)) == F(41, 160)
assert second([F(1,3)]*3) == F(-3511, 460800)

# First-order concavity and fixed-total-dimension optimum.
# h4'' = -39/16 < 0, so the simplex minimum is at a vertex.
assert F(-39, 16) < 0
K = F(63, 160) + 3*sqrt(38)/80
same_bank_total_N = F(207, 320)
assert float(same_bank_total_N) > K

# Exact genuinely rotated rational Householder stress family, sample N=100.
N = 100
den = N**4 + 5
w = [F(2*N*N, den), F(4*N*N, den), F(N**4-5, den)]
assert sum(x*x for x in w) == 1
B = [[(F(1) if i == j else F(0)) - 2*w[i]*w[j] for j in range(3)] for i in range(3)]

def matmul(A, C):
    return [[sum((A[i][k]*C[k][j] for k in range(len(C))), F(0))
             for j in range(len(C[0]))] for i in range(len(A))]

I = [[F(int(i == j)) for j in range(3)] for i in range(3)]
assert matmul(B, B) == I
assert sum(B[i][i] for i in range(3)) == 1
assert all(B[i][j] != 0 for i in range(3) for j in range(3))

print('partner_D1 =', d1_partner, float(d1_partner))
print('partner_D2 =', d2_partner, float(d2_partner))
print('aligned_D1 =', F(69,320), float(F(69,320)))
print('aligned_D2 =', F(-17411,2867200), float(F(-17411,2867200)))
print('balanced_D1 =', F(41,160), float(F(41,160)))
print('balanced_D2 =', F(-3511,460800), float(F(-3511,460800)))
print('K_total_dimension =', K)
print('equal_bank_total_dimension =', float(same_bank_total_N))
print('improvement =', float(same_bank_total_N)-K)
print('sample_w =', w)
print('sample_B_diagonal =', [B[i][i] for i in range(3)])
print('PASS QFORM_SHARP_BANK_SECOND_ORDER')
