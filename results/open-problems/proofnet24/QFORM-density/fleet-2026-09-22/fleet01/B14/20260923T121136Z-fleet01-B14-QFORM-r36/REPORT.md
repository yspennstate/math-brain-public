SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T12:11:36Z.
attacking: protected-smoother block localization—retain one whole product block through the singular random-slope step, localize every complementary bank coordinate with zero tax, and optimize the completed fleet02/B14 r34 compiler on a strict full-target fragmented family.

# fleet01/B14 r36 — protected-smoother localization and optimized partner compiler

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Worker:** fleet01/B14  
**Status:** NEW SUPPORTING ZERO-LOSS LOCALIZATION THEOREM + SHARPENED TARGET-VALID PARTNER APPLICATION; FULL QFORM OPEN.  
**Execution:** WITHOUT_VERIFIED_BRAIN. Continuity for the unrestricted target remains separate.

## 1. Fresh control and sources


The completed designated-partner result actually applied is fleet02/B14 r34:

`yspennstate/math-open-problems@ee5472663f2f7934749ac90f2a0305a4cbda37b0`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T112750Z-fleet02-B14-QFORM-r34/REPORT.md`.

Its theorem `QFORM-ARBITRARY-SELF-RANDOM-SLOPE-MASS-v1` gives the following. Let an outer pair of ORIGINAL coordinates have an invertible indefinite symmetric block `C`, with

`D=|det C|`, `kappa=sigma_min(C)>0`.

After exact completion of that pair, suppose the remaining positive bank submeasure has total mass `m`, and the remainder is

`Y=hX^2+X S(V)+R(V)`,

where `X` is an independent cap-one ORIGINAL coordinate, `h` is arbitrary, `R` may be arbitrarily correlated with `S`, and the unnormalised slope pushforward `S_#nu` has density cap `L`. Put `H=L/m`. Then

`||p_Q^sub||_inf`
` <= m inf_(q>0) { 8 q^(-1/2) sqrt(H/kappa) + D^(-1/2) J(q) },`       (1.1)

where

`J(q)=log(2q)+C0,                         q>=1/2,`

`C0=2+sqrt(2*pi*e) erfc(1/sqrt(2))`
`  =3.311359084837597...`.                                            (1.2)

The small-q formula is the partner's incomplete-gamma expression. The partner theorem is uniform in the self coefficient `h`, all slope translations and the correlated remainder; it uses no moments or support bounds.

The newer fleet02/B14 r35 artifact visible during this run was still only an early checkpoint, not a completed dependency. I therefore use completed r34 only.

## 2. New theorem: protected-smoother block localization

The single-coordinate anchor is not necessary. One may retain an arbitrary whole product block as the smoother and fragment/localize the entire complementary bank with exactly zero change in the r34 constant.

### Theorem 2.1 — `QFORM-PROTECTED-SMOOTHER-BLOCK-LOCALIZATION-v1`

Let `V=(V_j)_(j in K)` be independent cap-one ORIGINAL-coordinate probability variables, and let `W` be any independent bank. Let

`Z=c^T V`, `c !=0`,

and assume `Z` has density `g` with

`||g||_inf <= M`.                                                     (2.1)

Let the `W` law be decomposed into any finite or countable family of positive submeasures

`nu_W=sum_alpha nu_alpha`, `m_alpha=nu_alpha(1)`, `sum_alpha m_alpha=1`. (2.2)

No normalization of the pieces is performed. For arbitrary measurable `T_alpha` and arbitrary translations `beta_alpha`, consider on piece `alpha` the slope

`S_alpha(V,W)=beta_alpha+c^T V+T_alpha(W)`.                         (2.3)

Then the unnormalised pushforward slope density satisfies

`boxed: ||d(S_alpha#(mu_V tensor nu_alpha))/ds||_inf <= M m_alpha.`   (2.4)

Consequently, for every arbitrary self coefficient `h_alpha`, every arbitrary correlated remainder `R_alpha(V,W)`, and the same completed physical pair `(D,kappa)`, r34 gives

`||p_(Q,alpha)^sub||_inf`
` <= m_alpha B(D,kappa,M),`                                         (2.5)

where

`B(D,kappa,M)`
` := inf_(q>0) {8 q^(-1/2)sqrt(M/kappa)+D^(-1/2)J(q)}.              (2.6)

Positive summation therefore yields

`boxed: ||p_Q||_inf <= B(D,kappa,M),`                               (2.7)

**the identical whole-bank compiler constant**, independent of the number, masses, locations, separations or diameters of the localized `W` pieces.

#### Proof

Let `tau_alpha=T_alpha#nu_alpha`; it is a finite positive measure of total mass `m_alpha`. The slope density is simply

