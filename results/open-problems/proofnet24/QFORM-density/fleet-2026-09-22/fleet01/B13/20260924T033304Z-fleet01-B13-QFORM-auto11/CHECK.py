import math
import random

CSTAR = 2278125/(256*math.e**2)
EPS = 1e-11

# Verify the exact normalized tau/four-point identity algebraically on random data.
for _ in range(10000):
    c = 0.01 + 0.32*random.random()
    dk = random.choice([-1.0, 1.0])*(1.0 + 5.0*random.random())
    t = [random.uniform(-4,4) for _ in range(4)]
    s = [0.01 + 0.2*random.random() for _ in range(4)]
    d = [random.uniform(-3,3) for _ in range(4)]
    a = [c*d[i]/s[i] for i in range(4)]
    def G(i,j):
        return dk*(t[i]-t[j])**2 + a[i] + a[j]
    lhs = G(0,1)+G(2,3)-G(0,2)-G(1,3)
    rhs = -2*dk*(t[0]-t[3])*(t[1]-t[2])
    assert abs(lhs-rhs) <= EPS*(1+abs(lhs)+abs(rhs))

print('Cstar =', CSTAR)
print('3 Cstar =', 3*CSTAR)
print('(9/2) Cstar =', 4.5*CSTAR)
print('sqrt(2 Cstar) =', math.sqrt(2*CSTAR))
print('0.5 sqrt(2 Cstar) =', 0.5*math.sqrt(2*CSTAR))
print('four_point_random_checks = 10000 PASS')
