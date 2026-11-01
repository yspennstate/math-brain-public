"""Exact Walsh-Hadamard tools for FEI witness-cost experiments (W-witness-cost route).

Conventions: inputs x in {-1,1}^n encoded as bitmasks (bit k = 1 means x_k = -1),
truth table T[x] in {-1,+1}. Integer Walsh transform W[S] = sum_x T[x] chi_S(x),
fhat(S) = W[S] / 2^n exactly (Fraction when needed). chi_S(x) = (-1)^{popcount(S & x)}.
"""
from fractions import Fraction
import math


def fwht_int(vals):
    """In-place style integer fast Walsh-Hadamard transform; returns new list."""
    a = list(vals)
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectrum(T):
    """Return (n, W) with W[S] integer Walsh coefficient; fhat(S) = W[S]/2^n."""
    N = len(T)
    n = N.bit_length() - 1
    assert 1 << n == N
    return n, fwht_int(T)


def popcount(x):
    return bin(x).count("1")


def entropy_influence_exact(T):
    """Return (H_float, I_Fraction, Var_Fraction, masses dict S->Fraction)."""
    n, W = spectrum(T)
    N2 = 1 << (2 * n)
    masses = {}
    I = Fraction(0)
    H = 0.0
    var = Fraction(0)
    for S, w in enumerate(W):
        if w == 0:
            continue
        m = Fraction(w * w, N2)
        masses[S] = m
        I += popcount(S) * m
        if S != 0:
            var += m
        H += float(m) * math.log2(float(1 / m))
    return H, I, var, masses


def influences(T):
    n = len(T).bit_length() - 1
    out = []
    for k in range(n):
        cnt = 0
        for x in range(len(T)):
            if T[x] != T[x ^ (1 << k)]:
                cnt += 1
        out.append(Fraction(cnt, len(T)))
    return out


def is_unate_regular(T):
    """Check the paper's 'regular': unate, and after orienting to monotone the coordinates
    admit a total desirability order. Returns (ok, orientation signs, order) where order lists
    relevant coordinates from most to least desirable. Exhaustive check (small n only)."""
    n = len(T).bit_length() - 1
    N = len(T)
    # orientation: coordinate k is increasing (+1) if T(x with x_k=+1) >= T(x with x_k=-1) always
    sign = []
    relevant = []
    for k in range(n):
        up = down = False
        for x in range(N):
            if x & (1 << k):
                continue  # x has x_k = +1 (bit 0)
            a, b = T[x], T[x | (1 << k)]  # a: x_k=+1, b: x_k=-1
            if a > b:
                up = True
            elif a < b:
                down = True
        if up and down:
            return False, None, None
        if up:
            sign.append(1)
            relevant.append(k)
        elif down:
            sign.append(-1)
            relevant.append(k)
        else:
            sign.append(0)

    # monotone orientation: define value with coordinate k flipped if sign=-1
    def val(x):
        y = x
        for k in range(n):
            if sign[k] == -1:
                y ^= (1 << k)
        return T[y]
    # desirability: j >= i iff f(x_{j=1,i=-1}) >= f(x_{j=-1,i=1}) for all others (in oriented coords)
    def geq(j, i):
        for x in range(N):
            if x & ((1 << i) | (1 << j)):
                continue
            # x has x_i = x_j = +1 (bits 0); build x_{j=+1,i=-1} and x_{j=-1,i=+1}
            a = val(x | (1 << i))
            b = val(x | (1 << j))
            if a < b:
                return False
        return True
    infl = influences(T)
    order = sorted(relevant, key=lambda k: -infl[k])
    for p in range(len(order)):
        for q in range(p + 1, len(order)):
            if not geq(order[p], order[q]):
                return False, sign, None
    return True, sign, order
