SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T03:09:32Z.
attacking: projection-product overlap by conditioning genuinely overlapping original coordinates while retaining independent pure scalar and planar product banks.

# QFORM conditional-overlap projection-product transducer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Slot:** account01/B16 — Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM / FULL QFORM OPEN / CONTINUITY PARTIAL`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full conjecture is not proved here. The new result is an exact-rank-three structural/analytic implication. It strengthens the source-disjoint line/plane theorem of the designated partner by allowing an arbitrary set of original coordinates to carry both the line and plane spectral components; those overlap coordinates are conditioned, not rotated or assigned a fictitious conditional density cap. A second certificate applies the newest fractional-volume theorem directly to the overlap/pure cross block.

## 1. Sources and correction boundary


The designated partner result actually used is account02/B16 r23:

`yspennstate/math-open-problems@7044d3cf479cc067d97a317cf67b41121cc48aab:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T023136Z-account02-B16-QFORM-r23/REPORT.md`.

Its theorem `QFORM-DISJOINT-SPECTRAL-LINE-PLANE-44-v1` says, in exact rank three, that if the original-coordinate source splits into a spectral line bank and an orthogonal spectral-plane bank, then for arbitrary independent cap-one coordinate laws

`||p_Q||_infinity < 44`.                                           (1.1)

Crucially, the scalar line projection is independent of the whole dependent planar projection. The proof uses source-valid projection caps and never declares the two coordinates of the planar projection independent.

The newest Claude/interactive result actually used is the fractional three-volume theorem in

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its q=1 case says: for an original-coordinate cross block `M=A[I,J]`, if the third-volume row marginals satisfy `alpha_i^(vol)<=1/2`, then with `Z=e_3(M^TM)`

`||p_Q||_infinity <= 3 e Z^(-1/6)`,                               (1.2)

and the density has a continuous representative. The within-bank quadratic terms, outside couplings, and affine terms are arbitrary.

Live corrections retained throughout: no post-rotation independence; no arbitrary-joint rank-three coarea estimate; no positive moment of a worst conditional projection-density cap; no receiver-only indefinite trace estimate from a planar density cap; no law-uniform pointwise quadratic-phase decay; and no deletion of a small matrix term as a small random quadratic perturbation for arbitrary unbounded inputs.

## 2. Geometry with an arbitrary overlap bank

Let the entire physical matrix have exact rank three:

`A=R B R^T`, `R^T R=I_3`,                                        (2.1)

where `B` is real symmetric and

`min_j |lambda_j(B)| >= 1`.                                      (2.2)

Fix a spectral unit vector `e`. Partition the ORIGINAL coordinate indices into disjoint sets

`I disjoint_union J disjoint_union K=[n]`                         (2.3)

such that

`r_i in span(e)` for `i in I`,
`r_j in e^perp` for `j in J`,                                    (2.4)

while the rows `r_k`, `k in K`, are completely arbitrary. They may have simultaneous line and plane components and may be high leverage. Here `r_l^T` is row `l` of `R`.

Choose spectral coordinates with `e=e_1`. Write

`r_i=(a_i,0,0)`, `i in I`,
`r_j=(0,y_j)`, `y_j in R^2`, `j in J`.                           (2.5)

Define the surviving pure-bank Gram resources

`alpha = sum_(i in I) a_i^2`,
`G = sum_(j in J) y_j y_j^T`,
`m = min(alpha, lambda_min(G)).`                                  (2.6)

The new theorem assumes only `m>0`; there is no restriction on the number, laws, leverage, or spectral directions of the overlap coordinates in `K`.

## 3. Normalized product banks

Put

`u_I=(a_i/sqrt(alpha))_(i in I)`,
`U_J=R_J,plane G^(-1/2)`,                                        (3.1)

so

`||u_I||_2=1`, `U_J^T U_J=I_2`.                                  (3.2)

Define

`S=u_I^T X_I`,
`Y=U_J^T X_J in R^2`.                                             (3.3)

Because `I` and `J` are disjoint original-coordinate banks, `S` is genuinely independent of the **whole pair** `Y`. No independence between the two components of `Y` is asserted. The product-projection estimates used in the designated partner report give

`||p_S||_infinity <= sqrt(2)`,
`||p_Y||_infinity <= 2`.                                         (3.4)

Let

`D=diag(sqrt(alpha),G^(1/2))`.                                    (3.5)

Then the unconditioned contribution of the pure banks to the spectral coordinate is

`R_I^T X_I+R_J^T X_J=D xi`, `xi=(S,Y)`.                          (3.6)

## 4. Main theorem: condition the overlap, translate the original product source

### Theorem 4.1 — `QFORM-CONDITIONAL-OVERLAP-PURE-BANK-44-v1`

Under (2.1)--(2.6), for arbitrary independent input laws with one-dimensional densities bounded by one,

