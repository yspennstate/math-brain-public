from fractions import Fraction
from math import comb, sqrt
import random

ETA = Fraction(1,64)
GAMMA = 1.19876993884320
M0 = GAMMA*GAMMA
THETA = Fraction(1,4)
C = Fraction(6,5)

# Exact Newton/exterior identities on random positive rational spectra.
rng = random.Random(20260924)
for trial in range(500):
    r = rng.randrange(3,9)
    x = sorted([Fraction(rng.randrange(1,80), rng.randrange(1,50)) for _ in range(r)], reverse=True)
    M = x[0]*x[1]
    T = sum(x[2:], Fraction(0))
    U = sum((x[i]*x[j] for i in range(2,r) for j in range(i+1,r)), Fraction(0))
    R = sum((x[i]*x[j] for i in range(r) for j in range(i+1,r)), Fraction(0)) - M
    V = sum((x[i]*x[j]*x[k] for i in range(r) for j in range(i+1,r) for k in range(j+1,r)), Fraction(0))
    Vtail = sum((x[i]*x[j]*x[k] for i in range(2,r) for j in range(i+1,r) for k in range(j+1,r)), Fraction(0))
    assert R == (x[0]+x[1])*T + U
    assert V == M*T + (x[0]+x[1])*U + Vtail
    assert T <= V/M
    assert U <= V/(x[0]+x[1])
    assert R-x[0]*T <= 2*V/x[0]
    assert x[1]*R <= 2*V

# Partner-constant corollary.
s1_lower = M0*sqrt(float(THETA)/(2*float(ETA)))
fan_relative = 4*float(ETA)**2/(float(THETA)**2*M0**3)
tv_quarter = (sqrt(float(THETA))+float(THETA))/(1+float(THETA))
core_e2 = (Fraction(53,320))*M0
assert s1_lower > 4.0645
assert fan_relative < 0.005266
assert abs(tv_quarter-0.6) < 1e-15
assert core_e2 > 0.238

# Walsh-flat spectral family formulas need only singular values.  Dense fan q=N/16.
for N in (32,64,128,256,1024,4096):
    q = N//16
    x1 = Fraction(N*N)
    xt = C*C/Fraction(N*N)
    M = x1*xt
    E2 = x1*q*xt + comb(q,2)*xt*xt
    E3 = x1*comb(q,2)*xt*xt + comb(q,3)*xt*xt*xt
    dist2 = (q-1)*xt
    assert M == C*C
    assert E3 < ETA
    assert dist2 < Fraction(11,1000)  # stronger than r44 d_*^2 threshold
    assert Fraction(3,N) <= Fraction(1,2)
    assert E3 >= C**4/Fraction(1024)

# Sparse fan q=sqrt(N): E3 -> 0 while E2 -> infinity and rank-two Frobenius tail ->0.
prev_e3 = None
prev_dist2 = None
prev_e2 = None
for N in (64,256,1024,4096):
    q = int(sqrt(N))
    x1 = Fraction(N*N)
    xt = C*C/Fraction(N*N)
    E2 = x1*q*xt + comb(q,2)*xt*xt
    E3 = x1*comb(q,2)*xt*xt + comb(q,3)*xt*xt*xt
    dist2 = (q-1)*xt
    assert E3 < ETA
    if prev_e3 is not None:
        assert E3 < prev_e3
        assert dist2 < prev_dist2
        assert E2 > prev_e2
    prev_e3, prev_dist2, prev_e2 = E3, dist2, E2

print('gamma^2=', M0)
print('theta=1/4 s1 lower=', s1_lower)
print('theta=1/4 fan relative error upper=', fan_relative)
print('theta=1/4 determinant-law TV upper=', tv_quarter)
print('7/8-support E2 core lower=', float(core_e2))
print('pinned-D dense-fan bound=', 6*sqrt(2.718281828459045)*(1024/float(C**4))**(1/6))
print('STATUS=PASS')
