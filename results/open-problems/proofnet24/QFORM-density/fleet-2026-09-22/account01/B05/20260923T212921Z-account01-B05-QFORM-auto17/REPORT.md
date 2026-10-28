SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T21:29:21Z.
attacking: the source-shared puncture b->0 in the null-heavy-hub/two-sheet coarea normal form; replace the previous power loss by the sharp logarithmic annulus cost and identify the exact unsummed factor.

# account01/B05 auto17 — logarithmic puncture bridge from exact annulus integration

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** quadratic coarea bound.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `NEW SUPPORTING COAREA THEOREM / TARGET-VALID DIFFUSE PUNCTURE IMPROVED FROM POWER TO LOG / FULL QFORM OPEN`.  
**Regularity:** only an essentially bounded density is proved by the new route; continuity is not claimed. The unrestricted full-target continuity statement remains OPEN.

## 1. Exact target and first unpaid implication

The owner target is unchanged: for arbitrary finite `n`, independent real original coordinates with probability densities at most one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite bound for the essential supremum of the density of `X^T A X`, or give a valid counterexample. No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis independence, or post-rotation independence is available.

The previous B05 run isolated the canonical source-shared puncture

`Q_b = 2 H L + 2 b L P + V^2`,                                     (1.1)

where `H` is a genuinely independent cap-one physical scalar and `(L,P,V)` are simultaneous orthonormal linear forms of the same original-coordinate product bank. For every real `b`, the homogeneous matrix of (1.1) has nonzero spectrum

`{ +sqrt(1+b^2), -sqrt(1+b^2), 1 }`,                              (1.2)

so this family already satisfies the exact three-large-eigenvalue target. The endpoint `b=0` is paid by the completed null-hub square theorem, while the preceding projected-crossing estimate deteriorated like `|b|^(-1/3)` in the diffuse near-coloop regime. The first unpaid implication is uniformity through `b->0` without treating `bP` as a small random perturbation.

This run changes the quantitative mechanism: it does not optimize the projected-crossing determinant again. Instead it integrates the hub-slope plateau exactly against the one-dimensional `L` density and combines that with the completed account02/B05 curved shell estimate.

## 2. Completed partner input used at an actual inequality

The completed partner report

`yspennstate/math-open-problems@39f45eeebf3d7a9609c4e26c14f2f8ad5b6b3fb1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T203105Z-account02-B05-QFORM-auto11d/REPORT.md`

uses the proved two-bank curved-tube theorem. In its notation, let two independent banks

`A=(L_A,V_A,P_A)`, `B=(L_B,V_B,P_B)`

have `(L,V)` marginal density caps `M_{2,A},M_{2,B}` and three-dimensional density caps `M_{3,A},M_{3,B}`. Put

`(L,V,P)=A+B`,
`K_2=(M_{2,A}M_{2,B})^(1/2)`,
`K_3=(M_{3,A}M_{3,B})^(1/2)`,
`K=K_2+K_3`.

Let `H` be independent of both banks with density cap `m`. For

`Q=2HL+2bLP+V^2+alpha L^2+beta L+gamma_0`, `b!=0`,              (2.1)

and an interval `I` of length `h`, the partner's proof gives on every dyadic shell `0<r<=1`

`boxed{
 P(Q in I, r<=|L|<=2r)
 <= A h sqrt(r/|b|),
 A=(C_T/4) K,
}`                                                                  (2.2)

where `C_T` is the absolute constant from the source-pinned two-bank curved-tube theorem. This is the partner result spent below at an actual shell inequality.

Two elementary bounds coexist with (2.2). If `L` has density cap `M_L`, then conditioning on the light bank gives

`P(Q in I | L,V,P) <= m h/(2|L|)`.                                (2.3)

Consequently on a shell

`P(Q in I, r<=|L|<=2r)
 <= (m h/(2r)) P(r<=|L|<=2r)
 <= m M_L h.`                                                       (2.4)

Also, without using the shell probability,

`P(Q in I, |L|>=R) <= m h/(2R).`                                  (2.5)

The new point is to **not** count (2.4) once per dyadic scale across the whole middle plateau.

## 3. Main calculus lemma — exact logarithmic plateau integration

