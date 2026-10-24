from fractions import Fraction
from itertools import product, combinations
import math


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, math.isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def least_prime_ge(n):
    q = n
    while not is_prime(q):
        q += 1
    return q


def K_of_N(N):
    return min(N, max(2, math.isqrt(N) + 1))


def eval_poly(coeffs, a, q):
    ans = 0
    power = 1
    for c in coeffs:
        ans = (ans + c * power) % q
        power = (power * a) % q
    return ans


ASSERTIONS = 0

def check(condition, message=''):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def G(q, i, j):
    ans = Fraction(0, 1)
    for u in range(1, q):
        x = Fraction(u, q)
        ans += x ** (i - 1) * (1 - x) ** (j - 1)
    return ans / (q - 1)


def beta_rate(i, j):
    return Fraction(math.factorial(i - 1) * math.factorial(j - 1),
                    math.factorial(i + j - 1))


def realizes_unordered_split(row, u, A, B):
    return ((all(row[t] < u for t in A) and all(row[t] >= u for t in B)) or
            (all(row[t] >= u for t in A) and all(row[t] < u for t in B)))


# Basic parameter checks.
for N in range(2, 13):
    q = least_prime_ge(N)
    K = K_of_N(N)
    check(is_prime(q))
    check(q >= N)
    check(2 <= K <= N)

# Exact OA projection multiplicities, exact threshold cylinders, and exact
# harmonic-grid specified-split rates for small N.
for N in range(2, 8):
    q = least_prime_ge(N)
    K = K_of_N(N)
    rows = [tuple(eval_poly(coeffs, a, q) for a in range(N))
            for coeffs in product(range(q), repeat=K)]
    check(len(rows) == q ** K)

    for b in range(1, K + 1):
        for cols in combinations(range(N), b):
            counts = {}
            for row in rows:
                pat = tuple(row[c] for c in cols)
                counts[pat] = counts.get(pat, 0) + 1
            check(len(counts) == q ** b)
            target = q ** (K - b)
            for pat in product(range(q), repeat=b):
                check(counts.get(pat, 0) == target)

            for u in range(1, q):
                x = Fraction(u, q)
                for bits in product((0, 1), repeat=b):
                    observed_count = 0
                    for row in rows:
                        observed = tuple(1 if row[c] < u else 0 for c in cols)
                        if observed == bits:
                            observed_count += 1
                    red = sum(bits)
                    expected = x ** red * (1 - x) ** (b - red)
                    check(Fraction(observed_count, len(rows)) == expected)

    for b in range(2, K + 1):
        cols = tuple(range(b))
        for i in range(1, b):
            j = b - i
            A = set(cols[:i])
            B = set(cols[i:])
            rate = Fraction(0, 1)
            for u in range(1, q):
                x = Fraction(u, q)
                num = sum(realizes_unordered_split(row, u, A, B) for row in rows)
                rate += Fraction(num, 1) / (2 * (q - 1) * q ** K * x * (1 - x))
            check(rate == G(q, i, j),
                  'N={} i={} j={} got={} expected={}'.format(N, i, j, rate, G(q, i, j)))
    check(G(q, 1, 1) == 1)

# Exact rational spot checks that the harmonic grid approaches the beta rates.
for i, j in [(1, 2), (2, 2), (2, 3), (3, 3)]:
    for q in [5, 11, 23, 47]:
        err = abs(G(q, i, j) - beta_rate(i, j))
        check(err <= Fraction(10, q))

# Full N=4 finite non-equivalence witness.
N = 4
q = 5
K = 3
rows = [tuple(eval_poly(coeffs, a, q) for a in range(N))
        for coeffs in product(range(q), repeat=K)]


def specified_split_rate(A):
    A = set(A)
    B = set(range(N)) - A
    rate = Fraction(0, 1)
    for u in range(1, q):
        x = Fraction(u, q)
        num = sum(realizes_unordered_split(row, u, A, B) for row in rows)
        rate += Fraction(num, 1) / (2 * (q - 1) * q ** K * x * (1 - x))
    return rate


singleton_rates = [specified_split_rate({a}) for a in range(4)]
balanced_rates = [specified_split_rate(A) for A in ({0, 1}, {0, 2}, {0, 3})]
for r in singleton_rates:
    check(r == Fraction(4, 15))
for r in balanced_rates:
    check(r == Fraction(7, 30))
total_nontrivial_rate = sum(singleton_rates, Fraction()) + sum(balanced_rates, Fraction())
check(total_nontrivial_rate == Fraction(53, 30))
root_P_2v2 = sum(balanced_rates, Fraction()) / total_nontrivial_rate
check(root_P_2v2 == Fraction(21, 53))
check(root_P_2v2 != Fraction(3, 11))

# Every pair has exactly unit separation rate at N=4.
for a, b in combinations(range(4), 2):
    rate = Fraction(0, 1)
    for u in range(1, q):
        x = Fraction(u, q)
        num = sum(((row[a] < u) != (row[b] < u)) for row in rows)
        rate += Fraction(num, 1) / (2 * (q - 1) * q ** K * x * (1 - x))
    check(rate == 1)

print('R11-I0054-C068 Reed-Solomon OA exact self-check')
print('ASSERTIONS={}'.format(ASSERTIONS))
print('N4_q={}'.format(q))
print('N4_K={}'.format(K))
print('N4_singleton_each={}'.format(singleton_rates[0]))
print('N4_balanced_each={}'.format(balanced_rates[0]))
print('N4_total_nontrivial_rate={}'.format(total_nontrivial_rate))
print('N4_root_P_2v2={}'.format(root_P_2v2))
print('DTCS4_root_P_2v2=3/11')
print('ALL_EXACT_CHECKS_PASS')
