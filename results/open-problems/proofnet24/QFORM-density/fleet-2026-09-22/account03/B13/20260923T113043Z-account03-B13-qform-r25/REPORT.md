SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T11:30:43Z.
attacking: extremal compact product witnesses and a translation-invariant slab-scale transfer that turns small but nonzero leaf curvature into a quantitative geometric obstruction, rather than deleting it uniformly.

# account03/B13 r25 — slab-scale robust curvature graph on extremal product witnesses

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: extremal product laws / STRUCTURE  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuity: **OPEN**.

Fresh owner control at run start was `yspennstate/math-research-brain@41da05cfaafd1a5e6b407992a5a0f5560566c271`, later refreshed during the run. OWNER CONTROL was revision `2026-09-22.15`, QFORM only.

This run deliberately changes mechanism from the preceding local-matrix compilers. The point is to exploit the already-proved extremal-product reduction and work directly on the geometric product-set slab inequality. The live correction that small coefficients cannot be deleted uniformly on arbitrarily translated/fragmented supports is respected: every perturbation below is measured against the *centered diameter of the actual bounded extreme witness and the actual slab width*.

## 1. Completed inputs actually used

### 1.1 Designated partner account04/B13

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

Its no-attainment purification theorem says that for every bounded measurable product kernel, in particular

`K(x)=1_{x^T A x in J}`,

the supremum over independent cap-one mass-one marginal densities is exactly the supremum over products of indicators `1_{E_i}` with `|E_i|=1`, where each `E_i` may be chosen a bounded finite union of intervals. No optimizer, single interval, bounded diameter, or fixed fragment count is asserted.

This theorem is applied in Section 5 to an actual new slab inequality.

### 1.2 account02/B13 diagonal-leaf and three-leaf theorems

Immutable source:

`yspennstate/math-open-problems@04973c0d13c8cbe814f1303b7de8aeffd40791df`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T110032Z-account02-B13-extremal-r25/REPORT.md`.

Let `H={h_1,h_2}` be two original hub coordinates and let `T` be a leaf bank. Put `b_j=A[H,{j}] in R^2`, `B=[b_j]_{j in T}`, `G=BB^T`, `D=det G`, and

`ell_j=b_j^T G^{-1}b_j`, `h=max_j ell_j`.

When the leaf-leaf block on `T` is diagonal and `rank B=2`, the completed theorem gives, for `h<1`,

`||p_Q||_inf <= M(B,h)`,

where

`M(B,h)=D^{-1/4} * 4` if `h<=1/2`,

and

`M(B,h)=D^{-1/4} * 2/((1-h)sqrt(2h))` if `1/2<h<1`.      (1.1)

All hub curvature, outside curvature/couplings, diagonal leaf twists and affine leakage are allowed.

Its three-leaf theorem says that if three selected leaves `j,k,l` have no mutual off-diagonal curvature, then, writing

`Delta=|det(b_j,b_k)|>0`, `b_l!=0`,

one has

`||p_Q||_inf <= C_3 (Delta ||b_l||_2)^(-1/3)`,

`C_3=3*2^(1/6)=3.367386144928...`.                         (1.2)

Again all remaining coordinates and couplings are retained through conditioning.

## 2. Translation-invariant centered support radii

Let `E subset R` be bounded measurable. Define

`rad(E)=inf_c ess sup_{x in E}|x-c|`.

For a bounded finite union this is half the length of its essential convex hull. Choose a center `c_E` attaining this value and write `x=c_E+y`; then `|y|<=rad(E)` on `E`.

This centering is essential. A product set may be translated arbitrarily far, and no estimate below is allowed to pay for its absolute location. Translating a coordinate changes a quadratic polynomial only by the same quadratic coefficients plus affine and constant terms; the completed input theorems explicitly allow those affine terms.

## 3. Near-diagonal leaf transfer on one extreme product set

### Theorem 3.1 — `QFORM-EXTREME-NEARDIAG-LEAF-TRANSFER-v1`

Let every input density be `1_{E_i}` with `|E_i|=1`, each `E_i` a bounded measurable set. Fix two original hub coordinates `H={h_1,h_2}` and a leaf bank `T`, and suppose the cross bank `B=A[H,T]` has rank two and maximum leverage `h<1` as above.

For every leaf `j in T`, put

`r_j=rad(E_j)`,

and define the centered support-scaled off-diagonal leaf currency

`Omega_T(E)=sum_{j<k, j,k in T} |A_jk| r_j r_k`.             (3.1)

Then for every interval `J` of length `L>0`,

`boxed:
 |{x in prod_i E_i : x^T A x in J}|
 <= M(B,h) [L+4 Omega_T(E)].
