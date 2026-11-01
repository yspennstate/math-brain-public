from fractions import Fraction
from math import comb


def atom_probability(m, k, r, j):
    """
    Conditional probability, inside one autonomous-chain deletion fiber,
    that exactly j of the m chain elements precede the r-th central neutral
    when k central neutrals are present.
    """
    numerator = comb(j + r - 1, r - 1) * comb(m - j + k - r, k - r)
    denominator = comb(m + k, k)
    return Fraction(numerator, denominator)


def verify(max_m=200):
    cases = 0
    global_max = Fraction(0, 1)
    argmax = None
    for m in range(2, max_m + 1):
        alpha = Fraction(2 * m, (m + 1) * (m + 2))
        assert alpha <= Fraction(1, 3)
        for k in (1, 2):
            for r in range(1, k + 1):
                for j in range(1, m):
                    q = atom_probability(m, k, r, j)
                    cases += 1
                    if q > global_max:
                        global_max = q
                        argmax = (m, k, r, j)
                    assert q <= Fraction(1, 3)
                    if k == 1:
                        assert q == Fraction(1, m + 1)
                    else:
                        assert q <= alpha
    print("POS3_TWO_CENTRAL_NEUTRAL_CHAIN_CHECK_PASS")
    print(f"m_range=2..{max_m}")
    print(f"exact_cases={cases}")
    print(f"global_max={global_max}")
    print(f"argmax={argmax}")
    print("m=2_k2_internal=" +
          repr([(r, 1, atom_probability(2, 2, r, 1)) for r in (1, 2)]))
    print("m=3_k2_bound=" + str(Fraction(6, 20)))


if __name__ == "__main__":
    verify()
