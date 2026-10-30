from fractions import Fraction
import math
import numpy as np

E0 = Fraction(11907, 16384)
M0SQ = Fraction(226233, 33554432)
S0 = Fraction(93, 10240) * E0
EPS = Fraction(1, 2**24)
B_RATIO = Fraction(1,1024) / M0SQ
ETA = Fraction(1,3) - B_RATIO
TAIL = 2*EPS/S0
TAIL_REL = 2*EPS/(S0*S0)
V2 = ETA - TAIL_REL
C_E2 = 3 * 2**(7/6) * math.exp(1/3)
PAID = C_E2 * float(M0SQ*EPS)**(-1/6)

print('E0', float(E0))
print('M0SQ', float(M0SQ))
print('S0', float(S0))
print('ETA', float(ETA), ETA)
print('TAIL', float(TAIL), TAIL)
print('TAIL_REL', float(TAIL_REL), TAIL_REL)
print('V2', float(V2), V2)
print('V_AMP', math.sqrt(float(V2)))
print('C_E2', C_E2)
print('PAID_BOUND', PAID)
assert PAID < 347
assert V2 > Fraction(1857,10000)
assert TAIL_REL < Fraction(274,100000)

rng = np.random.default_rng(20260923)
max_anchor_rel = 0.0
max_wedge_rel = 0.0
for _ in range(1000):
    p = int(rng.integers(2, 8))
    q = int(rng.integers(2, 8))
    N = rng.normal(size=(p,q))
    m = N[0,:].copy()
    M2 = float(m @ m)
    if M2 < 1e-12:
        continue
    Y = N[1:,:]
    C = Y - ((Y @ m)/M2)[:,None] * m[None,:]
    b = N[0,0]
    r = N[0,1:]
    c = N[1:,0]
    D = N[1:,1:]
    F = b*D - c[:,None]*r[None,:]
    lhs = float(np.sum(F*F))
    rhs = float(b*b*np.sum(C*C) + M2*np.sum(C[:,0]**2))
    max_anchor_rel = max(max_anchor_rel, abs(lhs-rhs)/max(1.0,abs(lhs),abs(rhs)))

    wedge = 0.0
    for j in range(1,p):
        for u in range(q):
            for v in range(u+1,q):
                d = N[0,u]*N[j,v] - N[0,v]*N[j,u]
                wedge += d*d
    wedge_rhs = M2*float(np.sum(C*C))
    max_wedge_rel = max(max_wedge_rel, abs(wedge-wedge_rhs)/max(1.0,abs(wedge),abs(wedge_rhs)))

print('MAX_ANCHOR_IDENTITY_RELERR', max_anchor_rel)
print('MAX_WEDGE_IDENTITY_RELERR', max_wedge_rel)
assert max_anchor_rel < 1e-12
assert max_wedge_rel < 1e-12
print('QFORM_B06_R41_RECIPROCAL_ANCHOR_CHECK_PASS')
