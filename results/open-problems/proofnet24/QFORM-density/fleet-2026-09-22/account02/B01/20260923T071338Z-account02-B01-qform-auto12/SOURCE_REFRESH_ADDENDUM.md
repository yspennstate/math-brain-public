# Source-refresh addendum — newest partner result applied

This addendum is later than `REPORT.md` and therefore controls any stale partner wording in that report. The cofactor theorem and all proofs in `REPORT.md` are unchanged.

Before final publication, the designated partner directory was refreshed and a newer completed account03/B01 handoff was present:

`account03-B01-20260923T065657Z-auto11-detarea.md`, canonical mathematics
`yspennstate/math-open-problems@e37f094a72721e92fa82334f3b55ee4dd6d6695b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T065657Z-auto11-detarea/REPORT.md`.

Its theorem is strictly newer than the logarithmic transverse-curvature receiver cited in the body of `REPORT.md`.

## Newest partner theorem actually applied

Partition original coordinates into disjoint banks `I,J,D,W`. If

`Q=2 X_I^T K X_J + c(X_D,X_W)^T X_J + H(X_I,X_D,X_W)`,

where the `J` bank enters only affinely, `H` is otherwise arbitrary, and the two largest singular values of `K` are `kappa_1>=kappa_2>0`, then

`||p_Q||_infinity <= 2 sqrt(pi) (kappa_1 kappa_2)^(-1/2)`.       (A.1)

No pointwise scalar Fresnel decay is used; the proof averages an inverse-radius singularity against the bounded density of a two-dimensional orthogonal projection of an original product bank. The theorem also yields the corresponding signed-Fejer/distribution-function bound.

Apply (A.1) to the target-valid family from `REPORT.md`,

`A_{m,eps,delta}=[[B_{eps,delta},K],[K^T,0]]`,
`B_{eps,delta}=eps u1u1^T+delta vv^T`,
`K=U V_m^T`,

with the three-center bank as `I` and the leaves as `J`. The entire center quadratic curvature belongs to the arbitrary `H`; the leaf bank has no self-curvature and hence is genuinely affine. Since the two nonzero singular values of `K` are exactly `1,1`, the newest partner theorem gives

`boxed: ||p_{X^T A_{m,eps,delta}X}||_infinity <= 2 sqrt(pi)
       = 3.5449077018...`                                       (A.2)

for every `m,eps,delta` in the family and every independent cap-one input law.

This is stronger than the `4*3^(1/4)=5.264296...` Theorem-H estimate in the original report. The required newest Claude/Fresnel result remains genuinely applied there: Theorem H independently gives the latter bound when two center coordinates are used as physical hubs and the deleted center coordinate is left unrestricted.

## What the comparison now says

For `delta>0`, the predecessor account03/B01 logarithmic transverse-curvature receiver remains a valid inequality on the same family:

`||p_Q||_infinity <= (135e/32)[4+log_+(1/delta)]`.              (A.3)

As `delta->0`, (A.3) diverges while the **newest** partner theorem (A.2) remains `<3.545`. Thus the structural lesson is even sharper than stated in `REPORT.md`: a proof must expose and spend one-sided-affine two-area structure before paying a tiny local transverse curvature whenever that structure is available.

At the exact endpoint `delta=0`, `d=g=0` and `Bv=0`; the cofactor synchronization theorem in `REPORT.md` remains the useful connector for cases where the opposite bank is not affine. The newest partner theorem does not pay simultaneous nonlinear self-curvature on both active banks, exactly as its own boundary states.

Accordingly the first unpaid implication is refined to:

`QFORM-KERNEL-COFACTOR-TO-TWO-SIDED-CURVED-ROUTING-v1`:
when `Bv=0`, use the synchronized physical pair and surviving cross area to route either to the newest one-sided-affine determinant-area receiver, the source Theorem-H diagonal/low-rank leaf receiver, or another already-paid packet; the genuinely residual case is substantial nonlinear curvature on both active banks with no such product-preserving exit.

Full QFORM remains OPEN. This addendum makes no new continuity claim.
