#!/usr/bin/env python3
"""Exact checker for B17 rare-pair spectral independence / face-boundary mechanism.

All identities involving the Boolean truth table, Walsh coefficients, influences,
face counts, and pairwise spectral independence use integers/Fraction. Floating
point is used only for reported Shannon entropy and the Hod-constant diagnostic.
"""
from fractions import Fraction
import json, math

def fwht_int(vals):
    a = list(map(int, vals))
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def build_family(k):
    # m control bits; two distinguished bits i=0, j=1.
    m = 2*k - 1
    n = m + 2
    M = 1 << m
    a = (1 << (k-1)) - 1
    U = set(range(0, a))
    V = set(range(a, 2*a))
    T = set(range(2*a, 2*a+2))
    vals = []
    for idx in range(1 << n):
        bi = (idx >> 0) & 1
        bj = (idx >> 1) & 1
        y = idx >> 2
        if y in U:
            val = 1 if bi == 0 else -1       # i-character face
        elif y in V:
            val = 1 if bj == 0 else -1       # j-character face
        elif y in T:
            val = -1 if (bi == 1 and bj == 1) else 1  # one-defect face
        else:
            val = 1                           # constant face
        vals.append(val)
    return vals, U, V, T, m, n

def influence(vals, bit):
    N = len(vals)
    return Fraction(sum(vals[x] != vals[x ^ (1 << bit)] for x in range(N)), N)

def set_influence(A, m):
    M = 1 << m
    ans = Fraction(0)
    for bit in range(m):
        ans += Fraction(sum(((y in A) != ((y ^ (1 << bit)) in A)) for y in range(M)), M)
    return ans

def entropy_bits_from_walsh(W):
    N = len(W)
    den = N*N
    out = 0.0
    for w in W:
        if w:
            p = (w*w)/den
            out -= p*math.log2(p)
    return out

def fracstr(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

rows = []
for k in range(2, 7):
    vals, U, V, T, m, n = build_family(k)
    N = len(vals)
    W = fwht_int(vals)
    den = N*N

    p = Fraction(sum(w*w for s,w in enumerate(W) if (s & 1)), den)
    r = Fraction(sum(w*w for s,w in enumerate(W) if (s & 2)), den)
    q = Fraction(sum(w*w for s,w in enumerate(W) if (s & 3) == 3), den)

    target = Fraction(1, 1 << k)
    assert p == r == target
    assert q == p*r

    infs = [influence(vals, b) for b in range(n)]
    I = sum(infs, Fraction(0))
    Ictrl = sum(infs[2:], Fraction(0))
    IU = set_influence(U, m)
    IV = set_influence(V, m)
    boundary_cert = (IU + IV) / 4
    assert Ictrl >= boundary_cert

    M = 1 << m
    expected_u = (1 << (k-1)) - 1
    assert len(U) == len(V) == expected_u and len(T) == 2
    # Face-type masses: u=v=p(1-2p), t=4p^2, w=0, c=1-2p.
    assert Fraction(len(U), M) == p*(1-2*p)
    assert Fraction(len(V), M) == p*(1-2*p)
    assert Fraction(len(T), M) == 4*p*p
    assert Fraction(M-len(U)-len(V)-len(T), M) == 1-2*p

    H = entropy_bits_from_walsh(W)
    C_hod = 6.4547837
    h2p = -(float(p)*math.log2(float(p)) + (1-float(p))*math.log2(1-float(p)))
    excess_pair = 2*(h2p - C_hod*float(p))
    iso_closed = 0.25*(float(p)*math.log2(2/float(p)) +
                       float(r)*math.log2(2/float(r)))

    rows.append({
        "k": k,
        "n": n,
        "control_dimension_m": m,
        "p_i": fracstr(p),
        "p_j": fracstr(r),
        "q_ij": fracstr(q),
        "q_equals_p_i_p_j_exact": q == p*r,
        "face_counts": {
            "constant": M-len(U)-len(V)-len(T),
            "i_dictator": len(U),
            "j_dictator": len(V),
            "parity": 0,
            "one_defect": len(T),
            "total": M
        },
        "total_influence_exact": fracstr(I),
        "control_influence_exact": fracstr(Ictrl),
        "indicator_boundary_quarter_exact": fracstr(boundary_cert),
        "control_ge_boundary_exact": Ictrl >= boundary_cert,
        "fourier_entropy_bits": H,
        "H_over_I": H/float(I),
        "pair_mutual_information_bits": 0.0,
        "hod_scalar_excess_for_two_rare_marginals": excess_pair,
        "analytic_independence_isoperimetric_lower_bound": iso_closed
    })

print(json.dumps({
    "status": "PASS",
    "scope": "exact family identities plus exact face-boundary precursor; entropy diagnostics are float64",
    "rows": rows
}, indent=2, sort_keys=True))
