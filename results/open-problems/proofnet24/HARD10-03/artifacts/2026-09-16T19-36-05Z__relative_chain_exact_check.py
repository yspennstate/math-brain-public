from collections import defaultdict
from fractions import Fraction

DIRS = [
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
]


def add(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def sub(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def edge(a, b):
    return tuple(sorted((a, b)))


def relative_transition_rates(z):
    """Exact rates for Z=Y-X from rate-one clocks on lattice edges incident to X or Y."""
    X = (0, 0, 0)
    Y = z
    edges = set()
    for d in DIRS:
        edges.add(edge(X, add(X, d)))
        edges.add(edge(Y, add(Y, d)))

    rates = defaultdict(int)
    for a, b in edges:
        X2, Y2 = X, Y
        if X == a:
            X2 = b
        elif X == b:
            X2 = a
        if Y == a:
            Y2 = b
        elif Y == b:
            Y2 = a
        z2 = sub(Y2, X2)
        if z2 != z:
            rates[z2] += 1
    return dict(rates)


def neg(z):
    return tuple(-x for x in z)


def main():
    # Nonadjacent representatives: every +/- coordinate relative move has rate 2.
    for z in [(2, 0, 0), (1, 1, 0), (3, -1, 2)]:
        rates = relative_transition_rates(z)
        assert sum(rates.values()) == 12, (z, rates)
        assert len(rates) == 6, (z, rates)
        for d in DIRS:
            zp = add(z, d)
            assert rates.get(zp) == 2, (z, zp, rates)

    # Every adjacent coordinate state: five retained nearest-neighbor moves at rate 2,
    # plus the shared-edge swap z -> -z at rate 1.
    for z in DIRS:
        rates = relative_transition_rates(z)
        assert sum(rates.values()) == 11, (z, rates)
        assert rates.get(neg(z)) == 1, (z, rates)
        expected = [add(z, d) for d in DIRS if add(z, d) != (0, 0, 0)]
        assert len(expected) == 5
        for zp in expected:
            assert rates.get(zp) == 2, (z, zp, rates)
        assert len(rates) == 6, (z, rates)

    # Exact exponent arithmetic in the NEW-L107 scale corollary.
    q_exp = Fraction(1, 8)
    r_exp = Fraction(1, 8)
    interval_exp = Fraction(3, 16)
    contamination_exp = 2 * q_exp + 2 * r_exp
    phase_count_exp = 1 - interval_exp
    fraction_decay_exp = phase_count_exp - contamination_exp

    assert contamination_exp == Fraction(1, 2)
    assert phase_count_exp == Fraction(13, 16)
    assert fraction_decay_exp == Fraction(5, 16)

    print("adjacent_total_rate=11")
    print("nonadjacent_total_rate=12")
    print(f"contamination_exponent={contamination_exp}")
    print(f"phase_count_exponent={phase_count_exp}")
    print(f"fraction_decay_exponent={fraction_decay_exp}")
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
