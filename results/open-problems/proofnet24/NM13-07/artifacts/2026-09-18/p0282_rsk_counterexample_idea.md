# P0282 idea before code — exact RSK counterexample search plus boundary-defect route

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-07`
Canonical claim: `P0282`
Frozen metric: `N_exact`, the largest N with an archived exact-arithmetic certificate verifying Chen's fixed-size LIS log-concavity inequalities for every `1 <= n <= N`.

The source conjecture is

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`

for the counts `ell_{n,k}=#{sigma in S_n : LIS(sigma)=k}`.

The published finite computation recovered in the admission check reaches `n<=50`, but this worker's frozen metric is still `UNMEASURED` until it executes and archives its own exact certificate.

## Method #2 — attack the negation first

Use Robinson-Schensted exactly:

`ell_{n,k} = sum_{lambda |- n, lambda_1=k} (f^lambda)^2`,

with `f^lambda` computed as an exact integer by the hook-length formula. This searches for a literal source counterexample without enumerating `n!` permutations. For every tested `(n,k)`, compute the exact integer margin

`Delta_{n,k}=ell_{n,k}^2-ell_{n,k-1}ell_{n,k+1}`.

Any negative margin is a source-level refutation. If none appears, archive the largest completely verified cutoff and the smallest exact margin ratio encountered; do not extrapolate.

## Method #15 — break symmetry on purpose

Do not treat the whole Plancherel shape space as one symmetric bulk. Reindex the high-LIS edge by the defect

`j=n-k`.

This isolates the sparse family of partitions with first row `n-j`, where exact formulas can be derived for fixed small `j`. During the finite search, record the closest-to-zero margin by defect `j`; this asks whether the dangerous configurations are genuinely bulk or live near a boundary. A structured boundary obstruction would be more informative than another undifferentiated finite cutoff.

## Method #29 — add the boundary point / compactify the tail

Treat fixed `j=n-k` as a boundary coordinate and derive exact formulas for the first few defect layers. In particular,

- `ell_{n,n}=1`,
- `ell_{n,n-1}=(n-1)^2`,
- for the two defect-2 shapes `(n-2,2)` and `(n-2,1,1)`,
  `ell_{n,n-2}=[n(n-3)/2]^2+[(n-1)(n-2)/2]^2` once the shapes are valid.

Try to prove the `k=n-1` log-concavity inequality symbolically for the full valid range, and, if the fixed-defect algebra stays tractable, push one layer deeper. This is an analytic boundary theorem, not a substitute for the all-`k` source conjecture.

Only after this note is committed should an exact checker be written or executed. A finite verification may move `N_exact`; a boundary theorem is recorded separately and does not change the metric normalization.