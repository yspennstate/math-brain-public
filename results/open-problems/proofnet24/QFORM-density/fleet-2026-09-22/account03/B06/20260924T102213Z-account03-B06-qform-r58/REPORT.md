SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T10:22:13Z.
attacking: the r57 large-diagonal / heavy-child obstruction by proving that diagonal cancellation with no physical pivot and no fixed star forces a near-coloop; peel all such coordinates at once, retain the third spectral scale, and re-enter the diffuse curved receiver without a dimension-growing fiber supremum.

# account03/B06 r58 — large-diagonal cancellation forces a finite near-coloop peel

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.
OWNER CONTROL at prepublication refresh: `2026-09-22.15`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Status: **new supporting structural/compiler theorem + partner-backed curved inequalities; full QFORM remains OPEN**.

Fresh correction inbox SHA at publication preparation: `ba7aeac3d879f59da5ec8a12daad74ea85714465`. The proof below does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, conditional projection caps, post-rotation independence, deletion of a nonzero random tail, or unrestricted fiber suprema.

## 1. Incoming live packet

The immediate B06 source is r57:

`yspennstate/math-open-problems@511e54eba7610a8bf2b8ac58c86b99179d66442c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T093325Z-account03-B06-qform-r57/REPORT.md`.

Inside its exact global-null localized packet, deleting one literal hub coordinate leaves a product-preserving child quadratic matrix `C` with

` s_3(C) >= 1/3. `                                                   (1.1)

The child has the form

` C = D + R, `                                                       (1.2)

where `D` is diagonal in the surviving ORIGINAL coordinates and `rank R <= 3`.  If `||D||op <= 1/6`, r57 already shows that either a whitened rank-three frame is diffuse and the completed separable-phase theorem pays the full scalar density, or there are at most five leverage-heavy physical coordinates.  Its open branch was therefore the literal `|D_qq|>1/6` certificate, together with the finite heavy-frame branch.

