SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-22T19:42:32Z.
attacking: one-cross half-Riesz smoothing from a zero-internal coefficient bank, then routing the current curved-bank residual without square-root decoupling.

# fleet02/B09 QFORM r8 — one cross direction is enough for half-Riesz when one bank is linear

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet02/B09` — Bilinear block mechanism  
Run: `20260922T194232Z-fleet02-B09-QFORM-r8`  
Outcome: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted theorem remains open. This report proves a new translation-uniform half-Riesz estimate that uses only one cross singular direction when one original-coordinate bank has no internal quadratic curvature. Combined with a physical square pivot it gives a direct `O(|L|)` interval estimate. It also gives an exact low-diagonal rank-one-square regression showing why the zero-internal hypothesis cannot simply be replaced by “small diagonal”.

## 1. Current sources and corrections actually used

The newest completed named-partner result is fleet03/B09 run `20260922T194535Z-fleet03-B09-QFORM-r16`, theorem `QFORM-THREE-BANK-RANKONE-TRIANGLE-v1`, canonical source

`yspennstate/math-open-problems@5e92c0aa0681b3d24630451076ab511f92dc718c:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260922T194535Z-fleet03-B09-QFORM-r16/REPORT.md`.

For three disjoint rank-one product banks with aggregate strengths `s_IJ,s_IK,s_JK`, it proves

`||p_F||_infinity <= 2(3+log 8)(s_IJ s_IK s_JK)^(-1/3)`.              (1.1)

Its exact next debt is `QFORM-ONE-STRONG-CROSS-CURVED-BANK-v1`: starting from `s_2(S)>=1`, low physical diagonals and one strong cross singular direction, either expose a triangle/wedge/ridge certificate or make the curved bank itself pay a translation-uniform half-Riesz potential.

I also use the product-marginal fact already source-recorded and applied in that partner proof: if `v` is a unit vector supported on original independent cap-one coordinates, then the scalar projection `<v,X>` has density at most `sqrt(2)`. No post-rotation independence is asserted or needed.

For comparison, fleet03/B09 r15 proved `QFORM-HALFRIESZ-TWO-CROSS-v1`: two cross singular values at least `beta` imply `sup_w E|F-w|^(-1/2)<=8 beta^(-1/2)` even with arbitrary self blocks. The theorem below reaches the same constant from only **one** cross singular value when one side is genuinely linear.

The live corrections enforced here include the failures of law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, positive conditional projection-density moments, post-rotation independence, a universal good local minor, and one-heavy-row plus its own matching square. No conditional supremum over a rotated spectral fiber is taken.

## 2. Two elementary half-Riesz facts

### Lemma 2.1 — capped-density half-Riesz rearrangement

If a real random variable `Z` has probability density bounded by `M`, then for every `t`,

`E |Z-t|^(-1/2) <= 2 sqrt(2M)`.                                      (2.1)

Proof. The kernel `|z-t|^(-1/2)` is symmetric decreasing about `t`. Under the constraints `0<=f<=M`, `int f=1`, the bathtub principle maximizes the integral by density `M` on the interval of length `1/M` centered at `t`. Therefore

`E|Z-t|^(-1/2)
 <= M int_{-1/(2M)}^{1/(2M)} |u|^(-1/2) du
 = 2 sqrt(2M)`.                                                        (2.2)

### Lemma 2.2 — linear product projection

If `X=(X_i)_{i in I}` has independent cap-one coordinates and `a in R^I\{0}`, then `<a,X>` has density at most `sqrt(2)/||a||_2`. Hence, by Lemma 2.1,

`sup_t E |<a,X>-t|^(-1/2)
 <= 2^(7/4) ||a||_2^(-1/2)`.                                         (2.3)

This is an application of the one-dimensional product-marginal bound, not an independence statement about rotated coordinates.

## 3. Main theorem — one cross singular direction pays half-Riesz

### Theorem 3.1 — `QFORM-ZEROINTERNAL-BANK-ONECROSS-HALFRIESZ-v1`

Let `I,J,R` be pairwise disjoint original-coordinate sets. Let all input coordinates be independent with densities bounded by one. Condition arbitrarily on the outside bank `R`; all constants below may therefore depend measurably on that conditioning.

On the two active banks suppose the quadratic-affine expression is

`F(X_I,X_J)
 = 2 X_I^T C X_J + ell_I^T X_I + H(X_J)`,                              (3.1)

where `C` is an arbitrary real `|I| x |J|` matrix, `H` is an **arbitrary** quadratic-affine function of `X_J`, and there is no quadratic term in the coefficient-side variables `X_I`. Put

`sigma=||C||_op>0`.                                                    (3.2)

Then, uniformly in every outside conditioning and every `w`,

`boxed: E |F-w|^(-1/2) <= 8 sigma^(-1/2).`                            (3.3)

No rank assumption on `C`, no restriction on `H`, no moment/support assumption, and no local-entry lower bound is imposed.

#### Proof

Fix `Y=X_J`. Write

`d=ell_I/2`,  `a(Y)=2(CY+d)`.

For this fixed `Y`, `F-w` is a linear form in the still-independent original coordinates `X_I`, plus a scalar shift. Lemma 2.2 gives

`E_{X_I}(|F-w|^(-1/2) | Y)
 <= 2^(7/4)||a(Y)||_2^(-1/2)
 = 2^(5/4)||CY+d||_2^(-1/2).`                                        (3.4)

Choose unit left/right top singular vectors `u,v` of `C`, so

`u^T C = sigma v^T`.                                                   (3.5)

Pointwise,

`||CY+d||_2
 >= |u^T(CY+d)|
 = |sigma <v,Y> + u^T d|`.                                            (3.6)

The scalar projection `<v,Y>` uses only the independent original coordinates in bank `J`; its density is at most `sqrt(2)`. Hence `sigma<v,Y>+u^Td` has density at most `sqrt(2)/sigma`. Lemma 2.1 therefore gives

`E_Y ||CY+d||_2^(-1/2)
 <= 2^(7/4) sigma^(-1/2).`                                            (3.7)

Combining (3.4) and (3.7) gives

`2^(5/4) 2^(7/4) sigma^(-1/2)=8 sigma^(-1/2)`,                         (3.8)

which proves (3.3). Since every estimate was uniform in the conditioned outside variables, averaging over `X_R` preserves the same bound. QED.

### Matrix form

The theorem applies whenever an original-coordinate subbank `I` satisfies `S[I,I]=0` and its cross block to a disjoint bank `J` has `||S[I,J]||_op=sigma`; all curvature on `J`, all outside curvature, and all outside couplings may be retained by conditioning outside `I union J`. Thus a single aggregate cross direction suffices for half-Riesz smoothing once one side is genuinely linear.

This is stronger in a different direction from the prior zero-internal-bank **density** theorem, which needed two cross singular directions. The present endpoint is weaker (`L^{-1/2}` potential rather than a density) but exactly what the outer physical-square mechanism needs.

## 4. Direct target consequence after one physical square pivot

### Corollary 4.1 — `QFORM-PIVOT-ONECROSS-LINEARBANK-v1`

Suppose a full quadratic form has a nonzero original-coordinate scalar pivot `a`, and after completing that physical square its Schur residual `F` satisfies Theorem 3.1 with cross norm `sigma`. Then

`boxed: ||p_Q||_infinity <= 8 (|a| sigma)^(-1/2).`                    (4.1)

Consequently every interval `L` satisfies

`boxed: P{Q in L} <= 8 (|a| sigma)^(-1/2) |L|.`                       (4.2)

Proof. Completing the physical coordinate gives

`Q=a(X_0+m(Y))^2+F(Y)`.                                                (4.3)

Conditionally on `Y`, `X_0+m(Y)` is a translate of a cap-one variable. Its square pushforward is pointwise bounded by `|a|^(-1/2)|z|^(-1/2)` on the relevant half-line. Thus

`p_Q(t) <= |a|^(-1/2) E|F-t|^(-1/2)`,                                (4.4)

and (3.3) proves (4.1). Integrating over an interval proves (4.2). QED.

### Application to the current named-partner routing

Fleet03/B09 r15 reduces the heavy-pivot Schur problem to low diagonals plus one strong cross direction after paying its second-pivot and two-cross branches. On the explicit singleton/heavy-pivot scale already used there,

`|a| >= 157/320`,  `sigma >= 3/16`,                                   (4.5)

the additional hypothesis `S[I,I]=0` on the coefficient-side bank now gives

`||p_Q||_infinity
 <= 8 / sqrt((157/320)(3/16))
 = 26.3763388788... <26.377.`                                         (4.6)

Thus the named partner’s `one-strong-cross` residual can now exclude the entire **zero-internal coefficient-bank** subbranch, with arbitrary curvature on the opposite bank and arbitrary extra spectrum outside the packet.

The newest partner r16 independently pays a complementary coherent three-bank cycle. For example, at the actual scales

`s_IJ>=3/16`, `s_IK,s_JK>=1/8`,                                      (4.7)

its theorem (1.1) gives

`||p_Q||_infinity
 <=2(3+log8)[(3/16)(1/8)^2]^(-1/3)
 =70.9968144413...<71.`                                                (4.8)

Equations (4.6) and (4.8) are therefore two source-compatible, nonoverlapping ways to pay current one-strong-cross geometry: a linear coefficient bank needs only one cross singular direction; a genuinely three-bank cycle can pay even though each two-bank link has rank one.

## 5. Target-valid diffuse stress family

Let `I,J` be disjoint banks of arbitrary sizes and let `C=u v^T` with `||u||_2=||v||_2=1`; individual entries may tend to zero with dimension. Add an independent physical scalar coordinate `X_0` and take the matrix

`A = [1] direct_sum [[0,C],[C^T,0]].`                                  (5.1)

The nonzero spectrum is exactly

`{1,1,-1}`.                                                           (5.2)

Hence this is a genuine target family for every bank size. The residual has zero internal `I`-bank and `||C||_op=1`, so Corollary 4.1 gives, for every admissible product input law,

`boxed: ||p_{X^TAX}||_infinity <=8.`                                  (5.3)

For constant unit vectors on size-`m` banks every physical cross entry is only `1/m`, yet (5.3) is dimension-free. This is aggregate-before-inversion and uses no selected local minor.

## 6. Exact regression: low diagonals plus one strong cross are not enough by themselves

The zero-internal hypothesis in Theorem 3.1 is structural, not cosmetic. Consider the exact two-coordinate matrix

`S_*=[[49/100, 1/5],
      [1/5,    4/49]].`                                                (6.1)

Both physical diagonal magnitudes are `<1/2`, while the cross coefficient obeys

`1/5 > 3/16`.                                                         (6.2)

But

`det S_*=0`, and exactly

`X^T S_* X
 =(49/100)(X_1+(20/49)X_2)^2`.                                     (6.3)

For independent `X_1,X_2 ~ Uniform[-1/2,1/2]`, the variable

`W=X_1+(20/49)X_2`                                                    (6.4)

has a continuous density equal to one on a neighborhood of zero. Therefore

`E |X^T S_*X|^(-1/2)
 =(10/7) E|W|^(-1)
 =infinity.`                                                          (6.5)

So the tempting strengthening

> “all physical diagonals `<1/2` plus one cross coefficient `>3/16` already gives a uniform half-Riesz bound”

is false, even with exact rational coefficients and cap-one product inputs. This is a **mechanism counterexample**, not a QFORM counterexample: `S_*` has rank one and does not satisfy the partner residual condition `s_2(S)>=1`. Its role is to force every successful treatment of the remaining curved-bank branch to spend the genuine second spectral resource rather than silently perturbing Theorem 3.1 across a nonzero self-square.

This is a quantified specialization of the earlier same-square obstruction, now placed exactly inside the current partner low-diagonal / one-strong-cross numerical window.

## 7. Sharpened first unpaid implication

The first B09 debt is now

`QFORM-ONE-STRONG-CROSS-CURVED-BANK-SECOND-RESOURCE-v1`.

Starting from the named-partner residual

`s_2(S)>=1`,
`max_i |S_ii|<1/2`,
`one original-coordinate cut has sigma_1>3/16 but lacks the paid sigma_2 scale`,

prove a product-preserving routing that does one of the following before any reciprocal tiny-entry/minor payment:

1. extracts a zero-internal coefficient subbank retaining a universal cross norm, so Theorem 3.1 applies;
2. extracts the partner r16 coherent three-bank triangle, the prior zero-bank wedge, or a ridge certificate at universal aggregate scale; or
3. uses the nonzero self-bank curvature **together with** `s_2(S)>=1` to regularize the rank-one-square cancellation exhibited by (6.1)-(6.5).

The regression (6.1) makes option 3 genuinely two-resource: one strong bilinear direction and small diagonals alone cannot pay the half-Riesz potential. The remaining problem is therefore no longer “one strong cross plus arbitrary curvature” in full generality; after this run the unpaid curvature must be simultaneously nonzero on the coefficient side and arranged so that no zero-internal subbank, triangle, wedge or ridge packet carries universal mass.

## 8. Integrity

No Monte Carlo or histogram is used. The accompanying checker evaluates only the displayed finite constants and exact rational determinant identity; it is not proof evidence. Full QFORM remains open and continuity is not claimed. Repository transport was used, not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
