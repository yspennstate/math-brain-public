#!/usr/bin/env python3
"""Exact-arithmetic certificate for the I0130 optimized Du--Sun adversary.

This checks only the finite/rational arithmetic used by the theorem-sized
argument in the accompanying report. The universal adversarial proof itself
is written out in the report.
"""
from fractions import Fraction as Q

# Current literature lower bound (Neoh--Teh v2) and Du--Sun v1 upper bound.
L_CURRENT = Q(19, 30)
U_DUSUN = Q(33151, 33152)
W_BEFORE = U_DUSUN - L_CURRENT

# Optimized member of the generalized Du--Sun three-phase adversary.
N = 127
r = Q(4, N + 2)
gamma = Q(1, 16) - r
M = 2 * N + 8

assert r == Q(4, 129)
assert gamma == Q(65, 2064)
assert M == 262

# After N completed blocks, total safety <= 4-Nr = 2r,
# hence one of the two agents has safety <= r.
assert Q(4) - N * r == 2 * r
assert Q(4) - (N - 1) * r > 2 * r

# Five-item terminal trap. Values to L double and stay within exact MIV 1.
trap = [Q(2**j) * (r + gamma) for j in range(5)]
assert trap == [Q(1,16), Q(1,8), Q(1,4), Q(1,2), Q(1)]

# If L has received all earlier trap goods, missing the next one puts
# L's safety at exactly -gamma at the worst allowed starting safety r.
sL = r
trap_rows = []
for j, a in enumerate(trap[:4], start=1):
    trap_rows.append((j, sL, a, sL-a))
    assert sL - a == -gamma
    sL += a
assert sL == r + Q(15,16)
assert sL - trap[4] == -gamma
assert Q(1) >= gamma > 0

# Resulting universal upper bound: a failed safety <= -gamma in an instance
# of at most M goods of per-item value <=1 yields ratio <= 1-gamma/M.
gap = gamma / M
U_NEW = Q(1) - gap
W_AFTER = U_NEW - L_CURRENT
assert gap == Q(65, 540768)
assert U_NEW == Q(540703, 540768)
assert W_AFTER == Q(330361, 901280)
assert U_NEW < U_DUSUN
assert W_AFTER < W_BEFORE

# Exact improvement over the Du--Sun upper endpoint.
improvement = U_DUSUN - U_NEW
assert improvement == Q(50441, 560235648)

# Optimize the whole one-parameter family:
# r_N=4/(N+2), gamma_N=1/16-r_N, M_N=2N+8,
# g_N=gamma_N/M_N=(N-62)/(32(N+2)(N+4)).
def family_gap(k: int) -> Q:
    return Q(k - 62, 32 * (k + 2) * (k + 4))

def diff_sign_poly(k: int) -> int:
    # Sign of g_{k+1}-g_k.
    return -k*k + 123*k + 442

assert diff_sign_poly(126) == 64
assert diff_sign_poly(127) == -66
# q(k+1)-q(k)=122-2k<0 for every k>=62, so this single crossing
# proves N=127 is the unique integer maximizer for N>=63.
for k in range(63, 127):
    assert family_gap(k+1) > family_gap(k)
for k in range(127, 5000):  # arithmetic sanity check; proof is symbolic above
    assert family_gap(k+1) < family_gap(k)
assert family_gap(127) == gap

print("L_CURRENT", L_CURRENT, float(L_CURRENT))
print("U_DUSUN", U_DUSUN, float(U_DUSUN))
print("W_BEFORE", W_BEFORE, float(W_BEFORE))
print("N", N)
print("r", r, float(r))
print("gamma", gamma, float(gamma))
print("M", M)
print("trap_values", ",".join(map(str, trap)))
for row in trap_rows:
    print("trap_step", *map(str, row))
print("gap", gap, float(gap))
print("U_NEW", U_NEW, float(U_NEW))
print("W_AFTER", W_AFTER, float(W_AFTER))
print("U_IMPROVEMENT", improvement, float(improvement))
print("q126", diff_sign_poly(126), "q127", diff_sign_poly(127))
print("I0130_OPTIMIZED_ADVERSARY_PASS")
