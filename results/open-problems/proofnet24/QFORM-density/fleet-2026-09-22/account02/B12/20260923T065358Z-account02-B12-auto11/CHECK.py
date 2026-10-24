import math
import numpy as np

# Exact constants in Section 4.
eps = 1.0/20.0
a = 2.0 - eps
R = 8.0*a*a
C = (2.0 + eps)**2
rho = C
margin = R - 2.0*C - 4.5*rho
term = R*(R-C)*(R-2.0*C)/6.0
cross_cap = (9.0*math.sqrt(3.0)*math.e/2.0)*term**(-1.0/6.0)
d5_cap = 5.0*math.sqrt(2.0*math.e)/a
print('R', R)
print('C', C)
print('gate_margin', margin)
print('cross_cap', cross_cap)
print('d5_cap', d5_cap)

# Deterministic perturbation inequalities in Theorem 2, sampled only as a sanity check.
np.random.seed(1)
violations = 0
trials = 10000
for _ in range(trials):
    m = np.random.randint(5,15)
    n = np.random.randint(5,15)
    M0 = np.random.randn(m,n)
    eps0 = np.random.rand()*0.5
    E = np.random.randn(m,n)
    op = np.linalg.svd(E,compute_uv=False)[0]
    E *= eps0/(op+1e-15)*np.random.rand()
    M = M0 + E
    s0 = np.linalg.svd(M0,compute_uv=False)
    s = np.linalg.svd(M,compute_uv=False)
    aa = np.maximum(s0-eps0,0.0)
    R0 = float(np.dot(aa,aa))
    S = float(np.dot(s,s))
    C0 = (s0[0]+eps0)**2
    cc = s[0]**2
    r0 = np.max(np.sum(M0*M0,axis=1))
    q0 = np.max(np.sum(M0*M0,axis=0))
    rho_star = min((math.sqrt(r0)+eps0)**2,(math.sqrt(q0)+eps0)**2)
    rho_actual = min(np.max(np.sum(M*M,axis=1)),np.max(np.sum(M*M,axis=0)))
    if np.any(s+1e-10 < aa) or S+1e-9 < R0 or cc > C0+1e-9 or rho_actual > rho_star+1e-9:
        violations += 1
        break
print('trials', trials)
print('violations', violations)
