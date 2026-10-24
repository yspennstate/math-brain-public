# account02/B10 substantive checkpoint — exact-graph near-null interpolation

Programme: `QFORM-DENSITY-3EIG-20260922`
Run: `20260923T014801Z-account02-B10-QFORM-auto11`
Status: supporting calculation; full QFORM remains OPEN.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The newest ruled-side theorem at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` already gives, for an exact-rank-three indefinite form with spectral scale at least one,

`p_Q(t) <= pi*sqrt(2)`

on the one-sheet side. I therefore work only on the surviving near-null/two-sheet geometry; I do not reprove that theorem.

Start from the quantitative one-heavy/one-transverse-bank geometry used in account03/B13: `A=RMR^T`, `R^TR=I_3`, `sigma_min(M)>=s`, heavy physical row `r_0=sqrt(c)u`, and a disjoint bank `B` whose rows are an exact graph over `u^perp`,

`r_j=(w dot p_j)u+p_j`, `p_j in u^perp`,

with `G=sum_B p_j p_j^T >= kappa I_2`. Put `h=det G`, `q=u^T M u`, and `D=|det M|`.

Because the total longitudinal Parseval mass outside the heavy row is `1-c`,

`w^T G w=sum_B (w dot p_j)^2 <=1-c`,

hence

`||w||^2 <=(1-c)/kappa`.

Condition on all original coordinates outside `{0} union B`. Let `Z=sum_B p_j X_j`; the source-valid two-dimensional product-projection theorem gives

`||p_Z||_infinity <=2/sqrt(h)`,

and `X_0` is genuinely independent of `Z`. In an orthonormal basis `(u,e_1,e_2)` of spectral space, set `Tz=z+(w dot z)u`, `F=[sqrt(c)u,Te_1,Te_2]`, and `H=F^T M F`. Then

`|det H|=cD`, `H_00=cq`.

Write the receiver block of `H` as `C=T^TMT` and its scalar-to-receiver cross vector as `b=sqrt(c)T^TMu`. The cross-transverse invariant used by account01/B16 is

`P=|b^T adj(C)b|=|cq det C-det H|`.

Let `n=u-w` (with `w` embedded in `u^perp`). The two graph columns have cross product `n`, so the 3D adjugate identity gives exactly

`det C=det(M) n^T M^(-1)n`.

Therefore

`P=cD |1-q n^T M^(-1)n|`.

Since `||M^(-1)||op<=1/s` and `||n||^2=1+||w||^2`, define

`eta=(|q|/s)(1+(1-c)/kappa)`.

If `eta<1`, then

`P >= cD(1-eta)`.

Applying account01/B16 `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1` to the actual independent scalar `X_0` and the actual two-dimensional bank projection `Z` yields

`||p_Q||_infinity
 <= C_CT * 2^(2/3) h^(-1/3)(cD)^(-1/3)(1-eta)^(-1/6)`,

`C_CT=103680^(1/3)`.

This is already uniform through `q=0`; no small random perturbation, support bound, or projected-coordinate independence is used.

For the live B13 constants `c>3/10`, `kappa=7/800`, one has `1+(1-c)/kappa<81`. Hence throughout

`|q|<=1/162`

we have `eta<=1/2`, `h>=kappa^2`, `D>=1`, and the explicit bound

`||p_Q||_infinity <2944.722`.

The complementary `|q|>=1/162` regime is to be spliced with the completed designated-partner account03/B10 nonnull rank-one-bank estimate

`||p_Q||_infinity <=128 sqrt(2) c^(-1/2)D^(-1/4)|q|^(-1/4)`,

which gives `<1179.080` at the same live constants. Thus the exact-graph bank branch should close for every scalar pivot, not merely the exact-null point. The final report will write the invariant proof and the splice carefully and record the positive-regression-residual branch as the remaining gap.
