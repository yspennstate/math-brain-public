#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from math import factorial
from functools import lru_cache
import bisect

MAX_N = 7
MAX_DEG = 2 * MAX_N


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out[: MAX_DEG + 1]


def poly_mul(a, b):
    out = [Fraction(0)] * (min(MAX_DEG, len(a) + len(b) - 2) + 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if i + j > MAX_DEG:
                break
            out[i + j] += x * y
    return out


def poly_scale(a, c):
    return [c * x for x in a]


def bessel_I_series(order):
    # I_order(2y) = sum_{r>=0} y^(2r+order)/(r!(r+order)!).
    out = [Fraction(0)] * (MAX_DEG + 1)
    r = 0
    while 2 * r + order <= MAX_DEG:
        out[2 * r + order] = Fraction(1, factorial(r) * factorial(r + order))
        r += 1
    return out


def sign_perm(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def toeplitz_bessel_det_series(m):
    if m == 0:
        out = [Fraction(0)] * (MAX_DEG + 1)
        out[0] = 1
        return out
    out = [Fraction(0)] * (MAX_DEG + 1)
    for p in permutations(range(m)):
        term = [Fraction(1)]
        for i in range(m):
            term = poly_mul(term, bessel_I_series(abs(i - p[i])))
        out = poly_add(out, poly_scale(term, sign_perm(p)))
    return out


def lis_len(p):
    tails = []
    for a in p:
        j = bisect.bisect_left(tails, a)
        if j == len(tails):
            tails.append(a)
        else:
            tails[j] = a
    return len(tails)


def u(m, n):
    return sum(lis_len(p) <= m for p in permutations(range(n)))


def check_gessel():
    for m in (1, 2, 3):
        d = toeplitz_bessel_det_series(m)
        for n in range(MAX_N + 1):
            got = d[2 * n]
            want = Fraction(u(m, n), factorial(n) ** 2)
            assert got == want, (m, n, got, want)
    print("GESSEL_COEFFICIENT_CHECK_PASS m=1,2,3 n=0..7")


@lru_cache(None)
def dim(lam):
    n = sum(lam)
    if n == 0:
        return 1
    hooks = 1
    for i, row in enumerate(lam):
        for j in range(row):
            below = sum(1 for r in lam[i + 1 :] if r > j)
            hooks *= row - j + below
    return factorial(n) // hooks


def addable(lam):
    L = list(lam)
    ans = []
    for i in range(len(L)):
        if i == 0 or L[i] + 1 <= L[i - 1]:
            M = L.copy()
            M[i] += 1
            ans.append(tuple(M))
    ans.append(tuple(L + [1]))
    return list(dict.fromkeys(ans))


def transition(lam, mu):
    n = sum(lam)
    return Fraction(dim(mu), (n + 1) * dim(lam))


def check_nonmarkov():
    # Exact Plancherel-growth DP through time 6 suffices.
    # State stores T2,T3,T4, first times row 1 reaches lengths 2,3,4.
    dp = {((), None, None, None): Fraction(1)}
    for n in range(6):
        nd = {}
        for (lam, t2, t3, t4), p in dp.items():
            for mu in addable(lam):
                q = p * transition(lam, mu)
                ts = [t2, t3, t4]
                old = lam[0] if lam else 0
                new = mu[0]
                if new > old:
                    for idx, k in enumerate((2, 3, 4)):
                        if ts[idx] is None and new >= k:
                            ts[idx] = n + 1
                key = (mu, *ts)
                nd[key] = nd.get(key, Fraction(0)) + q
        dp = nd
        assert sum(dp.values()) == 1

    def cond(b, c, d):
        den = num = Fraction(0)
        for (lam, t2, t3, t4), p in dp.items():
            if t2 == b and t3 == c:
                den += p
                if t4 == d:
                    num += p
        return num / den

    a = cond(2, 5, 6)
    b = cond(4, 5, 6)
    assert a == Fraction(19, 66), a
    assert b == Fraction(5, 18), b
    assert a != b
    print(
        "PLANCHEREL_HITTING_NONMARKOV_PASS",
        "P(T4=6|T3=5,T2=2)=19/66",
        "P(T4=6|T3=5,T2=4)=5/18",
    )


def check_k2_tail():
    # Source formula P(B2=b)=1/[b(b-2)!] = 1/(b-1)! - 1/b!.
    # Its tail telescopes: P(B2>n)=1/n!, exactly the m=1 LIS law.
    for n in range(1, 10):
        finite = sum(Fraction(1, b * factorial(b - 2)) for b in range(2, n + 1))
        tail = 1 - finite
        assert tail == Fraction(1, factorial(n)), (n, tail)
    print("K2_SOURCE_TAIL_CHECK_PASS n=1..9")


if __name__ == "__main__":
    check_k2_tail()
    check_gessel()
    check_nonmarkov()
    print("ALL_EXACT_CHECKS_PASS")
