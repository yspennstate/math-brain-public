from fractions import Fraction
from math import e, sqrt

# A deterministic finite-union quantile example.
lengths = [Fraction(1,5), Fraction(7,20), Fraction(9,20)]
starts = [Fraction(-3,1), Fraction(1,1), Fraction(5,1)]
assert sum(lengths) == 1

s = [Fraction(0,1)]
for ell in lengths:
    s.append(s[-1] + ell)

c = [starts[k] - s[k] for k in range(3)]
assert c == [Fraction(-3,1), Fraction(4,5), Fraction(89,20)]
assert c[1]-c[0] == Fraction(19,5)
assert c[2]-c[1] == Fraction(73,20)
assert c[0] <= c[1] <= c[2]

# On every quantile cell T(u)=u+c, so the quadratic expansion is exact
# algebraically: (u+c)^T A (u+c)=u^T A u+2(Ac)^T u+c^T A c,
# and the Hessian is 2A, independent of c.

C5 = 10 * sqrt(2*e)
assert 23.316 < C5 < 23.317
assert 46.632 < 2*C5 < 46.633

# Fiber length check for q(x)=a(x-h)^2+d.  If the target interval has
# length L, the total x-length of q^{-1}(J) is at most 2 sqrt(L/|a|).
# The far-from-vertex case reduces to
# 2(sqrt(beta)-sqrt(alpha)) <= 2 sqrt(beta-alpha).
for p in range(1,20):
    for q in range(p+1,30):
        alpha = Fraction(p,7)
        beta = Fraction(q,7)
        lhs = 2*(sqrt(float(beta))-sqrt(float(alpha)))
        rhs = 2*sqrt(float(beta-alpha))
        assert lhs <= rhs + 1e-14

print('length_sum=1')
print('pure_gap_offsets=-3,4/5,89/20')
print('gap_increments=19/5,73/20')
print(f'C5={C5:.15f}')
print(f'2C5={2*C5:.15f}')
print('fiber_length_inequality_grid=PASS')
print('QFORM_B13_R27_QUANTILE_CUBE_CHECK_PASS')
