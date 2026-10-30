SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T04:23:03Z.
attacking: consume the diffuse q=0 double-incident third-volume packet directly, before deshearing into one edge plus residual E2, by a self-matched mixed 3-minor/2-minor Fourier law.

# fleet03/B08 r27 — anchored third-volume self-matched 3/2 mixture

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `NEW CONTINUOUS PAID BRANCH + SHARPER STAR/NEST ROUTER / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source discipline

The unrestricted target remains open: independent ORIGINAL real coordinates with one-dimensional densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, iid, log-concavity, spectral-coordinate independence, law-uniform pointwise Fresnel decay, arbitrary-joint coarea bound, conditional projection-height moment, or one-good-minor principle is used.


The immediate B08 predecessor is

`yspennstate/math-open-problems@74d0a2e9069b79a331c8a0b304f1772901f16b32`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T032334Z-fleet03-B08-qform-diffuse-r26/REPORT.md`.

Its diffuse q=0 route starts from the r25 Pluecker packet

`Delta3(B)>=L^6/2304`

for an ORIGINAL-coordinate cross block `B=A[I,J]`. Applying the completed fractional-volume theorem at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`,

with `q=4/3` gives either a continuous branch `||p_Q||inf<77/L`, or physical anchors `i in I`, `a in J` for which the double-incident third-volume mass

`Z:=sum_{R subset I\{i}, |R|=2} sum_{C subset J\{a}, |C|=2}
      det B[{i} union R,{a} union C]^2`

satisfies

`Z>L^6/6912`.                                                      (1.1)

The predecessor then desheared this packet into `|b|sqrt(E2(D))` or a four-bank packet. The present run changes mechanism: it spends `Z` itself before that split.

The analytic engine is the completed mixed-order physical-minor Brascamp--Lieb/Fourier theorem

`yspennstate/math-open-problems@86f318f0826325e6df3504e1e8ec15f4316cc861`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T001242Z-b01-qform-auto11/REPORT.md`.

For any probability law `Omega` on nonzero square physical minors of an original-coordinate cross block, if every row inclusion marginal is at most `1/2` and the mean minor order `kbar>2`, it proves a continuous `C0` density with

`||p_Q||inf <= 2sqrt(e) kbar/(kbar-2) K(Omega)^(-1/(2kbar))`,       (1.2)

where

`K(Omega)=exp(E_Omega log det(M_ST)^2 + H(Omega))`.                (1.3)

All same-side quadratic terms, conditioned outside couplings, and induced affine terms remain present.

## 2. The anchored natural third-minor law

Assume `Z>0` in (1.1). Define the natural anchored third-minor law

`w3(R,C)=det B[{i} union R,{a} union C]^2/Z`.                       (2.1)

For every residual row `k in I\{i}`, let

`alpha_k=P_w3(k in R)`.                                             (2.2)

Because every draw selects exactly two residual rows,

`sum_(k!=i) alpha_k=2`.                                             (2.3)

The determinant-squared law has exact entropy-determinant currency

`K(w3)=Z`.                                                          (2.4)

Let `r_i` denote the entire physical row of `B` at anchor `i`, and set

`R_i=||r_i||_2`.                                                    (2.5)

Since `Z>0`, `R_i>0`.

## 3. New theorem: self-match the row-pair distribution by physical 2-minors

### Theorem 3.1 — `QFORM-ANCHORED-THREEVOLUME-SELF-MATCHED-MIX-v1`

If

`max_(k!=i) alpha_k <=1/2`,                                        (3.1)

then the FULL ambient quadratic form has a bounded continuous density and

`boxed:
 ||p_Q||inf <= 10sqrt(e) (2Z/R_i)^(-1/5).
`                                                                     (3.2)

The identical theorem holds after transposing `B`, with the anchor column norm and residual column inclusion marginals.

### Proof

For an unordered residual row pair `R={j,k}`, put

`W_R=sum_C det B[{i} union R,{a} union C]^2`,                      (3.3)

so the row-pair distribution under `w3` is

`eta_R=W_R/Z`.                                                      (3.4)

Let

`D_R=sum_{|U|=2} det B[R,U]^2
    =||r_j wedge r_k||_2^2`,                                       (3.5)

where the sum is over all physical column pairs of the same cross block. Since the terms in `W_R` are only a subset of the coordinates of the full exterior vector `r_i wedge r_j wedge r_k`,

`W_R <= ||r_i wedge r_j wedge r_k||_2^2
     <= R_i^2 ||r_j wedge r_k||_2^2
     =R_i^2 D_R`.                                                   (3.6)

Thus whenever `eta_R>0`, `D_R>0` and

`D_R >= eta_R Z/R_i^2`.                                            (3.7)

Construct a physical order-two minor law `v2*` as follows: draw the residual row pair `R` with law `eta`; conditional on `R`, draw a physical column pair `U` with probability

`det B[R,U]^2/D_R`.                                                 (3.8)

Its residual row marginals are exactly the same `alpha_k` as in `w3`. Moreover

`log K(v2*)
 =H(eta)+sum_R eta_R log D_R
 >=H(eta)+sum_R eta_R log(eta_R Z/R_i^2)
 =log(Z/R_i^2)`,                                                    (3.9)

because `H(eta)=-sum eta_R log eta_R`. Hence

`K(v2*)>=Z/R_i^2`.                                                  (3.10)

Now mix BEFORE any reciprocal minor is selected:

`Omega=(1/2)w3+(1/2)v2*`.                                          (3.11)

The two supports have different orders, so their supports are disjoint. The anchor row `i` has `Omega`-marginal exactly `1/2`; every residual row `k` has marginal

