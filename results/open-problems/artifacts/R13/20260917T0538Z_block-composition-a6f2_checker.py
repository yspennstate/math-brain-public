#!/usr/bin/env python3
from fractions import Fraction as F
import math

# R13 exact-arithmetic certificate for the block-composition envelope.
# All comparisons used for acceptance are rational. Pi is bracketed by a
# rational Machin-series certificate rather than floating-point arithmetic.

# Certified squared base bounds retained from prior R13 reports.
BASE2 = {
    4: F(3,1),       # (sqrt 3)^2
    5: F(4,1),       # 2^2
    6: F(9,2),       # (3/sqrt 2)^2
    7: F(21,4),      # (sqrt 21 / 2)^2
    8: F(6,1),       # (sqrt 6)^2
    9: F(27,4),      # (3 sqrt 3 / 2)^2
}

# Previous certified rational entries, newest state before this run.
OLD = {
    10:F(149,50), 11:F(25,8), 12:F(417,125), 13:F(3473,1000), 14:F(3657,1000),
    15:F(1893,500), 16:F(3951,1000), 17:F(4), 18:F(4), 19:F(4141,1000),
    20:F(4249,1000), 21:F(881,200), 22:F(1127,250), 23:F(4653,1000), 24:F(4753,1000),
    25:F(611,125), 26:F(997,200), 27:F(5), 28:F(5), 29:F(1269,250), 30:F(521,100),
    31:F(662,125), 32:F(2711,500), 33:F(2753,500), 34:F(45,8), 35:F(5707,1000),
    36:F(5821,1000), 37:F(2951,500), 38:F(6), 39:F(6), 40:F(6), 41:F(6049,1000),
    42:F(6123,1000), 43:F(6233,1000), 44:F(1261,200), 45:F(6411,1000), 46:F(3241,500),
    47:F(823,125), 48:F(3327,500), 49:F(6753,1000), 50:F(3411,500), 51:F(3459,500),
    52:F(1397,200), 53:F(7), 54:F(7), 55:F(7), 56:F(7073,1000), 57:F(892,125),
    58:F(7231,1000), 59:F(1823,250), 60:F(1477,200), 61:F(3723,500),
}

def ceil_div(n,k):
    return (n+k-1)//k

def block_sq(n):
    vals = {k: BASE2[k]*ceil_div(n,k) for k in BASE2}
    best = min(vals.values())
    winners = tuple(k for k,v in vals.items() if v == best)
    return best, winners

# Strict movement against every previous finite rational entry 10..61.
for n in range(10,62):
    q,w = block_sq(n)
    assert q < OLD[n]*OLD[n], (n,q,OLD[n]*OLD[n],w)

# Count: 52 rational-table entries move.
assert len(OLD) == 52

# Exact first and last finite block values used in the claimed domain.
assert block_sq(10)[0] == 8               # B(10) <= 2 sqrt 2
assert block_sq(61)[0] == F(189,4)
assert block_sq(62)[0] == F(189,4)
assert block_sq(63)[0] == F(189,4)
assert block_sq(72)[0] == 54
assert block_sq(73)[0] == 57

# The block envelope is monotone on the relevant range; the report proves this
# for all n because it is a pointwise minimum of nondecreasing ceiling functions.
last = None
for n in range(10,200):
    q,_ = block_sq(n)
    if last is not None:
        assert last <= q
    last = q

# Exact rational Machin bracket for pi.
def atan_partial(x:F,N:int)->F:
    s=F(0)
    for j in range(N+1):
        term=x**(2*j+1)/F(2*j+1)
        s += term if j%2==0 else -term
    return s

a5_lo=atan_partial(F(1,5),11)
a5_hi=atan_partial(F(1,5),10)
a239_lo=atan_partial(F(1,239),3)
a239_hi=atan_partial(F(1,239),2)
pi_lo=16*a5_lo-4*a239_hi
pi_hi=16*a5_hi-4*a239_lo
assert pi_lo < pi_hi
assert pi_lo > 3
assert pi_hi < F(22,7)

# GFL universal squared constant is 18*pi.
# Every n=62..72 improves it because block_sq <= 54 < 18*pi.
for n in range(62,73):
    q,_ = block_sq(n)
    assert q <= 54
    assert q < 18*pi_lo

# At n=73 the block candidate is already worse than GFL:
# 18*pi < 18*(22/7) = 396/7 < 57 = block_sq(73).
assert 18*pi_hi < 57
assert 18*F(22,7) < 57
assert 18*pi_hi < block_sq(73)[0]

# Since each component k -> BASE2[k] ceil(n/k) is nondecreasing in n,
# their minimum is nondecreasing; therefore n=73 is the permanent crossover.

# Movement count: 10..61 (52) plus 62..72 (11) = 63 entries.
assert (61-10+1) + (72-62+1) == 63

print('R13 block-composition exact checker')
print('base_squared_bounds=', {k:str(v) for k,v in BASE2.items()})
print('B10_squared_new=', block_sq(10)[0], 'winners=', block_sq(10)[1])
print('B61_squared_new=', block_sq(61)[0], 'winners=', block_sq(61)[1])
print('B72_squared_new=', block_sq(72)[0], 'winners=', block_sq(72)[1])
print('B73_squared_block_candidate=', block_sq(73)[0], 'winners=', block_sq(73)[1])
print('pi_lower_minus_3=', pi_lo-F(3,1))
print('22_over_7_minus_pi_upper=', F(22,7)-pi_hi)
print('strictly_improved_entries_10_through_61=', 52)
print('strictly_improved_entries_62_through_72=', 11)
print('total_strictly_improved_entries=', 63)
print('finite_block_domain=10..72')
print('universal_GFL_domain=73..infinity')
print('ALL_EXACT_CHECKS_PASS')
