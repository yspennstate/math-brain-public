SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-24T00:33:26Z.
attacking: aggregate a zero-pivot determinant star before selecting a physical minor; close the exact-rank-three low-residual-rank nullstar branch and identify the exact surviving isotropic-shear geometry.

# account01/B05 auto20 — aggregate zero-pivot star before minor selection

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bound preserving arbitrary product densities.  
**Status:** `PROVED SUPPORTING THEOREM / EXACT STRUCTURAL CLASSIFICATION / PARTNER RESULT APPLIED / FULL QFORM OPEN`.  
**Regularity:** essential boundedness is proved in the theorem below. Continuity is **not** claimed from this argument. Full-target continuity remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Compact end-to-end reduction and the first unpaid implication

The previous B05 run proved that conditioning away the third curvature can leave a logarithmically singular rank-two saddle even when the square-carrier overlap is arbitrarily small. The newest account02/B05 partner report sharpened the complementary geometric currency: for an exact-rank-three physical form, the total principal-determinant star through a physical coordinate `i` is

`S_i := sum_{j<k, j,k != i} |det A[{i,j,k}]| = c_i Delta_3`,          (1.1)

where `c_i` is the spectral leverage of the coordinate and `Delta_3` is the product of the absolute values of the three nonzero eigenvalues. Its ratio-packet formulas compute the same star exactly for heavy scalar sources.

The missing operation was to use `S_i` **before** selecting one tiny physical triple. This run proves such an aggregate receiver for every exact-rank-three **zero-pivot** form whose residual principal block has rank at most two:

`boxed{ ||p_Q||_(infinity,ess) <= C_star S_i^(-1/3),`                 (1.2)
`        C_star = 7.761982175235 * 2^(2/3) < 12.322. }`

Consequently, at target normalization, if `c_i>=1/2`, then `S_i>=1/2` and

`boxed{ ||p_Q||_(infinity,ess) < 15.524. }`                          (1.3)

The proof does not choose any pair `(j,k)`. It sums the entire Pluecker/determinant star first, converts it exactly into a two-dimensional projection Jacobian, and only then invokes the completed account02/B05 null-hub receiver.

There is also an exact classification. For an exact-rank-three zero-pivot matrix

`A = [[0,l^T],[l,C]],`                                                (1.4)

the only case not covered by the new theorem is

`rank(C)=3,  l in Ran(C),  l^T C^+ l = 0.`                           (1.5)

Writing `w=C^+l`, this survivor has the exact isotropic-shear identity

`boxed{ Q(H,Z) = (Z+H w)^T C (Z+H w),  w^T C w=0. }`                 (1.6)

Thus the zero-pivot debt is no longer “all null hubs” or “small square-carrier overlap.” It is precisely a product-destroying shear along a `C`-isotropic direction of a rank-three indefinite residual. The earlier target-valid overlap family lands exactly in (1.5)-(1.6), so this classification reconciles the previous obstruction with the present positive theorem.

The next B05 implication is therefore:

`QFORM-ISOTROPIC-SHEAR-LINE-CONVOLUTION-v1`:

> control the quadratic trace of the line-convolved product density produced by `Y=Z+Hw` when `rank(C)=3` and `w^T C w=0`, using the aggregate determinant star before any conditioning that turns the problem into a rank-two saddle.

## 2. Aggregate-star theorem

### Theorem 2.1 — `QFORM-NULLSTAR-LOW-RESIDUAL-RANK-AGGREGATOR-v1`

Let `X_0,X_1,...,X_m` be independent real random variables with probability densities bounded by one. Let

`A = [[0,l^T],[l,C]]`                                                (2.1)

be real symmetric of rank exactly three, where `l in R^m` and `C` is the residual `m x m` block. Assume

`rank(C) <= 2.`                                                       (2.2)

Put

`Q = X^T A X`

and define the principal-determinant star through coordinate zero by

`S_0 = sum_{1<=j<k<=m} |det A[{0,j,k}]|.`                            (2.3)

Then `S_0>0`, the law of `Q` has an essentially bounded density, and

`boxed{
 ||p_Q||_(infinity,ess)
 <= C_star S_0^(-1/3),
 C_star=7.761982175235*2^(2/3)
       =12.321378670326... <12.322.
}`                                                                    (2.4)

No moment, support, connected-support, Gaussian, log-concavity or rotated-coordinate independence assumption is used.

### Proof

We first show that the homogeneous quadratic form has a two-linear-form representation with a genuine transverse square.

