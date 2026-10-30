#!/usr/bin/env python3
"""Standard-library falsification checker for fleet04/B15 logarithmic all-shift tariff."""
import math


def shell_c(m, r):
    p = 2.0 ** (1 - m)
    return (2.0 * math.sqrt(p * (1.0-p))) ** r - 4.0 * (1.0-p) ** (m-r/2.0) * p ** (r/2.0)


def brute_error(m):
    p = 2.0 ** (1-m)
    n = 1 << m
    amp = []
    for T in range(n):
        r = T.bit_count()
        q = p**r * (1.0-p)**(m-r)
        amp.append((1.0 if T == 0 else -1.0) * math.sqrt(q))
    err = 0.0
    for U in range(1, n):
        c = sum(amp[T] * amp[T ^ U] for T in range(n))
        err = max(err, abs(c - shell_c(m, U.bit_count())))
    return err


def quantities(m):
    p = 2.0 ** (1-m)
    I = m*p
    e0 = (1.0-p)**2
    e1 = p*p
    H = -e0*math.log2(e0) - ((1 << m)-1)*e1*math.log2(e1)
    h2 = -p*math.log2(p) - (1.0-p)*math.log2(1.0-p)
    K = m*h2-H
    L = 0.0
    B = 0.0
    for r in range(1, m+1):
        c = shell_c(m, r)
        q = c*c
        mult = math.comb(m, r)
        B += mult*q
        if q:
            L += mult*q*math.log2(1.0/q)
    return p, I, H, K, B, L


print("brute shell verification")
maxerr = 0.0
for m in range(2, 8):
    e = brute_error(m)
    maxerr = max(maxerr, e)
    print(f"m={m:2d} max_abs_error={e:.3e}")
assert maxerr < 5e-15

print("\nasymptotic diagnostics")
print("m  I                 H/I             K/I              B/I             L/(4I)          (L/4-K)/I")
for m in (4,6,8,12,16,24,32):
    p,I,H,K,B,L = quantities(m)
    print(f"{m:2d} {I:.15e} {H/I: .12f} {K/I: .12f} {B/I: .12f} {L/(4*I): .12f} {(L/4-K)/I: .12f}")

offset = 2.0 - 1.0/math.log(2.0)
print(f"\ncritical_offset_limit={offset:.15f}")
_,I,_,K,_,L = quantities(32)
assert abs(L/(4*I) - 29.0) < 1e-4
assert 0.50 < (L/4-K)/I < offset
assert K >= L/4 - I

print("PASS")
