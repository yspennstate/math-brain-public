from collections import defaultdict
from fractions import Fraction

# Exact r=2 canonical greedy-embedding frontier certificate.
# Genuine source model: the construction starts from two independent fair binary strings.

M = 20
Z = Fraction(1, 3)
WORDS = ("00", "01", "10", "11")


def endpoint_vec(start, r1, r2, r3):
    """Greedy endpoints for 00,01,10,11 from start bit and first 3 run lengths."""
    if start == 0:
        return (
            2 if r1 >= 2 else r2 + 2,
            r1 + 1,
            r1 + r2 + 1,
            r1 + 2 if r2 >= 2 else r1 + r3 + 2,
        )
    q = endpoint_vec(0, r1, r2, r3)
    # bit-complement sends 00<->11 and 01<->10
    return (q[3], q[2], q[1], q[0])


def frontier_exponents(px, py):
    """Endpoint sums for lex-tie-broken Pareto-minimal depth-2 words."""
    out = []
    for i in range(4):
        a, b = px[i], py[i]
        dominated = False
        for j in range(4):
            if j == i:
                continue
            c, d = px[j], py[j]
            if c <= a and d <= b and ((c < a or d < b) or (c == a and d == b and j < i)):
                dominated = True
                break
        if not dominated:
            out.append(a + b)
    return out


def greedy_endpoint(s, w):
    p = 0
    for c in w:
        p = s.index(c, p) + 1
    return p


def brute_endpoint_vec(start, r1, r2, r3):
    bits = []
    b = str(start)
    for r in (r1, r2, r3):
        bits.extend([b] * r)
        b = "1" if b == "0" else "0"
    # one symbol of run 4 suffices for every length-2 target
    bits.append(b)
    s = "".join(bits)
    return tuple(greedy_endpoint(s, w) for w in WORDS)


# Validate the run formulas independently on a finite exact grid.
for start in (0, 1):
    for r1 in range(1, 6):
        for r2 in range(1, 6):
            for r3 in range(1, 6):
                assert endpoint_vec(start, r1, r2, r3) == brute_endpoint_vec(start, r1, r2, r3)


# For a fair iid binary string, conditional on the start bit, each complete run length
# has law P(R=r)=2^{-r}.  Truncate all three run lengths at M and aggregate the
# endpoint map with common dyadic denominator D=2^(1+3M), including P(start)=1/2.
D = 1 << (1 + 3 * M)
dist = defaultdict(int)
for start in (0, 1):
    for r1 in range(1, M + 1):
        for r2 in range(1, M + 1):
            for r3 in range(1, M + 1):
                e = 1 + r1 + r2 + r3
                wt = 1 << ((1 + 3 * M) - e)
                dist[endpoint_vec(start, r1, r2, r3)] += wt

mass = Fraction(sum(dist.values()), D)
assert mass == (1 - Fraction(1, 2**M)) ** 3

# At z=1/3 all frontier weights are powers of 3.  Under the truncation every
# depth-2 endpoint is at most 2M+2, so a common denominator is 3^(4M+4).
Emax = 4 * M + 4
pow3 = [3**k for k in range(Emax + 1)]
num = 0
items = list(dist.items())
for px, ax in items:
    for py, ay in items:
        s = 0
        for e in frontier_exponents(px, py):
            s += pow3[Emax - e]
        num += ax * ay * s

den = D * D * pow3[Emax]
m2_trunc = Fraction(num, den)

# If any of the six run lengths exceeds M, the probability is exactly the tail below.
# A depth-2 frontier has at most 4 words and every endpoint in each string is >=2,
# so its total z-weight is at most 4 z^4 = 4/81.  This is a rigorous omitted-tail bound.
tail_prob = 1 - (1 - Fraction(1, 2**M)) ** 6
tail_bound = Fraction(4, 81) * tail_prob
m2_upper = m2_trunc + tail_bound

# r=1 has the closed form m1(z)=z^2/2+z^3/(2-z).  At z=1/3 this is 7/90.
m1 = Fraction(7, 90)
assert m2_upper < m1 * m1

# Exact logarithm-free comparison U_2(1/3)<857/1000.
# U_2=4 log(3)/(-log m2).  The inequality is equivalent to
# 3^4000 * m2^857 < 1.
a, b = 857, 1000
n, d = m2_upper.numerator, m2_upper.denominator
assert (3 ** (4 * b)) * (n**a) < d**a

# The same z does not already give U_1<857/1000; the depth-2 cross-branch pruning
# is doing genuine work.
assert (3 ** (2 * b)) * (m1.numerator**a) > m1.denominator**a


# Falsification of the tempting one-layer finite-profile Markov closure.
def lcs(a, b):
    dp = [0] * (len(b) + 1)
    for x in a:
        nd = [0] * (len(b) + 1)
        for j, y in enumerate(b, 1):
            nd[j] = dp[j - 1] + 1 if x == y else max(dp[j], nd[j - 1])
        dp = nd
    return dp[-1]


def extension_signature(x, y):
    L = lcs(x, y)
    return (
        lcs(x, y + "0") - L,
        lcs(x, y + "1") - L,
        lcs(x + "0", y) - L,
        lcs(x + "1", y) - L,
    )


x = "00001011"
y = "11110100"
assert extension_signature(x, y) == (1, 1, 1, 1)
for u in "01":
    for v in "01":
        assert extension_signature(x + u, y + v) == (1, 1, 1, 1)

print("PROB10-02 R17 exact canonical greedy-frontier checker")
print("M =", M, "z =", Z)
print("endpoint_maps =", len(dist))
print("truncated_mass =", mass)
print("m2_trunc =", m2_trunc)
print("tail_prob =", tail_prob)
print("tail_bound =", tail_bound)
print("m2_upper =", m2_upper)
print("m1 =", m1)
print("m2_upper_lt_m1_sq =", m2_upper < m1 * m1)
print("U2_lt_857_over_1000 =", True)
print("one_layer_signature_self_loop =", x, y, (1, 1, 1, 1))
print("ALL_EXACT_CHECKS_PASS")
print("RETURN_CODE=0")
