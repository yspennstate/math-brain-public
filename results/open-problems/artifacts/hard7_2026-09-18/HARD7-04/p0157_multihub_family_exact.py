import sympy as sp

m = sp.symbols('m', positive=True, integer=True)
M = m**5
d = m**2
n = 8*m**12
x = 3*m**11 + M*(d-1)**2/4
N3 = 2*m**12 - x
N1 = 6*m**12 + x - M

ell = sp.expand(N1 + 3*N3 + d*M)
fac2 = sp.expand(6*N3 + d*(d-1)*M)
gap = sp.expand(ell - fac2)

assert sp.expand(N1 + N3 + M - n) == 0
assert sp.expand(gap - 12*m**11) == 0
D = 24*m**7 - 12*m**6 - m**4 + 4*m**2 - 3
assert sp.expand(2*ell - m**5*D) == 0

delta = sp.cancel(gap/ell)
third = sp.cancel((N1 + 27*N3 + d**3*M)/n)
nu = sp.cancel(fac2/ell)
off2 = sp.cancel((12*N3 + d*(d-1)**2*M)/ell)
sigma2 = sp.cancel(off2 - nu**2)
Q = sp.cancel(sigma2/(d*delta))

# Condition on one direct edge between two degree-d hubs and contract it.
ellp = sp.expand(ell - 2)
fac2p = sp.expand(fac2 - 2*d*(d-1) + (2*d-2)*(2*d-3))
gapp = sp.expand(ellp - fac2p)
deltap = sp.cancel(gapp/ellp)
assert sp.expand(gapp - (12*m**11 - 2*m**4 + 8*m**2 - 8)) == 0

# Direct hub-hub matching counts.
S = M*d
mu_raw = sp.cancel(S*(S-1)/(2*(ell-1)))
mu_self = sp.cancel(M*d*(d-1)/(2*(ell-1)))
mu_dist = sp.cancel(M*(M-1)*d**2/(2*(ell-1)))
# E[X(X-1)] for X = number of matching pairs wholly in the S hub half-edges.
fac_raw = sp.cancel(S*(S-1)*(S-2)*(S-3)/(4*(ell-1)*(ell-3)))

z = sp.symbols('z', positive=True)
def lim_inf(expr):
    return sp.limit(sp.cancel(expr.subs(m, 1/z)), z, 0, dir='+')

checks = {
    'm_delta': lim_inf(m*delta),
    'third': lim_inf(third),
    'sigma2': lim_inf(sigma2),
    'm_Q': lim_inf(m*Q),
    'ndelta3_over_m9': lim_inf(n*delta**3/m**9),
    'ddelta_over_m': lim_inf(d*delta/m),
    'delta_star_over_delta': lim_inf(deltap/delta),
    'contracted_scale_over_H': lim_inf(((2*d-2)/d)*(delta/deltap)),
    'mu_raw_over_m2': lim_inf(mu_raw/m**2),
    'mu_dist_over_m2': lim_inf(mu_dist/m**2),
    'm3_mu_self': lim_inf(m**3*mu_self),
    'fac2_ratio': lim_inf(fac_raw/mu_raw**2),
}
expected = {
    'm_delta': 1,
    'third': sp.Rational(15, 2),
    'sigma2': 1,
    'm_Q': 1,
    'ndelta3_over_m9': 8,
    'ddelta_over_m': 1,
    'delta_star_over_delta': 1,
    'contracted_scale_over_H': 2,
    'mu_raw_over_m2': sp.Rational(1, 24),
    'mu_dist_over_m2': sp.Rational(1, 24),
    'm3_mu_self': sp.Rational(1, 24),
    'fac2_ratio': 1,
}
assert checks == expected, (checks, expected)

print('ell =', sp.factor(ell))
print('delta =', sp.factor(delta))
for k, v in checks.items():
    print(k, '=', v)
print('ALL_EXACT_CHECKS_PASS')
