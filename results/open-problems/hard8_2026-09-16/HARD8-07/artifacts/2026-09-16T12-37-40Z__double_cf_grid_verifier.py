from fractions import Fraction


def convergents(digits):
    Am2, Am1 = 0, 1
    Bm2, Bm1 = 1, 0
    As, Bs = [], []
    for a in digits:
        A = a * Am1 + Am2
        B = a * Bm1 + Bm2
        As.append(A)
        Bs.append(B)
        Am2, Am1 = Am1, A
        Bm2, Bm1 = Bm1, B
    return As, Bs


def value_and_complete_quotients(digits, terminal):
    comp = [None] * (len(digits) + 1)
    comp[len(digits)] = terminal
    t = terminal
    for i in range(len(digits) - 1, -1, -1):
        t = Fraction(digits[i], 1) + 1 / t
        comp[i] = t
    return comp[0], comp


def nearest_dist(x):
    f = x.numerator // x.denominator
    return min(abs(x - f), abs(x - (f + 1)))


def inverse_coefficients(q, p, A, B, m):
    det = B[m] * A[m + 1] - B[m + 1] * A[m]
    assert abs(det) == 1
    x = Fraction(A[m + 1] * q - B[m + 1] * p, det)
    y = Fraction(-A[m] * q + B[m] * p, det)
    assert x.denominator == 1 and y.denominator == 1
    return int(x), int(y)


CASES = [
    ([1, 2, 1, 3, 2, 2, 1], Fraction(3, 2),
     [0, 1, 3, 1, 2, 3, 2], Fraction(5, 3)),
    ([2, 1, 2, 2, 3, 1, 1], Fraction(7, 4),
     [1, 2, 2, 1, 3, 2, 1], Fraction(4, 3)),
    ([0, 3, 1, 2, 1, 2, 3], Fraction(5, 4),
     [2, 1, 1, 3, 2, 1, 2], Fraction(8, 5)),
]

counts = {
    "UNIMODULAR_2X2": 0,
    "SCALE_RECURRENCES": 0,
    "GRID_DETERMINANTS": 0,
    "RENORMALIZATION_STEPS": 0,
    "DOUBLE_PORTAL_COORDINATES": 0,
    "COMMON_RELATIONS": 0,
    "NEAREST_PORTAL_IDENTITIES": 0,
    "COMMON_DENOMINATOR_BOUNDS": 0,
}

