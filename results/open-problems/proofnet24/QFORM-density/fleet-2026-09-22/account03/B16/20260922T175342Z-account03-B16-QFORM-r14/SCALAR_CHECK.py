from fractions import Fraction
import math

# At S=1/(sqrt(2)m), the D fiber is [-a,a], a=1/(sqrt(2)m).
# For T=X3^2-X4^2 with X3,X4 iid Unif[0,1],
# p_T(t)=1/2 asinh(sqrt((1-t)/t)), hence p_T(d^2)=1/2 acosh(1/d).

def lower_bound(m):
    a = 1.0/(math.sqrt(2.0)*m)
    return 0.5*(math.log(1.0/a)+1.0)

def midpoint_numeric(m, n=500000):
    # midpoint rule avoids the integrable logarithmic singularity at d=0
    a = 1.0/(math.sqrt(2.0)*m)
    total = 0.0
    for j in range(n):
        d = a*(j+0.5)/n
        total += 0.5*math.acosh(1.0/d)
    return total/n

for m in (1,2,10,100):
    val = midpoint_numeric(m, n=10000)
    lb = lower_bound(m)
    assert val >= lb - 1e-4, (m,val,lb)

assert lower_bound(1000) > lower_bound(100)
print('PASS')
print('m=100 lower_bound=', repr(lower_bound(100)))
print('m=1000 lower_bound=', repr(lower_bound(1000)))
print('growth coefficient on log(m)=', 0.5)
