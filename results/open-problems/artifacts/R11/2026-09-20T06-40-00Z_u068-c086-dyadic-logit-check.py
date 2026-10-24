from fractions import Fraction
from math import comb, factorial

ASSERTIONS = 0

def check(cond, msg=""):
    global ASSERTIONS
    if not cond:
        raise AssertionError(msg)
    ASSERTIONS += 1

def beta(i, j):
    return Fraction(factorial(i - 1) * factorial(j - 1), factorial(i + j - 1))

def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))

def clock(N, s):
    return Fraction(N, 2 * s * (N - s))

def rate(N, ps, i, j):
    out = Fraction(0)
    for s, p in enumerate(ps, 1):
        out += clock(N, s) * (p**i * (1 - p)**j + p**j * (1 - p)**i)
    return out

def tau_r1(x):
    # L = log 4. D(y)=2y mod L on [0,L), identity outside.
    if x < Fraction(1, 2) or x >= Fraction(4, 5):
        return x
    if x < Fraction(2, 3):
        return x * x / (x * x + (1 - x) * (1 - x))
    return x * x / (x * x + 4 * (1 - x) * (1 - x))

def branch_moment(b, m, k):
    # Exact integral over t in [k/b,(k+1)/b] of (b*t-k)^m dt.
    lo = Fraction(k, b)
    hi = Fraction(k + 1, b)
    total = Fraction(0)
    for a in range(m + 1):
        coeff = Fraction(comb(m, a) * (b**a) * ((-k)**(m - a)), 1)
        total += coeff * (hi**(a + 1) - lo**(a + 1)) / Fraction(a + 1, 1)
    return total

# CTCS beta-rate identities and total split rate H_{m-1}.
for i in range(1, 15):
    for j in range(1, 15):
        check(beta(i, j) == beta(j, i), "beta symmetry")
for m in range(2, 18):
    total = Fraction(0)
    for i in range(1, m):
        # oriented subsets, each at rate B(i,m-i)/2
        total += Fraction(comb(m, i), 2) * beta(i, m - i)
    check(total == harmonic(m - 1), "CTCS total rate")

# Exact finite-partition test of Lebesgue preservation by t -> b*t mod 1.
for r in range(1, 9):
    b = 2**r
    for den in range(2, 16):
        for a in range(0, den):
            for c in range(a + 1, den + 1):
                u = Fraction(a, den)
                v = Fraction(c, den)
                total = Fraction(0)
                for k in range(b):
                    total += (Fraction(k) + v) / b - (Fraction(k) + u) / b
                check(total == v - u, "preimage length")

# Independent exact polynomial-moment pushforward checks.
for r in range(1, 9):
    b = 2**r
    for m in range(0, 18):
        total = sum((branch_moment(b, m, k) for k in range(b)), Fraction(0))
        check(total == Fraction(1, m + 1), "polynomial moment")

# Exact r=1 pullback formulas and a noninjectivity witness.
for x in [Fraction(1, 4), Fraction(1, 3), Fraction(2, 5), Fraction(1, 2),
          Fraction(3, 5), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5),
          Fraction(5, 6)]:
    y = tau_r1(x)
    check(Fraction(0) < y < Fraction(1), "paintbox probability")
check(tau_r1(Fraction(1, 2)) == Fraction(1, 2), "left fixed endpoint")
check(tau_r1(Fraction(2, 3)) == Fraction(1, 2), "noninjective witness")
check(tau_r1(Fraction(4, 5)) == Fraction(4, 5), "right fixed endpoint")
check(tau_r1(Fraction(3, 4)) == Fraction(9, 13), "second branch formula")
check(tau_r1(Fraction(3, 5)) == Fraction(9, 13), "first branch formula")

# Exact N=4 C086 witness.
ps = [tau_r1(Fraction(s, 4)) for s in range(1, 4)]
check(ps == [Fraction(1, 4), Fraction(1, 2), Fraction(9, 13)], "N=4 biases")
q13 = rate(4, ps, 1, 3)
q22 = rate(4, ps, 2, 2)
root = 4 * q13 + 3 * q22
pbal = 3 * q22 / root
check(q13 == Fraction(406041, 1827904), "q13")
check(q22 == Fraction(310519, 1827904), "q22")
check(root == Fraction(2555721, 1827904), "root rate")
check(pbal == Fraction(310519, 851907), "balanced root probability")
check(pbal - Fraction(3, 11) == Fraction(859988, 9370977), "separation from CTCS")
check(q13 / q22 == Fraction(406041, 310519), "scale-free split ratio")
check(q13 / q22 != Fraction(2, 1), "not CTCS split ratio")
check(pbal != Fraction(3, 11), "not CTCS root topology")

# Source CTCS(4) values independently from B(i,j).
src_q13 = beta(1, 3)
src_q22 = beta(2, 2)
src_root = 4 * src_q13 + 3 * src_q22
src_pbal = 3 * src_q22 / src_root
check(src_q13 == Fraction(1, 3), "source q13")
check(src_q22 == Fraction(1, 6), "source q22")
check(src_root == Fraction(11, 6), "source root rate")
check(src_pbal == Fraction(3, 11), "source balanced probability")

# Separation from the immediately preceding deterministic C084 witness.
check(pbal != Fraction(1682121, 4572893), "distinct from C084 at N=4")

# Exact complexity arithmetic for r_N=floor((log_2 N)/2), N>=4.
# floor(log_2 N)=bit_length-1, so r_N=(bit_length-1)//2.
for N in range(4, 5000):
    r = max(1, (N.bit_length() - 1) // 2)
    b = 2**r
    check(b * b <= N, "b_N^2 <= N")
    check(b <= N, "branch count <= N")
    check(Fraction(b, N) <= Fraction(1, b), "b_N/N <= 1/b_N")

print("STATUS=ALL_EXACT_CHECKS_PASS")
print(f"ASSERTIONS={ASSERTIONS}")
print("N4_BIASES=1/4,1/2,9/13")
print(f"N4_Q13={q13}")
print(f"N4_Q22={q22}")
print(f"N4_ROOT_RATE={root}")
print(f"N4_BALANCED_PROB={pbal}")
print(f"N4_BALANCED_MINUS_CTCS={pbal - Fraction(3,11)}")
print(f"N4_SPLIT_RATIO={q13/q22}")