SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T04:30:13Z.
attacking: the exact singular-physical-pair corner of the scalar-Schur tri-hub survivor, by converting a zero Schur self coefficient into an original-matrix anchored star certificate and compressing the exact zero-star case product-preservingly.

# account01/B13 auto15 — singular-pair anchored two-volume and proportional-row product compression

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Extremal product laws / STRUCTURE  
Status: **ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING TARGET-LEVEL STRUCTURAL THEOREMS / FULL QFORM OPEN / CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-valid inputs

The target remains: independent original-coordinate real variables `X_i` with probability densities `0<=f_i<=1`, real symmetric `A`, and at least three eigenvalues of `A` of absolute value at least one. Prove a universal essential-density bound for `Q=X^T A X`, or exhibit a valid counterexample. No moment, support, centering, iid, log-concavity, finite-fragment, or post-rotation-independence hypothesis is made.

Fresh owner control remained QFORM-only, revision `2026-09-22.15`. The live correction set is respected. In particular, nothing below uses law-uniform pointwise quadratic oscillatory decay, arbitrary-joint 3D coarea, a positive moment of a worst conditional projection density, bounded-diameter localization, a fixed fragment count, deletion of a small quadratic coefficient on unbounded supports, or independence after rotating the source.

Three completed inputs are used at their exact scopes.

1. **Designated partner account02/B13 r23**, canonical report
   `yspennstate/math-open-problems@892bfe36756e09cbaff3f05070f7a3e20fea0fd1`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T040105Z-account02-B13-extremal-r23/REPORT.md`.
   It proves the no-attainment extremal-product front end: every cap-one marginal is an `L^1` limit of finite convex mixtures of indicators of bounded finite unions of intervals of measure one, so every fixed slab inequality transfers with zero asymptotic constant loss. It also proves `QFORM-SCALAR-E2-LINF-OR-TRIHUB-v1`: after a nonzero scalar pivot, an aggregate Schur `E_2` bank is either paid or more than half of its natural pair-volume is jointly incident to at most three physical row hubs and at most three physical column hubs.

2. **Curvature-robust zero-self star theorem**, account02/B07, canonical report commit
   `yspennstate/math-open-problems@beafed16f383ac6853be8caa902acb3d12a40702`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T223302Z-account02-B07-QFORM-ddc6a5/REPORT.md`.
   If `S=S^T`, `S_ii=0`, and `ell=(S_ij)_{j!=i}` is nonzero, then for the quadratic remainder in independent cap-one original coordinates,

   `H_{1/2}(R):=sup_t E|R-t|^{-1/2} <= (16/sqrt(3)) ||ell||_2^{-1/2}`.     (1.1)

   Arbitrary complementary quadratic curvature is retained.

