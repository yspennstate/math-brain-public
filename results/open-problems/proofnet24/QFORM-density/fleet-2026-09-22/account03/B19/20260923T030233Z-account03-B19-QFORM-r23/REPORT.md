SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T03:02:33Z.
attacking: uniform square-root small-ball control for an arbitrary-diagonal physical hub with a nonzero aggregate star, then splice it into the current universal proof tree.

# account03/B19 r23 — arbitrary-diagonal hub small-ball theorem and current proof splice

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Owner control read at startup:** `yspennstate/math-research-brain@1068581415b9064b6b20d3fc3e26bf7c184f7426`, OWNER CONTROL revision `2026-09-22.15`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING ANALYTIC THEOREM / TARGET-LEVEL COLLAR IMPROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Target and correction boundary

The unrestricted target remains OPEN: for every `n`, every independent real coordinate family with marginal probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `Q=X^T A X`, or give a target-valid counterexample. Continuity is a separate requested conclusion and remains open globally.

This report uses no post-rotation independence, no law-uniform pointwise Fresnel decay, no arbitrary-joint rank-three coarea lemma, no positive conditional-projection-density moment, no worst-fiber supremum, and no claim that a single physical minor must carry aggregate spectral volume. The live corrections explicitly forbid all of those shortcuts.

The immediate current exact-rank-three collar is supplied by account03/B10 r23b, `yspennstate/math-open-problems@91759f77fcdf696a75d8e6c6ef398c03654b025a`: when the Pluecker disjointness mass satisfies `0<d<1/64`, either a scalar pivot already pays the density, or there is an ORIGINAL physical coordinate `i` with

`c_i>1/4`, `|A_ii|<1/64`, and `||A_{i,-i}||_2>sqrt(1023)/64`.       (1.1)

The previous zero-hub fractional theorem, account01/B03 r21 at `yspennstate/math-open-problems@4abbc0fca2936aa89d1259cceb66e881f01e5563`, proved useful `1/4`-Riesz control only when the hub diagonal was exactly zero and explicitly left the near-zero-diagonal hub bridge open. The first mathematical goal below is to remove that exact-zero restriction without treating the small nonzero coefficient as a perturbation.

A separate new warning from account01/B19 r12, `yspennstate/math-open-problems@8519812f42a34ba2612f61ff2d4c8fbbfad8c6ee`, is also incorporated: co-heavy rank-two banks can spread all grouped determinant mass over arbitrarily many tiny physical atoms, even with every physical diagonal zero. Therefore nothing below tries to recover a single large local minor from aggregate star/bank mass.

## 2. Linear projection input

I use the completed one-dimensional product-projection bound recorded in account01/B03 r21 (source there: account02/B04): if `Y=(Y_j)` has independent marginal densities at most one and `m != 0`, then

`||p_{m^T Y}||_infinity <= sqrt(2)/||m||_2`.                       (2.1)

Consequently, for

`C=2 m^T Y + beta`,                                                (2.2)

we have

`||p_C||_infinity <= M := 1/(sqrt(2)||m||_2)`.                    (2.3)

Only this genuine original-product linear projection fact is needed in the main lemma.

## 3. Main theorem: an arbitrary hub diagonal still has uniform square-root small-ball

Let `X` be one original coordinate, independent of the disjoint original-coordinate bank `Y`. Assume every original marginal density is at most one. Let

`R = a X^2 + X(2m^T Y + beta) + S(Y)`,                            (3.1)

where

- `a,beta` are arbitrary real numbers;
- `m != 0` is an arbitrary deterministic vector;
- `S(Y)` is an arbitrary measurable real function, in particular it may contain **all** quadratic, affine and constant terms on the residual bank.

No sign or size assumption is placed on `a`. This is exactly the form of a physical source-coordinate hub with an arbitrary self coefficient and arbitrary same-side curvature behind its cross row.

### Theorem 3.1 — `QFORM-ARBITRARY-HUB-SQRT-SMALLBALL-v1`

