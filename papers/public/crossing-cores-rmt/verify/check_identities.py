"""Independent arithmetic verification of every closed-form identity in
"Crossing cores, Gorenstein moment polytopes, and sharp volume gaps for random
Toeplitz and Hankel laws" (revision of 2026-08).

Everything here is re-derived from the paper's *formulas* with exact rational
arithmetic and compared against the paper's *printed* numbers.  No polytope
volumes are computed in this script (see check_volumes_spot.py for those); the
moment table (11.1) is taken as input where a check needs it, and is itself
re-derived by the separate full orbit sweep.

Run:  python check_identities.py
"""
from fractions import Fraction as Fr
from math import comb, factorial, exp

FAIL = []

def check(name, got, expect):
    ok = (got == expect)
    print(f"{'OK  ' if ok else 'FAIL'} {name}: got {got}" + ("" if ok else f"  expected {expect}"))
    if not ok:
        FAIL.append((name, got, expect))

def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r

def cat(k):
    return comb(2 * k, k) // (k + 1)

# ---------------------------------------------------------------- inputs
# Exact moments (paper Theorem 11.1); independently re-derived by the orbit sweep.
mT = {1: Fr(1), 2: Fr(8, 3), 3: Fr(11), 4: Fr(908, 15), 5: Fr(415),
      6: Fr(23840, 7), 7: Fr(325719, 10)}
mH = {1: Fr(1), 2: Fr(2), 3: Fr(11, 2), 4: Fr(281, 15), 5: Fr(2717, 36),
      6: Fr(1052, 3), 7: Fr(1331087, 720)}

# ------------------------------------------------- Section 6: primitive masses
def q(r, j):
    # q_{r,j} = (2r/(2r-j)) * C(2r-j, j), the j-edge matchings of the cycle C_{2r}
    return Fr(2 * r, 2 * r - j) * comb(2 * r - j, j)

def kappa_from_moments(m, r):
    # (6.5): kappa_r = sum_{k=2}^{r} (-1)^{r-k} q_{r,r-k} (m_{2k} - Cat_k)
    return sum((-1) ** (r - k) * q(r, r - k) * (m[k] - cat(k)) for k in range(2, r + 1))

kT_expect = {2: Fr(2, 3), 3: Fr(2), 4: Fr(178, 15), 5: Fr(253, 3),
             6: Fr(24798, 35), 7: Fr(206797, 30)}
kH_expect = {2: Fr(0), 3: Fr(1, 2), 4: Fr(11, 15), 5: Fr(131, 36),
             6: Fr(83, 5), 7: Fr(63907, 720)}
for r in range(2, 8):
    check(f"(6.6) kappa_{r}^T", kappa_from_moments(mT, r), kT_expect[r])
    check(f"(6.6) kappa_{r}^H", kappa_from_moments(mH, r), kH_expect[r])

# Round trip (6.2): m_{2k} = Cat_k + sum_{r=2}^{k} C(2k, k-r) kappa_r
for k in range(2, 8):
    for tag, m, kap in (("T", mT, kT_expect), ("H", mH, kH_expect)):
        rt = cat(k) + sum(comb(2 * k, k - r) * kap[r] for r in range(2, k + 1))
        check(f"(6.2) round-trip m_{2*k}^{tag}", rt, m[k])

# Corollary 6.5 lower bounds (nonnegative primitive retention)
for k in range(3, 8):
    lb = cat(k) + Fr(2, 3) * comb(2 * k, k - 2) + 2 * comb(2 * k, k - 3)
    check(f"Cor 6.5 lower bound T holds at k={k}", lb <= mT[k], True)
for k in range(4, 8):
    lb = cat(k) + Fr(1, 2) * comb(2 * k, k - 3) + Fr(11, 15) * comb(2 * k, k - 4)
    check(f"Cor 6.5 lower bound H holds at k={k}", lb <= mH[k], True)

# ------------------------------------- Section 12: reduced-core counts, Poisson
def cT(r):
    if r == 0:
        return 1
    if r == 1:
        return 0
    return sum((-1) ** j * q(r, j) * dfact(2 * r - 2 * j - 1) for j in range(0, r + 1))

def cH(r):
    if r == 0:
        return 1
    if r == 1:
        return 0
    return sum((-1) ** j * q(r, j) * factorial(r - j) for j in range(0, r + 1))

cT_expect = {2: 1, 3: 4, 4: 31, 5: 293, 6: 3326, 7: 44189}
cH_expect = {2: 0, 3: 1, 4: 2, 5: 13, 6: 80, 7: 579}
for r in range(2, 8):
    check(f"(12.1) c_{r}^T", cT(r), Fr(cT_expect[r]))
    check(f"(12.1) c_{r}^H", cH(r), Fr(cH_expect[r]))

