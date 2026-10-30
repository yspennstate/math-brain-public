#!/usr/bin/env python3
"""Exact finite check of the rectangle-anchor factorization lemma.

Exhausts every Boolean sign table on a 4 x 4 product cube.  For each table it
checks that the average Hamming error of all anchored rank-one products is
exactly the multiplicative rectangle-defect probability, and hence that the
best Boolean rank-one approximation has no larger error.
"""

from fractions import Fraction


def bit(mask: int, x: int, y: int) -> int:
    """Return a {-1,+1} table value for row x, column y."""
    return -1 if ((mask >> (4 * x + y)) & 1) else 1


def mismatch_count(mask: int, x0: int, y0: int) -> int:
    """Error count for u(x)=f(x,y0), v(y)=f(x0,y)f(x0,y0)."""
    c = 0
    anchor = bit(mask, x0, y0)
    for x in range(4):
        for y in range(4):
            product = bit(mask, x, y0) * bit(mask, x0, y) * anchor
            c += product != bit(mask, x, y)
    return c


def rectangle_defect_count(mask: int) -> int:
    c = 0
    for x in range(4):
        for xp in range(4):
            for y in range(4):
                for yp in range(4):
                    prod = (
                        bit(mask, x, y)
                        * bit(mask, xp, y)
                        * bit(mask, x, yp)
                        * bit(mask, xp, yp)
                    )
                    c += prod == -1
    return c


def main() -> None:
    assertions = 0
    max_defect = Fraction(0)
    max_best_error = Fraction(0)
    for mask in range(1 << 16):
        errors = [mismatch_count(mask, x0, y0) for x0 in range(4) for y0 in range(4)]
        defect_count = rectangle_defect_count(mask)

        # Sum over the 16 anchors and 16 query points has the same 256
        # ordered quadruples as the rectangle-defect definition.
        assert sum(errors) == defect_count
        assertions += 1

        rho = Fraction(defect_count, 4**4)
        best = Fraction(min(errors), 4**2)
        assert best <= rho
        assertions += 1

        if defect_count == 0:
            assert min(errors) == 0
            assertions += 1

        max_defect = max(max_defect, rho)
        max_best_error = max(max_best_error, best)

    print("rectangle interface exhaustive check: PASS")
    print("tables_checked=65536")
    print(f"assertions={assertions}")
    print(f"max_rectangle_defect={max_defect}")
    print(f"max_best_anchor_error={max_best_error}")
    print("scope=all Boolean sign tables on a 4x4 product cube; exact integer/Fraction arithmetic")


if __name__ == "__main__":
    main()
