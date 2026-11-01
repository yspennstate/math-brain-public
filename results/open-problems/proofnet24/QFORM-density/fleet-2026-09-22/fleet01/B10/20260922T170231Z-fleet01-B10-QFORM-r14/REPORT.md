# fleet01/B10 — exact same-ray cascade compression and the full null-ray endpoint

**Run:** `20260922T170231Z-fleet01-B10-QFORM-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Outcome:** `ESSENTIAL_STEP_APPLIED / TARGET_BRANCH_CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and fresh source state

The owner target remains the full arbitrary-law statement: independent real physical coordinates `X_i` with probability densities bounded by one, and a real symmetric matrix with at least three eigenvalues of modulus at least one; prove one universal bound on the density of `X^T A X`, or give a target-valid counterexample. Continuity is tracked separately.

This run began under owner revision `2026-09-22.7`; the prepublication refresh found revision `2026-09-22.8`. The target and B10 rank-three assignment are unchanged. The later owner note proposes a rank-three coarea/projection route, but the live correction set and the completed cone-trace counterexample show that a generic bounded 3D projected density by itself does **not** control an indefinite quadratic pushforward. The argument below therefore retains exact product provenance and never substitutes a generic projection cap for the needed independence.

The newest synthesis also supplies `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` at `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1`, path `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`: every arbitrary-orientation exact rank-two quadratic plus arbitrary affine term has a universal half-Riesz bound. Consequently the old small-Rayleigh debt **inside** a rank-two Schur remainder is no longer the B10 frontier; the hard exact-rank-three branch is the small/zero **outer** pivot and, in particular, the heavy isotropic overlap state.

### Completed inputs used at proof level

1. **Assigned partner fleet02/B10, r13.** Canonical source `yspennstate/math-open-problems@9a34dc516006d7eb417687b3d7d409f7dfaf33d9`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T154900Z-fleet02-B10-QFORM-r13/REPORT.md`. It proves the diffuse exact-rank-three branch `max_i ||u_i||^2<=1/2 => ||p_Q||_infinity<=3e`, gives the exact conditional-whitening formula, and constructs arbitrarily long zero-pivot heavy peeling chains on one isotropic spectral ray. Its chain has whitened leverage `2/3` at every nonterminal step and proves bounded-depth peeling false.
2. **Independent-scalar / dependent-pair hyperbolic-square smoothing.** fleet01/B11, `yspennstate/math-open-problems@aff1f42f4b68ea31eec27673e7d56b5370f6dec3`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/QFORM-B11-20260922T151340Z-r11/REPORT.md`. If `S` is independent of a pair `(V,W)`, `||p_S||_infinity<=M`, `||p_(V,W)||_infinity<=K`, then `2aSW+bV^2` has a bounded continuous density at most `6(MK)^(2/3)|a|^(-2/3)|b|^(-1/3)`.
3. **Weighted affine-fiber Brascamp--Lieb projection cap.** fleet02/B06, `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. A normalized one-dimensional product projection has density at most `sqrt(e)` and an isotropic two-dimensional product projection has joint density at most `e`.

Corrections explicitly respected include `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`, and `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`.

## 2. Compact conditional end-to-end architecture

Write an exact rank-three target as

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_j(Lambda)|>=1`,

and let `u_i` denote the physical rows of `U`.

The current exact-rank-three route is:

1. If `max_i ||u_i||^2<=1/2`, the assigned partner gives `||p_Q||_infinity<=3e`.
2. If a quantitatively nonzero physical diagonal pivot is available, the orientation-free rank-two affine half-Riesz theorem pays the full Schur remainder; the old residual-Rayleigh split is obsolete.
3. The hard state is therefore a heavy physical row close to the spectral null cone. The partner r13 result proves that repeated heavy-row deletion cannot be expected to terminate after any universal number of steps: an arbitrarily long chain can remain exactly isotropic and leverage `2/3` after every whitening.
4. The new result below shows that if such a chain really stays on **one spectral ray**, then the chain should never be peeled coordinate-by-coordinate. All coordinates on the ray compress exactly into one genuine product-linear bank. If that ray consumes its full Parseval mass, the entire remaining arbitrary transverse frame is paid with a continuous density bound `<=6e`, independent of the number of coordinates and without any transverse support separation.
5. A same-ray chain that has not yet consumed full mass has one and only one exact residual defect: a scalar leakage projection of coefficient norm `sqrt(rho)`, where `rho` is the remaining ray mass. After `k` consecutive whitened leverage-`>1/2` steps, `rho<2^(-k)`. Smallness of `rho` cannot be used perturbatively because the input supports have no moment or diameter control; the live corrections forbid that shortcut.