`boxed: ||p_(X^T A X)||_infinity < 44/m.`                         (4.1)

Equivalently,

`||p_Q||_infinity < 44 / min(alpha,lambda_min(G)).`               (4.2)

The conclusion is essential boundedness. Continuity is not asserted by this proof.

### Proof

Condition on the original overlap coordinates `X_K=x_K`. Original-coordinate independence leaves the laws of all coordinates in `I union J` unchanged and mutually independent. Put

`z_K=R_K^T x_K`.                                                  (4.3)

Since the whole matrix is exactly `RBR^T`, the conditional quadratic form is exactly

`Q | X_K=x_K = (D xi+z_K)^T B(D xi+z_K)`.                        (4.4)

No residual quadratic term has been discarded. Since `m>0`, `D` is invertible. Set

`eta=D^(-1)z_K`,
`C=D B D`.                                                        (4.5)

Then

`Q | X_K=x_K = (xi+eta)^T C(xi+eta)`.                            (4.6)

The deterministic translation `xi -> xi+eta` preserves the exact original-product provenance needed by the partner theorem. Indeed, writing `eta=(eta_0,eta_plane)`,

`S+eta_0 = u_I^T (X_I+eta_0 u_I)`,                               (4.7)

and

`Y+eta_plane = U_J^T (X_J+U_J eta_plane)`.                       (4.8)

All shifted physical coordinates are still independent, and translating a one-dimensional density does not alter its cap. The shifted scalar bank and shifted planar bank also remain source-disjoint. Thus `(S+eta_0,Y+eta_plane)` lies in exactly the stochastic class of account02/B16 r23; this is not an arbitrary joint-density substitution.

Next,

`s_min(C)=s_min(DBD)
 >= s_min(D)^2 s_min(B)
 >= m`.                                                           (4.9)

Because `C` is symmetric, the three eigenvalues of

`C_0=C/m`                                                         (4.10)

all have modulus at least one. Realize the shifted vector in (4.6) as the rank-three normalized physical frame whose rows on `I` lie on the first spectral axis and whose rows on `J` lie in the transverse plane. The hypotheses of the designated partner theorem apply verbatim to `C_0`. Hence

`||p_((xi+eta)^T C_0 (xi+eta))||_infinity <44`.                  (4.11)

Since the conditional output in (4.6) is `m` times the scalar random variable in (4.11), scalar density scaling gives

`||p_(Q | X_K=x_K)||_infinity <44/m`,                             (4.12)

uniformly in `x_K`. Integrating these conditional densities over the law of `X_K` gives a density for `Q` with the same essential bound. This proves (4.1). QED.

### What the theorem changes

The partner r23 report identified any overlap between the leaked line direction and transverse plane on the same original coordinates as unpaid. Theorem 4.1 shows that **arbitrary overlap coordinates can be present and can have arbitrary laws**: they may simply be conditioned, provided a quantitative pure scalar source and a quantitative pure planar source remain. The only price is the inverse surviving Gram scale `m^(-1)`. Thus the actual obstruction is narrower: *pure-bank depletion*, not overlap by itself.

For example, if

`alpha>=1/64`, `G >= (1/64)I_2`,                                 (4.13)

then regardless of the overlap bank `K`,

`||p_Q||_infinity < 2816`.                                       (4.14)

No quantity depending on `|K|`, its leverage, or its support appears.

## 5. A second certificate that uses the overlap bank instead of conditioning it

The conditional theorem deteriorates when a pure-bank Gram resource tends to zero. The newest fractional-volume theorem gives a complementary certificate directly on the cross interaction between `K` and the pure bank `D_0:=I union J`.

Put

`G_D=R_D0^T R_D0=diag(alpha,G)`,
`G_K=R_K^T R_K=I_3-G_D
    =diag(1-alpha,I_2-G)`.                                       (5.1)

Assume both `G_D` and `G_K` are positive definite. Let

`M=A[K,D_0]=R_K B R_D0^T`.                                      (5.2)

Factor

`R_K=U_K G_K^(1/2)`, `R_D0=U_D G_D^(1/2)`,                       (5.3)

where `U_K,U_D` have orthonormal columns. Then

`M=U_K [G_K^(1/2) B G_D^(1/2)] U_D^T`.                           (5.4)

Therefore `M` has rank three and the product of its three squared singular values is

`Z=e_3(M^TM)
 =det(G_K) det(G_D) det(B)^2`.                                   (5.5)

Using (5.1),

`Z=alpha(1-alpha) det(G) det(I_2-G) det(B)^2`.                   (5.6)

For a rank-three cross block the third-volume row marginal matrix is exactly the orthogonal projector onto its row-index range. Since `range(M)=range(R_K)`, its marginal at `k in K` is