`h_alpha(s)=int g(s-beta_alpha-u) tau_alpha(du)`.                   (2.8)

Hence `h_alpha(s)<=M m_alpha`, proving (2.4). In partner notation, `L_alpha<=Mm_alpha`, so `H_alpha=L_alpha/m_alpha<=M`. Equation (1.1) is homogeneous in `m_alpha`; for every fixed `q`,

`||p_(Q,alpha)^sub||_inf`
` <=m_alpha[8q^(-1/2)sqrt(M/kappa)+D^(-1/2)J(q)].`                 (2.9)

Take the infimum in `q` and sum over `alpha`; `sum m_alpha=1`. This proves (2.7). QED.

### Why this is a localization theorem rather than a support assumption

The protected block `V` itself may already have arbitrarily remote fragments, disconnected or unbounded support, and no moments. It is never normalized on individual fragments. Its full linear projection is the smoother. The complementary bank `W` may simultaneously be split into arbitrary finite/countable spatial fragments. Outside ORIGINAL coordinates may be conditioned first; their effect is only to change `beta_alpha` and `R_alpha`, to which the theorem is uniform.

For product `V`, two law-uniform caps available in the current QFORM corpus are

`M <= 1/||c||_inf`                                                  (2.10)

(by conditioning on the largest coefficient coordinate), and the source-pinned product-projection estimate

`M <= sqrt(2)/||c||_2`.                                             (2.11)

Thus one can protect a diffuse block rather than one heavy scalar anchor. In the common Schur slope `c=2a_K`,

`M <= min{1/(2||a_K||_inf), 1/(sqrt(2)||a_K||_2)}.`                (2.12)

This strictly interpolates between a heavy-coordinate anchor and a whole diffuse smoothing bank while keeping all complementary localization free.

## 3. Closed-form log-branch choice for the completed partner theorem

The r34 report displayed the simple choice `q=1`. In the logarithmic branch one can do better without any new analytic premise.

Assume `H>0` and choose

`q_* = 16 D H/kappa`.                                               (3.1)

When `q_*>=1/2`, this lies in the explicit branch (1.2). Substitution gives

`8 q_*^(-1/2)sqrt(H/kappa)=2/sqrt(D)`,                             (3.2)

and therefore

`boxed:
 B(D,kappa,H)
 <= D^(-1/2)[2+C0+log(32 D H/kappa)].
`                                                                       (3.3)

At the boundary `32DH/kappa=1`, choosing `q=1/2` gives the same value. For `32DH/kappa<1`, the safe boundary choice is

`B(D,kappa,H)
 <=8sqrt(2H/kappa)+C0/sqrt(D).`                                    (3.4)

Equation (3.3) is only a choice from the completed partner infimum; no new Fourier or coarea estimate is asserted.

The important localization feature is that (3.3) can be used with the **same `H` on every piece** in Theorem 2.1, so optimization and positive mixture summation commute exactly.

## 4. Actual full-target inequality: a strict rational fragmented family

Consider the cap-one laws

`E_N = union_(j=1)^N [4^j,4^j+1/N]`,                               (4.1)

with `V_1,V_2` having density `1_(E_N)`; let `U_1,U_2,X` be any independent cap-one probability variables. Define

`Q_N = 4 U_1U_2 -3X^2 +2X V_1+2X V_2 +V_1^2+V_2^2`.              (4.2)

Its coefficient matrix is the direct sum of

`C=[[0,2],[2,0]]`

and

`B=[[-3,1,1],[1,1,0],[1,0,1]].`                                   (4.3)

The exact spectra are

`spec(C)={-2,2}`,                                                   (4.4)

`spec(B)={1,-1-sqrt(6),-1+sqrt(6)}`.                              (4.5)

Hence (4.2) is genuinely inside the full three-large-eigenvalue target, with room to spare. All matrix coefficients and fragment endpoints are rational.

Complete the outer pair. Then

`D=4`, `kappa=2`, `h=-3`,
`S(V)=2(V_1+V_2)`, `R(V)=V_1^2+V_2^2`.                            (4.6)

Because convolution with a probability density cannot increase `L^infinity`, `V_1+V_2` has density cap at most one, so `S` has cap

`H<=1/2`.                                                          (4.7)

Applying the **completed fleet02/B14 r34 inequality (1.1)** with

`q_*=16`                                                           (4.8)

gives

