from fractions import Fraction
from math import erf, pi, sqrt

patterns = [
    (1,1,1),
    (1,-1,1),
    (1,1,-1),
    (1,-1,-1),
]

gram = [[sum(p[i]*p[j] for p in patterns) for j in range(3)] for i in range(3)]
assert gram == [[4,0,0],[0,4,0],[0,0,4]]

for m in (1,2,3,5,17,101):
    N = 4*m
    parseval = [[Fraction(m,N)*gram[i][j] for j in range(3)] for i in range(3)]
    assert parseval == [[Fraction(int(i==j),1) for j in range(3)] for i in range(3)]
    assert Fraction(3,N) == Fraction(3,4*m)

lam = (1,1,-1)
assert sorted(lam) == [-1,1,1]

def I(alpha):
    if alpha == 0:
        return 1.0
    return sqrt(pi)/(2*sqrt(alpha))*erf(sqrt(alpha))

worst = 0.0
for j in range(0,20001):
    alpha = 20.0*j/20000.0
    lhs = I(alpha)
    rhs = (1+2*alpha/3)**(-0.5)
    assert lhs <= rhs + 2e-14
    worst = max(worst, lhs-rhs)

peak = 3*sqrt(2)
assert abs(peak - 4.242640687119285) < 2e-15

def p0_minority(ell):
    if ell == 0:
        return peak
    a = 3*ell/(2*(2-ell))
    return 6/sqrt(2-ell)*I(a)

vals = [p0_minority(j/1000) for j in range(1001)]
assert max(vals) <= peak + 2e-14
for a,b in zip(vals, vals[1:]):
    assert b <= a + 2e-13

print("PASS")
print("gram=", gram)
print("peak=", repr(peak))
print("minority_endpoint_ell1=", repr(vals[-1]))
print("integral_grid_max_violation=", repr(worst))