# Direct enumeration cross-check of the reduced-core counts, r <= 6:
# reduced = no chord joining cyclically adjacent slots (no ear).
import itertools
def all_pairings(n2k):
    slots = list(range(n2k))
    def rec(avail):
        if not avail:
            yield ()
            return
        a = avail[0]
        for jx in range(1, len(avail)):
            b = avail[jx]
            for sub in rec(avail[1:jx] + avail[jx + 1:]):
                yield ((a, b),) + sub
    for pairs in rec(slots):
        pm = [0] * n2k
        for a, b in pairs:
            pm[a], pm[b] = b, a
        yield tuple(pm)

def is_reduced(pm):
    n = len(pm)
    return all(pm[i] != (i + 1) % n and pm[i] != (i - 1) % n for i in range(n))

def is_parity_mixing(pm):
    return all((i + pm[i]) % 2 == 1 for i in range(len(pm)))

for r in range(2, 7):
    cnt_t = cnt_h = 0
    for pm in all_pairings(2 * r):
        if is_reduced(pm):
            cnt_t += 1
            if is_parity_mixing(pm):
                cnt_h += 1
    check(f"direct enumeration c_{r}^T", cnt_t, cT_expect[r])
    check(f"direct enumeration c_{r}^H", cnt_h, cH_expect[r])

# (12.3) is a probability law: masses must sum to 1 (equivalently Thm 6.1 with F=1)
for k in range(3, 9):
    tot_T = sum(comb(2 * k, m) * cT(k - m) for m in range(0, k - 1)) + cat(k)
    check(f"(12.3) normalization T at k={k}", tot_T, dfact(2 * k - 1))
    tot_H = sum(comb(2 * k, m) * cH(k - m) for m in range(0, k - 1)) + cat(k)
    check(f"(12.3) normalization H at k={k}", tot_H, factorial(k))

# float of a ratio of huge integers without overflow
def fx(fr):
    fr = Fr(fr)
    a, b = fr.numerator, fr.denominator
    neg = a < 0
    a = abs(a)
    shift = max(a.bit_length(), b.bit_length()) - 512
    if shift > 0:
        a >>= shift
        b >>= shift
        if b == 0:
            return float("inf")
    val = a / b
    return -val if neg else val

# (12.7) first-order coefficients, numerically: r*(e * c_r/(2r-1)!! - 1) -> -3/4
r1, r2v = 400, 800
resid = lambda r: r * (fx(Fr(cT(r), dfact(2 * r - 1))) * exp(1) - 1.0)
a1, a2 = resid(r1), resid(r2v)
# Richardson: with resid = -3/4 + O(1/r), 2*a2 - a1 -> -3/4 faster
check("(12.7) Toeplitz 1st-order coeff ~ -3/4 (|err|<0.01)",
      abs((2 * a2 - a1) - (-0.75)) < 0.01, True)
residH = lambda r: r * (fx(Fr(cH(r), factorial(r))) * exp(2) - 1.0)
b1, b2 = residH(r1), residH(r2v)
check("(12.7) Hankel 1st-order coeff ~ -1 (|err|<0.01)",
      abs((2 * b2 - b1) - (-1.0)) < 0.01, True)

# (12.9) sharp TV constants: k * d_TV -> e^{-1} (T), 4 e^{-2} (H)
def dtv(k, kind):
    N = dfact(2 * k - 1) if kind == "T" else factorial(k)
    cfun = cT if kind == "T" else cH
    lam = 1.0 if kind == "T" else 2.0
    tot = 0.0
    # exact law masses
    masses = {}
    for m in range(0, k - 1):
        masses[m] = fx(Fr(comb(2 * k, m) * cfun(k - m), N))
    masses[k - 1] = 0.0
    masses[k] = fx(Fr(cat(k), N))
    pois = lambda m: (exp(-lam) * lam ** m / factorial(m)) if m <= 170 else 0.0
    allm = set(masses) | set(range(0, k + 40))
    return 0.5 * sum(abs(masses.get(m, 0.0) - pois(m)) for m in allm)

t300, t600 = 300 * dtv(300, "T"), 600 * dtv(600, "T")
h300, h600 = 300 * dtv(300, "H"), 600 * dtv(600, "H")
check("(12.9) lim k dTV(T) = e^-1 (Richardson |err|<0.01)",
      abs((2 * t600 - t300) - exp(-1)) < 0.01, True)
check("(12.9) lim k dTV(H) = 4e^-2 (Richardson |err|<0.01)",
      abs((2 * h600 - h300) - 4 * exp(-2)) < 0.01, True)

