"""Numaro's 18-input gate g at an arbitrary product bias.

Conventions.  Truth table T[x] in {+1,-1}, bit i of x is coordinate i, bit value 1 <-> x_i = -1 <-> "true".
Input i is true with probability p_i; mu_i = E x_i = 1 - 2 p_i; V_i = 1 - mu_i^2 = 4 p_i (1 - p_i).
Biased orthonormal basis phi_i = (x_i - mu_i)/sqrt(V_i).  For one coordinate and a pair of values
(a at x_i = +1, b at x_i = -1) the two coefficients are

    c0 = (1 - p) a + p b,        c1 = sqrt(p (1 - p)) (a - b).

Applying this on every axis gives Ghat_mu(T) for all T (a biased Walsh-Hadamard transform, O(n 2^n)).
Then Htilde = sum_T Ghat^2 log2(1/Ghat^2), It_i = sum_{T ni i} Ghat^2, Pr[G true] = (1 - Ghat(empty))/2.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy")
N = 18


def load_table():
    t = np.load(TABLE).astype(np.float64)
    assert t.shape == (1 << N,)
    return t


def biased_spectrum(table, p):
    """Ghat_mu(T) as a flat array indexed like the truth table (bit i of the index <-> i in T)."""
    n = N
    a = table.reshape((2,) * n)      # C order: axis k <-> bit n-1-k
    for i in range(n):
        ax = n - 1 - i
        pi = float(p[i])
        if pi == 0.5:
            s0 = 0.5; s1 = 0.5
            lo = np.take(a, 0, axis=ax); hi = np.take(a, 1, axis=ax)
            c0 = s0 * lo + s1 * hi
            c1 = 0.5 * (lo - hi)
        else:
            lo = np.take(a, 0, axis=ax); hi = np.take(a, 1, axis=ax)
            c0 = (1.0 - pi) * lo + pi * hi
            c1 = np.sqrt(pi * (1.0 - pi)) * (lo - hi)
        a = np.stack([c0, c1], axis=ax)
    return a.reshape(-1)


def phi_sum(w):
    w = w[w > 0]
    return float(-(w * np.log2(w)).sum())


_bits = None


def bit_masks():
    global _bits
    if _bits is None:
        idx = np.arange(1 << N, dtype=np.int64)
        _bits = [((idx >> i) & 1).astype(bool) for i in range(N)]
    return _bits


def evaluate(table, p):
    """Return (Htilde, It[18], p_out) of g at input truth-probabilities p."""
    c = biased_spectrum(table, p)
    w = c * c
    Ht = phi_sum(w)
    bm = bit_masks()
    It = np.array([w[bm[i]].sum() for i in range(N)])
    pout = 0.5 * (1.0 - c[0])
    return Ht, It, pout


def h2(v):
    v = np.asarray(v, dtype=float)
    out = np.zeros_like(v)
    m = (v > 0) & (v < 1)
    vm = v[m]
    out[m] = -vm * np.log2(vm) - (1 - vm) * np.log2(1 - vm)
    return out


if __name__ == "__main__":
    from fractions import Fraction
    t = load_table()
    # unbiased spectrum and exact checks
    c = biased_spectrum(t, [0.5] * N)
    W = np.rint(c * (1 << N)).astype(np.int64)
    assert np.abs(c * (1 << N) - W).max() < 1e-6
    assert int((W * W).sum()) == (1 << N) ** 2
    idx = np.arange(1 << N)
    pc = np.array([bin(x).count("1") for x in range(1 << N)])
    I = Fraction(int((W * W * pc).sum()), (1 << N) ** 2)
    print("I(g) =", I, float(I))
    H = phi_sum(c * c)
    print("H(g) = %.15f   H/(I-1) = %.15f" % (H, H / float(I - 1)))
    for i in range(N):
        print("  ghat({%d}) = %s" % (i, Fraction(int(W[1 << i]), 1 << N)), end="")
    print()
    print("ghat(empty) =", W[0], " ghat({0,9}) =", Fraction(int(W[(1 << 0) | (1 << 9)]), 1 << N))
    # validation point from CONTEXT section 3
    p = [0.5] * N; p[0] = 3 / 8
    Ht, It, pout = evaluate(t, p)
    print("p_0 = 3/8: p_out = %.12f (967/2048 = %.12f)" % (pout, 967 / 2048))
    print("  It_0 = %.15f (855/4096 = %.15f)" % (It[0], 855 / 4096))
    print("  sum_{i>=1} It_i = %.15f (465/256 = %.15f)" % (It[1:].sum(), 465 / 256))
    print("  Htilde = %.16f (6.7442547370563132664)" % Ht)
