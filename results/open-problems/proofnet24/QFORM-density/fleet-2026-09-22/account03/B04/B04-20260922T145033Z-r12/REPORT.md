# account03/B04 — square-assisted product-Fourier closure at the two-cross threshold

Run: `B04-20260922T145033Z-r12`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The owner target is unchanged: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal bound for the essential supremum of the density of `X^T A X`, or give a valid counterexample. No moment, compact-support, log-concavity, connected-support, Gaussian, or post-rotation-independence hypothesis is added here. Continuity is tracked separately.

The prior B04 mechanism established regularized-determinant/diffuse branches and reviewed the determinant proof. This run changes mechanism: it uses an `L^(3/2)_t -> L^3_x` Fourier bridge and then spends the resulting `L^3` currency through a scalar-square half-Riesz coarea estimate. The key point is that **two** physical cross singular directions, not three, are enough once one genuine original-coordinate square is available. This is a product-space integrated estimate, not the refuted law-uniform pointwise scalar Fresnel decay.

The exact assigned partner `account04/B04` had no completed current-QFORM report or handoff at the fresh prepublication scans, so no such result is fabricated. A completed compatible account04 result, `account04/B20 / QFORM-AGGREGATE-HYPERBOLIC-SQUARE-v1`, is applied in Section 6 to an actual structural inequality.

## 2. Source-pinned inputs actually used

1. **Regularized determinant theorem.** `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`. For a physical cut with cross block `B`, if the left range-projection diagonal is at most `q/2`, `1<=q<2`, then

   `|phi_R(t)| <= det(I + 2 q t^2 B B^T/(pi^2 e^2))^(-1/(4q))`.

   The proof keeps arbitrary self-block phases and original-coordinate product structure. The `q=2` version is unconditional.

2. **Sharp Hausdorff--Young.** In the same source-pinned report, with Fourier convention `hat f(s)=int exp(isx) f(x) dx`, for `p=3/2`, `p'=3`,

   `||hat f||_3 <= (2pi)^(1/3) C_HY ||f||_(3/2)`,

   where

   `C_HY=(3/2)^(1/3) 3^(-1/6)=3^(1/6)2^(-1/3)`.

3. **Universal half-Riesz conversion.** `yspennstate/math-open-problems@bf7bff5c9b11cf495ccbcb09ef48549fd9c0d409`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/account03-B05-20260922T133738Z-qform-r12/REPORT.md`. If a probability density `p` lies in `L^3`, then

   `sup_t int |t-u|^(-1/2) p(u) du <= H_3 ||p||_3^(3/4)`,

   `H_3=8 sqrt(2)/3^(3/4)`.

   The same report records the scalar-square coarea inequality

   `p_[a(X+m(Y))^2+R(Y)](t) <= |a|^(-1/2) E|t-R(Y)|^(-1/2)`

   for an original independent coordinate `X` of density cap one; the random shift `m(Y)` is allowed.

4. **Compatible account04 aggregate theorem.** `yspennstate/math-open-problems@c233995d6abf7574b8b1a876cac244b1b91e3c38`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260922T132134Z-account04-B20-QFORM-r1/REPORT.md`.

Fresh corrections consumed include the failure of law-uniform pointwise quadratic-phase decay, fiber-sup dimension loss, no independence after spectral rotation, the single-Schur extraction failure, conditional-cap failure, local-cross/rank-three dichotomy failure, fiberwise trace failure, and the phase-Wiener absolute-value failure. None is used as a premise.

## 3. General square-assisted determinant theorem

Let `Y=(Y_1,...,Y_m)` have independent coordinates with densities bounded by one. Let `R(Y)=Y^T C Y` be a real quadratic form. Choose disjoint original-coordinate sets `I,J` and write `B=C[I,J]`. Let `X` be one additional original coordinate, independent of `Y`, with density bounded by one. Let `a!=0` and let `m(Y)` be any measurable real function finite almost surely.

### Theorem `QFORM-SQUARE-ASSISTED-L32-v1`

Fix `1<=q<=2`. For `q<2`, assume the diagonal of the orthogonal projection onto `range(B)` is at most `q/2` on one side of the cut; for `q=2` no leverage condition is needed. Suppose `B` has at least `r` singular values at least `sigma>0` and

`r > 4q/3`.

Then

`Q = a (X+m(Y))^2 + R(Y)`

has an essentially bounded density and

`||p_Q||_infinity <= C(q,r) / sqrt(|a| sigma)`,                    (3.1)

where

`nu = 3r/(8q)`,