Thus the first unpaid same-ray implication becomes a product-provenance leakage theorem uniform for `0<rho<1/2`; angular departure from the ray is a separate branch that should create cross-volume/shear payment.

## 3. Exact same-ray bank compression

### Lemma 3.1 — `QFORM-COLLINEAR-SPECTRAL-BANK-COMPRESSION-v1`

Let `I` be a set of physical coordinates whose spectral rows are all collinear:

`u_i=alpha_i v`, `i in I`,

where `||v||_2=1`. Put

`w=sum_(i in I) alpha_i^2`.

For `w>0` define the normalized bank variable

`S_I = w^(-1/2) sum_(i in I) alpha_i X_i`.

Then:

1. `S_I` is independent of all physical coordinates in `I^c`;
2. `S_I` has a density bounded by `sqrt(e)`;
3. if `Z_C=sum_(j notin I) u_j X_j`, then exactly

`Q = w (v^T Lambda v) S_I^2
     +2 sqrt(w) S_I v^T Lambda Z_C
     +Z_C^T Lambda Z_C`.                                            (3.1)

No approximation and no post-rotation independence is used.

### Proof

The independence statement is immediate because the bank and its complement use disjoint original-coordinate sets. The coefficient vector `(alpha_i/sqrt(w))_(i in I)` has Euclidean norm one, so the completed one-dimensional product-projection theorem gives the density cap `sqrt(e)`. Finally

`sum_i u_i X_i = sqrt(w) v S_I + Z_C`,

and expanding the spectral quadratic gives (3.1). `QED`

This lemma is the exact operation missing from bounded-depth peeling: a long collinear cascade is a single independent bank, not a sequence of unrelated local pivots.

## 4. Exact whitening recurrence for a same-ray cascade

Suppose some rows on the unit ray `v` have already been conditioned/deleted and their total original frame mass is

`s=sum alpha_i^2<1`.

The residual frame Gram matrix is

`G_s=I_3-s vv^T`.                                                     (4.1)

Whitening the residual rows by `G_s^(-1/2)` restores a Parseval frame. For the next original row `u=alpha v`, its whitened leverage is exactly

`ell_tilde = alpha^2 v^T G_s^(-1)v
           = alpha^2/(1-s)`.                                        (4.2)

Consequently, if this next same-ray row is heavy after whitening,

`ell_tilde>1/2`,

then

`alpha^2>(1-s)/2`

and the still-unconsumed mass on that ray obeys

`1-s-alpha^2 < (1-s)/2`.                                             (4.3)

After `k` consecutive same-ray whitened-heavy steps,

`rho_k := 1-s_k < 2^(-k)`.                                          (4.4)

More generally, a uniform lower bound `ell_tilde>=gamma` forces `rho_k<=(1-gamma)^k`.

The partner r13 construction is the exact `gamma=2/3` model: its weights satisfy

`alpha_k^2=(2/3) rho_(k-1)`,

so `rho_k=rho_(k-1)/3`, and the terminal row consumes the remaining mass. This recovers its geometric weights and explains structurally why arbitrarily long peeling is possible: the rows are simply finer pieces of one scalar bank.

The null property is stable under this whitening. If `v^T Lambda v=0`, then for the whitened spectral matrix `Lambda_tilde=G_s^(1/2)Lambda G_s^(1/2)` and whitened ray `v_tilde=G_s^(-1/2)v`,

`v_tilde^T Lambda_tilde v_tilde=v^T Lambda v=0`.                     (4.5)

Thus no number of same-ray whitening steps can manufacture a nonzero pivot from an exactly null ray.

## 5. Main theorem: a full null-ray bank closes with arbitrary transverse orientation

### Theorem 5.1 — `QFORM-FULL-NULL-RAY-BANK-v1`

Assume the exact-rank-three target `A=U Lambda U^T`, `U^T U=I_3`, `|lambda_j|>=1`. Suppose a set `I` of physical rows is contained in one unit spectral ray,

`u_i=alpha_i v`, `i in I`,

and satisfies the two exact conditions

`sum_(i in I) alpha_i^2=1`,
`v^T Lambda v=0`.                                                     (5.1)

No restriction is imposed on the orientation, support pattern, or number of rows in `I^c`.

