#!/usr/bin/env python3
"""Exact checker for the B15 rare-tribes valuation-reserve selector obstruction.

All certification inequalities below use exact Fraction arithmetic.
No truth table of the large witnesses is generated.
"""

from fractions import Fraction
from math import comb
import json
import sys
sys.set_int_max_str_digits(0)


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 expects a positive integer")
    return (n & -n).bit_length() - 1


def reserve_equal_blocks(m: int, w: int) -> Fraction:
    """Exact R for T_{m,w}, once w exceeds all binomial valuations.

    T_{m,w} = -1 + 2 * product_j (1 - A_j),
    where A_j is the all-ones indicator on a w-bit block.

    The nonconstant magnitude packet indexed by k touched blocks has
      p_k = 4 C(m,k) eps^k (1-eps)^(2m-k),
      r_k = v2(C(m,k)).
    """
    eps = Fraction(1, 2**w)
    q = 1 - eps
    if w <= max(v2(comb(m, k)) for k in range(1, m + 1)):
        raise ValueError("w too small for the valuation formula")
    out = Fraction(0)
    for k in range(1, m + 1):
        out += (
            4
            * comb(m, k)
            * eps**k
            * q ** (2 * m - k)
            * v2(comb(m, k))
        )
    return out


def reserve_average_children(m: int, w: int) -> Fraction:
    """Exact average child reserve after restricting one physical coordinate.

    One child is T_{m-1,w}.  The other has one (w-1)-bit block and
    m-1 w-bit blocks.  The two packet families in the second child
    combine exactly, giving the formula below.
    """
    eps = Fraction(1, 2**w)
    q = 1 - eps
    if w <= max(v2(comb(m - 1, k)) for k in range(1, m)):
        raise ValueError("w too small for the valuation formula")
    out = Fraction(0)
    for k in range(1, m):
        out += (
            4
            * comb(m - 1, k)
            * eps**k
            * q ** (2 * m - 1 - k)
            * v2(comb(m - 1, k))
        )
    return out


def coordinate_influence(m: int, w: int) -> Fraction:
    eps = Fraction(1, 2**w)
    return 2 * eps * (1 - eps) ** (m - 1)


def reserve_selector_lower_ratio(m: int, w: int) -> Fraction:
    """(-Delta R)/Inf_i, a lower bound for Delta D/Inf_i.

    Uses Delta D = Delta H/2 - Delta R and Delta H >= 0.
    """
    root = reserve_equal_blocks(m, w)
    kids = reserve_average_children(m, w)
    delta_r = root - kids
    return -delta_r / coordinate_influence(m, w)


def main():
    rows = []
    witnesses = [
        # (a, m=2^a+1, w, exact comparison target)
        (1, 3, 12, 3),
        (2, 5, 12, 15),
        (3, 9, 12, 47),
        (4, 17, 16, 127),
        (6, 65, 18, 767),
        (8, 257, 20, 4094),
        (10, 1025, 24, 20000),
    ]
    for a, m, w, target in witnesses:
        assert m == 2**a + 1
        ratio = reserve_selector_lower_ratio(m, w)
        limit = 2 * (m - 1) * v2(m - 1)
        assert v2(m - 1) == a
        assert ratio > target
        rows.append(
            {
                "a": a,
                "m": m,
                "w": w,
                "variables": m * w,
                "v2_m_minus_1": v2(m - 1),
                "limit_formula": limit,
                "certified_lower_bound_gt": target,
                "ratio_decimal": f"{float(ratio):.12f}",
                "ratio_numerator_digits": len(str(ratio.numerator)),
                "ratio_denominator_digits": len(str(ratio.denominator)),
            }
        )

    # First-order coefficient check for the analytic asymptotic:
    # for odd m, R_root has no O(eps) term because v2(C(m,1))=v2(m)=0;
    # the average child reserve has O(eps) coefficient
    # 4(m-1)v2(m-1).  Inf_i has O(eps) coefficient 2.
    for m in [3, 5, 7, 9, 17, 33, 65]:
        assert m % 2 == 1
        root_linear = 4 * m * v2(m)
        child_linear = 4 * (m - 1) * v2(m - 1)
        influence_linear = 2
        predicted = (child_linear - root_linear) // influence_linear
        assert predicted == 2 * (m - 1) * v2(m - 1)

    result = {
        "status": "PASS",
        "statement_checked": (
            "For T_{m,w} with odd m and sufficiently large w, "
            "Delta_i D / Inf_i >= -Delta_i R / Inf_i, and for m=2^a+1 "
            "the latter tends to 2^(a+1)*a. Hence no finite universal "
            "existential-coordinate selector constant can pay D alone."
        ),
        "large_exact_witness": rows[-1],
        "witnesses": rows,
        "notes": [
            "All comparison assertions use exact Fraction arithmetic.",
            "The large witnesses use compressed packet formulas, not truth-table enumeration.",
            "The checker does not use the finite calculations as the proof of asymptotic divergence.",
            "Full FEI is not claimed."
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