`||p_(Q_N)||_inf`
` <= 1 + (1/2)[log 32 + C0]`
` = (1/2)[2+C0+log32]`
` = 4.388547493818661... .`                                        (4.9)

This is uniform in `N`; in particular, the exponential fragment separation and all moments of `V_i` are irrelevant. This improves the same r34 branch's `q=1` certificate `6.002253...` for this family.

### One-sided localization has exactly zero tax

Now split `V_1` into its `N` interval components but keep the entire wildly fragmented law of `V_2` protected. Each `V_1` piece has mass `m=1/N`. Since `2V_2` itself has density cap `1/2`, Theorem 2.1 gives unnormalised slope cap

`L_piece <= m/2`.                                                   (4.10)

Thus every piece has the same ratio `H=L/m<=1/2`, and summing its optimized r34 bound reproduces **exactly** (4.9), not merely another uniform constant.

The same remains true for any finite or countable positive localization of `V_1`, not just its geometric interval components, and for arbitrary translations of those pieces.

## 5. Sharpened two-sided fragmentation barrier

If one instead normalizes/pays both active fragment labels before the singular random-slope step, the partner compiler necessarily sees a growing per-unit-mass slope cap.

For a pair of interval components of `V_1,V_2`, the cell mass is

`m=N^(-2)`,                                                         (5.1)

while the exact unnormalised density of `S=2(V_1+V_2)` is triangular with peak

`L=1/(2N)`.                                                        (5.2)

Hence

`H=L/m=N/2`.                                                       (5.3)

For this cell, the logarithmic-branch stationary choice is

`q_*=16N`,                                                         (5.4)

and (3.3) gives

`||p_cell^sub||_inf`
` <= N^(-2) * (1/2)[2+C0+log(32N)].`                              (5.5)

Summing all `N^2` cells yields

`boxed:
 cellwise r34 certificate
 <= (1/2)[2+C0+log(32N)]
 = 4.388547493818661... + (1/2)log N.
`                                                                       (5.6)

For this family the `q<1/2` branch cannot improve (5.6): there the first positive term alone is at least

`8sqrt(2H/kappa)=8sqrt(N/2)`,                                      (5.7)

which already exceeds the logarithmic value for every `N>=1`. Thus within the completed r34 compiler the symmetric two-sided cell payment has a genuine logarithmic divergence, while the whole-law or protected-block order stays at 4.3885474938.

This is a proof-order obstruction, not a counterexample to QFORM. It sharpens the earlier `q=1` `sqrt(N)` loss to the best branch-visible `0.5 log N` tax and identifies exactly what has to be preserved: at least one whole smoothing block must survive until after the reciprocal/logarithmic step.

## 6. Consequence for arbitrary shifts, distant fragments and unbounded support

The support/localization debt in this branch is now cleanly separated from the matrix debt:

1. A whole protected product block may be arbitrarily disconnected or unbounded; its projection cap is law-uniform and translation-invariant.
2. Every complementary bank factor may be decomposed into arbitrarily remote finite/countable pieces; the unnormalised slope cap retains the full piece mass, so the optimized partner constant is unchanged.
3. Outside original-coordinate conditioning creates arbitrary deterministic slope translations and correlated remainders, both already uniform in r34.
4. No moment, support radius, fragment count or fragment separation appears anywhere.

This is compatible with the live corrections: no post-rotation independence is used, no law-uniform pointwise quadratic Fourier decay is invoked, no conditional projection-density moment is assumed, and there is no bounded-diameter or fixed-fragment-count reduction.

The full QFORM conjecture nevertheless remains OPEN. The unpaid implication is matrix-structural: from bare `s_3(A)>=1`, produce before two-sided active normalization either (i) an invertible indefinite physical pair plus a protected smoothing block with quantitative projection cap, or (ii) one of the already-paid ridge/volume/grouped-bank/mixed-hub exits. Diffuse configurations where no useful physical pair exists are not closed by the present localization theorem.

## 7. Checks

- SymPy check: `(lambda-1)(lambda^2+2lambda-5)` is the characteristic polynomial of the `3x3` block (4.3), giving (4.5).
- Numerical constants: `C0=3.311359084837597...`; partner `C_*=C0+log2=4.004506265397542...`; (4.9) equals `4.388547493818661...`.
- At `N=1`, the small-q lower term in (5.7) is `4sqrt(2)=5.65685...>4.38855...`; it grows as `sqrt(N)` while (5.6) grows only logarithmically, so the claimed branch comparison is safe for every integer `N>=1`.

No claim here is the unrestricted theorem, and no continuity claim is promoted beyond scopes already proved elsewhere.