Because `rank(A)=3` and the upper-left pivot is zero, the rank classification proved in Section 3 implies that under (2.2) there exist linearly independent vectors `l,v in R^m` and real numbers `alpha,beta,lambda` with `lambda !=0` such that

`C = alpha l l^T + beta(l v^T+v l^T)+lambda v v^T.`                  (2.5)

Write

`H=X_0,  L=l^T Z,  V=v^T Z,  Z=(X_1,...,X_m)^T.`                    (2.6)

Then

`Q=2HL+alpha L^2+2 beta L V+lambda V^2.`                            (2.7)

The determinant star can now be computed without selecting a pair. For each `j<k`, direct expansion gives the exact cancellation

`det A[{0,j,k}]
 = -lambda (l_j v_k-l_k v_j)^2.`                                   (2.8)

All `alpha` and `beta` terms disappear. Hence all nonzero determinants in the star have one sign before absolute values, and Cauchy-Binet gives

`S_0
 = |lambda| sum_{j<k}(l_j v_k-l_k v_j)^2
 = |lambda| (||l||_2^2 ||v||_2^2-<l,v>^2).`                         (2.9)

Set

`s=||l||_2>0,
 theta=<l,v>/s^2,
 v_perp=v-theta l,
 r=||v_perp||_2>0.`                                                  (2.10)

Define the normalized physical linear forms

`U=(l/s)^T Z,
 W=(v_perp/r)^T Z.`                                                  (2.11)

Their coefficient vectors are orthonormal. Therefore `(U,W)` is an honest two-dimensional orthogonal marginal of the original product density. The sharp product-projection theorem used throughout the current QFORM programme gives

`||p_(U,W)||_infinity <= 2.`                                        (2.12)

No claim of independence of `U` and `W` is made.

Moreover

`L=sU,  V=theta sU+rW.`                                              (2.13)

Let `H'=sH`. Since `H` is independent of the residual original coordinates, `H'` is genuinely independent of `(U,W)` and has density cap at most `1/s`. Substituting (2.13) into (2.7) gives

`Q=2H'U+A_0 U^2+2B_0 U W+(lambda r^2)W^2`                           (2.14)

for explicit real `A_0,B_0` whose values are irrelevant.

Now apply the completed designated-partner theorem account02/B05, `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`, to the actual variables in (2.14). Its hypotheses are exactly met with

`m=1/s,  M=2,  c_2=lambda r^2.`                                     (2.15)

Therefore

`||p_Q||_(infinity,ess)
 <=7.761982175235 (2/s)^(2/3) (|lambda|r^2)^(-1/3)`
` = [7.761982175235*2^(2/3)]`
`   (|lambda|s^2r^2)^(-1/3).`                                      (2.16)

But by (2.9)-(2.10),

`|lambda|s^2r^2=S_0.`                                                (2.17)

Equations (2.16)-(2.17) prove (2.4). QED.

### Why this is genuinely aggregate

If the determinant mass is spread over `N` physical pairs, choosing the largest pair first can only guarantee a determinant of order `S_0/N` and the zero-pivot triple theorem would lose `N^(1/3)`. Formula (2.9) instead recognizes the **sum of all squared wedges** as one Euclidean two-volume. The two-dimensional projection theorem spends that two-volume before any reciprocal determinant is taken. This is exactly the missing ordering requested by the coarea assignment.

## 3. Exact rank classification at a zero physical pivot

### Lemma 3.1 — `QFORM-ZERO-PIVOT-RESIDUAL-RANK-TRICHOTOMY-v1`

Let

`A=[[0,l^T],[l,C]]`                                                  (3.1)

be symmetric of rank exactly three. Then exactly one of the following holds.

1. `l notin Ran(C)` and `rank(C)=1`.
2. `l in Ran(C)`, `rank(C)=2`, and `kappa:=l^T C^+l !=0`.
3. `l in Ran(C)`, `rank(C)=3`, and `kappa:=l^T C^+l =0`.

Cases 1 and 2 are exactly the scope of Theorem 2.1. Case 3 is the isotropic-shear survivor.

### Proof

Because `C` is symmetric,

`R^m = Ran(C) direct_sum Ker(C)`                                     (3.2)

orthogonally.

If `l notin Ran(C)`, it has a nonzero component in `Ker(C)`. In a basis adapted to (3.2), the new hub coordinate couples to that kernel component and contributes a nondegenerate `2 x 2` off-diagonal block, while `C` contributes its own rank. Hence

`rank(A)=rank(C)+2.`                                                  (3.3)

