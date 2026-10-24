#!/usr/bin/env python3
"""Exact finite-core checker for PROB10-09 vertical-subgroup spectral-budget iteration.

Load-bearing radical inequalities are reduced to integer/rational square comparisons.
The Decimal beta grid is only a consistency cross-check, not the proof.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 80

# Frozen graph: genus-5 surface quotient, kernel F_3 x F_3 with standard product marking.
g = 5
s = 3
D0 = 4*g
m = 4*s
D = D0 + m
B = 4*g - 3
q = D - 1

# New norm budget: r_Q <= 4 sqrt(g), r_V = 4 sqrt(2s-1).
# Here both radicals are sqrt(5), so a_new = 8 sqrt(5).
# beta_D(a_new) = (8 sqrt(5) + sqrt(320-124))/2 = 7+4 sqrt(5).
assert D == 32 and q == 31 and B == 17
assert 8*8*5 - 4*q == 196
assert 14*14 == 196
# beta < 17 iff 7+4 sqrt(5)<17 iff 4 sqrt(5)<10.
beta_lt_B_square_margin = 10**2 - 4**2*5
assert beta_lt_B_square_margin == 20 and beta_lt_B_square_margin > 0

# p_u - p_c >= 1/(7+4 sqrt5)-1/17 = (68 sqrt5 -150)/527.
# Show this is >1/260: 17680 sqrt5 >39527.
gap_gt_1_260_square_margin = 17680**2*5 - 39527**2
assert gap_gt_1_260_square_margin == 528271 and gap_gt_1_260_square_margin > 0

# Previous cardinality theorem had m < M_5=(77-17 sqrt5)/4.
# m=12 lies outside: 12>M_5 iff 17 sqrt5>29.
m_gt_M5_square_margin = 17**2*5 - 29**2
assert m_gt_M5_square_margin == 604 and m_gt_M5_square_margin > 0

# Equivalent direct failure of the old +m spectral condition:
# beta_32(12+4sqrt5)<17 would require a_old<17+31/17=320/17.
# But 12+4sqrt5 > 320/17 iff 68 sqrt5 >116 iff sqrt5>29/17.
old_plus_m_failure_square_margin = 17**2*5 - 29**2
assert old_plus_m_failure_square_margin > 0

# Quotient-Cheeger stress test does not cross the new uniqueness floor.
# The crude spectral Cheeger bound gives p_c <= 1/(21-4sqrt5), while
# p_u >= 1/(7+4sqrt5).  The former is larger since
# 21-4sqrt5 < 7+4sqrt5 iff 14<8sqrt5, certified by 14^2<64*5.
cheeger_failure_square_margin = 8**2*5 - 14**2
assert cheeger_failure_square_margin == 124 and cheeger_failure_square_margin > 0


def new_surface_product_kernel_exact(g: int, s: int) -> bool:
    """Exact predicate for beta_{4g+4s}(4sqrt(g)+4sqrt(2s-1)) < 4g-3.

    If B=4g-3 and q=4g+4s-1 with B^2>q, beta<B is equivalent to
      sqrt(g)+sqrt(2s-1) < C=(4g^2-5g+s+2)/B.
    Squaring once reduces this to R=C^2-g-(2s-1)>0 and R^2>4g(2s-1).
    """
    B = 4*g - 3
    q = 4*g + 4*s - 1
    if B*B <= q:
        return False
    C = Fraction(4*g*g - 5*g + s + 2, B)
    h = 2*s - 1
    R = C*C - g - h
    return R > 0 and R*R > 4*g*h


def old_cardinality_exact(g: int, s: int) -> bool:
    """Exact predicate 4s < M_g from the preceding +m theorem."""
    B = 4*g - 3
    T = 4*g*g - 5*g + 2 - 4*s*(g-1)
    return T > 0 and T*T > B*B*g

# Frozen new example succeeds and the predecessor criterion fails.
assert new_surface_product_kernel_exact(5,3)
assert not old_cardinality_exact(5,3)

# Broad exact scope scan; count cases where the new theorem strictly extends the old theorem.
grid_cases = 0
new_successes = 0
strict_extensions = 0
first_extensions = []
for gg in range(2,41):
    for ss in range(2,41):
        grid_cases += 1
        new = new_surface_product_kernel_exact(gg,ss)
        old = old_cardinality_exact(gg,ss)
        new_successes += int(new)
        if new and not old:
            strict_extensions += 1
            if len(first_extensions) < 10:
                first_extensions.append((gg,ss))

assert grid_cases == 1521
assert new_successes == 1231
assert strict_extensions == 651
assert first_extensions[:4] == [(5,3),(6,4),(6,5),(6,6)]

# Independent high-precision numerical consistency cross-check of the exact predicate.
def beta_decimal(D: int, a: Decimal) -> Decimal:
    qq = Decimal(D-1)
    if a <= 2*qq.sqrt():
        return qq.sqrt()
    return (a + (a*a - 4*qq).sqrt())/2

mismatches = 0
for gg in range(2,41):
    for ss in range(2,41):
        a = Decimal(4)*Decimal(gg).sqrt() + Decimal(4)*Decimal(2*ss-1).sqrt()
        direct = beta_decimal(4*gg+4*ss, a) < Decimal(4*gg-3)
        if direct != new_surface_product_kernel_exact(gg,ss):
            mismatches += 1
assert mismatches == 0

sqrt5 = Decimal(5).sqrt()
beta_frozen = Decimal(7) + Decimal(4)*sqrt5
pc_bound = Decimal(1)/Decimal(17)
pu_bound = Decimal(1)/beta_frozen
gap = pu_bound-pc_bound
M5 = (Decimal(77)-Decimal(17)*sqrt5)/Decimal(4)
old_a = Decimal(12)+Decimal(4)*sqrt5
old_threshold = Decimal(320)/Decimal(17)
cheeger_pc_upper = Decimal(1)/(Decimal(21)-Decimal(4)*sqrt5)

print('PROB10-09 VERTICAL SUBGROUP SPECTRAL BUDGET EXACT CHECK')
print(f'D={D} q={q} B={B}')
print('new_adjacency_bound=8*sqrt(5)')
print('new_beta=7+4*sqrt(5)')
print(f'new_beta_decimal={beta_frozen}')
print(f'beta_lt_17_square_margin={beta_lt_B_square_margin}')
print(f'pc_upper=1/17={pc_bound}')
print(f'pu_lower=1/(7+4sqrt5)={pu_bound}')
print(f'gap_lower=(68sqrt5-150)/527={gap}')
print(f'gap_gt_1_260_square_margin={gap_gt_1_260_square_margin}')
print(f'M5={M5} m=12 old_scope_fails={not old_cardinality_exact(5,3)}')
print(f'm_gt_M5_square_margin={m_gt_M5_square_margin}')
print(f'old_plus_m_a={old_a}')
print(f'old_plus_m_beta_lt_17_required_a_lt={old_threshold}')
print(f'old_plus_m_condition_fails={old_a >= old_threshold}')
print(f'cheeger_pc_upper={cheeger_pc_upper}')
print(f'cheeger_crosses_uniqueness_floor={cheeger_pc_upper < pu_bound}')
print(f'cheeger_failure_square_margin={cheeger_failure_square_margin}')
print(f'grid_cases={grid_cases}')
print(f'grid_new_successes={new_successes}')
print(f'grid_strict_extensions_over_old={strict_extensions}')
print(f'first_strict_extensions={first_extensions}')
print(f'grid_decimal_mismatches={mismatches}')
print('ALL_EXACT_CHECKS_PASS')