`(1/2)alpha_k+(1/2)alpha_k=alpha_k<=1/2`.                          (3.12)

The mean order is

`kbar=(3+2)/2=5/2`.                                                (3.13)

The binary mixing entropy gives

`K(Omega)=2 sqrt(K(w3)K(v2*))
          >=2Z/R_i`.                                                (3.14)

Apply (1.2) with `kbar=5/2`. Since

`2sqrt(e)*(5/2)/(1/2)=10sqrt(e)`,                                  (3.15)

we obtain exactly (3.2). The mixed-order theorem gives `phi_Q in L1`, hence a continuous `C0` representative. QED.

This proof uses only physical minors and original-coordinate product structure. No spectral rotation of random coordinates occurs.

## 4. Explicit diffuse q=0 payment: a new `<85/L` branch

Return to the diffuse q=0 packet (1.1). If

`R_i<=L`                                                           (4.1)

and the anchored residual row marginals satisfy (3.1), then Theorem 3.1 gives

`||p_Q||inf
 <10sqrt(e) [2(L^6/6912)/L]^(-1/5)
 =10sqrt(e) 3456^(1/5)/L
 =84.1127801341.../L
 <85/L`.                                                           (4.2)

This branch has a continuous `C0` density.

The same conclusion holds if the anchor COLUMN norm is at most `L` and all residual column marginals of `w3` are at most `1/2`, by applying Theorem 3.1 to `B^T`.

Thus the predecessor's anchored q=0 survivor has a substantially earlier analytic exit: no scalar-edge deshearing and no residual `E2` estimate are needed when the anchored third-volume law remains diffuse on either physical side.

## 5. What failure of the new branch forces

If the row-oriented `<85/L` branch fails, then at least one of the following is true:

1. `R_i>L`; or
2. there is a residual physical row `k` with `alpha_k>1/2`.

In case 2 the fixed three-anchor packet has mass

`sum_{R contains k,C}
 det B[{i} union R,{a} union C]^2
 =alpha_k Z
 >Z/2
 >L^6/13824`.                                                      (5.1)

Likewise, failure of the column-oriented branch forces either the anchor column norm `C_a>L` or a residual physical column carrying more than `Z/2>L^6/13824` of the anchored third-volume law.

Hence, after the already-paid `<77/L` fractional-volume exit, every remaining diffuse q=0 state obeys the two-sided router:

**on the row side:** large physical star norm `>L` OR a residual row nested packet `>L^6/13824`;

**on the column side:** large physical star norm `>L` OR a residual column nested packet `>L^6/13824`.

This is stronger structural information than merely knowing that a third-volume leverage gate failed.

## 6. Completed fleet04 result applied to an actual inequality

A fresh repository search still finds no completed current-QFORM artifact under the designated `fleet04/B08` path, so no designated-partner theorem is fabricated.

The compatible completed fleet04/B18 product-projection theorem is recorded at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`

(with source graph pin `ce50e74f705c49f66524aa6565d4aa4a9be88061`). Its one-dimensional consequence is

`||p_(u^T X)||inf <=sqrt(2)/||u||_2`                               (6.1)

for every nonzero coefficient vector on an original-coordinate product bank.

Apply (6.1) to the actual anchor row projection

`Y_i=r_i^T X_J`.                                                    (6.2)

On the large-row-star survivor `R_i>L`,

`boxed: ||p_(Y_i)||inf <sqrt(2)/L.`                                (6.3)

Similarly the large-column-star survivor gives an original-coordinate projection `Z_a` on bank `I` with the same cap. If BOTH star norms exceed `L`, the banks `I` and `J` are disjoint, so these two projections are genuinely independent and

`boxed: ||p_(Y_i,Z_a)||inf <2/L^2.`                                (6.4)

Equation (6.4) is a genuine partner-result application to the new router. It is retained as product-linear currency; it is NOT promoted to a generic indefinite quadratic pushforward bound.

## 7. Relation to the previous hub/E2 split

The r26 deshearing theorem remains valid and useful. Its anchored-hub branch says, after the same double-incident event,

`|b|sqrt(E2(D))>L^3/(96sqrt(3))`,                                  (7.1)

or else a four-bank packet occurs. The new theorem is logically upstream of (7.1): it attempts payment directly from the anchored determinant law `w3` before cancellation is split into a scalar edge and residual pair volume.

Therefore a future proof can now enter the expensive hub/E2 or four-bank machinery only after the following simpler possibilities have been excluded:

- the fractional-volume continuous branch `<77/L`;
- the new self-matched anchored-volume continuous branch `<85/L` from either side;
- a large physical row/column star carrying the projection cap (6.3)-(6.4).

What then remains has a fixed nested third-volume packet of size `>L^6/13824` on every non-large-star side. This is exactly the aggregate-before-localization form needed for a next mixed-order iteration.

## 8. Continuity, open scope, and next implication

Theorem 3.1 and the `<85/L` diffuse corollary prove **bounded continuous `C0` density** in their stated branches. This is stronger than essential boundedness there.

The full universal QFORM conjecture remains **OPEN / not proved / not disproved**. Global continuity remains open.

The next B08 implication is now narrower: consume a three-anchor packet of mass `>L^6/13824` (or the mixed large-star + nested state) by a second self-matched mixed-order law, without selecting one local determinant and without discarding same-bank curvature. The older hub/E2 and four-bank routes remain available in parallel.

## 9. Arithmetic check

`CHECKS.py` and `CHECKS.txt` beside this report verify the exact q=4/3 anchor scale, the `<85/L` constant, the `1/13824` nested threshold, and the partner projection caps. The checker terminates `QFORM_B08_R27_CHECK_PASS`.
