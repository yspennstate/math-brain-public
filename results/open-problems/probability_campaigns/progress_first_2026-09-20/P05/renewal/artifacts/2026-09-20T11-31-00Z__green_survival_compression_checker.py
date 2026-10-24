from fractions import Fraction
from math import comb


def exact_green_and_terminal(n):
    """Exact killed Green table for the reverse pivotal walk from (n,n)."""
    dist = {(n, n): Fraction(1)}
    green = {}
    terminal = []  # (absorption time, terminal imbalance, probability)
    t = 0
    while dist:
        for st, p in dist.items():
            green[st] = green.get(st, Fraction(0)) + p

        nxt = {}
        for (a, b), p in dist.items():
            for da, db, pr in (
                (1, 1, Fraction(1, 2)),
                (1, 0, Fraction(1, 4)),
                (0, 1, Fraction(1, 4)),
            ):
                aa, bb = a - da, b - db
                pp = p * pr
                if aa <= 0 or bb <= 0:
                    terminal.append((t + 1, abs(aa - bb), pp))
                else:
                    nxt[(aa, bb)] = nxt.get((aa, bb), Fraction(0)) + pp
        dist = nxt
        t += 1
        assert t <= 2 * n
    return green, terminal


def compressed_difference_mass(n, k):
    """Exact one-dimensional compression H_n(k) from Theorem P05-R14.1."""
    total = Fraction(0)
    ak = abs(k)
    for u in range(ak, 2 * n):
        if (u + k) & 1:
            continue
        plus = (u + k) // 2
        if plus < 0 or plus > u:
            continue

        # Conditional on u non-diagonal steps, the difference is a length-u
        # simple symmetric random walk.
        p_walk = Fraction(comb(u, plus), 2**u)

        # c is the number of diagonal decrements.  Survival is exactly
        # 2c + u + |k| <= 2n-2.
        cmax = (2 * n - 2 - u - ak) // 2
        if cmax < 0:
            continue
        inner = Fraction(0)
        for c in range(cmax + 1):
            inner += Fraction(comb(c + u, c), 2 ** (c + u))
        total += p_walk * inner
    return total


def run():
    checked_difference_cells = 0
    for n in range(1, 9):
        green, terminal = exact_green_and_terminal(n)
        h_direct = {}
        for (a, b), p in green.items():
            h_direct[a - b] = h_direct.get(a - b, Fraction(0)) + p

        for k in range(-(n - 1), n):
            lhs = h_direct.get(k, Fraction(0))
            rhs = compressed_difference_mass(n, k)
            assert lhs == rhs, (n, k, lhs, rhs)
            checked_difference_cells += 1

        W = sum(green.values(), Fraction(0))
        E_tau = sum(Fraction(t) * p for t, h, p in terminal)
        E_H = sum(Fraction(h) * p for t, h, p in terminal)
        E_H2 = sum(Fraction(h * h) * p for t, h, p in terminal)

        # Occupation mass equals expected lifetime.
        assert W == E_tau
        # Exact stopped sum-coordinate martingale identity.
        assert Fraction(3, 2) * E_tau + E_H == 2 * n
        # Exact stopped difference-square martingale identity.
        assert E_H2 == Fraction(1, 2) * E_tau

        print(
            f"n={n}: W={W}, E[H]={E_H}, "
            f"difference_cells={2*n-1} PASS"
        )

    print(f"checked_difference_cells={checked_difference_cells}")
    print("EXACT_GREEN_SURVIVAL_COMPRESSION_PASS")


if __name__ == "__main__":
    run()