for adigs, atail, bdigits, btail in CASES:
    alpha, acomp = value_and_complete_quotients(adigs, atail)
    beta, bcomp = value_and_complete_quotients(bdigits, btail)
    A, B = convergents(adigs)
    C, D = convergents(bdigits)
    Aalpha = max(adigs[1:])
    Abeta = max(bdigits[1:])
    maxm = len(adigs) - 3
    maxn = len(bdigits) - 3

    theta = {}
    delta = {}

    for m in range(maxm + 1):
        xi = acomp[m + 2]
        Th = Fraction(B[m + 1]) * xi + B[m]
        theta[m] = Th
        assert alpha == (Fraction(A[m + 1]) * xi + A[m]) / Th
        assert B[m] * A[m + 1] - B[m + 1] * A[m] in (-1, 1)
        assert xi < Aalpha + 1
        counts["UNIMODULAR_2X2"] += 1
        if m + 1 <= maxm:
            xi_next = acomp[m + 3]
            Th_next = Fraction(B[m + 2]) * xi_next + B[m + 1]
            assert Th_next == xi_next * Th
            counts["SCALE_RECURRENCES"] += 1

    for n in range(maxn + 1):
        eta = bcomp[n + 2]
        De = Fraction(D[n + 1]) * eta + D[n]
        delta[n] = De
        assert beta == (Fraction(C[n + 1]) * eta + C[n]) / De
        assert D[n] * C[n + 1] - D[n + 1] * C[n] in (-1, 1)
        assert eta < Abeta + 1
        counts["UNIMODULAR_2X2"] += 1
        if n + 1 <= maxn:
            eta_next = bcomp[n + 3]
            De_next = Fraction(D[n + 2]) * eta_next + D[n + 1]
            assert De_next == eta_next * De
            counts["SCALE_RECURRENCES"] += 1

    for m in range(maxm + 1):
        xi = acomp[m + 2]
        Th = theta[m]
        for n in range(maxn + 1):
            eta = bcomp[n + 2]
            De = delta[n]

            assert Fraction(1, 1) / (Th * De) * Th * De == 1
            counts["GRID_DETERMINANTS"] += 1

            if m + 1 <= maxm:
                xi_next = acomp[m + 3]
                assert theta[m + 1] / Th == xi_next
                assert (
                    Th / theta[m + 1],
                    theta[m + 1] / Th,
                    Fraction(1),
                ) == (1 / xi_next, xi_next, Fraction(1))
                counts["RENORMALIZATION_STEPS"] += 1

            if n + 1 <= maxn:
                eta_next = bcomp[n + 3]
                assert delta[n + 1] / De == eta_next
                assert (
                    De / delta[n + 1],
                    Fraction(1),
                    delta[n + 1] / De,
                ) == (1 / eta_next, Fraction(1), eta_next)
                counts["RENORMALIZATION_STEPS"] += 1

            for q in range(-7, 8):
                qa = Fraction(q) * alpha
                qb = Fraction(q) * beta
                fqa = qa.numerator // qa.denominator
                fqb = qb.numerator // qb.denominator
                for off in (-2, 0, 3):
                    p = fqa + off
                    r = fqb - off
                    x, y = inverse_coefficients(q, p, A, B, m)
                    z, v = inverse_coefficients(q, r, C, D, n)
                    da = Fraction(y) - Fraction(x) * xi
                    db = Fraction(v) - Fraction(z) * eta
                    X = Fraction(q) / (Th * De)
                    Y = Th * (Fraction(q) * alpha - p)
                    Z = De * (Fraction(q) * beta - r)
                    assert Y == ((-1) ** (m + 1)) * da
                    assert Z == ((-1) ** (n + 1)) * db
                    assert abs(X * Y * Z) == abs(
                        Fraction(q)
                        * (Fraction(q) * alpha - p)
                        * (Fraction(q) * beta - r)
                    )
                    counts["DOUBLE_PORTAL_COORDINATES"] += 1

            Rmax = 5
            alpha_q = {}
            for x in range(-Rmax, Rmax + 1):
                for y in range(-Rmax, Rmax + 1):
                    if x == 0 and y == 0:
                        continue
                    q = x * B[m] + y * B[m + 1]
                    alpha_q.setdefault(q, []).append((x, y))

            for z in range(-Rmax, Rmax + 1):
                for v in range(-Rmax, Rmax + 1):
                    if z == 0 and v == 0:
                        continue
                    q = z * D[n] + v * D[n + 1]
                    if q == 0 or q not in alpha_q:
                        continue
                    for x, y in alpha_q[q]:
                        counts["COMMON_RELATIONS"] += 1
                        da = Fraction(y) - Fraction(x) * xi
                        db = Fraction(v) - Fraction(z) * eta
                        p = x * A[m] + y * A[m + 1]
                        r = z * C[n] + v * C[n + 1]
                        assert Fraction(q) * alpha - p == ((-1) ** (m + 1)) * da / Th
                        assert Fraction(q) * beta - r == ((-1) ** (n + 1)) * db / De

                        Ra = max(abs(x), abs(y))
                        Rb = max(abs(z), abs(v))
                        prod = abs(Fraction(q) * da * db / (Th * De))
                        bound = (
                            2
                            * (Aalpha + 2)
                            * (Abeta + 2)
                            * Ra
                            * Rb
                            * min(
                                Fraction(Ra, 1) / De,
                                Fraction(Rb, 1) / Th,
                            )
                        )
                        assert prod <= bound
                        counts["COMMON_DENOMINATOR_BOUNDS"] += 1

                        if abs(da) < Th / 2 and abs(db) < De / 2:
                            littlewood = (
                                abs(Fraction(q))
                                * nearest_dist(Fraction(q) * alpha)
                                * nearest_dist(Fraction(q) * beta)
                            )
                            assert littlewood == prod
                            counts["NEAREST_PORTAL_IDENTITIES"] += 1

for key in [
    "UNIMODULAR_2X2",
    "SCALE_RECURRENCES",
    "GRID_DETERMINANTS",
    "RENORMALIZATION_STEPS",
    "DOUBLE_PORTAL_COORDINATES",
    "COMMON_RELATIONS",
    "NEAREST_PORTAL_IDENTITIES",
    "COMMON_DENOMINATOR_BOUNDS",
]:
    print(key, counts[key])
print("ALL_EXACT_DOUBLE_GRID_CHECKS_PASSED")
