from fractions import Fraction
import math

# Deterministic exact algebra check for the rank-one pair identities.
lam = Fraction(7, 3)
u1, u2 = Fraction(3, 5), Fraction(4, 5)
a = lam * u1 * u1
b = lam * u1 * u2
c = lam * u2 * u2
assert a * c - b * b == 0

p = [Fraction(1,5), Fraction(-7,10), Fraction(11,10), Fraction(2,5)]
q = [Fraction(1,2), Fraction(3,10), Fraction(-1,5), Fraction(17,10)]
d = [Fraction(1,10), Fraction(-2,5), Fraction(2,1), Fraction(7,10)]

w = [qk - (b/a) * pk for pk, qk in zip(p, q)]
eta2 = sum((-u2*pk + u1*qk)**2 for pk, qk in zip(p, q))
lhs_sq = a*a * sum(x*x for x in w)
rhs_sq = a*lam*eta2
assert lhs_sq == rhs_sq

# Exact 3x3 determinant mass identity M_I = |lambda| eta^2.
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

dets = []
for pk, qk, dk in zip(p, q, d):
    T = [[a,b,pk],[b,c,qk],[pk,qk,dk]]
    dets.append(det3(T))
M = lam * eta2
assert sum(abs(x) for x in dets) == M

C_raw = 2**(11/4)
C_invariant = C_raw * 2**(1/4)
C_peer = 18 * 2**(1/3)
crossover_eta_over_lambda = (C_peer / C_invariant)**6
assert abs(C_invariant - 8.0) < 1e-12
assert abs(crossover_eta_over_lambda - 518.9853515625) < 1e-9

print('rank-one pair determinant identity: PASS')
print('pair determinant:', float(a*c-b*b))
print('M_I:', float(M))
print('sum_abs_triple_determinants:', float(sum(abs(x) for x in dets)))
print('raw_original-pivot_constant:', C_raw)
print('invariant_constant:', C_invariant)
print('peer_constant:', C_peer)
print('new_bound_beats_peer_when_eta_over_abs_lambda_le:', crossover_eta_over_lambda)
print('QFORM_B13_R15_CHECK_PASS')
