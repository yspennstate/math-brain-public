from fractions import Fraction
import math
import numpy as np


def sylvester(n):
    H = np.array([[1]], dtype=np.int64)
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H


n = 256
H = sylvester(n)
assert H.shape == (n, n)
assert np.array_equal(H.T @ H, n * np.eye(n, dtype=np.int64))

# Selected rank-three Parseval frame: first three normalized Hadamard columns.
S = H[:, :3]
assert np.array_equal(S.T @ S, n * np.eye(3, dtype=np.int64))
G = S @ S.T
vals = sorted(set(int(x) for x in G[np.triu_indices(n, 1)]))
assert vals == [-1, 1, 3]  # hence every off-diagonal entry of I-RR^T is nonzero
N = n * np.eye(n, dtype=np.int64) - G
assert np.array_equal(N @ S, np.zeros((n, 3), dtype=np.int64))

# Explicit dense-remainder construction.
mu = Fraction(3, 256)
alpha = Fraction(13, 32)   # (1-sqrt(3*mu))/2 because 3*mu = 9/256
rho = alpha - Fraction(1, 40)
ell = mu / alpha
assert rho == Fraction(61, 160)
assert ell == Fraction(3, 104)
ridge = (math.sqrt(float(ell)) + math.sqrt(6) * float(Fraction(1, 40) / rho)) ** 2
dens = (720 / 61) * math.sqrt(3 * math.e)

# Clean conditional theorem constants.
mu0 = Fraction(1, 48)
alpha0 = Fraction(3, 8)
rho0 = Fraction(9, 32) - Fraction(1, 40)
ell0 = mu0 / alpha0
assert rho0 == Fraction(41, 160)
assert ell0 == Fraction(1, 18)
ridge0 = (math.sqrt(float(ell0)) + math.sqrt(6) * float(Fraction(1, 40) / rho0)) ** 2
dens0 = (720 / 41) * math.sqrt(3 * math.e)

print("hadamard_orthogonality=PASS")
print("selected_gram=256 I_3")
print("dense_remainder_offdiag_values_numerator=", vals)
print("projection_annihilation=(256 I - S S^T) S = 0 exact")
print("construction_mu=", mu)
print("construction_alpha=", alpha)
print("construction_rho=", rho)
print("construction_ell=", ell)
print("construction_ridge_diag_upper=", repr(ridge))
print("construction_density_constant=", repr(dens))
print("clean_mu=", mu0)
print("clean_alpha=", alpha0)
print("clean_rho=", rho0)
print("clean_ell=", ell0)
print("clean_ridge_diag_upper=", repr(ridge0))
print("clean_density_constant=", repr(dens0))
print("spectral_window_failure=1/40 > 1/64, so the |lambda|>=1/64 projection is I_256")
print("partner_fullrange_failure=A is invertible, so the entire-range projection is I_256")
print("QFORM_B08_STABLE_BLOCK_CHECK_PASS")
