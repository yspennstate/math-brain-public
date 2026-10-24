from fractions import Fraction as F
from math import factorial

# Exact integer/rational certificate for a 3-atom ACG trial law.
D = F(46865077, 10000000)   # 4.6865077
U_REPORTED = F(1171627, 250000)       # 4.686508 > D
W = 100_000_000
weights = [30_378_594, 61_227_086, 8_394_320]  # sum W
V = 100_000_000
znum = [44_712_052, 8_630_144, V]               # x,y,1
DMAX = 26
LOG_LOCAL_TERMS = 8
LOG2_TERMS = 14
EDGE_TERMS = 12
EXP_TERMS = 38
DYAD_BITS = 96
DYAD = 1 << DYAD_BITS

assert sum(weights) == W

# A(z)=(2+z)/3 and B(z)=(1+2z)/3, with common denominator 3V.
Anum = [2*V + z for z in znum]
Bnum = [V + 2*z for z in znum]

# powers for exact state arithmetic
Apow = [[1]*(DMAX+1) for _ in range(3)]
Bpow = [[1]*(DMAX+1) for _ in range(3)]
Zpow = [[1]*(DMAX+1) for _ in range(3)]
Wpow = [[1]*(DMAX+1) for _ in range(3)]
for i in range(3):
    for k in range(1, DMAX+1):
        Apow[i][k] = Apow[i][k-1] * Anum[i]
        Bpow[i][k] = Bpow[i][k-1] * Bnum[i]
        Zpow[i][k] = Zpow[i][k-1] * znum[i]
        Wpow[i][k] = Wpow[i][k-1] * weights[i]


def atanh_partial(t: F, n: int) -> F:
    s = F(0); pw = t; t2 = t*t
    for j in range(n):
        s += pw / (2*j+1)
        pw *= t2
    return 2*s


def atanh_tail_abs(t: F, n: int) -> F:
    a = abs(t)
    return 2 * a**(2*n+1) / F(2*n+1) / (1-a*a)

# rigorous lower bound on log 2 via t=1/3
T2 = F(1,3)
LOG2_LO = atanh_partial(T2, LOG2_TERMS) - atanh_tail_abs(T2, LOG2_TERMS)
assert LOG2_LO > 0


def ceil_dyad(q: F) -> int:
    num = q.numerator * DYAD
    den = q.denominator
    return -((-num)//den)


def floor_dyad(q: F) -> int:
    return (q.numerator * DYAD)//q.denominator


def log_upper_from_ratio(num: int, den: int) -> int:
    # 0 < num/den <= 1. Scale upward by powers of two into [1/2,1].
    assert 0 < num <= den
    r = 0
    n = num
    while 2*n < den:
        n *= 2
        r += 1
    # z=n/den in [1/2,1], t=(z-1)/(z+1) in [-1/3,0].
    t = F(n-den, n+den)
    assert F(-1,3) <= t <= 0
    # For t<=0 all omitted atanh terms are negative, so the partial sum is an upper bound.
    up = atanh_partial(t, LOG_LOCAL_TERMS) - r*LOG2_LO
    return ceil_dyad(up)


def log_lower(q: F) -> int:
    assert 0 < q <= 1
    # q here is an edge factor >= 2/3, so t is small and no power-of-two scaling is needed.
    t = (q-1)/(q+1)
    part = atanh_partial(t, EDGE_TERMS)
    lo = part - atanh_tail_abs(t, EDGE_TERMS)
    return floor_dyad(lo)

# Compute conditional log upper bounds as exact integers over W^D * 2^B.
series = F(0)
dpow_over_fact = F(1)
for n in range(DMAX+1):
    if n:
        dpow_over_fact = dpow_over_fact * D / n
    cond_num = 0
    fn = factorial(n)
    denS = (3*V)**n
    three_pow_n = 3**n
    for k1 in range(n+1):
        for k2 in range(n-k1+1):
            k3 = n-k1-k2
            mult = fn // (factorial(k1)*factorial(k2)*factorial(k3))
            prob_num = mult * Wpow[0][k1] * Wpow[1][k2] * Wpow[2][k3]
            s_num = (
                3 * Apow[0][k1]*Apow[1][k2]*Apow[2][k3]
                - 3 * Bpow[0][k1]*Bpow[1][k2]*Bpow[2][k3]
                + three_pow_n * Zpow[0][k1]*Zpow[1][k2]*Zpow[2][k3]
            )
            assert 0 < s_num <= denS
            log_hi_dyad = log_upper_from_ratio(s_num, denS)
            cond_num += prob_num * log_hi_dyad
    cond_hi = F(cond_num, (W**n)*DYAD)
    series += dpow_over_fact * cond_hi

assert series < 0


def exp_upper(q: F) -> F:
    term = F(1); s = F(1)
    for n in range(1, EXP_TERMS+1):
        term = term*q/n
        s += term
    nxt = term*q/(EXP_TERMS+1)
    ratio = q/(EXP_TERMS+2)
    assert ratio < 1
    return s + nxt/(1-ratio)

# Since series<0, lower-bounding e^{-d} by 1/upper(e^d) produces an upper bound.
first_upper = series / exp_upper(D)

# Exact lower bound for the edge-log expectation on the 3x3 support.
edge_num = 0
for i in range(3):
    for j in range(3):
        # R=1-(1-a)(1-b)/3 with a=z_i/V,b=z_j/V.
        Rq = F(3*V*V - (V-znum[i])*(V-znum[j]), 3*V*V)
        lo_dyad = log_lower(Rq)
        edge_num += weights[i]*weights[j]*lo_dyad
edge_lower = F(edge_num, W*W*DYAD)
assert edge_lower < 0

sigma_upper = first_upper - D*edge_lower/2

print(f'd_cert = {float(D):.9f}')
print(f'reported_endpoint = {float(U_REPORTED):.9f}')
print('weights =', [w/W for w in weights])
print('support =', [z/V for z in znum])
print('D_max =', DMAX)
print('dyad_bits =', DYAD_BITS)
print('first_term_upper ~= %.18e' % float(first_upper))
print('edge_log_expect_lower ~= %.18e' % float(edge_lower))
print('Sigma_upper ~= %.18e' % float(sigma_upper))
print('SIGMA_STRICTLY_NEGATIVE =', sigma_upper < 0)
print('D_CERT_STRICTLY_BELOW_REPORTED_ENDPOINT =', D < U_REPORTED)
print('ALL_EXACT_CHECKS_PASS =', (sigma_upper < 0) and (D < U_REPORTED))
