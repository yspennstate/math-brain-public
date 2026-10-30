SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T10:47:49Z.
attacking: the determinant-balanced two-hub near-triangle survivor; turn weighted Pluecker near-triangle concentration into either a chirp-stable physical-pivot payment with a direct O(interval length) bound or a single near-coloop physical leaf.

# fleet01/B09 — near-triangle elimination by chirped-pivot cross volume

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This run closes the weighted near-triangle branch of the determinant-balanced two-physical-hub / diagonal-leaf packet: after the completed two-hub Pluecker smoothing and weighted EKR localization are spliced together, a near-triangle is either paid by a promoted physical pivot whose self-quadratic phase may be arbitrary, or it already contains a single near-coloop/high-leverage physical leaf. Thus the near-triangle geometry is not an independent residual branch.

No projected coordinates are declared independent. All partitions below are literal original-coordinate partitions. No moment, compact-support, connected-support, Gaussian, log-concave, diagonal-basis, pointwise van-der-Corput, arbitrary-joint coarea, worst-fiber density supremum, or small-random-error argument is used. Every positive estimate is a genuine density estimate and hence gives an O(|I|) interval bound with the same coefficient.

## 1. Exact packet and completed inputs

Partition original coordinates into two literal physical hubs `H={h1,h2}`, an active leaf bank `L`, and an arbitrary conditioned outside bank `J`. Assume only for this theorem that the surviving active leaf principal block is diagonal. Its diagonal entries are arbitrary. The physical `2 x 2` hub core, every block involving `J`, and all conditioning-generated affine terms are arbitrary.

Write the actual hub-to-leaf cross rows as

`c_i=(A_{i,h1},A_{i,h2}) in R^2`, `i in L`,

let `C` be the matrix with rows `c_i`, and put

`G=C^T C>0`.                                                    (1.1)

Whiten only this deterministic two-column coefficient frame,

`U=C G^(-1/2)`, so `U^T U=I_2`.                               (1.2)

For `i<j`, define the Pluecker edge weights

`w_ij=det(U_{ij})^2=det(c_i,c_j)^2/det G`.                     (1.3)

Cauchy--Binet gives `sum_(i<j) w_ij=1`. If `S,T` are iid edges with law `w`, put

`rho=P(S cap T=empty)`.                                        (1.4)

The coordinate marginal is exactly the physical-row leverage

`ell_i=sum_(j!=i)w_ij=c_i^T G^(-1)c_i`.                        (1.5)

Three completed source-pinned inputs are used.

1. **fleet02/B09 two-hub Pluecker smoothing**, canonical proof `yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T064043Z-fleet02-B09-QFORM-r13/REPORT.md`: for this diagonal-leaf packet,

`||p_Q||_infinity <= 2 sqrt(e) [rho det G]^(-1/4)`             (1.6)

whenever `rho>0`; the density is continuous and the same coefficient multiplies every interval length. The physical hub core is arbitrary.

2. **fleet03/B09 weighted EKR stability and chirp-stable pivot**, canonical proof `yspennstate/math-open-problems@e6d2395b5b13bf75552b015668177a0270d3e89f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T091354Z-fleet03-B09-QFORM-r27/REPORT.md`. If `0<rho<1/4`, with

`tau=(rho/2)^(1/3)`,                                           (1.7)

either some physical leaf has

`ell_i >= 1-rho-tau`,                                         (1.8)

or some literal physical triangle `T={1,2,3}` has internal Pluecker mass

`t_T=w_12+w_13+w_23 >= 1-rho-tau/(1-tau)`.                    (1.9)

The same report proves that if a physical leaf `i` is promoted as a pivot and the residual hub-to-leaf cross has rank two, then, with

`Delta_i=sqrt(det(G-c_i c_i^T))`,                              (1.10)

one has the chirp-stable estimate

`||p_Q||_infinity
 <= K0 [||c_i|| Delta_i]^(-1/3)`,                              (1.11)

where

`K0=3 e^(1/3) 2^(1/6)=4.6995659439...`.                       (1.12)

The pivot self-phase is arbitrary; in particular its physical diagonal coefficient is free. This estimate is continuous and linear in interval length.

3. **fleet02/B09 exact rho-zero classification**, canonical proof `yspennstate/math-open-problems@0feb5b58d53a266b5df517982780448aa9b6daf5`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T094400Z-fleet02-B09-QFORM-auto11/REPORT.md`: at `rho=0`, the positive Pluecker edge support is exactly a physical star/coloop or a physical triangle. In the star case the coloop row has leverage exactly one.

## 2. New deterministic triangle-to-pivot lemma

### Lemma `QFORM-TWOFRAME-TRIANGLE-PIVOT-VOLUME-v1`

Assume a literal physical triangle `{1,2,3}` has internal Pluecker mass

`t=w_12+w_13+w_23 >=1-delta`,                                 (2.1)

where `0<delta<1/2`. Then either

`max(ell_1,ell_2,ell_3) >=1-2delta`,                           (2.2)

or every internal edge satisfies

`w_12,w_13,w_23 >=delta`.                                      (2.3)

In the second alternative, some physical triangle vertex `i` satisfies

`boxed: ||c_i|| Delta_i >= (delta det G)^(3/4)`.               (2.4)

Consequently the full quadratic form has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= K0 (delta det G)^(-1/4)`,                                 (2.5)

