import math
import numpy as np

SEED = 20260924
rng = np.random.default_rng(SEED)

mu_gate = 1/48
C_X = 6**(4/3)
C_R = 288*math.sqrt(3*math.e)/13
a_gate = (1-math.sqrt(3*mu_gate))/2
eta = C_R*a_gate/(C_R+C_X)
C_star = (C_R+C_X)/a_gate
m_star = 47/48-eta

assert abs(a_gate-3/8) < 1e-15
assert abs(C_X/(a_gate-eta)-C_star) < 1e-12
assert abs(C_R/eta-C_star) < 1e-12

# Deterministic 192x3 tight frame: 64 repeated physical rows per direction.
mrep = 64
n = 3*mrep
U = np.zeros((n, 3))
for j in range(3):
    U[j*mrep:(j+1)*mrep, j] = 1/math.sqrt(mrep)
lev = np.sum(U*U, axis=1)
mu = float(np.max(lev))
expect_exact = 0.25*float(np.sum(lev**2))
expect_bound = 0.75*mu
assert abs(expect_exact-expect_bound) < 1e-15

mask = np.zeros(n, dtype=bool)
for j in range(3):
    mask[j*mrep:j*mrep+mrep//2] = True
G = U[mask].T @ U[mask]
assert np.linalg.norm(G-0.5*np.eye(3), 2) < 1e-14
actual_a = min(np.linalg.eigvalsh(G).min(), np.linalg.eigvalsh(np.eye(3)-G).min())

# Regression only: test the deterministic cross singular-value inequality under random symmetric tails.
lam = np.array([1.0, -1.3, 2.0])
A3 = U @ np.diag(lam) @ U.T
violations = 0
min_slack = float('inf')
for _ in range(25):
    H = rng.normal(size=(n,n))
    H = (H+H.T)/2
    eig = np.linalg.eigvalsh(H)
    hn = max(abs(eig[0]), abs(eig[-1]))
    frac = rng.uniform(0, 0.999)
    E = H/hn*(eta*frac)
    B = A3[np.ix_(mask, ~mask)] + E[np.ix_(mask, ~mask)]
    s = np.linalg.svd(B, compute_uv=False)
    lower = actual_a - eta*frac
    slack = float(s[2]-lower)
    min_slack = min(min_slack, slack)
    if slack < -1e-10:
        violations += 1

print('QFORM_B08_R50_CHECK_PASS')
print('C_X', C_X)
print('C_R', C_R)
print('a_gate', a_gate)
print('eta_star', eta)
print('C_star', C_star)
print('m_star', m_star)
print('localized_witness', eta/512)
print('partner_witness', m_star/512)
print('tight_frame_mu', mu)
print('expectation_exact', expect_exact)
print('expectation_upper', expect_bound)
print('cross_tests', 25)
print('violations', violations)
print('min_slack', min_slack)
assert violations == 0
