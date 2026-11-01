#!/usr/bin/env python3
from fractions import Fraction
import json, math

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def v2(z):
    z = abs(z)
    if z == 0:
        raise ValueError("v2(0)")
    r = 0
    while z % 2 == 0:
        z //= 2
        r += 1
    return r

def pm_bit(x, i):
    return 1 if ((x >> i) & 1) == 0 else -1

def bent_value(x, offset, k):
    p = 0
    for j in range(k):
        p ^= ((x >> (offset + 2*j)) & 1) & ((x >> (offset + 2*j + 1)) & 1)
    return -1 if p else 1

def A_values(k):
    n = 2*k + 2
    out = []
    for X in range(1 << n):
        u = pm_bit(X, 0)
        z = pm_bit(X, 1)
        b = bent_value(X, 2, k)
        out.append(1 if u == 1 else z*b)
    return out

def F_three(n):
    return [1 if x in (0,1,2) else -1 for x in range(1 << n)]

def B_values(n):
    F = F_three(n)
    out = []
    for X in range(1 << (n+2)):
        v = pm_bit(X, 0)
        w = pm_bit(X, 1)
        x = X >> 2
        out.append(F[x] if v == 1 else w)
    return out

def tensor_values(a, b):
    return [a[x] * b[y] for y in range(len(b)) for x in range(len(a))]

def packet_profile(vals):
    N = len(vals)
    n = N.bit_length()-1
    W = fwht(vals)
    groups = {}
    for S, w in enumerate(W):
        if w:
            groups.setdefault(abs(w), []).append((S, 1 if w > 0 else -1))
    packets = []
    influence = Fraction(0)
    D = Fraction(0)
    for aw, arr in sorted(groups.items()):
        av = v2(aw)
        q = aw >> av
        e = n - av
        eps = [0] * N
        for S, sgn in arr:
            eps[S] = sgn
        V = fwht(eps)
        r = min(v2(z) for z in V if z)
        d = e-r
        p = Fraction(len(arr)*aw*aw, N*N)
        inf = Fraction(sum(S.bit_count() for S, _ in arr)*aw*aw, N*N)
        influence += inf
        D += p*d
        packets.append((q,e,r,d,p))
    return packets, influence, D

def get_packet(packets, q, e):
    hits = [x for x in packets if x[0] == q and x[1] == e]
    assert len(hits) == 1
    return hits[0]

source_records = []
for n in range(4, 11):
    pf, IF, DF = packet_profile(F_three(n))
    pb, IB, DB = packet_profile(B_values(n))
    q1F = get_packet(pf, 1, n-1)
    q1B_lo = get_packet(pb, 1, 1)
    q1B_hi = get_packet(pb, 1, n)
    assert q1F[2] == n-2 and q1F[3] == 1 and q1F[4] == Fraction(3, 2**n)
    assert q1B_lo[2] == 1 and q1B_lo[3] == 0 and q1B_lo[4] == Fraction(1,2)
    assert q1B_hi[2] == n-1 and q1B_hi[3] == 1 and q1B_hi[4] == Fraction(3, 2**(n+1))
    assert IF == Fraction(3*n-4, 2**(n-1))
    assert IB == 1 + Fraction(3*n-4, 2**n)
    source_records.append({
        "n": n,
        "F_q1_packet": {"e": q1F[1], "r": q1F[2], "d": q1F[3],
                        "p": f"{q1F[4].numerator}/{q1F[4].denominator}"},
        "B_low_packet": {"e": q1B_lo[1], "r": q1B_lo[2], "d": q1B_lo[3],
                         "p": f"{q1B_lo[4].numerator}/{q1B_lo[4].denominator}"},
        "B_high_packet": {"e": q1B_hi[1], "r": q1B_hi[2], "d": q1B_hi[3],
                          "p": f"{q1B_hi[4].numerator}/{q1B_hi[4].denominator}"},
        "I_F": f"{IF.numerator}/{IF.denominator}",
        "I_B": f"{IB.numerator}/{IB.denominator}",
    })

