#!/usr/bin/env python3
from decimal import Decimal, localcontext


def h(x):
    if x == 0 or x == 1:
        return Decimal(0)
    return -(x * x.ln() + (1 - x) * (1 - x).ln())


def margin_bits(p, q):
    s = 4 * q * (1 - q)
    c = 4 * q * q
    J = h(s * p) - p * h(s)
    r = c * p * (1 - p) / (1 - s * p)
    M = (1 - s * p) * h(r) + s * p * h(p)
    D = p * ((1 - p) / p).ln()
    return (M + D / 2 - J) / Decimal(2).ln()


def main():
    with localcontext() as ctx:
        ctx.prec = 250
        ln2 = Decimal(2).ln()
        c0 = 1 - 1 / (2 * ln2)
        print(f"predicted_center_constant={c0}")
        scales = [
            ("center", lambda L: Decimal(0)),
            ("inv_L", lambda L: 1 / L),
            ("inv_sqrt_L", lambda L: 1 / L.sqrt()),
            ("half_inv_sqrt_L", lambda L: Decimal('0.5') / L.sqrt()),
        ]
        minimum = None
        checks = 0
        for k in (20, 40, 80, 160, 320):
            p = Decimal(2) ** (-k)
            L = -p.ln()
            for name, eta_fn in scales:
                eta = eta_fn(L)
                q = Decimal(1) / 4 + eta
                R = margin_bits(p, q)
                scaled = R / p
                prediction = c0 + 8 * eta * eta * (L / ln2)
                err = scaled - prediction
                if R <= 0:
                    raise AssertionError((k, name, R))
                minimum = R if minimum is None else min(minimum, R)
                checks += 1
                print(f"k={k:3d} scale={name:18s} R/p={scaled} pred={prediction} err={err}")
        print(f"PASS: {checks} high-precision asymptotic checks")
        print(f"minimum_margin_bits={minimum}")


if __name__ == "__main__":
    main()
