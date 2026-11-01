from fractions import Fraction as F


def gamma(r, beta2):
    r = F(r)
    beta2 = F(beta2)
    return r * (-1 + beta2 * (r - 1) / 2)


def threshold(beta2):
    beta2 = F(beta2)
    return 1 + F(2, 1) / beta2

# Fixed candidate beta^2 = 1.
beta2 = F(1, 1)
theta = 1 - beta2 / 2
assert theta == F(1, 2)
assert threshold(beta2) == F(3, 1)
assert gamma(2, beta2) == F(-1, 1)
assert gamma(3, beta2) == 0
assert gamma(4, beta2) == F(2, 1)

print('fixed beta^2 = 1')
print('coercivity theta =', theta)
print('critical r_c =', threshold(beta2))
print('gamma_2 =', gamma(2, beta2))
print('gamma_3 =', gamma(3, beta2))
print('gamma_4 =', gamma(4, beta2))

# Family sanity checks for the no-uniform-range corollary.
# For each rational R>2 use beta^2 = 1 + 1/(R-1), which lies in (2/(R-1),2).
for R in [F(5, 2), F(3), F(4), F(10)]:
    b2 = 1 + F(1, 1) / (R - 1)
    rc = threshold(b2)
    assert F(0) < b2 < 2
    assert rc < R
    print(f'R={R}: beta^2={b2}, r_c={rc}, r_c<R={rc < R}')

print('ALL EXACT CHECKS PASSED')
