from fractions import Fraction
import math
import sympy as sp

# 1. Schur/principal-triple determinant identity.
a, wi, wj, sjj, m = sp.symbols('a wi wj sjj m', nonzero=True)
Aii = wi**2/a
Aij = wi*wj/a + m
Ajj = wj**2/a + sjj
T = sp.Matrix([[a,wi,wj],[wi,Aii,Aij],[wj,Aij,Ajj]])
assert sp.factor(T.det()) == -a*m**2
print('principal_triple_det =', sp.factor(T.det()))

# 2. Layer-cake constants from the Rudelson--Vershynin concentration exponent.
# For F(t)<=min(1,(C t)^beta), E Z^{-alpha} <= C^alpha beta/(beta-alpha).
def multiplier(alpha,beta):
    return beta/(beta-alpha)
assert abs(multiplier(0.5,0.75)-3.0)<1e-15
assert abs(multiplier(1.0,1.5)-3.0)<1e-15
print('alpha=1/2,beta=3/4 multiplier =', multiplier(0.5,0.75))
print('alpha=1,beta=3/2 multiplier =', multiplier(1.0,1.5))

# 3. Constants in the outer-square lift and the newest near-coloop exterior reserve.
c = Fraction(4191,281804800)
outer = 3*2**(5/4)                    # coefficient multiplying sqrt(C_RV)
# If E2=sum_{p<q}s_p^2 s_q^2, then E2 <= ||M||_HS^4/2, hence
# ||M||_HS^(-1/2) <= (2 E2)^(-1/8).
grouped_exterior_to_hs = (2*float(c))**(-1/8)
near_grouped = outer*grouped_exterior_to_hs
print('pair_currency_c = %.18g' % float(c))
print('outer_square_coefficient_times_sqrt_C_RV = %.15f' % outer)
print('grouped_exterior_to_HS_factor = %.15f' % grouped_exterior_to_hs)
print('near_coloop_grouped_coefficient_times_sqrt_C_RV = %.15f' % near_grouped)

# Verify e2 <= HS^4/2 on representative singular-value lists.
for ss in ([1,2],[0.3,7,0.5],[5,5,1],[1e-3,3,4,0.2]):
    hs2=sum(x*x for x in ss)
    e2=sum(ss[i]**2*ss[j]**2 for i in range(len(ss)) for j in range(i+1,len(ss)))
    assert e2 <= 0.5*hs2*hs2 + 1e-12

print('STATUS=PASS')
