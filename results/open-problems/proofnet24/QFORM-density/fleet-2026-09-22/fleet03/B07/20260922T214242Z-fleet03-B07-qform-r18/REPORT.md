SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-22T21:42:42Z.
attacking: the surviving O0 anchored edge/two-star obstruction by a second effective-rank ridge on the rectangular Schur bank, selecting a physical 2x2 cross minor only after aggregate second-compound mass has already been concentrated.

# fleet03/B07 r18 — nested effective-rank-one selector inside the O0 anchored packet

**Run:** `20260922T214242Z-fleet03-B07-qform-r18`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL PAYMENT / FULL TARGET OPEN`.

## 1. Exact target and correction discipline

The owner target remains unrestricted: for every finite dimension, every independent real original-coordinate family with one-dimensional probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `Q=X^TAX`, or give a valid counterexample. Continuity is a separate requested conclusion.

This report uses no Gaussian, moment, support, log-concavity, iid, diagonal-basis, or post-rotation-independence assumption. It does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, conditional projection-density supremum/moment, single-good-minor extraction, or naive fiber-supremum routes. The selection below occurs only after an aggregate second-compound packet has been produced and then after a second effective-rank collapse; it is therefore not the corrected-away inference that one arbitrary tiny principal/cross minor must be uniformly good.

The designated `fleet04/B07` current-QFORM canonical location was still absent at the fresh check, so no partner theorem is fabricated. The completed compatible same-assignment result actually consumed is fleet01/B07:

`yspennstate/math-open-problems@f82fe367b06909082f94eda2b98f4a2fd2a5bb7c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260922T210652Z-r11/REPORT.md`.

Its `QFORM-COMPOUND-ORDER-TRANSFER-v1` starts from the O0 third-compound resource `E_3(B)>=1/256` and proves

`E_2(B) >= c_2=(9/2^17)^(1/3)=0.04094908428451402... >1/25`.      (1.1)

It then combines the preceding B07 effective-rank-two theorem with this resource. In the surviving two-sided near-coloop branch there are physical row/column anchors `(i,j)` such that

`M_ij:=sum_(k!=i,l!=j) det B[{i,k},{j,l}]^2 > E_2(B)/2 >1/50`.   (1.2)

Writing the original-coordinate cross block in anchored form

`B=[[b,r^T],[c,C]]`,                                                (1.3)

one has the exact identity

`M_ij=||bC-c r^T||_F^2`.                                           (1.4)

The immediate unpaid implication was to turn this anchored aggregate packet into a source-valid density or half-Riesz payment without paying a reciprocal arbitrary tiny minor.

The analytic endpoint used below is fleet03/B03:

`yspennstate/math-open-problems@924b3c4c70f86a64402863fe228f641bf3db60b2`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T175531Z-fleet03-B03-QFORM-r17/REPORT.md`.

For an original-coordinate cross block of exact rank two with nonzero singular values `s_1,s_2`, retaining arbitrary same-side quadratic phases and outside couplings, it proves

`H_(1/2)(R):=sup_y E|R-y|^(-1/2)
 <= C_2 (s_1s_2)^(-1/4),`                                      (1.5)

where

`C_2=sqrt(e) 2^(-3/4) B(1/4,1/4)=7.270461147134126...`.         (1.6)

For a genuine `2x2` physical cross block, `s_1s_2=|det|`.

## 2. Rectangular Schur bank under a nonzero anchor

Assume the first-stage anchored coefficient in (1.3) satisfies

`b!=0`.                                                           (2.1)

Define the rectangular Schur bank

`S:=C-c r^T/b`.                                                   (2.2)

Then (1.4) gives the exact aggregate identity

`boxed(M_ij=b^2 ||S||_F^2.)`                                     (2.3)

Moreover ordinary invertible block elimination transforms `B` to `diag(b,S)`, hence

`boxed(rank(B)=1+rank(S).)`                                      (2.4)

In the O0 survivor `rank(B)>=3` (indeed the preceding fleet01/B07 reduction leaves rank at least four after its exact-rank-three payment), so

`rank(S)>=2`.                                                     (2.5)

Thus a second effective-rank calibration is available.

## 3. A dimension-free size-one mass lemma at effective rank one

Let the nonzero singular values of `S` be `t_a`. There is a unique `rho>0` such that

`sum_a t_a^2/(rho^2+t_a^2)=1`,                                  (3.1)

because the left side decreases continuously from `rank(S)>=2` to zero. Put

`q_a=t_a^2/(rho^2+t_a^2) in (0,1)`, `sum_a q_a=1`,              (3.2)

and let

`N=sum_a Bernoulli(q_a)`                                        (3.3)

with independent Bernoulli summands. This is the subset-size law of the ridge `L`-ensemble on either side of `S`.

### Lemma 3.1 — `QFORM-EFFRANK1-SIZEONE-MASS-v1`

`boxed(P(N=1) >= c_0:=1/2-e^(-1)=0.13212055882855767... .)`      (3.4)

### Proof

First,

`P(N=0)=prod_a(1-q_a) <= exp(-sum_a q_a)=e^(-1)`.               (3.5)

Second,

`P(N>=2) <= (1/2) E[N(N-1)]`
`          =(1/2)[(sum q_a)^2-sum q_a^2] <=1/2`.                (3.6)

Therefore

`P(N=1)=1-P(N=0)-P(N>=2) >=1/2-e^(-1)`.                         (3.7)

QED.

Define the fixed threshold

`eps_0:=c_0/4=0.033030139707139416...`,
`ell_0:=1-eps_0=0.9669698602928606...`.                          (3.8)

## 4. New nested selector

Let

`K_L=SS^T(rho^2 I+SS^T)^(-1),`
`K_R=S^TS(rho^2 I+S^TS)^(-1)`                                  (4.1)

