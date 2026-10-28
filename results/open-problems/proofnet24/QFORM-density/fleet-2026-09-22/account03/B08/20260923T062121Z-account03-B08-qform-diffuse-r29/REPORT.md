SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T06:21:21Z.
attacking: optimize the anchored order-3/order-2 self-matched law up to its exact 2/3 occupancy barrier, then feed the resulting nested packet into the newest physical-link and residual-core compilers without selecting a tiny local minor.

# account03/B08 r29 — variable-mixture 2/3 barrier and nested-packet core router

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / quantitative inequalities  
**Run:** `20260923T062121Z-account03-B08-qform-diffuse-r29`  
**Classification:** `NEW SUPPORTING ANALYTIC THEOREM + STRONGER DIFFUSE ROUTER / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Target and source discipline

The unrestricted target remains OPEN: for arbitrary finite dimension, independent real ORIGINAL coordinates with probability densities bounded by one, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite essential-density bound for `Q=X^TAX`, or give a valid counterexample. Continuity is a separate requested conclusion.

No moment, Gaussian, log-concave, compact-support, connected-support, iid, spectral-coordinate-independence, law-uniform scalar Fresnel-decay, arbitrary-joint coarea, positive conditional projection-height moment, fiber-supremum, or one-good-minor hypothesis is used.


The immediate predecessor is

`yspennstate/math-open-problems@af8d585f3ac8b3cc243045caf6bbe65d8e956f99`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T052144Z-account03-B08-qform-diffuse-r28/REPORT.md`.

Its theorem `QFORM-MIXED-ORDER-JENSEN-COMPILER-v1` will be used exactly at its proved scope. The live co-heavy correction is respected throughout: aggregate determinant currency is not converted into one universal-size physical minor before an aggregate compiler is applied.

Two newly completed neighboring structural sources are also used at theorem level:

1. account03/B07 r25, canonical source reported as
   `yspennstate/math-open-problems@5e2f0ed9c6f5b7621d6344af21b13a05234fdd47`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T053905Z-account03-B07-qform-r25/REPORT.md`,
   proving `QFORM-NESTED-THIRDVOLUME-TO-DISJOINT-LINKS-v1`.
2. account03/B07 r26, observed at
   `yspennstate/math-open-problems@67a8e05e237bc914ad0563e361f6eb035b76e7fe`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T060629Z-account03-B07-qform-r26/REPORT.md`,
   proving `QFORM-NESTED-CORE-R1-E2-VOLUME-OR-BICORE-v1`.

The designated `account04/B08` current-QFORM handoff directory was checked fresh and remained absent. No result is fabricated for that slot. A compatible completed account04/B18 product-projection consequence is applied quantitatively in Section 6.

## 2. Incoming anchored packet

Use the exact setup already proved in B08 r27-r28. A physical ORIGINAL-coordinate cross block `B` has a fixed row anchor `i` and column anchor `a`. Let

`Z = sum_(R,C) det B[{i} union R,{a} union C]^2 > 0`,              (2.1)

where `R,C` range over residual physical pairs. Let `w3` be the normalized determinant-square law on those anchored order-three minors. For residual physical rows `k != i`, put

`alpha_k=P_w3(k in R)`, `sum_(k!=i) alpha_k=2`,                    (2.2)

and let

`h=max_(k!=i) alpha_k`.                                           (2.3)

Write `R_i=||B[i,:]||_2` for the anchor-row star norm.

B08 r27 constructed an order-two physical-minor law `v2*` with the SAME residual-row marginals `alpha_k` and entropy-determinant currency

`K(v2*) >= Z/R_i^2`,                                               (2.4)

while

`K(w3)=Z`.                                                         (2.5)

The order-two law contains no anchor row `i`; the order-three law contains it always.

The diffuse `q=0` route already proved upstream gives either a continuous branch `<77/L`, or an anchored packet satisfying

`Z > L^6/6912`.                                                    (2.6)

This run starts from the latter branch.

## 3. New theorem: arbitrary mixture weight and the exact 2/3 barrier

For `0<theta<1`, define the self-matched mixed-order law

`Omega_theta = theta w3 + (1-theta) v2*`.                         (3.1)

Because the supports have different minor orders, they are disjoint.

