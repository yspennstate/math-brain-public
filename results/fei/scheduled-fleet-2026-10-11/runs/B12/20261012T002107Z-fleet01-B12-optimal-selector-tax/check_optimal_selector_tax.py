#!/usr/bin/env python3
"""Exact/interval certificate for the optimal constant-branch selector tax.

The analytic reduction is exact.  Rational intervals certify the stationary
point bracket, the sharp constant bracket, and the displayed 10-bit witness.
The finite truth-table audit through four data bits is exhaustive.  No
randomness is used.
"""

from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from math import log2
from time import perf_counter


def fwht(values):
    out = list(values)
    h = 1
    while h < len(out):
        for i in range(0, len(out), 2 * h):
            for j in range(i, i + h):
                a, b = out[j], out[j + h]
                out[j], out[j + h] = a + b, a - b
        h *= 2
    return out


# Closed rational intervals represented by pairs (lower, upper).
def I(x, y=None):
    x = Q(x)
    return (x, x if y is None else Q(y))


def iadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def ineg(x):
    return (-x[1], -x[0])


def isub(x, y):
    return iadd(x, ineg(y))


def imul(x, y):
    z = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return (min(z), max(z))


def idiv(x, y):
    assert 0 < y[0] <= y[1]
    return imul(x, (1 / y[1], 1 / y[0]))


def ipow2(x):
    assert x[0] >= 0
    return (x[0] * x[0], x[1] * x[1])


