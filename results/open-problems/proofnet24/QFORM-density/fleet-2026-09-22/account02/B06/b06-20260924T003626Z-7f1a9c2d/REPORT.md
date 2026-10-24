SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-24T00:36:26Z.
attacking: partner account03/B06 r48's singular-T nonresonant branch; replace the missing physical diagonal pivot by averaging the exact rank-one Schur square through the product law, then use the completed physical-pair logarithmic receiver instead of a curved-fiber supremum.

# account02/B06 — rank-one Schur-square payment without a physical diagonal pivot

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `ESSENTIAL_STEP_APPLIED + REFUTED_INTERMEDIATE_STRUCTURAL_CLAIM / FULL QFORM OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains OPEN / NOT PROVED / NOT DISPROVED. Essential boundedness is the target here; continuity is not claimed by the pair-log argument.

## 1. First unpaid implication, source boundary, and corrections

Fresh brain control was resolved before this calculation. OWNER CONTROL remains revision `2026-09-22.15`; QFORM is the sole active research target. The live correction inbox blob at the final pre-write refresh is `a884b835aba929c5376e6417ae5cfcd44c0f7a76`.

The newest designated partner account03/B06 result is r48:

- `yspennstate/math-open-problems@a4090a876e18635918b87f87a7af42726b29337a`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T001713Z-account03-B06-qform-r48/REPORT.md`.

Its exact shear-flat normal form is

`A=[[H,E],[E^T,C]]`, `H=H^T` invertible `2 x 2`,

`S:=C-E^T H^(-1)E = D+E^T T E`,

with `D` diagonal, `T=T^T` `2 x 2`, `G=E E^T`, and all coordinates literal original coordinates. r48 pays `det T!=0` after a heavy physical pivot when a post-pivot pair-area law is sufficiently disjoint. Its next debt explicitly includes `det T=0` with nonresonance `1+lambda v^T H v !=0` when `T=lambda vv^T`, and the repeated low-disjointness/two-heavy-hub branch.

I retain the standing corrections: no law-uniform pointwise quadratic-phase decay, no post-rotation independence, no arbitrary-joint rank-three coarea, no positive moment of worst conditional projection-density heights, no unrestricted curved-fiber supremum, no deletion of a nonzero quadratic tail, and no inference of a uniformly good individual physical minor.

The required pinned package was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

In particular `RESULTS.md` Section 7 records the completed two-coordinate logarithmic smoothing theorem, whose immutable proof is

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

That theorem is applied below at an actual inequality, not merely cited.

## 2. A product small-ball lemma for a rank-one square

Let `Y=(Y_j)_{j in J}` have independent cap-one densities and let `w!=0`. Put

`L=w dot Y`.

The sharp one-dimensional Rogozin--Ball product-projection bound gives

`||p_L||_infinity <= sqrt(2)/||w||_2`.                            (2.1)

For `lambda!=0`, define `R=lambda L^2`. For every `t in R` and `rho>0`, the inverse image

`{z: |lambda z^2-t|<rho}`

has total length at most

`2 sqrt(2 rho/|lambda|)`.                                         (2.2)

Indeed, after reflecting the output if necessary assume `lambda>0`. For `t<=-rho` the set is empty; for `-rho<t<=rho` it is contained in `|z|<sqrt((t+rho)/lambda)<=sqrt(2rho/lambda)`; for `t>rho` its total length is

`2[ sqrt((t+rho)/lambda)-sqrt((t-rho)/lambda) ]`,

which is decreasing in `t` and at `t=rho` equals `2 sqrt(2rho/lambda)`.

Combining (2.1)-(2.2),

`boxed:
 sup_t P(|lambda L^2-t|<rho)
 <= 4 (|lambda| ||w||_2^2)^(-1/2) sqrt(rho).`                     (2.3)

More generally, let `Z` be any random variable independent of `L`. Conditioning on `Z` and translating `t` shows

`boxed:
 sup_t P(|lambda L^2+Z-t|<rho)
 <= 4 (|lambda| ||w||_2^2)^(-1/2) sqrt(rho).`                     (2.4)

Thus arbitrary extra quadratic curvature on an original-coordinate bank disjoint from the support of `w` is harmless for this half-power small-ball payment. Nothing is conditioned on a spectral complement.

## 3. Main new receiver: indefinite physical pair + product rank-one square

### Theorem — `QFORM-PAIR-RANK1SQUARE-WEIGHTED-v1`

Let `X_1,X_2` be two literal original coordinates, independent of a remaining product bank `Y`. Suppose after completing that physical pair the exact quadratic polynomial has the form

`Q=((X_1,X_2)+m(Y))^T B ((X_1,X_2)+m(Y))
   + lambda (w dot Y_J)^2 + R_0(Y_K)`,                             (3.1)

where

