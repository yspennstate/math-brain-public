import math
import numpy as np

THETA0 = 2.0**-12
MU0 = 2.0**-9
KAPPA0 = 2.0**-6

C_scalar = 16.0*math.sqrt(60.0)*THETA0**(-0.25)
C_pair = 4.0*math.sqrt(20.0)*(8.0**0.25)
C_pair_branch = C_pair*(MU0*KAPPA0)**(-0.25)
C_def = 2.0*math.pi/KAPPA0
partner_threshold = 34.0*math.sqrt(math.log(math.e/math.exp(-8.0)))

assert C_scalar < 992.0
assert C_pair < 30.085
assert C_pair_branch < 405.0
assert C_def < 403.0
assert abs(partner_threshold-102.0) < 1e-10

rng = np.random.default_rng(20260922)
for _ in range(200):
    M = rng.normal(size=(3,3))
    M = (M+M.T)/2.0
    if abs(np.linalg.det(M)) < 0.05:
        continue
    v1 = rng.normal(size=3)
    v1 /= np.linalg.norm(v1)
    b = rng.normal(size=3)
    b -= v1*(v1@b)
    if np.linalg.norm(b) < 1e-8:
        continue
    b /= np.linalg.norm(b)
    v2 = 0.4*v1 + math.sqrt(1.0-0.4**2)*b
    lam1,lam2 = rng.uniform(0.05,0.35,2)
    G = np.eye(3)-lam1*np.outer(v1,v1)-lam2*np.outer(v2,v2)
    if np.linalg.eigvalsh(G).min() < -1e-10:
        continue
    B = np.array([
        [lam1*(v1@M@v1), math.sqrt(lam1*lam2)*(v1@M@v2)],
        [math.sqrt(lam1*lam2)*(v2@M@v1), lam2*(v2@M@v2)],
    ])
    if abs(np.linalg.det(B)) < 1e-8:
        continue
    w0 = np.cross(v1,v2)
    g2 = float(w0@w0)
    mu = abs(np.linalg.det(M))*lam1*lam2*g2
    V = np.column_stack([v1,v2])
    C = V.T@M@V
    w = w0/math.sqrt(g2)
    P = np.column_stack([v1,v2,w])
    eta = np.linalg.det(P.T@M@P)/np.linalg.det(C)
    assert abs(abs(eta)*abs(np.linalg.det(B))-mu) < 1e-7*(1.0+mu)

print('C_scalar', C_scalar)
print('C_pair', C_pair)
print('C_pair_branch', C_pair_branch)
print('C_def', C_def)
print('partner_threshold', partner_threshold)
print('QFORM_B19_R19_BANK_PIVOT_CHECK_PASS')
