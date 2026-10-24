from functools import lru_cache
from fractions import Fraction as F
from math import factorial

# P04 / T10 rigorous certificate: moving-centered 3-row, 9-column block.
# The finite-state exponential-infection recurrence is evaluated with fixed-point
# integer upward rounding. If U(S)/Q upper-bounds the exact expectation at all
# children, then ceil((Q + sum m_j U(child))/m)/Q upper-bounds the parent.
# The same positive recurrence certifies the terminal outer-lane probability.

L = 9
Q = 10**15
verts = [(x, r) for x in range(L + 1) for r in range(3)]
idx = {v: i for i, v in enumerate(verts)}
out = [[] for _ in verts]
for x in range(L):
    for rr in (0, 1):
        a, b = idx[(x, rr)], idx[(x, rr + 1)]
        out[a].append(b)
        out[b].append(a)
    for rr in range(3):
        out[idx[(x, rr)]].append(idx[(x + 1, rr)])

targets = [idx[(L, rr)] for rr in range(3)]
target_mask = sum(1 << t for t in targets)
outer_mask = (1 << targets[0]) | (1 << targets[2])
state_count = 0

@lru_cache(None)
def rec(mask):
    global state_count
    state_count += 1
    if mask & target_mask:
        # A first-hit absorbing state contains exactly the newly infected target.
        return 0, Q if (mask & outer_mask) else 0

    rates = {}
    total = 0
    mm = mask
    while mm:
        bit = mm & -mm
        i = bit.bit_length() - 1
        mm -= bit
        for j in out[i]:
            if not ((mask >> j) & 1):
                rates[j] = rates.get(j, 0) + 1
                total += 1
    assert total > 0

    # Exact expectation recurrence:
    # E(S)=1/total + sum_j rates[j]/total * E(S union {j}).
    # Integer ceiling division makes both returned coordinates rigorous uppers.
    tsum = Q
    psum = 0
    for j, mult in rates.items():
        tchild, pchild = rec(mask | (1 << j))
        tsum += mult * tchild
        psum += mult * pchild
    tupper = (tsum + total - 1) // total
    pupper = (psum + total - 1) // total
    return tupper, pupper

g9_int, pouter_int = rec(1 << idx[(0, 1)])
assert state_count == 4162734

g9_upper = F(g9_int, Q)
a9_upper = F(g9_int, Q * L)
pouter_upper = F(pouter_int, Q)
axis_cap = a9_upper                     # exact rational rigorous upper cap
pouter_cap = F(631541, 1000000)        # 0.631541
assert axis_cap == a9_upper
assert pouter_upper < pouter_cap

# Consumed canonical ten-local weighted SAW constants.
A = F(3889, 2000)
B = F(27893, 10000)
r = F(1993, 400)
Kbar = F(44100) * F(10**14) * (B / r) ** 10

# Positive atanh-series bounds for log x, x>1.
def log_bounds_gt1(x, N):
    assert x > 1
    z = (x - 1) / (x + 1)
    lo = F(0)
    for k in range(N + 1):
        lo += F(2) * z ** (2 * k + 1) / F(2 * k + 1)
    tail = F(2) * z ** (2 * N + 3) / (F(2 * N + 3) * (1 - z * z))
    return lo, lo + tail

LA_L, LA_U = log_bounds_gt1(A, 18)
LB_L, LB_U = log_bounds_gt1(B, 18)

# New critical-slope bracket for the fixed ten-local compiler + new axis cap.
# rho_* = ((r-1) axis_cap - log A)/log B.
rho_lo = F(3275299, 2000000)           # 1.6376495
rho_hi = F(8188248, 5000000)           # 1.6376496
G_lo_upper = LA_U + rho_lo * LB_U - (r - 1) * axis_cap
G_hi_lower = LA_L + rho_hi * LB_L - (r - 1) * axis_cap
assert G_lo_upper < 0 < G_hi_lower

# Closed rational cone and uniform strict-triangle defect.
rho0 = F(16377, 10000)                 # 1.6377
c = F(588807, 1000000)                 # 0.588807
s = F(3982501, 1000000)                # (r-1)+1e-6
q = r / (1 + s)
assert q == F(4982500, 4982501)
beta_hat = F(99999, 100000)            # 0.99999
assert axis_cap < c
assert rho0 > rho_hi

LQ_L, LQ_U = log_bounds_gt1(1 / q, 3)
logbeta_upper = s * c - LA_L - rho0 * LB_L - (1 + rho0) * LQ_L
LBH_L, LBH_U = log_bounds_gt1(1 / beta_hat, 3)
log_beta_hat_lower = -LBH_U
assert logbeta_upper < log_beta_hat_lower < 0

delta = 2 * (c - axis_cap)
assert delta == F(188760773, 11250000000000)

# Explicit finite-to-infinite residual at m=an. For the axis target 2m e1,
# N=2m/9 moving blocks. Since increments are iid, symmetric, and xi^2 is the
# outer-hit indicator, E|S_N| <= sqrt(N p_out). At the chosen scale a simple
# integer square upper bound yields repair/m < 11239/m.
mfinite = 900000000
assert mfinite % 9 == 0
Nblocks = 2 * mfinite // 9
assert Nblocks == 200000000
# Nblocks*pouter_cap = 126308200 and 11239^2 = 126315121.
assert F(Nblocks) * pouter_cap < F(11239**2)
repair_hat = F(11239, mfinite)

Cbar = Kbar / (1 - q)
# beta_hat^m <= exp(-m/100000) = exp(-9000) <= 20!/9000^20.
exp_tail_hat = F(factorial(20), 9000**20)
tail_error_hat = 2 * c * Cbar * exp_tail_hat
finite_margin = delta - repair_hat - tail_error_hat
assert finite_margin > F(4, 1000000)

print('P04 T10 moving-centered strip-9 / cone-1.6377 rigorous certificate')
print('ALL_RIGOROUS_CHECKS_PASS = True')
print('fixed_point_scale_Q =', Q)
print('block_states_center =', state_count)
print('g9_int =', g9_int)
print('g9_upper =', g9_upper, '=', float(g9_upper))
print('a9_upper =', a9_upper, '=', float(a9_upper))
print('axis_cap =', axis_cap, '=', float(axis_cap))
print('pouter_int =', pouter_int)
print('pouter_upper =', pouter_upper, '=', float(pouter_upper))
print('pouter_cap =', pouter_cap, '=', float(pouter_cap))
print('rho_star_bracket = (', float(rho_lo), ',', float(rho_hi), ')')
print('G_lo_upper =', float(G_lo_upper))
print('G_hi_lower =', float(G_hi_lower))
print('rho0 =', rho0, '=', float(rho0))
print('c =', c, '=', float(c))
print('s =', s, '=', float(s))
print('q =', q, '=', float(q))
print('beta_hat =', beta_hat, '=', float(beta_hat))
print('logbeta_upper =', float(logbeta_upper))
print('log_beta_hat_lower =', float(log_beta_hat_lower))
print('delta =', delta, '=', float(delta))
print('Kbar =', Kbar, '=', float(Kbar))
print('Cbar =', Cbar, '=', float(Cbar))
print('finite_m =', mfinite)
print('Nblocks =', Nblocks)
print('repair_hat =', repair_hat, '=', float(repair_hat))
print('tail_error_hat =', tail_error_hat, '=', float(tail_error_hat))
print('finite_margin =', finite_margin, '=', float(finite_margin))
print('finite_margin > 4e-6 =', finite_margin > F(4, 1000000))