Then `Q=X^TAX` has a bounded **continuous** density and

`boxed: ||p_Q||_infinity <= 6e |det Lambda|^(-1/3) <= 6e <16.310`.    (5.2)

### Step 1: the complement is exactly a two-dimensional Parseval frame

Because `U^T U=I_3` and the bank in (5.1) contributes `vv^T`,

`sum_(j notin I) u_j u_j^T=I_3-vv^T`.                               (5.3)

In particular

`sum_(j notin I)(u_j dot v)^2=0`,

so every residual row lies in the Euclidean plane `v^perp`.

Choose an orthonormal basis matrix `E` for `v^perp`. Write

`Z_C=E Y`, `Y in R^2`.

The two coefficient columns producing `Y` are orthonormal by (5.3). Hence the completed two-dimensional product-projection theorem gives

`||p_Y||_infinity<=e`.                                               (5.4)

By Lemma 3.1, the normalized bank scalar

`S=sum_(i in I) alpha_i X_i`

is independent of `Y` and has density at most `sqrt(e)`.

### Step 2: exact Witt reduction without declaring the transverse coordinates independent

In the orthogonal spectral basis `(v,E)`, write

`M=[[0,c^T],[c,H]]=O^T Lambda O`.                                    (5.5)

Because `Lambda` is invertible and `v^T Lambda v=0`, `c!=0`. Rotate only the **two-dimensional joint transverse variable** so that

`c=(r,0)`, `r>0`.

This rotation preserves the joint density cap (5.4). Write the resulting matrix as

`M=[[0,r,0],[r,h11,h12],[0,h12,h22]]`.                               (5.6)

Since

`det M=-r^2 h22=det Lambda`,                                         (5.7)

we have `h22!=0`.

Now shear the transverse pair by

`W=Y_1`,
`V=Y_2+(h12/h22)Y_1`.                                                (5.8)

The shear has determinant one, so `(V,W)` still has joint density at most `e`; no independence between `V` and `W` is asserted. The quadratic becomes exactly

`Q=2r S W + kappa W^2 + h22 V^2`,                                   (5.9)

where `kappa=h11-h12^2/h22`.

### Step 3: spend the independent-bank hyperbolic-square theorem

The fleet01/B11 smoothing proof remains valid with an additional arbitrary measurable output translation depending on `W`: condition on `W=w`; the term `kappa w^2` merely translates the conditional output and changes none of the density estimates. Therefore, for

`Y0=2aSW+h(W)+bV^2`,

with `S` independent of `(V,W)`, density caps `M0,K0`, the same proof gives

`||p_Y0||_infinity <=6(M0 K0)^(2/3)|a|^(-2/3)|b|^(-1/3)`.           (5.10)

Apply (5.10) to (5.9) with

`M0=sqrt(e)`, `K0=e`, `a=r`, `b=h22`.

Then

`||p_Q||_infinity
 <=6 e |r|^(-2/3)|h22|^(-1/3)
 =6 e |det Lambda|^(-1/3)
 <=6e`,                                                             (5.11)

where (5.7) gives the exact determinant cancellation. The same smoothing theorem gives continuity and vanishing at infinity. `QED`

### What is new in this endpoint

The earlier `c=1` null-heavy theorem was stated for a **single physical row** carrying the null direction. The present theorem permits an arbitrary number of original coordinates on that ray, with arbitrary cap-one laws and arbitrary coefficient fragmentation. They are compressed before any reciprocal local minor is paid. The complement may be a completely dense two-dimensional Parseval frame; no three-bank support separation is required.

## 6. Direct application to the assigned partner's unbounded-peeling family

The assigned partner r13 constructs, for every `K`, a target matrix with spectral form

`Lambda_0=[[0,1,0],[1,0,0],[0,0,1]]`,

and `K` physical rows on the null ray `v=e_1` having squared lengths

`w_k=2/3^k` for `k<K`,
`w_K=1/3^(K-1)`,

so

`sum_(k=1)^K w_k=1`.                                                 (6.1)

Its key completed result is that the successive whitened leverages are exactly `2/3` until the terminal leverage-one row, while every pivot on this ray is zero. Theorem 5.1 applies to the **entire partner family at once**, with no peeling and no use of its special transverse support pattern:

`||p_Q||_infinity <=6e<16.310`,                                     (6.2)

and the density is continuous.

