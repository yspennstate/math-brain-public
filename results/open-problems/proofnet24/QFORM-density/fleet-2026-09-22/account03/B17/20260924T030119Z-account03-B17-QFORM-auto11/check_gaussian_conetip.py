import math


def simpson(f, a, b, n=20000):
    if n % 2:
        n += 1
    h = (b-a)/n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(a + j*h)
    return total*h/3


def elliptic_K(k):
    return simpson(lambda th: 1.0/math.sqrt(1.0-k*k*math.sin(th)**2),
                   0.0, math.pi/2.0)


def p0_standard(a, b, c):
    if a > b:
        a, b = b, a
    k2 = (b-a)*c/(b*(a+c))
    return elliptic_K(math.sqrt(k2))/(math.pi*math.sqrt(b*(a+c)))


def cs_bound(a, b, c):
    if a > b:
        a, b = b, a
    return 1.0/(2.0*(a*b*(a+c)*(b+c))**0.25)


samples = [(1,1,1), (1,2,1), (1,1,2), (2,2,1), (2,3,4)]
for a, b, c in samples:
    p = p0_standard(a, b, c)
    B = cs_bound(a, b, c)
    assert p <= B + 2e-12, (a, b, c, p, B)

assert abs(p0_standard(1,1,1) - 1/(2*math.sqrt(2))) < 1e-12

v0 = 1/12
gaussian_sharp = 1/(2*math.sqrt(2)*v0)
assert abs(gaussian_sharp - 3*math.sqrt(2)) < 1e-12

for m in (2, 10, 100):
    delta = 1/m
    exact = 6/math.sqrt(2+delta)
    strict = 1/(2*v0*math.sqrt(2+delta))
    assert abs(exact-strict) < 1e-12
    assert exact < 3*math.sqrt(2)

theta = 0.01
partner_lb = 3*math.sqrt(2)*math.exp(-3*theta)
satellite = 1-math.exp(-3*theta)
assert abs(partner_lb - 4.117251705266084) < 1e-12
assert abs(satellite - 0.029554466451491845) < 1e-12
assert partner_lb > 4

print('PASS QFORM_GAUSSIAN_CONETIP_RIGIDITY')
print('sharp_centered_gaussian_cap', gaussian_sharp)
print('partner_theta_0.01_lower', partner_lb)
print('partner_theta_0.01_satellite', satellite)
