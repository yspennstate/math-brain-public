from fractions import Fraction
from math import comb


def atom_probability(m, k, r, j):
    numerator = comb(j + r - 1, r - 1) * comb(m - j + k - r, k - r)
    denominator = comb(m + k, k)
    return Fraction(numerator, denominator)


def envelope(m, k):
    return Fraction(m * k, (m + k) * (m + k - 1))


def verify(max_m=60):
    cases = 0
    global_max = Fraction(0, 1)
    argmax = None
    for m in range(2, max_m + 1):
        for k in range(1, m + 1):
            env = envelope(m, k)
            assert env <= Fraction(1, 3)
            for r in range(1, k + 1):
                for j in range(1, m):
                    q = atom_probability(m, k, r, j)
                    cases += 1
                    assert q <= env
                    assert q <= Fraction(1, 3)
                    if q > global_max:
                        global_max = q
                        argmax = (m, k, r, j)
    print("POS3_AUTONOMOUS_CHAIN_K_LE_M_CHECK_PASS")
    print(f"m_range=2..{max_m}")
    print(f"exact_cases={cases}")
    print(f"global_max={global_max}")
    print(f"argmax={argmax}")
    print("envelope_m2_k2=" + str(envelope(2, 2)))
    print("envelope_m3_k3=" + str(envelope(3, 3)))
    print("envelope_m6_k4=" + str(envelope(6, 4)))


if __name__ == "__main__":
    verify()