The diffuse theorem used below is the completed `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, canonical source

`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`.

The all-sign physical scalar-pivot theorem used below is

`yspennstate/math-open-problems@1d81e62c818d6b592a6a6da78870f12f533d615a`

`proofnet24/QFORM-density/interactive/20260923T192150Z-all-sign-scalar-pivot/REPORT.md`.

The designated account04/B06 source actually applied in Section 6 is

`yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260924T001014Z-account04-B06-QFORM-r3/REPORT.md`,

theorem `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`.

## 2. Exact row identity behind diagonal cancellation

Let more generally

` C = D + V M V^T, `                                                 (2.1)

where `D` is diagonal, `V` has orthonormal columns, `M=M^T`, and

` r := rank V <= 3. `                                                 (2.2)

No invertibility of `M` is required in this section.  For an original coordinate `q`, write

` v_q = V^T e_q,  alpha_q = ||v_q||^2, `

` r_q = e_q^T V M V^T e_q = v_q^T M v_q, `

and let

` c_q = (V M V^T)_{q,q^c} = C_{q,q^c}. `                             (2.3)

The final equality uses diagonality of `D`.

### Lemma 2.1 — `QFORM-DIAGCANCEL-CROSS-LEVERAGE-v1`

For every `q`,

` ||c_q||_2^2 = ||M v_q||_2^2 - r_q^2, `                             (2.4)

and hence, whenever `r_q != 0`,

` ||c_q||_2 >= |r_q| sqrt((1-alpha_q)/alpha_q). `                    (2.5)

#### Proof

Since `V^T V=I`, deleting the `q`th physical row gives

` V_{q^c}^T V_{q^c}=I-v_q v_q^T. `

Therefore

` ||c_q||^2
 = v_q^T M V_{q^c}^T V_{q^c} M v_q
 = ||M v_q||^2-(v_q^T M v_q)^2, `

which is (2.4).  Cauchy--Schwarz gives

` r_q^2 <= ||v_q||^2 ||M v_q||^2 = alpha_q ||M v_q||^2. `

Substitution into (2.4) gives (2.5).  No probability argument is used. `QED`.

This identity is the relevant weighted replacement: the amount by which a large diagonal separable coefficient can be cancelled by the rank-three core is tied to the **entire physical cross-star norm**, weighted by the physical leverage.  No individual tiny minor is inverted.

## 3. Fixed-scale cancellation dichotomy

Set

` delta = 1/6,      tau = eta = 1/96. `                              (3.1)

Suppose a coordinate `q` obeys

` |D_qq| > delta,   |C_qq| < tau,   ||C_{q,q^c}||_2 < eta. `          (3.2)

Then

` |r_q| = |C_qq-D_qq| > delta-tau = 5/32. `                          (3.3)

Applying (2.5),

` sqrt((1-alpha_q)/alpha_q)
 < (1/96)/(5/32)=1/15. `                                             (3.4)

Thus

` boxed: alpha_q > 225/226. `                                        (3.5)

Because

` sum_q alpha_q = tr(VV^T)=r <= 3, `                                 (3.6)

there can be at most three coordinates satisfying (3.2).

This is the key new implication: **large separable curvature which almost cancels the actual scalar pivot and also produces no fixed cross-star is necessarily a literal near-coloop of the entire rank-at-most-three physical carrier.**

## 4. `QFORM-LARGEDIAG-NEARCOLOOP-PEEL-v1`

Assume (1.1)--(1.2): `s_3(C)>=1/3`, `C=D+R`, `rank R<=3`.

Then at least one of the following alternatives holds.

### (A) Paid actual scalar pivot

There is an original coordinate `q` with

` |D_qq|>1/6,   |C_qq|>=1/96. `                                     (4.1)

The all-sign scalar-pivot theorem applies to the **actual** child matrix `C`, with `sigma=1/3`, and gives

` boxed: ||p_Q||_infinity <= C_* sqrt(288), `                         (4.2)

where

` C_* = 1.391402171... x 10^9. `                                    (4.3)

Numerically the displayed constant is below `2.3623 x 10^10`.  The bound is uniform in every conditioning value used to create the child, so it pays the parent scalar law.  This is an essential-boundedness conclusion; that source theorem does not assert continuity.

### (B) Fixed original-coordinate cross-star

There is an original coordinate `q` with

` |D_qq|>1/6,   |C_qq|<1/96,   ||C_{q,q^c}||_2>=1/96. `              (4.4)

This is a dimension-free physical star certificate in the **complete child matrix**, not merely in an auxiliary low-rank approximation.  It is not claimed here to solve the whole scalar law; Section 6 shows how the designated curved partner absorbs its tangential part without a reciprocal star coefficient.

### (C) At most three near-coloops may be peeled, after which the diagonal is small

If neither (A) nor (B) occurs, let

` H={q: |D_qq|>1/6}. `                                               (4.5)

Every `q in H` satisfies (3.2), so

` |H|<=3,   alpha_q>225/226. `                                      (4.6)

Condition on the ORIGINAL variables indexed by `H`, equivalently pass to the literal principal child

` C_L=C[H^c,H^c]. `                                                  (4.7)

Product structure is preserved.  We now quantify exactly how much of the third spectral scale can be lost.

For one coordinate `q`, write the current symmetric matrix in the physical split `q | q^c` as

` [[a,c^T],[c,B]]. `

Replacing it by `0 direct_sum B` changes it by

` E=[[a,c^T],[c,0]]. `                                               (4.8)

Its operator norm is exactly

` ||E||op = (|a|+sqrt(a^2+4||c||^2))/2. `                            (4.9)

For every `q in H`, even after earlier members of `H` have been deleted, the diagonal is unchanged and the surviving cross norm can only decrease.  Hence

` ||E||op < kappa_0 := (1+sqrt(5))/192
                    = 0.0168545207161... . `                         (4.10)

Weyl's singular-value inequality applied successively at most three times gives

` boxed:
  s_3(C_L) >= sigma_* := 1/3 - 3 kappa_0
  = (61-3 sqrt(5))/192
  = 0.282769771184899... . `                                         (4.11)

By definition of `H`,

` ||D_L||op <= 1/6. `                                                 (4.12)

Consequently the surviving low-rank core `R_L=C_L-D_L` satisfies

` s_3(R_L) >= sigma_0 := sigma_* - 1/6
 = (29-3 sqrt(5))/192
 = 0.116103104518232... . `                                          (4.13)

Since `rank R_L<=3`, (4.13) forces `rank R_L=3`.  Thus write

` R_L=U K U^T,   U^T U=I_3, `                                       (4.14)

and all three singular values of `K` are at least `sigma_0`, so

` |det K| >= sigma_0^3. `                                            (4.15)

If the whitened physical three-frame is diffuse,

` max_j ||U_{j,*}||^2 <= 1/2, `                                     (4.16)

then `QFORM-DIFFUSE-SEPARABLE-PHASE-v1` applies with the complete diagonal `D_L` and every conditioning-induced affine term retained.  It gives a continuous `C_0` density satisfying

` boxed:
 ||p_Q||_infinity
 <= 3e |det K|^(-1/3)
 <= 3e/sigma_0
 < 70.238. `                                                         (4.17)

If (4.16) fails, the obstruction is finite: since the leverage sum is three, there are at most five original coordinates with leverage strictly greater than `1/2`.

### Proof of the trichotomy

If some coordinate with `|D_qq|>1/6` has `|C_qq|>=1/96`, we are in (A).  Otherwise all large-diagonal coordinates have small actual pivots.  If any of them has cross norm at least `1/96`, we are in (B).  If none does, every large-diagonal coordinate satisfies (3.2), so Lemma 2.1 gives (4.6).  The deletion estimate (4.8)--(4.13) and the rank-three/diffuse argument then give (C). `QED`.

The point is that the former r57 `||D||op>1/6` obstruction is no longer an unstructured large diagonal: it either pays immediately, creates a fixed physical star, or consists of at most three near-coloops which can be removed **once** while preserving a quantitative third singular value.  No scale-losing indefinite recursion is needed.

## 5. A curved full-fold weighted replacement from product structure

The following auxiliary lemma is useful whenever one of the physical square resources exposed above is disjoint from a diffuse curved two-frame.  It also records explicitly how to integrate an ellipse rather than take a fiber maximum.

### Lemma 5.1 — `QFORM-PRODUCT-ELLIPSE-FULLFOLD-v1`

Let `S`, `{q}`, and `R` be disjoint original-coordinate banks.  Let `w,v in R^S` be orthonormal and satisfy

` w_i^2+v_i^2 <= 1/2  (i in S). `                                    (5.1)

Put

` L=<w,X_S>,   V=<v,X_S>,   Z=X_q. `                                (5.2)

Let `B_R` be arbitrary and measurable in `X_R`.  For constants `lambda,a !=0` of the same sign, arbitrary real `alpha,gamma,beta`, and arbitrary centers, consider

` Y=lambda(V-v_0)^2 + a(Z-z_0)^2
    + beta(alpha L+gamma V+B_R)+c. `                                 (5.3)

Then the joint law of `(L,Y)` has an essentially bounded density and

` boxed: ||p_{L,Y}||_infinity <= 4 pi / sqrt(|lambda a|). `           (5.4)

The same conclusion holds if the center `z_0` is allowed to depend measurably on `X_R`.

#### Proof

The designated account04/B06 proof establishes, under (5.1), the product-Fourier / geometric-Brascamp--Lieb estimate

` ||p_{L,V}||_infinity <=4. `                                        (5.5)

Complete the `V` square in (5.3) and use the determinant-one output shear

` (l,y) -> (l,y-beta alpha l-constant). `                            (5.6)

Condition on `X_R`.  The shift of `Z` is harmless because `Z` is an original independent coordinate with density at most one.  Hence the conditional joint source density of `(L,V,Z)` is at most four.  For fixed `l`, integrate the entire curved fiber rather than its supremum.  With `lambda,a>0`,

` integral_{R^2} delta(s-lambda v^2-a z^2) dv dz
  = pi/sqrt(lambda a) `                                              (5.7)

for `s>0`; reflection gives the same value when both coefficients are negative.  Multiplying (5.7) by the source cap four proves (5.4).  Finally averaging in the disjoint `R` bank only translates the second output and cannot increase the essential supremum. `QED`.

This is precisely a weighted curved-fiber replacement: the complete ellipse is integrated with its Jacobian and the physical product density cap, rather than bounded by a fiberwise maximum.  The same-sign hypothesis is essential for this full-fold statement; an unrestricted hyperbolic fiber has the familiar logarithmic obstruction.

## 6. Actual designated partner splice

The designated account04/B06 theorem is `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`.  In the r57/r58 rank-two tail-plane geometry, any shared affine statistic lying in the physical tail carrier has the form

` B_S=alpha L+gamma V. `                                             (6.1)

Conditioning the at-most-three near-coloops from alternative (C) merely changes `alpha,gamma` and adds a source-disjoint remainder `B_R`; it does not create a new spectral direction in that two-plane.

Therefore, whenever the two-frame obeys (5.1), the partner theorem applies to the **actual** post-peel off-fold section

` Y=lambda(V-v_0)^2+beta(alpha L+gamma V+B_R)+c. `                   (6.2)

At the live radius `r=1/64`, it gives

` boxed: ||g_off||_infinity <= 256/|lambda|. `                       (6.3)

This inequality is uniform in the tangential leakage coefficients, so the near-coloop conditioning introduces no reciprocal leakage cost.  When a disjoint same-sign physical square is also available, Lemma 5.1 upgrades the curved payment across the fold to (5.4).

I do **not** promote (6.3) through an arbitrary same-bank diagonal quadratic phase: that is outside the partner theorem's scope.  The remaining cross-star branch (B) is therefore narrowed to a genuinely non-tangential/shared-curvature or finite-heavy-core compiler, not declared solved.

## 7. Constants and deterministic checks

The exact constants used above are

` alpha_min = 225/226 = 0.995575221238938... `

` kappa_0=(1+sqrt(5))/192 = 0.0168545207161447... `

` sigma_*=(61-3sqrt(5))/192 = 0.282769771184899... `

` sigma_0=(29-3sqrt(5))/192 = 0.116103104518232... `

and

` 3e/sigma_0 = 70.23796236298... . `                                (7.1)

The committed checker verifies (2.4) on random orthonormal carriers, the algebraic threshold `alpha>225/226`, the exact norm formula (4.9), and the numerical constants.  Those computations are diagnostics only; the proof above is exact.

## 8. What is closed and what remains

**Proved in this run.**

1. `QFORM-DIAGCANCEL-CROSS-LEVERAGE-v1`: exact leverage/cross-star identity (2.4)--(2.5).
2. `QFORM-LARGEDIAG-NEARCOLOOP-PEEL-v1`: the r57 large-diagonal branch is reduced exhaustively to an already-paid actual pivot, a fixed physical cross-star of norm at least `1/96`, or at most three near-coloops whose one-shot deletion preserves `s_3 >=0.2827`; the resulting small-diagonal diffuse branch has continuous density `<70.238`.
3. `QFORM-PRODUCT-ELLIPSE-FULLFOLD-v1`: a product-weighted full ellipse integration gives `4 pi/sqrt(|lambda a|)` for a diffuse curved two-frame plus one disjoint same-sign physical square.
4. The account04/B06 tangential shared-leakage theorem is applied to the actual post-peel off-fold inequality (6.3).

**Still open.**

The full QFORM conjecture is not proved.  Inside this B06 packet the remaining finite obstructions are now:

- the fixed cross-star branch `||C_{q,q^c}||_2>=1/96` when it is not entirely tangential to a paid curved plane;
- the at-most-five heavy rows of the final rank-three whitened child;
- interaction of those finite physical resources with arbitrary same-bank diagonal curvature without deleting any nonzero coefficient tail.

The next B06 target is therefore

`QFORM-FIXEDSTAR-HEAVY5-PAIRWEIGHT-COMPILER-v1`:

aggregate the fixed star and the at-most-five heavy rows before selecting a reciprocal physical pair, and route either a two-sided star mass or a same-sign curved square through Lemma 5.1 / existing half-Riesz receivers while preserving the complete diagonal phase.

**Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.  Global continuity: OPEN.**  Continuity is proved only on the diffuse branch (4.17); the scalar-pivot and general cross-star branches above do not establish it.