- `B` is invertible and indefinite;
- `J,K` are disjoint original-coordinate subbanks of `Y`;
- `w` is supported on `J` and is nonzero;
- `R_0` is arbitrary and depends only on `Y_K` (affine and quadratic terms are allowed);
- the pair shift `m(Y)` may depend arbitrarily on every remaining coordinate.

Write

`D_B=|det B|`, `kappa_B=sigma_min(B)`.

Then the complete ambient law is absolutely continuous and

`boxed:
 ||p_Q||_infinity
 <= 8 sqrt(2)
    [D_B kappa_B |lambda| ||w||_2^2]^(-1/4).`                    (3.2)

#### Proof

The remainder in (3.1) is

`R=lambda(w dot Y_J)^2+R_0(Y_K)`.

Because the two banks are independent, (2.4) gives the translation-uniform estimate

`sup_t P(|R-t|<rho) <= H sqrt(rho)`,

with

`H=4 (|lambda| ||w||_2^2)^(-1/2)`.                               (3.3)

The completed physical-pair logarithmic theorem in the pinned package states that an invertible indefinite physical pair with such a remainder obeys

`||p_Q||_infinity <= 4 sqrt(2H) (D_B kappa_B)^(-1/4)`.            (3.4)

Substituting (3.3) into (3.4) gives exactly (3.2). The theorem explicitly permits arbitrary dependence of the translated pair centre `m(Y)` on the remainder, so no false conditional independence is introduced. QED.

This is a curved-fiber weighted receiver: the logarithmic singularity of the indefinite physical pair is not replaced by its infinite fiber supremum. It is integrated against the genuine product-derived half-power small-ball profile of the rank-one square.

## 4. Direct splice into partner r48's singular-T endpoint

In r48, suppose

`T=lambda v v^T`, `||v||=1`, `lambda!=0`,                        (4.1)

and first take the exact subbranch `D=0`. Then the two-hub Schur remainder is

`S=lambda (v^T E Y)^2`.                                           (4.2)

Set

`w=E^T v`.

Since `G=E E^T`,

`||w||_2^2=v^T G v`.                                               (4.3)

If the physical outer block `H` is indefinite, Theorem (3.2) applies with `B=H`, `R_0=0` and gives

`boxed:
 ||p_Q||_infinity
 <= 8 sqrt(2)
 [ |det H| sigma_min(H) |lambda| v^T G v ]^(-1/4).`               (4.4)

No environment diagonal pivot `D_hh` is required. The conclusion is valid both on and off the r48 resonance `1+lambda v^T H v=0`; nonresonance is therefore not itself the analytic difficulty in the exact `D=0` subbranch.

If `H` is definite, the already completed two-dimensional physical-pair area bound gives a uniform conditional density bound after conditioning on the environment, so the singular-T / `D=0` branch is paid there as well. The new content of (4.4) is the indefinite-pair case, where a logarithmic pair singularity really has to be averaged.

The same proof allows any part of the diagonal curvature `D` that lies on a product bank disjoint from `supp(E^T v)`; it is absorbed into `R_0` in (3.1). What remains unpaid is diagonal curvature on the same coordinates that feed the rank-one linear statistic.

## 5. Source-valid diffuse target family: nonresonance does not force a diagonal pivot or localized triple

A tempting structural shortcut would be:

> in the r48 branch `det T=0`, nonresonance plus three large eigenvalues should force either some `D_hh!=0` usable by the heavy-pivot compiler or a uniformly conditioned physical `3 x 3` principal block.

This is false even in an exact target family.

For `m>=2`, let

`u=m^(-1/2)(1,...,1)` on a `Y` bank of size `m`,
`v=m^(-1/2)(1,...,1)` on a disjoint `Z` bank of size `m`,

and set

`H=diag(1,-1)`,

`E=[[u,0],[0,v]]`, so `E E^T=I_2`,

`D=0`,

`T=-2 e_1 e_1^T`.                                                 (5.1)

Then

`U:=H^(-1)+T=-I_2`,

so the r48 nonresonance scalar is

`1+lambda e_1^T H e_1 = 1-2 = -1 !=0`.                            (5.2)

The full physical matrix is

`A_m=[[H,E],[E^T,-E^T E]]`.                                       (5.3)

Its quadratic form is

`Q_m=x_1^2-x_2^2+2x_1<u,Y>+2x_2<v,Z>-<u,Y>^2-<v,Z>^2`.           (5.4)

Because the two rows of `E` are orthonormal, an orthogonal change of basis used **only to compute the deterministic spectrum** reduces the nonzero part of `A_m` to the direct sum

`[[1,1],[1,-1]] direct_sum [[-1,1],[1,-1]]`.                     (5.5)

Therefore

`boxed: spec_nonzero(A_m)={sqrt(2),-sqrt(2),-2}.`                 (5.6)

