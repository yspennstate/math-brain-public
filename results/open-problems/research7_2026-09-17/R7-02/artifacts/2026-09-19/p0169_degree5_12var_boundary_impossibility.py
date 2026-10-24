#!/usr/bin/env python3
"""Exact finite certificate for the R7-02 P0169 twelve-variable d=5 boundary.

The preceding R7-02 work proves that any 12-variable boundary object with
signed singleton mass 9/4 is balanced and, after orienting coordinates, has
all 12 singleton coefficients equal to 3/16.  For each coordinate its two
11-variable restrictions therefore have means +3/16 and -3/16 and average
signed singleton mass 33/16.  The known exact 11-variable bound is 34/16,
and equality 34/16 forces mean zero.  Hence both restrictions would have to
have signed singleton mass exactly 33/16.

This script exhausts every integer Newton/Hamming-layer profile that could
come from an 11-variable Boolean function of real Fourier degree <=5 with
mean +/-3/16 and signed singleton mass 33/16.  There are none.

All arithmetic is integer/Fraction.  This checks a necessary symmetrized
condition; zero surviving necessary profiles proves nonexistence of the
actual restriction, hence rules out the 12-variable 9/4 boundary object.
"""
from fractions import Fraction
from math import comb

N = 11
TARGET_L = Fraction(33, 16)
TARGET_MEANS = (Fraction(3, 16), Fraction(-3, 16))


def b_from_u(u, k):
    return sum(u[j] * comb(N-j, k-j) for j in range(6) if j <= k)


def singleton_sum(u):
    return (-Fraction(u[1]) - Fraction(u[2])
            - Fraction(3,4)*u[3] - Fraction(1,2)*u[4]
            - Fraction(5,16)*u[5])


def mean(u):
    # sum_k b_k = sum_j u_j 2^(N-j), and mean = 2 B / 2^N - 1.
    return sum(Fraction(u[j], 2**j) for j in range(6)) - 1


def enumerate_profiles(target_mean):
    out = []
    target16 = int(16 * TARGET_L)  # 33
    rhs_mean32 = 32 * (target_mean + 1)
    assert rhs_mean32.denominator == 1
    rhs_mean32 = int(rhs_mean32)

    # Triangular Newton system.  Loop over the first four actual layer counts
    # b_0,b_1,b_2,b_3; the two exact linear constraints (mean,L) then uniquely
    # determine u_4,u_5.  This is exhaustive for all integer layer profiles.
    for u0 in (0, 1):
        for b1 in range(comb(N,1) + 1):
            u1 = b1 - comb(N,1)*u0
            for b2 in range(comb(N,2) + 1):
                u2 = b2 - comb(N,2)*u0 - comb(N-1,1)*u1
                for b3 in range(comb(N,3) + 1):
                    u3 = (b3 - comb(N,3)*u0
                          - comb(N-1,2)*u1 - comb(N-2,1)*u2)

                    # Mean equation:
                    # 32u0+16u1+8u2+4u3+2u4+u5 = 32(1+mean).
                    mrem = rhs_mean32 - (32*u0 + 16*u1 + 8*u2 + 4*u3)

                    # L equation in sixteenths:
                    # -16u1-16u2-12u3-8u4-5u5 = 33.
                    lrem = target16 + 16*u1 + 16*u2 + 12*u3
                    # Substitute u5=mrem-2u4:
                    # 2u4 - 5*mrem = lrem.
                    num = lrem + 5*mrem
                    if num % 2:
                        continue
                    u4 = num // 2
                    u5 = mrem - 2*u4
                    u = (u0,u1,u2,u3,u4,u5)

                    if singleton_sum(u) != TARGET_L or mean(u) != target_mean:
                        continue
                    bs = tuple(b_from_u(u,k) for k in range(N+1))
                    if all(0 <= bs[k] <= comb(N,k) for k in range(N+1)):
                        out.append((u,bs))
    return out


print('P0169 d=5 twelve-variable boundary impossibility certificate')
print('arithmetic=integer/Fraction; floating_point=False')
print('target_restriction_singleton_sum', TARGET_L)
for mu in TARGET_MEANS:
    prof = enumerate_profiles(mu)
    print('target_mean', mu, 'surviving_necessary_profiles', len(prof))
    assert prof == []

# Arithmetic used in the written lifting argument.
assert Fraction(9,4) - Fraction(3,16) == Fraction(33,16)
assert Fraction(17,8) == Fraction(34,16)
assert Fraction(35,16) * Fraction(35,16) < 5
assert Fraction(36,16) * Fraction(36,16) > 5
print('no_11var_profile_at_mean_plus_or_minus_3_over_16_and_L_33_over_16', True)
print('therefore_12var_L_9_over_4_boundary_impossible', True)
print('improved_12var_bound', Fraction(35,16))
print('ASSERTIONS_PASS')
