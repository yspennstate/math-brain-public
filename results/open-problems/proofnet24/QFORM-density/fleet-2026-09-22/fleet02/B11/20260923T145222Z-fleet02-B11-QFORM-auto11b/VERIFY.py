import math
import numpy as np

rho = 0.5
tau = min(rho, 1-rho)
gamma = tau**3/9216
h0 = gamma/2

assert h0 <= tau/96
assert tau**2/3456 >= tau**3/4608
assert tau**3/4608 - tau**3/9216 == gamma
assert 3/h0 == 55296/tau**3

# Nonredundancy calibration matrix from REPORT.md.
M = np.array([[0.0,1.0,1.0],[1.0,0.0,1.0],[1.0,1.0,0.0]])
eigs = np.linalg.eigvalsh(M)
assert np.allclose(eigs, [-1.0,-1.0,2.0])

# A finite exact frame calibration with one leverage-0.6 row and all
# remaining row weights below h0. Only masses are needed for the check.
N = 100_000
N3 = 200_000
weights = [0.6, 0.4/N, 0.5/N, 0.5/N, 1.0/N3]
assert weights[0] > 0.5
assert max(weights[1:]) < h0
assert 0.4 > rho/48
assert 0.5 > rho/48
assert 0.5 > (1-rho)/48
assert 1.0 > (1-rho)/48

print('gamma', gamma)
print('h0', h0)
print('cut_constant_at_tau_half', 55296*math.sqrt(math.e)/tau**3)
print('stability_constant_at_tau_half', 211968/tau**3)
print('ruled_pi_sqrt2', math.pi*math.sqrt(2))
print('eigenvalues', eigs.tolist())
print('QFORM_B11_NULL_RULING_CROSSCUT_CHECK_PASS')
