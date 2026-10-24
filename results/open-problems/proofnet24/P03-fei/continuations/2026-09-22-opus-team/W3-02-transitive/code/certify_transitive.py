"""Standalone certificate for a balanced transitive-symmetric function and the lower bound it gives.

Usage: python certify_transitive.py TABLE.npy GENS.json
  TABLE.npy : int8 array of length 2^n with entries +-1 (bit i of the index is coordinate i, -1 = true)
  GENS.json : list of permutations of [n] (perm[i] = image of i) generating the claimed symmetry group

Checks, with exact integer arithmetic: f(x o g) = f(x) for every generator; the generated group is
transitive on [n]; f is balanced; the integer Walsh transform W(S) = sum_x f(x) chi_S(x).
Then I = sum |S| W(S)^2 / 4^n exactly (a rational), and H = sum (W^2/4^n) log2(4^n / W^2) is enclosed in
an mpmath interval (iv) with 60 decimal digits.  Prints H, I, H/(I-1).

Consequence (amplification): the self-compositions f^(k) are invariant under the iterated wreath
product of the group, which is transitive on the n^k leaves, and H(f^(k))/I(f^(k)) -> H(f)/(I(f)-1).
"""
import sys, json
from fractions import Fraction
import numpy as np
from mpmath import iv, mp


def walsh_int(f):
    a = [int(v) for v in f]
    N = len(a)
    h = 1
    while h < N:
        for i in range(0, N, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def main():
    tab = np.load(sys.argv[1]).astype(int).tolist()
    gens = json.load(open(sys.argv[2]))
    N = len(tab)
    n = N.bit_length() - 1
    assert 1 << n == N and all(v in (1, -1) for v in tab)
    for g in gens:
        assert sorted(g) == list(range(n))
        for x in range(N):
            y = 0
            for i in range(n):
                if (x >> i) & 1:
                    y |= 1 << g[i]
            assert tab[y] == tab[x], "not invariant"
    seen = {0}; fr = [0]
    while fr:
        nf = []
        for i in fr:
            for g in gens:
                if g[i] not in seen:
                    seen.add(g[i]); nf.append(g[i])
        fr = nf
    assert len(seen) == n, "group not transitive"
    assert sum(tab) == 0, "not balanced"
    W = walsh_int(tab)
    D = N * N  # 4^n
    I = Fraction(sum(bin(S).count('1') * W[S] ** 2 for S in range(N)), D)
    iv.dps = 60
    H = iv.mpf(0)
    for S in range(N):
        w2 = W[S] ** 2
        if w2:
            H += iv.mpf(w2) / D * (iv.log(iv.mpf(D)) - iv.log(iv.mpf(w2))) / iv.log(iv.mpf(2))
    R = H / (iv.mpf(I.numerator) / I.denominator - 1)
    mp.dps = 30
    print("n =", n, " generators:", len(gens), " invariant: yes  transitive: yes  balanced: yes")
    print("I =", I, "=", float(I))
    print("H in [%s, %s]" % (mp.nstr(mp.mpf(H.a.a), 40), mp.nstr(mp.mpf(H.b.b), 40)))
    print("H/(I-1) in [%s, %s]" % (mp.nstr(mp.mpf(R.a.a), 40), mp.nstr(mp.mpf(R.b.b), 40)))


if __name__ == '__main__':
    main()
