SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T18:22:07Z.
attacking: the joint-maximal-curvature bridge; globalize the partner's conditional determinants into genuine original-coordinate rank-three crossings before any frozen-fiber or Borel maximalisation.

# fleet02/B05 auto11b — conditional determinants globalized by physical three-crossings

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea bound; complementary constructions/source-valid counterexamples.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `PROVED_SUPPORTING_THEOREM / NEW PHYSICAL-CROSSING ATLAS / FULL QFORM OPEN`.  
**Regularity:** the new conclusions are essential-density bounds. Continuity of the final unconditional mixture is not asserted.

The predecessor B05 run corrected an invalid interval-to-Borel frozen-slice transfer and isolated the unpaid joint-maximal-curvature bridge. The present run avoids that interface entirely. It keeps disjoint original-coordinate banks intact, converts the latest partner's conditional determinant currencies into exact rank-three **physical cross blocks**, and applies a completed product-preserving crossing theorem before any arbitrary measurable-set supremum appears.

## 1. Sources actually applied

The required pinned source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its Theorem F is applied below to remove the globally diffuse exact-rank-three branch:

`all spectral-row leverages <=1/2  ==>  ||p_Q||_infinity<=12`.          (1.1)

Its product-projection density input is also used in the physical crossing receiver.

The newer completed crossing theorem used at the main inequality is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401:`
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For independent physical groups with exact-rank-`r` cross block whose nonzero singular values have product `Gamma`, if the two corresponding `r`-dimensional orthogonal projections have density caps `M_L,M_R`, then for `r>2`

`||p_Q||_infinity <= r/(r-2) (M_L M_R/Gamma)^(1/r)`.                  (1.2)

All functions internal to either physical side are arbitrary. For cap-one product coordinates and `r=3`, the standard three-dimensional projection caps are at most `2^(3/2)` on each side, so

`boxed{ ||p_Q||_infinity <=6 Gamma^(-1/3). }`                          (1.3)

The latest compatible designated partner is fleet03/B05 r29, source-pinned at

`yspennstate/math-open-problems@9e0a5c32599f8cc180dd905615c9d034a9b51d2c:`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T172119Z-fleet03-B05-QFORM-r29/REPORT.md`.

Its deterministic currency compensation and exact determinant identities are consumed explicitly below.

## 2. Ratio-packet notation from the partner

The first original-coordinate product bank carries an orthonormal two-dimensional frame `U`; write its rows as `u_i in R^2` and its aggregate projection as

`x=U^T X=(S,R)`.

Two disjoint original-coordinate product banks carry normalized scalar projections `Y,Z`; they are independent of each other and of the first bank. The homogeneous aggregate packet is

`H=[[C,P],[P^T,B]]`,

`B=[[a,c],[c,d]]`, `P=[[alpha,beta],[r,s]]`,                            (2.1)

with `B` invertible indefinite and

`C-P B^(-1)P^T = [[L,0],[0,0]]`,
`L=lambda*m`, `mu=|det B| |lambda|`, `m>=3/20`.                         (2.2)

Put

`Delta=det B<0`, `q=(r,s)^T`, `z=B^(-1)q=(z1,z2)^T`,
`theta^2=z1^2+z2^2`.                                                    (2.3)

The partner proves that, after conditioning on `Z`, the retained matrix on `(Y,S,R)` has determinant

`boxed{ |det H_Y|=mu*m*z2^2, }`                                        (2.4)

and after conditioning on `Y`,

`boxed{ |det H_Z|=mu*m*z1^2. }`                                        (2.5)

It also proves the low-`Psi` compensation

`chi |det C|+Psi >= (1/4)mu*m*theta^4`,                                (2.6)

which gives a strong rank-two half-Riesz trace as `chi->0`. The predecessor showed that this fractional trace cannot simply be promoted to a Borel square-root profile. The point here is to globalize (2.4)-(2.5) directly in physical coordinates instead.

## 3. A general conditional-determinant globalization theorem

### Theorem 3.1 — `QFORM-CONDITIONAL-DET-PHYSICAL-CROSSING-v1`

Let one original-coordinate product bank have an orthonormal two-frame `U` and aggregate `W=U^T X`. Let a disjoint original-coordinate product bank have a normalized scalar projection

`Y=sum_j v_j Z_j`, `sum_j v_j^2=1`.