`A(q,r)=sqrt(pi) Gamma(nu-1/2)/Gamma(nu)`,

and

`C(q,r)=2^(5/2) 3^(-5/8) q^(-1/4) sqrt(e A(q,r)).`               (3.2)

The proof yields absolute continuity and the essential-supremum bound. It does **not** by itself prove that the density is continuous when the square shift `m(Y)` depends on the residual variables.

### Proof

By the regularized determinant theorem and the `r` singular values,

`|phi_R(t)| <= (1 + beta^2 t^2)^(-r/(4q))`,                     (3.3)

where

`beta=sqrt(2q) sigma/(pi e)`.

Raise (3.3) to the `3/2` power. The hypothesis `r>4q/3` is exactly `nu>1/2`, so

`int_R |phi_R(t)|^(3/2) dt
 <= beta^(-1) int_R (1+s^2)^(-nu) ds
 = beta^(-1) A(q,r).`                                           (3.4)

Thus `phi_R in L^(3/2)`. Sharp inverse Hausdorff--Young gives an `L^3` density `p_R` with

`||p_R||_3
 <= (2pi)^(-2/3) C_HY ||phi_R||_(3/2)
 <= C_HY A(q,r)^(2/3)
       [e/(2 sqrt(2q) sigma)]^(2/3).`                            (3.5)

This already supplies absolute continuity of `R`; no pointwise scalar Fresnel estimate is being asserted.

Now apply scalar-square coarea conditionally on `Y`:

`p_Q(t) <= |a|^(-1/2) E |t-R(Y)|^(-1/2).`                       (3.6)

The half-Riesz inequality from the completed B05 report gives

`sup_t E |t-R|^(-1/2)
 <= H_3 ||p_R||_3^(3/4),
 H_3=8sqrt(2)/3^(3/4).`                                         (3.7)

Substituting (3.5) into (3.7) and simplifying

`C_HY^(3/4)=3^(1/8)2^(-1/4)`

produces exactly (3.1)--(3.2). QED.

### Threshold specialization

The most useful new endpoint is

`q=1, r=2`.

Only **two** cross singular values are then required, provided the corresponding physical range leverage is at most `1/2`. Here

`A(1,2)=sqrt(pi) Gamma(1/4)/Gamma(3/4)
       =5.2441151085842396...`

and

`C(1,2)=10.748739899781292... .`                                (3.8)

Therefore

`boxed(||p_Q||_infinity <= 10.748740 / sqrt(|a| sigma)).`        (3.9)

This is the exact gain of the present run: the determinant estimate alone with two `q=1` cross directions is only at the non-`L^1` Fourier endpoint, but it is in `L^(3/2)_t`; a single genuine scalar square converts that `L^3` residual density into an `L^infinity` output density.

For comparison, the unconditional `q=2` mechanism needs `r>=3` for the same `L^(3/2)->L^3` bridge.

## 4. Exact-rank-three genuinely rotated indefinite target instance

The theorem applies at the sharp **three-nonzero-eigenvalue** target, not only to a high-rank control.

Take one original coordinate `W` and eight further original coordinates split into two banks `I,J` of four coordinates each. Define an `8 x 2` frame with rows on `I`

`(1/2,0), (0,1/2), (-1/2,0), (0,-1/2)`

and rows on `J`

`(1/(2sqrt2),1/(2sqrt2)),
 (-1/(2sqrt2),1/(2sqrt2)),
 (-1/(2sqrt2),-1/(2sqrt2)),
 (1/(2sqrt2),-1/(2sqrt2)).`

Let its two column linear forms be `L_1,L_2`. Both columns are orthonormal, and each bank has frame operator `(1/2)I_2`.

Set

`R=2 L_1^2 - 2 L_2^2`,

`Q_*=2 (W + L_1/2)^2 + R.`                                    (4.1)

For the residual `R`, the physical cross block `B=C[I,J]` has exactly two nonzero singular values equal to one. Its range projection on `I` has every diagonal entry exactly `1/2`. Thus Theorem 3 applies with

`q=1, r=2, sigma=1, a=2`,

and gives

`boxed(||p_(Q_*)||_infinity <= 7.600506873...).`                 (4.2)

This bound holds for **every** choice of the nine independent coordinate laws with densities bounded by one.

The spectral check is exact. In the orthonormal three-dimensional span `(W,L_1,L_2)`, the quadratic matrix is

`[[2,1,0],
  [1,5/2,0],
  [0,0,-2]].`

Hence the three nonzero eigenvalues are

`(9+sqrt(17))/4`, `(9-sqrt(17))/4`, and `-2`,                    (4.3)

