from fractions import Fraction as F

# Exact normalization check for the block Schur-complement reserve identity.
# This is not a MOC4 witness; the theorem in REPORT.md is analytic.
#
# A = [[B,C],[C^T,D]] with
# B = diag(2,0), C=(1,0)^T, D=2, beta=(u,v)=((4,0),5).
# The pair block is singular and A is PSD with a one-dimensional kernel.

Bplus00 = F(1, 2)
u0 = F(4)
v = F(5)
C0 = F(1)
D = F(2)

R_pair = u0 * Bplus00 * u0
S = D - C0 * Bplus00 * C0
r = v - C0 * Bplus00 * u0
R_cross = r * r / S

# The active full block is [[2,1],[1,2]] with inverse (1/3)[[2,-1],[-1,2]].
R_full = F(2,3)*u0*u0 + 2*F(-1,3)*u0*v + F(2,3)*v*v

assert R_pair == 8
assert S == F(3,2)
assert r == 3
assert R_cross == 6
assert R_full == 14
assert R_full == R_pair + R_cross

# PSD principal minors of the active block.
assert F(2) > 0
assert F(2)*F(2)-F(1)*F(1) == 3 > 0

print('PASS MOC4-MSQR-CROSS-SPLIT-RESERVE-v1 normalization')
print('R_pair =', R_pair)
print('S =', S)
print('r =', r)
print('R_cross =', R_cross)
print('R_full =', R_full)
print('R_full - R_pair - R_cross =', R_full-R_pair-R_cross)
