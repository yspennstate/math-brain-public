#!/usr/bin/env python3
"""Rigorous balanced-transposition barrier for the source-valid n=18 FEI gate.

For the exact balanced prime gate f, certify that every balanced truth-table
transposition (flip one +1 cell and one -1 cell) strictly DECREASES
    H(f) - C*(I(f)-1)
at C = 6.5218512.

Entropy logarithms are enclosed by rational atanh series.  All reported
inequalities are then integer fixed-point inequalities.
"""
from fractions import Fraction
from hashlib import sha256
import numpy as np

N = 1 << 18
DIM = 18
SCALE = 10**18
C = Fraction(4076157, 625000)  # 6.5218512 exactly
EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"

TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
     "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

def fwht(a):
    a = np.array(a, dtype=np.int64, copy=True)
    h = 1
    n = len(a)
    while h < n:
        a = a.reshape(-1, 2*h)
        x = a[:, :h].copy()
        y = a[:, h:].copy()
        a[:, :h] = x + y
        a[:, h:] = x - y
        a = a.reshape(n)
        h <<= 1
    return a

def interval_fwht(lo, hi):
    lo = np.array(lo, dtype=np.int64, copy=True)
    hi = np.array(hi, dtype=np.int64, copy=True)
    h = 1
    n = len(lo)
    while h < n:
        lo = lo.reshape(-1, 2*h)
        hi = hi.reshape(-1, 2*h)
        lx, hx = lo[:, :h].copy(), hi[:, :h].copy()
        ly, hy = lo[:, h:].copy(), hi[:, h:].copy()
        lo[:, :h], hi[:, :h] = lx + ly, hx + hy
        lo[:, h:], hi[:, h:] = lx - hy, hx - ly
        lo, hi = lo.reshape(n), hi.reshape(n)
        h <<= 1
    return lo, hi

def reconstruct():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for m in masks:
        assert not (seen & m)
        assert m.bit_count() == 2
        seen |= m
        hosts.append([x for x in range(512) if (m >> x) & 1])
    core = np.array([1 if (base >> x) & 1 else 0 for x in range(512)], dtype=np.int8)
    g = np.tile(core, (1 << 9, 1))
    hm = np.arange(1 << 9, dtype=np.int64)
    for j, cells in enumerate(hosts):
        active = (hm & (1 << j)) != 0
        g[np.ix_(active, np.array(cells, dtype=int))] = 1
    signed = np.where(g.ravel() == 1, -1, 1).astype(np.int64)
    got = sha256(",".join(map(str, signed)).encode()).hexdigest()
    assert got == EXPECTED_SHA
    assert signed.sum() == 0
    return signed

def ln_interval_unit(num, den, terms=50):
    assert den <= num <= 2*den
    t = Fraction(num-den, num+den)
    s = Fraction(0)
    tp = t
    for j in range(terms):
        s += tp / (2*j+1)
        tp *= t*t
    lo = 2*s
    if t == 0:
        return lo, lo
    first = t**(2*terms+1)
    rem = 2*first / (2*terms+1) / (1-t*t)
    return lo, lo + rem

LN2_LO, LN2_HI = ln_interval_unit(2, 1)