Since `rank(A)=3`, necessarily `rank(C)=1`. Choosing `v` spanning `Ran(C)` gives `C=lambda vv^T`, `lambda!=0`, and `l,v` are independent. Thus (2.5) holds with `alpha=beta=0`.

Now suppose `l in Ran(C)`. Put

`w=C^+l,  kappa=l^T C^+l=w^T Cw.`                                  (3.4)

Since `Cw=l`, the homogeneous form satisfies the exact completion

`Z^T C Z+2H l^T Z
 =(Z+Hw)^T C(Z+Hw)-kappa H^2.`                                      (3.5)

This is an invertible linear congruence, so

`rank(A)=rank(C)+1` if `kappa!=0`,
`rank(A)=rank(C)`   if `kappa=0`.                                   (3.6)

Rank three therefore gives cases 2 or 3.

It remains only to justify the nonzero transverse-square coefficient in case 2. Since `rank(C)=2` and `l in Ran(C)`, choose `v` so that `Ran(C)=span{l,v}`. Symmetry gives a representation

`C=[l v] K [l v]^T,
 K=[[alpha,beta],[beta,lambda]],`                                    (3.7)

with `det K !=0`. Let `G=[l v]^T[l v]`. Solving `Cw=l` inside the range gives

`K G x=e_1,  w=[l v]x.`                                              (3.8)

Therefore

`kappa=l^T w=e_1^T Gx=e_1^T K^(-1)e_1=lambda/det K.`                (3.9)

Case 2 has `kappa!=0`, hence `lambda!=0`, exactly as needed in Theorem 2.1.

In case 3, (3.5) reduces to

`boxed{ Q(H,Z)=(Z+Hw)^T C(Z+Hw),  w^TCw=0, }`                        (3.10)

and `C` must be indefinite on its three-dimensional range because a nonzero isotropic vector cannot exist for a definite form. QED.

## 4. Target-normalized corollary via the partner star identity

For an exact-rank-three matrix write

`A=V M V^T,  V^TV=I_3,`                                             (4.1)

and let

`c_i=||V^T e_i||_2^2,
 Delta_3=|det M|.`                                                    (4.2)

The account02/B05 cofactor compiler proves the exact volume-sampling identity

`S_i=sum_{T: |T|=3, i in T}|det A_T|=c_i Delta_3.`                   (4.3)

Apply Theorem 2.1 at a zero-pivot coordinate `i` whose complementary residual block has rank at most two. If the three nonzero eigenvalues satisfy the target normalization `|lambda_j|>=1`, then `Delta_3>=1`. Hence if `c_i>=1/2`,

`S_i>=1/2`                                                           (4.4)

and

`||p_Q||_(infinity,ess)
 <=12.321378670326... * 2^(1/3)
 =15.52396435047... <15.524.`                                       (4.5)

This is dimension-free and uses no individual physical minor lower bound.

The existing diffuse exact-rank-three theorem already controls the complementary leverage chamber in which every `c_i<=1/2`. Thus, **inside the exact-rank-three zero-pivot route**, the new unpaid high-leverage geometry is forced into case 3 of Lemma 3.1: rank-three residual plus isotropic Schur zero. This statement does not close nonzero-pivot near-null branches or arbitrary extra spectrum.

## 5. Second designated-partner application: the live ratio packet

The newest account02/B05 ratio-packet report proves for a literal `Y`-source coordinate `U_j`

`S_(Y,j)=eta_j^2 mu m (1+z_2^2).`                                   (5.1)

Consider the homogeneous exact-rank-three ratio packet and suppose the selected heavy `Y` coordinate has exact zero physical pivot and its complementary residual block has rank at most two. Theorem 2.1 and (5.1) give the actual inequality

`boxed{
 ||p_Q||_(infinity,ess)
 <=12.321378670326...
   [eta_j^2 mu m (1+z_2^2)]^(-1/3).
}`                                                                    (5.2)

In the live heavy-scalar chamber `q_Y=max eta_j^2>3/4`, choose a maximizing source. Under the standard ratio-packet lower bound `m>=3/20`,

`S_(Y,j) > (3/4)(3/20) mu = (9/80)mu`,                              (5.3)

so

`boxed{
 ||p_Q||_(infinity,ess)
 < 12.321378670326...(80/9)^(1/3) mu^(-1/3)
 = 25.52359221507... mu^(-1/3).
}`                                                                    (5.4)

