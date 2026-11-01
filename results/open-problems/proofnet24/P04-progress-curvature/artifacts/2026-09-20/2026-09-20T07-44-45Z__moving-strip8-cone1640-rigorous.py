from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

# P04 / T10 rigorous certificate.
# New part: an 8-column moving-centered strip block is evaluated with
# directed ROUND_CEILING Decimal arithmetic. Every recurrence operation is
# positive, so induction on the infection-state DAG makes the returned value
# an upper bound on the exact rational expectation.
# Consumed part: the canonical PROB10-10 ten-local-SAW transfer constants.

# ---------------------------------------------------------------------------
# Part I. Rigorous upper bound for the center-start free-terminal L=8 block.
# ---------------------------------------------------------------------------
L = 8
PREC = 50
verts = [(x, r) for x in range(L + 1) for r in range(3)]
idx = {v: i for i, v in enumerate(verts)}
out = [[] for _ in verts]
for x in range(L):
    # Undirected physical vertical edges in departure columns.
    for rr in (0, 1):
        a, b = idx[(x, rr)], idx[(x, rr + 1)]
        out[a].append(b)
        out[b].append(a)
    # Horizontal physical edges are used only eastward by this restricted policy.
    for rr in range(3):
        out[idx[(x, rr)]].append(idx[(x + 1, rr)])
targets = [idx[(L, rr)] for rr in range(3)]
state_count = 0

with localcontext() as ctx:
    ctx.prec = PREC
    ctx.rounding = ROUND_CEILING
    D = Decimal

    @lru_cache(None)
    def rec(mask):
        global state_count
        state_count += 1
        for t in targets:
            if (mask >> t) & 1:
                return D(0)

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

        # Every operation below is on nonnegative quantities and is rounded
        # toward +infinity, hence gives an upper bound on the exact recurrence.
        et = D(1) / D(total)
        for j, mult in rates.items():
            child = rec(mask | (1 << j))
            et += (D(mult) / D(total)) * child
        return +et

    g8_upper = rec(1 << idx[(0, 1)])
    a8_upper_decimal = g8_upper / D(L)

assert state_count == 856569
axis_cap = F(294639, 500000)   # 0.589278 exactly
assert a8_upper_decimal < Decimal('0.589278')

# ---------------------------------------------------------------------------
# Part II. Consumed ten-local-SAW endpoint compiler with a simple explicit K.
# ---------------------------------------------------------------------------
A = F(3889, 2000)
B = F(27893, 10000)
r = F(1993, 400)
s = F(398251, 100000)
q = r / (1 + s)
assert q == F(498250, 498251)
assert max(A, 1 / A, B, 1 / B) == B

# The canonical exact artifact certifies 44100 states and a positive Collatz
# vector with z_min=1 and z_max=10^14. Thus for lengths ell>=10,
# L_ell <= Kbar r^ell. The crude all-words bound covers ell<10.
Kbar = F(44100) * F(10**14) * (B / r) ** 10
for ell in range(1, 10):
    assert (F(4) * B / r) ** ell < Kbar
Cbar = Kbar / (1 - q)

# New lower-tail parameters.
c = F(58937, 100000)       # 0.58937
rho = F(41, 25)            # 1.64
beta_hat = F(9999, 10000)  # 0.9999
assert axis_cap < c
assert rho < F(1701, 1000) # strict enlargement over prior best cone 1.701


def log_bounds_gt1(x, N):
    # log x = 2 sum_{k>=0} z^(2k+1)/(2k+1), z=(x-1)/(x+1), x>1.
    # The omitted positive tail is bounded geometrically.
    assert x > 1
    z = (x - 1) / (x + 1)
    lo = F(0)
    for k in range(N + 1):
        lo += F(2) * z ** (2 * k + 1) / F(2 * k + 1)
    tail = F(2) * z ** (2 * N + 3) / (F(2 * N + 3) * (1 - z * z))
    return lo, lo + tail

LA_L, LA_U = log_bounds_gt1(A, 14)
LB_L, LB_U = log_bounds_gt1(B, 14)
LQ_L, LQ_U = log_bounds_gt1(1 / q, 2)
logbeta_upper = s * c - LA_L - rho * LB_L - (1 + rho) * LQ_L
LBH_L, LBH_U = log_bounds_gt1(1 / beta_hat, 3)
log_beta_hat_lower = -LBH_U
assert logbeta_upper < log_beta_hat_lower
assert beta_hat < 1

# Infinite-volume strict-triangle defect based on the rational axis cap.
delta = 2 * (c - axis_cap)
assert delta == F(23, 125000)

# ---------------------------------------------------------------------------
# Part III. Explicit finite transfer error.
# ---------------------------------------------------------------------------
# For axis target distance 2m and L=8, use N=m/4 moving-centered blocks.
# Their vertical increments are iid, symmetric, and bounded by 1, hence
# E|S_N| <= sqrt(N). Dividing the endpoint repair by m gives <=1/(2 sqrt m).
# Take m=16,000,000, so that correction is exactly <=1/8000.
mfinite = 16_000_000
assert mfinite % 4 == 0
Nblocks = mfinite // 4
axis_error_hat = F(1, 8000)

# beta_hat^m = (1-1/10000)^m <= exp(-m/10000)=exp(-1600).
# Since exp(1600) >= 1600^50/50!, exp(-1600) <= 50!/1600^50.
exp_tail_hat = F(factorial(50), 1600**50)
tail_error_hat = 2 * c * Cbar * exp_tail_hat
finite_margin = delta - axis_error_hat - tail_error_hat
assert finite_margin > F(589, 10_000_000)  # > 5.89e-5

print('P04 T10 moving-centered strip-8 / cone-1.64 rigorous certificate')
print('ALL_RIGOROUS_CHECKS_PASS = True')
print('decimal_precision =', PREC, 'rounding = ROUND_CEILING')
print('block_states_center =', state_count)
print('g8_upper =', g8_upper)
print('a8_upper_decimal =', a8_upper_decimal)
print('axis_cap =', axis_cap, '=', float(axis_cap))
print('A =', A, 'B =', B, 'r =', r)
print('q =', q, '=', float(q))
print('Kbar =', Kbar, '=', float(Kbar))
print('Cbar =', Cbar, '=', float(Cbar))
print('c =', c, '=', float(c))
print('rho =', rho, '=', float(rho))
print('beta_hat =', beta_hat, '=', float(beta_hat))
print('logbeta_upper =', float(logbeta_upper))
print('log_beta_hat_lower =', float(log_beta_hat_lower))
print('delta =', delta, '=', float(delta))
print('finite_m =', mfinite)
print('Nblocks =', Nblocks)
print('axis_error_hat =', axis_error_hat, '=', float(axis_error_hat))
print('tail_error_hat =', tail_error_hat, '=', float(tail_error_hat))
print('finite_margin =', finite_margin, '=', float(finite_margin))
print('finite_margin > 5.89e-5 =', finite_margin > F(589, 10_000_000))
