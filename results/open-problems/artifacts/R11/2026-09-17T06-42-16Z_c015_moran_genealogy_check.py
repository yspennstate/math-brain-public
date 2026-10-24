from fractions import Fraction
from math import comb, factorial


def H(n):
    return sum((Fraction(1, r) for r in range(1, n + 1)), Fraction(0))


def H2(n):
    return sum((Fraction(1, r * r) for r in range(1, n + 1)), Fraction(0))


def beta_int(i, j):
    return Fraction(factorial(i - 1) * factorial(j - 1), factorial(i + j - 1))


def e_blocks(m, b, i):
    # Expected number of size-i blocks in Kingman's partition when b lineages remain.
    if i < 1 or b < 2 or b > m or i > m - b + 1:
        return Fraction(0)
    return Fraction(b * comb(m - i - 1, b - 2), comb(m - 1, b - 1))


checks = 0

# 1. Expected lineage-hit opportunities of descendant size i in the N-site Moran genealogy.
# At b lineages, active-lineage hit count before the next coalescence is
# Geom((b-1)/(N-1)); each hit selects a uniform active lineage.
for N in range(3, 41):
    c = N - 1
    for m in range(2, N + 1):
        for i in range(1, m):
            got = sum(
                (e_blocks(m, b, i) * Fraction(c, b * (b - 1)) for b in range(2, m + 1)),
                Fraction(0),
            )
            want = Fraction(c, i)
            assert got == want, (N, m, i, got, want)
            checks += 1

# 2. Exchangeability turns the SFS c/i into the CTCS beta split coefficient.
for N in range(3, 61):
    c = N - 1
    for m in range(2, min(N, 25) + 1):
        for i in range(1, m):
            j = m - i
            specified_A = Fraction(c, i * comb(m, i))
            specified_Ac = Fraction(c, j * comb(m, j))
            assert (specified_A + specified_Ac) / c == beta_int(i, j)
            checks += 1

# 3. Exact first and second moments of total active-lineage birth opportunities J_m.
# G_b ~ Geom((b-1)/(N-1)) independently across b=2,...,m.
for N in range(3, 101):
    c = N - 1
    for m in range(2, N + 1):
        mean = c * H(m - 1)
        var = sum((Fraction(c * (c - r), r * r) for r in range(1, m)), Fraction(0))
        second = mean * mean + var
        closed = c * c * (H(m - 1) ** 2 + H2(m - 1)) - c * H(m - 1)
        assert second == closed
        assert second <= c * c * (H(m - 1) ** 2 + H2(m - 1))
        checks += 1

# 4. Chosen scale delta_N=1/N, u_N=delta_N/(N-1).
# The accumulated multi-mark bound is <= delta_N*(H^2+H2)/2 -> 0.
vals = []
for N in [10, 20, 50, 100, 200, 500, 1000]:
    d = Fraction(1, N)
    bound = d * (H(N - 1) ** 2 + H2(N - 1)) / 2
    vals.append((N, float(bound)))
    checks += 1
assert vals[-1][1] < vals[0][1]

# 5. N=3 exact non-equivalence witness.
# Stage b=3 has one active-lineage hit. At b=2, G~Geom(1/2).
# Mutation probability u=delta/(N-1)=1/6.
N = 3
delta = Fraction(1, N)
u = delta / Fraction(N - 1)
assert u == Fraction(1, 6)
# For G~Geom(1/2), E[(1-u)^G]=(1-u)/(1+u).
p_stage2_no = (1 - u) / (1 + u)
p_no_visible = (1 - u) * p_stage2_no
p_deg3_raw = u * (1 - p_stage2_no)
p_visible = 1 - p_no_visible
p_deg3_first_visible = p_deg3_raw / p_visible
assert p_stage2_no == Fraction(5, 7)
assert p_no_visible == Fraction(25, 42)
assert p_deg3_raw == Fraction(1, 21)
assert p_deg3_first_visible == Fraction(2, 17)
checks += 5

previous = {
    "C001": Fraction(0),
    "C002": Fraction(1, 10),
    "C003": Fraction(1, 22),
    "C004": Fraction(1, 6),
    "C005": Fraction(1, 728),
    "C006": Fraction(1, 7),
    "C007": Fraction(1, 71),
    "C008": Fraction(1, 71),  # separated from C007 at N=4 in an earlier report
    "C009": Fraction(0),
    "C010": Fraction(0),
    "C011": Fraction(2, 105),
    "C012": Fraction(21521, 4909716),
    "C013": Fraction(35, 1296),
    "C014": Fraction(14, 2201),
}
for name, v in previous.items():
    assert p_deg3_first_visible != v, (name, v)
    checks += 1

# 6. Failure of non-rare standard population-genetic scaling.
# If theta=(N-1)u stays fixed, no-mark probability during a stage with r=b-1
# converges to r/(r+theta), so stages b=3 and b=2 both receive a mark with
# positive limiting probability theta/(theta+2)*theta/(theta+1).
for theta in [Fraction(1, 10), Fraction(1, 2), Fraction(1), Fraction(2)]:
    lb = theta / (theta + 2) * theta / (theta + 1)
    assert lb > 0
    checks += 1

print("R11 I0054 C015 exact self-check")
print("checks =", checks)
print("N=3 mutation_probability =", u)
print("N=3 no_visible_refinement =", p_no_visible)
print("N=3 raw_degree3 =", p_deg3_raw)
print("N=3 first_visible_degree3 =", p_deg3_first_visible)
print("accumulated_multi_mark_bound_samples =")
for N, v in vals:
    print(" ", N, f"{v:.12g}")
print("ALL_EXACT_CHECKS_PASS")
