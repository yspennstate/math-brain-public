"""Do the Brailovskaya-van Handel matrix-concentration parameters close the Veronese hard edge?

The Veronese Gram is X = sum_{i=1}^{n} Z_i, Z_i = z_i z_i^T - I_p, z_i = (x_i x_i^T - I)/sqrt2 in an
orthonormal basis of Sym_d (p = d(d+1)/2, E z z^T = I_p), x_i ~ N(0, I_d), n = p-1.

The framework's edge control needs the single-summand boundedness R(X) small against the variance
scale sigma(X): roughly R(X) << sigma(X) (log p)^{-beta}. The crux for the hard edge is the SCALING
of the ratio R/sigma with d. Measured here:

    sigma(X)^2 = || E X^2 || = n || E Z^2 ||,   E Z^2 = E[|z|^2 z z^T] - I_p   (since E z z^T = I),
    R(X)       = a high quantile / max of || Z_i ||_op ~ |z_i|^2,
    ratio      R / sigma.

If R/sigma -> 0 the tool closes the hard edge; if it stays order one it sits at the edge of
applicability (which would explain why the hard edge is HARD and the inverse smallest singular value
is not uniformly integrable at fixed d), and a truncation of the heavy |z|^2 tail is needed.
"""
import os, sys
for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[v] = "3"
import numpy as np


def zvec(X, d):
    """Orthonormal Sym_d coordinates of z=(xx^T - I)/sqrt2 for rows x of X (n,d). Returns (n,p)."""
    iu = np.triu_indices(d, 1)
    off = X[:, iu[0]] * X[:, iu[1]]                 # <z, (E_ab+E_ba)/sqrt2> = x_a x_b
    dia = (X ** 2 - 1.0) / np.sqrt(2.0)             # <z, E_aa> = (x_a^2 - 1)/sqrt2
    return np.concatenate([off, dia], axis=1)


print(f"{'d':>4} {'p':>6} {'n':>6} {'||EZ^2||':>10} {'sigma':>10} {'R(max)':>10} {'R(p99)':>10} "
      f"{'R/sig':>8} {'Rq/sig':>8} {'E|z|^2/p':>9}")
for d in (10, 16, 22, 28, 34, 40, 44):
    p = d * (d + 1) // 2
    n = p - 1
    rng = np.random.default_rng(11 + d)
    # estimate E Z^2 = E[|z|^2 z z^T] - I  by batches, accumulating the p x p matrix
    S = np.zeros((p, p))
    nz = []
    total = 0
    batches = max(4, 40000 // max(1, p))            # keep memory modest
    per = 2000
    for _ in range(batches):
        Xb = rng.standard_normal((per, d))
        Z = zvec(Xb, d)                              # (per, p)
        n2 = np.einsum("ij,ij->i", Z, Z)             # |z_i|^2
        nz.append(n2)
        S += (Z * n2[:, None]).T @ Z                 # sum |z|^2 z z^T
        total += per
    EZ2 = S / total - np.eye(p)                      # E[|z|^2 zz^T] - I
    normEZ2 = float(np.linalg.eigvalsh(EZ2)[-1])     # operator norm (symmetric, top eig)
    sigma = np.sqrt(n * normEZ2)
    nz = np.concatenate(nz)
    # ||Z_i|| = ||z_i z_i^T - I|| = max(|z_i|^2 - 1, 1) ~ |z_i|^2 for large; use |z|^2 as the scale
    Rmax = float(nz.max())
    Rq = float(np.quantile(nz, 0.99))
    print(f"{d:4d} {p:6d} {n:6d} {normEZ2:10.2f} {sigma:10.1f} {Rmax:10.1f} {Rq:10.1f} "
          f"{Rmax/sigma:8.3f} {Rq/sigma:8.3f} {nz.mean()/p:9.3f}", flush=True)
