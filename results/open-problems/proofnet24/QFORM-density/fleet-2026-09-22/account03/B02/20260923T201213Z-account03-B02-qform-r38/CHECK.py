import itertools
import json
import math
import numpy as np

rng = np.random.default_rng(20260923)

def adj3(P):
    return np.array([
        [P[1,1]*P[2,2]-P[1,2]*P[2,1], P[0,2]*P[2,1]-P[0,1]*P[2,2], P[0,1]*P[1,2]-P[0,2]*P[1,1]],
        [P[1,2]*P[2,0]-P[1,0]*P[2,2], P[0,0]*P[2,2]-P[0,2]*P[2,0], P[0,2]*P[1,0]-P[0,0]*P[1,2]],
        [P[1,0]*P[2,1]-P[1,1]*P[2,0], P[0,1]*P[2,0]-P[0,0]*P[2,1], P[0,0]*P[1,1]-P[0,1]*P[1,0]],
    ], dtype=float)

trials = 0
violations = 0
max_rel = 0.0
max_adj_rel = 0.0
min_slack1 = float('inf')
min_slack2 = float('inf')

for n in range(4, 11):
    for _ in range(200):
        R = rng.normal(size=(n,n))
        A = (R + R.T) / 2
        L = tuple(rng.choice(n, 3, replace=False))
        O = [j for j in range(n) if j not in L]
        P = A[np.ix_(L,L)]
        C = A[np.ix_(L,O)]
        G = C @ C.T
        d = np.linalg.det(P)**2
        z = max(0.0, float(np.linalg.det(G))) if len(O) >= 3 else 0.0
        AP = adj3(P)
        v = sum(float(np.dot(AP @ C[:,r], AP @ C[:,r])) for r in range(len(O)))
        u = 0.0
        for r,s in itertools.combinations(range(len(O)),2):
            w = np.cross(C[:,r], C[:,s])
            pw = P @ w
            u += float(np.dot(pw,pw))
            lhs = np.cross(AP @ C[:,r], AP @ C[:,s])
            rhs = np.linalg.det(P) * (P @ w)
            max_adj_rel = max(max_adj_rel, float(np.linalg.norm(lhs-rhs)/(1+np.linalg.norm(rhs))))
        lhs = float(np.linalg.det(P@P + G))
        rhs = d + v + u + z
        max_rel = max(max_rel, float(abs(lhs-rhs)/(1+abs(lhs))))
        s1 = v*v - 3*d*u
        s2 = u*u - 3*v*z
        min_slack1 = min(min_slack1, float(s1))
        min_slack2 = min(min_slack2, float(s2))
        if max_rel > 1e-9 or s1 < -1e-7 or s2 < -1e-7:
            violations += 1
        trials += 1

out = {
    'seed': 20260923,
    'trials': trials,
    'violations': violations,
    'max_relative_cubic_identity_error': max_rel,
    'max_relative_adjugate_cross_error': max_adj_rel,
    'minimum_newton_slack_v2_minus_3du': min_slack1,
    'minimum_newton_slack_u2_minus_3vz': min_slack2,
    'partner_hybrid_constant': (9/2)*2**(4/9)*3**(1/6),
    'principal_threshold_constant_d_ge_1_4': 216*2**(1/3),
    'cross_E3_threshold_density_constant_z_ge_1_4': 10.345083232147514*4**(1/6),
    'cross_E3_threshold_L1_constant_z_ge_1_4': 2*math.pi*10.345083232147514*4**(1/6),
}
print(json.dumps(out, indent=2, sort_keys=True))
