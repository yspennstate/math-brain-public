SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T09:39:49Z.
attacking: collapse the entire r31/r33 Dodgson split into unconditional physical E2 currency, then extract a full-form L2-density and half-Riesz estimate without ridge or leverage gates.

# fleet03/B08 r34 — Dodgson split collapses to unconditional pair-volume

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / quantitative inequalities  
**Run:** `20260923T093949Z-fleet03-B08-qform-diffuse-r34`  
**Status:** `NEW SUPPORTING ANALYTIC THEOREMS / PREVIOUS HIGH-COLOOP HALF-RIESZ DEBT CLOSED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source pins

The unrestricted target remains OPEN. Inputs are independent ORIGINAL coordinates with one-dimensional densities bounded by one; no moment, support, log-concavity, Gaussian, iid, post-rotation-independence, arbitrary-joint coarea, pointwise law-uniform Fresnel decay, fiber supremum, or one-good-minor premise is used.


The exact algebraic input is B08 r31:

`yspennstate/math-open-problems@5283f320ecb1386e9210a8d2588c2bf8219dd32c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T072549Z-fleet03-B08-qform-diffuse-r31/REPORT.md`.

The immediate predecessor is B08 r33:

`yspennstate/math-open-problems@6f8e99aec5b12f0e3a5f13d60e7da490ce491647`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T090721Z-fleet03-B08-qform-diffuse-r33/REPORT.md`.

The unconditional aggregate pair-volume half-Riesz theorem used below is fleet01/B01:

`yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T030821Z-fleet01-B01-qform-auto11/REPORT.md`.

For every literal physical cross block `M` of an otherwise arbitrary full quadratic-affine form,

`H_(1/2)(Q):=sup_s E|Q-s|^(-1/2)
 <= C_E2 E_2(M)^(-1/8)`,                                      (1.1)

where

`C_E2=12*2^(5/6)*e^(5/24)=26.334046180759735...`.              (1.2)

Arbitrary same-bank quadratic curvature and outside couplings are retained.

For one step in the new L2 theorem I also use the completed fleet03/B09 two-cross characteristic envelope already applied by r33: if an actual two-row physical cross cut `T` has `Delta=sigma_1(T)sigma_2(T)>0`, then

`|phi_Q(t)| <= min(1,2*pi*Delta^(-1/2)|t|^(-1))`.              (1.3)

## 2. Incoming exact Dodgson geometry

In the r31 aligned double-nest survivor, after physical permutations only, the actual cross block has anchor

`C=[[a,b],[c,d]]`, `delta=ad-bc`,                              (2.1)

with residual rows/columns and the actual physical 2x2 minors

`W_rj = a n_rj-s_r x_j`,
`U_j  = a y_j-c x_j`,
`V_r  = a t_r-b s_r`.                                           (2.2)

For the anchored 3x3 determinant `d_rj`, r31 proves exactly

`a d_rj = delta W_rj-U_jV_r`.                                  (2.3)

Its quantitative triangle split, before the later weakening used in r33, is the stronger exhaustive dichotomy

`|delta| ||W||_F > L^4/270000`,                                (2.4)

or

`||U||_2 ||V||_2 > L^4/270000`.                                (2.5)

The key observation of this run is that **every factor in (2.4)-(2.5) is already part of the same physical second-compound sum**. No ridge argument is needed.

## 3. Main deterministic theorem: the whole Dodgson survivor has fixed E2

Let

`E_2(B)=sum_(|R|=|T|=2) det B[R,T]^2`.                          (3.1)

The anchor determinant `delta` is one literal `2x2` minor. Every `W_rj` is a literal minor using the pivot row/column and residual row/column. Every `U_j` and every `V_r` is likewise a literal anchored `2x2` minor. These index families are distinct subsets of the complete sum (3.1).

### Theorem 3.1 — `QFORM-DODGSON-E2-COLLAPSE-v1`

Every r31 aligned double-nest survivor satisfies

`boxed: E_2(B) > L^4/135000.`                                   (3.2)

#### Proof

If (2.4) holds, then

`E_2(B) >= delta^2+||W||_F^2
         >=2|delta| ||W||_F
         >2L^4/270000
         =L^4/135000.`                                         (3.3)

