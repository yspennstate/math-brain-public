from fractions import Fraction
from math import comb, factorial
from itertools import product

assertions = 0


def check(cond, msg="assertion failed"):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(msg)


def H(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def clock_rate(N, s):
    # harmonic-grid proposal rate at x=s/N
    return Fraction(N, 2 * s * (N - s))


def beta_rate(i, j):
    return Fraction(factorial(i - 1) * factorial(j - 1), factorial(i + j - 1))


def iid_mark_prob(x, i, j):
    # specified unordered i|j support: two color orientations
    return x**i * (1 - x)**j + x**j * (1 - x)**i


def occ_mark_prob_mixture(M, x, i, j):
    # Count via the empirical red-box fraction P=R/M, R~Bin(M,x).
    ans = Fraction(0)
    for r in range(M + 1):
        prob_r = Fraction(comb(M, r), 1) * x**r * (1 - x) ** (M - r)
        p = Fraction(r, M)
        ans += prob_r * (p**i * (1 - p)**j + p**j * (1 - p)**i)
    return ans


def occ_mark_prob_direct(M, x, i, j):
    # Independent exact enumeration of all label->box assignments and all box colors.
    m = i + j
    ans = Fraction(0)
    assignment_prob = Fraction(1, M**m)
    for assignment in product(range(M), repeat=m):
        for colors in product((0, 1), repeat=M):
            nred = sum(colors)
            color_prob = x**nred * (1 - x) ** (M - nred)
            y = [colors[b] for b in assignment]
            orient1 = all(y[t] == 1 for t in range(i)) and all(
                y[t] == 0 for t in range(i, m)
            )
            orient2 = all(y[t] == 0 for t in range(i)) and all(
                y[t] == 1 for t in range(i, m)
            )
            if orient1 or orient2:
                ans += assignment_prob * color_prob
    return ans


def occ_rate(N, M, i, j):
    return sum(
        (
            clock_rate(N, s)
            * occ_mark_prob_mixture(M, Fraction(s, N), i, j)
            for s in range(1, N)
        ),
        Fraction(0),
    )


def iid_rate(N, i, j):
    return sum(
        (
            clock_rate(N, s) * iid_mark_prob(Fraction(s, N), i, j)
            for s in range(1, N)
        ),
        Fraction(0),
    )


# 1. Harmonic-grid proposal normalization.
for N in range(2, 16):
    check(
        sum((clock_rate(N, s) for s in range(1, N)), Fraction(0)) == H(N - 1),
        f"clock normalization failed N={N}",
    )

# 2. Count the specified split law in two genuinely different ways.
for M in range(2, 5):
    for N in range(3, 8):
        for s in range(1, N):
            x = Fraction(s, N)
            for m in range(2, 5):
                for i in range(1, m):
                    j = m - i
                    a = occ_mark_prob_mixture(M, x, i, j)
                    b = occ_mark_prob_direct(M, x, i, j)
                    check(a == b, f"two-count mismatch M,N,s,i,j={(M,N,s,i,j)}: {a} != {b}")
            # exact pair-separation law at one mark
            check(
                occ_mark_prob_mixture(M, x, 1, 1)
                == 2 * x * (1 - x) * (1 - Fraction(1, M)),
                f"pair mark formula failed M,N,s={(M,N,s)}",
            )

# 3. Exact pair generator and U060 generator bounds in small cases.
for N in range(3, 12):
    for M in range(2, 6):
        check(
            occ_rate(N, M, 1, 1)
            == Fraction(N - 1, N) * (1 - Fraction(1, M)),
            f"pair generator failed N,M={(N,M)}",
        )
        for m in range(2, min(6, N + 1)):
            for i in range(1, m):
                j = m - i
                diff_occ_iid = abs(occ_rate(N, M, i, j) - iid_rate(N, i, j))
                collision_bound = Fraction(comb(m, 2), M) * Fraction(N - 1, N)
                check(
                    diff_occ_iid <= collision_bound,
                    f"collision generator bound failed N,M,i,j={(N,M,i,j)}: "
                    f"{diff_occ_iid}>{collision_bound}",
                )

                # The simple Lipschitz Riemann-sum bound used in the growing-k proof.
                diff_iid_beta = abs(iid_rate(N, i, j) - beta_rate(i, j))
                riemann_bound = Fraction(m - 1, N)
                check(
                    diff_iid_beta <= riemann_bound,
                    f"Riemann bound failed N,i,j={(N,i,j)}: {diff_iid_beta}>{riemann_bound}",
                )

# 4. Exact finite witness for C080 at N=4, M_4=floor(sqrt(4))=2.
N = 4
M = 2
q13 = occ_rate(N, M, 1, 3)
q22 = occ_rate(N, M, 2, 2)
check(q13 == Fraction(3, 32), f"N=4 q13={q13}")
check(q22 == Fraction(3, 32), f"N=4 q22={q22}")
root_rate = 4 * q13 + 3 * q22
check(root_rate == Fraction(21, 32), f"N=4 root rate={root_rate}")
balanced_root_prob = 3 * q22 / root_rate
check(balanced_root_prob == Fraction(3, 7), f"N=4 balanced prob={balanced_root_prob}")
check(balanced_root_prob != Fraction(3, 11), "C080 accidentally matches CTCS(4) root topology")
check(balanced_root_prob != 1, "C080 accidentally matches C079 N=4 root topology")
check(q13 > 0, "C080 must differ from C079 zero singleton rate")

print(f"assertions = {assertions}")
print("N4 M =", M)
print("N4 specified 1|3 rate =", q13)
print("N4 specified 2|2 rate =", q22)
print("N4 total root rate =", root_rate)
print("N4 balanced root probability =", balanced_root_prob)
print("source CTCS(4) balanced root probability =", Fraction(3, 11))
print("C079 N=4 balanced root probability = 1")
print("ALL_EXACT_CHECKS_PASS")
