from math import sqrt, log
import random

# Fixed constants used in REPORT.md.
delta = 1/8
a0 = sqrt((1-delta**2)/2)
C_tail = 4/(1-1/4)
C_log = 2/(1-1/16)
c0 = 48**(1/3)
C_small = (16/3 + (32/15)*(2 + 3*log(1+c0*a0)))/a0
C_large = 128*delta**(-1/4)

print(f"delta={delta}")
print(f"a0={a0:.15f}")
print(f"C_tail={C_tail:.15f}")
print(f"C_log={C_log:.15f}")
print(f"C_small={C_small:.15f}")
print(f"C_large={C_large:.15f}")
print("C3=216")

assert a0 > delta
assert delta/a0 < 1/4
assert C_small < 26
assert C_large < 216

# Algebra: K satisfies K^2-2aK+d1*d2=0, so
# K(x+d2*y/K)(y+d1*x/K) has coefficients d1, 2a, d2.
for _ in range(10000):
    d1 = random.uniform(-delta, delta)
    d2 = random.uniform(-delta, delta)
    # choose an off-diagonal coefficient satisfying the proof branch
    a = random.choice((-1,1))*random.uniform(a0, 4)
    Delta = a*a-d1*d2
    K = a + (1 if a>0 else -1)*sqrt(Delta)
    lam = d2/K
    mu = d1/K
    # normalized coefficient residuals
    r_x2 = abs(K*mu-d1)
    r_y2 = abs(K*lam-d2)
    r_xy = abs(K*(1+lam*mu)-2*a)
    assert max(r_x2,r_y2,r_xy) < 1e-11
    assert max(abs(lam),abs(mu)) < 1/4
    A=abs(a)
    L=abs(K)*Delta
    assert L <= 6*A**3 + 1e-10

print("factorization_random_checks=10000")
print("STATUS=PASS")
