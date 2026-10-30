SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T09:07:21Z.
attacking: pay the r31 one-pivot-minor-star alternative by lifting its aggregate minors into an actual two-row original-coordinate cross cut, then route the anchored-E2 sibling through the calibrated ridge theorem.

# fleet03/B08 r33 — minor-star lifting to a genuine two-cross cut

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control at start:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / quantitative inequalities  
**Run:** `20260923T090721Z-fleet03-B08-qform-diffuse-r33`  
**Classification:** `NEW SUPPORTING ANALYTIC PAYMENT + STRUCTURAL ROUTER / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Scope and source-pinned inputs

The full target remains OPEN: for every finite `n`, independent real ORIGINAL coordinates with marginal probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `Q=X^TAX`, or give a target-valid counterexample. Continuity is tracked separately.

No Gaussian, moment, compact-support, connected-support, log-concavity, post-rotation independence, arbitrary-joint coarea, positive conditional projection-height moment, law-uniform pointwise Fresnel decay, one-good-minor selector, or Monte Carlo extremality premise is used.

Immediate predecessor:

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T072549Z-fleet03-B08-qform-diffuse-r31/REPORT.md`.

Its aligned double-nest survivor contains an ACTUAL original-coordinate cross block

`B = [ C  R ]`
`    [ S  N ]`,

with `C=[[a,b],[c0,d]]`, and it proves

`|a| > L/(600 sqrt(3))`.                                            (1.1)

For residual columns `j` and rows `r`, put

`R[:,j]=[x_j,y_j]^T`, `S[r,:]=[s_r,t_r]`,

and define the ACTUAL anchored order-two minors

`W_rj = a n_rj-s_r x_j`,
`U_j  = a y_j-c0 x_j`,
`V_r  = a t_r-b s_r`.                                               (1.2)

The exact Desnanot--Jacobi identity is

`a d_rj = det(C) W_rj-U_jV_r`,                                     (1.3)

where `d_rj` is the corresponding anchored physical `3x3` determinant. The r31 dichotomy is:

**A.** `||W||_F > L^2/270000`,                                      (1.4)

or

**B.** with `u_hat=U/a`, `v_hat=V/a`,

`||u_hat||_2 ||v_hat||_2 > L^2/270000`.                            (1.5)

Completed analytic input used below is fleet03/B09 `QFORM-HALFRIESZ-TWO-CROSS-v1`, canonical source

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260922T184648Z-fleet03-B09-QFORM-r15/REPORT.md`.

For any full quadratic-affine form and any disjoint ORIGINAL-coordinate cut with cross block `T`,

`H_(1/2)(Q):=sup_t E|Q-t|^(-1/2)
 <=8 (sigma_1(T)sigma_2(T))^(-1/4)`                              (1.6)

whenever `rank(T)>=2`. Arbitrary same-side quadratic blocks, affine terms, outside couplings and extra spectrum are retained. The same source proves the characteristic-function envelope

`|phi_Q(t)| <= min(1, 2pi (sigma_1(T)sigma_2(T))^(-1/2)|t|^(-1)).` (1.7)

For branch A I also apply fleet03/B07 `QFORM-E2-RIDGE-HALFRIESZ-COLLAR-v1`, canonical report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T203738Z-fleet03-B07-qform-r17/REPORT.md`.

For an actual physical cross block `M`, if `rank(M)=2`,

`H_(1/2)<=8 E_2(M)^(-1/8)`,                                     (1.8)

and if `rank(M)>=3`, at its effective-rank-two calibrated ridge scale, a one-sided maximum ridge leverage at most `23/24` gives

`H_(1/2)<=79.98514376669046 E_2(M)^(-1/8)`.                     (1.9)

If the ridge gate fails on both sides, that theorem produces a physical row/column double-incident packet `>E_2(M)/2`, followed by its exact edge-versus-two-star dichotomy.

