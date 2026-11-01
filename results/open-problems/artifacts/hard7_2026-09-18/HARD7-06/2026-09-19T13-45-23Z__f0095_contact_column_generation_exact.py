from fractions import Fraction as F
from math import factorial

# HARD7-06 exact self-check: the previously certified three-atom ACG witness,
# evaluated at a strictly smaller average degree. Every sign decision below
# is an exact Fraction/integer comparison; displayed decimals are presentation.
D = F(46865076662, 10_000_000_000)  # 4.6865076662
W = 100_000_000
weights = [30_378_594, 61_227_086, 8_394_320]
V = 100_000_000
znum = [44_712_052, 8_630_144, V]
DMAX = 26
LOG_LOCAL_TERMS = 8
LOG2_TERMS = 14
EDGE_TERMS = 12
EXP_TERMS = 38
DYAD_BITS = 96
DYAD = 1 << DYAD_BITS

assert sum(weights) == W

Anum = [2*V + z for z in znum]      # numerator of A(z)=(2+z)/3
Bnum = [V + 2*z for z in znum]      # numerator of B(z)=(1+2z)/3
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

def atanh_partial(t, n):
    s = F(0)
    pw = t
    t2 = t*t
    for j in range(n):
        s += pw / (2*j+1)
        pw *= t2
    return 2*s

def atanh_tail_abs(t, n):
    a = abs(t)
    return 2*a**(2*n+1) / F(2*n+1) / (1-a*a)

# rigorous lower bound for log(2)
t2 = F(1, 3)
LOG2_LO = atanh_partial(t2, LOG2_TERMS) - atanh_tail_abs(t2, LOG2_TERMS)
assert LOG2_LO > 0

def ceil_dyad(q):
    return -((-q.numerator * DYAD) // q.denominator)

def floor_dyad(q):
    return (q.numerator * DYAD) // q.denominator

def log_upper_ratio(num, den):
    # 0 < num/den <= 1. Scale to [1/2,1].
    assert 0 < num <= den
    r = 0
    n = num
    while 2*n < den:
        n *= 2
        r += 1
    t = F(n-den, n+den)
    assert F(-1,3) <= t <= 0
    # t<=0: all omitted atanh terms are negative, so the partial sum is upper.
    return ceil_dyad(atanh_partial(t, LOG_LOCAL_TERMS) - r*LOG2_LO)

def log_lower(q):
    assert 0 < q <= 1
    t = (q-1)/(q+1)
    lo = atanh_partial(t, EDGE_TERMS) - atanh_tail_abs(t, EDGE_TERMS)
    return floor_dyad(lo)

# Vertex term. For every state S is a probability in (0,1], so deleting the
# Poisson tail deletes non-positive log terms and is an upper bound.
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
            cond_num += prob_num * log_upper_ratio(s_num, denS)
    cond_hi = F(cond_num, W**n * DYAD)
    series += dpow_over_fact * cond_hi
assert series < 0

def exp_upper(q):
    term = F(1)
    s = F(1)
    for n in range(1, EXP_TERMS+1):
        term = term*q/n
        s += term
    nxt = term*q/(EXP_TERMS+1)
    ratio = q/(EXP_TERMS+2)
    assert ratio < 1
    return s + nxt/(1-ratio)

# series<0, so a lower bound on e^{-d} gives an upper bound on the vertex term.
first_upper = series / exp_upper(D)

# Exact lower bound for E log R; subtraction then gives an upper bound on Sigma.
edge_num = 0
for i in range(3):
    for j in range(3):
        Rq = F(3*V*V - (V-znum[i])*(V-znum[j]), 3*V*V)
        edge_num += weights[i]*weights[j]*log_lower(Rq)
edge_lower = F(edge_num, W*W*DYAD)
assert edge_lower < 0

sigma_upper = first_upper - D*edge_lower/2

print(f"d_cert = {float(D):.10f}")
print("weights =", [w/W for w in weights])
print("support =", [z/V for z in znum])
print("D_max =", DMAX)
print("dyad_bits =", DYAD_BITS)
print("first_term_upper ~= %.18e" % float(first_upper))
print("edge_log_expect_lower ~= %.18e" % float(edge_lower))
print("Sigma_upper ~= %.18e" % float(sigma_upper))
print("SIGMA_STRICTLY_NEGATIVE =", sigma_upper < 0)
print("ALL_EXACT_CHECKS_PASS =", sigma_upper < 0)
