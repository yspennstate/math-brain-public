from fractions import Fraction
import sympy as sp
from itertools import product

rt2=sp.sqrt(2)
z=4+3*rt2
A=sp.Matrix([
[1,1,-2,-2,-2,-2],
[1,1,-2,-2,-2,-2],
[-2,-2,1,1,-2,-2],
[-2,-2,1,1,-2,-2],
[-2,-2,-2,-2,1,1],
[-2,-2,-2,-2,1,1],
])/6
B=sp.eye(3)-sp.Rational(2,3)*sp.ones(3)
y=sp.Matrix([1,1,z])
assert sp.simplify((y.T*B*y)[0])==0
assert sorted([ev for ev,mult in A.eigenvals().items() for _ in range(mult)], key=lambda x: float(x))==[-1,0,0,0,1,1]

c=[1/sp.sqrt(2),1/sp.sqrt(2),1/sp.sqrt(2),1/sp.sqrt(2),z/sp.sqrt(2),z/sp.sqrt(2)]
def T(v):
    return sp.Matrix([(v[0]+v[1])/sp.sqrt(2),(v[2]+v[3])/sp.sqrt(2),(v[4]+v[5])/sp.sqrt(2)])
mins=None
for bits in product([0,1], repeat=6):
    if not any(bits):
        continue
    yy=T([c[i]*bits[i] for i in range(6)])
    norm2=sp.simplify(sum(t*t for t in yy))
    if mins is None or sp.N(norm2-mins) < 0:
        mins=norm2
assert sp.simplify(mins-sp.Rational(1,4))==0

# Rational strict certificate for R>=3600:
# p_* < 508/125, 252 sqrt(6)/R < 630/R, sqrt(2)>140/99.
assert 6 < sp.Rational(25,4)
assert sp.Rational(19600,9801) < 2  # (140/99)^2 < 2
upper=sp.Rational(508,125)+sp.Rational(630,3600)
lower=sp.Rational(140,33)
assert upper < lower
print('PASS QFORM_IRRATIONAL_NULL_FRAGMENT_SUPPRESSION')
print('q(1,1,4+3sqrt2)=',sp.simplify((y.T*B*y)[0]))
print('spectrum=',A.eigenvals())
print('min_nonempty_subset_norm_squared=',mins)
print('remote_error_bound_R3600_lt=',sp.Rational(630,3600))
print('total_upper_R3600_lt=',upper, float(upper))
print('3sqrt2_lower_gt=',lower, float(lower))
print('rational_gap=',sp.simplify(lower-upper), float(lower-upper))
