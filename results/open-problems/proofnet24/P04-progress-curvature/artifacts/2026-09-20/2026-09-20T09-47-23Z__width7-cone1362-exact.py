from fractions import Fraction as F
from math import factorial

# P04 / T10 exact rational scalar certificate consuming:
#  (i) width-7 length-4 undirected moving-slab upper certificate, and
# (ii) canonical ten-local weighted SAW count constants.

# Finite block output (rigorous upward-rounded fixed-point certificate).
tau_num = 2071160703929378
Q = 10**15
L = 4
axis = F(tau_num, Q*L)
xi2_upper = F(2496533430161757, Q)
xi2_bar = F(124827, 50000)  # 2.49654 > certified xi^2 upper
assert xi2_upper < xi2_bar

# Canonical ten-local weighted SAW constants.
A = F(3889, 2000)
B = F(27893, 10000)
r = F(1993, 400)
Kbar = F(44100) * F(10**14) * (B / r) ** 10

# Positive atanh bounds: log x = 2 sum z^(2k+1)/(2k+1), z=(x-1)/(x+1).
def log_bounds_gt1(x, N):
    assert x > 1
    z = (x - 1) / (x + 1)
    lo = F(0)
    for k in range(N + 1):
        lo += F(2) * z ** (2*k + 1) / F(2*k + 1)
    tail = F(2) * z ** (2*N + 3) / (F(2*N + 3) * (1 - z*z))
    return lo, lo + tail

LA_L, LA_U = log_bounds_gt1(A, 24)
LB_L, LB_U = log_bounds_gt1(B, 24)

# Critical slope rho_* = ((r-1)a - log A)/log B.
rho_lo = F(13619684, 10_000_000)  # 1.3619684
rho_hi = F(13619685, 10_000_000)  # 1.3619685
G_lo_upper = LA_U + rho_lo*LB_U - (r-1)*axis
G_hi_lower = LA_L + rho_hi*LB_L - (r-1)*axis
assert G_lo_upper < 0 < G_hi_lower

# Clean closed cone |y|/x >= 681/500 = 1.362.
rho0 = F(681, 500)
c = F(129449, 250000)             # 0.517796 > axis cap
assert c > axis
s = (r - 1) + F(1, 10_000_000)
q = r / (1 + s)
assert q == F(49825000, 49825001)
beta_hat = F(999991, 1_000_000)

LQ_L, LQ_U = log_bounds_gt1(1/q, 5)
logbeta_upper = s*c - LA_L - rho0*LB_L - (1+rho0)*LQ_L
LBH_L, LBH_U = log_bounds_gt1(1/beta_hat, 5)
log_beta_hat_lower = -LBH_U
assert logbeta_upper < log_beta_hat_lower < 0

delta = 2*(c-axis)
assert delta == F(11648035311, 10**15)
assert delta > F(11, 10**6)       # > 1.1e-5

# Explicit finite residual scale.  For target 2m e1, length-4 moving blocks
# require N=m/2 blocks (m even).  E|S_N| <= sqrt(N E xi^2).
m = 100_000_000_000
assert m % 2 == 0
N = m // 2
assert F(N)*xi2_bar < F(353309**2)
repair_hat = F(353309, m)

Cbar = Kbar / (1-q)
# beta_hat^m=(1-9e-6)^m <= exp(-900000) <= 20!/900000^20.
exp_tail_hat = F(factorial(20), 900000**20)
tail_error_hat = 2*c*Cbar*exp_tail_hat
finite_margin = delta - repair_hat - tail_error_hat
assert finite_margin > F(8, 10**6)

# Stronger defect on the already-covered old 1.6377 cone using its old c=0.588807.
old_c = F(588807, 1_000_000)
old_cone_defect = 2*(old_c-axis)
assert old_cone_defect == F(142033648035311, 10**15)

print('P04 T10 width-7 length-4 undirected moving-slab / cone-1.362 exact scalar certificate')
print('ALL_EXACT_CHECKS_PASS = True')
print('axis_cap =', axis, '=', float(axis))
print('xi2_upper =', xi2_upper, '=', float(xi2_upper))
print('xi2_bar =', xi2_bar, '=', float(xi2_bar))
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
print('finite_m =', m)
print('Nblocks =', N)
print('repair_hat =', repair_hat, '=', float(repair_hat))
print('tail_error_hat =', tail_error_hat, '=', float(tail_error_hat))
print('finite_margin =', finite_margin, '=', float(finite_margin))
print('old_1.6377_cone_defect =', old_cone_defect, '=', float(old_cone_defect))
