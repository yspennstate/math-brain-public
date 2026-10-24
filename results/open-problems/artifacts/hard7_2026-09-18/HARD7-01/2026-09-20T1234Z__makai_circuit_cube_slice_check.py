from fractions import Fraction
from math import factorial

Q = Fraction


def det(M):
    A = [list(map(Q, row)) for row in M]
    n = len(A)
    out = Q(1)
    for j in range(n):
        piv = next((i for i in range(j, n) if A[i][j]), None)
        if piv is None:
            return Q(0)
        if piv != j:
            A[j], A[piv] = A[piv], A[j]
            out = -out
        p = A[j][j]
        out *= p
        for k in range(j, n):
            A[j][k] /= p
        for i in range(j + 1, n):
            f = A[i][j]
            if f:
                for k in range(j, n):
                    A[i][k] -= f * A[j][k]
    return out


def center_density(weights):
    """Exact density at 1 for sum_i weights[i] * U_i, U_i~Unif[0,1]."""
    m = len(weights)
    P = Q(1)
    for w in weights:
        P *= w
    num = Q(0)
    for mask in range(1 << m):
        s = Q(0)
        parity = 0
        for i, w in enumerate(weights):
            if mask >> i & 1:
                s += w
                parity ^= 1
        r = Q(1) - s
        if r > 0:
            num += (-1 if parity else 1) * r ** (m - 1)
    return num / (factorial(m - 1) * P)


def comps_bounded(total, m, maxv, prefix=()):
    if m == 1:
        if 1 <= total <= maxv:
            yield prefix + (total,)
        return
    lo = max(1, total - maxv * (m - 1))
    hi = min(maxv, total - (m - 1))
    for x in range(lo, hi + 1):
        yield from comps_bounded(total - x, m - 1, maxv, prefix + (x,))


def check_bipyramid(a1, a2, a3, t):
    """Exact cofactor/circuit check on a rational triangular bipyramid."""
    assert a1 + a2 + a3 == 1 and 0 < t < 1 and min(a1, a2, a3) > 0
    vs = [
        [Q(0), Q(0), Q(0)],
        [Q(1), Q(0), Q(0)],
        [Q(0), Q(1), Q(0)],
        [a2, a3, 1 - t],
        [a2, a3, -t],
    ]
    c = [a1, a2, a3, -t, -(1 - t)]
    A = [v + [Q(1)] for v in vs]
    minors = []
    for i in range(5):
        M = [A[j] for j in range(5) if j != i]
        minors.append(abs(det(M)))
    assert minors == [abs(x) for x in c], (minors, c)
    weights = [abs(x) for x in c]
    f = center_density(weights)
    predicted_product = Q(2, 3) * f
    return weights, f, predicted_product


# 1. Exact determinant/cofactor checks for five-vertex 3D circuits.
examples = [
    (Q(1, 3), Q(1, 3), Q(1, 3), Q(1, 2)),
    (Q(4, 5), Q(1, 10), Q(1, 10), Q(1, 2)),
    (Q(1, 4), Q(1, 4), Q(1, 2), Q(1, 3)),
    (Q(2, 7), Q(3, 7), Q(2, 7), Q(2, 5)),
]
for ex in examples:
    ws, f, p = check_bipyramid(*ex)
    assert f >= 1 and p >= Q(2, 3)
    print("BIPYRAMID", ex, "weights=", ws, "f_mean=", f,
          "Makai_product_prediction=", p)

# 2. Exhaustive exact rational self-check of f_W(1) >= 1 on the stated grid.
grand = 0
equal = 0
strict_no_unit = 0
for m in range(3, 8):
    count = 0
    mn = None
    arg = None
    for q in range(2, 11):
        for parts in comps_bounded(2 * q, m, q):
            ws = [Q(k, q) for k in parts]
            f = center_density(ws)
            assert f >= 1, (m, q, parts, f)
            count += 1
            grand += 1
            if f == 1:
                equal += 1
            if max(parts) < q:
                assert f > 1, (m, q, parts, f)
                strict_no_unit += 1
            if mn is None or f < mn:
                mn = f
                arg = (q, parts)
    print("ENUM", "m=", m, "count=", count, "min_f=", mn, "arg=", arg)
print("ENUM_TOTAL", grand, "EQUALITY_CASES_SAMPLED", equal,
      "STRICT_NO_UNIT_CASES", strict_no_unit)

# 3. Exact three-width identity used at the terminal stage of the proof.
triple_count = 0
for q in range(2, 31):
    for parts in comps_bounded(2 * q, 3, q):
        a, b, c = [Q(k, q) for k in parts]
        f = center_density([a, b, c])
        x, y, z = 1 - a, 1 - b, 1 - c
        rhs = (x * y + y * z + z * x) / ((x + y) * (y + z) * (z + x))
        assert f == rhs
        assert rhs >= 1
        triple_count += 1
print("THREE_WIDTH_IDENTITY_CASES", triple_count)

# 4. Exact grid check of the pair-merging peakedness comparison.
pair_checks = 0
for den in range(2, 21):
    for ia in range(1, den + 1):
        for ib in range(1, ia + 1):
            a, b = Q(ia, den), Q(ib, den)
            if a + b > 1:
                continue
            for k in range(0, ia + ib + 1):
                r = Q(k, 2 * den)
                merged = min(Q(1), 2 * r / (a + b))
                if r <= (a - b) / 2:
                    pair = 2 * r / a
                elif r <= (a + b) / 2:
                    d = a + b - 2 * r
                    pair = 1 - d * d / (4 * a * b)
                else:
                    pair = Q(1)
                assert pair >= merged, (a, b, r, pair, merged)
                pair_checks += 1
print("PAIR_PEAKEDNESS_GRID_CASES", pair_checks)

print("ALL_EXACT_CHECKS_PASS = True")
