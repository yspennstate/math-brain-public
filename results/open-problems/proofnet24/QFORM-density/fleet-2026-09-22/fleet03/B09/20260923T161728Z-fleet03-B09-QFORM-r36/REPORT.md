# fleet03/B09 r36 — column-diffuse third-volume smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Logical worker: `fleet03/B09`  
Run: `20260923T161728Z-fleet03-B09-QFORM-r36`  
Status: supporting theorem proved/applied; full QFORM remains OPEN.  
Continuity: proved only in the branch below.  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and source-valid setting

The full target is the universal bounded-density conjecture for `Q=X^TAX` with independent real coordinates whose densities are at most one and with at least three eigenvalues of `A` of magnitude at least one. No moment, compact-support, log-concavity, connected-support, Gaussian, or rotated-independence hypothesis is used here.

This run continues the r35 localized two-hub branch. In that branch a literal physical hub pair `a,b` and a physical leaf partition `S,T` were obtained. Put

`R={a,b} union S`, `M=A[R,T]`.

The r35 anchored volume is

`V_ab(S)=sum_{k in S} sum_{J subset T, |J|=3} det M[{a,b,k},J]^2`

and r35 proved

`V_ab(S) >= (27/400) G_*`.

The unresolved issue was interpolation across zero/rank-one/indefinite strata of the pair core `E=A[{a,b},{a,b}]`: every exact-core formula was available, but reciprocal powers of `det E`, `sigma_min(E)`, or the nonzero rank-one coefficient blew up near a lower-rank stratum.

The present result removes `E` entirely in a substantial subbranch.

## 2. Dependency read in full scope

The regularized-determinant theorem from

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