For every `z in R` and every `eps>0`,

`P(|R-z|<=eps)
 <= 4*2^(1/4) ||m||_2^(-1/2) eps^(1/2).`                         (3.2)

More precisely, if `M=||p_C||_infinity` for `C=2m^TY+beta`, then

`P(|R-z|<=eps) <= 4 sqrt(2) sqrt(M eps).`                         (3.3)

This estimate is uniform in `a`, in `S`, in all signs, in all fragmented supports, and in the dimension of `Y`.

#### Proof

Fix `z` and put, for a realized `Y=y`,

`q_y(x)=a x^2 + c(y)x + s(y)-z`,
`c(y)=2m^T y+beta`.                                               (3.4)

For a parameter `eta>0`, split the small-ball event according to the physical derivative

`q_y'(X)=2aX+C`.                                                   (3.5)

### Far-slope contribution

Condition on the whole original bank `Y`. The polynomial `q_y` has at most two monotonicity branches. On the portion of either branch where `|q_y'|>=eta`, the inverse-image under `q_y` of the output interval `[-eps,eps]` has Lebesgue measure at most

`2 eps / eta`.                                                     (3.6)

There are at most two branches, and the density of `X` is at most one. Hence

`P(|R-z|<=eps, |2aX+C|>=eta | Y)
 <= 4 eps/eta`.                                                    (3.7)

Averaging over `Y` preserves (3.7).

### Near-slope contribution

Here do **not** condition on `Y`; instead condition on the genuinely independent original scalar `X`. By (2.3), for every fixed `x`,

`P(|2ax+C|<eta | X=x) <= 2M eta`.                                (3.8)

Therefore

`P(|2aX+C|<eta) <= 2M eta`.                                      (3.9)

Combining (3.7) and (3.9),

`P(|R-z|<=eps)
 <= 4 eps/eta + 2M eta`.                                         (3.10)

The optimizer is

`eta=sqrt(2eps/M)`.                                                (3.11)

Substitution gives

`P(|R-z|<=eps) <= 4 sqrt(2) sqrt(M eps)`.                         (3.12)

Finally use (2.3):

`4 sqrt(2) sqrt(M)
 <=4 sqrt(2) [1/(sqrt(2)||m||)]^(1/2)
 =4*2^(1/4)||m||^(-1/2)`.                                        (3.13)

This proves (3.2). QED.

### Why this avoids the former obstruction

The proof does not set `a=0`, however small `a` may be. The potentially dangerous stationary set is exactly the near-slope event `|2aX+C|<eta`; its probability is paid by the independent random slope `C` before any reciprocal derivative is taken. Thus the method survives arbitrary cancellation between `aX^2`, the mixed hub term, and the arbitrary same-side quadratic function `S(Y)`.

The estimate is intentionally a `sqrt(eps)` bound, not a density bound. A single star such as `2XY` can have a logarithmically singular density, so one should not expect one physical hub alone to give an `O(eps)` small-ball estimate uniformly.

## 4. Quarter-Hoelder and fractional-Riesz consequences

Let

`H_2 = 4*2^(1/4)||m||^(-1/2)`.                                   (4.1)

Then (3.2) says

`P(|R-z|<=rho) <= min(1,H_2 rho^(1/2))`.                         (4.2)

For every `rho>0`,

`min(1,H_2 rho^(1/2)) <= H_2^(1/2) rho^(1/4)`.                  (4.3)

Hence

`boxed:
 sup_z P(|R-z|<=rho)
 <=2^(9/8)||m||^(-1/4) rho^(1/4).`                               (4.4)

There is also a useful fractional-potential form. For `0<alpha<1/2`, the layer-cake identity and (4.2), split at `rho=H_2^(-2)`, give

`sup_z E|R-z|^(-alpha)
 <= [1/(1-2alpha)] H_2^(2alpha).`                                (4.5)

At `alpha=1/4`,

`boxed:
 sup_z E|R-z|^(-1/4)
 <=4*2^(1/8)||m||^(-1/4)
 =4.36203093066... ||m||^(-1/4).`                                (4.6)

