"""Diagnostic cutoff search, not a proof certificate. Standard library only."""
import math
from audit import guard
guard()
J = 2.6220575542921198
best = None
for i in range(500, 2501):
    t = i/10000
    p = 2*math.erfc(1/math.sqrt(2*t))
    A = math.sqrt(2/(math.pi*t))*J
    for s_units in range(150, 301):
        s = s_units/10
        m = p+A/(math.e*s)
        c = -math.log(3*m)/s
        if best is None or c > best[0]:
            best = (c, t, s, p, A, s*c)
print("best diagnostic (c,t,s,p,A,theta):", best)
for t in (1/18, 1/8, 1/7):
    p = 2*math.erfc(1/math.sqrt(2*t))
    mills = 4*math.sqrt(t/(2*math.pi))*math.exp(-1/(2*t))
    A = math.sqrt(2/(math.pi*t))*J
    print("t,p,mills,A:",t,p,mills,A)
    for s in (19, 19.25, 19.5, 20):
        m = p+A/(math.e*s)
        c = -math.log(3*m)/s
        print("s,m,c,xi_upper_at_tail_boundary:", s, m, c, 1-(2/33)*c/math.log(3))