def h_interval(w):
    z = abs(int(w))
    if z == 0:
        return Fraction(0), Fraction(0)
    k = (N // z).bit_length() - 1
    while z*(1 << (k+1)) <= N:
        k += 1
    while z*(1 << k) > N:
        k -= 1
    den = z*(1 << k)
    lq_lo, lq_hi = ln_interval_unit(N, den)
    log_lo = Fraction(k) + lq_lo / LN2_HI
    log_hi = Fraction(k) + lq_hi / LN2_LO
    fac = Fraction(2*z*z, N*N)
    return fac*log_lo, fac*log_hi

def floor_scaled(x):
    return (x.numerator*SCALE) // x.denominator

def ceil_scaled(x):
    return -((-x.numerator*SCALE) // x.denominator)

def main():
    f = reconstruct()
    W = fwht(f)
    ids = np.arange(N, dtype=np.uint32)
    pc8 = np.array([i.bit_count() for i in range(256)], dtype=np.int64)
    lev = pc8[ids & 255] + pc8[(ids >> 8) & 255] + pc8[(ids >> 16) & 255]

    assert W[0] == 0
    J = int(np.dot(lev, W*W))
    assert Fraction(J, N*N) == Fraction(261, 128)

    hb, mb, nb = {}, {}, {}
    for w0 in np.unique(W):
        w = int(w0)
        h0l, h0u = h_interval(w)
        hpl, hpu = h_interval(w+4)
        hml, hmu = h_interval(w-4)
        ul, uu = hpl-h0u, hpu-h0l
        vl, vu = hml-h0u, hmu-h0l
        ml, mu = (ul+vl)/2, (uu+vu)/2
        nl, nu = (vl-uu)/2, (vu-ul)/2
        hb[w] = (floor_scaled(h0l), ceil_scaled(h0u))
        mb[w] = (floor_scaled(ml), ceil_scaled(mu))
        nb[w] = (floor_scaled(nl), ceil_scaled(nu))

    hlo = np.empty(N, np.int64); hhi = np.empty(N, np.int64)
    mlo = np.empty(N, np.int64); mhi = np.empty(N, np.int64)
    nlo = np.empty(N, np.int64); nhi = np.empty(N, np.int64)
    for w, (a,b) in hb.items():
        mask = W == w
        hlo[mask], hhi[mask] = a, b
        a,b = mb[w]; mlo[mask], mhi[mask] = a,b
        a,b = nb[w]; nlo[mask], nhi[mask] = a,b

    Hlo, Hhi = int(hlo.sum()), int(hhi.sum())
    cap = C * Fraction(133,128)
    cap_floor, cap_ceil = floor_scaled(cap), ceil_scaled(cap)
    root_slack_lo = Hlo - cap_ceil
    root_slack_hi = Hhi - cap_floor
    assert root_slack_hi < 0

    Mmlo, Mmhi = interval_fwht(mlo, mhi)
    Nmlo, Nmhi = interval_fwht(nlo, nhi)
    Lhat = fwht(lev)
    Khat = fwht(lev*W)

    diff_hi = int(Mmhi[0]) - Mmlo
    oddm_hi = -np.floor_divide(-diff_hi, 2)
    oddlev = ((int(Lhat[0]) - Lhat)//2).astype(np.int64)
    cterm_floor = {}
    for ol in np.unique(oddlev):
        cterm_floor[int(ol)] = floor_scaled(C*16*int(ol)/Fraction(N*N))
    CElo = np.array([cterm_floor[int(x)] for x in oddlev], dtype=np.int64)
    Ehi = oddm_hi - CElo
    max_E_nonzero = int(Ehi[1:].max())
    argmax_E = 1 + int(np.argmax(Ehi[1:]))

    halfN_hi = -np.floor_divide(-Nmhi, 2)
    halfN_lo = np.floor_divide(Nmlo, 2)
    kt_floor, kt_ceil = {}, {}
    for k in np.unique(Khat):
        term = C*4*int(k)/Fraction(N*N)
        kt_floor[int(k)] = floor_scaled(term)
        kt_ceil[int(k)] = ceil_scaled(term)
    Qlo = halfN_lo + np.array([kt_floor[int(k)] for k in Khat], dtype=np.int64)
    Qhi = halfN_hi + np.array([kt_ceil[int(k)] for k in Khat], dtype=np.int64)
    q_range_hi = int(Qhi.max()) - int(Qlo.min())

    transposition_change_hi = max_E_nonzero + q_range_hi
    child_slack_hi = root_slack_hi + transposition_change_hi

    assert max_E_nonzero < 0
    assert transposition_change_hi < 0
    assert child_slack_hi < 0

    print("PASS")
    print("truth_sha256 =", EXPECTED_SHA)
    print("source_I = 261/128")
    print("source_cap_slack_upper =", root_slack_hi, "/ 10^18")
    print("source_cap_slack_upper_decimal = %.18g" % (root_slack_hi/SCALE))
    print("max_E_nonzero_upper =", max_E_nonzero, "/ 10^18")
    print("argmax_E_nonzero =", argmax_E, "hamming_weight =", int(lev[argmax_E]))
    print("Q_range_upper =", q_range_hi, "/ 10^18")
    print("transposition_change_upper =", transposition_change_hi, "/ 10^18")
    print("transposition_change_upper_decimal = %.18g" % (transposition_change_hi/SCALE))
    print("all_transposed_cap_slack_upper =", child_slack_hi, "/ 10^18")
    print("all_transposed_cap_slack_upper_decimal = %.18g" % (child_slack_hi/SCALE))
    print("balanced_transposition_barrier = True")

if __name__ == "__main__":
    main()
