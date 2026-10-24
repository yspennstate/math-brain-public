from math import isqrt

P = 523
Q = 617
N = 9


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def order_mod(a, p):
    x = 1
    for k in range(1, p):
        x = x * a % p
        if x == 1:
            return k
    raise AssertionError("no order")


assert is_prime(P)
assert is_prime(Q)
assert order_mod(Q % P, P) == 9
assert order_mod(19, P) == 9
assert order_mod(3, P) == 58
assert pow(3, 29, P) == P - 1

K = sorted({pow(19, k, P) for k in range(9)})
assert len(K) == 9
assert (Q % P) in K

cosets = []
seen = set()
for j in range(58):
    C = sorted({pow(3, j, P) * k % P for k in K})
    assert len(C) == 9
    assert not (set(C) & seen)
    seen.update(C)
    cosets.append(C)
assert seen == set(range(1, P))
for j in range(58):
    assert {(-x) % P for x in cosets[j]} == set(cosets[(j + 29) % 58])

# f(x)=x^9+86x^8+451x^7+136x^6+546x^5+271x^4+31x^3+490x^2+531x+235
MOD = [235, 531, 490, 31, 271, 546, 136, 451, 86, 1]  # low -> high


def trim(a):
    a = [x % Q for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def psub(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % Q
    return trim(out)


def pmul_raw(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % Q
    return trim(out)


def pdivmod(a, b):
    a = trim(a[:])
    b = trim(b[:])
    assert b != [0]
    if len(a) < len(b):
        return [0], a
    inv = pow(b[-1], -1, Q)
    qq = [0] * (len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] * inv % Q
        qq[d] = c
        for i, bi in enumerate(b):
            a[i + d] = (a[i + d] - c * bi) % Q
        a = trim(a)
    return trim(qq), a


def pmod(a):
    return pdivmod(a, MOD)[1]


def pmul_poly(a, b):
    return pmod(pmul_raw(a, b))


def ppow(a, e):
    r = [1]
    b = pmod(a)
    while e:
        if e & 1:
            r = pmul_poly(r, b)
        b = pmul_poly(b, b)
        e //= 2
    return r


def pgcd(a, b):
    a = trim(a)
    b = trim(b)
    while b != [0]:
        _, r = pdivmod(a, b)
        a, b = b, r
    inv = pow(a[-1], -1, Q)
    return trim([(inv * x) % Q for x in a])


X = [0, 1]
assert ppow(X, Q ** N) == X
assert pgcd(psub(ppow(X, Q ** 3), X), MOD) == [1]

ZERO = (0,) * N
ONE = (1,) + (0,) * (N - 1)
ALPHA = (0, 1) + (0,) * (N - 2)


def fadd(a, b):
    return tuple((a[i] + b[i]) % Q for i in range(N))


def fmul(a, b):
    conv = [0] * (2 * N - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            conv[i + j] = (conv[i + j] + x * y) % Q
    for d in range(2 * N - 2, N - 1, -1):
        c = conv[d] % Q
        if c:
            for k in range(N):
                conv[d - N + k] = (conv[d - N + k] - c * MOD[k]) % Q
    return tuple(x % Q for x in conv[:N])


def fpow(a, e):
    r = ONE
    b = a
    while e:
        if e & 1:
            r = fmul(r, b)
        b = fmul(b, b)
        e //= 2
    return r


zeta = fpow(ALPHA, (Q ** N - 1) // P)
assert zeta != ONE
assert fpow(zeta, P) == ONE

zpows = [ONE]
for _ in range(1, P):
    zpows.append(fmul(zpows[-1], zeta))

etas = []
for C in cosets:
    s = ZERO
    for a in C:
        s = fadd(s, zpows[a])
    # Q mod P is in K, so Frobenius-Q permutes each K-coset and fixes the period.
    assert fpow(s, Q) == s
    assert all(v == 0 for v in s[1:])
    etas.append(s[0])
assert sum(etas) % Q == Q - 1


def rank_mod(A, p):
    A = [row[:] for row in A]
    r = 0
    n = len(A)
    m = len(A[0])
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] % p), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c] % p, -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] % p:
                fac = A[i][c] % p
                A[i] = [(A[i][j] - fac * A[r][j]) % p for j in range(m)]
        r += 1
        if r == n:
            break
    return r


M = [[etas[(i + j) % 58] for j in range(58)] for i in range(58)]
assert rank_mod(M, Q) == 58

# Both surviving d=9 row-sum profiles have the required zero-frequency identity.
profiles = [(37, 19, 19, 1), (17, 17, 17, 35)]
for rs in profiles:
    assert sum(r * r for r in rs) == 4 * P

# Exact lifting lemma.
# For any +/-1 sequence A of odd length P and nonzero shift s,
# PAF_A(s)=P-2D(s), where D(s) is the Hamming distance from A to its shift.
# Product_x A(x)A(x+s)=1, so (-1)^D=1 and D is even. Therefore
# PAF_A(s) == P (mod 4). The sum R(s) of four such PAFs is divisible by 4.
#
# If the 29 K-orbit character equations over F_Q hold, then at every nonzero
# 523rd-root character t we have sum_i Ahat_i(t)Ahat_i(-t)=4P mod Q.
# The row-sum identity supplies the same equality at t=0. Inverse DFT over
# F_(Q^9) therefore gives R(s)=0 mod Q for every s != 0.
# Since |R(s)| <= 4P=2092 and R(s) is divisible by both 4 and 617,
# while 4*617=2468>2092, necessarily R(s)=0 exactly.
assert 4 * Q > 4 * P
allowed = [r for r in range(-4 * P, 4 * P + 1) if r % 4 == 0 and r % Q == 0]
assert allowed == [0]

print("P", P)
print("Q", Q)
print("prime_Q", is_prime(Q))
print("ord_523(617)", order_mod(Q % P, P))
print("617_mod_523_in_K", Q % P, (Q % P) in K)
print("K", K)
print("coset_count", len(cosets), "negation_shift", 29)
print("field_modulus_low_to_high", MOD)
print("zeta_order", P)
print("periods_F617", etas)
print("period_transform_rank_F617", rank_mod(M, Q))
print("row_sum_profiles", profiles)
print("row_sum_square_totals", [sum(r * r for r in rs) for rs in profiles])
print("residual_bound", 4 * P)
print("automatic_residual_divisor", 4)
print("four_times_617", 4 * Q)
print("bounded_multiples_of_4_and_617", allowed)
print("THEOREM_CHECK: the 29 F617 K-orbit character equations plus either fixed row-sum profile are sufficient for exact periodic complementarity")
print("ALL_EXACT_SPLIT617_LIFT_CHECKS_PASSED")