### Theorem 3.1 — `QFORM-PUNCTURED-SHELL-PLATEAU-INTEGRAL-v1`

Assume the setting of Section 2, and suppose additionally that `L` has density cap `M_L`. Set

`A=(C_T/4)K`,
`B=m M_L`,
`C=m/2`,
`r_- = |b| (B/A)^2`,
`r_+ = C/B = 1/(2M_L)`.                                          (3.1)

Assume the curved-shell estimate (2.2) is available for all shells below `r_+` (this is automatic whenever `r_+<=1`). Then every interval `I` satisfies

`boxed{
 P(Q in I)
 <= B |I| [ 2+sqrt(2) + log_+(r_+/r_-) ].
}`                                                                  (3.2)

Equivalently,

`boxed{
 ||p_Q||_(infinity,ess)
 <= m M_L [2+sqrt(2)
   + log_+( C_T^2 K^2 /(32 |b| m^2 M_L^3) )].
}`                                                                  (3.3)

Here `log` is the natural logarithm.

### Proof

First suppose `r_-<r_+`. Split the `L` axis into three regions.

**Small region `0<|L|<r_-`.** Cover it by the disjoint dyadic shells

`r_j<=|L|<=2r_j`, `r_j=r_- 2^(-j-1)`, `j>=0`.

By (2.2),

`P(Q in I, shell_j)
 <= A h sqrt(r_j/|b|)
 = B h 2^(-(j+1)/2).`

Therefore

`P(Q in I, 0<|L|<r_-)
 <= B h sum_{j>=0}2^(-(j+1)/2)
 = (1+sqrt(2)) B h.`                                               (3.4)

**Middle region `r_-<=|L|<r_+`.** Here do not sum a scale-independent shell cap. Integrate the exact hub slope (2.3) against the honest one-dimensional marginal density `p_L<=M_L`:

`P(Q in I, r_-<=|L|<r_+)
 <= (m h/2) int_{r_-<=|l|<r_+} p_L(l)/|l| dl`
` <= m M_L h log(r_+/r_-)`
` = B h log(r_+/r_-).`                                             (3.5)

This is the entire logarithmic cost. No dyadic counting loss remains.

**Large region `|L|>=r_+`.** By (2.5),

`P(Q in I, |L|>=r_+) <= C h/r_+ = B h.`                           (3.6)

Adding (3.4)--(3.6) proves (3.2).

If `r_- >= r_+`, use (2.2) on dyadic shells below `r_+`. Since

`A sqrt(r_+/|b|)=B sqrt(r_+/r_-)<=B`,

the whole small region costs at most `(1+sqrt(2))Bh`; the large region again costs at most `Bh`. Thus (3.2) remains true with the logarithm replaced by zero. Finally

`r_+/r_-
 = (C/B) A^2/(|b|B^2)
 = C_T^2 K^2/(32 |b| m^2 M_L^3),`

which gives (3.3). Since the bound is linear in the length of every interval, the output law is absolutely continuous with the displayed essential density cap. QED.

### Why this is stronger than the previous punctured summation

The completed account02/B05 global theorem obtained a power loss `|b|^(-1/3)` by optimizing a small-shell `sqrt(R/|b|)` term against the large-hub `1/R` term. The new estimate inserts the honest `L`-density cap between those mechanisms. The only surviving deterioration is the exact logarithmic integral

`m int_{r_-}^{r_+} p_L(l) dl/l`,                                  (3.7)

not a reciprocal power of `b`.

A same-hour early partner checkpoint independently noticed the logarithmic bridge by dyadic plateau counting. Equation (3.5) sharpens that counting step to direct annulus integration and removes the extra dyadic/base constants. The mathematical input used here remains the already-completed partner shell estimate (2.2).

## 4. Product-origin diffuse target family

Now apply Theorem 3.1 to the actual source-shared target family (1.1).

Let `X_j` be independent original coordinates with densities at most one, and let the rows

`w_j=(l_j,v_j,p_j) in R^3`

form a Parseval frame:

`sum_j w_j w_j^T=I_3`.                                             (4.1)

