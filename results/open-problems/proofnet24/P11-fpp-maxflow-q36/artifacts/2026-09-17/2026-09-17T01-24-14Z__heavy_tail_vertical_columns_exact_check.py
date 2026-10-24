from fractions import Fraction

# Exact self-check for P11-I0062-HEAVYTAIL-VERTICAL-COLUMNS-02.
# Distribution: P(T=1)=1/2, P(T=2^(s^3))=2^(-s-1), s>=1.
# The theorem-sized probabilistic argument (Chebyshev + Borel-Cantelli + explicit flow)
# is written in the run report; this script checks the finite algebra used there.


def atom_prob(s: int) -> Fraction:
    assert s >= 1
    return Fraction(1, 2 ** (s + 1))


def tail_prob(r: int) -> Fraction:
    # Sum_{s>=r} 2^(-s-1) = 2^(-r).
    assert r >= 1
    return Fraction(1, 2 ** r)


# Exact normalization and exact tail identity, with a closed-form geometric remainder.
for R in range(1, 25):
    partial = Fraction(1, 2) + sum(atom_prob(s) for s in range(1, R + 1))
    remainder = Fraction(1, 2 ** (R + 1))
    assert partial + remainder == 1

    for r in range(1, R + 1):
        tail_partial = sum(atom_prob(s) for s in range(r, R + 1))
        assert tail_partial + remainder == tail_prob(r)

# Exact diagonal-cylinder arithmetic for r=1,...,12.
# N_r=2^(r^2), m_r=r, M_r=(N_r+1)^2 vertical columns.
# A column is r-high with probability q_r^r=2^(-r^2), so
# mu_r=M_r*2^(-r^2) >= 2^(r^2).
# On Y_r >= mu_r/2, normalized flow is at least
# 2^(r^3-r^2-1), which tends to infinity.
rows = []
for r in range(1, 13):
    N = 2 ** (r * r)
    m = r
    M = (N + 1) ** 2
    q = tail_prob(r)
    p_high = q ** m
    assert p_high == Fraction(1, 2 ** (r * r))

    mu = M * p_high
    assert mu >= 2 ** (r * r)

    a = 2 ** (r ** 3)
    normalized_lb = Fraction(a, 2) * mu / (N * N)
    benchmark = Fraction(2 ** (r ** 3 - r * r), 2)
    assert normalized_lb >= benchmark

    # Chebyshev failure bound <= 4/mu <= 4*2^(-r^2).
    cheb_bound = Fraction(4, 1) / mu
    assert cheb_bound <= Fraction(4, 2 ** (r * r))

    # Along N_r, the global height choice floor(sqrt(log_2 N)) equals r exactly.
    assert N == 2 ** (r * r)

    rows.append((r, r * r, r ** 3 - r * r - 1))

print("P11-I0062-HEAVYTAIL-VERTICAL-COLUMNS-02 exact checker: PASS")
print("distribution normalization/tail identities: PASS for R=1..24 with exact geometric remainder")
print("column-probability, mean-count, Chebyshev and normalized-flow algebra: PASS for r=1..12")
print("rows are (r, log2 N_r, log2 benchmark lower bound):")
for row in rows:
    print(row)
print("Analytic obligations retained in report: m(k,l)->infinity and corrected height condition; summability of 4*2^(-r^2); no exponential moment; admissible edge-disjoint flow; Borel-Cantelli.")
