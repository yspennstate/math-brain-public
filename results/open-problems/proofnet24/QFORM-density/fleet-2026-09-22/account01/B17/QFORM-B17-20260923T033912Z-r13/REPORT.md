# QFORM B17 — all equal-magnitude three-dimensional rotations and a finite one-heavy envelope

Run: `QFORM-B17-20260923T033912Z-r13`  
Account/slot: `account01/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed: revision `2026-09-22.15`  
Status: `NEW_SUPPORTING_SHARP-WITNESS_THEOREM`; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity of the full target remains separate.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and live corrections

The target remains: independent real physical coordinates with probability densities bounded by one, and a real symmetric quadratic-form matrix having at least three eigenvalues of modulus at least one. The unrestricted theorem is still open.

This report does **not** use any of the live refuted interfaces: no law-uniform pointwise Fresnel decay, no arbitrary-joint three-dimensional coarea bound, no positive moment of conditional projection-density caps, no independence after spectral rotation, no fixed finite-fragment bathtub reduction, and no forced good local cross-minor. The proof below keeps the original-coordinate product structure in the far field and uses only the trivial joint cap `prod_i f_i<=1` in a bounded physical ball.

The current sharp target-level lower obstruction remains

\[
C_{\rm univ}\ge 3\sqrt2,
\]

from exact source-valid diffuse product families with nonzero spectrum `{1,1,-1}`. The earlier account01/B17 periodic-frame expansion additionally shows that fixed diffuse cube frames approach `3sqrt(2)` from below. This report is an upper/exclusion theorem for a large rotated finite-dimensional stress class, not a new lower bound.

## 2. New theorem: the full equal-magnitude three-dimensional rotation orbit

### `QFORM-3D-EQUALMAG-ROTATION-v1`

Let `X=(X_1,X_2,X_3)` have independent real coordinates, each with probability density bounded by one. Let `B` be a real symmetric `3x3` matrix of indefinite signature such that

\[
B^2=\alpha^2 I_3,
\qquad \alpha\ne0.
\tag{2.1}
\]

Equivalently, the eigenvalues of `B` are either `(alpha,alpha,-alpha)` or `(alpha,-alpha,-alpha)`, up to the sign of `alpha`; this is the **entire orthogonal rotation orbit** of the equal-magnitude signature `(2,1)` form. For arbitrary `ell in R^3` and `c in R`, put

\[
Q=X^T B X+2\ell^T X+c.
\]

Then `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le {C_{\rm rot}\over |\alpha|},
\qquad
C_{\rm rot}=2\sqrt{3\pi\sqrt6}
=9.609557105905257\ldots .
}
\tag{2.2}
\]

No centering, moments, support connectedness, symmetry, unimodality or regularity of the input densities is assumed.

The estimate is uniform over **all rotations** of the eigenbasis. It improves, on this exact orbit, the existing general three-variable affine bound

\[
(2\pi+3\sqrt3)/|\alpha|
=11.479337729886218\ldots/|\alpha|.
\]

The gain comes from computing the bounded-ball indefinite cone density exactly instead of using the coarser `2pi r` volume estimate.

### Ambient corollary

If an arbitrary high-dimensional symmetric matrix `A` has a physical three-coordinate principal block `B` satisfying (2.1), then after conditioning on every other original coordinate the remaining polynomial is exactly of the affine form above. Hence

\[
\boxed{
\|p_{X^TAX}\|_\infty\le C_{\rm rot}/|\alpha|
}
\tag{2.3}
\]

with **all outside quadratic coefficients and cross-couplings arbitrary**. This is only a scoped physical-block theorem; the bare three-large-eigenvalue hypothesis does not force such a block.

## 3. Reduction to a symmetric orthogonal involution

Complete the square:

\[
X^T B X+2\ell^T X+c
=(X+B^{-1}\ell)^T B(X+B^{-1}\ell)
+c-\ell^TB^{-1}\ell.
\]

A deterministic coordinatewise translation preserves independence and every density cap. Output translation does not change the density norm. Scaling by `|alpha|` changes the output density norm by `1/|alpha|`. We may therefore take

\[
B=H,
\qquad H^T=H,
\qquad H^2=I_3,
\qquad \operatorname{sig}(H)=(2,1).
\tag{3.1}
\]

The `(1,2)` case follows by replacing the output by its negative. Write

\[
q(x)=x^THx,
\qquad \nabla q(x)=2Hx.
\]

Because `H` is orthogonal,

\[
|Hx|=|x|.
\tag{3.2}
\]

Fix `r>0` and an output interval `J` of length `eta`. Split the probability into the physical ball `N_r={|x|<=r}` and its complement.

