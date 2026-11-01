from fractions import Fraction as F


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


# F(lambda)=(1+lambda+lambda^2)(2-lambda)
lhs = poly_mul([F(1), F(1), F(1)], [F(2), F(-1)])
rhs = [F(2), F(1), F(1), F(-1)]
assert lhs == rhs
# F(lambda)-2=lambda(1+lambda-lambda^2)
assert [lhs[i] - (F(2) if i == 0 else F(0)) for i in range(len(lhs))] == [F(0), F(1), F(1), F(-1)]


def hdiff(p, q, r, s, t):
    return max(p, r + t) + max(q, s - t)


# Exact finite self-check of the piecewise-linear fibre algebra.
# This is NOT an exhaustive certificate for convex bodies and is not used as the theorem proof.
vals = [F(-1, 2), F(-1, 4), F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
count = 0
for p in vals:
    for q in vals:
        wa = p + q
        if wa < 0 or wa > 1:
            continue
        for r in vals:
            for s in vals:
                wc = r + s
                if wc < 0 or wc > 1:
                    continue
                lo = p + s - F(1)
                hi = F(1) - r - q
                assert hi - lo == F(2) - wa - wc
                assert hi >= lo
                assert hdiff(p, q, r, s, lo) == 1
                assert hdiff(p, q, r, s, hi) == 1
                alpha = p - r
                beta = s - q
                t0 = (alpha + beta) / 2
                assert hdiff(p, q, r, s, t0) == max(wa, wc)
                count += 1


def class_bound(lam):
    assert F(0) <= lam <= F(1)
    return F(1, 3) * (F(1) + lam + lam * lam) * (F(2) - lam)


samples = [F(0), F(1, 5), F(1, 2), F(3, 4), F(1)]
for lam in samples:
    b = class_bound(lam)
    defect = b - F(2, 3)
    assert defect == F(1, 3) * lam * (F(1) + lam - lam * lam)
    assert b >= F(2, 3)
    if lam > 0:
        assert b > F(2, 3)

print("POLY_F =", lhs)
print("EXACT_FIBRE_TUPLES_CHECKED =", count)
for lam in samples:
    print("lambda =", lam, "class_bound =", class_bound(lam), "defect =", class_bound(lam) - F(2, 3))
print("ALL_EXACT_CHECKS_PASS = True")
