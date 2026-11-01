import sympy as sp

r = sp.symbols("r", positive=True)
m = sp.symbols("m", positive=True)
eps = sp.symbols("eps", real=True)

lambda0 = sp.sqrt(2*m)

# alpha=1 eta->0 marginal moment identity
moment_from_laplace = 2*sp.gamma(2*r)/(sp.gamma(r)*lambda0**(2*r))
moment_gamma = (2/m)**r * sp.gamma(r + sp.Rational(1,2))/sp.sqrt(sp.pi)
assert sp.simplify(sp.gammasimp(moment_from_laplace/moment_gamma)) == 1

# Gamma(shape=1/2, rate=m/2) mean
mean_gamma = (sp.Rational(1,2))/(m/2)
assert sp.simplify(mean_gamma - 1/m) == 0

# x=1/4 exact normalization hurdle
x = sp.Rational(1,4)
mx = (sp.sqrt(x) + sp.sqrt(1-x))/2
R = sp.simplify(sp.sqrt(2)*mx)
R_expected = (sp.sqrt(6)+sp.sqrt(2))/4
assert sp.simplify(R-R_expected) == 0
assert sp.simplify(R-sp.cos(sp.pi/12)) == 0

delta = sp.simplify(1-R)
assert sp.simplify(delta - (1-(sp.sqrt(6)+sp.sqrt(2))/4)) == 0

# Near-endpoint epsilon = 1/2-x:
# R(eps) = cos(1/2 asin(2 eps))
#        = sqrt((1+sqrt(1-4 eps^2))/2).
R_eps = sp.sqrt((1 + sp.sqrt(1-4*eps**2))/2)
series = sp.series(R_eps, eps, 0, 8)
expected = 1 - eps**2/sp.Integer(2) - 5*eps**4/sp.Integer(8) - 21*eps**6/sp.Integer(16)
assert sp.expand(series.removeO()-expected) == 0

print("moment_ratio =", sp.simplify(sp.gammasimp(moment_from_laplace/moment_gamma)))
print("Gamma_limit = Gamma(shape=1/2, rate=m_x/2)")
print("E_q_limit =", mean_gamma)
print("R_1_4 =", R)
print("R_1_4_numeric =", sp.N(R, 16))
print("delta_1_4 =", delta)
print("delta_1_4_numeric =", sp.N(delta, 16))
print("R_endpoint_series =", series)
print("ALL_EXACT_CHECKS_PASS = True")
