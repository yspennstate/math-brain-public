from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 60


def C(x):
    return x if x <= F(1, 2) else 1 - x


def T(x):
    return C(2 * x)


def cost(x):
    return x * (1 - 2 * x) / 2


def U(orbit, j):
    n = len(orbit)
    s = F(0)
    fac = F(1)
    for ell in range(n):
        s += fac * cost(orbit[(j + ell) % n])
        fac /= 2
    return s / (1 - F(1, 2**n))


def dec(x, places=24):
    y = Decimal(x.numerator) / Decimal(x.denominator)
    return f"{y:.{places}f}"


y = F(57, 1081)
orbit = [y]
for _ in range(252):
    orbit.append(T(orbit[-1]))
assert len(orbit) == 253
assert T(orbit[-1]) == y
z = F(313, 1081)
assert orbit[17] == z

U0 = U(orbit, 0)
U17 = U(orbit, 17)

a = F(3, 8)
r = F(967, 2048)
x = F(1081, 2048)
q = F(1024, 1081)
s = F(768, 1081)
cw = F(57, 256)
assert x * q == F(1, 2)
assert s * x == a

M0 = x * q * (1 - x) * (1 - q)
M1 = s * x * (1 - s) * (1 - x)

kappa = (
    F(455, 512) * x * U0
    + cw * x * U17
    + F(455, 512) * M0
    + cw * M1
)
A = F(258204856, 10**9)
d0 = F(17611, 10**6)
B = 4 * (cw * a * (1 - a) - r * (1 - r)) + F(465, 256)

assert kappa < F(67635, 10**6)
assert kappa * A < d0
assert B == F(1078193, 1048576)

print("STATUS PASS")
print("period =", len(orbit))
print("T17_y =", z)
print("U_y =", dec(U0))
print("U_z =", dec(U17))
print("kappa =", dec(kappa))
print("kappa_upper = 0.067635000000000000000000")
print("A =", dec(A))
print("kappa_A =", dec(kappa * A))
print("certified_d_coarse = 0.017611000000000000000000")
print("gap_d_minus_kappaA =", dec(d0 - kappa * A))
print("K_required_coarse =", dec(d0 / kappa))
print("center_coefficient_B =", dec(B))
