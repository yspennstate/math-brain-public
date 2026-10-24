from fractions import Fraction
import math
import numpy as np

beta = Fraction(34,111)*Fraction(17,288)
kappa = Fraction(34,111)*Fraction(17,288)**2
zeta = Fraction(27,256)*kappa**2*beta**2/Fraction(8,1)
C3 = 10.345084
assert abs(float(beta)-0.01808058058058058) < 1e-16
assert abs(float(kappa)-0.001067256492603715) < 1e-16
assert abs(float(zeta)-4.909035430513786e-12) < 1e-25
assert C3*float(zeta)**(-1/6) < 793.539
assert 2048*math.sqrt(2/7) < 1094.703

rng = np.random.default_rng(20260923)
max_individual_error = 0.0
max_sum_error = 0.0
ntests = 0
for m in range(5,13):
    for rep in range(50):
        G = rng.normal(size=(m,3))
        E,_ = np.linalg.qr(G, mode='reduced')
        H = rng.normal(size=(3,3))
        C = (H+H.T)/2
        A = E@C@E.T
        U = E[:,:2]
        h = C[:,2]
        W_lhs = 0.0
        W_rhs = 0.0
        for i in range(m):
            ui = U[i,:]
            zi = E[i,:]
            ell = float(ui@ui)
            q = float(zi@zi)
            b = float(h@zi)
            mask = np.arange(m) != i
            c = A[mask,i]
            Um = U[mask,:]
            coef = np.linalg.lstsq(Um,c,rcond=None)[0]
            resid = c-Um@coef
            delta2 = float(resid@resid)
            lhs = (1-ell)*delta2
            rhs = (1-q)*b*b
            max_individual_error = max(max_individual_error,abs(lhs-rhs))
            W_lhs += lhs
            W_rhs += rhs
        max_sum_error = max(max_sum_error,abs(W_lhs-W_rhs))
        ntests += 1

assert max_individual_error < 1e-12
assert max_sum_error < 1e-12
print('beta0 =', float(beta))
print('kappa_* =', float(kappa))
print('zeta_* =', float(zeta))
print('E3 density constant <', C3*float(zeta)**(-1/6))
print('partner large-leaf constant =', 2048*math.sqrt(2/7))
print('random frame tests =', ntests)
print('max individual identity error =', max_individual_error)
print('max aggregate identity error =', max_sum_error)
print('QFORM_B11_R42_CURVATURE_TRANSFER_CHECK_PASS')