Thus every `A_m` is an exact QFORM target.

Yet in the exact shear-flat representation (5.1),

`boxed: D_hh=0 for every environment coordinate h.`               (5.7)

Moreover no uniformly conditioned physical `3 x 3` principal block emerges as `m` grows. Put `r=m^(-1/2)`. A three-coordinate block containing no hub is singular. With exactly one hub, either two same-bank environment columns give an exact duplicate-direction null vector, or a mixed-bank block contains an isolated eigenvalue of magnitude `r^2`. With both hubs and one `Z` coordinate the block is singular. With both hubs and one `Y` coordinate, the only possibly small eigenvalue comes from

`[[1,r],[r,-r^2]]`,

whose determinant has magnitude `2r^2` while the other eigenvalue has magnitude at least one. Hence

`boxed:
 max_{|S|=3} sigma_min(A_m[S,S]) <= 2/m ->0.`                     (5.8)

So this family simultaneously has three fixed large eigenvalues, exact singular-T nonresonance, no `D`-pivot at all, and no uniformly good physical triple. This refutes the intermediate structural inference, not QFORM.

The new receiver (4.4) controls the whole diffuse family directly. Here

`|det H|=sigma_min(H)=v^T G v=1`, `|lambda|=2`,

so

`boxed:
 ||p_{Q_m}||_infinity
 <= 8*2^(1/4)
 = 9.513656920021768...`                                          (5.9)

for every `m` and every collection of independent input densities bounded by one.

Thus the obstruction is source-valid and paid: the missing third resource can be consumed by the rank-one Schur square itself through the logarithmic physical-pair receiver, without producing a physical diagonal pivot and without extracting a localized triple.

## 6. Required pinned-result application, explicitly at the inequality

The completed result from the required `e5f71d79...` package used here is the physical-pair logarithmic smoothing theorem recorded in `RESULTS.md` Section 7 and proved in the source-pinned pair-log report. In the present r48 splice its hypothesis is supplied by the actual product estimate

`sup_t P(|lambda(v^T E Y)^2-t|<rho)
 <= 4 (|lambda| v^T G v)^(-1/2) sqrt(rho)`.                       (6.1)

Putting (6.1) into the completed theorem gives the real r48 inequality (4.4). This is the required receiver use; it is not a theorem-name-only handoff.

As a separate check on the explicit family (5.3), one may also group the two disjoint banks and invoke the pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A after rescaling the bank projections to cap one. That gives another universal bound, but (5.9) is stronger and does not depend on the disjoint support of the two rows beyond the construction itself.

## 7. New correction and exact remaining debt

New correction ID:

`QFORM-RANK1T-NONRESONRANCE-NO-DPIVOT-LOCALBLOCK-v1`.

Statement: in the partner r48 shear-flat normal form, `det T=0`, `1+lambda v^T H v!=0`, rank `E=2`, and even the exact three-large-eigenvalue hypothesis do **not** imply a nonzero diagonal coefficient in `D` and do **not** imply a uniformly conditioned physical `3 x 3` principal block. The family (5.1)-(5.8) is an exact counterexample to that intermediate claim.

First unpaid implication after this run:

`QFORM-R48-RANK1T-SHARED-DIAGONAL-SQUARE-AVERAGING-v1`.

Keep r48's complete product structure with

`S=sum_j d_j Y_j^2 + lambda(w dot Y)^2`

when the diagonal terms and `w` live on the **same** original coordinates. Prove a translation-uniform half-power small-ball bound strong enough to feed the physical-pair logarithmic receiver, or route this shared-bank case into the r48 two-heavy-hub certificate without taking a worst conditional fiber supremum. The `D=0` and disjoint-diagonal-bank cases are now paid by (3.2)-(4.4). The example above proves that trying to manufacture a nonzero `D_hh` or a localized principal triple cannot be the missing bridge.

Full QFORM remains OPEN. Global continuity remains OPEN. No scheduler, task, email, notification, permission, account, public-release, or cross-account state was changed.

## 8. Source pins

- Fresh brain main before final write: `yspennstate/math-research-brain@332aee7e8c39f7f0223820f54f4cc83450b6d52e`; OWNER CONTROL `2026-09-22.15`.
- Live correction inbox blob: `a884b835aba929c5376e6417ae5cfcd44c0f7a76`.
- Newest designated partner account03/B06 r48: `yspennstate/math-open-problems@a4090a876e18635918b87f87a7af42726b29337a`, exact REPORT path above.
- Required pinned package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.
- Physical-pair proof: `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
- One-dimensional product projection input: sharp Rogozin/Ball / Juškevičius--Lee maximum-density consequence as used throughout the current QFORM source package; for nonzero `w`, `||p_<w,Y>||_infinity<=sqrt(2)/||w||_2`.