# (12.10) mean/variance first-order: E D_k^T = 1 + 1/k, Var = 1 + 3/(2k); H: 2+2/k, 2+4/k
def moments_D(k, kind):
    N = dfact(2 * k - 1) if kind == "T" else factorial(k)
    cfun = cT if kind == "T" else cH
    e1 = e2 = Fr(0)
    for m in range(0, k - 1):
        p = Fr(comb(2 * k, m) * cfun(k - m), N)
        e1 += m * p
        e2 += m * m * p
    p = Fr(cat(k), N)
    e1 += k * p
    e2 += k * k * p
    return fx(e1), fx(e2 - e1 * e1)

for kind, m0, v0, m1c, v1c in (("T", 1, 1, 1.0, 1.5), ("H", 2, 2, 2.0, 4.0)):
    ka, kb = 200, 400
    ea, va = moments_D(ka, kind)
    eb, vb = moments_D(kb, kind)
    check(f"(12.10) E D^{kind} 1/k-coeff ~ {m1c} (|err|<0.02)",
          abs(2 * kb * (eb - m0) - ka * (ea - m0) - m1c) < 0.02, True)
    check(f"(12.10) Var D^{kind} 1/k-coeff ~ {v1c} (|err|<0.05)",
          abs(2 * kb * (vb - v0) - ka * (va - v0) - v1c) < 0.05, True)

# ------------------------------------------ Section 13: cumulants and free ID
# classical cum4 (centered, unit variance): m4 - 3
check("cum4(gamma_T) = -1/3", mT[2] - 3, Fr(-1, 3))
check("cum4(gamma_H) = -1", mH[2] - 3, Fr(-1))

# free cumulants by the moment-cumulant recursion  m_n = sum_s r_s [z^{n-s}] M(z)^s
def free_cumulants(m_even, top, m_top_extra=None):
    """m_even: dict k -> m_{2k}. Returns dict n -> r_n for even n <= top.
    If m_top_extra is not None it is used as the (symbolic) value of m_top: we
    return the constant part, i.e. r_top computed with m_top = 0."""
    m = {0: Fr(1)}
    for k, v in m_even.items():
        m[2 * k] = v
    for n in range(1, top + 1):
        m.setdefault(n, Fr(0))
    if m_top_extra is not None:
        m[top] = Fr(0)
    # power series of M up to degree top
    M = [m.get(i, Fr(0)) for i in range(top + 1)]
    powers = {1: M[:]}
    for s in range(2, top + 1):
        prev = powers[s - 1]
        cur = [Fr(0)] * (top + 1)
        for i, a in enumerate(prev):
            if a == 0:
                continue
            for j in range(0, top + 1 - i):
                if M[j]:
                    cur[i + j] += a * M[j]
        powers[s] = cur
    r = {}
    for n in range(1, top + 1):
        acc = m[n]
        for s in range(1, n):
            if r.get(s):
                acc -= r[s] * powers[s][n - s]
        r[n] = acc
    return r

rH = free_cumulants(mH, 16)
check("free r2(H)", rH[2], Fr(1))
check("free r4(H)", rH[4], Fr(0))
check("free r6(H)", rH[6], Fr(1, 2))
check("free r8(H)", rH[8], Fr(11, 15))
check("Prop 13.2 det block = -1/4", rH[4] * rH[8] - rH[6] ** 2, Fr(-1, 4))

rT = free_cumulants(mT, 16)
r13 = {2: Fr(1), 4: Fr(2, 3), 6: Fr(2), 8: Fr(454, 45), 10: Fr(619, 9),
       12: Fr(546794, 945), 14: Fr(1546397, 270)}
for n, v in r13.items():
    check(f"(13.1) free r{n}(T)", rT[n], v)

# r16 with m16 unknown: r16 = m16 + const;  paper says r16 = m16 - 196536946/675
rT0 = free_cumulants(mT, 16, m_top_extra=0)
check("r16 = m16 - 196536946/675", rT0[16], Fr(-196536946, 675))

# conditional-positivity blocks from (r_{i+j})
def hankel_block(idx, r):
    return [[r[i + j] for j in idx] for i in idx]

def leading_minors(Mx):
    from copy import deepcopy
    out = []
    for t in range(1, len(Mx) + 1):
        sub = [row[:t] for row in Mx[:t]]
        # exact determinant by fraction-free-ish Gaussian elimination
        A = [list(map(Fr, row)) for row in sub]
        det = Fr(1)
        for c in range(t):
            piv = next((rr for rr in range(c, t) if A[rr][c] != 0), None)
            if piv is None:
                det = Fr(0)
                break
            if piv != c:
                A[c], A[piv] = A[piv], A[c]
                det = -det
            det *= A[c][c]
            for rr in range(c + 1, t):
                if A[rr][c]:
                    f = A[rr][c] / A[c][c]
                    for cc in range(c, t):
                        A[rr][cc] -= f * A[c][cc]
        out.append(det)
    return out