Condition on any disjoint environment. Suppose the remaining homogeneous quadratic part in `(W,Y)` is represented by an invertible symmetric `3 x 3` matrix `G`; arbitrary affine terms are allowed.

Define the first-bank split currency

`sigma_U := max_I sqrt(det(U_I^T U_I) det(U_{I^c}^T U_{I^c}))`,          (3.1)

and the scalar-bank split currency

`sigma_v := max_A sqrt(p_A(1-p_A)),`
`p_A:=sum_{j in A}v_j^2`.                                               (3.2)

Then, whenever `sigma_U sigma_v>0`, the conditional law, and hence the unconditional law after averaging the environment, satisfies

`boxed{
 ||p_Q||_infinity <=6 (|det G| sigma_U sigma_v)^(-1/3).
}`                                                                        (3.3)

#### Proof

Choose partitions `I/I^c` and `A/A^c` attaining or approximating (3.1)-(3.2). Put the physical coordinates `I union A` on the left and `I^c union A^c` on the right. Because the two source banks are disjoint, the two physical groups are independent product vectors.

Let `R_L` be the map from the left physical coordinates to their partial aggregate `(W_L,Y_L)`, and `R_R` the analogous right map. Their Gram matrices are block diagonal:

`R_L^T R_L=diag(U_I^T U_I,p_A)`,
`R_R^T R_R=diag(U_{I^c}^T U_{I^c},1-p_A)`.                             (3.4)

The physical cross block of the conditioned quadratic form is exactly

`M_cross=R_L G R_R^T`.                                                  (3.5)

Thin polar/QR factorisation shows that the three nonzero singular values of (3.5) have product

`Gamma
 = |det G| sqrt(det(R_L^T R_L) det(R_R^T R_R))
 = |det G| sqrt(det(U_I^T U_I)det(U_{I^c}^T U_{I^c})p_A(1-p_A)).`       (3.6)

Thus `Gamma>=|det G| sigma_U sigma_v` up to an arbitrarily small approximation to the suprema. Every term internal to either side, including arbitrary quadratic terms generated by the conditioned environment, is permitted by the exact-rank-three physical crossing theorem (1.3). Hence

`||p_{Q|environment}||_infinity<=6 Gamma^(-1/3)`.

The bound is uniform in the environment, so averaging gives (3.3). No output continuity, conditional projection-density cap, post-rotation independence, or curved-fiber supremum is used. QED.

## 4. Exact lower bounds for the two split currencies

### 4.1 The scalar bank

Let

`g_v:=max_j v_j^2`.                                                     (4.1)

There is always a subset `A` with

`|p_A-1/2|<=g_v/2`.                                                     (4.2)

Indeed, order the weights arbitrarily and stop at the first partial sum crossing `1/2`; the distances of the pre- and post-crossing sums from `1/2` add to the last weight, at most `g_v`, so one distance is at most `g_v/2`. Therefore

`boxed{ sigma_v >= (1/2)sqrt(1-g_v^2). }`                              (4.3)

In particular, if `g_v<=1/2`, then `sigma_v>=sqrt(3)/4`.

### 4.2 The two-dimensional product frame and its exact Pluecker currency

For rows `u_i`, put

`w_ij=det(u_i,u_j)^2`, `i<j`.                                          (4.4)

Cauchy-Binet and Parseval give

`sum_{i<j}w_ij=1`,
`sum_{j:j!=i}w_ij=||u_i||^2`.                                          (4.5)

Define the ordered disjoint-edge mass

`D_U:=sum_{e cap f=empty} w_e w_f`.                                    (4.6)

For a fair random partition `I/I^c`,

`E[det(U_I^T U_I)det(U_{I^c}^T U_{I^c})]=D_U/16`,                      (4.7)

because a disjoint pair of Pluecker edges lands wholly on opposite sides with probability `1/16`. Hence

`boxed{ sigma_U >= (1/4)sqrt(D_U). }`                                  (4.8)

The currency also has the exact identity

`D_U=1-sum_i ||u_i||^4 + sum_{i<j}w_ij^2`.                              (4.9)

To see this, `sum_i ||u_i||^4` counts all ordered intersecting edge pairs through their common vertex, while identical edges are counted twice and must be subtracted once.

If `h:=max_i||u_i||^2<1/2`, then for each edge `{i,j}` the total Pluecker mass disjoint from it is at least `1-2h`; averaging over the first edge gives

