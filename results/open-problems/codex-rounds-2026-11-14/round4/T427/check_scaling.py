#!/usr/bin/env python3
"""Exact rational checks of the localization exponents, not a simulation."""
import os
import sys
import resource
from fractions import Fraction as F

assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 15:
    raise SystemExit("REFUSED: actual niceness must be at least 15")
resource.setrlimit(resource.RLIMIT_CPU, (30, 35))

# Represent n^a log(en)^b by the pair (a,b); multiply by addition.
def add(x, y):
    return tuple(a+b for a, b in zip(x, y))

def scale(x, r):
    return tuple(a*r for a in x)

t = (-F(5,6), F(0))
delta2 = add((F(-1), F(1)), scale(t, -1))
r = scale(delta2, F(1,5))
collar_error = r
potential_error = add(scale(r, -4), delta2)
assert collar_error == potential_error
repair = add(scale(r, F(1,2)), (F(0), F(1)))
assert repair == (-F(1,60), F(11,10))

# Independently solve -b=4b-1/6 and c=1-4c.
b = F(1,6)/5
c = F(1,5)
balanced_repair = (-b/2, c/2+1)
assert balanced_repair == repair

heat_delta = add((F(1), F(0)), scale(t, F(3,2)))
heat_cost = add(scale(heat_delta, F(1,2)), (F(0), F(1,2)))
assert heat_delta == (-F(1,4), F(0))
assert heat_cost == (-F(1,8), F(1,2))
assert heat_cost[0] < repair[0]
assert t[0]/2 < delta2[0]  # sqrt(t) = o(delta^2)
assert t[0]/4 < r[0]       # displacement L = o(r)
prefactor = add(scale(delta2, -1), scale(t, -3))
assert prefactor == (F(8,3), F(-1))
assert 13-F(8,3) > 10
assert 10*(F(1,10)+3*F(1,100))**2 == F(169,1000) < 1

# At t=n^(-2/3), the global heat comparison loses its negative n power.
# That time cannot simply be used to improve the repair exponent.
assert F(5,6) > F(2,3)
assert F(1,2)-F(3,4)*F(2,3) == 0

print(f"niceness={priority}; exact Fraction arithmetic")
for name, value in (("delta^2", delta2), ("r", r),
                    ("repair", repair), ("global heat squared distance", heat_delta),
                    ("global heat cost comparison", heat_cost),
                    ("concentration prefactor", prefactor)):
    print(f"{name}: n^({value[0]}) log(en)^({value[1]})")
print("cyclical-monotonicity reassignment factor: 169/1000 < 1")
print("PASS: independent balances and all strict exponent margins.")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss if sys.platform == "darwin" else rss*1024
assert rss < 1_000_000_000
print(f"Peak resident memory: {rss} bytes")