### Theorem 3.1 — `QFORM-ANCHORED-VARIABLE-MIXTURE-v1`

For every `theta in (0,1)`, the law `Omega_theta` has

`kbar = E|S| = 2+theta`,                                         (3.2)

anchor-row marginal

`alpha_i(Omega_theta)=theta`,                                    (3.3)

and every residual-row marginal remains exactly

`alpha_k(Omega_theta)=alpha_k`.                                  (3.4)

Its entropy-determinant currency satisfies

`boxed:
 K(Omega_theta)
 >= Z R_i^(-2(1-theta))
    theta^(-theta)(1-theta)^(-(1-theta)).
`                                                                    (3.5)

Consequently, if `q>=1`,

`max(theta,h)<=q/2`,                                               (3.6)

and

`2+theta>2q`,                                                      (3.7)

then the FULL ambient quadratic form, retaining arbitrary same-bank quadratic terms, outside couplings and induced affine terms, has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <= e q^(-1/2) (2+theta)/(2+theta-2q)
    Z^(-1/(2(2+theta)))
    R_i^((1-theta)/(2+theta))
    [theta^theta(1-theta)^(1-theta)]^(1/(2(2+theta))).
`                                                                    (3.8)

#### Proof

Equations (3.2)-(3.4) are immediate because the order-three component has order three and contains the anchor, while the order-two component has order two, excludes the anchor, and was constructed to reproduce the residual row marginals.

For disjoint supports the mixture entropy decomposes exactly:

`H(Omega_theta)
 = H_Bern(theta)+theta H(w3)+(1-theta)H(v2*)`.                    (3.9)

Likewise the expectation of `log det^2` is the same convex combination. Therefore

`K(Omega_theta)
 = theta^(-theta)(1-theta)^(-(1-theta))
   K(w3)^theta K(v2*)^(1-theta)`.                               (3.10)

Insert (2.4)-(2.5):

`K(Omega_theta)
 >= theta^(-theta)(1-theta)^(-(1-theta))
    Z^theta (Z/R_i^2)^(1-theta)`,                               (3.11)

which is (3.5).

Now apply B08 r28 `QFORM-MIXED-ORDER-JENSEN-COMPILER-v1`. Its hypotheses are exactly (3.6)-(3.7), and its coarse estimate is

`||p_Q||_infinity
 <= e q^(-1/2) kbar/(kbar-2q)
    K(Omega_theta)^(-1/(2kbar)).`                               (3.12)

Substituting `kbar=2+theta` and (3.5) gives (3.8). The inherited Fourier proof has an `L^1` characteristic-function majorant, so the density is continuous and vanishes at infinity. QED.

### Corollary 3.2 — every occupancy strictly below 2/3 is payable by this family

If

`1/2 <= h < 2/3`,                                                (3.13)

choose

`theta=h`, `q=2h`.                                               (3.14)

Then `max(theta,h)=h=q/2`, while

`2+theta-2q = 2-3h >0`,                                         (3.15)

so (3.8) applies.

For `h<=1/2`, the predecessor choice `theta=1/2,q=1` applies. Thus every fixed `h<2/3` is analytically payable by a finite constant.

### Proposition 3.3 — `2/3` is the exact barrier of this two-order self-matched mechanism

Suppose one insists on using only a mixture (3.1) and the r28 mixed-order Jensen compiler while preserving the residual marginals `alpha_k`. If `h>=2/3`, there are NO parameters `theta in (0,1)`, `q>=1` satisfying both the marginal gate and strict integrability.

Indeed the marginal gate forces

`q >= 2 max(theta,h)`.                                          (3.16)

If `theta<=h`, then strict integrability would require

`2+theta > 2q >=4h`,                                           (3.17)

but `2+theta<=2+h<=4h` for `h>=2/3`, contradiction. If `theta>h>=2/3`, then `q>=2theta`, so

`2+theta > 2q >=4theta`                                        (3.18)

would force `theta<2/3`, again a contradiction.

This is a limitation of the present order-3/order-2 self-matched compiler, NOT a counterexample to QFORM. It identifies exactly where the next mechanism must change.

## 4. Fixed universal certificate at occupancy 16/25

For the universal proof tree one cannot let a constant diverge as `h` approaches `2/3`, so fix

`eta=16/25`, `theta=16/25`, `q=32/25`.                          (4.1)

Then

`kbar=66/25`,
`kbar-2q=2/25`,
`kbar/(kbar-2q)=33`.                                            (4.2)

Assume the incoming diffuse anchored packet (2.6), the non-large-star condition

`R_i<=L`,                                                        (4.3)

and

`h<=16/25`.                                                      (4.4)

Equation (3.8) and the scale identity

`-6/[2(66/25)] + (1-16/25)/(66/25) = -1`                       (4.5)

give

`||p_Q||_infinity < C_16/25 / L`,                               (4.6)

where

`C_16/25
 = e (32/25)^(-1/2) 33
   6912^(25/132)
   [(16/25)^(16/25)(9/25)^(9/25)]^(25/132)`                    (4.7)

and the checker gives

`C_16/25 = 373.8140962624... <374`.                              (4.8)

Thus:

`boxed: h<=16/25 and R_i<=L  ==>  ||p_Q||_infinity<374/L,`       (4.9)

with a continuous `C_0` density.

If (4.9) fails while `R_i<=L`, then some residual physical row `k` has `alpha_k>16/25`. The complete one-sided nested packet containing rows `i,k` and column anchor `a` therefore satisfies

`P=alpha_k Z > (16/25)(L^6/6912)
  = boxed(L^6/10800).`                                           (4.10)

This improves the preceding B08 threshold `L^6/11520` while retaining aggregate determinant currency.

The transposed argument gives the same row/column statement. In particular, if both row- and column-oriented `16/25` branches fail on the SAME anchored law, then there are a residual row `k` and column `b` with conditional inclusion probabilities both `>16/25`; the union bound gives their simultaneous inclusion probability `>7/25`, hence the fixed double-nested packet obeys

`boxed:
 sum_(ell,c) det B[{i,k,ell},{a,b,c}]^2
 > 7 L^6/172800.
