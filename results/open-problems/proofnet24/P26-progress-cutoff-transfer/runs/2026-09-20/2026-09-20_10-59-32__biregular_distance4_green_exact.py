from fractions import Fraction


def D2(K, k):
    return K * (K + 1) * k * k


def q2_num(x, K, k):
    return x * x - (2 * K + k + 1) * x + K * (K + 1)


def radial_counts(K, k):
    # Interior half-radius increments for one exact bigraph-distance-four move.
    return {
        -2: 1,
        -1: k - 1,
        0: (K - 1) * k,
        1: (k - 1) * K * k,
        2: K * K * k * k,
    }


# Generic exact identities on a parameter grid.
for K in range(2, 13):
    for k in range(2, K + 1):
        D = D2(K, k)
        counts = radial_counts(K, k)
        assert sum(counts.values()) == D

        v = Fraction(sum(j * c for j, c in counts.items()), D)
        assert v == Fraction((K * k - 1) * (2 * K * k + k + 1), D)

        M2 = Fraction(sum(j * j * c for j, c in counts.items()), D)
        assert M2 > 0 and v > 0

        # q_2(x)=1 has the Perron value as its unique nonnegative root.
        top = (K + 1) * (k + 1)
        assert q2_num(top, K, k) == D
        other = -K * (k - 1)
        assert q2_num(other, K, k) == D
        assert other < 0

        # Output tree benchmark strictly exceeds the inherited shell growth.
        assert (K * k) ** 2 < D - 1


# Concrete Eisenstein p=2 parameters: (9,3)-biregular, so K=8,k=2.
K, k = 8, 2
D = D2(K, k)
counts = radial_counts(K, k)
v = Fraction(sum(j * c for j, c in counts.items()), D)
M2 = Fraction(sum(j * j * c for j, c in counts.items()), D)
tau2 = M2 / (v ** 3)

# Adj-Ramanujan squared singular-value bulk is [2,18]; zero modes may occur.
q0 = Fraction(q2_num(0, K, k), D)
q_lo = Fraction(q2_num(2, K, k), D)
q_hi = Fraction(q2_num(18, K, k), D)

# q_2 is convex, so its maximum on [2,18] is at an endpoint.
assert q0 == Fraction(1, 4)
assert q_lo == Fraction(19, 144)
assert q_hi == Fraction(3, 16)
assert max(q0, q_lo, q_hi) == Fraction(1, 4)
assert Fraction(1, 1) - max(q0, q_lo, q_hi) == Fraction(3, 4)

assert counts == {-2: 1, -1: 1, 0: 14, 1: 16, 2: 256}
assert v == Fraction(175, 96)
assert M2 == Fraction(1045, 288)
assert tau2 == Fraction(642048, 1071875)
assert (K * k) ** 2 == 256 and D - 1 == 287

print("GENERIC_DISTANCE4_IDENTITIES_PASS")
print("K=8 k=2 degree =", D)
print("radial_counts =", counts)
print("v =", v)
print("M2 =", M2)
print("tau2 =", tau2)
print("spectral_image_zero =", q0)
print("spectral_image_bulk_endpoints =", q_lo, q_hi)
print("gap_lower_bound =", Fraction(3, 4))
print("branching_growth =", (K * k) ** 2, "<", D - 1)
print("center_coefficient_log16 =", Fraction(1, 1) / v)
print("P26_T08_BIGRAPH_DISTANCE4_GREEN_EXACT_PASS")
