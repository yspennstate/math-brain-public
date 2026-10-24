"""Exact sign of B_i - K* Inf_i via prime-exponent linear forms in logs (code path independent of A082).
A sum e_p ln p with integer e_p is zero iff every e_p is zero (unique factorization);
otherwise its sign is decided by an outward-rounded mpmath interval at 400 bits."""
from collections import Counter
import mpmath

_fc = {}


def factor(m):
    if m in _fc:
        return _fc[m]
    c = Counter()
    x = m
    p = 2
    while p * p <= x:
        while x % p == 0:
            c[p] += 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        c[x] += 1
    _fc[m] = c
    return c


def linear_form(pairs, const=(8, 5, -9)):
    """pairs: (a, b, mult) with a=W_T^2, b=W_{T+i}^2 (integers), multiplicity mult.
    Returns (e, L): e = integer exponents with
    sum_p e_p ln p = ln2 * 2 * [4^n B_i - K* 4^n Inf_i]  when const=(8,5,-9) encodes 2K* = 8+5log2 5-9log2 3.
    L = 4^n Inf_i."""
    e = Counter()
    L = 0
    for a, b, m in pairs:
        s = a + b
        if s == 0:
            continue
        for p, k in factor(s).items():
            e[p] += 2 * m * s * k
        if a:
            for p, k in factor(a).items():
                e[p] -= 2 * m * a * k
        if b:
            for p, k in factor(b).items():
                e[p] -= 2 * m * b * k
        L += m * b
    c2, c5, c3 = const
    e[2] -= c2 * L
    e[5] -= c5 * L
    e[3] -= c3 * L
    return {p: k for p, k in e.items() if k != 0}, L


def sign_form(e, prec=400):
    if not e:
        return 0
    iv = mpmath.iv
    iv.prec = prec
    tot = iv.mpf(0)
    for p, k in e.items():
        tot += iv.mpf(k) * iv.log(iv.mpf(p))
    if tot.a > 0:
        return 1
    if tot.b < 0:
        return -1
    raise RuntimeError('interval did not separate; raise precision')


def sign_pairs_vs_kstar(pairs):
    e, L = linear_form(pairs)
    return sign_form(e), e
