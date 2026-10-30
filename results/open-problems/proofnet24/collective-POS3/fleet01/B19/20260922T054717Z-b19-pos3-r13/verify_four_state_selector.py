from fractions import Fraction


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def E_R(N):
    if N < 8:
        raise ValueError("R_N formula used only for N>=8")
    return 8 * fib(N + 1) - 13 * fib(N - 7)


def q_R(N, i):
    # Exact adjacent-inversion probability from fleet04/B11 r15.
    return Fraction(E_R(i) * fib(N - i - 1), E_R(N))


def main(limit=50):
    checked = 0
    equality_examples = []
    min_ratio = None
    min_data = None

    # Exact integer regression for the local five-label count cone:
    # E=3a+2b+2c+t, b<=a, t<=b,c.
    for a in range(limit + 1):
        for b in range(a + 1):
            for c in range(limit + 1):
                for t in range(min(b, c) + 1):
                    E = 3 * a + 2 * b + 2 * c + t
                    if E == 0:
                        continue
                    vals = (2 * c + t, a + b, a + c, 2 * b + t)
                    M = max(vals)
                    checked += 1
                    assert 11 * M >= 3 * E
                    if 11 * M == 3 * E:
                        assert 11 * a == 2 * E
                        assert 11 * b == E
                        assert 11 * c == E
                        assert 11 * t == E
                        if len(equality_examples) < 4:
                            equality_examples.append((a, b, c, t, E, vals))
                    ratio = Fraction(M, E)
                    if min_ratio is None or ratio < min_ratio:
                        min_ratio = ratio
                        min_data = (a, b, c, t, E, vals)

    # Source-valid guard from the fleet04/B11 R_N family: four
    # consecutive exact-two corridor minorities can all stay below 3/10.
    N = 30
    qs = [q_R(N, i) for i in (12, 13, 14, 15)]
    assert all(Fraction(3, 11) < x < Fraction(3, 10) for x in qs)

    print("POS3_FOUR_STATE_SELECTOR_CHECK_PASS")
    print("integer_tuples_checked", checked)
    print("minimum_ratio", f"{min_ratio.numerator}/{min_ratio.denominator}")
    print("minimum_witness", min_data)
    print("equality_examples", equality_examples)
    print("R30_total_extensions", E_R(N))
    print("R30_q12_q15", [f"{q.numerator}/{q.denominator}" for q in qs])
    print("R30_decimal", [round(float(q), 9) for q in qs])


if __name__ == "__main__":
    main()
