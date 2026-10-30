SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-24T06:00:28Z.
attacking: the r50 robust-rank-two / hub-star frontier, optimizing the leverage peel so the surviving physical rank-two planes satisfy the exact row-leverage <=1/2 Brascamp--Lieb gate while the failure branch still exposes a dimension-free literal hub star.

# fleet03/B19 r51 — BL-compatible leverage peel for the ultra-thin physical rank-two frontier

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW TARGET-RELEVANT COMPILER / PARTNER RESULT APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository transport is not native authenticated brain ingestion.

Regularity: the new theorem by itself gives a fractional-potential / interval-concentration conclusion on its robust branch, not an `L^infinity` density theorem. Full-target continuity remains **OPEN**.

All coordinate sets below are literal ORIGINAL-coordinate sets. No random variable is rotated. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, arbitrary-joint coarea, conditional projection-height, fiber-supremum or law-uniform pointwise oscillatory-decay assumption is used. The nonzero cross tail is retained throughout.

## 1. Fresh source-pinned frontier


The immediate same-slot source is fleet03/B19 r50:

`yspennstate/math-open-problems@f3a0b13c6d73bb3ec94be4ad5fc293c60ab7da3f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260924T050225Z-fleet03-B19-QFORM-r50/REPORT.md`.

It leaves disjoint physical banks `R,C` and the actual cross block

`N=A[R,C]`,

with top-two SVD truncation

`N_2=U Sigma V^T`, `Sigma=diag(sigma_1,sigma_2)`,

such that

`||N-N_2||_F < tau`, `tau=2^-16`,                              (1.1)

`sigma_2(N)>=s_0`, `s_0=1/64`.                                 (1.2)

The completed analytic receiver used again below is fleet02/B19

