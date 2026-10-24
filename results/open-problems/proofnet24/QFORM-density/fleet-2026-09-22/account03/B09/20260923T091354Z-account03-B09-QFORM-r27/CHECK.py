import math
import numpy as np

rho0 = 1/512
tau = (rho0/2)**(1/3)
star_threshold = 1-rho0-tau
triangle_threshold = 1-rho0-tau/(1-tau)
large_rho_constant = 2*math.sqrt(math.e)*(512)**0.25
promoted_constant = 3*math.e**(1/3)*2**(1/6)

print('rho0', rho0)
print('tau', tau)
print('star_threshold', star_threshold)
print('triangle_threshold', triangle_threshold)
print('large_rho_constant_detG1', large_rho_constant)
print('promoted_pivot_constant', promoted_constant)

A = np.array([
    [1,1,0,0,0],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [0,1,0,0,0],
    [0,0,1,0,0],
], dtype=float)
eigs = np.linalg.eigvalsh(A)
print('regression_eigenvalues', repr(eigs.tolist()))
print('regression_large_eigenvalue_count', int(np.sum(np.abs(eigs) >= 1-1e-12)))

# Matrix determinant lemma regression for det(G-cc^T)=det(G)(1-c^T G^-1 c).
rng = np.random.default_rng(20260923)
max_det_err = 0.0
for _ in range(1000):
    C = rng.normal(size=(9,2))
    G = C.T @ C
    i = int(rng.integers(0, C.shape[0]))
    c = C[i]
    lhs = np.linalg.det(G - np.outer(c,c))
    ell = c @ np.linalg.solve(G,c)
    rhs = np.linalg.det(G)*(1-ell)
    max_det_err = max(max_det_err, abs(lhs-rhs))
print('max_det_leverage_abs_error', max_det_err)

# Numerical stress test of the weighted EKR lemma. This is regression evidence only.
# Generate sparse/concentrated random weighted edge laws so rho<1/4 is sampled often.
def check_weighted_ekr(weights, n):
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    w = np.asarray(weights, dtype=float)
    w /= w.sum()
    rho = 0.0
    for a,e in enumerate(edges):
        for b,f in enumerate(edges):
            if set(e).isdisjoint(f):
                rho += w[a]*w[b]
    if not (0 < rho < 0.25):
        return None
    t = (rho/2)**(1/3)
    star_req = 1-rho-t
    tri_req = 1-rho-t/(1-t)
    deg = np.zeros(n)
    edge_map = {}
    for x,(i,j) in zip(w,edges):
        deg[i] += x; deg[j] += x; edge_map[(i,j)] = x
    best_tri = 0.0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                best_tri = max(best_tri,
                    edge_map.get((i,j),0.0)+edge_map.get((i,k),0.0)+edge_map.get((j,k),0.0))
    margin = max(deg.max()-star_req, best_tri-tri_req)
    return margin

trials = 0
violations = 0
min_margin = float('inf')
for _ in range(20000):
    n = 7
    m = n*(n-1)//2
    raw = rng.gamma(shape=0.12, scale=1.0, size=m)
    out = check_weighted_ekr(raw,n)
    if out is not None:
        trials += 1
        min_margin = min(min_margin, out)
        if out < -1e-10:
            violations += 1
print('weighted_ekr_rho_lt_quarter_trials', trials)
print('weighted_ekr_violations', violations)
print('weighted_ekr_min_margin', min_margin if trials else None)