## 4. Exact near-field cone-volume constant

On `N_r` the product density is at most one. Orthogonally diagonalize `H`; the change of variables has unit Jacobian. Thus it is enough to bound the Lebesgue pushforward of the radius-`r` ball under

\[
q_0(z)=z_1^2+z_2^2-z_3^2.
\]

Set `s=z_3` and `u=z_1^2+z_2^2`. Planar area is

\[
2\pi\rho\,d\rho=\pi\,du,
\]

so the density at output `t` is `pi` times the length of the set of `s` satisfying

\[
0\le t+s^2\le r^2-s^2.
\tag{4.1}
\]

For `0<=t<=r^2`, that length is

\[
\sqrt{2(r^2-t)}\le\sqrt2\,r.
\tag{4.2}
\]

For `t=-u_0` with `0<=u_0<=r^2`, it is

\[
2\left(\sqrt{(r^2+u_0)/2}-\sqrt{u_0}\right)
\le\sqrt2\,r,
\tag{4.3}
\]

because the displayed function is decreasing for `u_0>0`. Outside `[-r^2,r^2]` it is zero. Therefore the exact bounded-ball pushforward density obeys

\[
\boxed{
\|p_{q_0,\,|z|\le r}^{\rm Leb}\|_\infty
\le\pi\sqrt2\,r.
}
\tag{4.4}
\]

Consequently

\[
\Pr(X\in N_r,\ q(X)\in J)
\le \pi\sqrt2\,r\,\eta.
\tag{4.5}
\]

No independence after the orthogonal change of variables is asserted or needed: on this bounded near region we use only the original product-density cap `<=1`, which survives as a pointwise bound under the unit-Jacobian rotation.

## 5. Far-field original-coordinate slicing

On `N_r^c`, (3.2) implies `|Hx|>r`. Hence for at least one original coordinate `i`,

\[
|(Hx)_i|>r/\sqrt3.
\]

Let `E_i` be the part of `{q(X) in J}` where this inequality holds. Condition on the other two **original** coordinates. As a function of `x_i`, `q` is a real quadratic and

\[
{d\over dx_i}q(x)=2(Hx)_i.
\]

The set where `|(Hx)_i|>r/sqrt3` is the union of at most two intervals, and `q` is monotone on each. Each inverse image of `J` has length at most

\[
{\eta\over 2r/\sqrt3}.
\]

Summing the at most two monotone pieces gives conditional allowed length at most `sqrt3 eta/r`. Since the conditioned physical coordinate has density at most one,

\[
\Pr(E_i)\le {\sqrt3\over r}\eta.
\]

Summing `i=1,2,3`,

\[
\boxed{
\Pr(X\in N_r^c,\ q(X)\in J)
\le {3\sqrt3\over r}\eta.
}
\tag{5.1}
\]

Combining (4.5) and (5.1) gives, for every `r>0`,

\[
\Pr(q(X)\in J)
\le
\left(\pi\sqrt2\,r+{3\sqrt3\over r}\right)\eta.
\tag{5.2}
\]

The optimizing radius is

\[
r_*^2={3\sqrt3\over\pi\sqrt2},
\tag{5.3}
\]

and

\[
\pi\sqrt2\,r_*+{3\sqrt3\over r_*}
=2\sqrt{(\pi\sqrt2)(3\sqrt3)}
=2\sqrt{3\pi\sqrt6}.
\]

Since (5.2) holds for every interval, the output law is dominated by `C_rot` times Lebesgue measure and therefore has an essentially bounded density. This proves (2.2).

Continuity is **not** claimed by this argument.

## 6. Applying the completed designated partner result to an actual inequality

The latest completed `account02/B17` theorem is source-pinned at

`yspennstate/math-open-problems@189fc052089ae2d3237bc0865b290b01b26a6513`

and proves the exact finite extremizer for

\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m),
\qquad
\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.
\]

Writing

\[
S_m=m^{-1/2}\sum_{j=1}^mU_j,
\qquad
T_m=m^{-1/2}\sum_{j=1}^mV_j,
\]

it proves, for every cap-one heavy law `f`,

\[
\boxed{
\sup_f\|p_{X_f^2+S_m^2-T_m^2}\|_\infty
=p_{U^2+S_m^2-T_m^2}(0),
\quad U\sim {\rm Unif}[-1/2,1/2].
}
\tag{6.1}
\]

This is now inserted into a quantitative inequality rather than merely cited.

For `m>=2`, the residual two-frame behind `S_m^2-T_m^2` has `2m` rows, each of leverage `1/m<=1/2`, and spectral matrix `Gamma=diag(1,-1)`, hence `|det Gamma|=1`. The completed account03/B01 sharp dependence-safe square theorem at

