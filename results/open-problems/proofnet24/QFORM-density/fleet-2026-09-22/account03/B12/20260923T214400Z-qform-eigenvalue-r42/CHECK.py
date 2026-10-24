import numpy as np
from math import sqrt

rng = np.random.default_rng(202609232144)
N = 10000
viol1 = viol2 = viol3 = 0
min1 = min2 = min3 = float('inf')

for _ in range(N):
    m = int(rng.integers(3, 15))
    q = int(rng.integers(3, 20))
    B = rng.normal(size=(m, q))
    w = B[0].copy()
    h = np.linalg.norm(w)
    P = np.outer(w, w) / (h*h)
    R = B[1:] @ (np.eye(q)-P)

    s2 = np.linalg.svd(B, compute_uv=False)[1]
    opR = np.linalg.svd(R, compute_uv=False)[0]
    margin1 = opR-s2
    min1 = min(min1, margin1)
    viol1 += margin1 < -1e-9

    rownorms = np.linalg.norm(R, axis=1)
    jj = int(np.argmax(rownorms))
    j = jj+1
    G2 = B[[0,j]] @ B[[0,j]].T
    area = sqrt(max(np.linalg.det(G2), 0.0))
    target2 = h*s2/sqrt(m-1)
    margin2 = area-target2
    min2 = min(min2, margin2)
    viol2 += margin2 < -1e-8

    M = B[[0,j]]
    P2 = M.T @ np.linalg.inv(M@M.T) @ M
    inds = [k for k in range(m) if k not in (0,j)]
    C = B[inds] @ (np.eye(q)-P2)
    F = np.linalg.norm(C, 'fro')
    if F > 1e-12:
        row2 = np.sum(C*C, axis=1)
        kk = int(np.argmax(row2))
        if row2[kk] > 0.5*F*F:
            k = inds[kk]
            M3 = B[[0,j,k]]
            vol3 = np.prod(np.linalg.svd(M3, compute_uv=False)[:3])
            S = sqrt(np.linalg.det(M@M.T))
            target3 = S*F/sqrt(2)
            margin3 = vol3-target3
            min3 = min(min3, margin3)
            viol3 += margin3 < -1e-7

print({
    'seed': 202609232144,
    'trials': N,
    'viol_s2_vs_projected_op': int(viol1),
    'viol_pair_area': int(viol2),
    'viol_concentrated_three_volume': int(viol3),
    'min_margin_s2_vs_projected_op': float(min1),
    'min_margin_pair_area': float(min2),
    'min_margin_concentrated_three_volume': float(min3),
})