`D_U>=1-2h`,                                                           (4.10)

so

`boxed{ sigma_U >= (1/4)sqrt(1-2h). }`                                 (4.11)

### 4.3 Exact zero structure

`D_U=0` means every two nonzero Pluecker edges intersect. A graph whose edges are pairwise intersecting is a star or a triangle.

- In the star case all noncentral nonzero rows are parallel. Parseval then forces the central row to have leverage exactly one and the rest to span its orthogonal line: this is an exact coloop geometry.
- In the triangle case there can be no nonzero row outside the three triangle vertices, otherwise it creates an edge disjoint from one triangle edge. Thus the two-frame is supported on at most three original coordinates.

So the exact failure of the split currency is localized; it is not a diffuse high-dimensional phenomenon. Quantitative stability as `D_U downarrow0` remains a separate task.

## 5. Apply Theorem 3.1 to the partner's two conditional determinants

Let `g_Y` and `g_Z` be the largest squared coefficients in the normalized scalar projections `Y,Z`. Apply Theorem 3.1 after conditioning on `Z` and use (2.4), (4.3), (4.8):

`boxed{
 ||p_Q||_infinity
 <=6 [8/(mu*m*z2^2 sqrt(D_U(1-g_Y^2)))]^(1/3),
}`                                                                        (5.1)

whenever the displayed split currency is nonzero. Symmetrically,

`boxed{
 ||p_Q||_infinity
 <=6 [8/(mu*m*z1^2 sqrt(D_U(1-g_Z^2)))]^(1/3).
}`                                                                        (5.2)

These are full ambient essential-density bounds. Conditioning the opposite scalar bank creates only affine terms on the retained product groups, which are harmless in the crossing theorem.

If `h<=3/8` and both scalar banks satisfy `g_Y,g_Z<=1/2`, then `D_U>=1/4`, and choosing the larger component of `z` gives `max(z1^2,z2^2)>=theta^2/2`. Hence

`boxed{
 ||p_Q||_infinity
 <=6 [32/(sqrt(3)*mu*m*theta^2)]^(1/3)
 <19.985 (mu*m*theta^2)^(-1/3).
}`                                                                        (5.3)

This removes the shear-imbalance problem completely in the diffuse three-bank packet. It does not matter if one of `z1,z2` tends to zero: use the other conditional determinant and split that scalar source bank itself.

At the level of the partner's low-`Psi` chamber, (5.3) supplies the missing full-order smoothing whenever the same-bank two-frame and the relevant scalar source bank remain physically splittable. No Borel maximalisation of the half-Riesz trace is needed.

## 6. A second globalization that needs no scalar-bank split

There is a complementary three-crossing which is useful when the scalar banks themselves are concentrated.

Place the whole `Y` bank with a first-bank subset `I`, and the whole `Z` bank with `I^c`. The aggregate `3 x 3` cross matrix is

`K=[[C,p_Z],[p_Y^T,c]]`,
`p_Y=(alpha,r)^T`, `p_Z=(beta,s)^T`.                                   (6.1)

For a symmetric `2 x 2` matrix,

`p_Y^T adj(C)p_Z=(Jp_Y)^T C(Jp_Z)`.                                    (6.2)

The partner's mixed-transverse identity and determinant formula therefore yield

`det K=c det C-U_mix=-L Delta z1 z2`,                                  (6.3)

so

`boxed{ |det K|=mu*m*|z1 z2|. }`                                      (6.4)

The two whole scalar projections are normalized and sit on opposite physical sides. Combining (4.8), (6.4), and (1.3) gives

`boxed{
 ||p_Q||_infinity
 <=6 [4/(mu*m*|z1z2| sqrt(D_U))]^(1/3).
}`                                                                        (6.5)

If `h<=3/8`, then `D_U>=1/4`, and

`boxed{ ||p_Q||_infinity <=12 (mu*m*|z1z2|)^(-1/3). }`                 (6.6)

Thus scalar-bank concentration by itself is not an obstruction when both inverse-pair shear components remain quantitative.

Equation (6.3) was also checked symbolically: `det K+L Delta z1 z2` simplifies identically to zero. The singular-volume factorisation (3.6) was checked on seeded finite matrices to relative error below `2.7e-15`; these checks are diagnostic only, not proof substitutes.

## 7. Why the grouped-hub projected-crossing receiver cannot spend `det C`