This extends the exact-zero-hub quarter-Riesz theorem to **every** real hub diagonal `a`. The constant is slightly worse than the zero-diagonal endpoint, but it is uniform through `a=0` and through all nonzero values.

## 5. Splice into an indefinite physical-pair transducer

The completed account02/B03 indefinite-pair logarithmic transducer, source-pinned in account01/B03 r21, states the following. After completing an invertible indefinite ORIGINAL-coordinate physical pair `B`, put

`D=|det B|`, `kappa=sigma_min(B)`.                                (5.1)

If the exact Schur residual `R` obeys

`sup_z P(|R-z|<=rho) <= H rho^(1/4)`                              (5.2)

for every `rho>0`, then

`||p_Q||_infinity
 <=3*2^(4/3) H^(2/3) D^(-1/3) kappa^(-1/6).`                    (5.3)

Apply (4.4) to any residual that contains an ORIGINAL-coordinate hub of the form (3.1). We obtain:

### Corollary 5.1 — `QFORM-INDEFINITE-PAIR-ARBITRARY-HUB-v1`

If, after exact completion of an invertible indefinite original-coordinate pair, the residual has a physical hub whose cross row to a disjoint original-coordinate bank is `m !=0`, with **arbitrary** residual hub diagonal and arbitrary remaining quadratic curvature, then

`boxed:
 ||p_Q||_infinity
 <= 3*2^(25/12)
    D^(-1/3) kappa^(-1/6) ||m||_2^(-1/6)
 <12.714 D^(-1/3) kappa^(-1/6)||m||_2^(-1/6).`                   (5.4)

No near-zero assumption is needed. This strictly removes the exact-zero self-coefficient restriction from the corresponding B03 star splice.

For a concrete target-level threshold,

`D>=1/64`, `kappa>=1/64`, `||m||_2>=1/4`                          (5.5)

imply

`boxed: ||p_Q||_infinity<129.`                                   (5.6)

This branch allows arbitrary additional spectrum and arbitrary couplings outside the completed pair/hub packet, because they are retained in `S(Y)` and in the exact Schur residual.

The conclusion of this branch is an essentially bounded density. Continuity is **not** claimed here.

## 6. Actual application to the live exact-rank-three small-Pluecker collar

The current account03/B10 reduction (source `91759f77fcdf696a75d8e6c6ef398c03654b025a`) gives, in the only unpaid collar `0<d<1/64`, an ORIGINAL physical hub satisfying (1.1), unless a scalar-pivot exit has already paid the full density.

Take

`m=A_{i,-i}`.                                                      (6.1)

Then

`||m||_2 > m_0 := sqrt(1023)/64 =0.4997557997...`.               (6.2)

Theorem 3.1 therefore gives the **entire remaining collar**, without deleting the small nonzero `A_ii`, the uniform target-level estimate

`boxed:
 sup_z P(|Q-z|<=eps)
 <6.729 sqrt(eps).`                                               (6.3)

Equivalently,

`boxed:
 sup_z P(|Q-z|<=rho)
 <2.594 rho^(1/4),`                                               (6.4)

and

`boxed:
 sup_z E|Q-z|^(-1/4)<5.188.`                                     (6.5)

These are not yet an `L^infinity` density bound for that collar, so the exact-rank-three theorem remains open. They do, however, remove the **analytic near-zero-hub bridge**: the surviving issue is now to supply one additional product-preserving smoothing channel, not to control the arbitrary nonzero hub diagonal itself.

This is useful in every proof route that encounters the collar behind a genuine indefinite pair, scalar square, or other completed singularity transducer.

## 7. Designated partner account04/B19 applied to an actual inequality

The designated partner account04/B19 theorem `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`, canonical source

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`,

proves in its **residual-diffuse exact-null-coloop** scope, for `0<D_res<=1`,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`,                        (7.1)

with a continuous density. Therefore on the actual quantitative range

`e^(-8)<=D_res<=1`,                                                (7.2)