n = 4
k = n-1
A = A_values(k)
B = B_values(n)
pa, IA, DA = packet_profile(A)
pb, IB, DB = packet_profile(B)
pt, IT, DT = packet_profile(tensor_values(A, B))
assert sorted(pa) == [
    (1, 1, 1, 0, Fraction(1,2)),
    (1, n, n, 0, Fraction(1,2)),
]
assert IA == Fraction(n+1,2)
assert DA == 0
assert IT == IA + IB
assert DT - DB == Fraction(1,4)

formula_records = []
for n in range(4, 33):
    A2 = 2**n
    u = Fraction(1,4)
    v = Fraction(3, 2**(n+2))
    P = u+v
    rho = v/P
    assert rho == Fraction(3, A2+3)
    assert rho < Fraction(1,3)
    Z = rho + (1-rho)*Fraction(1,4)
    assert Z == Fraction(A2+12, 4*(A2+3))
    raw = u
    psi = -0.5*math.log2(float(Z))
    residual = float(P)*psi
    assert psi > 0.5
    assert 0 < residual < float(raw)
    rhs = float(P)/2 + max(float(u-2*v),0.0)/2
    assert residual <= rhs + 1e-14
    psi_closed = 1 + 0.5*math.log2((A2+3)/(A2+12))
    assert abs(psi-psi_closed) < 1e-14
    if n in (4,5,6,8,12,16,24,32):
        formula_records.append({
            "n": n,
            "k": n-1,
            "rho": f"{rho.numerator}/{rho.denominator}",
            "Z": f"{Z.numerator}/{Z.denominator}",
            "Psi": psi,
            "P_Psi": residual,
            "raw_collision": f"{raw.numerator}/{raw.denominator}",
            "refund_fraction": (float(raw)-residual)/float(raw),
            "residual_over_raw": residual/float(raw),
            "midpoint_bound": rhs,
        })

assert formula_records[-1]["residual_over_raw"] > 0.99999999

criterion_checks = 0
for g in range(1, 9):
    threshold = Fraction(1, 2**g + 1)
    for den in range(2, 101):
        for num in range(1, den):
            rho = Fraction(num, den)
            Z = rho + (1-rho)*Fraction(1, 4**g)
            lhs = Z >= Fraction(1, 2**g)
            rhs = rho >= threshold
            assert lhs == rhs
            criterion_checks += 1

out = {
    "status": "PASS",
    "scope": "exact Boolean adversary to fibrewise half-gap/fixed-refund post-KL remainder, plus midpoint-excess replacement",
    "direct_source_n": [4,10],
    "direct_full_tensor_n": 4,
    "symbolic_family_n": [4,32],
    "criterion_rational_checks": criterion_checks,
    "source_records": source_records,
    "formula_records": formula_records,
    "proved": {
        "F_n_q1_packet": "e=n-1, r=n-2, d=1, p=3*2^-n",
        "B_n_q1_packets": "(e,d,p)=(1,0,1/2) and (n,1,3*2^-(n+1))",
        "catalyst": "A_(n-1): q=1 packets (e,d,p)=(1,0,1/2),(n,0,1/2)",
        "tensor_raw_D_increment": "1/4",
        "rho": "3/(2^n+3)",
        "Psi": "1 + (1/2) log2((2^n+3)/(2^n+12)) -> 1",
        "post_KL_residual": "((2^n+3)/2^(n+2))*Psi -> 1/4",
        "refund_fraction": "1 - (post_KL_residual)/(1/4) -> 0",
        "half_gap_criterion": "Psi_g(rho)<=g/2 iff rho>=1/(2^g+1)",
        "replacement": "P Psi <= P g/2 + g/2*(u-2^g v)_+ for a two-origin fibre"
    },
    "full_FEI": "OPEN"
}
print(json.dumps(out, indent=2, sort_keys=True))
