from fractions import Fraction

# Exact finite-core check for the ADH Question 36 heavy-tail counterexample.
# Capacity law:
#   P(T=1)=1/2,
#   P(T=2^(s^3))=2^(-s-1), s>=1.
# The theorem-sized asymptotic proof is in main.tex.  This script verifies
# exact distribution/tail identities and the finite algebra used in that proof.


def atom_prob(s: int) -> Fraction:
    assert s >= 1
    return Fraction(1, 2 ** (s + 1))


def tail_prob(r: int) -> Fraction:
    assert r >= 1
    return Fraction(1, 2 ** r)


# Exact normalization and tail identities with a closed-form remainder.
for R in range(1, 25):
    partial = Fraction(1, 2) + sum(atom_prob(s) for s in range(1, R + 1))
    remainder = Fraction(1, 2 ** (R + 1))
    assert partial + remainder == 1

    for r in range(1, R + 1):
        tail_partial = sum(atom_prob(s) for s in range(r, R + 1))
        assert tail_partial + remainder == tail_prob(r)

# Diagonal-cylinder algebra for r=1,...,12.
# N_r=2^(r^2), height r, M_r=(N_r+1)^2 independent vertical columns.
# High-column probability q_r^r=2^(-r^2)=1/N_r.
rows = []
for r in range(1, 13):
    N = 2 ** (r * r)
    M = (N + 1) ** 2
    q = tail_prob(r)
    p_high = q ** r
    assert p_high == Fraction(1, N)

    mu = M * p_high
    assert mu >= N

    # Chebyshev failure probability is <=4/mu<=4/N.
    cheb_bound = Fraction(4, 1) / mu
    assert cheb_bound <= Fraction(4, N)

    # If Y_r>=mu/2, the normalized flow is at least
    # a_r*mu/(2*N^2) >= 2^(r^3-r^2-1).
    a = 2 ** (r ** 3)
    normalized_lb = Fraction(a, 2) * mu / (N * N)
    benchmark = Fraction(2 ** (r ** 3 - r * r), 2)
    assert normalized_lb >= benchmark

    rows.append((r, r * r, r ** 3 - r * r - 1))

print("P11-I0062-Q36-SOURCE-REFUTATION-02P exact finite core: PASS")
print("distribution normalization/tail identities: PASS for R=1..24")
print("high-column probability, mean, Chebyshev, normalized lower bound: PASS for r=1..12")
print("rows=(r, log2 N_r, log2 benchmark lower bound)")
for row in rows:
    print(row)
print("Written-proof obligations in main.tex: no exponential moment; corrected Kesten height; summability; Borel-Cantelli; primal flow; dual cut.")
