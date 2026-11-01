from fractions import Fraction

# PROB10-10 exact arithmetic certificate for the 15/8 cone extension.
# No floating-point value is used in any asserted inequality.

A = Fraction(189, 100)
B = Fraction(291, 100)
w = [A, 1 / A, B, 1 / B]  # E,W,N,S tilted step weights
opp = [1, 0, 3, 2]

# Rational positive Collatz vector, normalized so min(z_i)=1.
z = [
    Fraction(2095936, 10**6),
    Fraction(1469509, 10**6),
    Fraction(2181303, 10**6),
    Fraction(1, 1),
]
r = Fraction(5083, 1000)

M = [[Fraction(0) for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        if j != opp[i]:
            M[i][j] = w[j]

ratios = []
for i in range(4):
    mz = sum(M[i][j] * z[j] for j in range(4))
    ratios.append(mz / z[i])

collatz_ok = all(x <= r for x in ratios)
zmin_ok = all(x >= 1 for x in z)

# Chernoff parameters. q<1 is the geometric-series ratio after summing path lengths.
s = Fraction(1021, 250)
q = r / (1 + s)
q_ok = q == Fraction(5083, 5084) and q < 1

# Boundary cone slope and lower time-constant coefficient.
rho = Fraction(15, 8)
c = Fraction(1291, 2000)

# At rho=15/8,
#   beta^8 = A^-8 B^-15 exp(8 s c) q^23.
# Certify exp(x) by the elementary exact inequality
#   exp(x) < (1-x/m)^(-m),  0<x<m,
# which follows from -log(1-u)>u for 0<u<1.
x = 8 * s * c
m = 8000
exp_domain_ok = 0 < x < m
exp_upper = (1 - x / Fraction(m, 1)) ** (-m)
beta8_upper = A ** (-8) * B ** (-15) * q ** 23 * exp_upper
beta_ok = beta8_upper < 1

# Finite prefactor in
# P(T(0,n(a,b)) <= c*a*n) <= C * beta^(a*n), b/a >= 15/8.
# W_m <= (w^T z) r^(m-1) = K r^m.
K = sum(w[i] * z[i] for i in range(4)) / r
C = K / (1 - q)

# Consume the exact axis upper bound from the proved P04 ladder theorem.
a0 = Fraction(
    127596793342690034600361684870097,
    197703921604834678505472000000000,
)
delta = 2 * (c - a0)
defect_ok = delta > 0

print("PROB10-10 exact 15/8 cone-tilt certificate")
print("A=", A, "B=", B, "r=", r)
print("z=", ",".join(str(v) for v in z))
print("collatz_ratios=", ",".join(str(v) for v in ratios))
print("collatz_ok=", collatz_ok)
print("zmin_ok=", zmin_ok)
print("s=", s, "q=", q, "q_ok=", q_ok)
print("rho=", rho, "c=", c)
print("x=8*s*c=", x, "m=", m, "exp_domain_ok=", exp_domain_ok)
print("beta8_upper_lt_1=", beta_ok)
print("beta8_upper_decimal=", float(beta8_upper))
print("beta_upper_decimal=", float(beta8_upper) ** (1 / 8))
print("K=", K)
print("C=", C)
print("a0=", a0)
print("delta=2*(c-a0)=", delta)
print("delta_decimal=", float(delta))
print("defect_ok=", defect_ok)

assert collatz_ok
assert zmin_ok
assert q_ok
assert exp_domain_ok
assert beta_ok
assert defect_ok
print("ALL_EXACT_CHECKS_PASS = True")
