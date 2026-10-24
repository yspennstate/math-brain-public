#!/usr/bin/env python3
"""Exact certificate for P0169 degree-5 12/13-active boundary reductions.

No floating point arithmetic.  This enumerates all integer Newton layer profiles
for a 12-variable degree<=5 Boolean symmetrization at signed singleton mass 9/4,
under the necessary layer-count constraints 0 <= b_k <= C(12,k).
It does NOT claim that either surviving layer profile is realized by a Boolean
truth table.  It also checks the exact common-bias polynomials and the arithmetic
used in the 13-active-coordinate saturation exclusion.
"""
from fractions import Fraction
from math import comb

N = 12
TARGET16 = 36  # 16 * (9/4)


def b_from_u(u, k):
    return sum(u[j] * comb(N-j, k-j) for j in range(6) if j <= k)


def objective16(u):
    # 16 L = -16u1 -16u2 -12u3 -8u4 -5u5
    return -16*u[1] - 16*u[2] - 12*u[3] - 8*u[4] - 5*u[5]


def krawtchouk(n, j, k):
    return sum(((-1)**r) * comb(k, r) * comb(n-k, j-r)
               for r in range(j+1)
               if r <= k and j-r <= n-k)


def level_sums(profile):
    # A_j = sum_{|S|=j} fhat(S)
    out = []
    for j in range(6):
        num = 0
        for k, bk in enumerate(profile):
            layer_f_sum = 2*bk - comb(N, k)
            num += layer_f_sum * krawtchouk(N, j, k)
        out.append(Fraction(num, 2**N))
    return tuple(out)

# Sparse-dual deficiency equation at L=9/4.
# Max dual value is 331/144, so deficiency 7/144 gives
# 65*A + 8*B + 3*C = 70, where
# A=(1-b0)+b12, B=(220-b3)+b9, C=(495-b4)+b8.
deficiency_solutions = []
for A in range(3):
    for B in range(71):
        for C in range(71):
            if 65*A + 8*B + 3*C == 70:
                deficiency_solutions.append((A, B, C))
assert deficiency_solutions == [(0,2,18),(0,5,10),(0,8,2)]

# Exhaustive exact Newton enumeration.
# b0=1 and b12=0 follow from A=0.  Use u1,u2,u3 as free integers.
# Their complete ranges follow successively from 0<=b1<=12,
# 0<=b2<=66, 0<=b3<=220.  Then b12=0 and L=9/4 solve u4,u5.
profiles = []
u0 = 1
for u1 in range(-12, 1):
    b1 = 12 + u1
    assert 0 <= b1 <= 12
    u2_lo = -66 - 11*u1
    u2_hi = -11*u1
    for u2 in range(u2_lo, u2_hi + 1):
        b2 = 66 + 11*u1 + u2
        assert 0 <= b2 <= 66
        u3_lo = -220 - 55*u1 - 10*u2
        u3_hi = -55*u1 - 10*u2
        for u3 in range(u3_lo, u3_hi + 1):
            b3 = 220 + 55*u1 + 10*u2 + u3
            assert 0 <= b3 <= 220
            # Let S=u4+u5=-(u0+u1+u2+u3) from b12=0.
            S = -(u0 + u1 + u2 + u3)
            # -16u1-16u2-12u3-3u4-5S = 36.
            numer = -(TARGET16 + 16*u1 + 16*u2 + 12*u3 + 5*S)
            if numer % 3:
                continue
            u4 = numer // 3
            u5 = S - u4
            u = (u0,u1,u2,u3,u4,u5)
            if objective16(u) != TARGET16:
                continue
            bs = tuple(b_from_u(u,k) for k in range(N+1))
            if bs[12] != 0:
                continue
            if all(0 <= bs[k] <= comb(N,k) for k in range(N+1)):
                profiles.append((u,bs))

expected = [
    ((1,-4,31,-94,110,-44),
     (1,8,53,216,494,644,462,148,1,4,13,4,0)),
    ((1,-3,24,-76,90,-36),
     (1,9,57,219,486,630,462,162,9,1,9,3,0)),
]
assert profiles == expected

fourier = [level_sums(bs) for _,bs in profiles]
assert fourier == [
    (Fraction(0), Fraction(9,4), Fraction(0), Fraction(-4), Fraction(0), Fraction(11,4)),
    (Fraction(0), Fraction(9,4), Fraction(0), Fraction(-7,2), Fraction(0), Fraction(9,4)),
]

# Both layer profiles are antipodally complementary in aggregate.
for _,bs in profiles:
    assert all(bs[N-k] == comb(N,k) - bs[k] for k in range(N+1))

# Difference of the two common-bias polynomials has nonzero degree-5 coefficient.
assert fourier[0][5] - fourier[1][5] == Fraction(1,2)

# 13-active arithmetic.  Scale singleton coefficients by 16.
# Any 12-coordinate restriction has signed mass <=36/16, hence
# S-s_j<=36 for every j.  Summation gives S<=39.
assert (13*36)//12 == 39
# At S=39 all s_j>=3 and sum=39, hence all are 3.
assert 13*3 == 39
# At S=38, all s_j>=2 and at least one equals 2 (else sum>=39).
assert 13*3 > 38 and 13*2 <= 38
# If a coordinate attains s_j=S-36, both half-cube restrictions saturate 36/16.
# The written proof shows their profile types must match (otherwise their
# difference has degree 5, contradicting that a coordinate difference has degree<=4).
# Matching types make the global common-bias derivative 36/16, contradicting S/16
# for S=38 or39.
assert Fraction(36,16) != Fraction(38,16)
assert Fraction(36,16) != Fraction(39,16)

print("P0169 degree-5 exact boundary-profile certificate")
print("arithmetic=integer/Fraction; floating_point=False")
print("deficiency_solutions", deficiency_solutions)
print("profile_count", len(profiles))
for idx,(u,bs) in enumerate(profiles, start=1):
    print("profile", idx, "u", list(u))
    print("profile", idx, "b", list(bs))
    print("profile", idx, "level_fourier_sums_A0_to_A5", [str(x) for x in fourier[idx-1]])
    print("profile", idx, "antipodal_layer_complementarity", True)
print("bias_polynomial_1", "(9/4)t - 4 t^3 + (11/4)t^5")
print("bias_polynomial_2", "(9/4)t - (7/2)t^3 + (9/4)t^5")
print("bias_degree5_difference", str(fourier[0][5]-fourier[1][5]))
print("thirteen_active_generic_scaled_upper", 39)
print("thirteen_active_values_excluded_by_saturation", [38,39])
print("thirteen_active_remaining_possible_violation_scaled_values", [36,37])
print("REALIZABILITY_OF_THE_TWO_12_LAYER_PROFILES_NOT_ASSERTED")
print("ASSERTIONS_PASS")