and for every interval `I`,

`boxed:
 P{Q in I} <= K0 (delta det G)^(-1/4)|I|.`                    (2.6)

### Proof

Suppose first that every triangle leverage is `<1-2delta`. Since

`w_13+w_23 <= ell_3`,

we have

`w_12=t-(w_13+w_23) >= t-ell_3 > (1-delta)-(1-2delta)=delta`.

The same cyclic argument proves (2.3).

Put

`d_ij=|det(c_i,c_j)|`.                                         (2.7)

By (1.3) and (2.3),

`d_ij >= sqrt(delta det G)`                                    (2.8)

for all three pairs. After promoting leaf `i`, the residual cross matrix consists of all rows except `c_i`. Its rank-two singular-value product is

`Delta_i=sqrt(det(G-c_i c_i^T))`.                              (2.9)

Cauchy--Binet gives

`Delta_1>=d_23`, `Delta_2>=d_13`, `Delta_3>=d_12`.             (2.10)

Define `R_i=||c_i|| Delta_i`. Multiplying (2.10),

`R_1R_2R_3
 >= ||c_1||||c_2||||c_3|| d_12 d_13 d_23`.                  (2.11)

The elementary area inequalities `d_ij<=||c_i||||c_j||` imply

`||c_1||||c_2||||c_3|| >= (d_12d_13d_23)^(1/2)`.              (2.12)

Therefore

`R_1R_2R_3 >= (d_12d_13d_23)^(3/2)`,                          (2.13)

so for some `i`,

`R_i >= (d_12d_13d_23)^(1/2)
     >= (delta det G)^(3/4)`.                                  (2.14)

In particular the residual cross has rank two. Apply the completed chirp-stable pivot estimate (1.11):

`||p_Q||_infinity
 <=K0 R_i^(-1/3)
 <=K0 (delta det G)^(-1/4)`.                                  (2.15)

Its proof is an L2/Plancherel argument with an arbitrary unimodular pivot chirp, so no pointwise oscillatory decay is being smuggled in. This proves (2.5)-(2.6). QED.

The exponent in (2.5) is scaling-correct: under `A -> sA`, `det G` scales as `s^4`, hence `(det G)^(-1/4)` scales as `|s|^-1`.

## 3. New branch-closure theorem: near-triangle collapses to near-coloop

Fix any numerical cutoff `0<rho_*<1/4` and define

`tau_*=(rho_*/2)^(1/3)`,
`delta_*=rho_*+tau_*/(1-tau_*)`,                               (3.1)

`h_* = min(1-rho_*-tau_*, 1-2delta_*)`,                       (3.2)

and

`C_* = max(2sqrt(e) rho_*^(-1/4), K0 delta_*^(-1/4))`.        (3.3)

### Theorem `QFORM-TWOHUB-NEARTRIANGLE-TO-NEARCOLOOP-v1`

For every two-physical-hub / diagonal-leaf packet satisfying (1.1), exactly one of the following conclusions is available:

**Paid branch.** The full quadratic form has a continuous density and

`boxed: ||p_Q||_infinity <= C_* (det G)^(-1/4)`,               (3.4)

hence

`boxed: P{Q in I} <= C_* (det G)^(-1/4)|I|`                   (3.5)

for every interval `I`.

**Localized survivor.** A literal physical leaf satisfies

`boxed: ell_i >= h_*.`                                         (3.6)

Thus the weighted near-triangle state is not a separate survivor: if it cannot be paid, it becomes a one-row near-coloop/high-leverage state.

### Proof

If `rho>=rho_*`, apply (1.6), giving the first term in (3.3).

Assume `0<rho<rho_*`. Apply weighted EKR stability. In its star alternative,

`ell_i >=1-rho-tau >=1-rho_*-tau_* >=h_*`.                    (3.7)

In its triangle alternative, (1.9) gives `t>=1-delta(rho)`, where

`delta(rho)=rho+(rho/2)^(1/3)/(1-(rho/2)^(1/3)) <=delta_*`.    (3.8)

Apply Lemma 2 with `delta=delta_*`: since `t>=1-delta_*`, either a triangle leverage is at least `1-2delta_*>=h_*`, or (2.5) gives the second term in (3.3).

Finally let `rho=0`. The completed exact classification says the edge support is a star or a triangle. In the star case the coloop has leverage one. In the triangle case `t=1>=1-delta_*`, so Lemma 2 again gives either (3.6) or (3.4). QED.

A useful concrete choice is

`rho_*=10^-6`.                                                 (3.9)

Then

`tau_*=0.00793700525984...`,
`delta_*=0.00800150531259...`,
`h_*=0.9839969893748...`,                                     (3.10)

while

`2sqrt(e)rho_*^(-1/4)=104.2742888436...`,
`K0 delta_*^(-1/4)=15.7132066999...`.                          (3.11)

Therefore the very simple fixed corollary is

