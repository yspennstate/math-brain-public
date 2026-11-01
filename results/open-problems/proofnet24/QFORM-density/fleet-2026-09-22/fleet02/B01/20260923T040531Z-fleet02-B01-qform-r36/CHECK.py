import math
import numpy as np


def check(m):
    n = 5*m
    v = []
    for g in range(5):
        x = np.zeros(n)
        x[g*m:(g+1)*m] = 1/math.sqrt(m)
        v.append(x)
    a,b,c,d,w = v
    A = np.outer(a+c,a+c) - np.outer(b-d,b-d) + np.outer(w,w)
    eig = np.linalg.eigvalsh(A)
    nz = eig[np.abs(eig) > 1e-9]
    maxdiag = float(np.max(np.abs(np.diag(A))))
    maxdet = 0.0
    for i in range(n):
        for j in range(i+1,n):
            maxdet = max(maxdet, abs(float(np.linalg.det(A[np.ix_([i,j],[i,j])]))))
    I = np.r_[0:2*m]
    J = np.r_[2*m:4*m]
    s = np.linalg.svd(A[np.ix_(I,J)], compute_uv=False)
    assert np.allclose(nz, [-2.0,1.0,2.0], atol=1e-9)
    assert abs(maxdiag - 1/m) < 1e-9
    assert abs(maxdet - 1/m**2) < 1e-9
    assert np.allclose(s[:2], [1.0,1.0], atol=1e-9)
    return nz, maxdiag, maxdet, s[:2]

for m in (2,3,5,8):
    nz, md, det, s = check(m)
    print(f"m={m} eig={nz.tolist()} maxdiag={md:.12g} maxdet={det:.12g} cross_s={s.tolist()}")
print(f"8sqrt2={8*math.sqrt(2):.15f}")
print("STATUS=PASS")