`                                                                    (4.11)

No local `3x3` determinant is extracted from (4.10) or (4.11).

## 5. Feed the stronger one-sided packet into B07 r25 and r26

Assume the row-side survivor (4.10). If the heavy residual row itself has

`R_k=||B[k,:]||_2 > L`,                                          (5.1)

retain it as a large-star resource and go to Section 6. Otherwise

`R_i<=L`, `R_k<=L`.                                              (5.2)

Apply account03/B07 r25 `QFORM-NESTED-THIRDVOLUME-TO-DISJOINT-LINKS-v1` to the literal packet `P` in (4.10). Since

`sqrt(P) > L^3/sqrt(10800)=L^3/(60sqrt(3))`,                    (5.3)

one of the following holds.

### S — three disjoint linear banks

There are three coefficient vectors on mutually disjoint ORIGINAL-coordinate banks with

`boxed:
 ||c||_2 ||w_1||_2 ||w_2||_2
 > sqrt(P)/6
 > L^3/(360sqrt(3)).
`                                                                    (5.4)

### E — edge-star-core

There is a physical scalar edge, a disjoint physical star and a residual physical cross core `N` such that

`boxed:
 |edge| ||star||_2 ||N||_F
 > sqrt(P)/(6sqrt(2))
 > L^3/(360sqrt(6)).
`                                                                    (5.5)

Under (5.2), whichever anchor edge/star wins r25 satisfies

`|edge|<=L`, `||star||_2<=L`,                                    (5.6)

because both are subobjects of the two physical anchor rows. Hence (5.5) forces the dimension-free residual-core floor

`boxed:
 G:=||N||_F > L/(360sqrt(6)).