`boxed:
 either ||p_Q||_infinity <105 (det G)^(-1/4),
 or some physical leaf has leverage >0.98399.`                 (3.12)

The first alternative has continuous density and the same `<105(det G)^(-1/4)` coefficient times interval length.

This is useful precisely in a determinant-balanced packet: once `det G` has a universal lower bound, every non-near-coloop configuration is already paid with a universal constant. The only remaining cross-frame obstruction is a single source-coordinate row carrying more than 98.39% of one unit of the two-frame leverage budget.

## 4. Latest designated fleet02/B09 result applied to an actual inequality

During this run fleet02/B09 completed `QFORM-GROUPED-ONEHUB-DENSE-HUB-CURVATURE-v1`, canonical source

`yspennstate/math-open-problems@46f88948cb35d25a7b146a31c223ec83ca23d65a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T103752Z-fleet02-B09-QFORM-auto11/REPORT.md`.

Its theorem is: if an original-coordinate split `H union I union J` has rank-one physical cross block `A[H,I]=p c^T`, `||p||=1`, leaf block `A_II=D+lambda vv^T`, and

`Delta=||v||^2||c||^2-<v,c>^2>0`,                             (4.1)

with two-frame Pluecker disjointness mass `rho>0`, then arbitrary same-bank hub curvature `A_HH` is retained exactly and

`||p_Q||_infinity <=3e [rho |lambda| Delta]^(-1/3)`.           (4.2)

The density is continuous and (4.2) also multiplies every interval length.

Apply it to a literal target-valid family with four disjoint flat coefficient groups. Take a hub bank with orthonormal flat vectors `p,w`, a leaf bank with orthonormal flat vectors `c,v`, each flat vector supported on its own group of size `m=25`, and set

`F_25=2<p,X_H><c,X_I> + <v,X_I>^2 + <w,X_H>^2`.               (4.3)

No independence between `<p,X_H>` and `<w,X_H>` is asserted. In the deterministic coefficient basis `{p,c,v,w}`, the matrix is a hyperbolic `[[0,1],[1,0]]` block plus two positive unit squares, so

`spec_nonzero(F_25)={1,-1,1,1}`.                              (4.4)

Thus it satisfies the full three-large-eigenvalue target. Here

`lambda=1`, `Delta=1`, `rho=(24/25)^2=0.9216`.                (4.5)

Substitution in the designated partner theorem gives the actual inequality

`boxed:
 ||p_(F_25)||_infinity
 <=3e(24/25)^(-2/3)
 =8.3798243335...`,                                            (4.6)

and

`boxed:
 P{F_25 in I} <=8.379825 |I|.`                                 (4.7)

This is an explicit use of the newest partner result, not a citation-only dependency. Dense hub curvature `<w,X_H>^2` is kept inside the arbitrary hub phase, and the estimate is obtained by an integrable characteristic-function envelope rather than square-root decoupling.

## 5. What is now unpaid

The diagonal-leaf determinant-balanced two-hub branch is now sharper. Large Pluecker disjointness is paid by fleet02/B09. Small disjointness is near-star or near-triangle by fleet03/B09. The present theorem eliminates the near-triangle alternative: it either pays quantitatively through an actual promoted physical pivot and residual cross volume, or it yields the same near-coloop state as the near-star branch.

Therefore the first B09 debt is now

`QFORM-NEARCOLOOP-GENERAL-LEAFCURVATURE-ROUTING-v1`:

> Starting from one literal physical leaf carrying leverage at least 0.98399 in a determinant-balanced two-hub cross frame, while allowing the full same-side leaf operator to be arbitrary, preserve that row and route the remaining third spectral resource into either (i) the new fleet02/B09 grouped-hub dense-curvature smoother, (ii) a completed cross-volume/ridge/physical-pair/definite/grouped-square exit, or (iii) an exact bounded physical collar. Do not discard the residual cross frame or arbitrary leaf curvature as a small random quadratic perturbation.

This is strictly narrower than the prior “near-star or near-triangle” debt. It also interfaces with the current general-leaf-curvature frontier from fleet02/B09: the only determinant-balanced two-frame localization obstruction left is a single near-coloop physical row.

Full QFORM essential boundedness remains OPEN, and full-target continuity remains OPEN. Continuity is proved on the paid theorem branches above, not for the unrestricted conjecture.

## 6. Integrity / regression checks

- The proof uses only original-coordinate conditioning.
- The triangle lemma is deterministic and uses exact Cauchy--Binet identities.
- The promoted-pivot theorem explicitly tolerates arbitrary pivot self-curvature, so no diagonal coefficient is silently set to zero.
- The residual rank-two cross is certified by a positive physical pair determinant inside the triangle; no good fixed minor is assumed from the three-large-eigenvalue hypothesis.
- No law-uniform pointwise Fresnel decay is used.
- No conditional projection cap is invented; the source theorem uses the proved product-projection caps in its own statement.
- All positive results give density bounds first; interval bounds are obtained by integration of the density, not by squaring or square-root decoupling.
- Scaling check: `det G` is quartic in the matrix scale, so every `(det G)^(-1/4)` bound is homogeneous of degree `-1`, as required.
