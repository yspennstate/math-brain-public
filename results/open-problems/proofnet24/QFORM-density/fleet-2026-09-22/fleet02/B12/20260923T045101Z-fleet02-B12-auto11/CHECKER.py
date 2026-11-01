import json, math
import numpy as np

rng = np.random.default_rng(2026092302)
taus = [-1e6,-1e4,-100,-10,-4,-1,-1e-6,0,1e-6,1,4,10,100,1e4,1e6]
min_core = float("inf")
min_s3_4d = float("inf")
min_s4_5d = float("inf")
max_schur_tail = 0.0
violations = 0
tests = 0

C = np.array([[4.,-3.,-3.,3.],
              [-3.,4.,-3.,3.],
              [-3.,-3.,4.,3.],
              [3.,3.,3.,-8.]])
v = np.ones(4)/2

for tau in taus:
    Ct = C + tau*np.outer(v,v)
    for _ in range(200):
        G = rng.normal(size=(5,5))
        G = (G+G.T)/2
        op = np.linalg.norm(G,2)
        radius = rng.uniform(0,0.25)
        T = G*(radius/op)
        A0 = np.zeros((5,5))
        A0[0,0] = 2.
        A0[1:,1:] = Ct
        A = A0 + T
        a = A[0,0]
        c = A[1:,0]
        S = A[1:,1:] - np.outer(c,c)/a
        H = [0,1,2] if tau <= 0 else [1,2,3]
        core = np.linalg.svd(S[np.ix_(H,H)],compute_uv=False)[-1]
        schur_tail = np.linalg.norm(S-Ct,2)
        s4 = np.linalg.svd(A,compute_uv=False)[3]
        A4 = Ct + T[1:,1:]
        s3_4d = np.linalg.svd(A4,compute_uv=False)[2]
        min_core = min(min_core,float(core))
        min_s4_5d = min(min_s4_5d,float(s4))
        min_s3_4d = min(min_s3_4d,float(s3_4d))
        max_schur_tail = max(max_schur_tail,float(schur_tail))
        if core < 12/7 - 1e-10 or schur_tail > 2/7 + 1e-10 or s4 < 7/4 - 1e-10 or s3_4d < 27/4 - 1e-10:
            violations += 1
        tests += 1

out = {
    "tests": tests,
    "violations": violations,
    "min_selected_schur_core_smin": min_core,
    "proved_selected_schur_core_lower_bound": 12/7,
    "max_observed_schur_tail_norm": max_schur_tail,
    "proved_schur_tail_upper_bound": 2/7,
    "min_full_5d_s4": min_s4_5d,
    "proved_full_5d_s4_lower_bound": 7/4,
    "min_direct_4d_s3": min_s3_4d,
    "proved_direct_4d_s3_lower_bound": 27/4,
    "direct_4d_density_constant": 24*math.sqrt(math.pi)/7,
    "schur_terminal_density_constant": 7*math.sqrt(math.pi)/2,
    "partner_lifted_density_constant": 2*math.sqrt(2*math.sqrt(math.pi))
}
print(json.dumps(out, indent=2, sort_keys=True))
