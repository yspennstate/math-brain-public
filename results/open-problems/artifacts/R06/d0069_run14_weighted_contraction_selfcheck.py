from fractions import Fraction


def iparts(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for k in range(min(max_part, n), 0, -1):
        for tail in iparts(n-k, k):
            yield (k,) + tail


def main():
    # Degree-5 nonsimple parallel-class partitions.
    p5 = [p for p in iparts(5) if p != (5,) and p != (1, 1, 1, 1, 1)]
    expected5 = [(4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1)]
    assert p5 == expected5

    # R06-D0069-T2 local critical weights after contracting the triple matching
    # in a [3,1,1] graph. At z=1/2:
    #   same-endpoint transition: 1/2;
    #   switch-endpoint transition: 3*(1/2)^2 = 3/4.
    w31 = [Fraction(1, 2), Fraction(3, 4), Fraction(3, 4)]
    child31 = {
        0: min(w31),
        1: sum(sorted(w31)[:2]),
        2: sum(w31),
    }
    assert child31 == {
        0: Fraction(1, 2),
        1: Fraction(5, 4),
        2: Fraction(2, 1),
    }

    # Symbolic product lemma used in the proof:
    # if n2-n0 >= -1, then
    # (1/2)^n0 (5/4)^n1 2^n2
    # = 2^(n2-n0) (5/4)^n1 >= 1/2.
    # This loop is only an exact finite self-check of that algebra; the report
    # contains the all-n proof.
    for n0 in range(80):
        for n1 in range(80):
            for n2 in range(80):
                if n2 - n0 >= -1:
                    prod = (
                        Fraction(1, 2) ** n0
                        * Fraction(5, 4) ** n1
                        * Fraction(2, 1) ** n2
                    )
                    assert prod >= Fraction(1, 2)

    # Degree-6 quotient partitions after contracting a double matching in a
    # [2,1,1,1] graph. A quotient parallel class has size at most 4 because
    # between two 2-point fibers there are only four possible simple edges.
    p6 = [p for p in iparts(6) if max(p) <= 4]
    expected6 = [
        (4, 2),
        (4, 1, 1),
        (3, 3),
        (3, 2, 1),
        (3, 1, 1, 1),
        (2, 2, 2),
        (2, 2, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1),
    ]
    assert p6 == expected6

    covered6 = {
        (4, 2): "degree-2 weighted line",
        (3, 3): "degree-2 weighted line",
        (2, 2, 2): "double of a simple cubic skeleton",
        (2, 1, 1, 1, 1): "simple skeleton has degree 5",
        (1, 1, 1, 1, 1, 1): "simple skeleton has degree 6",
        (4, 1, 1): "contract multiplicity-4 matching to degree 4 + weighted-blue lemma",
        (3, 2, 1): "alternating (3,2)-factor + singleton matching block argument",
    }
    residual6 = [p for p in p6 if p not in covered6]
    assert residual6 == [(3, 1, 1, 1), (2, 2, 1, 1)]

    # [4,1,1] auxiliary local masses after contracting the multiplicity-4
    # matching. At z=1/2: no switch = 1/2; switch = 4*(1/2)^2 = 1.
    w411 = [Fraction(1, 2), Fraction(1, 1), Fraction(1, 1)]
    child411 = {
        0: min(w411),
        1: sum(sorted(w411)[:2]),
        2: sum(w411),
    }
    assert child411 == {
        0: Fraction(1, 2),
        1: Fraction(3, 2),
        2: Fraction(5, 2),
    }
    for n0 in range(80):
        for n1 in range(80):
            for n2 in range(80):
                if n2 - n0 >= -1:
                    prod = (
                        Fraction(1, 2) ** n0
                        * Fraction(3, 2) ** n1
                        * Fraction(5, 2) ** n2
                    )
                    assert prod >= Fraction(1, 2)

    # [3,2,1] critical factors. Inside the alternating 3/2 factor, every edge
    # has critical factor >=1; the outgoing singleton contributes 1/2, so the
    # two cycle arcs have total block contribution >=1.
    assert Fraction(3, 2) >= 1
    assert Fraction(2, 2) == 1
    assert Fraction(1, 2) + Fraction(1, 2) == 1

    # Degree-2 quotient-line cases: the alternating two-step products exceed 4.
    assert 4 * 2 == 8 > 4
    assert 3 * 3 == 9 > 4

    print("DEGREE5_TYPES", p5)
    print("TRIPLE_MATCHING_CHILD_MASSES", child31)
    print("DEGREE6_CONTRACTION_TYPES", p6)
    print("DEGREE6_COVERED", sorted(covered6))
    print("DEGREE6_RESIDUAL", residual6)
    print("FOUR_MATCHING_CHILD_MASSES", child411)
    print("EXACT_SELF_CHECK_PASS")


if __name__ == "__main__":
    main()
