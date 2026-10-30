SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T04:19:54Z.
attacking: integrated Fourier estimate — convert a leverage-free aggregate third-volume residual into a translation-safe physical-pair density bound, without selecting a residual minor or assuming conditional independence.

# fleet01/B02 r22 — leverage-free third-volume residual through a translation-uniform indefinite pair

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. The target-wide unweighted characteristic-function estimate

`int_R |E exp(i t X^T A X)| dt <= C`

also remains OPEN and is not refuted here. The new theorem below gives an essentially bounded density, together with a branchwise `L^2_t` Fourier estimate, on a new product-preserving composite branch. Continuity is **not** proved by this argument.

## 1. Exact target and source pins

The target is unchanged: independent original real coordinates with scalar densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, and one dimension/law/matrix-independent essential density bound for `Q=X^T A X`; continuity is a separate requested strengthening. No Gaussianity, moments, compact support, connected support, log-concavity, or independence after a spectral rotation is used.


Two completed source-valid analytic inputs are used at equation level.

### 1.1 Designated partner fleet02/B02 — translation-uniform indefinite-pair bridge

Canonical source:

`yspennstate/math-open-problems@a68504400f3679153ba22ad2852b3fe0c4048dc1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T181118Z-fleet02-B02-QFORM-r11/REPORT.md`.

Let `B` be a symmetric invertible indefinite physical `2 x 2` principal block, put

`D=|det B|`, `kappa=sigma_min(B)`,

and write after exact completion of that **original-coordinate** pair

`Q=(X+m(Z))^T B (X+m(Z))+R(Z)`,

where the two coordinates of `X` are independent cap-one inputs and are independent of the remaining original-coordinate bank `Z`. The partner theorem allows `m(Z)` and `R(Z)` to be arbitrarily dependent. For every `p>2`, `q=p/(p-1)`,

`||p_Q||_infinity
 <= C_p D^(1/p-1/2) kappa^(-1/p) ||p_R||_q`,                 (1.1)

with

`C_p^p = 4 int_0^infinity (2sqrt(2)+s)^p e^(-s) ds
        + 2^(2+3p/2)/(p/2-1)`.                                (1.2)

At `p=4`,

`C_4=(992+448sqrt(2))^(1/4)=6.34967158837028...`,

so

`||p_Q||_infinity <= C_4 (D kappa)^(-1/4)||p_R||_(4/3)`.       (1.3)

The crucial point for the present splice is the partner's translation uniformity: no independence between the pair translation and the residual output is needed.

### 1.2 Fresh fleet03/B06 — leverage-free aggregate third-volume `L^3` receiver

Canonical theorem source:

`yspennstate/math-open-problems@d739034105d8beb4bf6ddf90fd8179aef2bac58c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T041802Z-fleet03-B06-qform-r25/REPORT.md`.

If a quadratic-plus-affine residual `R` in independent original coordinates contains an original-coordinate physical cross block `C` and

`Z_3=e_3(C^T C)>0`,

then, retaining every same-bank quadratic term, affine term, outside coupling, and every additional cross singular direction, the source proves

`||p_R||_3 <= C_3 Z_3^(-1/9)`,                                  (1.4)

where

`C_3 = 3^(3/2)e^(2/3)2^(-2/3)
     = 6.375655946344417...`.                                  (1.5)

There is **no row- or column-leverage gate** in (1.4). The proof uses the source-valid third-volume decoupling only up to `phi_R in L^(3/2)`, then inverse Hausdorff--Young. It does not claim `phi_R in L^1`.

The latest fleet02/B02 nested-coloop theorem was also read at