and all three have modulus strictly greater than one. The remaining six eigenvalues are zero. Thus this is an exact-rank-three indefinite target instance. It is genuinely rotated in the original product coordinates: both nontrivial residual spectral directions are spread across eight coordinates, the two physical banks are rotated relative to each other, and the heavy scalar coordinate is coupled to the distributed `L_1` direction.

The entire-range diffuse theorem does not cover this example because the original coordinate `W` has full range leverage one. The present proof nevertheless yields (4.2) without selecting independent spectral coordinates.

Continuity is **not claimed** from this proof. Essential boundedness and absolute continuity are proved.

## 5. Why this is not a disguised use of the refuted pointwise route

The source correction says that bounded scalar density does not imply a law-uniform pointwise estimate of the form

`|E exp(it lambda X^2)| <= C |t|^(-1/2)`.

Nothing here asserts that. The pointwise estimate (3.3) is the already proved **product cross-block determinant estimate**, whose proof uses original-coordinate Cauchy--Schwarz plus geometric Brascamp--Lieb and whose hypotheses include a physical cross block. The present new step is integrated: (3.3) is placed in `L^(3/2)_t`, sharp Hausdorff--Young converts it to an `L^3` residual density, and decreasing singular-kernel integration spends that `L^3` norm. Phase-aligned fragmented scalar supports therefore do not invalidate the argument.

## 6. Actual application of compatible account04 mathematics

The designated `account04/B04` artifact was absent, but the completed compatible `account04/B20` theorem supplies the other currently live aggregate branch. In its notation, for disjoint original-coordinate aggregate blocks with coefficient vectors `e,c,d`, if the conditional quadratic has

`T=2aUV+alpha(w)U+H_w(V)+b(Z+theta_w(V))^2+G(w)`,

then its projection insertion gives

`||p_T||_infinity
 <= 8 / [sqrt(|ab|) ||d||_2 sqrt(||e||_2 ||c||_2)].`            (6.1)

Define the product-preserving aggregate parameter

`eta = |ab| ||d||_2^2 ||e||_2 ||c||_2.`                         (6.2)

Then the completed account04 result gives the actual inequality

`boxed(||p_T||_infinity <= 8 eta^(-1/2)).`                       (6.3)

Thus an eventual heavy-coordinate structural argument now has two quantitatively explicit exits that require no eigen-coordinate independence:

* **square-assisted Fourier exit:** produce a scalar-square coefficient/cross scale with `|a| sigma >= delta` and a leverage-valid two-cross residual; then (3.9) gives `||p||_infinity <=10.748740 delta^(-1/2)`;
* **aggregate hyperbolic-square exit:** produce the disjoint-bank parameter `eta>=delta`; then (6.3) gives `||p||_infinity <=8 delta^(-1/2)`.

This is a direct application of completed account04 mathematics to the same quantitative currency, not a claim that the structural extraction has been proved.

## 7. What remains unpaid

The full conjecture is still OPEN. The three-large-eigenvalue assumption by itself has not yet been shown to force a single favorable cut/pivot; current corrections explicitly refute several such local dichotomies.

The next B04 implication is therefore

`QFORM-SQUARE-ASSISTED-DETERMINANT-MIXTURE-v1`:

> Starting from the determinant-weighted/exterior mass supplied by the three-large-eigenvalue hypothesis, average the new `L^(3/2)_t -> L^3 -> half-Riesz` square-assisted mechanism over original-coordinate pivots and cuts, so that no tiny scalar pivot or one tiny principal/cross minor is paid. When regularized determinant mass concentrates on heavy coordinates, route that mass into the account04 aggregate hyperbolic-square parameter before taking reciprocal constants.

The paired-frame and local-cross corrections show why this must be a mixture/aggregation statement rather than “choose one good cut”. The present theorem supplies the analytic endpoint once such an aggregate certificate is available.

## 8. Integrity/status

Proved in this run:

- `QFORM-SQUARE-ASSISTED-L32-v1`, with explicit general constant (3.2);
- the `q=1,r=2` endpoint constant `10.748739899...`;
- the exact-rank-three rotated indefinite instance (4.1)--(4.3) with universal density bound `7.600506873...` for arbitrary admissible product laws;
- an explicit quantitative interface with the completed account04 aggregate theorem.

Not proved:

- the global determinant-mixture/heavy-coordinate extraction from the sole spectral hypothesis;
- the full QFORM conjecture;
- continuity in the shifted-square theorem or the explicit example;
- any law-uniform scalar pointwise Fresnel decay.

No novelty claim is made. Repository use did not establish native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
