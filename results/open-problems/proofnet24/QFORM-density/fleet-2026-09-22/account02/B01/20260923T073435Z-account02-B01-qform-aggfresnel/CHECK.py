import math
import numpy as np


def sylvester(m):
    H = np.array([[1.0]])
    while H.shape[0] < m:
        H = np.block([[H, H], [H, -H]])
    return H / math.sqrt(m)

eta = 0.25
c = 1.0 + eta
const = 20.0 / (3.0 * 2.0**(2.0/5.0))
print(f"r1_constant={const:.12f}")
print(f"bound_eta025={const*c**(-4.0/5.0):.12f}")

for m in [8, 16, 32, 64]:
    H = sylvester(m)
    u1, u2 = H[:, 0], H[:, 1]
    v1, v2, w = H[:, 0], H[:, 1], H[:, 2]
    K = c * (np.outer(u1, v1) + np.outer(u2, v2))
    A = np.block([[eta*H, K], [K.T, np.outer(w, w)]])
    eig = np.linalg.eigvalsh(A)
    abs_eig = np.sort(np.abs(eig))[::-1]
    svals = np.linalg.svd(K, compute_uv=False)
    maxdiag = np.max(np.abs(np.diag(A)))
    maxdet = 0.0
    for i in range(2*m):
        for j in range(i+1, 2*m):
            sub = A[np.ix_([i,j],[i,j])]
            maxdet = max(maxdet, abs(np.linalg.det(sub)))
    aug = np.column_stack([v1, v2, w])
    maxlev = np.max(np.sum(aug*aug, axis=1))
    assert abs(svals[0]-c) < 1e-10 and abs(svals[1]-c) < 1e-10
    assert np.sum(abs_eig >= 1-1e-10) >= 5
    assert maxlev <= 0.5
    print(
        f"m={m} top5_abs_eigs=" + ",".join(f"{x:.12f}" for x in abs_eig[:5])
        + f" maxdiag={maxdiag:.12f} maxpairdet={maxdet:.12f} maxlev={maxlev:.12f}"
    )

print("STATUS=PASS")