Thus `L=sum l_jX_j`, `V=sum v_jX_j`, `P=sum p_jX_j` are simultaneous orthonormal linear forms of the **same** product bank; no independence among `(L,V,P)` is asserted. Assume the diffuse row gate

`max_j ||w_j||^2 <= 1/64.`                                        (4.2)

The two-part Marcus--Spielman--Srivastava frame partition theorem gives a partition of the original coordinates into two independent banks `A,B` for which both partial Gram matrices lie between `a I_3` and `beta I_3`, where

`beta=(1/sqrt(2)+1/8)^2 = 33/64+sqrt(2)/8`,
`a=1-beta=(31-8sqrt(2))/64 = 0.3075983047... .`                    (4.3)

For either bank, the standard bounded-density projection theorem gives the concrete caps

`M_2 <= 2/a`,
`M_3 <= 2^(3/2) a^(-3/2).`                                       (4.4)

Indeed, whitening the bank coefficient matrix turns it into an orthonormal two- or three-dimensional projection, whose density cap is respectively `2` or `2^(3/2)`, while the Jacobian contributes the reciprocal square root of the bank Gram determinant. Hence

`K <= K_a := 2/a + 2^(3/2) a^(-3/2)
          = 23.0813970153... .`                                   (4.5)

The normalized scalar projection `L` satisfies

`M_L<=sqrt(2)`.                                                    (4.6)

Take the valid upper cap `M_L=sqrt(2)` in Theorem 3.1, with `m=1`. Since

`r_+=1/(2sqrt(2))<1`,

the shell theorem is available throughout the needed small region. Therefore, for every `b!=0`,

`boxed{
 ||p_(Q_b)||_(infinity,ess)
 <= sqrt(2) [2+sqrt(2)
   + log_+( C_T^2 K_a^2 /(64 sqrt(2) |b|) )].
}`                                                                  (4.7)

This is `O(1+log(1/|b|))` as `b->0`, with no moment or support assumption and with full same-source overlap in all three projected coordinates.