The symmetric statement holds for a heavy `Z` source. Thus the account02/B05 aggregate-star currency really does pay a complete nontrivial part of its current nullstar frontier once the residual-rank trichotomy is imposed. For an ambient conditioned use with arbitrary affine components outside the two active residual forms, (5.2) is **not** claimed without an additional affine-stability argument.

## 6. Reconciliation with the previous overlap-saddle obstruction

The previous B05 target-valid stress family was

`Q_delta
 =Y^2+2delta H Y+2H X-X^2/delta^2+Z^2.`                            (6.1)

Using `H` as the zero-pivot coordinate, its residual block and coupling vector are

`C_delta=diag(1,-delta^(-2),1),
 l_delta=(delta,1,0)^T.`                                             (6.2)

The residual has rank three. Moreover

`w_delta=C_delta^(-1)l_delta
       =(delta,-delta^2,0)^T`                                       (6.3)

and

`w_delta^T C_delta w_delta
 =delta^2-delta^2=0.`                                                 (6.4)

Thus this family lies **exactly** in case 3 of Lemma 3.1, not in the newly paid low-residual-rank cases. Equation (3.10) becomes its vertex-aligned isotropic shear. The earlier independent-square bridge happened to pay this special member because its third direction was a literal disjoint square; the present classification explains why that special proof does not automatically extend to a general isotropic shear.

This is useful negative information: trying to extend Theorem 2.1 merely by continuity from `rank(C)<=2` to `rank(C)=3` would cross precisely the geometry in which the rank-two conditional density developed a logarithmic saddle.

## 7. The surviving coarea problem in its cleanest form

In case 3, let `w=C^+l`. If `Z` has product density `prod_j f_j`, the shear variable

`Y=Z+Hw`                                                            (7.1)

has density

`g(y)=int_R f_H(h) prod_j f_j(y_j-h w_j) dh.`                        (7.2)

Then `0<=g<=1`, but a generic joint `L^infinity` cap is known to be insufficient for an indefinite quadratic trace. The extra usable datum is the **line-convolution/product provenance** in (7.2). The desired estimate becomes

`sup_t integral_{y^T C y=t} g(y)/(2|Cy|) d sigma(y) <= universal C`, (7.3)

under the spectral normalization inherited from the original exact-rank-three `A`, with the determinant star retained. Any proof of (7.3) which replaces (7.2) by only `g<=1` would violate the live arbitrary-joint coarea correction.

This formulation isolates the precise missing factor for B05: **one-dimensional convolution along an isotropic direction of a product density**, not an arbitrary joint density and not a post-rotation independent law.

## 8. Sources actually applied

1. Fresh owner/control state: `yspennstate/math-research-brain` main, current OWNER CONTROL revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`.
2. Designated partner null-hub theorem: `yspennstate/math-open-problems@e7a21ed67b943d7aded714ac17ca48bdab4a1349`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T200516Z-account02-B05-QFORM-auto11c/REPORT.md`, theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`.
3. Newest designated partner cofactor compiler: `yspennstate/math-open-problems@592ae3869873b6cf71cc375758b11655b1630aac`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T232530Z-account02-B05-QFORM-r11a/REPORT.md`.
4. Previous B05 overlap obstruction and independent-square repair: `yspennstate/math-open-problems@e4bf40b7376380c069ccee64a530fd2297ef04e3`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T233435Z-account01-B05-QFORM-auto17/RECONCILIATION.md`.
5. Two-dimensional product-projection cap used in (2.12): Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), Theorem 1.1, as source-pinned in the current QFORM synthesis.

## 9. Scope and correction audit

**Proved this run:** aggregate-star density bound (2.4); exact zero-pivot rank trichotomy; target-normalized `<15.524` high-leverage corollary in the low-residual-rank exact-rank-three branch; ratio-packet bound (5.4); exact identification of the previous overlap family with the surviving isotropic-shear class.

**Not proved:** the rank-three-residual isotropic-shear receiver (7.3); arbitrary affine stability outside the active two residual forms; nonzero-pivot near-null closure; arbitrary extra spectrum; the unrestricted full QFORM theorem; or full-target continuity.

The proof uses no pointwise quadratic-phase decay, no post-rotation independence, no generic joint-density coarea theorem, no conditional projection cap, no moment/support assumptions, and no selection of a single small determinant before aggregation. The product structure is spent only through an actual original-coordinate two-dimensional orthogonal projection and the actual independent physical hub.

No counterexample to the full target is claimed. Full QFORM remains `OPEN_NOT_PROVED_NOT_DISPROVED`. Full-target continuity remains `OPEN`.
