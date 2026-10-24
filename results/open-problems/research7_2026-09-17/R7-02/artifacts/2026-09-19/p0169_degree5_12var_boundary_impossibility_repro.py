#!/usr/bin/env python3
"""Reproducible exact certificate for P0169 12-variable d=5 boundary.

This is the same exhaustive Newton/Hamming-layer calculation as
p0169_degree5_12var_boundary_impossibility.py, with one extra counter so the
archived output records the number of triangular prefixes actually tested.
All arithmetic is integer/Fraction; no floating point is used.
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
    return sum(Fraction(u[j], 2**j) for j in range(6)) - 1


def enumerate_profiles(target_mean):
    out = []
    prefixes = 0
    target16 = int(16 * TARGET_L)
    rhs_mean32 = 32 * (target_mean + 1)
    assert rhs_mean32.denominator == 1
    rhs_mean32 = int(rhs_mean32)
    for u0 in (0, 1):
        for b1 in range(comb(N,1) + 1):
            u1 = b1 - comb(N,1)*u0
            for b2 in range(comb(N,2) + 1):
                u2 = b2 - comb(N,2)*u0 - comb(N-1,1)*u1
                for b3 in range(comb(N,3) + 1):
                    prefixes += 1
                    u3 = (b3 - comb(N,3)*u0
                          - comb(N-1,2)*u1 - comb(N-2,1)*u2)
                    mrem = rhs_mean32 - (32*u0 + 16*u1 + 8*u2 + 4*u3)
                    lrem = target16 + 16*u1 + 16*u2 + 12*u3
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
    return out, prefixes


print('P0169 d=5 twelve-variable boundary impossibility certificate')
print('arithmetic=integer/Fraction; floating_point=False')
print('target_restriction_singleton_sum', TARGET_L)
for mu in TARGET_MEANS:
    prof, prefixes = enumerate_profiles(mu)
    print('target_mean', mu, 'triangular_prefixes_checked', prefixes,
          'surviving_necessary_profiles', len(prof))
    assert prefixes == 223104
    assert prof == []
assert Fraction(9,4) - Fraction(3,16) == Fraction(33,16)
assert Fraction(17,8) == Fraction(34,16)
assert Fraction(35,16) * Fraction(35,16) < 5
assert Fraction(36,16) * Fraction(36,16) > 5
print('no_11var_profile_at_mean_plus_or_minus_3_over_16_and_L_33_over_16', True)
print('therefore_12var_L_9_over_4_boundary_impossible', True)
print('improved_12var_bound', Fraction(35,16))
print('ASSERTIONS_PASS')
