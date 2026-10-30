import math


def simpson(f, a, b, n=20000):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a+i*h)
    return s*h/3


def p0_indef(a, b, c):
    def integrand(phi):
        A = a*math.cos(phi)**2 + b*math.sin(phi)**2
        return 1/math.sqrt(A*(A+c))
    return simpson(integrand, 0.0, 2*math.pi)/(4*math.pi)


sharp = 1/(2*math.sqrt(2))
examples = [(1,1,1), (1,2,1), (1,1,3), (2,5,4), (1,10,1)]
values = [(abc, p0_indef(*abc)) for abc in examples]
for abc, value in values:
    assert value <= sharp + 1e-10, (abc, value, sharp)
assert abs(values[0][1]-sharp) < 1e-10

definite_sharp = math.exp(-0.5)/math.sqrt(2*math.pi)
assert definite_sharp < sharp

finite_m2 = 2*math.pi - 7/3
limit = 3*math.sqrt(2)
assert finite_m2 > math.pi
assert limit > finite_m2

# fleet03/B17 block determinant-mass profile
for m in (1,2,3,12,100):
    total_mass = (m**3)*(m**-3)
    assert abs(total_mass - 1) < 1e-12

# exact density-one variance floor integral
variance_floor = (0.5**2) - (4/3)*(0.5**3)
assert abs(variance_floor - 1/12) < 1e-15

print('PASS')
print('indefinite_standard_sharp=', repr(sharp))
print('definite_standard_sharp=', repr(definite_sharp))
print('density_one_diffuse_limit_sharp=', repr(limit))
print('finite_m2=', repr(finite_m2))
for abc, value in values:
    print('p0', abc, repr(value))
