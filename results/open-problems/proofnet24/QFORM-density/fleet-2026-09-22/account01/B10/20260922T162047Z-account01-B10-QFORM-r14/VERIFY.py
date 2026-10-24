from fractions import Fraction


def check(K):
    assert K >= 2
    w = [Fraction(2, 3**k) for k in range(1, K)]
    w.append(Fraction(1, 3**(K-1)))
    assert sum(w, Fraction(0, 1)) == 1

    residual = Fraction(1, 1)
    det_product = Fraction(1, 1)
    for idx, wk in enumerate(w, start=1):
        h = wk / residual
        if idx < K:
            assert h == Fraction(2, 3)
            det_product *= 1 - h
            residual -= wk
            assert residual == Fraction(1, 3**idx)
            assert det_product == residual
        else:
            assert h == 1
            residual -= wk
            assert residual == 0

    # New theorem's universal exact-rank-three constant is < 9.525.
    C = 3 * 2 ** (5 / 3)
    assert C < 9.525
    return C


for K in range(2, 33):
    C = check(K)

print("QFORM_GROUPED_ISOTROPIC_CASCADE_CHECK_PASS")
print("checked_K=2..32")
print("C_grouped=%.12f" % C)
