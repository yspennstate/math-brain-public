# fleet01/B10 — rank-three coupled case: zero-diagonal triple closure and one-heavy conditional-diffuse reduction

**Run:** `20260922T131954Z-fleet01-B10-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Rank-three coupled case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target, corrections, and conditional end-to-end route

The rank-three target in this workstream is: let `X_1,...,X_n` be independent real variables with densities bounded by one, and let

`A=U Lambda U^T`, `U^T U=I_3`,

where `Lambda` is real symmetric invertible and every eigenvalue of `Lambda` has modulus at least one. Prove a universal bound on the density of `Q=X^T A X`, with arbitrary orientation of `U` in the physical coordinates. No independence is assumed after rotating to spectral coordinates.

Fresh owner/control state was first read at `yspennstate/math-research-brain@7fca83478b59ed0358b20da77d877ddcc4f285a8` and refreshed immediately before publication at `88b88607b44d523117cc6886ed608739c92bdd2f`; the owner revision is unchanged. The live corrections used here include the failure of law-uniform pointwise quadratic oscillatory decay, the failure of conditional density caps to replace genuine independence in the heavy-isotropic normal form, and the new failure of a uniformly good local principal-block/cross-rank dichotomy. Accordingly, no pointwise van-der-Corput claim, no post-rotation independence, and no selection of one uniformly good physical minor is used.

The strongest current assembly read for context is fleet03/B19's `QFORM-TWOLEVEL-MIXED-LEVERAGE-AGGREGATION-v1` report. It leaves near-isotropic high-leverage pivots and second-level localization as the principal rank-three obstruction. This run attacks that first near-isotropic interface by two distinct mechanisms.

A compact conditional route is now:

1. diffuse three-frame (`max_i ||u_i||^2<=1/2`) is already paid by the Fourier--Brascamp--Lieb theorem;
2. a nonisotropic heavy pivot with diffuse rank-two Schur residual is already paid by the existing Schur/L^3 square-smoothing results;
3. an exactly isotropic physical pivot `A_ii=0` is now paid whenever one uses any *specified* nonsingular physical triple containing it, with an exact determinant-only constant proved below and with no triangular-zero assumption;
4. more generally, after conditioning one heavy physical coordinate, if the correctly whitened residual rank-three frame is diffuse, the arbitrary coupled remainder is paid by the separable-phase diffuse theorem, again without assuming the leakage is independent of the transverse pair;
5. what remains is genuinely global aggregation: near-isotropic heavy pivots for which the whitened residual frame is itself localized and all usable physical triples are individually too small. The latest correction shows that one cannot close this by demanding a uniformly nondegenerate principal block.

The first essential missing implication is therefore the product-preserving aggregation of that last nested-localization state, before reciprocal local minors or pivots are paid.

## 2. Named partner result actually applied

The required partner is `fleet02/B10`. Its canonical report is

`yspennstate/math-open-problems@11c9ae19edfd07e3a0bd4053a910667c20e721ab`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T130225Z-b10-qform-r11/REPORT.md`.

The exact theorem used below is its scaled dependent-pair hyperbolic-square lemma: if `W` is independent of a possibly dependent pair `(Y,Z)`,

`||p_W||_infinity<=K`, `||p_(Y,Z)||_infinity<=H`,

then for nonzero `a,b` and arbitrary measurable `F,theta`,

`T=2aWY+F(Y)+b(Z+theta(Y))^2`

has

`||p_T||_infinity <= 3*2^(2/3) H^(2/3) K^(2/3) |a|^(-2/3)|b|^(-1/3)`.   (2.1)

The same partner report proves that replacing independence of `W` by only a conditional density cap is false; that correction is respected below.

## 3. New theorem: every nonsingular physical triple with one zero diagonal entry is paid

### Theorem 3.1 — `QFORM-ZERO-DIAGONAL-TRIPLE-v1`

Let `S={i,j,k}` be three original physical coordinates. Suppose the principal matrix

`B=A_{S,S}`

