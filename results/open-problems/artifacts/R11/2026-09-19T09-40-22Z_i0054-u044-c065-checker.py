from fractions import Fraction
from itertools import permutations
import math

ASSERTIONS = 0


def A(cond):
    global ASSERTIONS
    assert cond
    ASSERTIONS += 1


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


def primes_1mod4_up_to(B):
    return [p for p in range(5, B + 1) if p % 4 == 1 and is_prime(p)]


def legendre(s, p):
    s %= p
    if s == 0:
        return 0
    v = pow(s, (p - 1) // 2, p)
    return 1 if v == 1 else -1


def falling(a, r):
    z = 1
    for t in range(r):
        z *= a - t
    return z


def beta_rate(i, j):
    return Fraction(math.factorial(i - 1) * math.factorial(j - 1), math.factorial(i + j - 1))


def q_legendre(p, i, j, eps=Fraction(1, 2)):
    k = i + j
    den = falling(p, k)
    total = Fraction(0)
    for s in range(1, p):
        w = Fraction(1) + eps * legendre(s, p)
        intensity = Fraction(p, 2 * s * (p - s)) * w
        prob = Fraction(
            falling(s, i) * falling(p - s, j) + falling(s, j) * falling(p - s, i),
            den,
        )
        total += intensity * prob
    return total


def q_baseline(p, i, j):
    return q_legendre(p, i, j, Fraction(0))


def discrepancy(p, eps=Fraction(1, 2)):
    cur = 0
    best = 0
    for s in range(1, p):
        cur += legendre(s, p)
        best = max(best, abs(cur))
    return Fraction(abs(eps.numerator) * best, eps.denominator)


def direct_prob_specified(p, s, Aset, Bset, N=4):
    labels = list(range(N))
    total = 0
    hit = 0
    for images in permutations(range(p), N):
        phi = dict(zip(labels, images))
        for R in range(p):
            arc = {(R + t) % p for t in range(s)}
            left = {x for x in labels if phi[x] in arc}
            right = set(labels) - left
            total += 1
            if (left == Aset and right == Bset) or (left == Bset and right == Aset):
                hit += 1
    return Fraction(hit, total)


# Core exact algebra on many prime circles.
for p in primes_1mod4_up_to(197):
    total_character = 0
    for s in range(1, p):
        chi = legendre(s, p)
        A(chi in (-1, 1))
        A(legendre(p - s, p) == chi)  # chi(-1)=+1 for p == 1 mod 4
        total_character += chi
    A(total_character == 0)

    for i in range(1, 5):
        for j in range(1, 5):
            if i + j <= min(7, p):
                A(q_baseline(p, i, j) == beta_rate(i, j))

                # Exact finite-N moment representation of the generator defect.
                k = i + j
                lhs = q_legendre(p, i, j) - beta_rate(i, j)
                rhs = Fraction(0)
                for s in range(1, p):
                    h = Fraction(1, 2) * legendre(s, p)
                    rhs += h * falling(s - 1, i - 1) * falling(p - s - 1, j - 1)
                rhs *= Fraction(p, falling(p, k))
                A(lhs == rhs)

    A(q_legendre(p, 1, 1) == 1)


# Direct injection/arc enumeration for the N=4, p=5 finite witness.
p = 5
for s in range(1, p):
    d13 = direct_prob_specified(p, s, {0}, {1, 2, 3})
    f13 = Fraction(
        falling(s, 1) * falling(p - s, 3) + falling(s, 3) * falling(p - s, 1),
        falling(p, 4),
    )
    A(d13 == f13)

    d22 = direct_prob_specified(p, s, {0, 1}, {2, 3})
    f22 = Fraction(2 * falling(s, 2) * falling(p - s, 2), falling(p, 4))
    A(d22 == f22)

q11 = q_legendre(5, 1, 1)
q13 = q_legendre(5, 1, 3)
q22 = q_legendre(5, 2, 2)
root_balanced = Fraction(3) * q22 / (Fraction(4) * q13 + Fraction(3) * q22)
A(q11 == 1)
A(q13 == Fraction(5, 12))
A(q22 == Fraction(1, 12))
A(root_balanced == Fraction(3, 23))
A(root_balanced != Fraction(9, 17))  # preceding C064 witness
A(root_balanced != Fraction(3, 11))  # source DTCS(4) witness


# U043/U044 quantitative prefix-discrepancy bound on tested prime circles.
for p in primes_1mod4_up_to(401):
    D = discrepancy(p)
    for i in range(1, 4):
        for j in range(1, 4):
            k = i + j
            if k <= p:
                err = abs(q_legendre(p, i, j) - beta_rate(i, j))
                bound = Fraction((k - 1) * (2 ** k), p) * D
                A(err <= bound)

print("R11-I0054-U044/C065 exact self-check")
print(f"assertions = {ASSERTIONS}")
print(f"N4_p5_q11 = {q11}")
print(f"N4_p5_q13 = {q13}")
print(f"N4_p5_q22 = {q22}")
print(f"N4_C065_root_P_2v2 = {root_balanced}")
for p in primes_1mod4_up_to(61):
    D = discrepancy(p)
    print(f"prime={p} Delta={D} Delta_over_p={float(D / p):.12f}")
print("ALL_EXACT_CHECKS_PASS")
