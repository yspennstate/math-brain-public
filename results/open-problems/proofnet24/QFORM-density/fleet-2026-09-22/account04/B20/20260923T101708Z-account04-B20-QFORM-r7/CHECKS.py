#!/usr/bin/env python3
import math
import numpy as np

def active(a,d,sigma,tau):
    return np.array([[a,0.0,0.0],[0.0,0.0,d*sigma*tau],[0.0,d*sigma*tau,0.0]])

cases=[
    (1.0,1.0,1.0,1.0),
    (-2.0,3.0,0.5,1.0),
    (4.0,-2.0,2.0,0.25),
]
for a,d,s,t in cases:
    got=np.linalg.eigvalsh(active(a,d,s,t))
    want=np.sort(np.array([a,d*s*t,-d*s*t]))
    assert np.allclose(got,want), (got,want)

C=4.0*math.sqrt(math.e)
C_sharp=4.0*math.sqrt(2.0)
assert 6.5948 < C < 6.5949
assert 5.6568 < C_sharp < 5.6569

# Weighted-section substitution:
# L=sqrt(e)/sigma, K=sqrt(e)/tau.
for a,d,s,t in cases:
    L=math.sqrt(math.e)/s
    K=math.sqrt(math.e)/t
    lhs=4.0*math.sqrt(L*K)/math.sqrt(abs(a*d))
    rhs=4.0*math.sqrt(math.e)/math.sqrt(abs(a*d)*s*t)
    assert abs(lhs-rhs)<1e-12

print("all checks passed")
print("4sqrt(e) =",repr(C))
print("4sqrt(2) =",repr(C_sharp))
print("normalized spectrum =",np.linalg.eigvalsh(active(1,1,1,1)).tolist())
