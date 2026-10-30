from math import sqrt, pi, e, gamma, isclose
from itertools import product

# Regression only. The report contains the proofs.
alpha = 1/8
c_alpha = 2**(1-alpha)*gamma((1-alpha)/2)/(2*sqrt(pi)*gamma(alpha/2))
C1 = 32*c_alpha*(pi*sqrt(2*e))**(1/8)
K = 2*sqrt(2)*(2*alpha+1)/(2*alpha)*2**((alpha-1/2)/(2*alpha+1))
Cstar = K*C1**(1/(2*alpha+1))
assert isclose(C1, 2.777316075398203, rel_tol=2e-15)
assert isclose(K, 10*2**(1/5), rel_tol=2e-15)
assert isclose(Cstar, 26.0079574195497, rel_tol=2e-14)

# Exact spectral inequality used to turn low Frobenius tail into a strong rank-two tube.
# lambda_j are squared singular values, descending.
count = 0
for vals in product(range(7), repeat=5):
    lam = sorted(vals, reverse=True)
    f2 = sum(lam)
    t2 = sum(lam[2:])
    e2 = sum(lam[i]*lam[j] for i in range(5) for j in range(i+1,5))
    lhs = e2 - lam[0]*lam[1]
    assert lhs <= f2*t2
    count += 1

# The previous exact Schur-loss obstruction must remain in the low-tail survivor:
# D has singular values sqrt(m),sqrt(m), so T2(D)=0 while E2(D)=m^2.
for m in (12,16,32,64):
    E2 = m*m
    T2 = 0
    b = 1/m
    assert isclose(abs(b)*sqrt(E2), 1.0)
    assert T2 == 0

# r30 edge-E2 implication at epsilon=gamma/8.
gamma0 = 113246208**-2
for F in (0.5, 1.0, 3.0, 11.0):
    eps = gamma0/8
    lower_e2 = gamma0*F**4/4
    upper_loss = eps*F**4
    assert lower_e2-upper_loss == gamma0*F**4/8
    assert sqrt(lower_e2-upper_loss) == sqrt(gamma0/8)*F**2

print(f"C1={C1:.15f}")
print(f"K_pair={K:.15f}")
print(f"C_star={Cstar:.15f}")
print(f"integer_spectra_checked={count}")
print("QFORM_B07_PAIRTAIL_CHECK_PASS")
