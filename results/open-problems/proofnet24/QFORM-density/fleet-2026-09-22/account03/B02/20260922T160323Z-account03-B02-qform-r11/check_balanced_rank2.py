import itertools, math
import numpy as np

# Regression for QFORM-RANK2-SCHUR-BALANCED-PAVING-v1.
# The proof in REPORT.md is symbolic; this only checks the key exterior-square
# identity and one explicit tight-frame instance at the mu=1/6 cutoff.

def tight_frame(m):
    th = np.arange(m) * math.pi / m
    return math.sqrt(2.0/m) * np.column_stack((np.cos(th), np.sin(th)))

m = 12
V = tight_frame(m)
assert np.max(np.abs(V.T @ V - np.eye(2))) < 1e-12
mu = float(np.max(np.sum(V*V, axis=1)))
assert abs(mu - 1/6) < 1e-12
M = np.array([[2.0, 0.7], [0.7, -1.3]])

found = None
for bits in itertools.product((-1.0, 1.0), repeat=m):
    eps = np.asarray(bits)
    T = sum(eps[i] * np.outer(V[i], V[i]) for i in range(m))
    op = float(np.linalg.norm(T, 2))
    if op >= 3/5:
        continue
    I = np.where(eps > 0)[0]
    J = np.where(eps < 0)[0]
    if len(I) < 2 or len(J) < 2:
        continue
    G = V[I].T @ V[I]
    lev = max(float(V[i] @ np.linalg.inv(G) @ V[i]) for i in I)
    if lev >= 7/8:
        continue
    B = V[I] @ M @ V[J].T
    e2_direct = 0.0
    for rr in itertools.combinations(range(len(I)), 2):
        for cc in itertools.combinations(range(len(J)), 2):
            e2_direct += float(np.linalg.det(B[np.ix_(rr, cc)])**2)
    e2_factored = float(np.linalg.det(M)**2 * np.linalg.det(G) * np.linalg.det(np.eye(2)-G))
    assert abs(e2_direct-e2_factored) <= 1e-10 * max(1.0, abs(e2_factored))
    assert e2_direct >= np.linalg.det(M)**2 * 16/625 - 1e-12
    found = (op, lev, e2_direct, e2_factored, len(I), len(J))
    break

assert found is not None

# Exact constants from the beta-function formula in the completed determinant
# estimate / square-pivot potential argument.
def beta(a,b):
    return math.gamma(a)*math.gamma(b)/math.gamma(a+b)

def P(r):
    return 4*(2-r)**((r-3)/2)*r**(-r/2)

def C(q,k,r):
    return (P(r)*math.sqrt(math.e)*2**(-3/4)*q**(-1/4)
            * math.sqrt((1/k)*beta(1/(2*k), r/(4*q)-1/(2*k))))

C_q1 = C(1,2,3/2)*(256/9)**(1/8)
C_q74 = C(7/4,2,15/8)*(625/16)**(1/8)
print('STATUS=PASS')
print('mu=', mu)
print('explicit_partition op,leverage,E2_direct,E2_factored,|I|,|J|=', found)
print('C_mu_lt_1_over_8=', C_q1)
print('C_mu_le_1_over_6=', C_q74)
print('rank3_heavy_nonisotropic_q1_bound=', C_q1*math.sqrt(2))
print('rank3_heavy_nonisotropic_q74_bound=', C_q74*math.sqrt(2))