`yspennstate/math-open-problems@a80bb254a3a1e2883cbfabdf03b53919d6621990`

(or its full r12 exposition at `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260922T142626Z-account03-B01-qform-r12/REPORT.md`) gives

\[
\|p_{X_f^2+S_m^2-T_m^2}\|_\infty
\le 2\sqrt\pi\,3^{1/4}\sqrt{B_m},
\tag{6.2}
\]

where its exact leverage product is

\[
B_m
=\prod_{j=1}^{2m}(1-1/m)^{-(1-1/m)/2}
=(1-1/m)^{-(m-1)}.
\tag{6.3}
\]

Applying the partner equality (6.1) to the left side yields the concrete scalar-sequence inequality

\[
\boxed{
p_{U^2+S_m^2-T_m^2}(0)
\le
2\sqrt\pi\,3^{1/4}(1-1/m)^{-(m-1)/2}
<2\,3^{1/4}\sqrt{\pi e}
=7.691879759019983\ldots .
}
\tag{6.4}
\]

The strict `B_m<e` follows from `-log(1-x)<x/(1-x)` with `x=1/m`. For `m=1`, the partner family is the diagonal control and the exact cap is at most `pi`.

Thus the completed partner theorem, when combined with an independent proved residual-smoothing estimate, turns the arbitrary heavy-law optimization into a single explicit centered-interval sequence and gives a **uniform finite-m global envelope** for every member of that source-valid one-heavy family. The partner's sharper Gaussian-completion calculation further gives

\[
\lim_{m\to\infty}p_{U^2+S_m^2-T_m^2}(0)
={12\over\pi}\int_0^{1/2}K_0(6x^2)\,dx
=3.5306641257709305\ldots<3\sqrt2,
\]

with a negative `1/m` correction. Inequality (6.4) does **not** prove that every intermediate finite `m` is below `3sqrt(2)`; that sharper scalar question remains open in the partner report.

## 7. Witness-side consequences

The currently certified witness picture is therefore:

1. the universal constant, if it exists, satisfies `C>=3sqrt(2)=4.2426406871...` by exact finite diffuse product families approaching the Gaussian signature `(1,1,-1)` law;
2. every genuinely three-dimensional equal-magnitude rotated physical block is globally bounded by `C_rot=9.609557...`, uniformly over all input laws and all rotations;
3. the one-heavy majority-sign family has an exact finite extremizer (centered interval at output zero), a uniform all-finite-bank envelope `<7.692`, and Gaussian-limit sharp constant `3.530664...` with approach from below.

Hence a witness that pushes the true universal sharp constant above `3sqrt(2)` cannot be explained merely by an arbitrary three-variable rotation of equal spectral magnitudes, nor by arbitrary fragmentation of the single heavy coordinate in the one-heavy majority-sign bank family. The still-serious witness mechanisms are non-collinear multi-heavy physical rows, coupled spectral tails sharing original coordinates, unequal spectral magnitudes, or finite/mesoscopic structures outside these closed stress classes.

## 8. Relation to older three-variable theorem

The older source-valid product theorem

`qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`

proves for every invertible symmetric physical `3x3` block `B`

\[
\|p\|_\infty\le(2\pi+3\sqrt3)/\sigma_{\min}(B).
\]

The present theorem is a genuine specialization/improvement, not a duplicate: when `B^2=alpha^2 I` and the signature is indefinite, the exact bounded-ball cone geometry replaces the near constant `2pi r` by `pi sqrt2 r`, and optimization improves the constant from `11.4793377...` to `9.6095571...`.

Neither theorem is the unrestricted QFORM result.

## 9. Source pins

* Designated partner actually applied: `yspennstate/math-open-problems@189fc052089ae2d3237bc0865b290b01b26a6513`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T031047Z-account02-B17-QFORM-r11/REPORT.md`.
* Partner weighted Edgeworth source note: `yspennstate/math-open-problems@66ff43d64083414ef8e64f5702e3e4f085a9f877`.
* Sharp dependent-square/diffuse rank-two input: `yspennstate/math-open-problems@a80bb254a3a1e2883cbfabdf03b53919d6621990`; expanded source `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260922T142626Z-account03-B01-qform-r12/REPORT.md`.
* Older arbitrary invertible physical-three-block theorem: `qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.
* Target-level diffuse lower-bound / first-correction source: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T123638Z-account01-B17-qform-diffuse-edgeworth-v1/REPORT.md`.

No novelty or publication-priority claim is made. Full QFORM remains open.