is invertible and, after relabeling within `S`, `B_ii=0`. The entries of `A` outside this principal block and all couplings to outside coordinates may be arbitrary. Then `Q=X^TAX` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= 3*2^(2/3) |det B|^(-1/3). )`               (3.1)

No sign condition is required. In particular, repeated eigenvalues elsewhere and an indefinite `B` cause no degeneration in this statement.

### Proof

Condition on every coordinate outside `S`. The conditional law of the three coordinates in `S` remains a product of their original densities, each bounded by one. The conditional quadratic is

`q(x)=x^T B x+2 ell^T x+c0`,

where `ell` and `c0` depend on the conditioned outside variables. The desired bound will be uniform in them.

Write, with `x=X_i` and `y=(X_j,X_k)^T`,

`B=[[0,v^T],[v,C]]`,

where `v in R^2`. Invertibility of `B` forces `v!=0`. Put `r=|v|`. Choose an orthogonal `2 x 2` matrix `R` whose first column is `v/r`, and write

`(u,w)^T=R^T y`.

Although `u,w` need not be independent, their **joint** density is at most one: the original pair has joint density `f_j f_k<=1`, and an orthogonal change of variables has Jacobian one. The variable `x` remains independent of the whole pair `(u,w)`.

In these coordinates the quadratic matrix is

`B'=[[0,r,0],[r,a,d],[0,d,b]]`                                      (3.2)

for real `a,d,b`. Expanding the determinant gives the exact identity

`det B = det B' = -r^2 b`.                                           (3.3)

Thus `b!=0`.

The conditioned linear term may contain `l_x x`. Translate `u` by the constant `l_x/(2r)`. This absorbs `l_x x` into the term `2rxu`; translation preserves the joint density bound of `(u,w)`. The remaining expression has the form

`2 r x u + a u^2+2d u w+b w^2+l_u u+l_w w+const`.

Since `b!=0`, complete the square in `w`:

`2 r x u + F(u) + b ( w + theta(u) )^2 + const`,                    (3.4)

where `F` is a quadratic polynomial and `theta` is affine. Apply the partner bound (2.1) with

`W=x`, `Y=u`, `Z=w`, `K=1`, `H=1`, `a_partner=r`, `b_partner=b`.

This gives, uniformly in the conditioned outside variables,

`||p_(Q | X_{S^c})||_infinity
 <=3*2^(2/3) r^(-2/3)|b|^(-1/3)
 =3*2^(2/3)|det B|^(-1/3)`

by (3.3). Averaging the conditional densities proves (3.1). QED.

### What is new relative to the earlier triangular hyperbolic-square branch

The earlier physical-triple theorem required a coordinate pattern such as `A_ii=0`, `A_ik=0`, `A_ij!=0`, `A_kk!=0`. Theorem 3.1 removes the extra zero `A_ik=0`: one orthogonally rotates only the *other two physical coordinates as a joint pair*. Their independence is not retained or needed; only their exact joint-density cap is used, while `X_i` stays genuinely independent of that pair. The determinant identity then exactly pays the resulting coefficients.

### Rank-three isotropic-pivot consequence

For rank exactly three, `A=U Lambda U^T`, suppose physical row `u_i` is nonzero and isotropic:

`A_ii=u_i^T Lambda u_i=0`.

Because the rows of `U` span `R^3`, there exist `j,k` for which `u_i,u_j,u_k` are linearly independent. For every such triple,

`det A_{S,S}=det Lambda * det(U_S)^2 !=0`.                            (3.5)

Therefore Theorem 3.1 always supplies a finite bound for some triple containing the isotropic pivot. Quantitatively,

`||p_Q||_infinity
 <=3*2^(2/3)|det Lambda|^(-1/3)|det U_S|^(-2/3)`.                    (3.6)

This is intentionally **not** promoted to a universal rank-three theorem: the current correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` exhibits target-valid families in which every fixed nonsingular physical `3 x 3` principal block can have its smallest singular value tend to zero. Equation (3.6) is therefore a local closure lemma whose reciprocal minor still has to be aggregated before payment.

## 4. New reduction: condition a heavy row, whiten exactly, and retain arbitrary coupled leakage

The next lemma uses the complete source-reported `QFORM-DIFFUSE-SEPARABLE-PHASE-v1` theorem at

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`,

`proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

That theorem is currently a supplied supporting proof pending its requested independent reviews, so the present result is explicitly conditional on that dependency's validity. Its relevant scope is: for an orthonormal `r=3` frame with every row leverage at most `1/2`, an invertible spectral matrix `Gamma`, and arbitrary coordinate-separable measurable potentials, the resulting quadratic has

`||p||_infinity <=3e |det Gamma|^(-1/3)`,                             (4.1)

with a bounded continuous density.

### Theorem 4.1 — `QFORM-ONE-HEAVY-CONDITIONAL-DIFFUSE-v1`

Let `A=U Lambda U^T` have rank exactly three, with `U^TU=I_3`. Fix an original coordinate `i` with leverage

`c=||u_i||^2<1`.

Set

`G=I_3-u_i u_i^T`,

and for every `j!=i` define the whitened residual leverage

`ell_j = u_j^T G^(-1) u_j`.                                          (4.2)

If

`max_{j!=i} ell_j <=1/2`,                                             (4.3)

then, conditional on the source theorem (4.1), `Q=X^TAX` has a bounded continuous density and

`boxed( ||p_Q||_infinity <=3e [(1-c)|det Lambda|]^(-1/3). )`          (4.4)

In the owner rank-three normalization `|det Lambda|>=1`, if in addition `c<=7/8`, this gives the explicit universal branch bound

`||p_Q||_infinity <=6e <16.31`.                                      (4.5)

### Proof

Delete row `i` of `U` and call the remaining matrix `U_-`. Since `U^TU=I_3`,

`U_-^T U_-=I_3-u_i u_i^T=G`.

Because `c<1`, `G` is positive definite. Define

`V=U_- G^(-1/2)`.

Then `V^T V=I_3`, and the squared norm of its `j`th row is exactly `ell_j` in (4.2). Thus (4.3) is precisely the leverage hypothesis in the diffuse separable-phase theorem.

Condition now on `X_i=x`. Since

`U^T X = u_i x + G^(1/2)V^T X_-`,

we have the exact identity

`Q = (V^T X_-)^T Gamma (V^T X_-)
     + 2x u_i^T Lambda G^(1/2)V^T X_- + x^2 u_i^T Lambda u_i`,        (4.6)

where

`Gamma=G^(1/2) Lambda G^(1/2)`.                                      (4.7)

For fixed `x`, the second term in (4.6) is a sum of one-coordinate linear potentials in the still-independent original variables `X_j`, `j!=i`; no rotated-coordinate independence is asserted. Therefore (4.1) applies uniformly in `x`.

The determinant is exact. By the matrix determinant lemma,

`det G=1-u_i^T u_i=1-c`,

so

`|det Gamma|=(1-c)|det Lambda|`.                                     (4.8)

Equations (4.1) and (4.8) yield the conditional bound (4.4), independent of `x`. Averaging gives the same `L^infinity` bound unconditionally. The source theorem's characteristic-function majorant is uniform in the separable potentials, hence also uniform in `x`; averaging that integrable majorant yields the stated continuous-density conclusion in this branch. QED, conditional on the source theorem (4.1).

### Relation to the partner's heavy-isotropic obstruction

Take the partner's heavy isotropic normal form, with `u_i=sqrt(c)e`, `delta=1-c`, and residual rows

`u_j=s_j e+y_j f+z_j g`.

Then

`G=diag(delta,1,1)`

in the spectral basis `(e,f,g)`, and (4.2) becomes exactly

`ell_j=s_j^2/delta+y_j^2+z_j^2`.                                    (4.9)

Thus Theorem 4.1 closes arbitrary **correlated** leakage whenever the whitened residual frame is diffuse; it never replaces the leakage by a conditional-density surrogate. In this branch the partner's nonlinear cancellation falsifier is irrelevant because the full original product representation is retained all the way through (4.6).

If `c=1`, the partner's isotropic state has `s_j=0` for all residual rows, so its leakage `T=sum s_jX_j` vanishes identically and the partner's genuinely-independent-leakage theorem applies directly. Hence the new residual obstruction is not the endpoint `c=1` itself but nested localization as `c` approaches one.

## 5. First unpaid implication after the two new steps

The rank-three hard branch can now be stated more sharply.

Choose a leverage-heavy physical row. The already proved diffuse/Schur mechanisms and Theorem 4.1 dispose of the case in which whitening after that row produces a diffuse residual three-frame. If the heavy pivot is exactly isotropic, Theorem 3.1 also pays any specified nonsingular physical triple without needing a triangular zero pattern.

Therefore a surviving near-isotropic branch must exhibit **nested localization**:

`max_{j!=i} u_j^T (I-u_i u_i^T)^(-1) u_j >1/2`,                     (5.1)

while any attempt to select one physical triple may incur an arbitrarily small determinant. The new correction shows that this is a genuine global issue, not a missing local-block lemma.

A precise next implication is:

**`QFORM-NESTED-HEAVY-BANK-AGGREGATION-v1` — OPEN.** In the rank-three indefinite case with a near-isotropic leverage-heavy row and (5.1), use the original product coordinates and the exact frame identities to aggregate the distributed off-diagonal/volume resource into a paid hyperbolic-square or two-level square-smoothing mechanism *before* any reciprocal principal-minor or scalar-pivot factor is introduced.

The fleet03/B19 identity

`sum_{j!=i} A_ij^2 = |Lambda u_i|^2 - A_ii^2`

shows why this is plausible: for a near-isotropic heavy row the total cross energy is large. But neither this run nor the current team assembly converts that aggregate energy into a dimension-free paid bank in complete generality. Theorem 3.1 cannot simply be maximized over triples because the largest physical determinant can decay with dimension. No such step is claimed.

## 6. Sanity checks and edge cases

- Theorem 3.1 is sign-free. The identity `det[[0,r,0],[r,a,d],[0,d,b]]=-r^2b` shows that its completed-square coefficient can never vanish when the physical triple is nonsingular.
- The orthogonal rotation in Theorem 3.1 is confined to the two-variable **joint density**; their independence is explicitly discarded. Independence is used only between `X_i` and that pair, which is preserved because `X_i` is a different original coordinate.
- Conditioning outside a physical triple changes only linear terms and constants, which were retained explicitly. Thus arbitrary outside couplings are allowed.
- Theorem 4.1 permits arbitrary signs and repeated eigenvalues of `Lambda`; only invertibility and the determinant enter.
- Theorem 4.1 does not silently assume moments, compact support, connected support, log-concavity, or smooth input densities.
- The essential-density conclusion and continuous-density conclusion are separated: Theorem 3.1 establishes only the former from the partner theorem as currently stated; Theorem 4.1 inherits continuity from the uniform integrable characteristic-function bound in its cited source theorem.
- A symbolic determinant check of (3.3) and random real coordinate rotations was performed locally; this is only an algebra sanity check, not a proof substitute.

## 7. Status and provenance

**Proved in this run:** `QFORM-ZERO-DIAGONAL-TRIPLE-v1`, conditional-density bound (3.1), using the named completed partner `fleet02/B10` result in the displayed inequality.

**Derived in this run conditional on a supplied supporting theorem pending review:** `QFORM-ONE-HEAVY-CONDITIONAL-DIFFUSE-v1`, equations (4.2)--(4.5), from `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`.

**Not proved:** `QFORM-NESTED-HEAVY-BANK-AGGREGATION-v1`; the arbitrary rank-three theorem; the full owner conjecture with additional spectral directions.

No public release, remote workflow, paid model/API, email, scheduler mutation, or permission change is part of this report. The changed-file allowlist for this scientific commit contains only this report, and a manual scope/pattern review found no credentials, scheduler identifiers, machine paths, or unrelated private material.
