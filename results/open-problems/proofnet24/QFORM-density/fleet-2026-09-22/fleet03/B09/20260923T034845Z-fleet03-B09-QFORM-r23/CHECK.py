import math
import numpy as np

# r23 deterministic regression for the strict-N3 stress family.
tau = 1/128
q = math.sqrt(tau + tau*tau)

nI = 1 + 40 + 144 + 144
v = np.zeros(nI)
v[0] = math.sqrt(0.6)
v[1:41] = 0.1
r1 = np.zeros(nI)
r1[41:41+144] = 1/12
r2 = np.zeros(nI)
r2[41+144:41+288] = 1/12
R = np.column_stack([r1, r2])
C = R.copy()
D = -np.diag(v*v)
AII = np.outer(v, v) + D
A = np.block([[AII, C], [C.T, np.zeros((2,2))]])

assert abs(np.dot(v,v)-1) < 1e-12
assert np.linalg.norm(R.T@R-np.eye(2)) < 1e-12
assert np.linalg.norm(R.T@v) < 1e-12
assert np.max(np.abs(np.diag(A))) < 1e-14

edge = A - np.diag(np.diag(A))
max_edge = np.max(np.abs(edge))
max_pair_det = max_edge**2
assert max_pair_det < tau

ev = np.linalg.eigvalsh(A)
assert np.sum(np.abs(ev) >= 1-1e-10) >= 4

lev = v*v + r1*r1 + r2*r2
assert np.max(lev) > 0.5
assert abs(np.sum(lev)-3) < 1e-12
sumsq = np.sum(lev**2)
eta = 1-sumsq
assert eta > 0

rho_exact = (1-(0.6**2 + 40*0.01**2)) * (1-144*(1/144)**2)**2
assert rho_exact >= eta

C_eta = (5*math.e/3) * eta**(-1/5)
C_rho = (5*math.e/3) * rho_exact**(-1/5)

print(f"tau={tau:.15f}")
print(f"q={q:.15f}")
print(f"max_edge={max_edge:.15f}")
print(f"max_pair_det={max_pair_det:.15f}")
print(f"large_eigenvalue_count={np.sum(np.abs(ev) >= 1-1e-10)}")
print(f"max_leverage={np.max(lev):.15f}")
print(f"sum_leverage_squares={sumsq:.15f}")
print(f"eta_union_bound={eta:.15f}")
print(f"rho_exact={rho_exact:.15f}")
print(f"density_bound_eta={C_eta:.15f}")
print(f"density_bound_rho={C_rho:.15f}")
