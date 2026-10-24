import math
import numpy as np

c = math.sqrt(512/1601)
k = math.sqrt((1-c*c)/2)-c
C_large = 16*math.sqrt(2)*c**(-0.25)
C_small = 2**(13/4)*k**(-0.25)

assert c < 1/math.sqrt(3)
assert abs(k-c/32) < 1e-14
assert abs(C_large-C_small) < 1e-12

B0=np.array([[0.,1.,1.],[1.,0.,1.],[1.,1.,0.]])
evals=np.linalg.eigvalsh(B0)
assert np.allclose(evals,[-1.,-1.,2.])
P=B0[:2,:2]
D=abs(np.linalg.det(P))
kappa=np.linalg.svd(P,compute_uv=False)[-1]
tau=np.linalg.det(B0)/np.linalg.det(P)
C_B0=2**(13/4)*abs(np.linalg.det(B0))**(-0.25)*kappa**(-0.25)
assert abs(D-1)<1e-12 and abs(kappa-1)<1e-12 and abs(abs(tau)-2)<1e-12
assert abs(C_B0-8)<1e-12

rng=np.random.default_rng(20260923)
small_count=0
min_margin=float("inf")
for _ in range(5000):
    M=rng.normal(size=(3,3))
    B=(M+M.T)/2
    vals=np.linalg.eigvalsh(B)
    s0=np.min(np.abs(vals))
    if s0 < 1e-10:
        continue
    B=B/s0
    s=np.min(np.abs(np.linalg.eigvalsh(B)))
    if np.max(np.abs(np.diag(B))) < c*s:
        small_count += 1
        ok=False
        for i in range(3):
            js=[j for j in range(3) if j != i]
            j=max(js,key=lambda j:abs(B[i,j]))
            P=B[np.ix_([i,j],[i,j])]
            kap=np.linalg.svd(P,compute_uv=False)[-1]
            min_margin=min(min_margin,kap-k*s)
            if np.linalg.det(P)<0 and kap >= k*s-1e-12:
                ok=True
        assert ok

print("c_star =",repr(c))
print("k_star =",repr(k))
print("C3 =",repr(C_large))
print("B0_eigenvalues =",evals.tolist())
print("B0_tau =",repr(tau))
print("B0_branch_constant =",repr(C_B0))
print("random_small_diagonal_cases =",small_count)
print("random_min_kappa_margin =",repr(min_margin))
print("QFORM_B03_LOCALIZED_3X3_REPAIR_PASS")
