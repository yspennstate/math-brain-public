#!/usr/bin/env python3
"""Exact/symbolic checker for the signed arithmetic carry decomposition.

All Walsh transforms, packet masses, depths, valuations and carry jumps are
computed with Python integers/Fraction.  Only displayed logarithms are binary64.
"""
from collections import defaultdict
from fractions import Fraction
from math import log2

NEGATIVE_WITNESS_N = 5
NEGATIVE_WITNESS_MASK = 0xD974B822

def fwht(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def v2(z):
    z = abs(int(z))
    assert z
    return (z & -z).bit_length() - 1

def truth_from_mask(n, mask):
    return [-1 if ((mask >> x) & 1) else 1 for x in range(1 << n)]

def packets(f):
    N = len(f)
    n = N.bit_length() - 1
    W = fwht(f)
    groups = defaultdict(list)
    for s, w in enumerate(W):
        if w:
            groups[abs(w)].append((s, 1 if w > 0 else -1))

    out = []
    for mag, entries in groups.items():
        t = v2(mag)
        q = mag >> t
        e = n - t
        signs = [0] * N
        for s, sg in entries:
            signs[s] = sg
        V = fwht(signs)
        r = min(v2(z) for z in V if z)
        Wphys = [z // (1 << r) for z in V]
        d = e - r
        assert d >= 0
        if d == 0:
            assert q == 1
        p = Fraction(len(entries) * mag * mag, N * N)
        infl = Fraction(
            mag * mag * sum(s.bit_count() for s, _ in entries), N * N
        )
        b2_norm = Fraction(q*q, 1 << (2*d)) * Fraction(
            sum(z*z for z in Wphys), N
        )
        assert b2_norm == p
        out.append({
            "q": q, "d": d, "p": p, "I": infl, "W": Wphys,
            "support": tuple(s for s, _ in entries),
        })
    return out

def arithmetic_D(pkts):
    raw = sum((c["p"] * c["d"] for c in pkts), Fraction())
    credit = sum(float(c["p"]) * log2(c["q"]) for c in pkts)
    return float(raw) - credit, raw, credit

def carry_events(f):
    comps = [dict(c) for c in packets(f)]
    events = []
    while True:
        D = max(c["d"] for c in comps)
        if D == 0:
            break
        top = [c for c in comps if c["d"] == D]
        rest = [c for c in comps if c["d"] < D]
        # A sole positive-depth primitive component would give an odd top
        # residue somewhere and cannot sum with coarser terms to +/-1.
        assert len(top) >= 2

        N = len(f)
        T = [sum(c["q"] * c["W"][x] for c in top) for x in range(N)]
        assert any(T)
        s = min(v2(z) for z in T if z)
        assert s >= 1
        jump = min(s, D)
        P = sum((c["p"] for c in top), Fraction())
        Q = sum(float(c["p"]) * log2(c["q"]) for c in top)
        events.append({
            "depth": D,
            "valuation_gain": s,
            "jump": jump,
            "mass": P,
            "odd_numerator_credit": Q,
            "net": float(P) * jump - Q,
            "q": tuple(c["q"] for c in top),
        })

        d_new = D - jump
        divisor = (1 << s) if d_new > 0 else (1 << D)
        assert all(z % divisor == 0 for z in T)
        Wnew = [z // divisor for z in T]
        if d_new > 0:
            assert min(v2(z) for z in Wnew if z) == 0
        new = {
            "q": 1,
            "d": d_new,
            "p": P,
            "I": sum((c["I"] for c in top), Fraction()),
            "W": Wnew,
            "support": tuple(s for c in top for s in c["support"]),
        }
        comps = rest + [new]

    D0, raw0, credit0 = arithmetic_D(packets(f))
    signed = sum(ev["net"] for ev in events)
    carry = sum(float(ev["mass"]) * ev["jump"] for ev in events)
    assert abs(carry - float(raw0)) < 1e-12
    assert abs(signed - D0) < 1e-12
    return events, D0, raw0, credit0

def entropy_influence(f):
    N = len(f)
    W = fwht(f)
    H = 0.0
    I = Fraction()
    for s, w in enumerate(W):
        if not w:
            continue
        p = Fraction(w*w, N*N)
        H += float(p) * log2(1.0/float(p))
        I += p * s.bit_count()
    return H, I

def exhaustive_small():
    checked = 0
    for n in range(1, 5):
        for mask in range(1 << (1 << n)):
            f = truth_from_mask(n, mask)
            pk = packets(f)
            events, D, raw, credit = carry_events(f)
            H, I = entropy_influence(f)
            R = sum((c["p"] * (0) for c in pk), Fraction())
            # Recompute r indirectly from H/2-D; just verify D is nonnegative.
            assert D >= -1e-12
            checked += 1
    return checked

def negative_event_witness():
    f = truth_from_mask(NEGATIVE_WITNESS_N, NEGATIVE_WITNESS_MASK)
    pk = sorted(packets(f), key=lambda c: (-c["d"], c["q"]))
    events, D, raw, credit = carry_events(f)
    assert [(c["q"], c["d"], c["p"]) for c in pk] == [
        (7, 4, Fraction(49,256)),
        (9, 4, Fraction(81,256)),
        (1, 3, Fraction(11,128)),
        (3, 3, Fraction(27,128)),
        (5, 3, Fraction(25,128)),
    ]
    e0, e1 = events
    assert e0["depth"] == 4 and e0["jump"] == 1
    assert e0["mass"] == Fraction(65,128)
    assert e0["net"] < 0
    assert e1["depth"] == 3 and e1["jump"] == 3
    assert e1["mass"] == 1
    assert e1["net"] > 0
    return pk, events, D, raw, credit

def one_point(n):
    # x=0 is the unique -1 point.
    return [-1] + [1] * ((1 << n) - 1)

def one_point_table():
    rows = []
    for n in range(3, 13):
        f = one_point(n)
        ev, D, raw, credit = carry_events(f)
        H, I = entropy_influence(f)
        assert len(ev) == 1
        assert ev[0]["depth"] == n-1
        assert ev[0]["jump"] == n-1
        assert ev[0]["mass"] == 1
        rows.append((n, raw, credit, D, I, D/float(I)))
    return rows

if __name__ == "__main__":
    checked = exhaustive_small()
    pk, ev, D, raw, credit = negative_event_witness()
    print(f"exhaustive_boolean_functions_n_le_4={checked}")
    print("negative_event_witness=0xd974b822")
    print("packets q d p:")
    for c in pk:
        print(c["q"], c["d"], c["p"])
    print("events depth s jump mass Q net:")
    for x in ev:
        print(
            x["depth"], x["valuation_gain"], x["jump"], x["mass"],
            f"{x['odd_numerator_credit']:.15f}", f"{x['net']:.15f}"
        )
    print(f"raw_depth={float(raw):.15f}")
    print(f"odd_numerator_credit={credit:.15f}")
    print(f"arithmetic_D={D:.15f}")
    print("one_point n raw_depth credit D I D_over_I")
    for n, raw, credit, D, I, ratio in one_point_table():
        print(
            n, f"{float(raw):.12f}", f"{credit:.12f}",
            f"{D:.12f}", f"{float(I):.12f}", f"{ratio:.12f}"
        )
    print("signed_carry_decomposition=PASS")
