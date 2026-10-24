from fractions import Fraction as F
from math import factorial

# HARD7-06 exact certificate: cavity-guided four-atom ACG trial law.
# Every sign decision below is exact integer/Fraction arithmetic.
D = F(4686507635, 10**9)  # 4.686507635
W = 100_000_000
weights = [15_333_616, 28_476_429, 48_318_715, 7_871_240]
V = 100_000_000
znum = [56_153_802, 26_488_215, 6_698_304, V]

DMAX = 28
LOG_LOCAL_TERMS = 10
LOG2_TERMS = 18
EDGE_TERMS = 16
EXP_TERMS = 45
DYAD_BITS = 128
DYAD = 1 << DYAD_BITS

assert sum(weights) == W
K = len(weights)

# A(z)=(2+z)/3, B(z)=(1+2z)/3, common denominator 3V.
Anum = [2 * V + z for z in znum]
Bnum = [V + 2 * z for z in znum]

Apow = [[1] * (DMAX + 1) for _ in range(K)]
Bpow = [[1] * (DMAX + 1) for _ in range(K)]
Zpow = [[1] * (DMAX + 1) for _ in range(K)]
Wpow = [[1] * (DMAX + 1) for _ in range(K)]
for i in range(K):
    for k in range(1, DMAX + 1):
        Apow[i][k] = Apow[i][k - 1] * Anum[i]
        Bpow[i][k] = Bpow[i][k - 1] * Bnum[i]
        Zpow[i][k] = Zpow[i][k - 1] * znum[i]
        Wpow[i][k] = Wpow[i][k - 1] * weights[i]


def atanh_partial(t: F, n: int) -> F:
    s = F(0)
    pw = t
    t2 = t * t
    for j in range(n):
        s += pw / F(2 * j + 1)
        pw *= t2
    return 2 * s


def atanh_tail_abs(t: F, n: int) -> F:
    a = abs(t)
    return 2 * a ** (2 * n + 1) / F(2 * n + 1) / (1 - a * a)


# Rigorous lower bound on log 2 from t=1/3.
T2 = F(1, 3)
LOG2_LO = atanh_partial(T2, LOG2_TERMS) - atanh_tail_abs(T2, LOG2_TERMS)
assert LOG2_LO > 0


def ceil_dyad(q: F) -> int:
    return -((-q.numerator * DYAD) // q.denominator)


def floor_dyad(q: F) -> int:
    return (q.numerator * DYAD) // q.denominator


def log_upper_from_ratio(num: int, den: int) -> int:
    # 0 < num/den <= 1. Scale by powers of two into [1/2,1].
    assert 0 < num <= den
    r = 0
    n = num
    while 2 * n < den:
        n *= 2
        r += 1
    t = F(n - den, n + den)
    assert F(-1, 3) <= t <= 0
    # For t<=0 every omitted atanh term is negative, so the partial sum
    # is an upper bound. Subtracting r*LOG2_LO remains an upper bound.
    up = atanh_partial(t, LOG_LOCAL_TERMS) - r * LOG2_LO
    return ceil_dyad(up)


def log_lower(q: F) -> int:
    assert 0 < q <= 1
    t = (q - 1) / (q + 1)
    part = atanh_partial(t, EDGE_TERMS)
    lo = part - atanh_tail_abs(t, EDGE_TERMS)
    return floor_dyad(lo)


def comps4(n: int):
    for k1 in range(n + 1):
        for k2 in range(n - k1 + 1):
            for k3 in range(n - k1 - k2 + 1):
                yield (k1, k2, k3, n - k1 - k2 - k3)


# Vertex term. Conditional on total Poisson degree n, enumerate the exact
# four-cell multinomial law. Since S<=1, every omitted n>DMAX contribution
# to E log S is <=0, hence discarding the tail is one-sided upward.
series = F(0)
dpow_over_fact = F(1)
for n in range(DMAX + 1):
    if n:
        dpow_over_fact = dpow_over_fact * D / n
    cond_num = 0
    fn = factorial(n)
    denS = (3 * V) ** n
    three_pow_n = 3 ** n
    for ks in comps4(n):
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
    cond_hi = F(cond_num, (W ** n) * DYAD)
    series += dpow_over_fact * cond_hi

assert series < 0


def exp_upper(q: F) -> F:
    term = F(1)
    s = F(1)
    for n in range(1, EXP_TERMS + 1):
        term = term * q / n
        s += term
    nxt = term * q / (EXP_TERMS + 1)
    ratio = q / (EXP_TERMS + 2)
    assert ratio < 1
    return s + nxt / (1 - ratio)


# For a negative partial series, 1/upper(e^d) is a lower bound on e^{-d};
# multiplying a negative number by it gives an upper bound on the vertex term.
first_upper = series / exp_upper(D)

# Edge-log expectation: exact support sum with rigorous lower log bounds.
edge_num = 0
for i in range(K):
    for j in range(K):
        rq = F(3 * V * V - (V - znum[i]) * (V - znum[j]), 3 * V * V)
        edge_num += weights[i] * weights[j] * log_lower(rq)
edge_lower = F(edge_num, W * W * DYAD)
assert edge_lower < 0

sigma_upper = first_upper - D * edge_lower / 2

print(f'd_cert = {float(D):.10f}')
print('weights =', [w / W for w in weights])
print('support =', [z / V for z in znum])
print('D_max =', DMAX)
print('dyad_bits =', DYAD_BITS)
print('first_term_upper ~= %.18e' % float(first_upper))
print('edge_log_expect_lower ~= %.18e' % float(edge_lower))
print('Sigma_upper ~= %.18e' % float(sigma_upper))
print('SIGMA_STRICTLY_NEGATIVE =', sigma_upper < 0)
print('ALL_EXACT_CHECKS_PASS =', sigma_upper < 0)
