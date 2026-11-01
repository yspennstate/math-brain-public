from fractions import Fraction
from itertools import combinations, product

ASSERTIONS = 0


def check(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)


def H(n):
    return sum((Fraction(1, r) for r in range(1, n + 1)), Fraction(0))


def weight_sum(q):
    return sum((Fraction(1, u * (q - u)) for u in range(1, q)), Fraction(0))


def coeffs_all(q, d):
    return product(range(q), repeat=d)


def eval_poly(coeffs, x, q):
    y = 0
    xp = 1
    for a in coeffs:
        y = (y + a * xp) % q
        xp = (xp * x) % q
    return y


def alpha(q, u):
    return Fraction(1, u * (q - u)) / weight_sum(q)


# Exact harmonic normalization W_q = 2 H_{q-1}/q.
for q0 in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
    check(weight_sum(q0) == Fraction(2, q0) * H(q0 - 1), f"W identity q={q0}")

# Exact k-wise evaluation uniformity at q=7,d=3, checked for every
# 1-, 2-, and 3-set of evaluation points and every output vector.
q = 7
d = 3
polys = list(coeffs_all(q, d))
for k in [1, 2, 3]:
    for xs in combinations(range(q), k):
        counts = {}
        for c in polys:
            ys = tuple(eval_poly(c, x, q) for x in xs)
            counts[ys] = counts.get(ys, 0) + 1
        expected = q ** (d - k)
        check(len(counts) == q ** k, f"support xs={xs}")
        for ys in product(range(q), repeat=k):
            check(counts.get(ys, 0) == expected, f"uniform xs={xs} ys={ys}")

# Thresholding preserves the exact conditional iid Bernoulli cylinders.
for k in [1, 2, 3]:
    for xs in combinations(range(q), k):
        for u in range(1, q):
            p = Fraction(u, q)
            for bits in product([0, 1], repeat=k):  # 1 = red
                cnt = 0
                for c in polys:
                    got = tuple(1 if eval_poly(c, x, q) < u else 0 for x in xs)
                    if got == bits:
                        cnt += 1
                r = sum(bits)
                check(
                    Fraction(cnt, len(polys)) == p ** r * (1 - p) ** (k - r),
                    f"threshold xs={xs},u={u},bits={bits}",
                )

# Pair normalization and exact grid identity at q=7.
Wq = weight_sum(q)
P11 = sum(
    (alpha(q, u) * 2 * Fraction(u, q) * (1 - Fraction(u, q)) for u in range(1, q)),
    Fraction(0),
)
lam = 1 / P11
check(P11 == Fraction(120, 343), f"P11 {P11}")
check(lam == Fraction(343, 120), f"lambda {lam}")
check(lam == Fraction(q, q - 1) * H(q - 1), f"lambda harmonic {lam}")

for i in range(1, 4):
    for j in range(1, 4 - i):
        mix = sum(
            (
                alpha(q, u)
                * (
                    Fraction(u, q) ** i * (1 - Fraction(u, q)) ** j
                    + Fraction(u, q) ** j * (1 - Fraction(u, q)) ** i
                )
                for u in range(1, q)
            ),
            Fraction(0),
        )
        grid = Fraction(1, q - 1) * sum(
            (
                Fraction(u, q) ** (i - 1)
                * (1 - Fraction(u, q)) ** (j - 1)
                for u in range(1, q)
            ),
            Fraction(0),
        )
        check(lam * mix == grid, f"grid i={i} j={j}")

# Finite nonexchangeability witness for the actual C055 rule at N=q=7,d=2.
d = 2
polys2 = list(coeffs_all(q, d))


def unordered_split_prob(A, B):
    A = set(A)
    B = set(B)
    visible = A | B
    ans = Fraction(0)
    for u in range(1, q):
        cnt = 0
        for c in polys2:
            red = {x for x in visible if eval_poly(c, x, q) < u}
            if red == A or red == B:
                cnt += 1
        ans += alpha(q, u) * Fraction(cnt, len(polys2))
    return ans


pA = unordered_split_prob((0, 1), (2, 3))
pB = unordered_split_prob((0, 1), (2, 4))
check(pA == Fraction(64, 1029), str(pA))
check(pB == Fraction(18, 343), str(pB))
check(pA - pB == Fraction(10, 1029), str(pA - pB))
check(lam * pA == Fraction(8, 45), str(lam * pA))
check(lam * pB == Fraction(3, 20), str(lam * pB))
check(lam * (pA - pB) == Fraction(1, 36), str(lam * (pA - pB)))

print("ASSERTIONS", ASSERTIONS)
print("W7", Wq)
print("P11_7", P11)
print("LAMBDA_7", lam)
print("WITNESS_A_RAW", pA)
print("WITNESS_B_RAW", pB)
print("WITNESS_A_NORMALIZED", lam * pA)
print("WITNESS_B_NORMALIZED", lam * pB)
print("NORMALIZED_GAP", lam * (pA - pB))
print("ALL_EXACT_CHECKS_PASS")
