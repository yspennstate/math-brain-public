#!/usr/bin/env python3
"""Exact checks for B16 clone-pair physical resolvent transfer.

Finite checks are falsification evidence only; the companion report gives
the all-dimensional algebraic proof.
"""
from fractions import Fraction
import json

def slice_phase(c, b):
    n = c + 1
    out = []
    for x in range(1 << n):
        old = x & ((1 << c) - 1)
        z = (x >> c) & 1
        out.append(-1 if old == 0 and z == b else 1)
    return out

def qsign(h, x, u, v):
    return h[x] * h[x ^ u] * h[x ^ v] * h[x ^ u ^ v]

def joint(c, u, v):
    h0, h1 = slice_phase(c, 0), slice_phase(c, 1)
    n = c + 1
    k = sum(qsign(h0, x, u, v) == -1 and qsign(h1, x, u, v) == -1
            for x in range(1 << n))
    return Fraction(k, 1 << n)

def bern_prob(mask, n, p):
    k = mask.bit_count()
    return p**k * (1-p)**(n-k)

def expected_joint(c, s, t):
    n = c + 1
    ans = Fraction(0)
    for u in range(1 << n):
        pu = bern_prob(u, n, s)
        for v in range(1 << n):
            ans += pu * bern_prob(v, n, t) * joint(c, u, v)
    return ans

def main():
    result = {"pointwise": {}, "noise_tests": 0}
    for c in range(1, 6):
        n = c + 1
        mx = Fraction(0)
        arg = None
        for u in range(1 << n):
            for v in range(1 << n):
                x = joint(c, u, v)
                if x > mx:
                    mx, arg = x, (u, v)
        result["pointwise"][str(c)] = {
            "max_joint": str(mx), "arg_u": arg[0], "arg_v": arg[1]
        }
        if c >= 2:
            assert mx <= Fraction(1, 1 << (c-1))
    # c=1 projective-parent obstruction: parent is a character but both slices
    # frustrate the old-coordinate/dummy-coordinate square.
    assert result["pointwise"]["1"]["max_joint"] == "1"

    grid = [Fraction(1,8), Fraction(1,4), Fraction(3,8), Fraction(1,2)]
    best = Fraction(0)
    best_data = None
    for c in range(2, 6):
        J = Fraction(c, 1 << (c-1))
        for s in grid:
            for t in grid:
                got = expected_joint(c, s, t)
                bound = 2*s*t*(1-s*t)*J
                assert got <= bound
                result["noise_tests"] += 1
                ratio = got / bound
                if ratio > best:
                    best = ratio
                    best_data = (c, s, t, got, bound)
    result["max_noise_ratio"] = str(best)
    result["max_noise_case"] = [str(x) for x in best_data]

    # 4 * integral_[0,1/2]^2 (1-st) ds dt
    resolvent = 4 * (Fraction(1,4) - Fraction(1,64))
    assert resolvent == Fraction(15,16)
    result["inverse_resolvent_constant"] = str(resolvent)
    result["ward_corollary_constant"] = str(Fraction(15,16)*Fraction(11,192))
    result["status"] = "PASS"
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
