#!/usr/bin/env python3
from itertools import product
from math import gcd

# Exact finite certificate for the renewal representation in the P05 report.
# G~Geom(1/2) on {1,2,...}; G^M=min(G,M).
# For M=6, probabilities have common denominator D=2^(M-1)=32:
# P(G^M=k)=2^{-k} for k<M and P(G^M=M)=2^{-(M-1)}.
R = 4
M = 6
D = 1 << (M - 1)


def weight(k: int) -> int:
    if 1 <= k < M:
        return 1 << (M - 1 - k)
    if k == M:
        return 1
    raise ValueError(k)


def make_bits(runs):
    out = []
    bit = 0
    for length in runs:
        out.extend([bit] * length)
        bit ^= 1
    return out


def masks(bits):
    z = o = 0
    for j, bit in enumerate(bits):
        if bit == 0:
            z |= 1 << j
        else:
            o |= 1 << j
    return z, o


def lcs_with_masks(a, zmask, omask):
    # Exact bitset LCS recurrence; Python integers are arbitrary precision.
    state = 0
    for bit in a:
        match = zmask if bit == 0 else omask
        x = match | state
        y = (state << 1) | 1
        state = x & ~(x - y)
    return state.bit_count()


states = []
for runs in product(range(1, M + 1), repeat=R):
    w = 1
    for k in runs:
        w *= weight(k)
    bits = make_bits(runs)
    zmask, omask = masks(bits)
    states.append((bits, w, zmask, omask))

numerator = 0
for a, wa, _, _ in states:
    for _, wb, zmask, omask in states:
        numerator += wa * wb * lcs_with_masks(a, zmask, omask)

denominator = D ** (2 * R)
g = gcd(numerator, denominator)
b_num, b_den = numerator // g, denominator // g
rho_num, rho_den = b_num, b_den * (2 * R)
g2 = gcd(rho_num, rho_den)
rho_num //= g2
rho_den //= g2

# Exact theorem-side tail allowance: 0 <= rho_R-rho_{R,M} <= 2^{-(M-1)}.
tail_num, tail_den = 1, 1 << (M - 1)
upper_num = rho_num * tail_den + tail_num * rho_den
upper_den = rho_den * tail_den
g3 = gcd(upper_num, upper_den)
upper_num //= g3
upper_den //= g3

print(f"R={R} M={M} states_per_string={len(states)}")
print(f"raw_weight_denominator={D}^{2*R}={denominator}")
print(f"b_RM={b_num}/{b_den}")
print(f"rho_RM={rho_num}/{rho_den}")
print(f"rho_RM_decimal={rho_num/rho_den:.18f}")
print(f"tail_allowance={tail_num}/{tail_den}")
print(f"rho_R_upper_from_cap={upper_num}/{upper_den}")
print(f"rho_R_upper_decimal={upper_num/upper_den:.18f}")

assert (b_num, b_den) == (1472414081, 268435456)
assert (rho_num, rho_den) == (1472414081, 2147483648)
assert (upper_num, upper_den) == (1539522945, 2147483648)
print("EXACT_CAPPED_RUN_CERTIFICATE_PASS")