at

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`

proves the following. For any physical original-coordinate cut `I|J`, `B=A[I,J]`, if the coordinate leverage of the projection onto `range(B)` on the `I` side is at most `1/2`, then

`|phi_Q(t)| <= det(I + alpha t^2 B B^T)^(-1/4),   alpha=2/(pi^2 e^2)`.

The theorem retains arbitrary quadratic self blocks, arbitrary outside coordinates/couplings, affine terms, signs, and arbitrarily small extra singular values. Swapping the two physical sides replaces `B` by `B^T`, so the same statement may be invoked using the leverage of `range(B^T)` on the column side.

No correction in the refreshed QFORM correction inbox challenges this exact regularized-determinant statement.

## 3. New theorem: `QFORM-COLUMN-DIFFUSE-E3-SMOOTHING-v1`

Let `I,J` be disjoint original-coordinate sets and `B=A[I,J]`. Define the third cross-volume

`Z_3(B)=e_3(B^T B)=e_3(B B^T)`.

Equivalently, by Cauchy--Binet,

`Z_3(B)=sum_{R subset I, |R|=3} sum_{C subset J, |C|=3} det(B[R,C])^2`.

Assume

`max_{j in J} (P_range(B^T))_{jj} <= 1/2`

and `Z_3(B)>0`. Then the full quadratic form, with completely arbitrary same-bank quadratic blocks and all outside couplings retained, has a continuous density satisfying

`||p_Q||_infinity <= C_3 Z_3(B)^(-1/6)`

where

`C_3 = e/(6 sqrt(2)) * Beta(1/6,1/12) = 5.655763773387239...`.

Consequently every interval `L` satisfies

`P(Q in L) <= C_3 Z_3(B)^(-1/6) |L|`.

### Proof

Apply the source regularized-determinant theorem after swapping the two physical banks. With `alpha=2/(pi^2 e^2)`,

`|phi_Q(t)| <= det(I + alpha t^2 B^T B)^(-1/4)`.

For any positive-semidefinite matrix `K`,

`det(I+sK)=sum_{k>=0} s^k e_k(K) >= 1+s^3 e_3(K)`

for `s>=0`. Hence

`|phi_Q(t)| <= (1 + alpha^3 Z_3(B) t^6)^(-1/4)`.

This is integrable. Fourier inversion gives

`||p_Q||_infinity <= (1/(2pi)) int_R (1 + alpha^3 Z_3 t^6)^(-1/4) dt`.

Using

`int_0^infinity (1+u^6)^(-1/4) du = (1/6) Beta(1/6,1/12)`

and `alpha^(-1/2)=pi e/sqrt(2)` yields exactly

`||p_Q||_infinity <= [e/(6sqrt(2)) Beta(1/6,1/12)] Z_3^(-1/6)`.

Because the characteristic function is in `L^1`, the density is continuous and vanishes at infinity. QED.

The important point is that only the aggregate third elementary symmetric volume is paid. Arbitrarily many smaller nonzero cross singular values cause no reciprocal product loss.

## 4. Application to the r35 near-stratum debt

Take the r35 cut

`M=A[{a,b} union S, T]`.

Every determinant counted by `V_ab(S)` is one of the nonnegative summands in `Z_3(M)`. Therefore

`Z_3(M) >= V_ab(S) >= (27/400) G_*`.

If the **column-side** range projection is diffuse,

`max_{j in T} (P_range(M^T))_{jj} <= 1/2`,

then the theorem gives the pair-core-free estimate

`||p_Q||_infinity <= C_3 V_ab(S)^(-1/6)`

and hence

`||p_Q||_infinity <= C_3 (400/27)^(1/6) G_*^(-1/6)`

with

`C_3 (400/27)^(1/6)=8.86354185148296...`.

Thus

`boxed: ||p_Q||_infinity < 8.864 G_*^(-1/6)`

throughout this branch, with a continuous density and the same coefficient multiplying interval length.

This estimate is completely independent of the physical pair core `E`. It therefore closes the r35 **near-stratum interpolation** problem whenever the opposite physical bank is column-diffuse. No limiting argument in `det E` and no deletion of a small quadratic coefficient is used.

The remaining survivor is now sharper:

`QFORM-LOCALIZED-HUBPAIR-HIGH-COLUMN-LEVERAGE-v1`:

`max_{j in T}(P_range(M^T))_{jj}>1/2`, while the anchored volume `V_ab(S)` remains at least `27G_*/400`. The next step should turn this column localization into either a physical 3x3 cross determinant paid by fleet04/B09, a finite-core/coloop endpoint, or another aggregate determinant law before reciprocal inversion.

## 5. Stress test: extra tiny singular values are harmless here

For integers `m>=2` and `0<eps<=1`, define a `4 x 4m` physical cross matrix `B_{m,eps}` with four disjoint column groups of size `m`. Row `r=1,2,3` equals `m^(-1/2)` on its own group and zero elsewhere; row `4` equals `eps m^(-1/2)` on the fourth group.

Then the nonzero singular values are exactly

`1,1,1,eps`,

so

`Z_3(B)=1+3 eps^2`.

The projection onto `range(B^T)` has every nonzero coordinate leverage exactly `1/m`, hence satisfies the `1/2` gate. Therefore

`||p_Q||_infinity <= C_3 (1+3eps^2)^(-1/6) <= C_3`

for the full quadratic form with this cross block, regardless of arbitrary same-bank curvature.

For the pure hyperbolic block matrix

`A=[[0,B],[B^T,0]]`

the nonzero spectrum is

`{+1,+1,+1,+eps,-1,-1,-1,-eps}`,

so this is a target-valid family for every `eps>0`. The full-rank product-of-all-singular-values cross-fiber estimate would deteriorate like `eps^(-1/4)`, while the new `e_3` estimate stays bounded.

At `m=16`, `eps=10^(-8)`, the new bound is `5.655763773...`. A literal physical `3x3` cross minor using one column from each of the first three groups has determinant `m^(-3/2)=1/64`; applying the designated fleet04/B09 theorem gives the valid but larger estimate

`||p_Q||_infinity <= 3*(64)^(1/3)=12`.

This is an actual application of the designated partner result and illustrates precisely why aggregate third volume should be spent before reciprocal physical-minor selection.

## 6. Designated partner result actually applied

Partner `fleet04/B09` proved `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1` at

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`

with canonical report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.

For any literal invertible physical `3x3` cross block `K`, it proves

`||p_Q||_infinity <= 3 |det K|^(-1/3)`

with arbitrary self blocks and a continuous density. On the target-valid stress family above, the stated physical minor has `|det K|=1/64`, so the partner theorem yields exactly `12`.

## 7. Scope and unresolved implication

This run does **not** prove the full QFORM conjecture. It proves a new branch that is uniform across all pair-core strata and converts r35's anchored determinant currency into a direct `O(|L|)` bound whenever the opposite-bank range projection has leverage at most `1/2`.

The full target and full-target continuity remain OPEN. The next B09 debt is the high-column-leverage branch described above. No Gaussianity, moments, compact support, log-concavity, connected support, diagonalization of the product law, or Monte Carlo inference is used.
