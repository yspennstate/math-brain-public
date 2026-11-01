#!/usr/bin/env python3
"""Exact compressed spectrum-entropy certificate for ternary NAND depth 3.
Run beside check_recovery.py. No enumeration of 2^27 inputs is required.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
import json
from check_recovery import log2_bounds


def term(p: F) -> tuple[F, F]:
    if not p:
        return F(0), F(0)
    lo, hi = log2_bounds(1/p)
    return p*lo, p*hi


def dec(p: F, rounding: str) -> str:
    with localcontext() as ctx:
        ctx.prec = 40
        ctx.rounding = rounding
        return str(Decimal(p.numerator) / Decimal(p.denominator))


def interval(lo: F, hi: F) -> dict:
    return {"lower_decimal": dec(lo, ROUND_FLOOR),
            "upper_decimal": dec(hi, ROUND_CEILING),
            "width_upper_decimal": dec(hi-lo, ROUND_CEILING)}


def main() -> None:
    alpha, e_lo, e_hi, energy, n = F(1,2), F(1), F(1), F(1,4), 1
    rows = []
    for depth in range(1,4):
        b = alpha**3
        old_lo, old_hi = term(b*b)
        new_lo, new_hi = term((1-b)**2)
        factor = 3*alpha*alpha
        e_lo, e_hi = factor*e_lo-old_hi+new_lo, factor*e_hi-old_lo+new_hi
        energy *= factor
        alpha = 1-b
        n *= 3
        a_lo, a_hi = term(alpha*alpha)
        f_lo, f_hi = term((1-2*alpha)**2)
        h_lo = f_lo + 4*(e_lo-a_hi)-8*alpha*(1-alpha)
        h_hi = f_hi + 4*(e_hi-a_lo)-8*alpha*(1-alpha)
        inf = 4*energy
        rows.append({"depth": depth, "variables": n, "indicator_mean": str(alpha),
                     "I_exact": str(inf), "H_bits": interval(h_lo,h_hi),
                     "H_over_I": interval(h_lo/inf,h_hi/inf)})
    assert h_lo > 4*inf
    assert h_lo/inf > F(44265,10000)
    result = {"status": "PASS", "function": "f=1-2*A3; A0 is one input bit; A_(j+1)=1-product of three disjoint copies of A_j",
              "method": "Exact indicator product/complement identities plus outward-rounded rational logarithm enclosures",
              "levels": rows,
              "H_gt_4I_certified": True,
              "minimum_artificial_boundary_A_over_total_I": interval((h_lo/inf-4)/2,(h_hi/inf-4)/2),
              "scope": "Rules out boundary-separated subcube-parity representations for this function; does not refute FEI."}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
