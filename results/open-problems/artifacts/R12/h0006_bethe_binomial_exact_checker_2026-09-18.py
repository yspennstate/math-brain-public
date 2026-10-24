from fractions import Fraction
from math import comb

# Exact finite-core check for the d=3 Bethe subclass used in the R12/H0006 report.
# Offspring is Bin(2,p) with p=1/4, hence rho=1/2 and xi=(1-rho)^(-1)=2.
# Dwass gives P(T=n)=n^{-1} P(Bin(2n,1/4)=n-1).

def P(n: int) -> Fraction:
    assert n >= 1
    p = Fraction(1, 4)
    q = Fraction(3, 4)
    return Fraction(comb(2*n, n-1), n) * p**(n-1) * q**(n+1)

for n in range(1, 101):
    r = P(n+1) / P(n)
    expected = Fraction(3*(2*n+1), 8*(n+2))
    assert r == expected, (n, r, expected)

# The exact ratio tends to 3/4. The source's printed exp(-n/xi) factor with xi=2
# would force the ratio to tend to exp(-1/2). Elementary exact separation:
# exp(1/2) > 1 + 1/2 = 3/2, hence exp(-1/2) < 2/3 < 3/4.
assert Fraction(2, 3) < Fraction(3, 4)

print("DWASS_B2_P1_4_RATIO_IDENTITY_PASS n=1..100")
print("ratio_formula = 3(2n+1)/(8(n+2))")
print("exact_ratio_limit = 3/4")
print("source_ratio_if_exp_minus_n_over_xi = exp(-1/2) < 2/3")
print("therefore_exact_ratio_limit_differs_from_source_printed_factor = PASS")
