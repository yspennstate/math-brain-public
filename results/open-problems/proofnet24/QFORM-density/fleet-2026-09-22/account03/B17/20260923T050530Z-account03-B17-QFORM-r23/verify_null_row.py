import math
import mpmath as mp
import numpy as np

mp.mp.dps = 50
sigma2 = mp.mpf(1) / 12
sigma = mp.sqrt(sigma2)

# Exact-family spectral checks (numerical, deterministic).
for m in (3, 7):
    e1 = np.array([1.0, 0.0, 0.0])
    e2 = np.array([0.0, 1.0, 0.0])
    e3 = np.array([0.0, 0.0, 1.0])
    a = (e1 + e3) / math.sqrt(2.0)
    b = (e1 - e3) / math.sqrt(2.0)
    c = e2
    R = np.vstack([a] + [b / math.sqrt(m)] * m + [c / math.sqrt(m)] * m)
    J = np.diag([1.0, 1.0, -1.0])
    A = R @ J @ R.T
    nz = np.linalg.eigvalsh(A)
    nz = nz[np.abs(nz) > 1e-10]
    print(f"m={m} frame_error={np.max(np.abs(R.T @ R - np.eye(3))):.3e} nonzero_eigs={nz}")

sqrt2pi = mp.sqrt(2 * mp.pi)

def gamma_pdf(x):
    return mp.e ** (-x*x/(2*sigma2)) / (sqrt2pi * sigma)

def H4(x):
    return x**4 - 6*x**2 + 3

def inner0(b):
    return mp.mpf('0.5') * mp.erf(mp.sqrt(b)/(mp.sqrt(2)*sigma))

def innerH(b):
    z = mp.sqrt(b)/sigma
    # integral_0^sqrt(b) gamma_sigma(c) H4(c/sigma) dc
    return (3*z - z**3) * mp.e**(-z*z/2) / mp.sqrt(2*mp.pi)

# b=y^2 removes the integrable b^{-1} singularity.
def c_integrand(y):
    if y == 0:
        return 4 * gamma_pdf(0)**2
    b = y*y
    return 4 * gamma_pdf(b) * inner0(b) / y

Cnull = mp.quad(c_integrand, [0, 1, mp.inf])

def i_integrand(y):
    if y == 0:
        return 24 * gamma_pdf(0)**2
    b = y*y
    return 4 * gamma_pdf(b) * (H4(b/sigma)*inner0(b) + innerH(b)) / y

Inull = mp.quad(i_integrand, [0, 1, 2, mp.inf])
Cstar = 3 * mp.sqrt(2)
print("C_null =", mp.nstr(Cnull, 30))
print("3sqrt2 =", mp.nstr(Cstar, 30))
print("gap =", mp.nstr(Cstar-Cnull, 30))
print("I_null =", mp.nstr(Inull, 30))
print("I_null/20 =", mp.nstr(Inull/20, 30))
assert Cnull < Cstar