def ln_unit_bounds(q, terms=90):
    """Bounds ln(q) after range reduction has put 1 <= q < 2."""
    assert Q(1) <= q < Q(2)
    t = (q - 1) / (q + 1)
    partial = 2 * sum(t ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
    tail = 2 * t ** (2 * terms + 1) / ((2 * terms + 1) * (1 - t * t))
    return partial, partial + tail


def ln2_bounds(terms=120):
    t = Q(1, 3)
    partial = 2 * sum(t ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
    tail = 2 * t ** (2 * terms + 1) / ((2 * terms + 1) * (1 - t * t))
    return partial, partial + tail


LN2 = ln2_bounds()


def ln_bounds(q):
    """Rigorous rational enclosure of ln(q), q>0, using powers of two."""
    q = Q(q)
    assert q > 0
    y = q
    k = 0
    while y < 1:
        y *= 2
        k += 1
    while y >= 2:
        y /= 2
        k -= 1
    lo, hi = ln_unit_bounds(y)
    if k >= 0:
        return lo - k * LN2[1], hi - k * LN2[0]
    return lo - k * LN2[0], hi - k * LN2[1]


def iln(x):
    assert x[0] > 0
    return (ln_bounds(x[0])[0], ln_bounds(x[1])[1])


def A_interval(p):
    one = I(1)
    ln2 = LN2
    om = isub(one, p)
    twom = isub(one, imul(I(2), p))
    term1 = imul(I(-2), imul(ipow2(om), iln(om)))
    term2 = imul(I(-2), imul(ipow2(p), iln(p)))
    term3 = imul(I(4), imul(ln2, imul(p, om)))
    term4 = imul(ipow2(twom), iln(twom))
    return iadd(iadd(term1, term2), iadd(term3, term4))


def C_interval(p):
    return idiv(A_interval(p), imul(p, LN2))


def F_point(p):
    """Interval for F=p A'-A on 0<p<1/2."""
    p = I(p)
    one = I(1)
    p2 = ipow2(p)
    om = isub(one, p)
    tm = isub(one, imul(I(2), p))
    t1 = imul(I(2), imul(isub(one, p2), iln(om)))
    t2 = imul(I(-2), imul(p2, iln(p)))
    t3 = imul(I(-4), imul(p2, LN2))
    t4 = imul(ineg(isub(one, imul(I(4), p2))), iln(tm))
    return iadd(iadd(t1, t2), iadd(t3, t4))


def entropy_float(walsh, size):
    ans = 0.0
    for w in walsh:
        if w:
            mass = (w * w) / (size * size)
            ans += mass * log2(1 / mass)
    return ans


def entropy_interval(walsh, size):
    ans = I(0)
    for w in walsh:
        if w:
            mass = Q(w * w, size * size)
            term = idiv(imul(I(mass), ineg(ln_bounds(mass))), LN2)
            ans = iadd(ans, term)
    return ans


def influence(walsh, size):
    return sum(Q(alpha.bit_count() * w * w, size * size)
               for alpha, w in enumerate(walsh))


def tax_formula_float(p):
    m = 1 - 2 * p
    e = lambda q: 0.0 if q == 0 else q * log2(1 / q)
    tax = e((1 - p) ** 2) + e(p * p) + 4 * p * (1 - p) - 0.5 * e(m * m)
    return tax / p


start = perf_counter()

# Rigorous location of the unique stationary point, relying on the analytic
# uniqueness proof archived with this checker.
p_lo = Q(22944127, 100000000)
p_hi = Q(22944128, 100000000)
Flo = F_point(p_lo)
Fhi = F_point(p_hi)
assert Flo[0] > 0
assert Fhi[1] < 0

# Direct interval evaluation on the root box certifies a useful upper bound.
Cstar_box = C_interval((p_lo, p_hi))
assert Cstar_box[1] < Q(4872322, 1000000)

# A concrete genuine Boolean near-extremizer: D=-1 on the first 235 points of
# the lexicographically indexed 10-cube, and +1 elsewhere.
N = 1024
k = 235
p_wit = Q(k, N)
D = [-1] * k + [1] * (N - k)
Dw = fwht(D)
K = [1] * N + D
Kw = fwht(K)

assert Dw[0] == 554
assert Counter(map(abs, Dw)) == Counter({2: 768, 6: 128, 10: 64, 22: 32, 42: 28, 470: 3, 554: 1})
assert Counter(map(abs, Kw)) == Counter({2: 1536, 6: 256, 10: 128, 22: 64, 42: 56, 470: 7, 1578: 1})
ID = influence(Dw, N)
IK = influence(Kw, 2 * N)
Ix = sum(Q(w * w, (2 * N) ** 2) for alpha, w in enumerate(Kw) if alpha & N)
assert ID == Q(277, 256)
assert IK == Q(789, 1024)
assert Ix == p_wit

Cwit = C_interval(I(p_wit))
assert Cwit[0] > Q(4872321, 1000000)
HD = entropy_interval(Dw, N)
HK = entropy_interval(Kw, 2 * N)
ratioK = idiv(HK, I(IK))

# Exhaustive structural/numerical audit through four data bits.
audited = 0
max_small = (-1.0, None, None)
for n in range(1, 5):
    size = 1 << n
    for mask in range(1 << size):
        vals = [-1 if (mask >> i) & 1 else 1 for i in range(size)]
        p = vals.count(-1) / size
        if p == 0:
            continue
        wD = fwht(vals)
        wK = fwht([1] * size + vals)
        HDf = entropy_float(wD, size)
        HKf = entropy_float(wK, 2 * size)
        Ixf = sum(w * w for alpha, w in enumerate(wK) if alpha & size) / (2 * size) ** 2
        direct = (HKf - 0.5 * HDf) / Ixf
        formula = tax_formula_float(p)
        assert abs(direct - formula) < 2e-12
        assert Q(sum(w * w for alpha, w in enumerate(wK) if alpha & size), (2 * size) ** 2) == Q(vals.count(-1), size)
        audited += 1
        if direct > max_small[0]:
            max_small = (direct, n, vals.count(-1))

assert audited == 65808
assert max_small[1:] == (2, 1)  # first occurrence; p=1/4 in all larger cubes
assert Q(4867, 1000) < C_interval(I(Q(1, 4)))[0]

elapsed = perf_counter() - start


def dec(q, digits=45):
    # Display only; all assertions above use Fractions.
    getcontext().prec = digits
    return str(Decimal(q.numerator) / Decimal(q.denominator))


print("scope: all constant-versus-Boolean fresh-selector splices")
print("randomness: none")
print(f"stationary root bracket: [{float(p_lo):.8f}, {float(p_hi):.8f}]")
print(f"F(left) lower > 0: {dec(Flo[0])}")
print(f"F(right) upper < 0: {dec(Fhi[1])}")
print(f"C_star interval lower: {dec(Cstar_box[0])}")
print(f"C_star interval upper: {dec(Cstar_box[1])}")
print(f"10-bit witness density: {k}/{N}")
print(f"10-bit witness tax lower: {dec(Cwit[0])}")
print(f"10-bit witness tax upper: {dec(Cwit[1])}")
print(f"exact mean(D)=277/512, I(D)={ID}, I_x(K)={Ix}, I(K)={IK}")
print(f"H(D) interval: [{dec(HD[0])}, {dec(HD[1])}]")
print(f"H(K) interval: [{dec(HK[0])}, {dec(HK[1])}]")
print(f"H(K)/I(K) interval: [{dec(ratioK[0])}, {dec(ratioK[1])}]")
print(f"exhaustive Boolean functions audited (n=1..4, excluding D=1): {audited}")
print(f"small-cube maximum: {max_small[0]:.15f} at first n={max_small[1]}, negatives={max_small[2]}")
print(f"runtime_seconds: {elapsed:.6f}")
print("certified: C_star<4.872322 and the 235/1024 Boolean witness has tax>4.872321")
print("PASS")
