from fractions import Fraction
import math

# Sharp subprobability variance identity on centered interval extremizers.
for p in [Fraction(1,10), Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(1,1)]:
    for M in [Fraction(1,1), Fraction(2,1), Fraction(5,2)]:
        L = p/M
        second = M * L**3 / 12
        rhs = p**3 / (12*M**2)
        assert second == rhs

# Tail conversion used in the triangular-array estimate.
for qn in range(101):
    q = Fraction(qn,100)
    p = 1-q
    assert p**3 >= 1-3*q

# Equal-weight rare-tail specialization tends to the 1/12 Gaussian floor.
for m in [10, 100, 1000, 10000]:
    alpha = Fraction(3,2)
    p = 1-alpha/m
    lb = p**3/Fraction(12,1)
    assert lb > 0
    assert abs(float(lb)-1/12) < 1/m

C = 3*math.sqrt(2)
assert 4.2426406871 < C < 4.2426406872
print('PASS')
print('C_3sqrt2=', format(C,'.15f'))