If (2.5) holds, then

`E_2(B) >= ||U||_2^2+||V||_2^2
         >=2||U||_2||V||_2
         >L^4/135000.`                                         (3.4)

This is exhaustive. QED.

This aggregation is correction-safe: there is no selected reciprocal minor, no coordinate rotation, no Schur-tail deletion, and no rank or leverage assumption.

### Consequence 3.2 — unconditional half-Riesz payment

Apply (1.1) directly to the actual full-form cross block `B` and (3.2):

`boxed:
 H_(1/2)(Q)
 < C_E2 * 135000^(1/8) L^(-1/2)
 =115.294692112635... L^(-1/2)
 <116 L^(-1/2).
`                                                                  (3.5)

Thus the high-ridge/high-coloop residue left by r33 is **not** an unpaid half-Riesz branch. The entire r31 Dodgson split is paid at the translation-uniform fractional-potential level without calibrated ridge gates.

This does not yet imply an L-infinity density.

## 4. New general theorem: aggregate physical E2 gives an L2 density

The fleet01/B01 proof contains enough pointwise characteristic-function information to upgrade its half-Riesz theorem to absolute continuity with an `L2` density. I state and prove the extracted consequence because it strengthens (3.5) in a different direction.

### Theorem 4.1 — `QFORM-E2-L2-DENSITY-v1`

For any full quadratic-affine form in independent cap-one ORIGINAL coordinates, if one literal physical cross block `M` has

`Delta_2:=E_2(M)>0`,                                             (4.1)

then the law has an `L2` density and

`boxed:
 ||p_Q||_2 <= C_2 Delta_2^(-1/8),
 C_2=2^(1/3)*sqrt(6)*e^(5/24)<3.801.
`                                                                    (4.2)

No continuity is asserted.

#### Proof

Use the natural squared-2-minor law of `M`. Let `H_i` be the total 2-minor mass incident to row `i`, and `h_i=H_i/Delta_2`, so `sum_i h_i=2`.

**Case 1: `max_i h_i<=1/2`.** The mixed-order determinant theorem in the B01 source, with mean order `2` and currency `Delta_2`, gives

`|phi_Q(t)| <= min(1,B|t|^(-1))`,
`B=2*pi*e^(1/2) Delta_2^(-1/4)`.                                (4.3)

Hence

`int_R |phi_Q(t)|^2 dt <=4B`.                                   (4.4)

Plancherel in the convention `p=(2pi)^(-1) F^{-1}phi` gives

`||p_Q||_2 <=2e^(1/4)Delta_2^(-1/8)`.                           (4.5)

**Case 2: some `h_i>1/2`.** Then `H_i>Delta_2/2`. Normalize the partner-row wedge masses by `q_j=W_j/H_i`.

If some `q_j>1/2`, then `W_j>Delta_2/4`. The actual two-row cut on rows `{i,j}` has

`(sigma_1 sigma_2)^2=W_j`.                                     (4.6)

Apply (1.3), square and integrate. This gives

`||p_Q||_2 <=2 W_j^(-1/8)
            <2^(5/4) Delta_2^(-1/8)`.                           (4.7)

If instead all `q_j<=1/2`, the diffuse-star envelope proved in the B01 source is

`|phi_Q(t)| <= min(1,D|t|^(-3/5))`,                             (4.8)

where

`D=C_0 H_i^(-3/20)`,
`C_0<=e^(1/4) 2^(1/4) pi^(3/5)`.                                (4.9)

The threshold is `t_0=D^(5/3)`, and direct integration gives

`int_R |phi_Q(t)|^2 dt <=12D^(5/3)`.                            (4.10)

Therefore

`||p_Q||_2
 <=sqrt(6/pi) C_0^(5/6) H_i^(-1/8)
 <sqrt(6/pi) C_0^(5/6) 2^(1/8) Delta_2^(-1/8)
 =2^(1/3)sqrt(6)e^(5/24) Delta_2^(-1/8).`                       (4.11)

