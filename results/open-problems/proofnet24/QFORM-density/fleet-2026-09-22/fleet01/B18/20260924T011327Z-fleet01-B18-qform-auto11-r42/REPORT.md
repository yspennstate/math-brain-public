SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-24T01:13:27Z.
attacking: literature-to-proof transfer for a two-sided anchor: use primary product-marginal density bounds to pay any genuinely two-dimensional cross coefficient map, then splice the newest fleet02/B18 one-sided-anchor theorem on its exact branch.

# fleet01/B18 r42 — rotating-anchor transfer and a punctured-boundary diagnosis

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **PROVED SUPPORTING TARGET-VALID FAMILY CLOSURE + DESIGNATED PARTNER APPLIED; FULL QFORM OPEN / NOT PROVED.**
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh scope and corrections

The owner target is unchanged: independent original coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. The goal is one universal essential-density bound; continuity is tracked separately.

This report uses no post-rotation independence, no arbitrary-joint coarea estimate, no conditional-density-cap-as-independence substitution, no law-uniform pointwise Fresnel decay, no positive moment of a worst conditional projection-density cap, no fixed-good-minor assertion, and no deletion of a small nonzero quadratic or cross coefficient.

## 2. Primary literature transfer, with exact hypotheses

The primary source used is G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949, Theorem 1.1. If an `n`-dimensional probability density is a genuine product `prod_i f_i(x_i)` and each `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. In particular every normalized scalar projection has density at most `sqrt(2)` and every two-dimensional orthogonal projection has joint density at most `2`.

There are no moment, iid, bounded-support, log-concavity, centering, symmetry, connected-support, or smoothness hypotheses. I use this only on linear projections of genuine original-coordinate product banks; the projected coordinates themselves are never declared independent.

For scope comparison, Herry--Malicet--Poly, arXiv:2303.09488, study regularity of quadratic forms for iid inputs whose common law is representable as a sufficiently smooth function of a Gaussian field. That does not match the owner's arbitrary rough non-iid cap-one quantifiers, so it cannot be imported as the unrestricted theorem here.

I also found that the exact two-singular-direction transfer below has already been proved inside the fleet, most recently as fleet03/B18 `QFORM-ONE-SIDED-CROSS-NEGATIVE-MOMENT-v1`, scientific commit `a2cf029c5c935d6eadf4216c073911fc8dc404ac`. I therefore make **no novelty claim** for that theorem. I rederive only the exact specialization needed here so that the new implication is source-valid and auditable.

## 3. Source-valid cross-bank receiver

Let the ORIGINAL coordinates be split into two disjoint product banks `X in R^m`, `Z in R^k`, with all scalar density caps at most one. Let `D` be an `m x k` real matrix with two positive singular values `d1>=d2>0`, let `alpha in R^m`, and let `G(Z)` be arbitrary measurable. Define

`T = 2 X^T D Z + alpha^T X + G(Z)`.

Then

`boxed: ||p_T||infinity <= 2 sqrt(pi) / sqrt(d1 d2).`          (3.1)

Proof. Conditional on `Z=z`, the coefficient of the original `X` bank is `c(z)=2Dz+alpha`. LPP in one dimension gives

`||p_(T|Z=z)||infinity <= sqrt(2)/||c(z)||`                    (3.2)

for a.e. `z`. Project `c(z)` onto the top two left singular directions of `D`. If `V_2^T Z` denotes the corresponding two-dimensional right-singular projection, LPP gives its joint density cap `2`. After the affine map `w=2 diag(d1,d2)V_2^T z+shift`, the two-dimensional density cap is

`H <= 2/(4 d1 d2)=1/(2 d1 d2)`.                               (3.3)

For any planar probability density bounded by `H`, the radial bathtub principle gives

`E |W|^{-1} <= 2 sqrt(pi H)`.                                  (3.4)

Indeed the maximizer is density `H` on the centered disk of area `1/H`. Hence

`E ||c(Z)||^{-1} <= sqrt(2 pi/(d1 d2))`,                       (3.5)

and averaging (3.2) yields (3.1). This proof never conditions a rotated coordinate and never promotes the two-dimensional marginal cap to independence.

Ambient quadratic corollary: if original coordinates split as `I sqcup J sqcup K`, `A_II=0`, and `D=A_{I,J}`, then after conditioning only `X_K`, all self-curvature on `J`, all `J-K`/`I-K` couplings, and all outside spectrum become part of `G` and `alpha`. Thus (3.1) applies with the top two singular values of the physical cross block `D`, uniformly in the conditioning.

Continuity is **not** asserted by this negative-moment proof.

## 4. New target-valid rotating-anchor family

Let `X in R^m`, `Y in R^n`, and `W` be disjoint ORIGINAL-coordinate product sources. Choose orthonormal `u,r in R^m` and orthonormal `v,s in R^n`. Put

`U=u^T X,  R=r^T X,  V=v^T Y,  S=s^T Y`.

For `0<delta<=1/64` and `0<=rho<=1`, write `q=sqrt(1-rho^2)` and define

`Q_(delta,rho) = 2 delta^(-1/2) U V + 2 W (rho R + q S) + delta W^2`.  (4.1)

No independence is assumed between `U,R` or between `V,S`; each pair is merely an orthogonal projection of its original product bank.

### Spectrum

The vectors `u,v` span one coefficient-space block and the unit vector `rho r+q s`, together with `W`, spans an orthogonal second block. Therefore the nonzero spectrum is exactly

`+delta^(-1/2), -delta^(-1/2),`

`lambda_+=(delta+sqrt(delta^2+4))/2,`

`lambda_-=(delta-sqrt(delta^2+4))/2`.                           (4.2)

Thus `lambda_+>1`, `|lambda_-|<1`, and because `delta^(-1/2)>=8`, (4.1) has exactly **three** eigenvalues of modulus at least one. It is a literal owner-target family.

### Pay from the X side

The `X-X` physical block is zero. Treat `(Y,W)` as the opposite original product bank. The cross map is

`D_X = [ delta^(-1/2) u v^T , rho r ]`.

Because `u perp r`, its two nonzero singular values are `delta^(-1/2)` and `rho`. Hence for `rho>0`, (3.1) gives

`||p_Q||infinity <= 2 sqrt(pi) delta^(1/4) rho^(-1/2)`.          (4.3)

### Pay from the Y side

The `Y-Y` physical block is also zero. Reverse the roles. The cross map from `Y` to `(X,W)` is

`D_Y = [ delta^(-1/2) v u^T , q s ]`,

with nonzero singular values `delta^(-1/2)` and `q`. For `q>0`,

`||p_Q||infinity <= 2 sqrt(pi) delta^(1/4) q^(-1/2)`.            (4.4)

Choose the better of (4.3)--(4.4). Since

`max{rho,q} >= 1/sqrt(2)`,

we obtain the whole-family estimate

`boxed: ||p_(Q_(delta,rho))||infinity`
`       <= 2 sqrt(pi) 2^(1/4) delta^(1/4)`
`       <= 1.490451.`                                           (4.5)

This is uniform in `m,n,rho`, and every admissible product input law. The value `1.490451` is the endpoint at `delta=1/64`; the bound improves as `delta downarrow0`.

This closes a concrete two-sided-anchor stress interpolation without ever rotating the random source: whenever the anchor moves from the Y bank into the X bank, one pays from whichever zero-self-curvature original bank carries the larger transverse anchor component.

## 5. Designated fleet02/B18 theorem applied to an actual inequality

The newest completed designated-partner result is fleet02/B18 `QFORM-ONE-SIDED-ANCHOR-CROSS-SQUARE-LP-v1`, scientific commit `39fec6de415da54a5947972780a6aa76816bdca0` (deterministic check follow-up `725262eae14b62acb3b2b41365e3d23f5a8d68e0`). It considers disjoint original-coordinate banks `X,Y,W` and

`T = X^T M Y + alpha^T X + G(Y) + a W^2 + h(Y)W + c`,

where the anchor `W` may couple arbitrarily into the `Y` bank but not into `X`. At `q=3/2` it proves

`||p_T||infinity <= 12*2^(1/3) (|a| ||M||op^2)^(-1/3)`,         (5.1)

and its physical normalization for `2X^T C Y` is

`boxed: ||p_Q||infinity <= (12/2^(1/3)) (|a| ||C||op^2)^(-1/3).` (5.2)

Apply (5.2) to the literal endpoint `rho=0` of (4.1). There `a=delta`, `C=delta^(-1/2)u v^T`, and therefore

`|a| ||C||op^2 = delta * delta^(-1)=1`.

The partner theorem gives the actual whole-line inequality

`boxed: ||p_(Q_(delta,0))||infinity <= 12/2^(1/3)`
`       = 9.524406311809196...`.                                (5.3)

This application is exact: the term `2WS` is precisely the allowed one-sided `h(Y)W`, and no coefficient is deleted. The source-transfer bound (4.4) is sharper on this special zero-`Y-Y` endpoint, but (5.3) remains important because the partner theorem tolerates **arbitrary Y-bank curvature**, where reversing sides is no longer available.

## 6. A curved-opposite-bank stress packet and the exact remaining collar

To make that distinction explicit, add one unit of curvature on the `S` direction:

`Q^curv_(delta,rho) = 2 delta^(-1/2) U V`
`                    + 2 W (rho R + q S) + delta W^2 + S^2`.    (6.1)

This is still a target family for every `rho`: the `U,V` block contributes eigenvalues `+/-delta^(-1/2)`, while the remaining `R,S,W` principal block has Rayleigh quotient one on the `S` vector, so its largest eigenvalue is at least one. Hence at least three eigenvalues have modulus at least one.

For every `rho>0`, the X-side cross map is unchanged, so

`||p_(Q^curv)||infinity <= 2 sqrt(pi) delta^(1/4) rho^(-1/2).`   (6.2)

In particular if `rho>=sqrt(delta)`,

`boxed: ||p_(Q^curv)||infinity <= 2 sqrt(pi)=3.5449077018...`.   (6.3)

At the exact endpoint `rho=0`, the designated partner theorem still allows the arbitrary `S^2` term inside `G(Y)` and gives

`boxed: ||p_(Q^curv_(delta,0))||infinity <= 9.524407.`           (6.4)

Thus the only portion of this explicit interpolation not paid by these two exact mechanisms is the **punctured near-one-sided collar**

`0 < rho < sqrt(delta)`.                                       (6.5)

The live corrections matter here: one may not infer the endpoint theorem for (6.5) merely by saying the extra `2 rho W R` edge is small, because arbitrary cap-one laws give no perturbative density continuity strong enough to justify deleting that random term. The next useful proof target is therefore a receiver uniform as a two-sided anchor edge tends to zero, while retaining the opposite-bank curvature exactly.

## 7. What is genuinely new in this run, and what is prior

The two-singular cross-bank theorem (3.1) is an exact prior fleet result; no novelty is claimed for it. The new contribution is the **literature-to-proof splice**: applying that source-valid theorem from both original zero-self banks closes the entire target-valid rotating-anchor family (4.1) uniformly in the anchor orientation, while the newest fleet02/B18 theorem closes the one-sided endpoint even after arbitrary opposite-bank curvature is restored. The curved family (6.1) then isolates the remaining failure as the strict small-nonzero two-sided collar (6.5), rather than a generic anchor obstruction.

I found no external primary theorem in the checked LPP and Herry--Malicet--Poly sources that states the full arbitrary-law, arbitrary-sign, arbitrary-dimension owner theorem. That is only a hypothesis/scope report, not a novelty claim.

## 8. Continuity

The main conclusions (4.5), (6.2)--(6.4) are essential-density bounds. I do **not** infer full continuity from the two-singular negative-moment argument. The designated partner theorem proves `C_0` continuity for its standalone one-sided form, including (5.3)/(6.4) at `rho=0`; if additional outside original coordinates are conditioned, I retain only the uniform essential bound unless a uniform integrable characteristic-function envelope is separately supplied.

## 9. Remaining full-target implication

Full QFORM remains OPEN. The bare condition `s_3(A)>=1` does not by itself force two literal zero-self original banks, nor a cross singular product bounded below. The next structural task is to route the general small-diagonal/overlap packet either to a two-sided-anchor receiver that stays uniform through the punctured collar (6.5), or to one of the already-paid ridge/grouped-cross/principal-core mechanisms, without dropping any small nonzero term or inventing independence after projection.