`alpha_k^(vol)
 =(P_range(R_K))_kk
 =r_k^T G_K^(-1)r_k`.                                            (5.7)

This can also be read from the exact marginal formula in the volume theorem: with exactly three nonzero singular values, all three spectral weights `p_j` equal one.

### Theorem 5.1 — `QFORM-OVERLAP-CROSS-VOLUME-v1`

In addition to (2.1)--(2.5), suppose `G_D,G_K` are positive definite and

`max_(k in K) r_k^T G_K^(-1)r_k <=1/2`.                          (5.8)

Then the law of `Q` has a continuous density and

`boxed: ||p_Q||_infinity
 <=3e [det(G_K)det(G_D)det(B)^2]^(-1/6)`                          (5.9)

and, because `|det B|>=1`,

`boxed: ||p_Q||_infinity
 <=3e [alpha(1-alpha)det(G)det(I_2-G)]^(-1/6).`                  (5.10)

### Proof

Equation (5.7) verifies the exact row-marginal gate `alpha_k^(vol)<=1/2` for the actual physical cross block `M`. Apply the q=1 case of the newest fractional-volume theorem (1.2). Its arbitrary self-bank phases retain `A[K,K]`, `A[D_0,D_0]` and all affine terms, so no component of the same quadratic form is thrown away. Substitute the exact determinant identity (5.5), then use `|det B|>=1`. QED.

This is an equation-level application of the newest volume result, rather than a claim that three cross singular values are automatically present or automatically diffuse.

## 6. Hybrid interpretation

Theorems 4.1 and 5.1 pay different pieces of the same overlap geometry.

* The conditional partner route permits **arbitrarily concentrated** overlap coordinates `K`, but requires a quantitative pure line bank and a quantitative pure planar bank. It gives the dimension-free bound `44/m`.
* The volume route uses the overlap bank itself. It permits arbitrary within-bank quadratic curvature and gives a continuous density, but requires the exact rank-three cross-volume marginal gate (5.8) and nondegenerate aggregate Grams on both sides.

When both apply one may take the better of the two explicit bounds. For example, if all six aggregate scalar eigenvalues

`alpha, 1-alpha, lambda_1(G), lambda_2(G), 1-lambda_1(G), 1-lambda_2(G)`

are at least `delta` and (5.8) holds, then

`||p_Q||_infinity <= 3e/delta`,                                  (6.1)

with a continuous density, because the determinant product in (5.10) is at least `delta^6`.

## 7. Concrete overlapping-source check

Take `G_D=(1/2)I_3`, so `alpha=1/2` and `G=(1/2)I_2`. Let the overlap bank consist of the eight rows

`r_epsilon=(epsilon_1,epsilon_2,epsilon_3)/4`,
`epsilon in {+1,-1}^3`.                                          (7.1)

Their Gram is `(1/2)I_3=G_K`, and each overlap leverage is

`r_epsilon^T G_K^(-1) r_epsilon
 =2*(3/16)=3/8<1/2`.                                             (7.2)

For any symmetric `B` with all eigenvalue moduli at least one, Theorem 4.1 gives `<88`. The volume certificate is much sharper here:

`det G_D det G_K=(1/8)^2=1/64`,                                  (7.3)

so

`||p_Q||_infinity <=3e*(64)^(1/6)=6e<16.31`,                     (7.4)

and the density is continuous. The eight overlap rows genuinely have simultaneous components in all three spectral directions, so this is not the source-disjoint endpoint in disguise.

## 8. Exact remaining implication

The full conjecture remains open. Even the unrestricted exact-rank-three case is not closed by this run. The remaining B16 structural debt after these two certificates is now:

`QFORM-PURE-BANK-DEPLETION-HEAVY-OVERLAP-v1`:

> handle exact rank three when, for every useful spectral line/plane split, one surviving pure-bank Gram resource is arbitrarily small **and** any complementary overlap cross block fails the diffuse third-volume marginal gate.

In the account03/B16 finite-heavy-core compiler this is expected to sit inside the finite near-null near-line/near-plane minority-sign chamber. A small angular width cannot simply be deleted for arbitrary unbounded input laws, and a marginal planar density cap cannot be promoted to a conditional independent scalar. The current theorem therefore does not convert near-pure rows into pure rows without cost.

A separate global debt remains arbitrary additional spectrum: the conditioning identity (4.4) is exact because the whole matrix here has rank three. Selecting three large eigenvectors from a higher-rank matrix and discarding the rest would be invalid.

## 9. Review and proof status

No independent end-to-end review of the two new theorems was performed in this run. They are supporting arguments, not a full-solution promotion. The full QFORM claim and global continuity claim remain OPEN. Repository transport was used for source retrieval and output delivery, but no authenticated native learned-memory receiver ingestion occurred; status remains `WITHOUT_VERIFIED_BRAIN`.
