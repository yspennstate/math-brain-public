from fractions import Fraction as F
from math import factorial

# Rigorous one-sided ACG certificate for the retained rational law.
# This is the previous neutral-atom checker with tighter truncation/log bounds.
D = F(46865076260769, 10**13)
M = 10000
base_active = [12_485_014, 37_444_482, 42_645_848]
active_weights = [M * x for x in base_active]
neutral_weight = 74_246_562_184
W = sum(active_weights) + neutral_weight
V = 100_000_000
active_z = [62_520_784, 25_744_044, 5_606_726]
SACTIVE = sum(active_weights)

DMAX = 34
LOG_LOCAL_TERMS = 13
LOG2_TERMS = 24
EDGE_TERMS = 22
EXP_TERMS = 60
DYAD_BITS = 192
DYAD = 1 << DYAD_BITS
K = 3

Anum = [2 * V + z for z in active_z]
Bnum = [V + 2 * z for z in active_z]
Apow = [[1] * (DMAX + 1) for _ in range(K)]
Bpow = [[1] * (DMAX + 1) for _ in range(K)]
Zpow = [[1] * (DMAX + 1) for _ in range(K)]
Wpow = [[1] * (DMAX + 1) for _ in range(K)]
for i in range(K):
    for k in range(1, DMAX + 1):
        Apow[i][k] = Apow[i][k - 1] * Anum[i]
        Bpow[i][k] = Bpow[i][k - 1] * Bnum[i]
        Zpow[i][k] = Zpow[i][k - 1] * active_z[i]
        Wpow[i][k] = Wpow[i][k - 1] * active_weights[i]


def atanh_partial(t, n):
    s = F(0)
    pw = t
    t2 = t * t
    for j in range(n):
        s += pw / F(2 * j + 1)
        pw *= t2
    return 2 * s


def atanh_tail_abs(t, n):
    a = abs(t)
    return 2 * a ** (2 * n + 1) / F(2 * n + 1) / (1 - a * a)


LOG2_LO = atanh_partial(F(1, 3), LOG2_TERMS) - atanh_tail_abs(F(1, 3), LOG2_TERMS)


def ceil_dyad(q):
    return -((-q.numerator * DYAD) // q.denominator)


def floor_dyad(q):
    return (q.numerator * DYAD) // q.denominator


def log_upper_from_ratio(num, den):
    assert 0 < num <= den
    r = 0
    n = num
    while 2 * n < den:
        n *= 2
        r += 1
    t = F(n - den, n + den)
    assert F(-1, 3) <= t <= 0
    return ceil_dyad(atanh_partial(t, LOG_LOCAL_TERMS) - r * LOG2_LO)


def log_lower(q):
    assert 0 < q <= 1
    t = (q - 1) / (q + 1)
    return floor_dyad(atanh_partial(t, EDGE_TERMS) - atanh_tail_abs(t, EDGE_TERMS))


def comps3(n):
    for k1 in range(n + 1):
        for k2 in range(n - k1 + 1):
            yield (k1, k2, n - k1 - k2)


series = F(0)
dpow_over_fact = F(1)
for n in range(DMAX + 1):
    if n:
        dpow_over_fact = dpow_over_fact * D / n
    cond_num = 0
    fn = factorial(n)
    denS = (3 * V) ** n
    three_pow_n = 3 ** n
    for ks in comps3(n):
        mult = fn
        for kk in ks:
            mult //= factorial(kk)
        prob_num = mult
        PA = PB = P0 = 1
        for i, kk in enumerate(ks):
            prob_num *= Wpow[i][kk]
            PA *= Apow[i][kk]
            PB *= Bpow[i][kk]
            P0 *= Zpow[i][kk]
        s_num = 3 * PA - 3 * PB + three_pow_n * P0
        assert 0 < s_num <= denS
        cond_num += prob_num * log_upper_from_ratio(s_num, denS)
    series += dpow_over_fact * F(cond_num, (W ** n) * DYAD)
assert series < 0


def exp_upper(q):
    term = F(1)
    s = F(1)
    for n in range(1, EXP_TERMS + 1):
        term = term * q / n
        s += term
    nxt = term * q / (EXP_TERMS + 1)
    ratio = q / (EXP_TERMS + 2)
    assert ratio < 1
    return s + nxt / (1 - ratio)


LAM = D * F(SACTIVE, W)
first_upper = series / exp_upper(LAM)

edge_num = 0
for i in range(K):
    for j in range(K):
        rq = F(3 * V * V - (V - active_z[i]) * (V - active_z[j]), 3 * V * V)
        edge_num += active_weights[i] * active_weights[j] * log_lower(rq)
edge_lower = F(edge_num, W * W * DYAD)

sigma_upper = first_upper - D * edge_lower / 2

print(f"d_cert = {float(D):.13f}")
print(f"active_mass = {float(F(SACTIVE, W)):.15f}")
print(f"lambda_active = {float(LAM):.15f}")
print("D_max_active =", DMAX)
print("first_term_upper ~= %.18e" % float(first_upper))
print("edge_log_expect_lower ~= %.18e" % float(edge_lower))
print("Sigma_upper ~= %.18e" % float(sigma_upper))
print("sigma_upper_numerator_sign =", -1 if sigma_upper < 0 else (1 if sigma_upper > 0 else 0))
print("SIGMA_STRICTLY_NEGATIVE =", sigma_upper < 0)
print("ALL_EXACT_CHECKS_PASS =", sigma_upper < 0)