The same new crossing source contains a grouped-hub theorem in which hub directions contribute `k` powers and a **projected** residual crossing contributes `ell`, with density integrability only when `k+ell>2`. A tempting idea is to group `(Y,Z)` as the hub and spend the partner's large low-`Psi` determinant `|det C|` as residual crossing curvature. That route is structurally impossible in this packet.

For any first-bank split `I,J`, let

`E_J=row(U_J^T)`, `dim E_J<=2`.                                        (7.1)

Any hub-light cross matrix supported by `(Y,Z)` on `J` has row space contained in `E_J`, because it is a compression of `P^T U_J^T`. If its rank is `k`, then the light-light block

`U_I C U_J^T`                                                         (7.2)

also has row space in `E_J`, and after the grouped-hub theorem projects away `row(M_J)` its remaining rank is at most `2-k`. Therefore every nonzero projected volume order satisfies

`boxed{ ell<=2-k, hence k+ell<=2. }`                                   (7.3)

The integrable regime `k+ell>2` can never occur. When `P` and `U_J` both have rank two, the projected crossing is identically zero.

This matters directly for partner r29. Its low-`Psi` compensation can force

`|det C| >= mu*m*theta^4/(8 chi)`,                                    (7.4)

which diverges as `chi->0`, but (7.3) says that **all of this large curvature lies in the same two-dimensional plane already seen by the hub cross directions**. Projecting away that plane destroys the resource. The successful estimates (5.1)-(6.6) instead repartition the original scalar banks so that the same determinant becomes a genuine rank-three cross volume before projection.

This is the exact reason the projected-crossing theorem is compatible with, but does not automatically solve, the r29 packet.

## 8. Required pinned e5f result applied to the global proof map

The pinned `e5f71d79...` Theorem F gives the actual full-target inequality

`all active rank-three spectral-row leverages <=1/2
   ==> ||p_Q||_infinity<=12`.                                          (8.1)

Thus an exact-rank-three survivor of the global problem has a high-leverage row. The new local crossing atlas does not contradict that: the first-bank two-frame in the ratio packet can still have `D_U` quantitative even when the full three-frame has a heavy row elsewhere. In that situation (5.1)-(6.6) spend the partner's escaped curvature without rotating the random inputs.

The required pinned counterexample search still reports no target-valid counterexample; its ruled one-sheet theorem is already paid, and the difficult geometry is on the convex/two-sheet side. The present branch estimates are full-line Fourier/crossing bounds, so they apply equally to both signs of the output level in their stated packet.

## 9. First unpaid implication after this run

The previous broad `QFORM-HUB-JOINT-MAXIMAL-CURVATURE-BRIDGE-v1` is now narrowed to a concrete coefficient-space survivor:

`QFORM-RATIOPACKET-SPLIT-CURRENCY-STABILITY-v1`:

> In the low-`Psi` active-shear ratio packet, handle the simultaneous degeneration of the physical split currencies after applying (5.1)-(6.6): `D_U ->0` together with concentration of the scalar bank carrying the larger `z_j^2`, or with collapse of the inverse-pair shear scale. Quantify the near-star/near-three-coordinate structure of a two-dimensional Parseval frame when `D_U` is small, and feed that localized structure into the already completed scalar/dependent-pair or physical-pair receivers. Do not replace small coefficient error by a small random quadratic perturbation.

More explicitly, after this run a diffuse packet with

`D_U >= delta_U`, `1-g_Y^2 >= delta_Y`, `1-g_Z^2 >= delta_Z`,
`mu*m*theta^2 >= delta_theta`

is fully paid by (5.1)-(5.3). If the relevant scalar split collapses but `mu*m|z1z2| sqrt(D_U)` remains quantitative, (6.5) pays it anyway. Therefore a genuine survivor must push toward **localized original-coordinate geometry**: small disjoint Pluecker mass, a nearly single-coordinate scalar bank, and/or a vanishing shear currency. The exact endpoint `D_U=0` is already classified as coloop/star or support on at most three first-bank coordinates.

The next mathematical task is quantitative stability of that endpoint, not another interval-to-Borel transfer and not another attempt to spend `det C` after the hub projection has removed its plane.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. No moments, support bounds, log-concavity, identical laws, diagonal-basis independence, post-rotation independence, arbitrary-joint coarea theorem, conditional-density supremum, or fiberwise maximal trace is used.
