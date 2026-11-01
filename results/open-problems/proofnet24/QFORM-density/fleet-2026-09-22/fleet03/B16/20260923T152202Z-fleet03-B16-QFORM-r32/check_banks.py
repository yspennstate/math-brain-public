from fractions import Fraction
import math

eps = Fraction(1, 4096)
tau = Fraction(1, 64)
D_pair = tau*tau - eps*eps
kappa = tau - eps
pair_bound = 8*math.sqrt(5)*(float(D_pair*kappa))**(-0.25)
assert pair_bound < 407

R2 = Fraction(63, 64) - eps*eps
mu_exact = (tau*tau) / R2
assert mu_exact < Fraction(1, 4031)

mu = Fraction(1, 4031)
theta = Fraction(1, 2000)
assert mu < theta
assert theta + mu < Fraction(1, 1300)
assert mu/theta < Fraction(1, 2)

sigma_lower = math.sqrt(float(R2/Fraction(2000, 1)))
assert sigma_lower > 0.02218

print(f"pair determinant floor = {float(D_pair):.15f}")
print(f"pair sigma_min floor = {float(kappa):.15f}")
print(f"pair-log bound = {pair_bound:.12f} < 407")
print(f"star energy floor = {float(R2):.15f}")
print(f"exact normalized atom cap = {float(mu_exact):.15f} < 1/4031")
print(f"bank upper theta+mu = {float(theta+mu):.15f} < 1/1300 = {1/1300:.15f}")
print(f"within-bank atom ratio < 2000/4031 = {float(mu/theta):.15f} < 1/2")
print(f"sigma_k lower = {sigma_lower:.12f} > 0.02218")
print("STATUS=PASS")