The designated `fleet04/B08` current-QFORM directory was absent at the fresh check, so no designated-partner theorem is fabricated. The compatible completed fleet04 theorem actually applied in Section 4 is fleet04/B18 at

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`,

which gives `||p_(q^TX)||_infinity<=sqrt(2)/||q||_2` for a coefficient vector on an original-coordinate cap-one product bank.

## 2. Main theorem: a one-pivot minor star is already a genuine two-cross certificate

Assume branch B, (1.5). Since

`sqrt(270000)=300sqrt(3)`,                                      (2.1)

at least one of the two normalized stars obeys

`max(||u_hat||,||v_hat||)>L/(300sqrt(3)).`                      (2.2)

Together with (1.1),

`max(||U||,||V||)
 =|a|max(||u_hat||,||v_hat||)
 >L^2/540000.`                                                   (2.3)

Suppose first that `||U||` is the maximum. Let the two physical anchor-row coordinates indexing the rows of `C` be `i,k`, and form the ACTUAL two-row physical cut

`T_row=A[{i,k}, [n]\{i,k}]`.                                    (2.4)

For every residual column `j`, the `2x2` minor of `T_row` using physical columns `{a,j}` is exactly

`det [[A_ia,A_ij],[A_ka,A_kj]]
 =a y_j-c0 x_j
 =U_j`.                                                          (2.5)

Therefore Cauchy--Binet gives

`E_2(T_row)
 =sum_{p<q} det T_row[:,{p,q}]^2
 >=sum_j U_j^2
 =||U||^2.`                                                      (2.6)

Because `T_row` has two rows,

`E_2(T_row)=(sigma_1(T_row)sigma_2(T_row))^2`,                  (2.7)

hence

`boxed: sigma_1(T_row)sigma_2(T_row)>L^2/540000.`               (2.8)

If instead `||V||` is the maximum, symmetry gives the identical conclusion from the two physical anchor-column coordinates `a,b`: for

`T_col=A[{a,b},[n]\{a,b}]`,                                    (2.9)

the minors using columns `{i,r}` are

`det [[A_ai,A_ar],[A_bi,A_br]]=a t_r-b s_r=V_r`,               (2.10)

so again

`boxed: sigma_1(T_col)sigma_2(T_col)>L^2/540000.`               (2.11)

This proves:

### Theorem 2.1 — `QFORM-ONEPIVOT-MINORSTAR-TO-PHYSICAL-TWOCROSS-v1`

Every r31 branch-B state contains an ACTUAL original-coordinate two-row cross cut `T` satisfying

`boxed: sigma_1(T)sigma_2(T)>L^2/540000.`                       (2.12)

No spectral rotation and no selection of one local minor is used; the whole minor star is inserted into the second compound of a physical two-row cut.

Applying (1.6), the **full ambient quadratic form** therefore satisfies

`boxed:
 H_(1/2)(Q)
 <8*540000^(1/4) L^(-1/2)
 =216.864480866363... L^(-1/2)
 <217 L^(-1/2).
`                                                                  (2.13)

Arbitrary same-bank quadratic curvature and every unused coupling are retained. This closes the r31 branch-B debt at the translation-uniform half-Riesz level.

## 3. The same branch has an L3 density, with an explicit bound

The two-cross characteristic-function estimate (1.7) gives more than a fractional potential. Put

`Delta=sigma_1(T)sigma_2(T)`, `K=2pi Delta^(-1/2)`.

Then

`int_R |phi_Q(t)|^(3/2) dt
 <=2[int_0^K 1 dt + K^(3/2)int_K^infinity t^(-3/2)dt]
 =6K.`                                                           (3.1)

Thus

`||phi_Q||_(3/2)<=(6K)^(2/3)`.                                  (3.2)

Hausdorff--Young for the inverse Fourier transform, in the convention

`p(x)=(2pi)^(-1)int e^(-itx)phi(t)dt`,

gives

`||p_Q||_3 <=(2pi)^(-2/3)||phi_Q||_(3/2)
 <=6^(2/3) Delta^(-1/3).`                                       (3.3)

Using (2.12),

`boxed:
 ||p_Q||_3
 <6^(2/3) 540000^(1/3)L^(-2/3)
 =268.884284793430... L^(-2/3)
 <269 L^(-2/3).
`                                                                  (3.4)

Hence branch B is not merely atom-free: it has an explicit `L^3` density. This does **not** imply a universal `L^infinity` bound, and continuity is not claimed from (3.4).

### Zero-anchor-block endpoint

There is a clean stronger endpoint. If the principal `2x2` self block on the winning pair of physical row coordinates is exactly zero, the completed two-anchor coefficient-plane theorem applies to the same actual cut and arbitrary outside curvature. Its bound is

`||p_Q||_infinity <=2sqrt(2) Delta^(-1/2)`.                     (3.5)

Therefore (2.12) gives a continuous `C_0` density with

`boxed:
 ||p_Q||_infinity
 <2sqrt(2)*sqrt(540000)/L
 =1200sqrt(3)/L
 =2078.460969082653.../L.
`                                                                  (3.6)

This endpoint is scoped exactly to a zero `2x2` self block; no nonzero quadratic coefficient is deleted.

## 4. Actual application of completed fleet04 mathematics

The fleet04/B18 projection theorem is applied to the **same r31 resource**, not cited decoratively. From (2.2), the winning normalized one-pivot minor-star vector `q` obeys

`||q||>L/(300sqrt(3))`.

It is a coefficient vector on a genuine original-coordinate residual bank. Hence

`boxed:
 ||p_(q^T X)||_infinity
 <sqrt(2)*300sqrt(3)/L
 =300sqrt(6)/L
 =734.846922834953.../L.