odd = hankel_block([1, 3, 5, 7], rT)
check("odd-block minors", leading_minors(odd),
      [Fr(1), Fr(14, 9), Fr(48814, 2025), Fr(226121391682, 28704375)])
even = hankel_block([2, 4, 6], rT)
check("even-block minors", leading_minors(even),
      [Fr(2, 3), Fr(368, 135), Fr(109932862, 637875)])

# Schur complement threshold (13.2)
A = even
v = [rT[10], rT[12], rT[14]]
# solve A x = v exactly
def solve3(A, v):
    import copy
    M = [row[:] + [v[i]] for i, row in enumerate(A)]
    n = 3
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [M[i][3] for i in range(n)]

x = solve3([row[:] for row in A], v[:])
vAv = sum(a * b for a, b in zip(v, x))
check("v^T A^-1 v = 137490819049597003/2181617646390", vAv,
      Fr(137490819049597003, 2181617646390))
thr = Fr(196536946, 675) + vAv
check("(13.2) m16 threshold fraction", thr, Fr(3863516832738344459, 10908088231950))
check("(13.2) threshold ~ 354188.2638", abs(float(thr) - 354188.2638) < 5e-4, True)

# ------------------------------------------------ Section 11: m8 core histogram
hist = [(14, Fr(1)), (28, Fr(2, 3)), (32, Fr(1, 2)), (4, Fr(9, 20)),
        (5, Fr(2, 5)), (22, Fr(11, 30))]
check("order-8 multiplicities sum to 105", sum(n for n, _ in hist), 105)
check("order-8 weighted sum = 908/15", sum(n * v for n, v in hist), Fr(908, 15))

# ------------------------------------------------ Section 9: refined bounds
# (9.4) upper bounds must hold at the exact moments (empty sums where r>k)
for k in range(4, 8):
    ub_T = (Fr(9, 20) * dfact(2 * k - 1) + Fr(11, 20) * cat(k)
            + Fr(13, 60) * comb(2 * k, k - 2) + Fr(1, 5) * comb(2 * k, k - 3)
            - 2 * sum(comb(2 * k, k - r) * Fr(cT(r), factorial(r + 1))
                      for r in range(5, k + 1)))
    check(f"(9.4) T upper bound holds at k={k}", mT[k] <= ub_T, True)
    ub_H = (Fr(9, 20) * factorial(k) + Fr(11, 20) * cat(k)
            + Fr(1, 20) * comb(2 * k, k - 3)
            - 2 * sum(comb(2 * k, k - r) * Fr(cH(r), factorial(r + 1))
                      for r in range(4, k + 1)))
    check(f"(9.4) H upper bound holds at k={k}", mH[k] <= ub_H, True)

# termwise domination (Cor 4.2): m_H <= m_T, strict for k >= 2
for k in range(2, 8):
    check(f"Cor 4.2 m_{2*k}^H < m_{2*k}^T", mH[k] < mT[k], True)

# --------------------------------------------- Section 6: Lagrange inversion
# [z^m] C(z)^{2r} = r/(m+r) C(2m+2r, m): check by direct series arithmetic
def catalan_series(top):
    return [Fr(cat(j)) for j in range(top + 1)]

def series_pow(S, e, top):
    out = [Fr(0)] * (top + 1)
    out[0] = Fr(1)
    for _ in range(e):
        nxt = [Fr(0)] * (top + 1)
        for i, a in enumerate(out):
            if a:
                for j in range(0, top + 1 - i):
                    if S[j]:
                        nxt[i + j] += a * S[j]
        out = nxt
    return out

TOP = 12
C = catalan_series(TOP)
for r in (1, 2, 3):
    P = series_pow(C, 2 * r, TOP)
    for m in range(0, TOP - 2):
        want = Fr(r, m + r) * comb(2 * m + 2 * r, m)
        if P[m] != want:
            check(f"Lagrange [z^{m}] C^{2*r}", P[m], want)
            break
    else:
        print(f"OK   Lagrange inversion [z^m] C(z)^(2r) for r={r}, m<=9")

# 9*(r+1)!/20 parity claim in Cor 9.2 (even for r+1 >= 6; endpoint r=4: 54 even)
for r in range(4, 10):
    val = Fr(9 * factorial(r + 1), 20)
    check(f"Cor 9.2 parity: 9(r+1)!/20 integer+even at r={r}",
          val.denominator == 1 and int(val) % 2 == 0, True)

print()
if FAIL:
    print(f"*** {len(FAIL)} FAILURES ***")
    for f in FAIL:
        print("   ", f)
else:
    print("ALL IDENTITY CHECKS PASSED")
