"""Independent evaluation of the constants and scalar facts used in the F5 proof."""
import math
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 40

# --- constants of Theorem 1 / Corollary 2
B = 3 * mp.sqrt(3 / mp.pi)
L1 = 2 * mp.log(B) + 2
print("B  =", mp.nstr(B, 20))
print("L1 =", mp.nstr(L1, 20))


def Cof(Lval):
    a = (1 + mp.sqrt(1 + 4 / Lval)) / 2
    val = 3 + (1 + mp.log(a / (a - 1)) + a * Lval) / mp.log(2)
    # confirm it is the minimum by a direct 1-d minimisation
    g = lambda t: 3 + (1 + mp.log(t / (t - 1)) + t * Lval) / mp.log(2)
    amin = mp.findroot(lambda t: mp.diff(g, t), a)
    return a, val, g(amin)


a, C1, C1b = Cof(L1)
print("a* =", mp.nstr(a, 20), " C =", mp.nstr(C1, 20), " (direct min:", mp.nstr(C1b, 20), ")")
for k in [2, 3, 4, 16, 100]:
    _, Ck, _ = Cof(L1 + 2 * mp.log(k))
    print(f"C_{k} =", mp.nstr(Ck, 8))

# --- Lemma 1: C(m, m//2)/2^m <= sqrt(2/(pi m)), exact rationals for m <= 3000, then log-gamma to 10^6
worst = 0.0
for m in range(1, 3001):
    lhs = Fraction(math.comb(m, m // 2), 2 ** m)
    rhs2 = Fraction(2, 1) / (Fraction(m, 1))  # compare squares: lhs^2 <= 2/(pi m)
    val = float(lhs * lhs * m) * math.pi / 2  # = lhs^2 / (2/(pi m))
    worst = max(worst, val)
for m in range(3001, 10 ** 6, 997):
    lg = math.lgamma(m + 1) - math.lgamma(m // 2 + 1) - math.lgamma(m - m // 2 + 1) - m * math.log(2)
    val = math.exp(2 * lg) * m * math.pi / 2
    worst = max(worst, val)
print("Lemma 1: max over m of [C(m,m/2)/2^m]^2 / (2/(pi m)) =", worst, "(must be <= 1)")

# --- Lemma 2: min(1, sqrt(2/(pi m))) <= (2/sqrt pi)(m+1)^-1/2 ; E[1/(m+1)] formula and <= 1/c
worst = 0.0
for m in range(0, 10 ** 5):
    lhs = 1.0 if m == 0 else min(1.0, math.sqrt(2 / (math.pi * m)))
    worst = max(worst, lhs / ((2 / math.sqrt(math.pi)) / math.sqrt(m + 1)))
print("Lemma 2 step: max ratio =", worst, "(must be <= 1)")
worst = 0.0
for N in [2, 3, 5, 10, 57, 400]:
    for c in [0.01, 0.3, 1, 2.5, N / 2, N]:
        if c > N:
            continue
        p = mp.mpf(c) / N
        E = mp.fsum(mp.binomial(N - 1, m) * p ** m * (1 - p) ** (N - 1 - m) / (m + 1) for m in range(N))
        formula = (1 - (1 - p) ** N) / c
        assert abs(E - formula) < mp.mpf(10) ** -30, (N, c, E, formula)
        worst = max(worst, float(E * c))
print("E[1/(m+1)] formula verified; max c*E[1/(m+1)] =", worst, "(must be <= 1)")

# --- Lemma 3: (1 - 1/(3K))^{-K} <= 3/2 for K >= 1 (nonincreasing)
prev = None
worst = 0.0
K = mp.mpf(1)
while K < 1e6:
    v = (1 - 1 / (3 * K)) ** (-K)
    worst = max(worst, float(v / mp.mpf(1.5)))
    if prev is not None:
        assert v <= prev + mp.mpf(10) ** -30
    prev = v
    K *= mp.mpf(1.01)
print("Lemma 3: max (1-1/3K)^-K / 1.5 over K in [1,1e6] =", worst, "; nonincreasing: yes")
# the tail integral
integ = mp.quad(lambda u: min(1, B * mp.e ** (-u / 2)), [0, 2 * mp.log(B), mp.inf])
print("Lemma 3 integral =", mp.nstr(integ, 20), " vs L1 =", mp.nstr(L1, 20))

# --- Lemma 5 elementary inequality, analytic form: alpha log(1/alpha) >= (1-alpha) log(1/(1-alpha)) on (0,1/2]
worst = -1e9
N = 2_000_00
for t in range(1, N + 1):
    al = 0.5 * t / N
    eps = 4 * al * (1 - al)
    lhs = (1 - math.sqrt(1 - eps)) * math.log2(2 / (1 - math.sqrt(1 - eps))) if eps < 1 else 1.0
    rhs = 0.5 * eps * math.log2(1 / eps) + eps
    worst = max(worst, rhs - lhs)
print("Lemma 5: max over grid of RHS - LHS =", worst, "(must be <= 0; equality at eps = 1)")
# (1-eps) log2(1/(1-eps)) <= 2 eps
worst = max(((1 - e) * math.log2(1 / (1 - e))) / (2 * e) for e in [i / 10 ** 5 for i in range(1, 10 ** 5)])
print("Lemma 5: max (1-eps)log(1/(1-eps))/(2eps) =", worst)

# --- Lemma 6: sum_s min(1,(k/s)^a) <= k a/(a-1), e_k <= (sum)^k/k!, k! >= (k/e)^k
worst = 0.0
for aa in [1.05, 1.2006422748, 1.5, 3.0]:
    for k in [1, 2, 3, 7, 30, 200]:
        for n in [k, 2 * k, 10 * k + 3, 1000]:
            if n < k:
                continue
            s = sum(min(1.0, (k / t) ** aa) for t in range(1, n + 1))
            worst = max(worst, s / (k * aa / (aa - 1)))
print("Lemma 6: max sum q / (k a/(a-1)) =", worst, "(must be <= 1)")
