#!/usr/bin/env python3
"""Reproduce the magnitude-DTC remainder identities and a carry dead-route witness.

No FEI finite sweep is performed.  The selected Boolean examples exercise the
new exact identities and the explicit event-entropy counterexample.
"""
from collections import defaultdict
from fractions import Fraction
from math import log2
import json


def fwht_int(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def truth(n, mask):
    return [-1 if ((mask >> x) & 1) else 1 for x in range(1 << n)]


def h2(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * log2(q) - (1.0 - q) * log2(1.0 - q)


def magnitude_remainder(f):
    N = len(f)
    n = N.bit_length() - 1
    W = fwht_int(f)
    p = [Fraction(w * w, N * N) for w in W]
    H = sum(float(x) * log2(1.0 / float(x)) for x in p if x)
    I = sum(p[s] * s.bit_count() for s in range(N))

    groups = defaultdict(list)
    for s, w in enumerate(W):
        if w:
            groups[abs(w)].append(s)

    H_M = 0.0
    packet_dtc = 0.0
    same = Fraction()
    for mag, A in groups.items():
        atom = Fraction(mag * mag, N * N)
        mass = atom * len(A)
        H_M += float(mass) * log2(1.0 / float(mass))
        Aset = set(A)
        internal_edges = 0
        for s in A:
            for i in range(n):
                if (s >> i) & 1 and (s ^ (1 << i)) in Aset:
                    internal_edges += 1  # each undirected edge once
        avg_internal_degree = Fraction(2 * internal_edges, len(A))
        packet_dtc += float(mass) * (
            log2(len(A)) - float(avg_internal_degree)
        )
        same += 2 * atom * internal_edges

    total_conditional = 0.0
    magnitude_ambiguity = 0.0
    for i in range(n):
        bit = 1 << i
        for t in range(N):
            if t & bit:
                continue
            p0, p1 = p[t], p[t | bit]
            m = p0 + p1
            if not m:
                continue
            c = float(m) * h2(float(p1 / m))
            total_conditional += c
            if p0 and p1 and abs(W[t]) != abs(W[t | bit]):
                magnitude_ambiguity += c

    global_dtc = H - total_conditional
    P_mag = H - float(same)

    assert abs(P_mag - (H_M + packet_dtc)) < 1e-11
    assert abs(P_mag - (global_dtc + magnitude_ambiguity)) < 1e-11
    assert float(same) <= 2.0 * float(I) + 1e-12

    return {
        "H": H,
        "I": float(I),
        "H_M": H_M,
        "packet_DTC": packet_dtc,
        "global_DTC": global_dtc,
        "magnitude_ambiguity_sum": magnitude_ambiguity,
        "same_packet_conditional": float(same),
        "P_mag": P_mag,
    }


def v2(z):
    z = abs(int(z))
    assert z
    return (z & -z).bit_length() - 1


def packets(f):
    N = len(f)
    n = N.bit_length() - 1
    W = fwht_int(f)
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
        V = fwht_int(signs)
        r = min(v2(z) for z in V if z)
        Wphys = [z // (1 << r) for z in V]
        d = e - r
        mass = Fraction(len(entries) * mag * mag, N * N)
        out.append({"q": q, "d": d, "p": mass, "W": Wphys})
    return out


def carry_events(f):
    comps = [dict(c) for c in packets(f)]
    events = []
    while True:
        D = max(c["d"] for c in comps)
        if D == 0:
            break
        top = [c for c in comps if c["d"] == D]
        rest = [c for c in comps if c["d"] < D]
        T = [sum(c["q"] * c["W"][x] for c in top) for x in range(len(f))]
        s = min(v2(z) for z in T if z)
        jump = min(s, D)
        P = sum((c["p"] for c in top), Fraction())
        Q = sum(float(c["p"]) * log2(c["q"]) for c in top)
        masses = [c["p"] for c in top]
        mixing = float(P) * sum(
            -float(p / P) * log2(float(p / P)) for p in masses
        )
        net = float(P) * jump - Q
        events.append({
            "depth": D,
            "jump": jump,
            "mass": str(P),
            "top_masses": [str(x) for x in masses],
            "odd_numerators": [c["q"] for c in top],
            "net": net,
            "mixing_entropy_mass": mixing,
            "net_minus_mixing": net - mixing,
        })
        d_new = D - jump
        divisor = (1 << s) if d_new > 0 else (1 << D)
        Wnew = [z // divisor for z in T]
        comps = rest + [{"q": 1, "d": d_new, "p": P, "W": Wnew}]
    return events


def main():
    cases = [
        ("one_point_n3", 3, 0x1),
        ("event_entropy_counterexample", 4, 0x7),
        ("plateaued_n3", 3, 23),
        ("negative_carry_n5", 5, 0xD974B822),
    ]
    out = {}
    for name, n, mask in cases:
        out[name] = magnitude_remainder(truth(n, mask))
        if name == "event_entropy_counterexample":
            out[name]["carry_events"] = carry_events(truth(n, mask))

    second = out["event_entropy_counterexample"]["carry_events"][1]
    assert second["jump"] == 1
    assert second["mass"] == "1"
    assert second["top_masses"] == ["3/16", "13/16"]
    assert second["odd_numerators"] == [1, 1]
    assert abs(second["net"] - 1.0) < 1e-12
    assert second["net_minus_mixing"] > 0.30

    print(json.dumps(out, indent=2, sort_keys=True))
    print("magnitude_dtc_remainder=PASS")
    print("event_entropy_payment=REFUTED_AT_EXACT_BOOLEAN_WITNESS")


if __name__ == "__main__":
    main()
