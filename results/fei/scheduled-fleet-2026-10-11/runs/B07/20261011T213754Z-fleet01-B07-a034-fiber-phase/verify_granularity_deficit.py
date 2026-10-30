#!/usr/bin/env python3
"""Exact/interval checks for the Boolean granularity-deficit refinement."""
from collections import defaultdict
from fractions import Fraction
from itertools import product


def walsh(table):
    a = [Fraction(v) for v in table]
    n = len(a)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return [z / n for z in a]


def factor(n):
    out = defaultdict(int)
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    if n > 1:
        out[n] += 1
    return out


def entropy_signature(probs):
    sig = defaultdict(Fraction)
    for q in probs:
        q = Fraction(q)
        if not q:
            continue
        for p, e in factor(q.numerator).items():
            sig[p] -= q * e
        for p, e in factor(q.denominator).items():
            sig[p] += q * e
    return {p: c for p, c in sig.items() if c}


def gamma_signature(coeffs, scale):
    """sum c^2 log_2((scale*c)^2), as a prime-log signature."""
    sig = defaultdict(Fraction)
    for c in coeffs:
        if not c:
            continue
        m = c * scale
        assert m.denominator == 1
        z = abs(m.numerator)
        for p, e in factor(z).items():
            sig[p] += c * c * 2 * e
    return {p: c for p, c in sig.items() if c}


def sig_add(*terms):
    out = defaultdict(Fraction)
    for scale, sig in terms:
        for p, c in sig.items():
            out[p] += Fraction(scale) * c
    return {p: c for p, c in out.items() if c}


def atanh_log_interval(y, terms=72):
    """Rigorous interval for ln(y), 1 <= y <= 2, by the atanh series."""
    y = Fraction(y)
    assert 1 <= y <= 2
    z = (y - 1) / (y + 1)
    partial = Fraction()
    for k in range(terms):
        partial += 2 * z ** (2 * k + 1) / (2 * k + 1)
    rem = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return partial, partial + rem


LN2 = atanh_log_interval(Fraction(2))


def ln_interval(x):
    x = Fraction(x)
    assert x > 0
    if x < 1:
        lo, hi = ln_interval(1 / x)
        return -hi, -lo
    k = 0
    y = x
    while y >= 2:
        y /= 2
        k += 1
    lo, hi = atanh_log_interval(y)
    return k * LN2[0] + lo, k * LN2[1] + hi


def entropy_interval(probs):
    lo = Fraction()
    hi = Fraction()
    for q in probs:
        q = Fraction(q)
        if not q:
            continue
        lq, hq = ln_interval(q)
        lo += -q * hq
        hi += -q * lq
    return lo, hi


def signature_ln_interval(sig):
    """Rigorous interval for sum_p c_p ln(p), preserving cancellation."""
    lo = Fraction()
    hi = Fraction()
    for p, c in sig.items():
        lp, hp = ln_interval(Fraction(p))
        if c >= 0:
            lo += c * lp
            hi += c * hp
        else:
            lo += c * hp
            hi += c * lp
    return lo, hi


def split_slices(table, nx, ny):
    return [[table[x | (y << nx)] for x in range(1 << nx)]
            for y in range(1 << ny)]


def x_degree(full_coeffs, nx, ny):
    d = 0
    for ymask in range(1 << ny):
        for xmask in range(1 << nx):
            if full_coeffs[xmask | (ymask << nx)]:
                d = max(d, xmask.bit_count())
    return d