we have

`log(e/D_res)<=9`, hence

`boxed: ||p_Q||_infinity<102.`                                   (7.3)

At `D_res=0` the same source's completed endpoint is `<5.844`, and for `D_res>=1` its fixed-exponent estimate is `<11.748`. Thus the designated partner pays the exact-null-coloop branch on

`D_res in {0} union [e^(-8),infinity)`                            (7.4)

at an actual inequality, within precisely its proved scope. I do not promote it to near-coloops or to a non-diffuse residual.

## 8. Compact correction-safe end-to-end proof map after this run

A current conditional assembly is now:

1. **Diagonal control.** Three large physical diagonal coefficients give a same-sign pair and the elementary `pi` bound, only in that proved scope.
2. **Physical/localized blocks and nonzero pivots.** Existing pair-log, rank-two affine half-Riesz, cross-transverse, definite-pair, grouped `2+1`, and scalar-pivot theorems pay their explicit quantitative resource branches without rotating independence.
3. **Diffuse spectral packets.** The proved Fresnel--Brascamp--Lieb Theorem F pays an exact rank-three packet with normalized physical-row leverages at most `1/2`; volume-sampling/cross-block theorems pay their stated higher-volume branches.
4. **Exact rank-three Pluecker split.** Current B10 work pays `d>=1/64` by a continuous `<24` branch and `d=0` by `<331`. In `0<d<1/64`, a non-small scalar pivot pays `<512`; otherwise one gets the physical near-null star (1.1).
5. **New analytic payment.** The whole near-null-star collar now has the uniform square-root small-ball estimate (6.3), regardless of the nonzero value of `A_ii`. Whenever a completed external singularity transducer leaves such a hub in its residual, Corollary 5.1 produces a true linear small-ball/density bound.
6. **Null-coloop boundary.** The designated partner gives the continuous estimate (7.1), with the concrete `<102` range (7.3).
7. **Co-heavy aggregate warning.** The account01/B19 target family proves that single-row determinant extraction can fail even in a safe target family. Whole-bank aggregation must precede reciprocal local payment in that branch.

No step above proves the unrestricted theorem, and no continuity statement is claimed outside source scopes that actually establish it.

## 9. First remaining implication

The first exact-rank-three analytic debt is now more precise:

### `QFORM-SQRT-COLLAR-TO-LINEAR-SMOOTHING-v1` — OPEN

Starting from an exact-rank-three small-Pluecker survivor with

`c_i>1/4`, `|A_ii|<1/64`, `||A_{i,-i}||_2>sqrt(1023)/64`,           (9.1)

and therefore the proved uniform estimate

`sup_z P(|Q-z|<=eps)<6.729 sqrt(eps)`,                             (9.2)

extract or retain one additional **original-product** smoothing currency that upgrades (9.2) to `O(eps)` without:

- conditioning away the aggregate star;
- replacing a projection by independent rotated coordinates;
- selecting one reciprocal minor from aggregate volume;
- or deleting the small nonzero hub square.

The best current candidates are: an indefinite physical pair whose Schur residual keeps a nonzero hub star (now paid by Corollary 5.1); a diffuse mixed-hub/Fresnel packet; or an aggregate co-heavy bank normal form. The analytic nonzero-hub obstruction itself is no longer the missing step.

For the full arbitrary-rank target, the separate additional-spectrum/descent compiler also remains open.

## 10. Status

- `QFORM-FULL`: **OPEN / NOT PROVED / NOT DISPROVED**.
- New `QFORM-ARBITRARY-HUB-SQRT-SMALLBALL-v1`: **PROVED SUPPORTING THEOREM**.
- New `QFORM-INDEFINITE-PAIR-ARBITRARY-HUB-v1`: **PROVED TARGET-LEVEL BRANCH**, conditional only on its explicit pair/star resources.
- Exact-rank-three small-Pluecker collar: **uniform square-root small-ball now proved; bounded density still OPEN**.
- Global continuous density: **OPEN**.
