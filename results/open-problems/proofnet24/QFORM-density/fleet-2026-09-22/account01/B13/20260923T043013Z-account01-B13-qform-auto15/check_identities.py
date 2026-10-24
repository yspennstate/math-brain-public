"""Deterministic checks for account01/B13 auto15.
Analytic proofs in REPORT.md do not depend on these floating checks.
"""
import numpy as np

rng = np.random.default_rng(20260923)
max_star_err = 0.0
max_zero_row = 0.0
max_compression_err = 0.0
max_spectrum_err = 0.0

for _ in range(500):
    n = 9
    h, i = 0, 1
    d = rng.normal()
    if abs(d) < 0.2:
        d = 0.2 if d >= 0 else -0.2
    c = rng.normal()
    b = rng.normal(size=n-2)
    defect = rng.normal(size=n-2)
    C = rng.normal(size=(n-2,n-2))
    C = (C + C.T)/2
    A = np.zeros((n,n))
    A[h,h] = d
    A[h,i] = A[i,h] = c*d
    A[i,i] = c*c*d
    A[h,2:] = b
    A[2:,h] = b
    A[i,2:] = c*b + defect
    A[2:,i] = c*b + defect
    A[2:,2:] = C

    idx = list(range(1,n))
    avec = A[idx,h]
    S = A[np.ix_(idx,idx)] - np.outer(avec,avec)/d
    star = sum((d*A[i,j] - A[i,h]*A[h,j])**2 for j in range(n) if j not in (h,i))
    row = S[0,1:]
    max_star_err = max(max_star_err, abs(star - d*d*np.dot(row,row)))

    # Exact zero-star endpoint: set defect=0 and verify proportional row + orthogonal compression.
    A[i,2:] = c*b
    A[2:,i] = c*b
    max_zero_row = max(max_zero_row, np.linalg.norm(A[i,:] - c*A[h,:]))
    s = np.sqrt(1+c*c)
    w = np.array([1.0,c])/s
    v = np.array([-c,1.0])/s
    O = np.eye(n)
    O[:2,:2] = np.column_stack([w,v])
    T = O.T @ A @ O
    max_compression_err = max(max_compression_err, np.linalg.norm(T[1,:]), np.linalg.norm(T[:,1]))
    evA = np.sort(np.linalg.eigvalsh(A))
    evB = np.sort(np.linalg.eigvalsh(np.delete(np.delete(T,1,axis=0),1,axis=1)))
    # Remove the eigenvalue of A closest to zero.
    k0 = np.argmin(np.abs(evA))
    evA_nz = np.delete(evA,k0)
    max_spectrum_err = max(max_spectrum_err, np.max(np.abs(np.sort(evA_nz)-evB)))

print({
    "trials": 500,
    "max_star_identity_error": max_star_err,
    "max_proportional_row_error": max_zero_row,
    "max_zero_compressed_rowcol_error": max_compression_err,
    "max_nonzero_spectrum_error": max_spectrum_err,
})
