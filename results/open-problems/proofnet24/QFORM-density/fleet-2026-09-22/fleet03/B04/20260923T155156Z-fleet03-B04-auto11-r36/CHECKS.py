import itertools, json, math
import numpy as np

L = 32.0
V = np.eye(4) - 0.5*np.ones((4,4))
signs = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]], dtype=float)
R = np.zeros((5,4))
R[0,0] = L
R[1:,1:] = signs
M = R @ V

triple_vols = {}
for S in itertools.combinations(range(5),3):
    B = M[list(S),:]
    triple_vols[str(S)] = float(np.linalg.det(B @ B.T))

pair_vols = {}
for S in itertools.combinations(range(1,5),2):
    B = M[list(S),:]
    pair_vols[str(S)] = float(np.linalg.det(B @ B.T))

A0 = np.block([[np.zeros((5,5)), M],[M.T, np.zeros((4,4))]])
A = np.block([[np.ones((5,5))/100.0, M],[M.T, np.ones((4,4))/100.0]])

svals = np.linalg.svd(M, compute_uv=False)
eigs0 = np.linalg.eigvalsh(A0)
eigs = np.linalg.eigvalsh(A)
incident = [v for k,v in triple_vols.items() if k.startswith('(0,')]
nonincident = [v for k,v in triple_vols.items() if not k.startswith('(0,')]
Z3 = sum(incident)
Z2 = sum(pair_vols.values())
new_bound = 5*math.e*2**(-1/5)*(Z3*Z2)**(-1/10)
exact_bound = 5*math.e/(4*3**(1/5))
peer_gibbs = 2.853602893356842
peer_rank3 = 3.0

checks = {
    'V_orthogonality_error': float(np.linalg.norm(V.T@V-np.eye(4),2)),
    'M_singular_values': [float(x) for x in svals],
    'A0_eigenvalues': [float(x) for x in eigs0],
    'A_eigenvalues': [float(x) for x in eigs],
    'same_bank_perturbation_op_norm': 0.05,
    'weyl_large_eigenvalue_floor': 1.95,
    'all_M_entries_nonzero': bool(np.all(np.abs(M)>0)),
    'incident_triple_volumes': incident,
    'nonincident_triple_volumes': nonincident,
    'light_pair_volumes': list(pair_vols.values()),
    'Z3_incident': Z3,
    'Z2_light': Z2,
    'new_bound_numeric': new_bound,
    'new_bound_exact_formula_numeric': exact_bound,
    'peer_gibbs_bound': peer_gibbs,
    'peer_rank3_conditional_bound': peer_rank3,
    'new_strictly_improves_both': bool(new_bound < peer_gibbs < peer_rank3),
}

assert np.linalg.norm(V.T@V-np.eye(4),2) < 1e-12
assert np.allclose(svals, [32,2,2,2], atol=1e-10)
assert all(abs(v-8192.0)<1e-7 for v in incident)
assert all(abs(v-16.0)<1e-9 for v in nonincident)
assert all(abs(v-8.0)<1e-9 for v in pair_vols.values())
assert abs(Z3-49152.0)<1e-7
assert abs(Z2-48.0)<1e-9
assert abs(new_bound-exact_bound)<1e-12
assert sum(abs(x)>=1.0 for x in eigs) >= 3
assert new_bound < peer_gibbs < peer_rank3
checks['checks_pass'] = True
print(json.dumps(checks, indent=2, sort_keys=True))