`                                                                    (5.7)

Now apply the newly completed B07 r26 quadrichotomy to this ACTUAL core `N`.

**VOL.** The full ambient quadratic form is continuously paid by

`||p_Q||_infinity < (27e/2)G^(-1)
 <4860 e sqrt(6)/L
 =32359.8408001.../L
 < boxed(32360/L).`                                               (5.8)

**R1.** The unresolved core is an honest relative rank-one tube:

`dist_F(N,{rank<=1})<G/2`.                                       (5.9)

The outer edge-star packet (5.5) remains present; no tail is deleted.

**E2.** The residual core has aggregate second-compound currency

`E_2(N)>=3G^4/16
 > boxed(L^4/(192*360^4))`,                                     (5.10)

and r26's physical coloring gives four disjoint subbanks with a matched Frobenius-product reserve

`P_match>=3G^4/256
 > boxed(L^4/(3072*360^4)).`                                   (5.11)

**BICORE.** There are a physical row and a physical column of `N` with norms each exceeding

`sqrt(2/27)G
 > sqrt(2/27) L/(360sqrt(6))
 = boxed(L/3240).`                                               (5.12)

Thus the previous undifferentiated nested packet has been reduced to a paid continuous branch or one of three quantitatively rigid product-preserving survivors: a relative rank-one tube, an aggregate E2/four-bank packet, or a two-sided physical core with explicit star scale.

## 6. Completed account04 mathematics applied to actual inequalities

A fresh check found no completed `account04/B08` current-QFORM artifact. I therefore do not attribute any theorem to the designated slot.

Use instead the compatible completed account04/B18 sharp product-projection consequence from

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`:
for every nonzero coefficient vector `u` supported on an ORIGINAL-coordinate cap-one product bank,

`||p_(u^T X)||_infinity <= sqrt(2)/||u||_2`.                    (6.1)

This is the sharp-Rogozin/Ball product-projection consequence used by neighboring completed workers.

First, every large-star alternative `R_j>L` yields the actual inequality

`boxed: ||p_(r_j^T X)||_infinity < sqrt(2)/L.`                   (6.2)

Second, on the B07 r25 S-branch (5.4), the three supports are disjoint original-coordinate banks, hence the three projections are genuinely independent. Multiplying (6.1) gives

`||p_(c^T X_R,w_1^T X_C1,w_2^T X_C2)||_infinity
 <= 2sqrt(2)/(||c|| ||w_1|| ||w_2||)
 < boxed(720sqrt(6)/L^3)`                                      (6.3)

with numerical coefficient `1763.6326148...`.

Equation (6.3) is retained as product-linear provenance currency; a bounded three-dimensional projection density is NOT being promoted to a generic indefinite quadratic-pushforward bound. That distinction is required by the live corrections.

## 7. What changed and first unpaid implication

The order-3/order-2 anchored Fourier mechanism is now completely optimized with respect to its mixing weight: it pays every fixed occupancy below `2/3`, and `2/3` is proved to be the exact barrier of that mechanism. A fixed universal threshold `16/25` gives a clean `<374/L` continuous branch and strengthens the nested packet to `P>L^6/10800`.

More importantly, the newly completed B07 r25-r26 compilers convert that stronger packet into an explicit downstream proof tree. Apart from large stars, one obtains either

1. a full continuous bound `<32360/L`;
2. three disjoint linear banks with product norm `>L^3/(360sqrt(3))` and joint cap `<720sqrt(6)/L^3`;
3. a nested edge-star plus relative-1/2 rank-one core tube;
4. an aggregate residual E2/four-bank reserve at the exact scales (5.10)-(5.11); or
5. two-sided physical core stars each `>L/3240`.

The first unpaid B08 implication is therefore no longer “consume an arbitrary three-anchor packet.” It is

`QFORM-DIFFUSE-POST-2/3-CORE-RECEIVER-v1`:
consume branches 2-5 above in the FULL ambient form, retaining arbitrary unused anchor couplings and same-bank curvature. The next run must change mechanism rather than further tune the same order-3/order-2 mixture, because Proposition 3.3 proves that mixture cannot cross the `2/3` occupancy barrier.

The unrestricted QFORM conjecture remains OPEN / not proved / not disproved. Global continuity remains OPEN. Continuity is proved on (4.9) and (5.8), not on the remaining structural survivors.

## 8. Finite arithmetic checker

`CHECKS.py` and `CHECKS.txt` beside this report verify all exact rational thresholds and displayed numerical constants, including `C_16/25<374`, `P>L^6/10800`, the B07 link constants, the partner joint cap, the double-nested `7/172800` coefficient, the `<32360/L` VOL constant, and the exact BICORE simplification `L/3240`.

These finite computations are regression evidence only; the substantive inequalities above are proved symbolically.
