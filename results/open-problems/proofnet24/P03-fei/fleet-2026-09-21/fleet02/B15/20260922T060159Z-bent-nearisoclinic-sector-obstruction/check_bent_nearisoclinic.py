from fractions import Fraction
import math

C = 6.521851214


def h2(x):
    if x == 0.0 or x == 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def parity(x):
    return x.bit_count() & 1


def bent_truth(r):
    # x=(u,v) in F_2^r x F_2^r; b(x)=(-1)^(u dot v).
    m = 2 * r
    mask = (1 << r) - 1
    vals = []
    for x in range(1 << m):
        u = x & mask
        v = x >> r
        vals.append(-1 if parity(u & v) else 1)
    return vals


def direct_exact_checks():
    for r in range(1, 5):
        m = 2 * r
        N = 1 << m
        b = bent_truth(r)
        W0 = fwht(b)
        target = 1 << r
        assert all(abs(w) == target for w in W0)

        # h flips only x=0, where b(0)=+1.
        g = list(b)
        g[0] *= -1
        W1 = fwht(g)
        assert all(w1 == w0 - 2 for w0, w1 in zip(W0, W1))

        plus = sum(w == target for w in W0)
        minus = N - plus
        assert plus == (N + target) // 2
        assert minus == (N - target) // 2

        # Exact spectral normalization and exact residual-coordinate influence.
        norm = sum(Fraction(w * w, N * N) for w in W1)
        assert norm == 1
        weighted = sum(Fraction(w * w * k.bit_count(), N * N)
                       for k, w in enumerate(W1))
        d = Fraction(1, N)
        assert weighted == Fraction(r, 1) * (1 + 4 * d)


def analytic_table():
    print("C", C)
    print("m d I_vertical local_L local_upper var_c child_slack_lower")
    for m in range(2, 22, 2):
        r = m // 2
        d = 2.0 ** (-m)
        s = math.sqrt(d)
        N = 1.0 / d
        n_plus = (N + 1.0 / s) / 2.0
        n_minus = (N - 1.0 / s) / 2.0

        I_vertical = 0.0
        H_branch = 0.0
        mean_theta = 0.0
        mean_c = 0.0
        total_T = 0.0
        cells = []
        for sigma, count in ((1.0, n_plus), (-1.0, n_minus)):
            A = 1.0 - 2.0 * sigma * s + 2.0 * d
            T = d * A
            theta = d / A
            branch_post = (1.0 - 4.0 * sigma * s + 4.0 * d) / (2.0 * A)
            c = (1.0 - 2.0 * sigma * s) / A
            weight = count * T
            total_T += weight
            mean_theta += weight * theta
            mean_c += weight * c
            H_branch += weight * h2(branch_post)
            I_vertical += weight * (
                theta * math.log2(theta / d)
                + (1.0 - theta) * math.log2((1.0 - theta) / (1.0 - d))
            )
            cells.append((weight, c))

        rho = 1.0 - 2.0 * d
        var_c = sum(weight * (c - rho) ** 2 for weight, c in cells)
        local_L = C * d - 1.0 - h2(d) + H_branch + I_vertical
        local_upper = d * (C - m + 40.0 * d)
        child_slack_lower = r * (C - 2.0) - 2.0

        assert abs(total_T - 1.0) < 1e-12
        assert abs(mean_theta - d) < 1e-12
        assert abs(mean_c - rho) < 1e-12
        if m >= 4:
            assert I_vertical <= 40.0 * d * d + 1e-15
            assert var_c <= 64.0 * d ** 3 + 1e-15
            assert local_L <= local_upper + 1e-12
        if m >= 8:
            assert local_L < 0.0

        print(
            m,
            f"{d:.12g}",
            f"{I_vertical:.12g}",
            f"{local_L:.12g}",
            f"{local_upper:.12g}",
            f"{var_c:.12g}",
            f"{child_slack_lower:.12g}",
        )


if __name__ == "__main__":
    direct_exact_checks()
    analytic_table()
    print("PASS")
