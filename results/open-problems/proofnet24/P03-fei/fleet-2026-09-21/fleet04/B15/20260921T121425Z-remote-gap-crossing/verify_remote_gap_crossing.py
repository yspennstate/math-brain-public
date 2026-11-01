#!/usr/bin/env python3
from fractions import Fraction
import json

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
    # A_k(u,z,y)=1 on u=+1 and z*b_k(y) on u=-1.
    n = 2*k + 2
    out = []
    for x in range(1 << n):
        u = pm_bit(x, 0)
        z = pm_bit(x, 1)
        b = bent_value(x, 2, k)
        out.append(1 if u == 1 else z*b)
    return out

def B_values(k):
    # U_{k+1}=1-2 1_{x=0}; B_k(v,w,x)=U on v=+1 and w on v=-1.
    m = k + 1
    n = m + 2
    out = []
    for X in range(1 << n):
        v = pm_bit(X, 0)
        w = pm_bit(X, 1)
        x = (X >> 2) & ((1 << m)-1)
        U = -1 if x == 0 else 1
        out.append(U if v == 1 else w)
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
    depth_energy = Fraction(0)
    for aw, arr in sorted(groups.items()):
        aw_v2 = v2(aw)
        q = aw >> aw_v2
        e = n - aw_v2
        eps = [0] * N
        for S, sgn in arr:
            eps[S] = sgn
        V = fwht(eps)
        r = min(v2(z) for z in V if z)
        d = e-r
        p = Fraction(len(arr)*aw*aw, N*N)
        inf = Fraction(sum(S.bit_count() for S, _ in arr)*aw*aw, N*N)
        influence += inf
        depth_energy += p*d
        packets.append({
            "q": q, "e": e, "r": r, "d": d,
            "p": p, "inf": inf, "size": len(arr)
        })
    return packets, influence, depth_energy

def frac(x):
    return f"{x.numerator}/{x.denominator}"

records = []
for k in (2, 3, 4):
    A = A_values(k)
    B = B_values(k)
    P = tensor_values(A, B)
    pa, IA, DA = packet_profile(A)
    pb, IB, DB = packet_profile(B)
    pp, IP, DP = packet_profile(P)

    assert DA == 0
    assert IA == Fraction(k,2) + 1
    assert IB == 1 + Fraction(k+1, 2**(k+1))
    assert IP == IA + IB
    assert DP - DB == Fraction(k,4)

    gotA = sorted((x["e"], x["d"], x["p"]) for x in pa)
    assert gotA == [
        (1, 0, Fraction(1,2)),
        (k+1, 0, Fraction(1,2)),
    ]

    q1 = sorted((x["e"], x["d"], x["p"]) for x in pb if x["q"] == 1)
    tau = Fraction(2**(k+1)-1, 2**(2*k+1))
    assert q1 == [
        (1, 0, Fraction(1,2)),
        (k+1, k, tau),
    ]

    records.append({
        "k": k,
        "dim_A": 2*k+2,
        "dim_B": k+3,
        "dim_tensor": 3*k+5,
        "I_A": frac(IA),
        "I_B": frac(IB),
        "delta_depth_energy": frac(DP-DB),
        "expected_delta": frac(Fraction(k,4)),
        "delta_over_I_B": float((DP-DB)/IB),
        "q1_tail_mass_B": frac(tau),
    })

for k in range(2, 33):
    IA = Fraction(k,2)+1
    IB = 1 + Fraction(k+1, 2**(k+1))
    delta = Fraction(k,4)
    if k >= 4:
        assert delta / IB > Fraction(k, 8)
    assert delta <= IA
    assert IB < 2

out = {
    "status": "PASS",
    "scope": "exact Walsh/Fraction verification of the remote-gap D0 catalyst obstruction",
    "direct_full_walsh_k": [2,3,4],
    "symbolic_formula_k": [2,32],
    "records": records,
    "proved_formula": {
        "I_A_k": "k/2+1",
        "I_B_k": "1+(k+1)/2^(k+1)",
        "DeltaD": "k/4",
        "ratio": "(k/4)/(1+(k+1)/2^(k+1)) -> infinity"
    },
    "full_FEI": "OPEN"
}
print(json.dumps(out, indent=2, sort_keys=True))
