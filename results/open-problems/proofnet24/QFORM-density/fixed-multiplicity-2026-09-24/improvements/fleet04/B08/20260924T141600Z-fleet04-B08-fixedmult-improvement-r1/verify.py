from fractions import Fraction as F
from math import factorial, ceil


def L(x, n=60):
    x = F(x)
    return sum(x**k / factorial(k) for k in range(n + 1))


def U(x, n=60):
    x = F(x)
    term = x**(n + 1) / factorial(n + 1)
    return L(x, n) + term / (1 - x / F(n + 2))


# Integral on [0,1]: exp(-x) is at most the even alternating
# Taylor truncation of degree 8.
gamma_upper = sum(F((-1)**k, factorial(k)) * F(8, 8*k + 3)
                  for k in range(9))

# Integral on [1,8], partitioned into intervals of length 1/16.
# The rounded u is verified exactly by u^8 a^5 >= 1.
for j in range(16, 128):
    a, b = F(j, 16), F(j + 1, 16)
    n = ceil(10**12 * float(a)**(-5/8))
    u = F(n, 10**12)
    while u**8 * a**5 < 1:
        n += 1
        u = F(n, 10**12)
    gamma_upper += u * (1 / L(a) - 1 / U(b))

# Tail [8,infinity].
a = F(8)
n = ceil(10**12 * 8**(-5/8))
u = F(n, 10**12)
while u**8 * a**5 < 1:
    n += 1
    u = F(n, 10**12)
gamma_upper += u / L(a)

assert gamma_upper < F(1187, 500)
assert F(1543, 1000)**8 > 32
assert F(5000, 3759)**4 < F(314, 100)

e_upper = sum(F(1, factorial(k)) for k in range(10))
e_upper += F(1, factorial(10)) / (1 - F(1, 11))
assert e_upper < F(68, 25)
assert F(68, 25)**3 < F(182, 125)**8

cq_upper = F(1543, 1000) * F(3759, 5000)
cq_upper *= F(182, 125) * F(1187, 500)
assert cq_upper < F(401, 100)

for x, target in [(F(347, 500), F(2)), (F(139, 100), F(401, 100))]:
    exp_lower = sum(x**k / factorial(k) for k in range(13))
    assert exp_lower > target

h_scalar_truncated = 10 * (
    F(22, 7) + 4 * F(347, 500) + 2 * F(239, 25)
)
h_scalar_full = h_scalar_truncated + 1
density_bound = 10 * h_scalar_full
assert density_bound < 2514

print("PASS")
print("Gamma(3/8) upper =", float(gamma_upper))
print("C_q upper =", float(cq_upper))
print("scalar half-potential upper =", float(h_scalar_full))
print("density constant upper =", float(density_bound))
