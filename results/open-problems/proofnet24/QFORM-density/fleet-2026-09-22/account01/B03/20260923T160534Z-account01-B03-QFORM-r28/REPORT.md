SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T16:05:34Z.
attacking: the critical two-selector residual — convert the designated partner's whole-copy L2/time estimate into a half-Frostman bound, then feed it through the normalization-optimized physical-pair logarithmic transducer to recover linear small-ball scaling without requiring an extra square.

# account01/B03 r28 — Lp selector residual + indefinite-pair logarithmic closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Run:** `20260923T160534Z-account01-B03-QFORM-r28`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING COMPILER / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted three-large-eigenvalue conjecture remains OPEN. This report proves a new end-to-end analytic compiler in which a two-selector residual that is only critical for direct Fourier inversion is nevertheless enough to give an essentially bounded output density once it sits behind a genuine original-coordinate indefinite physical pair. The mechanism is:

1. retain the independent-copy quantity `|phi_R|^2` for the whole residual;
2. use the designated account02/B03 `L^p` selector-Plancherel theorem to obtain both a weighted time integral and an `L^2` density;
3. convert that `L^2` density to a translation-uniform half-Frostman small-ball bound by Cauchy--Schwarz;
4. insert the half-Frostman bound into the normalization-aware logarithmic physical-pair transducer proved in the preceding account01/B03 run.

No coordinate sum/difference pair is split and re-capped conditionally. No law-uniform pointwise quadratic van-der-Corput estimate, post-rotation independence, arbitrary-joint coarea lemma, or naive fiber-sup estimate is used.

## 1. Fresh source boundary


### 1.1 Designated partner actually applied

The completed designated partner result is account02/B03:

`yspennstate/math-open-problems@c3bba054c20287883c43303711eec7eefc05d46e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T131311Z-account02-B03-QFORM-r11/REPORT.md`.

Its theorem `QFORM-JOINT-SELECTOR-PHASE-LP-PLANCHEREL-v1` says the following. Let `Z_1,Z_2` be genuine independent original-coordinate selectors with cap-one densities, independent of a background `W`. Let the coefficient vector

`C(W)=(C_1(W),C_2(W))`

have joint density `g in L^p(R^2)`, with `p>2`, and write

`G=||g||_p`, `theta=1-1/p`, `alpha=2 theta>1`,
`mathcalB=|beta_1 beta_2|>0`.

For arbitrary measurable joint selector phase `P(Z_1,Z_2)` and arbitrary background phase `R_0(W)`, set

`R=R_0(W)+P(Z_1,Z_2)
   +2 beta_1 Z_1 C_1(W)+2 beta_2 Z_2 C_2(W)`.                 (1.1)

Then, with

`A=G pi^alpha mathcalB^(-theta)`,                                  (1.2)

one has

`|phi_R(t)|^2 <= min{1,A |t|^(-alpha)}`.                           (1.3)

The same partner theorem gives

`||p_R||_2^2
 <= [alpha/(alpha-1)] G^(1/alpha) mathcalB^(-1/2)`.                (1.4)

These statements allow arbitrary cross-quadratic curvature inside `P`; the two coefficient coordinates may be dependent. The proof is a joint coefficient-space Holder/Plancherel argument, not a conditional-cap argument for conjugate variables.

### 1.2 Normalization-optimized physical-pair theorem

The immediately preceding account01/B03 result is

`yspennstate/math-open-problems@1a225e191722b852e59d9c8b7c4646929193cad8`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T134955Z-account01-B03-QFORM-r27/REPORT.md`.

It sharpens the completed physical-pair logarithmic transducer as follows. After completing an invertible indefinite physical pair `B_0`, put

`D=|det B_0|`, `kappa=sigma_min(B_0)`.                              (1.5)

If its residual critical value `R` obeys

`sup_z P(|R-z|<=rho) <= H sqrt(rho)` for every `rho>0`,             (1.6)

then

`||p_Q||_infinity <= D^(-1/2) Psi(Theta)`,                         (1.7)

where

`Theta=H sqrt(D/kappa)`,                                           (1.8)

and

`Psi(x)=4 sqrt(2x)` for `0<=x<=1/2`,
`Psi(x)=4+2 log(2x)` for `x>=1/2`.                                 (1.9)

This gives a genuine linear one-copy small-ball estimate; the logarithmic branch is strictly better than the older fourth-root receiver when `Theta>1/2`.

## 2. Main theorem: selector-Plancherel residual closes behind an indefinite pair

Define the common scale

`S_p = G^(1/(2alpha)) mathcalB^(-1/4)`.                            (2.1)

### Theorem 2.1 — `QFORM-LP-SELECTOR-PAIRLOG-CLOSURE-v1`

Assume the physical-pair hypotheses (1.5), and suppose its residual critical value has the exact partner representation (1.1) with `p>2`. Then:

**(a) dependence-safe whole-copy time integral**

`boxed:
 integral_R |t|^(-1/2)|phi_R(t)|^2 dt
 <= [4 alpha/(alpha-1/2)] sqrt(pi) S_p.
