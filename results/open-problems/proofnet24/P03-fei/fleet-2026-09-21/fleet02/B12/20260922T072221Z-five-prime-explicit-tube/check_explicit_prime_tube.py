from fractions import Fraction

# Exact arithmetic checks for REPORT.md. No external dependencies.

eps = Fraction(1, 2**18)
delta5 = Fraction(4906502214, 10**12)

# Biased Fourier coefficient transport. At p=1/2+x, |x|<=eps,
# ||d_j a||_2^2 <= 1/sigma^2 + x^2/sigma^4.
sigma2 = Fraction(1, 4) - eps * eps
deriv_sq = 1 / sigma2 + eps * eps / (sigma2 * sigma2)
assert deriv_sq < 9

# A nonconstant five-bit gate has central output mass in [1/32,31/32].
# Product-measure transport by at most five eps keeps the symmetric mass >1/64.
assert Fraction(1, 32) - 5 * eps > Fraction(1, 64)

# Source derivative bound on symmetric representative z>=1/64:
# |Gamma_0'| <= 4.9096*6 + 8.629 + 31*(1/ln2),
# 1/ln2 < 3/2, plus the quadratic-lift derivative <0.269.
source_derivative_upper = (
    Fraction(6137, 1250) * 6
    + Fraction(8629, 1000)
    + Fraction(93, 2)
    + Fraction(269, 1000)
)
assert source_derivative_upper < 85

# Fannes-Audenaert simplification for delta_TV<=15 eps:
# 31 e / (15 eps) < 2^21, using e<3.
assert 93 * 2**18 < 15 * 2**21

# h_2(2^-34) < 36*2^-34, using h_2(x)<=x log_2(e/x), log_2 e<2.
# Total uniform slack transport debit:
# input prices 470 eps + 5 h_2(2^-34), output potential 425 eps,
# spectral entropy 315 eps.
variation_bound = 1210 * eps + Fraction(180, 2**34)
reserve = delta5 - variation_bound
assert reserve > Fraction(29, 100000)

# Owner-comparable base-potential gate margin. If M_G>0 then
# c_G = a^dagger - D_Gamma^dagger/M_G, and M_G<=5/4.
a_dagger = Fraction(268204856, 10**9)
margin_upper = a_dagger - Fraction(4, 5) * Fraction(29, 100000)
assert margin_upper == Fraction(33496607, 125000000)

print("PASS")
print("epsilon", eps, float(eps))
print("derivative_norm_sq_endpoint", float(deriv_sq))
print("source_derivative_upper", float(source_derivative_upper))
print("variation_bound", float(variation_bound))
print("central_prime_reserve", float(delta5))
print("tube_reserve_exact", reserve)
print("tube_reserve_decimal", float(reserve))
print("certified_simple_floor", float(Fraction(29, 100000)))
print("margin_upper", float(margin_upper))
