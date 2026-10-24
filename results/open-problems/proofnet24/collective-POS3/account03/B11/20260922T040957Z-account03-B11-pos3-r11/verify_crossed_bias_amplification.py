from fractions import Fraction


def count_word(intervals, word):
    total = 0

    def rec(k, last_gap):
        nonlocal total
        if k == len(word):
            total += 1
            return
        lo, hi = intervals[word[k]]
        for gap in range(max(lo, last_gap), hi + 1):
            rec(k + 1, gap)

    rec(0, -10**9)
    return total


WORDS = [
    ("d", "y", "x", "u"),  # n1: y before x
    ("d", "x", "y", "u"),  # n2
    ("d", "x", "u", "y"),  # n3
    ("x", "u", "d", "y"),  # n4: u before d
    ("x", "d", "u", "y"),  # n5
    ("x", "d", "y", "u"),  # n6
]


def interval_regression():
    fibers = 0
    premise_fibers = 0
    for left in range(4):
        for right in range(left, 4):
            middle = (left, right)
            for dl in range(left + 1):
                for du in range(dl, right + 1):
                    lower = (dl, du)
                    if not (dl <= left and du <= right):
                        continue
                    for ul in range(left, 5):
                        for uu in range(max(ul, right), 5):
                            upper = (ul, uu)
                            intervals = {
                                "x": middle,
                                "y": middle,
                                "d": lower,
                                "u": upper,
                            }
                            n1, n2, n3, n4, n5, n6 = [
                                count_word(intervals, word) for word in WORDS
                            ]
                            E = n1 + n2 + n3 + n4 + n5 + n6
                            if E == 0:
                                continue
                            fibers += 1

                            # Exact adjacent-swap facts used in the proof.
                            assert n1 == n2
                            assert n4 <= n5

                            p_xy = Fraction(E - n1, E)
                            alpha = Fraction(n4 + n5 + n6, E)  # Pr(x<d)
                            beta = Fraction(n3 + n4 + n5, E)   # Pr(u<y)
                            gamma = Fraction(n4, E)             # Pr(u<d)
                            eta = Fraction(n4 + n5, E)

                            assert 2 * p_xy - 1 == alpha + beta - eta
                            assert eta >= 2 * gamma

                            if (
                                p_xy > Fraction(2, 3)
                                and alpha < Fraction(1, 3)
                                and beta < Fraction(1, 3)
                            ):
                                premise_fibers += 1
                                assert p_xy < Fraction(5, 6)
                                assert 1 - gamma > p_xy + Fraction(1, 6)

    return fibers, premise_fibers


def transitive_closure(n, relations):
    reach = [0] * n
    for a, b in relations:
        reach[a] |= 1 << b
    for k in range(n):
        for i in range(n):
            if (reach[i] >> k) & 1:
                reach[i] |= reach[k]
    return reach


def linear_extensions(n, relations):
    reach = transitive_closure(n, relations)
    pred = [0] * n
    for j in range(n):
        for i in range(n):
            if (reach[i] >> j) & 1:
                pred[j] |= 1 << i

    out = []

    def rec(mask, seq):
        if mask == (1 << n) - 1:
            out.append(tuple(seq))
            return
        for v in range(n):
            if ((mask >> v) & 1) == 0 and (pred[v] & ~mask) == 0:
                rec(mask | (1 << v), seq + [v])

    rec(0, [])
    return reach, out


def probability(exts, a, b):
    return Fraction(sum(ext.index(a) < ext.index(b) for ext in exts), len(exts))


def six_point_regression():
    # A width-three source-valid local adversary to any claim that one
    # crossed expansion already forces balance.  It is NOT a POS3
    # counterexample: (0,2) and (4,5) are balanced.
    relations = [
        (0, 1), (0, 3), (0, 4), (0, 5),
        (1, 4), (1, 5),
        (2, 3), (2, 4),
        (3, 4),
    ]
    _, exts = linear_extensions(6, relations)
    x, y, d, u = 1, 3, 2, 5

    E = len(exts)
    p_xy = probability(exts, x, y)
    alpha = probability(exts, x, d)
    beta = probability(exts, u, y)
    p_du = probability(exts, d, u)
    escape_1 = probability(exts, 0, 2)
    escape_2 = probability(exts, 4, 5)

    assert E == 14
    assert p_xy == Fraction(5, 7)
    assert alpha == Fraction(2, 7)
    assert beta == Fraction(2, 7)
    assert p_du == Fraction(13, 14)
    assert p_du > p_xy + Fraction(1, 6)
    assert escape_1 == Fraction(9, 14)
    assert escape_2 == Fraction(5, 14)

    return E, p_xy, alpha, beta, p_du, escape_1, escape_2


if __name__ == "__main__":
    fibers, premise_fibers = interval_regression()
    E, p_xy, alpha, beta, p_du, escape_1, escape_2 = six_point_regression()
    print("interval_fibers", fibers)
    print("premise_fibers", premise_fibers)
    print("six_point_extensions", E)
    print("endpoint_p", p_xy)
    print("lower_fringe_minority", alpha)
    print("upper_fringe_minority", beta)
    print("outer_majority", p_du)
    print("outer_minus_endpoint_minus_one_sixth", p_du - p_xy - Fraction(1, 6))
    print("balanced_escape_0_2", escape_1)
    print("balanced_escape_4_5", escape_2)
    print("POS3_CROSSED_BIAS_AMPLIFICATION_CHECK_PASS")
