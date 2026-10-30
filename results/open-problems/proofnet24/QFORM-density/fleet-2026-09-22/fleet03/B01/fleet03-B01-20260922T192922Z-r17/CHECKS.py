import math

for p in (2.1, 2.25, 2.5, 3.0, 4.0, 6.0, 10.0):
    C = (4*math.pi*(p-1))**(1/p) * ((p-1)/(p-2))**((p-1)/p)
    assert math.isfinite(C) and C > 0

C3 = (32*math.pi)**(1/3)
assert abs(C3**3 - 32*math.pi) < 1e-12
assert abs(C3**3/(2*math.pi) - 16.0) < 1e-12

# Optimizer in the square-density L^r estimate.
for r in (1.1, 1.25, 1.5, 1.75, 1.9):
    R = (r-1)/2
    lhs = 2*R**(2-r)/(2-r) + R**(1-r)
    rhs = R**(1-r)/(2-r)
    assert abs(lhs-rhs) < 1e-12*max(1.0, abs(rhs))

print('C3=', repr(C3))
print('density_constant=', repr(C3**3/(2*math.pi)))
print('STATUS=PASS')