3. **Sharp one-dimensional product-projection cap**, source-pinned in account04/B18 at
   `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.
   A normalized linear form of independent cap-one variables has density cap at most `sqrt(2)` (the sharp Rogozin/Juskevicius--Lee consequence used by the fleet).

The standard physical scalar-square peel, already source-pinned in the fleet, is also used: if `d=A_hh!=0` and `S` is the scalar Schur complement, then

`||p_Q||_infinity <= |d|^{-1/2} H_{1/2}(X_{-h}^T S X_{-h}).`             (1.2)

This conditions only on original independent coordinates.

## 2. Exact singular-pair geometry

Fix two distinct original coordinates `h,i` and assume

`d=A_hh !=0`.                                                         (2.1)

Write the scalar Schur complement after pivoting coordinate `h` as

`S=A_{-h,-h}-A_{-h,h}A_{h,-h}/d`.                                    (2.2)

The principal pair determinant is

`Delta_hi := det A[{h,i},{h,i}] = d A_ii-A_hi^2 = d S_ii`.            (2.3)

Thus the exact singular-principal-pair condition

`Delta_hi=0`                                                          (2.4)

is **exactly** the zero-self condition `S_ii=0` required by the completed zero-star theorem. No perturbative replacement of a small nonzero value is made.

For every `j notin {h,i}`, define the bordered physical minor

`B_{hi;j}:=det A[{h,i},{h,j}]`
`          = d A_ij-A_ih A_hj`
`          = d S_ij`.                                                 (2.5)

Define the aggregate anchored two-volume

`Sigma_{h,i}(A):=sum_{j notin {h,i}} B_{hi;j}^2`.                    (2.6)

By (2.5),

`boxed: Sigma_{h,i}(A)=d^2 sum_{j notin {h,i}} S_ij^2.`              (2.7)

This is an exact original-matrix identity. It aggregates the whole physical star before taking any reciprocal coefficient.

## 3. Main theorem: a singular physical pair plus anchored star pays in L-infinity

### Theorem 3.1 — `QFORM-SINGULAR-PAIR-ANCHORED2-LINF-v1`

Assume (2.1) and the exact singular-pair condition (2.4). If

`Sigma_{h,i}(A)>0`,                                                   (3.1)

then for arbitrary independent cap-one input laws,

`boxed:
||p_(X^T A X)||_infinity
 <= (16/sqrt(3)) Sigma_{h,i}(A)^(-1/4).
}`                                                                     (3.2)

Numerically, the coefficient is

`16/sqrt(3)=9.237604307034...`.                                      (3.3)

No assumption is imposed on the remaining spectrum, signs, same-side curvature, support fragmentation, or translations.

### Proof

Complete the square in the original scalar coordinate `X_h`:

`Q=d (X_h + d^{-1} A_{h,-h} X_{-h})^2 + R`,

`R=X_{-h}^T S X_{-h}`.                                               (3.4)

By (2.3)-(2.4), `S_ii=0`. By (2.7), the full off-diagonal row of `S` at coordinate `i` has Euclidean norm

`r_i := (sum_{j notin {h,i}} S_ij^2)^(1/2)
      = Sigma_{h,i}(A)^(1/2)/|d|`.                                  (3.5)

Condition (3.1) is exactly `r_i>0`. Apply the completed curvature-robust zero-self theorem (1.1):

`H_{1/2}(R) <= (16/sqrt(3)) r_i^(-1/2).`                             (3.6)

Now apply the original-coordinate scalar-square peel (1.2):

`||p_Q||_infinity
 <= |d|^(-1/2) (16/sqrt(3)) r_i^(-1/2)`
` = (16/sqrt(3)) (|d| r_i)^(-1/2)`
` = (16/sqrt(3)) Sigma_{h,i}(A)^(-1/4),`                             (3.7)

because `|d| r_i=Sigma_{h,i}^{1/2}`. This proves (3.2). QED.

### Homogeneity check

Under `A -> sA`, every bordered `2x2` determinant scales by `s^2`, hence `Sigma` scales by `s^4`; the right side of (3.2) therefore scales by `|s|^{-1}`, exactly as an output density should.

### Why this is complementary to the preceding B13 certificates

The preceding scalar anchored-four-volume theorem needed a nonzero scalar pivot and residual third exterior volume. The preceding pair anchored-five-volume theorem paid an invertible indefinite physical pair. Theorem 3.1 instead targets the exact **singular** physical pair. Its currency is only an aggregate star of bordered `2x2` minors. Thus the invertible-pair and singular-pair endpoints now have different source-valid payments rather than being connected by an invalid small-determinant continuity argument.

## 4. Actual geometric product-set inequality and partner application

Take arbitrary measurable sets `E_k subset R` with `|E_k|=1`; their indicators are admissible cap-one densities. Theorem 3.1 immediately yields, for every interval `J`,

`boxed:
|{x in product_k E_k : x^T A x in J}|
 <= (16/sqrt(3)) Sigma_{h,i}(A)^(-1/4) |J|.
}`                                                                     (4.1)

The sets may be disconnected, arbitrarily translated, and have arbitrarily many components.

Now apply the designated partner account02/B13 r23 **at the counterexample level**. Its exact/no-attainment product purification says that if a fixed matrix and slab violate a proposed uniform constant within the full cap-one product class, then, with arbitrarily small loss, the violation is witnessed by a product of indicators of bounded finite unions of intervals of measure one. Therefore Theorem 3.1 is not merely a statement about smooth or interval laws: throughout the singular-pair branch the exact B13 geometric slab supremum obeys (4.1), and every hypothetical bad-witness sequence in this branch must satisfy the quantitative collapse below.

If a slab witness has ratio

`R = P{Q in J}/|J|`,                                                (4.2)

then (3.2) implies the necessary condition

`boxed:
Sigma_{h,i}(A) < (16/(sqrt(3) R))^4
               = (65536/9) R^(-4).
}`                                                                     (4.3)

Thus a diverging product-indicator witness sequence cannot retain any fixed amount of singular-pair anchored two-volume.

For the finite-grid normalization used in the preceding B13 bad-witness route, where `R_m>C_3 m` with `C_3=9 sqrt(3e)`, (4.3) becomes

`boxed:
Sigma_{h,i}(A_m) < 0.016690 m^(-4)
}`                                                                     (4.4)

for every exact singular principal pair anchored at a nonzero physical diagonal. The rounded decimal is outward-safe relative to the exact coefficient `(16/(sqrt(3) C_3))^4=0.0166892150...`.

## 5. The exact zero-currency endpoint is algebraic, not analytic: global proportionality

The case `Sigma_{h,i}=0` has a rigid exact meaning.

### Lemma 5.1 — `QFORM-SINGULAR-PAIR-ZEROSTAR-PROPORTIONAL-v1`

Under (2.1) and (2.4), if

`Sigma_{h,i}(A)=0`,                                                  (5.1)

then the entire physical rows (and columns) are proportional:

`boxed: A_{i,*}=c A_{h,*},  A_{*,i}=c A_{*,h},  c=A_ih/d.`           (5.2)

Equivalently,

`e_i-c e_h in ker A`.                                                (5.3)

### Proof

For `j notin {h,i}`, (2.5) and (5.1) give `dA_ij-A_ihA_hj=0`, hence `A_ij=cA_hj`. At column `h`, this is the definition of `c`. At column `i`, the singular principal determinant gives

`A_ii=A_ih^2/d=c A_hi`.

Thus every coordinate of row `i` equals `c` times the corresponding coordinate of row `h`; symmetry gives the column statement. QED.

This endpoint should therefore be compressed, not attacked by a reciprocal tiny determinant.

## 6. Product-preserving simultaneous compression of proportional row classes

The following structural reduction is useful beyond a single pair.

### Theorem 6.1 — `QFORM-PROPORTIONAL-ROW-PRODUCT-COMPRESSION-v1`

Partition the nonzero physical rows of a real symmetric matrix `A` into their maximal proportionality classes `C_1,...,C_m`; discard identically zero rows. Then there exist

- an `n x m` matrix `U` with orthonormal columns, each column supported on one class;
- a symmetric `m x m` matrix `B=U^T A U`;
- independent random variables `Y_alpha=U_{C_alpha}^T X_{C_alpha}`,

such that

`boxed: A=U B U^T,  X^T A X=Y^T B Y,`                              (6.1)

and the nonzero eigenvalues of `B` are exactly the nonzero eigenvalues of `A`.

Moreover every `Y_alpha` has density cap at most `sqrt(2)`. Hence, putting

`Z=sqrt(2) Y`,                                                     (6.2)

all `Z_alpha` are independent with density caps at most one and

`boxed: 2 X^T A X = Z^T B Z.`                                    (6.3)

Therefore any slab witness of ratio `R` for `(A,X)` produces an `m`-dimensional target-valid cap-one product-law witness for `B` with slab ratio exactly `R/2`. In particular, a sequence with `R -> infinity` remains a divergent counterexample sequence after compressing **all** proportional classes at once.

If desired, applying the designated partner account02/B13 finite-mixture purification to the independent cap-one variables `Z_alpha` produces, with arbitrarily small additional loss, a lower-dimensional witness whose marginals are indicators of bounded finite unions of intervals of measure one.

### Proof

For each class `C_alpha`, choose a representative nonzero row and scalars `c_i` such that every row in the class is `c_i` times the representative. Let `u_alpha` be the vector supported on `C_alpha` with entries proportional to these `c_i` and normalized to Euclidean norm one. The vectors `u_alpha` have disjoint supports, so they are orthonormal; assemble them as the columns of `U`.

For every vector `x`, the coordinates of `Ax` inside one class are proportional to the class coefficient vector. Hence

`range(A) subset range(U)`.                                       (6.4)

Since `A` is symmetric, it vanishes on `range(U)^perp`, and therefore

`A=UU^T A UU^T=U(U^T A U)U^T=UBU^T`.                            (6.5)

The orthogonal decomposition `range(U) plus range(U)^perp` now shows that the nonzero spectrum of `A` is exactly the spectrum of `B` with any extra zeros removed.

Next,

`Y_alpha=u_alpha^T X_{C_alpha}`.                                  (6.6)

The classes use disjoint original-coordinate sets, so the `Y_alpha` are genuinely independent. Each coefficient vector `u_alpha` has norm one. The sharp one-dimensional product-projection theorem therefore gives

`||p_{Y_alpha}||_infinity <= sqrt(2)`.                             (6.7)

Equation (6.1) follows directly from (6.5). Scaling `Z_alpha=sqrt(2)Y_alpha` gives density cap at most one and

`Y^T B Y=(1/2) Z^T B Z`,                                         (6.8)

which is (6.3).

For an interval `J`,

`P{Z^T B Z in 2J}=P{X^T A X in J}`,                              (6.9)

while `|2J|=2|J|`; the slab ratio is therefore `R/2`. Because `B` has the same nonzero eigenvalues as `A`, the three-large-eigenvalue hypothesis is preserved **exactly** for the rescaled output `2Q`. QED.

### Consequence for irreducible counterexample searches

Without loss for a divergent counterexample sequence, one may first perform Theorem 6.1 and assume that no two nonzero physical rows are globally proportional. This is an exact product-law reduction, not a rotation-independence claim: the only new variables are linear aggregates on **disjoint original-coordinate classes**, and their one-dimensional laws are controlled before any further argument.

Combining this with Lemma 5.1, in such a proportionality-reduced witness the zero-star case `Sigma_{h,i}=0` cannot occur for an exact singular pair with `A_hh!=0`.

## 7. Apply the newest designated-partner tri-hub theorem to the new certificate

Let `d=A_hh!=0`, let `S` be the scalar Schur complement, and let `M=S[I,J]` be a disjoint physical cross block with

`E=e_2(M^T M)>0`.                                                  (7.1)

Apply account02/B13 r23, Theorem `QFORM-SCALAR-E2-LINF-OR-TRIHUB-v1`. Either

`||p_Q||_infinity <= 29.922421174319 |d|^(-1/2) E^(-1/8),`      (7.2)

or more than half of the natural squared `2x2`-minor mass is jointly incident to a row-hub set `H` and a column-hub set `K` with

`|H|<=3, |K|<=3`.                                                  (7.3)

This run pays an exact portion of that second branch. If any hub coordinate `i in H union K` satisfies

`S_ii=0` and `Sigma_{h,i}(A)>=eta>0`,                              (7.4)

then Theorem 3.1 gives the actual inequality

`boxed: ||p_Q||_infinity <= (16/sqrt(3)) eta^(-1/4).}`           (7.5)

For a slab witness of ratio `R`, every exact-zero-self hub in the surviving tri-hub branch must therefore satisfy

`Sigma_{h,i}(A) < (16/(sqrt(3)R))^4`.                             (7.6)

If equality is replaced by `Sigma_{h,i}=0`, Theorem 6.1 compresses the resulting globally proportional class and retains a target-valid divergent product witness with only the universal ratio factor `1/2` loss.

Thus the partner's first unpaid `SCALAR-E2-TRIHUB-STAR` state has been sharpened: after proportionality compression, its genuinely new content is concentrated in

1. hub coordinates with **nonzero** Schur self-curvature, or
2. exact-zero-self hubs whose positive anchored two-volume tends to zero at the forced `R^{-4}` rate.

No claim is made that a small positive `Sigma` may be deleted or replaced by zero; the live no-continuity correction forbids that shortcut.

## 8. What remains

The full QFORM conjecture is still **OPEN / NOT PROVED**. The new results close the exact singular-pair/noncollapsed-star endpoint and replace the exact zero-star endpoint by a product-preserving dimension compression. They do not control a near-singular but nonzero principal determinant, nor do they turn a merely small anchored star into an exact proportionality relation.

The sharpened B13 implication is

`QFORM-TRIHUB-NONZEROSELF-OR-VANISHING-ANCHORED2-CLOSURE-v1`:

> In the scalar-Schur `E_2` tri-hub survivor, aggregate the finitely many nonzero-self hub coordinates together with any exact-zero-self hubs whose anchored two-volume is positive but forced to vanish along a bad-witness sequence. Either obtain one of the paid pair / E2 / D5 / mixed-hub receivers before taking reciprocal coefficients, or construct a genuine bounded-finite-union product-indicator counterexample sequence. Do not perturb a small self coefficient to zero and do not rotate the product source and assert independence.

The separate all-zero-physical-diagonal chamber, where no nonzero scalar pivot exists at all, remains to be joined through the already-developed zero-hubpair / pair-anchored / pure-bipartite / grouped-bank mechanisms.

## 9. Arithmetic checks

The constants used above are

`16/sqrt(3)=9.237604307034013...`,

`(16/sqrt(3))^4=65536/9=7281.777777...`,

and, with `C_3=9sqrt(3e)`,

`(16/(sqrt(3) C_3))^4=0.016689215025176...`.

All determinant and compression identities in Sections 2, 5 and 6 are exact algebra; no numerical experiment is used as proof.

## 10. Source status

- Full QFORM: **OPEN**.
- Continuous-density conclusion for full QFORM: **OPEN**.
- Theorem 3.1: proved here conditional only on previously completed zero-self star and square-peel inputs at their stated scopes.
- Theorem 6.1: self-contained exact structural proof here, plus the completed normalized linear-form density cap.
- Independent end-to-end review of this run: not yet supplied.
- Native learned-memory receiver use: not observed; status remains `WITHOUT_VERIFIED_BRAIN`.
