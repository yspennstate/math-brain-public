#!/usr/bin/env python3
import math
from fractions import Fraction

R_RECORD = 6.521845710923046575

def h(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q*math.log2(q) - (1-q)*math.log2(1-q)

def j(q):
    t = 0.5 + math.sqrt(q*(1-q))
    return 1.0 - h(t)

def kappa(q):
    return (h(q)+j(q))/q

def beta(q):
    return h(q)/q

def solve_tau(r):
    lo, hi = 1e-12, 0.499999999999
    for _ in range(200):
        mid=(lo+hi)/2
        if kappa(mid) > r:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

tau=solve_tau(R_RECORD)
theta=tau/(1-tau)
a=math.sqrt(theta)
r2=kappa(0.2)
print(f"record_r={R_RECORD:.18f}")
print(f"tau(record)={tau:.18f}")
print(f"theta(record)={theta:.18f}")
print(f"sqrt_theta(record)={a:.18f}")
print(f"r2=kappa(1/5)={r2:.18f}")
print(f"beta(tau)={beta(tau):.18f}")
assert R_RECORD > r2
assert a < 0.5
for d in [1,2,5,10,15,32]:
    boolean_lower=Fraction(1,2**(d-1))
    m2_endpoint_upper=Fraction(1,2**d)
    threshold=2**(-1+1/d)
    assert m2_endpoint_upper < boolean_lower
    print(f"d={d:2d}: top_boolean_min={float(boolean_lower):.12g}, m2_endpoint_max={float(m2_endpoint_upper):.12g}, amplitude_threshold={threshold:.12g}")
print("exact_endpoint_contradiction_check=PASS")