At the exact endpoint `b=0`, `(L,V)` is a two-dimensional orthonormal product projection, so `||p_(L,V)||_infinity<=2`. The completed account02/B05 theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` gives

`boxed{
 ||p_(Q_0)||_(infinity,ess)
 <= 7.761982175235 * 2^(2/3)
 = 12.3213786704... .
}`                                                                  (4.8)

Thus every fixed member of the punctured family and the endpoint itself are paid; the only missing statement is a **uniform** cap as `b->0` through nonzero values.

## 5. Exact spectrum and near-coloop interpretation

In the orthonormal coordinates `(H,L,P,V)`, the homogeneous matrix of (1.1) is

`[[0,1,0,0],
  [1,0,b,0],
  [0,b,0,0],
  [0,0,0,1]].`                                                     (5.1)

The first `3x3` block has characteristic polynomial

`-lambda(lambda^2-(1+b^2))`,

so (1.2) follows exactly. Hence (4.7) is a target-valid supporting theorem, not a toy form outside the spectral hypothesis.

After rotating only for deterministic analysis, the normalized active hub vector has physical-H leverage

`c=1/(1+b^2)`,

and the near-coloop defect is

`rho=1-c=b^2/(1+b^2).`                                             (5.2)

For `0<|b|<=1`,

`log(1/|b|)=1/2 log((1-rho)/rho) <= 1/2 log(1/rho).`               (5.3)

Therefore the new diffuse puncture bound is

`||p_(Q_b)||_infinity = O(1+log(1/rho))`                            (5.4)

as `rho->0`. On the comparable diffuse heavy-hub branch, the earlier B05 projected-crossing result was

`||p_Q||_infinity <35.51 rho^(-1/6)`.

Thus this run replaces a power singularity by a logarithmic one on the canonical null-heavy-hub/source-shared puncture.

## 6. The logarithmic debt is concentrated at the quadratic critical level

The completed account02/B05 theorem also supplies, when the interval center is separated from the quadratic critical level by at least one, the stronger estimate

`P(Q_b in I)
 <= |I| { (C_T/4) R [K_2(1+2log2+log_+(1/(|b|R)))+K_3]
          +1/(2R) }`                                              (6.1)

for every `0<R<=1` in the present `m=1` normalization.

With the diffuse bank caps (4.4), choose

`L_b=1+log_+(1/|b|)`, `R=L_b^(-1/2)`.

Then `log_+(1/(|b|R)) <= log_+(1/|b|)+(1/2)log L_b <= (3/2)L_b`, so (6.1) gives

`boxed{
 p_(Q_b)(t) <= C_a sqrt(1+log_+(1/|b|))
}`                                                                  (6.2)

for almost every output level `t` at distance at least one from the critical level, where `C_a<infinity` is an absolute constant depending only on the fixed MSS threshold through (4.4) and on `C_T`.

Thus the full logarithmic deterioration in (4.7) is localized to the critical/two-sheet window. Away from it, the same completed partner geometry already improves the puncture cost to square-root logarithmic.

## 7. Precise missing factor

The remaining factor is now explicit. In the intermediate annulus

`r_- << |L| << r_+`,                                               (7.1)

the curved two-bank estimate (2.2) is more expensive than the independent-hub slope estimate, while the large-`L` slope estimate has not yet begun to decay. The present proof therefore pays exactly

`m int p_L(l)/(2|l|) dl`,                                          (7.2)

which is logarithmic under only the marginal cap `p_L<=M_L`.

To close the puncture uniformly one needs a **product-provenance gain on this middle annulus**. Concretely, it would suffice to replace the scale-flat estimate

`P(Q in I, r<=|L|<=2r) <= mM_L |I|`                               (7.3)

through the entire interval `r_-<r<r_+` by

`P(Q in I, r<=|L|<=2r) <= mM_L |I| omega_b(r)`                     (7.4)

with

`sum_{dyadic r in (r_-,r_+)} omega_b(r) <= C`                      (7.5)

uniformly as `b->0`. Any fixed positive power gain in distance from either crossover would suffice. Generic joint-density caps, bounded conditional densities, or unrestricted X-ray bounds cannot supply (7.4): the live correction system contains exact curved-shear counterexamples to precisely those relaxations. The new obligation is therefore source-linear/product-specific, not another marginal-density estimate.

I record the next implication as

**`QFORM-SHARED-PUNCTURE-MIDDLE-ANNULUS-GAIN-v1`.**  
For simultaneous orthonormal product projections `(L,P,V)`, prove a summable improvement of (7.3) on the middle annulus for `2HL+2bLP+V^2`, uniformly `b->0`, or produce a target-valid counterexample. The estimate must spend the fact that `P,L,V` are linear forms of the same independent coordinates before collapsing to arbitrary projected/conditional density data.

## 8. Corrections respected and scope

This proof does not use pointwise quadratic-phase decay, does not rotate and declare spectral coordinates independent, does not take an unrestricted curved-fiber supremum, does not use moments or support, and does not treat `bP` as a small random perturbation. The sole rotation in Section 5 is deterministic spectral bookkeeping after the probability estimate is already proved in original-coordinate banks.

The theorem proves only essential boundedness in its stated diffuse puncture scope. It does not prove continuity there. It does not close non-diffuse high-leverage leaves, arbitrary nonzero hub diagonal, or the unrestricted owner target. Full QFORM and full-target continuity remain OPEN.

## 9. Source pins

- Completed designated partner: `yspennstate/math-open-problems@39f45eeebf3d7a9609c4e26c14f2f8ad5b6b3fb1`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T203105Z-account02-B05-QFORM-auto11d/REPORT.md`.
- Source two-bank curved tube: `yspennstate/math-open-problems@5e23223ed8626d8df8343d2d26879c08cf139093`, `proofnet24/QFORM-density/interactive/20260923T202245Z-two-bank-curved-tube/REPORT.md`.
- Endpoint null-hub theorem: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T200516Z-account02-B05-QFORM-auto11c/REPORT.md`.
- Previous own diffuse projected-crossing comparison: `yspennstate/math-open-problems@35c8dcccdfd52b14eefbdc31f81dbc56a466231d`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T172848Z-account01-B05-QFORM-auto14/REPORT.md`.

Independent review of the new logarithmic annulus integration is PENDING. Full QFORM is OPEN.