For the partner's particular disjoint transverse banks, its separately cited three-bank theorem gives the sharper numerical bound `8sqrt(2)<11.314`. The point of (6.2) is different and stronger structurally: the same conclusion survives if those transverse rows are replaced by **any** residual frame satisfying Parseval, because full mass on the null ray forces the residual frame into `v^perp` and only a bounded joint two-dimensional density is needed.

The partner r12 flat-bank family is covered for the same reason: its heavy `e_+` coordinate plus the `m` additional `e_+` coordinates together carry total squared ray mass one. Thus two distinct partner constructions previously used to show local-minor failure are instances of one paid endpoint.

## 7. The exact residual when the null-ray bank has mass `w<1`

The same compression gives a precise normal form for the remaining open branch.

Let the total same-ray mass be `w in (0,1)` and put

`rho=1-w`.                                                           (7.1)

Decompose every complementary spectral row in an orthogonal basis `(v,E)` as

`u_j=s_j v+E y_j`.

The Parseval identities are exactly

`sum s_j^2=rho`,
`sum y_j y_j^T=I_2`,
`sum s_j y_j^T=0`.                                                   (7.2)

Thus the residual scalar coefficient vector has norm `sqrt(rho)` and is orthogonal, in coefficient space, to both transverse coefficient columns. Define

`T=sum s_j X_j`,
`Y=(Y_1,Y_2)=sum y_j X_j`.

The bank scalar `S` from `I` is genuinely independent of the entire residual triple `(T,Y_1,Y_2)`, but `T` is generally dependent on `(Y_1,Y_2)` because they use the same original coordinates.

Applying the same spectral rotation and unit-determinant shear as in Section 5 yields

`boxed:
Q=2r sqrt(w) S W +2r T W +kappa W^2+h22 V^2,}`                     (7.3)

with

`r^2 |h22|=|det Lambda|>=1`.                                         (7.4)

Equation (7.3) isolates the entire same-ray debt in the single correlated leakage term `2rTW`. At `rho=0`, `T=0` and Theorem 5.1 closes the endpoint. After `k` consecutive same-ray whitened-heavy rows, Section 4 gives `rho<2^(-k)`.

This does **not** permit a perturbative argument: bounded density inputs have no moment or diameter bound, so a coefficient vector of tiny Euclidean norm may still generate an arbitrarily large-valued random variable. Nor may one replace `sqrt(w)S+T` by a conditionally bounded scalar and invoke the independent theorem: the assigned partner's exact `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` counterexample proves that bounded `(V,W)` density plus a bounded conditional scalar density can still leave a logarithmic singularity.

The correct next theorem must use the stronger product-origin identities (7.2), not merely low-dimensional marginal caps.

## 8. First unpaid implication after this run

The same-ray frontier is now the following precise statement.

**`QFORM-NULL-RAY-PRODUCT-LEAKAGE-v1`.** Under (7.2)--(7.4), with `S` generated by a disjoint original-coordinate bank, prove a universal density bound for

`2r sqrt(w) S W +2r T W +kappa W^2+h22 V^2`

uniformly for every `w in [1/2,1)` and every cap-one product source, using the orthogonality/projection provenance in (7.2). The proof must remain uniform as `rho=1-w downarrow0`; small coefficient norm alone is not admissible.

A complementary escape is a **ray-switch theorem**: if an attempted heavy cascade departs quantitatively from one null spectral ray, show that the resulting angular/cross-volume energy triggers an already-paid affine-half-Riesz, cross-bank, or nonisotropic-pivot branch. These are now the two concrete mechanisms needed to replace the refuted bounded-depth peeling strategy.

## 9. Status and regularity

- `QFORM-COLLINEAR-SPECTRAL-BANK-COMPRESSION-v1`: **PROVED**.
- exact same-ray whitening recurrence and exponential residual-mass decay: **PROVED**.
- `QFORM-FULL-NULL-RAY-BANK-v1`: **PROVED**, with a **continuous** density and `||p_Q||_infinity<=6e` under the target spectral normalization.
- assigned partner's arbitrarily long same-ray cascade: **PAID by the new theorem**; it remains a valid refutation of bounded-depth peeling.
- arbitrary `0<rho<1` correlated leakage: **OPEN**.
- arbitrary exact-rank-three orientation: **OPEN**.
- full owner target with additional spectrum: **OPEN**.

No Gaussian, log-concavity, compact-support, moment, connected-support, diagonal-basis, or post-rotation-independence assumption is used. The only rotations after product aggregation act on a bounded joint transverse density; independence is never inferred from them.