`yspennstate/math-open-problems@87dbe53e75a736bc87f97e02e40ebf2c3c13b095`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T033508Z-fleet02-B02-QFORM-auto11/REPORT.md`.

It closes the exact-rank-two floor of the nested four-volume collar by automatic transversality. The new theorem below is complementary: it pays an **indefinite physical pair whose Schur residual retains aggregate third volume**, without any third-volume leverage condition and without requiring an additional scalar residual pivot.

## 2. Main theorem — `QFORM-INDEFINITE-PAIR-THIRDVOLUME-L3-v1`

Let `I={i,j}` be two original coordinates and suppose the physical principal block

`B=A[I,I]`

is symmetric, invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Let `K=[n]\I`. Completing the physical pair exactly gives

`Q=(X_I+m(X_K))^T B (X_I+m(X_K))+R(X_K)`,                         (2.1)

where `m` is the exact Schur translation and `R` is the exact residual quadratic form. No stochastic change of variables is made.

Assume that, inside the residual original coordinates `K`, there are disjoint physical banks `K_1,K_2` whose residual cross block is `C`, with

`Z_3=e_3(C^T C)>0`.                                                (2.2)

Then for every `p>2`,

`boxed(
 ||p_Q||_infinity
 <= K_p D^(1/p-1/2) kappa^(-1/p) Z_3^(-1/(6p)),
)`                                                                    (2.3)

where

`K_p = C_p C_3^(3/(2p))`.                                          (2.4)

In particular, at `p=4`,

`boxed(
 ||p_Q||_infinity
 <= K_4 (D kappa)^(-1/4) Z_3^(-1/24),
)`                                                                    (2.5)

with

`K_4
 =(992+448sqrt(2))^(1/4)
   [3^(3/2)e^(2/3)2^(-2/3)]^(3/8)
 =12.718857191446856... <12.719.`                                  (2.6)

Equivalently, define the homogeneous product-preserving currency

`Lambda_pair,3 := (D kappa Z_3^(1/6))^(1/4)`.                       (2.7)

Then

`boxed(||p_Q||_infinity < 12.719 / Lambda_pair,3.)`                 (2.8)

The scale is correct: if the full quadratic coefficient matrix is multiplied by `lambda`, then `D -> lambda^2 D`, `kappa -> |lambda|kappa`, `Z_3 -> |lambda|^6 Z_3`, so `Lambda_pair,3 -> |lambda| Lambda_pair,3`.

### Proof

By (1.4), the exact Schur residual has a probability density satisfying

`||p_R||_3 <= C_3 Z_3^(-1/9)`.                                      (2.9)

For `p>2` put `q=p/(p-1)`. Since `1<q<2<3`, interpolate between `L^1` and `L^3`. If `theta` is determined by

`1/q=(1-theta)/1+theta/3`,                                         (2.10)

then, because `1/q=1-1/p`,

`theta=3/(2p)`.                                                     (2.11)

As `||p_R||_1=1`,

`||p_R||_q
 <= ||p_R||_3^theta
 <= C_3^(3/(2p)) Z_3^[-(1/9)(3/(2p))]
 = C_3^(3/(2p)) Z_3^(-1/(6p)).`                                    (2.12)

Now apply the designated fleet02/B02 translation-uniform pair theorem (1.1) to the **actual** inequality (2.12). This gives (2.3) immediately. At `p=4`, `q=4/3` and `theta=3/8`, so

`||p_R||_(4/3) <= C_3^(3/8) Z_3^(-1/24)`,                          (2.13)

and substitution into (1.3) gives (2.5)--(2.6).

The pair translation `m(X_K)` is allowed to depend on exactly the same residual variables that determine `R`; this dependence is explicitly allowed in the partner theorem. Therefore no convolution-independence shortcut or conditional projected-density cap is being inserted.

QED.

## 3. Why this is stronger than the previous pair + determinant splice

The designated partner's own preceding composite inequality used an additional genuine scalar residual pivot `d` to manufacture an `L^infinity` residual density, and then obtained

`||p_Q||_infinity
 <=12.952609 (D kappa)^(-1/4)|d|^(-1/8)E_3(C)^(-1/48)`.

The new estimate (2.5) removes the scalar residual pivot completely and strengthens the third-volume exponent from `-1/48` to `-1/24`:

`||p_Q||_infinity
 <12.719 (D kappa)^(-1/4)E_3(C)^(-1/24).`

Thus, once an indefinite physical pair is available, **aggregate third volume in its Schur residual is itself sufficient**. No third-volume leverage gate, scalar residual diagonal, individual residual minor, or residual rank-three exactness is needed.

This is particularly useful in higher-rank/high-leverage collars where a physical pair has already been exposed but the Schur remainder is not clean enough for a square-pivot or exact-rank argument.

## 4. Integrated-Fourier consequence actually proved

The theorem above is an essential-density theorem, not an `L^1_t` Fourier theorem. Since `p_Q` is a probability density and `p_Q in L^infinity`,

`||p_Q||_2^2 <= ||p_Q||_infinity`.

Plancherel therefore gives the genuine branchwise estimate

`boxed(
 int_R |phi_Q(t)|^2 dt
 <= 2pi K_4 (D kappa)^(-1/4) Z_3^(-1/24)
 <79.915 (D kappa)^(-1/4) Z_3^(-1/24).
)`                                                                    (4.1)

This is useful integrated Fourier currency, but it does **not** imply the target-wide unweighted `L^1_t` estimate. No claim of continuity is made from (4.1).

## 5. Correction discipline

The proof uses none of the invalidated mechanisms:

- no law-uniform pointwise van-der-Corput/Fresnel decay;
- no Gaussian, moment, support, or log-concavity hypothesis;
- no independence after a spectral rotation;
- no arbitrary-joint rank-three coarea bound;
- no positive conditional projection-height moment;
- no fiber-supremum integration;
- no extraction of one residual `3 x 3` minor from aggregate `Z_3`;
- no deletion of a small but nonzero cross tail;
- no assumption that the Schur translation is independent of the Schur residual.

The aggregate third volume is summed **before** the reciprocal power `Z_3^(-1/24)` is paid.

## 6. Relation to the live nested-coloop frontier

The newest fleet02/B02 result closes the exact-rank-two floor after two nested heavy-volume deletions. The present theorem supplies a different exit for the rank-at-least-three side of the fleet's high-leverage collar whenever an actual indefinite principal pair is exposed before the remaining third-volume bank is spent.

The first unpaid structural implication for this branch is therefore:

`QFORM-PAIR-PLUS-THIRDVOLUME-EXTRACTION-v1` — from the surviving high-leverage / nested-coloop / overlap-compound geometry, force either

1. an already-paid exact-rank-two-floor or exact-rank-r physical-cross-block exit; or
2. a physical indefinite pair with `D kappa Z_3^(1/6)` bounded below at dimension-free scale in its exact Schur residual; or
3. one of the existing grouped-square, grouped-bilinear, ridge, mixed-hub, or outer-square exits.

The stress families in the correction ledger show that aggregate pair determinant mass alone does **not** select a uniformly conditioned pair, so this remaining step must aggregate before reciprocal conditioning or use a genuine hub/bank structure.

## 7. Fourier criterion status

I did not find a target-valid counterexample to

`int_R |E exp(i t X^T A X)| dt <= C`.

The global unweighted criterion remains `OPEN_NOT_REFUTED`. The present result proves only the branchwise `L^2_t` bound (4.1) and the essential `L^infinity` density bound (2.5). Full-target continuity remains open.

## 8. Arithmetic audit

The companion checker records:

- `C_3=6.375655946344417...`;
- `C_4(pair)=6.349671588370281...`;
- interpolation exponent at `p=4` is `theta=3/8`;
- `K_4=12.718857191446856...`;
- `2pi K_4=79.9149366294143...`.

MODEL: GPT-5.6 Sol. Requested reasoning effort: maximum actually supported. Configured/self-reported reasoning effort: UNKNOWN / not exposed. Provider reasoning-token and thinking-time counters: null / NOT_EXPOSED.
