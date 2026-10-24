#!/usr/bin/env python3
"""Exact-Walsh / high-precision verification for the 16-bit top-flip tribes witness.

Exact statements:
  * truth table and integer Walsh transform,
  * Parseval,
  * all 16 influences as exact rational numbers,
  * exact equality of all 16 coordinate fibre multisets,
  * exact orbit/fibre counts.

Transcendental entropy values are evaluated with Decimal at two precisions.
They are high-precision stability checks, not directed-rounding certificates.
No strict numerical improvement over the width-two-tribes baseline is claimed.
"""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
import json

N_BITS = 16
TRIBES = 8
N = 1 << N_BITS
N2 = N * N

def width2_tribes_value(x):
    for j in range(TRIBES):
        if ((x >> (2*j)) & 3) == 3:
            return -1
    return 1

def build_values(top_flip=False):
    f = [width2_tribes_value(x) for x in range(N)]
    if top_flip:
        assert f[N-1] == -1
        f[N-1] = 1
    return f

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        step = 2*h
        for s in range(0, len(a), step):
            for j in range(h):
                u = a[s+j]
                v = a[s+h+j]
                a[s+j] = u+v
                a[s+h+j] = u-v
        h *= 2
    return a

def influence_numerator(A, i):
    mask = 1 << i
    return sum(A[S]*A[S] for S in range(N) if S & mask)

def fibre_counter(A, i):
    mask = 1 << i
    c = Counter()
    for T in range(N):
        if T & mask:
            continue
        aa = A[T] * A[T]
        bb = A[T | mask] * A[T | mask]
        if aa + bb:
            c[(aa, bb)] += 1
    return c

def h2(q, one, ln2):
    if q == 0 or q == one:
        return Decimal(0)
    return -(q*q.ln() + (one-q)*(one-q).ln())/ln2

def entropy_stats(counter, p_num, precision):
    with localcontext() as ctx:
        ctx.prec = precision
        one = Decimal(1)
        ln2 = Decimal(2).ln()
        B = Decimal(0)
        JS = Decimal(0)
        for (aa, bb), mult in counter.items():
            den = aa + bb
            w = Decimal(den) / Decimal(N2)
            q = Decimal(bb) / Decimal(den)
            hb = h2(q, one, ln2)
            z = Decimal("0.5") + (q*(one-q)).sqrt()
            j = one - h2(z, one, ln2)
            B += Decimal(mult) * w * hb
            JS += Decimal(mult) * w * j
        p = Decimal(p_num) / Decimal(N2)
        return {
            "B": +B,
            "JS": +JS,
            "Delta": +(B+JS),
            "B_over_p": +(B/p),
            "JS_over_p": +(JS/p),
            "rho0": +((B+JS)/p),
        }

def spectral_HI(A, p_nums, precision):
    counts = Counter(a*a for a in A if a)
    with localcontext() as ctx:
        ctx.prec = precision
        ln2 = Decimal(2).ln()
        H = Decimal(0)
        for aa, mult in counts.items():
            p = Decimal(aa)/Decimal(N2)
            H -= Decimal(mult)*p*p.ln()/ln2
        I = Decimal(sum(p_nums))/Decimal(N2)
        return +H, +I, +(H/I), len(counts)

def dstr(x):
    return format(x, "f")

def analyze(top_flip):
    f = build_values(top_flip)
    A = fwht(f)
    assert sum(a*a for a in A) == N2
    p_nums = [influence_numerator(A, i) for i in range(N_BITS)]
    assert len(set(p_nums)) == 1
    counters = [fibre_counter(A, i) for i in range(N_BITS)]
    assert all(c == counters[0] for c in counters[1:])
    s80 = entropy_stats(counters[0], p_nums[0], 80)
    s110 = entropy_stats(counters[0], p_nums[0], 110)
    H80, I80, R80, n_sq = spectral_HI(A, p_nums, 80)
    H110, I110, R110, _ = spectral_HI(A, p_nums, 110)
    # 55-decimal stability is enough for the printed scientific figures.
    for k in s80:
        assert dstr(s80[k])[:57] == dstr(s110[k])[:57]
    assert dstr(R80)[:57] == dstr(R110)[:57]
    return {
        "top_flip": top_flip,
        "plus_inputs": sum(v == 1 for v in f),
        "walsh_min": min(A),
        "walsh_max": max(A),
        "parseval_integer_sum": sum(a*a for a in A),
        "influence_exact": str(Fraction(p_nums[0], N2)),
        "influence_decimal": dstr(Decimal(p_nums[0])/Decimal(N2)),
        "coordinate_fibre_multisets_identical": True,
        "unique_nonzero_fibre_types": len(counters[0]),
        "fibre_counter": [
            {"a2": aa, "b2": bb, "multiplicity": m}
            for (aa, bb), m in sorted(counters[0].items())
        ],
        "entropy_precision_80": {k: dstr(v) for k,v in s80.items()},
        "H_precision_80": dstr(H80),
        "I_precision_80": dstr(I80),
        "H_over_I_precision_80": dstr(R80),
        "distinct_nonzero_squared_walsh_magnitudes": n_sq,
    }

base = analyze(False)
star = analyze(True)
with localcontext() as ctx:
    ctx.prec = 80
    deficit = Decimal(base["entropy_precision_80"]["rho0"]) - Decimal(star["entropy_precision_80"]["rho0"])
out = {
    "status": "PASS",
    "normalization": "fhat(S)=A_S/2^16; spectral mass=A_S^2/2^32; log base 2",
    "baseline_width2_tribes_s8": base,
    "top_flip_witness": star,
    "rho0_deficit_from_baseline": dstr(deficit),
    "transcendental_status": "Decimal 80/110-digit stability check; not a directed-rounding enclosure; no strict improvement claimed",
}
print(json.dumps(out, indent=2, sort_keys=True))
