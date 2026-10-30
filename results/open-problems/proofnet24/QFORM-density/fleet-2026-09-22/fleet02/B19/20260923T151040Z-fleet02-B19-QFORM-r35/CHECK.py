import math
import numpy as np

alpha = 1 / math.sqrt(6)
beta = 1 / math.sqrt(3)
assert abs(alpha*alpha + beta*beta - 0.5) < 1e-14

for m in (8, 16, 64):
    p = np.ones(m) / math.sqrt(m)
    r = np.r_[np.ones(m//2), -np.ones(m//2)] / math.sqrt(m)
    q = np.ones(m) / math.sqrt(m)
    s = np.r_[np.ones(m//2), -np.ones(m//2)] / math.sqrt(m)

    n = 1 + 2*m
    eh = np.zeros(n); eh[0] = 1
    pv = np.zeros(n); pv[1:1+m] = p
    rv = np.zeros(n); rv[1:1+m] = r
    qv = np.zeros(n); qv[1+m:] = q
    sv = np.zeros(n); sv[1+m:] = s

    a = eh + pv + qv
    b = eh + rv + sv
    c = alpha*(pv-qv) + beta*(rv-sv)
    A = np.outer(a,a) - np.outer(b,b) + np.outer(c,c)

    ev = np.linalg.eigvalsh(A)
    nz = ev[np.abs(ev) > 1e-10]
    assert np.max(np.abs(nz - np.array([-math.sqrt(8), 1, math.sqrt(8)]))) < 1e-10

    N = A[1:1+m, 1+m:]
    svN = np.linalg.svd(N, compute_uv=False)
    assert np.sum(svN > 1e-10) == 2
    assert abs(svN[0]*svN[1] - 7/6) < 1e-10

    assert abs(np.sum(A[1:1+m,0]**2) - 2) < 1e-10
    assert abs(np.sum(A[1+m:,0]**2) - 2) < 1e-10

    B = A[1:,1:]
    evB = np.linalg.eigvalsh(B)
    nzB = evB[np.abs(evB) > 1e-10]
    assert np.max(np.abs(nzB - np.array([-2,1,2]))) < 1e-10

    v1 = (pv+qv)[1:] / math.sqrt(2)
    v2 = (rv+sv)[1:] / math.sqrt(2)
    v3 = c[1:]
    lev = v1*v1 + v2*v2 + v3*v3
    assert np.max(lev) < 2/m + 1e-12
    assert np.max(lev) <= 0.5 + 1e-12

    maxdiag = np.max(np.abs(np.diag(A)))
    maxpair = 0.0
    for i in range(n):
        for j in range(i+1,n):
            maxpair = max(maxpair, abs(A[i,i]*A[j,j]-A[i,j]**2))
    assert maxdiag < 1/m + 1e-12
    assert maxpair <= 4/m + 1e-12

    print(f"m={m} spectrum={nz.tolist()} cross_product={svN[0]*svN[1]:.15f} "
          f"maxdiag={maxdiag:.15f} maxpair={maxpair:.15f} maxlev={np.max(lev):.15f}")

print(f"TheoremF_bound={12/(4**(1/3)):.15f}")
print("QFORM_B19_R35_INPLANE_THIRD_CHECK_PASS")