`                                                                    (3.2)

### Proof

For each `j in T` choose a center `c_j` with `|x_j-c_j|<=r_j` on `E_j`, and put `y_j=x_j-c_j`. Expand every mutual leaf term:

`2 A_jk x_j x_k`
`=2 A_jk y_j y_k +2 A_jk c_k y_j+2 A_jk c_j y_k+2 A_jk c_j c_k`.  (3.3)

Define the auxiliary quadratic-affine polynomial `Q_0` by deleting only the first term `2A_jk y_jy_k` for all `j<k in T`, while keeping the linear and constant terms in (3.3). Thus the leaf-leaf quadratic block of `Q_0` is diagonal. The cross bank `B` is unchanged. Every added linear term is allowed by the source theorem, as are arbitrary couplings to the coordinates outside `H union T`.

On the actual product set,

`|Q-Q_0|`
`<=2 sum_{j<k}|A_jk| r_jr_k`
`=2 Omega_T(E)`.                                                (3.4)

Therefore

`{Q in J} subset {Q_0 in J^{+2 Omega_T(E)}}`,                 (3.5)

where the interval on the right has length `L+4 Omega_T(E)`. Apply (1.1) to `Q_0`. Since `prod_i 1_{E_i}` is a probability density (each `|E_i|=1`), (3.2) follows. QED.

### Consequence

If this product-set slab has ratio

`R_E=|{Q in J} cap prod E_i|/L`,

then necessarily

`boxed:
 Omega_T(E) >= (L/4) (R_E/M(B,h)-1)_+.
`                                                                    (3.6)

Thus a high-density extreme witness with a nonconcentrated two-hub cross bank cannot hide all genuine leaf curvature below the scale of the slab after translations are removed.

This is not a universal perturbative deletion theorem: `rad(E_j)` may be arbitrarily large, exactly as required by the live correction.

## 4. Robust three-leaf curvature graph

The same argument gives a sharper local obstruction that does not require the *exact* zero graph used in the source theorem.

### Theorem 4.1 — `QFORM-EXTREME-THREELEAF-CURVATURE-TRANSFER-v1`

For three distinct leaves `j,k,l`, define

`Omega_jkl(E)=|A_jk|r_jr_k+|A_jl|r_jr_l+|A_kl|r_kr_l`.       (4.1)

Let

`Delta=|det(b_j,b_k)|>0`, `b_l!=0`.

Then for every interval `J` of length `L`,

`boxed:
 |{x in prod E_i : Q(x) in J}|
 <= C_3 (Delta ||b_l||_2)^(-1/3) [L+4 Omega_jkl(E)].
`                                                                    (4.2)

The same estimate holds after any permutation of `(j,k,l)`.

### Proof

Center only the three selected leaf coordinates. Delete their three centered mutual products `2A_uv y_u y_v`, retaining all induced affine and constant terms. Every coupling from a selected leaf to an unconditioned outside coordinate is an allowed affine coefficient after conditioning on the outside coordinates. Hence the resulting auxiliary polynomial falls exactly under the completed three-leaf theorem (1.2).

The deleted part has absolute value at most `2 Omega_jkl(E)` on the product set. Enlarge `J` by that radius and apply (1.2), giving (4.2). QED.

### Corollary 4.2 — `QFORM-SLAB-SCALE-ROBUST-CURVATURE-GRAPH-v1`

For a product-set witness and interval `J` of length `L`, define a graph on leaf coordinates by putting an edge `u~v` exactly when

`|A_uv| rad(E_u) rad(E_v) > L/12`.                              (4.3)

If `j,k,l` are pairwise nonadjacent in this **slab-scale graph**, then `Omega_jkl(E)<=L/4`, and (4.2) gives

`R_E <= 2 C_3 (Delta ||b_l||_2)^(-1/3)`.                       (4.4)

Equivalently,

`boxed:
 |det(b_j,b_k)| ||b_l||_2
 <= (2 C_3/R_E)^3
 =216 sqrt(2) / R_E^3.