`                                                                    (2.2)

**(b) half-Frostman residual bound**

`boxed:
 sup_z P(|R-z|<=rho)
 <= H_p sqrt(rho),
 H_p=sqrt(2alpha/(alpha-1)) S_p.
`                                                                    (2.3)

**(c) linear output small-ball / density bound**

With

`Theta_p=sqrt(2alpha/(alpha-1)) S_p sqrt(D/kappa)`,                 (2.4)

`Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity <= D^(-1/2) Psi(Theta_p).
`                                                                    (2.5)

Consequently every interval `I` obeys

`boxed:
 P(Q in I) <= D^(-1/2) Psi(Theta_p) |I|.
`                                                                    (2.6)

The theorem does **not** assert continuity of the density. Full-target continuity remains open.

### Proof

Start from the partner's squared-characteristic envelope (1.3). For the B03 assignment take the weight exponent `gamma=1/2`. Directly splitting at the crossover `T=A^(1/alpha)` gives

`integral |t|^(-1/2)|phi_R(t)|^2 dt
 <= [2alpha/((1/2)(alpha-1/2))] A^(1/(2alpha)).`                   (2.7)

Because `alpha=2theta`,

`A^(1/(2alpha))
 =G^(1/(2alpha)) pi^(1/2)
  mathcalB^(-theta/(2alpha))
 =sqrt(pi) G^(1/(2alpha)) mathcalB^(-1/4)
 =sqrt(pi) S_p`.                                                    (2.8)

Equations (2.7)-(2.8) prove (2.2).

The independent-copy identity is retained at the level of the whole residual:

`|phi_R(t)|^2=E exp(it(R-R'))`.                                     (2.9)

Nothing in (2.7) conditions on one member of a dependent coordinate sum/difference pair.

Next use the partner's actual `L^2` conclusion (1.4):

`||p_R||_2^2 <= [alpha/(alpha-1)] S_p^2`.                          (2.10)

For every `z` and `rho>0`, Cauchy--Schwarz on the interval `[z-rho,z+rho]` gives

`P(|R-z|<=rho)
 <=(2rho)^(1/2)||p_R||_2
 <=sqrt(2alpha/(alpha-1)) S_p sqrt(rho)`.                           (2.11)

This is exactly (2.3). Apply the already-proved normalization-aware physical-pair theorem (1.7)-(1.9) with `H=H_p`; (2.4)-(2.6) follow. QED.

### Why this is a real closure step

For two selectors, `alpha<=2`; therefore the partner's direct continuous-density threshold `alpha>2` cannot fire. The two-selector packet is intrinsically critical for direct `L^1_t` inversion. The present theorem nevertheless turns it into a bounded density by using the **outer indefinite pair as the final logarithmic smoother**. In particular, it removes the need for the extra disjoint physical square that was required by the partner's separate square-peel corollary.

## 3. Clean `p=infinity` endpoint

When the coefficient vector has a bounded joint density `||g||_infinity<=G`,

`alpha=2`,
`S=G^(1/4) mathcalB^(-1/4)`.                                      (3.1)

Then the assigned whole-copy integral becomes

`boxed:
 integral |t|^(-1/2)|phi_R(t)|^2 dt
 <=(16/3)sqrt(pi) S
 =9.453087204829417... S.
`                                                                    (3.2)

The residual half-Frostman constant is only

`boxed: H=2S,`                                                       (3.3)

which is sharper than passing through the partner's translation-uniform half-Riesz potential (`4sqrt(2) S`). This improvement comes from using the partner's `L^2` theorem and exact interval length `2rho`.

Thus

`Theta=2S sqrt(D/kappa)`.                                           (3.4)

Equivalently,

`boxed:
 ||p_Q||_infinity <=
  8 G^(1/8) mathcalB^(-1/8)(D kappa)^(-1/4),
`                                                                    (3.5)

when `Theta<=1/2`, while for `Theta>=1/2`,

`boxed:
 ||p_Q||_infinity
 <=D^(-1/2)[4+2 log(4 G^(1/4) mathcalB^(-1/4) sqrt(D/kappa))].
`                                                                    (3.6)

The two formulas agree at the threshold.

## 4. Physical rank-two cross residual: aggregate before reciprocal selection

There is an immediate original-coordinate corollary that avoids choosing a single reciprocal cross entry.

Let the residual after the outer physical pair be

`R=Z^T C Z+2 Z^T M Y+R_0(Y)`,                                     (4.1)

where:

- `Z=(Z_1,Z_2)` consists of two genuine independent original-coordinate selectors with cap-one densities;
- `Y` is a disjoint original-coordinate product bank;
- `C` is an arbitrary real symmetric `2x2` matrix;
- `R_0(Y)` is arbitrary;
- `M` has row rank two.

Put

`Delta_2=sqrt(det(M M^T))>0`.                                     (4.2)

Factor `M=H R_0` with `R_0 R_0^T=I_2`. The completed product-projection theorem used in the designated partner report gives

`||p_(M Y)||_infinity <= e/Delta_2`.                               (4.3)

Apply Theorem 2.1 with `p=infinity`, `mathcalB=1`, `G=e/Delta_2`. Then

`boxed:
 integral |t|^(-1/2)|phi_R(t)|^2dt
 <=(16/3)sqrt(pi)e^(1/4) Delta_2^(-1/4),
`                                                                    (4.4)

and

`boxed:
 ||p_Q||_infinity
 <=D^(-1/2)
 Psi(2e^(1/4)Delta_2^(-1/4)sqrt(D/kappa)).
`                                                                    (4.5)

All residual same-selector curvature `Z^TCZ` and all background curvature `R_0(Y)` are retained. The result spends the **full rank-two cross area** `Delta_2` before inversion; no single physical cross coefficient is selected.

At the normalized point `D=kappa=Delta_2=1`, (4.5) gives

`||p_Q||_infinity <=4+2log(4e^(1/4))
 =7.272588722239782...`.                                           (4.6)

## 5. Exact target-valid control family

Let six independent cap-one coordinates be `X_1,...,X_6` and take

`Q_0=2X_1X_2+2X_3X_5+2X_4X_6`.                                   (5.1)

Its coefficient matrix is the direct sum of three blocks

`[[0,1],[1,0]]`,                                                    (5.2)

so its spectrum is exactly

`{1,-1,1,-1,1,-1}`.                                                 (5.3)

Thus it is an exact owner-target family. Use `(X_1,X_2)` as the outer indefinite pair. The residual has selectors `(X_3,X_4)` and coefficient vector `(X_5,X_6)`, whose joint density is at most one. Hence `G=mathcalB=D=kappa=1`, so (3.6) yields

`boxed:
 ||p_(Q_0)||_infinity <=4+2log4
 =6.772588722239782... .
`                                                                    (5.4)

The whole-copy residual time estimate is

`boxed:
 integral |t|^(-1/2)|phi_(2X_3X_5+2X_4X_6)(t)|^2dt
 <=(16/3)sqrt(pi)
 =9.453087204829417... .
`                                                                    (5.5)

This control family is not claimed as progress on the structural extraction itself; it verifies the exact quantifiers and scaling of the new analytic compiler.

## 6. What remains unpaid

The full conjecture is still OPEN. The new theorem pays the analytic branch once one has **both**:

1. a genuine invertible indefinite original-coordinate pair, and
2. in its residual, a two-selector coefficient vector with quantitative `L^p`, `p>2`, control (or in particular a quantitative rank-two cross-area packet).

The bare hypothesis `s_3(A)>=1` does not by itself force a uniformly conditioned physical pair or a uniformly nondegenerate physical rank-two cross block; known star/bank examples rule out such a local-minor shortcut. The remaining structural debt is therefore an aggregate-before-inversion alternative: extract this pair+selector packet at a universal scale, or route the state to the already-paid grouped-hub/ridge/diffuse/near-coloop exits.

The useful new point for the fleet is that a **critical two-selector packet no longer needs an extra independent square** if an outer indefinite pair is available. Its whole-copy `L^2/time` control can be spent directly through the logarithmic pair geometry.

Full-target continuity: OPEN. This theorem proves essential boundedness/absolute continuity in its stated branch, not a continuous representative.