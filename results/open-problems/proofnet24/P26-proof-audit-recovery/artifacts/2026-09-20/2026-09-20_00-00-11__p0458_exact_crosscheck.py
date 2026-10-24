from fractions import Fraction
from math import factorial, comb


def beta_influence_integral(n, k):
    # C(n-3,k-1) * B(k,n-k-1)
    return (
        Fraction(factorial(n-3), factorial(k-1)*factorial(n-k-2))
        * Fraction(factorial(k-1)*factorial(n-k-2), factorial(n-2))
    )


def mu_direct(r):
    s = Fraction(0)
    for ell in range(r):
        s += Fraction(
            (r-ell) * factorial(r+ell-1),
            factorial(r-1) * factorial(ell) * 2**(r+ell)
        )
    return s


def mu_closed(r):
    return Fraction(r * comb(2*r, r), 4**r)


def m2(r):
    s = Fraction(0)
    for ell in range(r):
        for m in range(r):
            s += Fraction(
                (r-ell)*(r-m)*factorial(r+ell+m-1),
                factorial(r-1)*factorial(ell)*factorial(m)*3**(r+ell+m)
            )
    return s


beta_cases = 0
for n in range(4, 61):
    for k in range(1, n-1):
        assert beta_influence_integral(n, k) == Fraction(1, n-2)
        beta_cases += 1

for r in range(1, 21):
    assert mu_direct(r) == mu_closed(r)

mu1, m21 = mu_closed(1), m2(1)
nu1 = mu1 + m21 - mu1*mu1
mu2, m22 = mu_closed(2), m2(2)
nu2 = mu2 + m22 - mu2*mu2

assert mu1 == Fraction(1, 2)
assert m21 == Fraction(1, 3)
assert nu1 == Fraction(7, 12)
assert mu2 == Fraction(3, 4)
assert m22 == Fraction(22, 27)
assert nu2 == Fraction(433, 432)

endpoint_sq_1 = mu1*mu1/nu1
endpoint_sq_2 = mu2*mu2/nu2
assert endpoint_sq_1 == Fraction(3, 7)
assert endpoint_sq_2 == Fraction(243, 433)
assert endpoint_sq_1 != endpoint_sq_2

print("P26_P0458_EXACT_FORMULA_CROSSCHECK_PASS")
print("beta_influence_integral_cases =", beta_cases)
print("beta_influence_identity =", "1/(n-2)")
print("mu_direct_equals_central_binomial_r_1_to_20 =", "PASS")
print("r1_mu_m2_nu =", mu1, m21, nu1)
print("r2_mu_m2_nu =", mu2, m22, nu2)
print("standardized_upper_endpoint_sq_r1 =", endpoint_sq_1)
print("standardized_upper_endpoint_sq_r2 =", endpoint_sq_2)
print("boundary_laws_distinct_certificate =", "PASS")