be the physical row/column ridge kernels at the scale (3.1).

### Theorem 4.1 — `QFORM-NESTED-EFFRANK1-MINOR-SELECTOR-v1`

Suppose there are a physical residual row `k` and physical residual column `l` satisfying

`(K_L)_kk>ell_0`, `(K_R)_ll>ell_0`.                              (4.2)

Then

`boxed(S_kl^2 > (1/2)||S||_F^2.)`                               (4.3)

and therefore the original physical `2x2` cross minor through the first-stage anchors obeys

`boxed(
 |det B[{i,k},{j,l}]|^2
   > M_ij/2
   > E_2(B)/4.
)`                                                               (4.4)

### Proof

For the row `L`-ensemble, `P(k in I)=(K_L)_kk`. Condition on the event `N=1`. By Lemma 3.1,

`P(k notin I | N=1)
 <= P(k notin I)/P(N=1)
 < eps_0/c_0=1/4`.                                               (4.5)

Thus the conditioned size-one row marginal assigns probability `>3/4` to `k`. The same argument on the column ensemble gives conditioned size-one column marginal `>3/4` at `l`.

The common fixed-size-one joint minor law is explicitly

`mu(a,b)=S_ab^2/||S||_F^2`.                                     (4.6)

Indeed its row marginal is `||row_a(S)||_2^2/||S||_F^2`, exactly the row `L`-ensemble conditioned on size one, and similarly for columns. Hence the union bound under this *joint* law gives

`mu(k,l)>1-1/4-1/4=1/2`,                                       (4.7)

which is (4.3).

Finally, by (2.2),

`det B[{i,k},{j,l}]
 = b C_kl-c_k r_l
 = b S_kl`.                                                      (4.8)

Using (2.3), (4.3), and (1.2),

`|det|^2=b^2S_kl^2
 >(1/2)b^2||S||_F^2
 =M_ij/2
 >E_2(B)/4`,                                                     (4.9)

proving (4.4). QED.

### Why this does not revive the one-tiny-minor mistake

The local minor is selected only after two aggregate steps:

1. the complete second-compound packet `M_ij>E_2/2` is forced through first-stage physical anchors by the effective-rank-two ridge law;
2. its exact rectangular Schur bank is calibrated to effective rank one, where a constant lower bound on the size-one determinantal mass converts two *conditional* near-coloops into one joint physical entry carrying more than half of the Schur-bank Frobenius mass.

No assertion is made that an arbitrary spectral lower bound directly yields a good physical `2x2` minor.

## 5. Actual application of the compatible fleet01/B07 theorem

Insert (1.1) into (4.4):

`|det B[{i,k},{j,l}]|^2 > E_2(B)/4 >1/100`,                     (5.1)

so

`boxed(|det B[{i,k},{j,l}]|>1/10.)`                             (5.2)

This is an actual quantitative use of the completed fleet01/B07 compound-order theorem.

The two selected rows belong to one original-coordinate bank and the two selected columns to the disjoint other bank, so this is a genuine invertible `2x2` original-coordinate cross block. Apply the completed fleet03/B03 exact-rank-two cross estimate (1.5):

`H_(1/2)(R)
 < C_2 (1/10)^(-1/4)
 =7.270461147134126... *10^(1/4)
 =12.928911359436583...`.                                      (5.3)

Hence the nested-high, nonzero-anchor branch is quantitatively paid by

`boxed(H_(1/2)(R)<12.93.)`                                      (5.4)

All arbitrary same-side quadratic terms, affine terms, outside couplings, signs and additional spectrum allowed by the B03 theorem remain present. If this residual sits behind a genuine physical scalar square pivot `a`, the already-proved scalar transducer further gives

`||p_Q||_infinity <12.93 |a|^(-1/2)`.                          (5.5)

Equation (5.5) is stated only at that scalar-pivot scope; no universal lower bound on `|a|` is silently inserted here.

## 6. Exact remaining coordinate-minor debt

The surviving O0 anchored obstruction is now strictly narrower. After the first effective-rank-two near-coloop packet, either:

1. `b=0`, in which case (1.4) is the genuine two-star geometry `M_ij=||c||^2||r||^2`; or
2. `b!=0`, but at the second ridge scale (3.1) at least one physical side has
   `max diag K <= ell_0=0.9669698602...`.

The branch `b!=0` with both second-stage sides above `ell_0` is closed by (5.4). Therefore the first unpaid implication is

`QFORM-O0-ZERO-ANCHOR-OR-SECONDSTAGE-MODERATE-PAYMENT-v1`:

prove a product-preserving half-Riesz/density estimate for the exact zero-anchor two-star bank, or for the rectangular Schur bank whose effective-rank-one ridge is not doubly concentrated, while keeping arbitrary same-bank curvature and extra spectrum. A promising next step is a first-compound mixed ridge estimate that spends `|b|^2||S||_F^2` before selecting an entry; in the exact zero-anchor case one instead needs a two-star bilinear mechanism that does not pretend the two aggregate projections are independent of their within-bank quadratic remainders.

## 7. Status and regularity

This is a supporting target-level reduction and a new payment of a genuine surviving O0 subbranch. It is **not** a proof of the full QFORM conjecture and **not** a counterexample. Full QFORM remains OPEN. The present endpoint is a half-Riesz bound; this run does not by itself prove the requested continuous-density conclusion on this branch. Continuity remains proved only on previously completed branches whose characteristic-function estimates are genuinely integrable.

Finite numerical checks used only as regression checks:

`c_0 =0.13212055882855767...`,
`eps_0=0.033030139707139416...`,
`ell_0=0.9669698602928606...`,
`C_2*10^(1/4)=12.928911359436583...`.
