"""Standalone certificate for H, I, J = H/(I-1) of a balanced Boolean function given as a truth table string.

Exact: integer Walsh transform (pure Python ints), I as an exact rational, mean exactly 0.
H: python-flint arb balls at 256 bits, H = sum_S p_S log2(1/p_S), p_S = W_S^2 / N^2 (exact rationals).
Also checks composition-primality by exhaustive cofactor counting (pure Python), independent of core.py.

Usage: python certify_J.py <table-string of 0/1, bit x = f(x) true> [threshold]
"""
import sys
from fractions import Fraction
import flint

flint.ctx.prec = 256


def walsh(vals):
    a = list(vals)
    N = len(a)
    h = 1
    while h < N:
        for s in range(0, N, 2 * h):
            for j in range(s, s + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def certify(tab, thr=None):
    N = len(tab)
    n = N.bit_length() - 1
    assert 1 << n == N
    f = [-1 if c == '1' else 1 for c in tab]
    W = walsh(f)
    assert sum(w * w for w in W) == N * N  # Parseval, exact
    mean = Fraction(W[0], N)
    I = sum(Fraction(bin(S).count('1') * W[S] * W[S], N * N) for S in range(N))
    H = flint.arb(0)
    ln2 = flint.arb(2).log()
    for S in range(N):
        if W[S] == 0:
            continue
        p = flint.arb(W[S] * W[S]) / flint.arb(N * N)
        H += -p * p.log() / ln2
    out = dict(n=n, mean=mean, I=I, H=H)
    if mean == 0 and I > 1:
        J = H / (flint.arb(I.numerator) / flint.arb(I.denominator) - 1)
        out['J'] = J
    # relevant variables and primality (exhaustive cofactor count)
    rel = [i for i in range(n) if any(f[x] != f[x ^ (1 << i)] for x in range(N))]
    k = len(rel)
    prime = k >= 3
    if prime:
        for mask in range(1, 1 << k):
            A = [rel[j] for j in range(k) if (mask >> j) & 1]
            if len(A) < 2 or len(A) > k - 1:
                continue
            B = [i for i in range(n) if i not in A]
            cof = set()
            for a in range(1 << len(A)):
                xa = sum(1 << A[j] for j in range(len(A)) if (a >> j) & 1)
                row = tuple(f[xa | sum(1 << B[j] for j in range(len(B)) if (b >> j) & 1)] for b in range(1 << len(B)))
                cof.add(row)
                if len(cof) > 2:
                    break
            if len(cof) <= 2:
                prime = False
                break
    out['relevant'] = rel
    out['prime'] = prime
    if thr is not None and 'J' in out:
        out['J_exceeds_threshold'] = bool(out['J'] > flint.arb(thr))
    return out


if __name__ == '__main__':
    tab = sys.argv[1]
    thr = sys.argv[2] if len(sys.argv) > 2 else None
    r = certify(tab, thr)
    for k, v in r.items():
        print(k, '=', v)