`                                                                  (4.1)

Using the full product reserve (1.5) on the two disjoint residual banks also gives

`boxed:
 ||p_(u_hat^T X, v_hat^T X)||_infinity
 <=2/(||u_hat||||v_hat||)
 <540000/L^2.
`                                                                  (4.2)

These are retained as product-linear provenance bounds. They are not mislabelled as a generic indefinite quadratic pushforward estimate.

## 5. The anchored-W sibling is now routed to a calibrated ridge payment or a stronger coloop reserve

Assume branch A, (1.4). Every `W_rj` is itself an ACTUAL `2x2` physical minor of the inherited cross block `B`:

`W_rj=det B[{i,r},{a,j}]`.                                      (5.1)

Therefore

`E_2(B)>=sum_{r,j}W_rj^2
 >L^4/270000^2.`                                                 (5.2)

Set

`E0=L^4/270000^2.`                                              (5.3)

If `rank(B)=2`, (1.8) gives

`H_(1/2)(Q)<8*270000^(1/4)L^(-1/2)
 =182.360564556382...L^(-1/2).`                                 (5.4)

If `rank(B)>=3` and at least one calibrated ridge side has maximum leverage at most `23/24`, (1.9) gives

`boxed:
 H_(1/2)(Q)
 <1823.266996677134...L^(-1/2)
 <1824L^(-1/2).
`                                                                  (5.5)

Thus the only branch-A state not already paid at the half-Riesz level is the two-sided calibrated ridge-near-coloop state. The exact B07 theorem then produces physical anchors `p,q` carrying double-incident second-compound mass `>E_2(B)/2`, and consequently either

`boxed:
 |b| ||C_res||_F > L^2/(540000sqrt(2)),
`                                                                  (5.6)

or

`boxed:
 ||r||_2 ||c||_2 > L^2/(540000sqrt(2)).
`                                                                  (5.7)

These follow from the source theorem's squared reserve `>E_2(B)/8` and (5.2).

In the two-star alternative define `P=||r||^2||c||^2`. If the corresponding physical checkerboard two-row block has

`E_2(D_check)>=P/16`,

then the completed checkerboard two-cross payment gives the explicit further estimate

`boxed:
 H_(1/2)(Q)<334.450750038578...L^(-1/2)<335L^(-1/2).
`                                                                  (5.8)

Otherwise that source's exact near-leaf conclusion applies: the two checkerboard rows are quantitatively nearly proportional. Hence branch A is reduced to the already-recognized **edge-core** or **near-leaf two-star** geometries, now with the explicit scale (5.6)-(5.7). No claim is made that those final two geometries are yet universally paid.

This proves the supporting router

### Theorem 5.1 — `QFORM-DODGSON-W-BANK-RIDGE-ROUTER-v1`

The r31 anchored-W alternative is either paid by a translation-uniform half-Riesz estimate `<1824L^(-1/2)` (and `<183L^(-1/2)` in exact rank two), or is forced into a physical two-sided near-coloop with the quantitative reserves (5.6)-(5.7); the checkerboard-nondegenerate part of (5.7) is further paid by `<335L^(-1/2)`.

## 6. What changed and what remains

The r31 Desnanot--Jacobi split no longer leaves two equally opaque analytic debts.

* **One-pivot minor-star branch B:** fully converted to a genuine physical two-cross cut. It now has an unconditional full-form half-Riesz bound `<217L^(-1/2)` and an actual `L^3` density `<269L^(-2/3)`. If the winning anchor self block is zero, it has a continuous bounded density `<1200sqrt(3)/L`.
* **Anchored E2 branch A:** moderate-ridge and exact-rank-two states are paid at the half-Riesz level. Only the explicit high-ridge-coloop edge-core / checkerboard-near-leaf states remain.

The unrestricted universal `L^infinity` conjecture remains **OPEN**. The first B08 implication is now narrower:

`QFORM-DODGSON-HIGHCOLOOP-DENSITY-LIFT-v1` — in the branch-A two-sided ridge-coloop state, combine the edge-core reserve (5.6) or the checkerboard near-leaf geometry from failure of (5.8) with a third product-preserving curvature source to obtain an `L^infinity` bound, without conditioning away the original-coordinate product structure.

Global continuity also remains OPEN; continuity is asserted only in the zero-anchor-block endpoint (3.6) and previously paid continuous subbranches.

## 7. Verification

`CHECKS.py` verifies on 1,000 seeded symmetric integer matrices that `U_j`, `V_r`, and `W_rj` are exactly the claimed physical `2x2` minors of the two-row cuts / inherited cross block. It also checks all displayed numerical constants. The output terminates

`QFORM_B08_R33_CHECK_PASS`.

Repository transport is not native learned-memory ingestion. Status remains `WITHOUT_VERIFIED_BRAIN`.