The constant in (4.11) exceeds those in (4.5) and (4.7), proving (4.2). Since `phi_Q in L2`, Fourier-Plancherel uniqueness gives an `L2` density for the law. QED.

The theorem is full-ambient: all unused same-side curvature and all other couplings remain present because each source characteristic estimate has that scope.

## 5. Apply the L2 theorem to the entire aligned B08 survivor

Substitute (3.2) into (4.2):

`boxed:
 ||p_Q||_2
 < C_2 135000^(1/8)L^(-1/2)
 =16.6413553818413...L^(-1/2)
 <16.65 L^(-1/2).
`                                                                  (5.1)

Thus the whole r31/r33 aligned survivor has an actual absolutely continuous density, uniformly in dimension and all allowed coordinate laws. It is not merely atom-free and no rank-two assumption is needed.

By Cauchy-Schwarz, every interval `I` obeys

`boxed:
 P(Q in I)<16.65 L^(-1/2)|I|^(1/2).
`                                                                  (5.2)

In centered small-ball notation,

`boxed:
 sup_s P(|Q-s|<=epsilon)
 <23.535 sqrt(epsilon/L).
`                                                                  (5.3)

The missing target exponent is still linear in interval length; (5.2) has exponent `1/2`. So this is not a proof of the universal bounded-density conjecture.

## 6. Completed designated-partner result applied at an actual inequality

The designated partner `fleet04/B08` has now landed. Its completed report is

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T091414Z-fleet04-B08-QFORM-r1/REPORT.md`.

It proves `QFORM-ANISOTROPIC-RANK1-E2-DIRECTSUM-RECEIVER-v1` for the target-valid physical family

`Q_R=X_0^2+2R U_1V_1+2R^(-1)U_2V_2`, `R>=3`,                  (6.1)

whose cross block has `E_2=1` although `s_1/s_2=R^2 -> infinity`. The theorem gives

`||p_(Q_R)||_infinity <7.251`.                                  (6.2)

Apply it after the actual scalar rescaling `A_R -> L A_R`. Density scaling is exact, so for the corresponding target family with three eigenvalues of modulus at least `L`,

`boxed: ||p_(L Q_R)||_infinity <7.251/L.`                        (6.3)

This is a genuine equation-level use of the designated partner theorem. On the same family Theorem 4.1 gives `||p_(LQ_R)||_2<3.801L^(-1/2)`. The contrast isolates the remaining B08 difficulty accurately: fixed physical `E_2` already forces strong full-form integrability, while the universal `L-infinity` step must be made stable under arbitrary same-bank leakage and extra couplings. The partner proves exactly that the no-leakage anisotropic endpoint is harmless.

## 7. What changed and next implication

The r33 branch-A calibrated-ridge/high-coloop router is no longer needed for a half-Riesz or absolute-continuity conclusion. Returning to the stronger r31 product dichotomy and aggregating **both factors** before inversion yields one unconditional physical certificate:

`E_2(B)>L^4/135000`.

Consequently the entire aligned double-nest survivor now has

- `H_(1/2)(Q)<116L^(-1/2)`;
- an actual `L2` density with `||p_Q||_2<16.65L^(-1/2)`;
- square-root small-ball bound (5.3).

The first remaining B08 implication is therefore sharper:

`QFORM-E2-L2-TO-LINF-LEAKAGE-STABLE-v1` — exploit the anchored provenance still present in the Dodgson packet to improve the interval exponent from `1/2` to `1`, without discarding arbitrary same-bank curvature or extra couplings. The completed fleet04/B08 direct-sum theorem shows this lift is possible in the maximally anisotropic no-leakage endpoint, but does not yet prove leakage stability.

Full QFORM remains **OPEN**. Global continuity remains **OPEN**; Theorem 4.1 proves existence of an `L2` density but not continuity.

## 8. Verification and provenance

`CHECKS.py` verifies the constants and, on seeded random physical blocks, checks that `delta^2+||W||^2` and `||U||^2+||V||^2` are literal sub-sums of the complete physical `E_2(B)`. It terminates `QFORM_B08_R34_CHECK_PASS`.

Repository transport occurred; verified native brain ingestion did not. Status remains `WITHOUT_VERIFIED_BRAIN`.