def audit(table, nx, ny):
    full = walsh(table)
    d = x_degree(full, nx, ny)
    slices = split_slices(table, nx, ny)
    sw = [walsh(g) for g in slices]
    checks = 0

    # X marginal of the full squared Fourier law.
    px = []
    for R in range(1 << nx):
        px.append(sum(full[R | (T << nx)] ** 2 for T in range(1 << ny)))
    assert sum(px) == 1
    checks += 1

    # Physical Y influence from spectral degree.
    iy = sum(T.bit_count() * full[R | (T << nx)] ** 2
             for T in range(1 << ny) for R in range(1 << nx))

    if d == 0:
        assert px[0] == 1 and not any(px[1:])
        checks += 1
        return checks, d, iy

    scale = 1 << (d - 1)
    havg_terms = []
    gamma_terms = []
    for coeffs in sw:
        # Degree-d Boolean granularity: scale*c is integral.
        assert all((c * scale).denominator == 1 for c in coeffs)
        checks += len(coeffs)
        hs = entropy_signature([c * c for c in coeffs])
        gs = gamma_signature(coeffs, scale)
        # Exact slice identity H = 2(d-1) - Gamma_d.
        rhs = sig_add((1, {2: Fraction(2 * (d - 1))}), (-1, gs))
        assert hs == rhs
        checks += 1
        # Gamma >= 2 times mass on nonminimal coefficients.
        theta = sum(c * c for c in coeffs if abs(c * scale) >= 2)
        # Gamma >= 2 theta is pointwise: every selected integer has m^2 >= 4.
        assert all(abs(c * scale).numerator ** 2 >= 4
                   for c in coeffs if c and abs(c * scale) >= 2)
        checks += 1
        havg_terms.append(hs)
        gamma_terms.append(gs)

    den = 1 << ny
    havg = sig_add(*[(Fraction(1, den), h) for h in havg_terms])
    gavg = sig_add(*[(Fraction(1, den), g) for g in gamma_terms])
    assert havg == sig_add((1, {2: Fraction(2 * (d - 1))}), (-1, gavg))
    checks += 1

    # Rigorous interval verification of I(S;Y)=H(p_X)-avg H(slice) <= 2 I_Y.
    # Form the exact formal difference first, so equality cases cancel exactly.
    hpx_sig = entropy_signature(px)
    mutual_sig = sig_add((1, hpx_sig), (-1, havg))
    mutual_i = signature_ln_interval(mutual_sig)
    assert mutual_i[0] >= 0
    assert mutual_i[1] <= 2 * iy
    checks += 1
    return checks, d, iy


def sign(bit):
    return 1 if bit else -1


def point_defect(vals):
    return -1 if all(v == -1 for v in vals) else 1


cases = []

# Exhaustive three-variable Boolean functions, split as X^2 x Y.
exact_assertions = 0
degree_hist = defaultdict(int)
for bits in range(1 << 8):
    table = [sign((bits >> i) & 1) for i in range(8)]
    n, d, iy = audit(table, 2, 1)
    exact_assertions += n
    degree_hist[d] += 1

# Addressing: four X-data signs selected by two Y-address signs.
table = []
for z in range(1 << 6):
    xbits = z & 15
    addr = (z >> 4) & 3
    table.append(sign((xbits >> addr) & 1))
cases.append(("addressing_2", table, 4, 2))

# Parity lift of a three-bit point defect: f(x,z)=g(x_1 z,x_2 z,x_3 z).
table = []
for q in range(1 << 4):
    xs = [sign((q >> j) & 1) for j in range(3)]
    z = sign((q >> 3) & 1)
    table.append(point_defect([x * z for x in xs]))
cases.append(("parity_lift_point_defect", table, 3, 1))

# Physical selector between majority_3 and parity_3, both genuine prime gates.
table = []
for q in range(1 << 4):
    xs = [sign((q >> j) & 1) for j in range(3)]
    y = sign((q >> 3) & 1)
    maj = 1 if sum(xs) > 0 else -1
    par = xs[0] * xs[1] * xs[2]
    table.append(maj if y == 1 else par)
cases.append(("majority_parity_selector", table, 3, 1))

# Near tensor: majority_3(X) times a two-bit point defect in Y.
table = []
for q in range(1 << 5):
    xs = [sign((q >> j) & 1) for j in range(3)]
    ys = [sign((q >> (3 + j)) & 1) for j in range(2)]
    maj = 1 if sum(xs) > 0 else -1
    table.append(maj * point_defect(ys))
cases.append(("near_tensor", table, 3, 2))

# Shared signed dictator carrying a one-point-defect address core.
table = []
for q in range(1 << 4):
    xs = [sign((q >> j) & 1) for j in range(3)]
    y = sign((q >> 3) & 1)
    table.append(point_defect(xs) * y)
cases.append(("activation_equivalence", table, 3, 1))

rows = []
for name, table, nx, ny in cases:
    n, d, iy = audit(table, nx, ny)
    exact_assertions += n
    rows.append((name, n, d, str(iy)))

print("PASS")
print("exhaustive_boolean_functions=256")
print("exhaustive_split=X^2_by_Y^1")
print("degree_hist=" + repr(dict(sorted(degree_hist.items()))))
print("named_cases=" + str(len(rows)))
print("exact_and_interval_assertions=" + str(exact_assertions))
for name, n, d, iy in rows:
    print(f"case={name} assertions={n} X_degree={d} I_Y={iy}")
print("log_bounds=exact rational atanh intervals, 72 terms")
print("random_seed=None")

