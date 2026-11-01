# r42 finite diagnostic checks

These are finite diagnostics only; the proofs are the exact derivations in `REPORT.md`.

## Exterior identity

For random real vectors `a,b` and random symmetric `C` in background dimensions 5 and 8, with `i=0,j=1,K=rest`, form

`B=[[0,a_K],[b_i,C_iK],[b_j,C_jK]]`.

The diagnostic compared

`det(B B^T)`

against

`det(Gram(a_K, b_i C_jK-b_j C_iK)) + det(Gram(a_K,C_iK,C_jK))`.

Ten random trials in each tested dimension agreed to floating-point roundoff; no discrepancy above `1e-8` occurred.

A minimal reproduction is:

```python
import numpy as np
rng=np.random.default_rng(0)
for m in [5,8]:
    for _ in range(10):
        a=rng.normal(size=m); b=rng.normal(size=m)
        C=rng.normal(size=(m,m)); C=(C+C.T)/2
        i,j=0,1; K=[k for k in range(m) if k not in (i,j)]
        aa=a[K]; ci=C[i,K]; cj=C[j,K]
        B=np.vstack([np.r_[0,aa],np.r_[b[i],ci],np.r_[b[j],cj]])
        d=b[i]*cj-b[j]*ci
        rhs=np.linalg.det(np.vstack([aa,d])@np.vstack([aa,d]).T)
        rhs+=np.linalg.det(np.vstack([aa,ci,cj])@np.vstack([aa,ci,cj]).T)
        assert abs(np.linalg.det(B@B.T)-rhs)<1e-8
```

## Flat-rigidity model

Generate nonzero `a_i`, arbitrary `u_i`, and define off-diagonal

`C_ij=a_i a_j(u_i+u_j)`.

Then for every distinct `i,j`, the vector

`a_i C_{j,K}-a_j C_{i,K}`

is proportional to `a_K`, so every twisted wedge in Theorem 5.1 vanishes. A six-coordinate floating-point check gave maximum wedge-Gram determinant approximately `2.95e-10`, consistent with roundoff at the scales used.

## Constant

`3*sqrt(e)=4.946163812100385`.
