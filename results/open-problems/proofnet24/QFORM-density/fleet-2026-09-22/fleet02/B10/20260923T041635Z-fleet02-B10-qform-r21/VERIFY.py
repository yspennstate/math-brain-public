import itertools, math
import numpy as np

DELTA = 1/128
M = 5

def check(rho):
    c = 1-rho
    b = math.sqrt(1+DELTA)
    rows = [math.sqrt(c)*np.array([1.,0.,0.]), math.sqrt(rho)*np.array([1.,0.,0.])]
    rows += [np.array([0.,1/math.sqrt(M),0.]) for _ in range(M)]
    rows += [np.array([0.,0.,1/math.sqrt(M)]) for _ in range(M)]
    R = np.vstack(rows)
    Lam = np.array([[DELTA,b,0.],[b,0.,0.],[0.,0.,1.]])
    A = R @ Lam @ R.T
    eig = np.linalg.eigvalsh(A)
    nz = eig[np.abs(eig)>1e-10]
    weights = []
    triples = []
    for S in itertools.combinations(range(len(rows)),3):
        w = np.linalg.det(R[list(S),:])**2
        if w > 1e-14:
            triples.append(S); weights.append(w)
    d = 0.0
    for S,w in zip(triples,weights):
        sS=set(S)
        for T,v in zip(triples,weights):
            if sS.isdisjoint(T): d += w*v
    d_formula = 2*c*rho*(1-1/M)**2
    hmax = max(float(r[1:]@r[1:]) for r in rows[1:])
    star = float(np.linalg.norm(A[0,1:]))
    print(f"rho={rho:.12g}")
    print("  parseval_error=", np.linalg.norm(R.T@R-np.eye(3)))
    print("  nonzero_eigenvalues=", nz.tolist())
    print("  plucker_weight_sum=", sum(weights))
    print("  disjoint_mass=", d, " formula=", d_formula, " error=", abs(d-d_formula))
    print("  max_residual_transverse_leverage=", hmax)
    print("  hub_diagonal=", A[0,0])
    print("  star_l2=", star)
    assert np.linalg.norm(R.T@R-np.eye(3)) < 1e-12
    assert np.max(np.abs(np.sort(nz)-np.array([-1.,1.,1+DELTA]))) < 1e-10
    assert abs(d-d_formula) < 1e-12
    assert hmax < 1/4
    assert A[0,0] < 1/64
    assert star > math.sqrt(1023)/64
    assert d < 1/64

for rho in (1/256, 1/1024, 1e-6):
    check(rho)
print("STATUS=PASS")
