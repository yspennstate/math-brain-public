#!/usr/bin/env python3
import math

def simpson(f, a, b, n=200000):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a)+f(b)
    for i in range(1,n):
        s += (4 if i%2 else 2)*f(a+i*h)
    return s*h/3

B0_closed = math.sqrt(math.pi)/(2*math.sqrt(3))*math.erf(math.sqrt(3)) - (1-math.exp(-3))/6
B0_quad = simpson(lambda u:(1-u)*math.exp(-3*u*u), 0.0, 1.0, 20000)
C_col = 12*B0_closed
C_global = 3*math.sqrt(2)
assert abs(B0_closed-B0_quad) < 1e-12
assert C_col < C_global
vals=[]
for a in [0.0,0.05,0.1,0.25,0.5,1.0,2.0]:
    ba=simpson(lambda u:(1-u)*math.exp(-3*u*u-6*a*u),0.0,1.0,20000)
    assert ba <= B0_closed + 1e-12
    vals.append((a,ba))
print("PASS")
print("B0 =",repr(B0_closed))
print("C_col =",repr(C_col))
print("3sqrt2 =",repr(C_global))
print("gap =",repr(C_global-C_col))
for a,v in vals:
    print("B(a=%g) = %.16g"%(a,v))