`yspennstate/math-open-problems@f4d95bc33caf8db11888cceb817c005484f67d31`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260924T031336Z-fleet02-B19-QFORM-auto11/REPORT.md`,

`QFORM-PHYSICAL-R2-FRACTIONAL-SMOOTHING-v1`. For every literal disjoint physical cross block `M`, with

`Z_2(M)=e_2(M^T M)>0`,

it controls the FULL ambient quadratic law, retaining arbitrary same-bank curvature, outside couplings, affine terms, signs and extra spectrum, by

`H_(1/4)(Q):=sup_s E|Q-s|^(-1/4)
 <= C_R2 Z_2(M)^(-1/16)`,                                        (1.3)

where

`C_R2=3.929131770449763...`.                                    (1.4)

This is a fractional smoothing theorem, not an endpoint density theorem.

The point of the present run is to alter the r50 heavy/light threshold so that the robust branch is not merely a strong rank-two crossing: its two coefficient planes become exactly compatible with the existing `<=1/2` row-leverage Brascamp--Lieb gates.

## 2. General leverage-peel lemma

Let `U` be any matrix with two orthonormal columns. Its physical leverage scores are

`ell_i=||U_{i,*}||_2^2`,                                         (2.1)

so

`sum_i ell_i=2`.                                                  (2.2)

Fix `eta in (0,1)` and declare

`H={i:ell_i>eta}`, `L=H^c`.                                      (2.3)

Then

`|H|<2/eta`.                                                      (2.4)

Set

`G=U[L,:]^T U[L,:]`.                                             (2.5)

If `lambda_min(G)>=g>0`, define the normalized restricted frame

`U_tilde=U[L,:] G^(-1/2)`.                                      (2.6)

Then

`U_tilde^T U_tilde=I_2`,                                         (2.7)

and every light physical row satisfies

`||U_tilde_{i,*}||_2^2
 =U_{i,*} G^(-1) U_{i,*}^T
 <=ell_i/g
 <=eta/g`.                                                       (2.8)

Thus choosing `eta<=g/2` forces the exact leverage gate

`max_i ||U_tilde_{i,*}||_2^2 <=1/2`.                             (2.9)

If instead `lambda_min(G)<g`, then

`U[H,:]^T U[H,:]=I_2-G`                                         (2.10)

has largest eigenvalue `>1-g`, hence

`tr(U[H,:]^T U[H,:])>1-g`.                                      (2.11)

This elementary alternative is the entire deterministic engine of the optimized compiler.

## 3. Threshold optimization

To retain the leverage gate, set `eta=g/2`. If at most `m` heavy rows are desired, the strict inequality in (2.4) permits `m` whenever

`2/eta=m+1`, i.e. `g=4/(m+1)`.                                  (3.1)

On a failure branch, the argument below gives a star scale proportional to

`sqrt((1-g)/m)
 =sqrt((m-3)/(m(m+1)))`.                                         (3.2)

Among integers `m>=4`, this quantity is maximized at `m=6` and `m=7`, where it equals `1/sqrt(14)`. Taking `m=6` gives the stronger robust crossing, so use

`boxed: g=4/7, eta=2/7`.                                        (3.3)

There are therefore at most six heavy coordinates on either bank, while every robust normalized light-plane row has leverage at most one half.

## 4. Main theorem

### Theorem 4.1 — `QFORM-BL-COMPATIBLE-HEAVY12-PEEL-v1`

Assume (1.1)-(1.2). Define

`H_R={i in R: ||U_{i,*}||^2>2/7}`, `L_R=R\H_R`,

`H_C={j in C: ||V_{j,*}||^2>2/7}`, `L_C=C\H_C`,                  (4.1)

and

`G_R=U[L_R]^T U[L_R]`, `G_C=V[L_C]^T V[L_C]`.                   (4.2)

Then `|H_R|,|H_C|<=6`, and at least one of the following alternatives holds.

### A. BL-compatible robust rank-two branch

If

`lambda_min(G_R)>=4/7`, `lambda_min(G_C)>=4/7`,                  (4.3)

then the ACTUAL literal light-light crossing

`M=N[L_R,L_C]`                                                    (4.4)

satisfies

`boxed:
 sigma_2(M)
 > (4/7)(1/64)-2^-16
 =4089/458752
 =0.008913312639508928... .`                                     (4.5)

Moreover the coefficient subspaces obtained by restricting the top-two singular frames to the light banks admit orthonormal frames

`U_tilde=U[L_R]G_R^(-1/2)`, `V_tilde=V[L_C]G_C^(-1/2)`           (4.6)

whose literal physical row leverages obey

`boxed:
 max_i ||U_tilde_{i,*}||^2 <=1/2,
 max_j ||V_tilde_{j,*}||^2 <=1/2.`                               (4.7)

Thus the robust survivor simultaneously carries a strong actual physical rank-two crossing and the exact diffuse-plane leverage gate used by the fleet's product-preserving Brascamp--Lieb/Fresnel receivers.

Applying the completed fleet02/B19 theorem (1.3) to the ACTUAL block `M`, not to its rank-two approximation, gives

`Z_2(M)>=sigma_2(M)^4`,                                          (4.8)

hence

`boxed:
 H_(1/4)(Q)<12.787535.`                                          (4.9)

Consequently every interval `I` of length `delta` satisfies

`boxed:
 P(Q in I)<10.752992 delta^(1/4).`                               (4.10)

All same-bank curvature and the nonzero `2^-16` crossing tail remain in the law because the source fractional receiver is full-ambient.

### B. Literal physical hub-star branch

If the first inequality in (4.3) fails, then some literal physical coordinate `i in H_R` obeys

`boxed:
 ||A[i,C]||_2
 > 1/(64 sqrt(14))-2^-16
 =0.004160698115819131... .`                                     (4.11)

If the second inequality fails, the transpose statement holds:

`boxed:
 ||A[R,j]||_2>0.004160698115819131...`                           (4.12)

for some `j in H_C`.

So the price of making the surviving rank-two planes BL-compatible is only a finite exceptional set of at most six coordinates per bank; failure still exposes a dimension-free original-coordinate star.

### Proof

The cardinality bound follows immediately from

`sum_i ||U_i||^2=sum_j ||V_j||^2=2`: seven rows each strictly larger than `2/7` would have total leverage greater than two.

Assume (4.3). Let

`U_L=U[L_R]`, `V_L=V[L_C]`.                                     (4.13)

Then

`sigma_min(U_L)>=sqrt(4/7)`, `sigma_min(V_L)>=sqrt(4/7)`.        (4.14)

The rank-two restriction is

`N_2[L_R,L_C]=U_L Sigma V_L^T`,                                  (4.15)

so, by thin QR or the min-singular-value product inequality,

`sigma_2(N_2[L_R,L_C])
 >=(4/7)sigma_2(N)
 >=1/112`.                                                        (4.16)

Restriction does not increase the Frobenius or operator norm of the tail. Weyl therefore gives

`sigma_2(M)>1/112-2^-16=4089/458752`,                            (4.17)

which is (4.5).

Equations (4.6)-(4.7) are exactly (2.6)-(2.9) with `eta=2/7`, `g=4/7`. Applying (1.3) and the elementary inequality `Z_2(M)>=sigma_1(M)^2 sigma_2(M)^2>=sigma_2(M)^4` proves (4.9). Finally

`1_{Q in I}<=(delta/2)^(1/4)|Q-mid(I)|^(-1/4)`                  (4.18)

proves (4.10).

Now suppose `lambda_min(G_R)<4/7`. By (2.10)-(2.11),

`tr(U[H_R]^T U[H_R])>3/7`.                                      (4.19)

Since `V^T V=I_2` and `Sigma^2>=sigma_2(N)^2 I_2`,

`||N_2[H_R,C]||_F^2
 =tr(Sigma^2 U[H_R]^T U[H_R])
 >(3/7)sigma_2(N)^2`.                                            (4.20)

There are at most six heavy rows, so one such physical row has norm

`||N_2[i,C]||_2
 >sigma_2(N) sqrt((3/7)/6)
 =sigma_2(N)/sqrt(14)
 >=1/(64 sqrt(14)).`                                             (4.21)

Restoring the actual tail costs at most its global Frobenius norm `2^-16`, proving (4.11). The column-side proof is identical after transposition. QED.

## 5. What this accomplishes in the conditional proof assembly

The r47--r50 compiler had reduced one difficult full-target frontier to an ultra-thin physical rank-two crossing, with arbitrary same-bank curvature separately organized into finite latent/hub structure plus spectrally diffuse residuals, but the r50 robust light planes were not guaranteed to satisfy the strongest existing product-Fourier leverage gates.

Theorem 4.1 removes that mismatch. In the robust branch the exact top-two coefficient subspaces on the surviving literal light banks now have row leverage `<=1/2`, while the ACTUAL crossing, including its nonzero tail, retains `sigma_2>0.0089133` and the full-law `H_(1/4)` resource improves from `15.732` to `12.788`. In the failure branch one of at most twelve total exceptional physical coordinates carries a star exceeding `0.00416069`.

This does **not** finish the endpoint. The first remaining implication on this route is now

`QFORM-BL-DIFFUSE-R2-WITH-RETAINED-TAIL-AND-THIRD-SOURCE-ENDPOINT-v1`:

> Starting from the robust branch of Theorem 4.1, spend the two `<=1/2` physical leverage planes together with the r49 diffuse third/high-spectrum resource to obtain an `L^1` characteristic function or a linear small-ball bound, while retaining the genuine nonzero cross tail and arbitrary same-bank curvature. Alternatively, show that the finite hub/latent structure forces an already-paid physical pair, grouped-star, incident-volume, ridge-window or bipartite crossing receiver.

The star failure branch is narrower as well, but an `l2` star alone does not force a large individual edge or an invertible pair; no dimension-dependent extraction is made. Fresh fleet03/B20 work pays a strong *individual* edge under additional physical-pair hypotheses, so it is a valid receiver when such an edge is genuinely present, not from (4.11) alone.

Parallel global debts from r50 remain visible: the giant near-rank-one crossing, the small-Pluecker aggregate branch, and the extra-spectrum/low-rank-carrier glue. Therefore no claim of a completed full proof is made.

## 6. Failed shortcut preserved: marginalizing the tail is not legitimate

A tempting next step is to replace the actual light crossing by its rank-two truncation, prove a clean BL/Fresnel endpoint for the two diffuse planes, and then regard the `2^-16` tail as a small random perturbation. That is invalid under the owner's hypotheses: the input coordinates can be unbounded and have no moments, so a small coefficient matrix does not produce a uniformly small random quadratic term.

A second tempting shortcut is to project to the two latent coordinates on each side and keep only the bounded projected density. The same-bank and tail phases then create phase-weighted amplitudes depending on the opposite bank; the projected variables are not independent. The fleet04/B19 moving-ridge construction below shows concretely why replacing this provenance by an arbitrary bounded joint density cannot be an endpoint argument.

Thus the new leverage gate is a **product-coordinate analytic interface**, not permission to forget the original product source.

## 7. Designated fleet04/B19 result applied at actual inequalities

The completed fleet04/B19 exact-null-coloop theorem is

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`,

`QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`. Inside its exact residual-diffuse rank-three null-coloop scope, for `0<D_res<=1` and `|det M_3|>=1`,

`||p_Q||_infinity<34 sqrt(log(e/D_res))`,                         (7.1)

with a continuous `C_0` density. Therefore, at the concrete gate

`2^-52<=D_res<=1`,                                                (7.2)

one obtains

`boxed:
 ||p_Q||_infinity
 <34 sqrt(log(e 2^52))
 =206.935892...<207,`                                             (7.3)

with continuous density. This is applied only in the partner's exact proved scope; it is not asserted for the merely near-null r51 carrier.

The newer completed partner barrier is fleet04/B19

`yspennstate/math-open-problems@dbadc6024c1dbcafa4269688b2a21cc5c3b25dd0`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260923T151700Z-fleet04-B19-QFORM-r4/REPORT.md`,

`QFORM-MOVING-RIDGE-JOINT-CAP-BARRIER-v1`. At the actual parameter `eps=2^-18`, it supplies a joint-density-cap-one dependent triple for which

`boxed:
 ||p_(4XY+Z^2-YW)||_infinity
 >=2^18/9
 =29127.111111... .`                                              (7.4)

This is **not** a target counterexample because `(Y,Z,W)` are dependent. It is directly relevant to the r51 endpoint debt: the two diffuse projected planes cannot simply be compressed to an arbitrary bounded joint law after product provenance is forgotten.

## 8. Deterministic verification

`CHECK.py` independently reconstructs 6,000 random noncommuting rectangular matrices from exact prescribed SVD data, always with `sigma_2(N)>=1/64` and top-two Frobenius tail `<2^-16`. It recomputes the heavy sets, light Grams, actual restricted crossing, whitened row leverages, and the appropriate robust or star inequality.

Observed:

- robust cases: `3551`;
- `R`-failure star tests: `1357`;
- `C`-failure star tests: `1432`;
- violations: `0`;
- maximum heavy count observed: `6` on `R`, `5` on `C`;
- minimum actual / instance-specific robust lower-bound ratio: `1.0000059455527155`;
- minimum actual / instance-specific star lower-bound ratio: `1.0002797417465399`;
- maximum normalized light leverage: `0.48414200319219863`.

Terminal marker:

`QFORM_B19_R51_BL_COMPATIBLE_PEEL_CHECK_PASS`.

These computations are diagnostics only; Theorem 4.1 is proved algebraically above.

## 9. Status

Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.

Full universal continuous-density conclusion: **OPEN**.

New r51 robust branch: actual physical rank-two crossing with `sigma_2>4089/458752`, coefficient-plane row leverage `<=1/2`, full-law `H_(1/4)<12.787535`, and interval concentration `<10.752992 delta^(1/4)`.

New r51 failure branch: at most six exceptional coordinates per bank and a literal physical cross-star `>0.0041606981` on a failing side.

No coefficient tail is discarded and no post-rotation independence is used.
