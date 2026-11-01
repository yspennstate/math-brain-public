import itertools, math
import numpy as np

SEED = 23092026
SAMPLES = 500
rng = np.random.default_rng(SEED)

def incident_three(B):
    m, n = B.shape
    J = 0.0
    ar = np.zeros(m)
    bc = np.zeros(n)
    for S in itertools.combinations(range(m), 3):
        if 0 not in S:
            continue
        for T in itertools.combinations(range(n), 3):
            if 0 not in T:
                continue
            w = float(np.linalg.det(B[np.ix_(S,T)])**2)
            J += w
            for i in S: ar[i] += w
            for j in T: bc[j] += w
    return J, ar/J, bc/J

def residual_two(B):
    m, n = B.shape
    E = 0.0
    ar = np.zeros(m)
    bc = np.zeros(n)
    for S in itertools.combinations(range(1,m), 2):
        for T in itertools.combinations(range(1,n), 2):
            w = float(np.linalg.det(B[np.ix_(S,T)])**2)
            E += w
            for i in S: ar[i] += w
            for j in T: bc[j] += w
    return E, ar/E, bc/E

minimum_ratio = float('inf')
failures = 0
for _ in range(SAMPLES):
    B = rng.normal(size=(5,5))
    J, alpha3, beta3 = incident_three(B)
    E, alpha2, beta2 = residual_two(B)
    alpha = 0.5*(alpha3 + alpha2)
    beta = 0.5*(beta3 + beta2)
    d = np.exp(rng.normal(size=5))
    e = np.exp(rng.normal(size=5))
    lhs = float(np.linalg.det(np.diag(e) + B.T @ np.diag(d) @ B))
    rhs = 2.0*math.sqrt(J*E)*float(np.prod(d**alpha))*float(np.prod(e**(1.0-beta)))
    ratio = lhs/rhs
    minimum_ratio = min(minimum_ratio, ratio)
    failures += int(ratio < 1.0-1e-10)

C1 = 5.0*math.e/(2.0**(1.0/5.0))
compound_product = (31.0/288.0)*(992.0/585.0)
compound_constant = C1*compound_product**(-0.1)
partner_hybrid_constant = ((3.0*math.sqrt(2.0)/math.pi)
    * (math.sqrt(6.0*math.pi*2.0**(2.0/3.0)))**(1.0/3.0)
    * (2.0**(-1.0/4.0)*math.e**(5.0/4.0)*math.pi**(5.0/4.0))**(2.0/3.0))

print(f'seed={SEED}')
print(f'samples={SAMPLES}')
print(f'minimum_determinant_ratio={minimum_ratio:.15f}')
print(f'determinant_failures={failures}')
print(f'q1_mixed_constant={C1:.15f}')
print(f'compound_JE_over_Z2={compound_product:.15f}')
print(f'compound_density_constant={compound_constant:.15f}')
print(f'partner_hybrid_constant={partner_hybrid_constant:.15f}')
print('STATUS=PASS' if failures == 0 else 'STATUS=FAIL')