`                                                                    (4.5)

This is the robust replacement for an exact-zero leaf-curvature graph. A coefficient may be nonzero and still count as a nonedge when its *actual centered effect on the extreme witness at the tested slab scale* is small.

A useful domination form follows. If

`delta > 2 C_3/R_E = 6*2^(1/6)/R_E`,                            (4.6)

call a leaf `delta`-active when `||b_j||_2>=delta`. If `j,k` are a slab-scale nonedge pair satisfying

`|det(b_j,b_k)|>=delta^2`,                                     (4.7)

then every other `delta`-active leaf is slab-scale adjacent to `j` or to `k`. Otherwise a third active leaf `l` nonadjacent to both would make `j,k,l` pairwise nonadjacent, while

`|det(b_j,b_k)| ||b_l||_2 >=delta^3>(2C_3/R_E)^3`,

contradicting (4.5).

So the remaining high-density off-diagonal survivor is stronger than an abstract nonzero graph: a transverse nonedge pair must dominate all active leaves through edges whose centered contribution is individually larger than `L/12`.

## 5. Designated partner application to arbitrary cap-one laws

Fix `A,J` and arbitrary independent marginal densities `0<=f_i<=1`, `int f_i=1`. Write

`R_f=P(X^TAX in J)/|J|`.

By the designated account04/B13 no-attainment purification theorem, for every `epsilon>0` there exist bounded finite-union sets `E_i` of measure one such that

`R_E >= R_f-epsilon`.                                           (5.1)

Apply Theorems 3.1 and 4.1 to this actual extreme product witness. For example, whenever the chosen two-hub bank has `h<1`,

`Omega_T(E) >= (|J|/4) ((R_f-epsilon)/M(B,h)-1)_+`.             (5.2)

And every slab-scale independent transverse triple satisfies

`|det(b_j,b_k)| ||b_l||_2
 <=216 sqrt(2)/(R_f-epsilon)^3`.                                (5.3)

This is a zero-loss use of the partner theorem at the new inequalities: arbitrary rough cap-one laws are reduced to compact extreme products, but no global support bound, single interval, centered uniform law, or bounded fragment count is asserted.

If the full conjecture is false, then for every `R` there is therefore a bounded finite-union product-indicator witness of ratio `>R` satisfying the robust graph normal form (4.5)-(4.7).

## 6. Combination with the previous B13 localized compiler

The preceding account03/B13 r24 theorem gives, on the same product witness,

`R_E <= L_*/sigma_min(A[I,I])`,

for every original-coordinate triple `I`, where

`L_*=128*2^(1/4)<152.219`.

Hence every high-density extreme witness simultaneously obeys

`boxed:
 sigma_min(A[I,I]) <= L_*/R_E  for every physical triple I,
`                                                                    (6.1)

and the robust leaf-graph constraint (4.5). Thus a divergent counterexample sequence must become both locally principal-triple singular at rate `R^{-1}` and, for every transverse slab-scale independent leaf triple, cross-volume-degenerate at rate `R^{-3}`.

This is a stricter geometric normal form than either statement alone and preserves the original-coordinate product structure throughout.

## 7. Status and first unpaid implication

Proved in this run:

1. `QFORM-EXTREME-NEARDIAG-LEAF-TRANSFER-v1`, the translation-invariant support-scaled extension of the diagonal-leaf aggregate inequality;
2. `QFORM-EXTREME-THREELEAF-CURVATURE-TRANSFER-v1`, the analogous robust extension of the three-leaf theorem;
3. `QFORM-SLAB-SCALE-ROBUST-CURVATURE-GRAPH-v1`, converting the exact leaf zero-graph obstruction into a slab-width quantitative graph with exact constant `216 sqrt(2)`;
4. an actual zero-loss use of account04/B13 purification to force this normal form on any arbitrary-law strict bad witness.

Not proved: a universal bound on `Omega_T(E)/|J|`; the radii can grow with separated fragments, so (3.2) by itself is not a universal density theorem. No near-null term has been deleted uniformly. No continuity conclusion for the original `Q` is obtained by the perturbative comparison.

The next B13 implication is `QFORM-ROBUST-DETSTAR-CURVATURE-GLUE-v1`: combine the determinant-star concentration from account02/B13 with the robust domination graph above and the local-principal near-singularity (6.1). The target is to show that a star survivor cannot simultaneously have (i) all transverse nonedges dominated by slab-scale-large curvature edges, (ii) every physical triple `O(R^{-1})`-singular, and (iii) the pinned higher-order cross volumes small, unless an already-paid grouped-bank/null-bank/ridge certificate fires. A counterexample would instead have to realize all three degeneracies on bounded finite-union product sets.

Continuity of the full target remains a separate open requirement.
