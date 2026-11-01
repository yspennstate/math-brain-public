#!/usr/bin/env python3
import math

C_SL = math.sqrt(6.0*math.pi)*math.erf(math.sqrt(1.5))
C_DIFF = 3.0*math.sqrt(2.0)
assert C_SL < C_DIFF

def cap_bound(M):
    # Simpson integration, deterministic and amply accurate for the scalar check.
    a = 1.0/(2.0*M)
    n = 200000
    h = a/n
    s = 1.0 + math.exp(-6.0*a*a)
    for j in range(1,n):
        x = j*h
        s += (4.0 if j & 1 else 2.0)*math.exp(-6.0*x*x)
    integ = h*s/3.0
    return 12.0*M*integ

lo, hi = 1.0, 1.3
for _ in range(70):
    mid = (lo+hi)/2.0
    if cap_bound(mid) < C_DIFF:
        lo = mid
    else:
        hi = mid
MSTAR = (lo+hi)/2.0
assert abs(C_SL - 3.9801056750420088) < 2e-15
assert abs((C_DIFF-C_SL) - 0.2625350120772763) < 2e-15
assert abs(MSTAR - 1.1079013713103110) < 2e-12
assert cap_bound(1.0) < C_DIFF < cap_bound(1.2)

print('C_SL = %.17g' % C_SL)
print('3sqrt2 = %.17g' % C_DIFF)
print('gap = %.17g' % (C_DIFF-C_SL))
print('ratio = %.17g' % (C_SL/C_DIFF))
print('M_star = %.17g' % MSTAR)
print('PASS')
