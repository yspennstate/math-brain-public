SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-23T14:53:30Z.
attacking: the designated partner's null-hub heavy-anchor star survivor; transfer the primary product-marginal theorem through an exact Schur complement and then apply the completed physical-pair logarithmic smoothing theorem.

# fleet01/B18 r34 — heavy null-hub anchor: exact Schur rank-one remainder and pair-log payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Literature-to-proof transfer  
**Status:** `NEW SUPPORTING TARGET-LEVEL THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source pins

The unrestricted owner target remains OPEN: independent real inputs with arbitrary one-dimensional probability densities bounded by one, arbitrary dimension, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one.

Fresh control was consumed before this proof. The latest completed designated-partner result is fleet02/B18 r29, present at source snapshot

`yspennstate/math-open-problems@d522cbf61b6744403b82d955f27d8059465e6f38`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/fleet02-B18-20260923T130619Z-r29/REPORT.md`.

Its exact-rank-three null-hub normal form and star ledger are the input to the application in Section 6 below.

The smoothing theorem applied below is the completed physical-pair logarithmic theorem

`QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1 / QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1`,

source-pinned at

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Its general form is: if two independent cap-one original coordinates form a fixed invertible indefinite physical pair `B`, with `Delta=|det B|` and `kappa=sigma_min(B)`, and after completing that pair the remaining random critical value `R` obeys

`sup_t P(|R-t|<rho) <= H sqrt(rho)` for all `rho>0`,

then

`||p_Q||_infinity <= 4 sqrt(2H) (Delta kappa)^(-1/4)`.             (1.1)

Arbitrary shifts of the pair depending on the remaining variables are explicitly allowed. Thus this theorem does not replace a conditional density cap by independence.

The primary literature transfer is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1. For a genuine product density `prod f_j`, `||f_j||_infinity<=1`, every normalized one-dimensional orthogonal marginal has density cap at most `sqrt(2)`. No moment, support, iid, log-concavity, centering, or smoothness assumption is added.

## 2. Incoming null-hub geometry

Use the exact null-hub shear normal form already verified in the null-hub compiler and consumed by partner r29:

`Q = 2 (X_0 + ell dot X_L) (g dot X_L) + d (beta dot X_L)^2`,       (2.1)

where

`||beta||_2=1`, `beta dot g=0`, `gamma:=||g||_2>0`.                 (2.2)

In the normalized rank-three spectral representation `A=R M R^T`, the hub has spectral row `sqrt(h)n`, `n^T M n=0`, and

`|d| gamma^2 = h D`, `D:=|det M|=|pdet A|`.                        (2.3)

For each leaf `i`, put

`q_i := beta_i^2 + g_i^2/gamma^2`.                                 (2.4)

Partner r29 proves `sum_{j != i}(alpha_i beta_j-alpha_j beta_i)^2=q_i`, and in its heavy alternative some anchor has `q_i>1/2`.

The purpose of this run is to pay a large subbranch of that heavy alternative without selecting a single partner leaf `j` and without paying the tiny individual star determinant `|det A[{0,i,j}]|`.

## 3. Exact Schur-complement identity at one heavy anchor

Fix a leaf `i` with `g_i !=0`. Set

`U=X_0`, `V=X_i`, `Z=X_{L\{i}}`.

The physical principal pair on `(U,V)` is

`B_i = [[0,g_i],[g_i,a_i]]`,                                      (3.1)

where, from (2.1),

`a_i=2 ell_i g_i+d beta_i^2`.                                     (3.2)

It is automatically indefinite and invertible, with

`Delta_i=|det B_i|=g_i^2`,                                        (3.3)

and write

`kappa_i=sigma_min(B_i)>0`.                                       (3.4)

Let `g_-`, `beta_-`, `ell_-` denote the vectors with coordinate `i` deleted. The pair-to-rest coefficient matrix has rows

`g_-`,

`g_i ell_- + ell_i g_- + d beta_i beta_-`.                         (3.5)

Since

`B_i^(-1) = [[-a_i/g_i^2,1/g_i],[1/g_i,0]]`,                      (3.6)

direct Schur elimination gives the ENTIRE remaining quadratic block

`S_i
 = (d/g_i^2) (g_i beta_- - beta_i g_-)(g_i beta_- - beta_i g_-)^T`.  (3.7)

All `ell` terms cancel exactly. This is not a perturbative deletion and not a conditioning approximation.

For completeness, expand the one-dimensional coefficient vector

`h_i := g_i beta_- - beta_i g_-`.                                  (3.8)

Using `beta dot g=0`, `||beta||=1`, and `||g||=gamma`,

`||h_i||^2
 = g_i^2(1-beta_i^2)+beta_i^2(gamma^2-g_i^2)
   -2g_i beta_i(beta_- dot g_-)
 = g_i^2 + beta_i^2 gamma^2
 = gamma^2 q_i`.                                                    (3.9)

Thus, with

`u_i=h_i/(gamma sqrt(q_i))`, `||u_i||=1`,                           (3.10)

the completed-pair critical remainder is exactly

`R_i(Z)=lambda_i (u_i dot Z)^2`,                                   (3.11)

where

`lambda_i = d gamma^2 q_i/g_i^2`.                                  (3.12)

This identity is the main structural gain: all leaves other than the anchor have been aggregated into one normalized ORIGINAL-source linear statistic, and the star currency `q_i` survives in its curvature.

## 4. Primary LPP transfer gives the exact small-ball input

The coordinates of `Z` are still independent ORIGINAL input variables with one-dimensional density caps at most one. Equation (3.10) is a normalized one-dimensional linear projection, so the Livshyts--Paouris--Pivovarov theorem gives

`||p_(u_i dot Z)||_infinity <= sqrt(2)`.                            (4.1)

If `Z` consists of one coordinate, the direct cap-one bound is even stronger, so there is no `k<n` endpoint issue.

Let `Y=u_i dot Z`. For every `rho>0` and every target `t`, the inverse image

`{y: |lambda_i y^2-t|<rho}`

has Lebesgue measure at most

`2 sqrt(2rho/|lambda_i|)`.                                         (4.2)

Indeed the largest inverse-image length occurs when the output interval touches the quadratic vertex. Multiplying (4.2) by the density cap `sqrt(2)` yields

`sup_t P(|R_i-t|<rho)
 <= 4 sqrt(rho/|lambda_i|)`.                                       (4.3)

Therefore (1.1) applies with

`H_i=4/sqrt(|lambda_i|)`.                                          (4.4)

No conditional projection-density supremum or moment has been used; (4.1) is an unconditional marginal theorem for the disjoint original block `Z`.

## 5. Pair-log payment and the star cancellation

Substitute (3.3), (3.4), and (4.4) into (1.1):

`||p_Q||_infinity
 <=4 sqrt( 8/sqrt(|lambda_i|) ) (g_i^2 kappa_i)^(-1/4)
 =8 sqrt(2) [g_i^2 kappa_i |lambda_i|]^(-1/4)`.                    (5.1)

Now use (3.12):

`g_i^2 |lambda_i| = |d| gamma^2 q_i`.                              (5.2)

Finally (2.3) gives the target-level form

`boxed:
 ||p_Q||_infinity
 <= 8 sqrt(2) [ h D q_i kappa_i ]^(-1/4).`                         (5.3)

Call this `QFORM-NULLHUB-HEAVY-ANCHOR-PAIRLOG-v1`.

The important point is that the explicit hub-anchor coupling `g_i` has disappeared. A tiny individual edge `g_i` makes the Schur-complement curvature (3.12) larger by exactly the compensating factor `g_i^-2`. The analytic payment therefore uses the entire star aggregate through `q_i`, not a selected `3 x 3` minor.

The only local degeneracy left in this mechanism is the physical-pair singular value `kappa_i`.

## 6. Actual application to designated partner fleet02/B18 r29

Partner r29's target-normalized exact-rank-three Schur-isotropic null-hub compiler, in the range `r>=1/2`, has

`h=r^2/(1+r^2)>=1/5`,                                              (6.1)

and because all three nonzero eigenvalue magnitudes are at least one,

`D=|pdet A|>=1`.                                                    (6.2)

Its heavy alternative supplies an anchor `i` with

`q_i>1/2`.                                                         (6.3)

Hence

`h D q_i >1/10`.                                                   (6.4)

If that heavy anchor satisfies the concrete physical-pair condition

`kappa_i>=1/10`,                                                    (6.5)

then (5.3) gives

`||p_Q||_infinity
 < 8 sqrt(2) (1/100)^(-1/4)
 = 8 sqrt(20)
 = 35.77708763999664...`.                                          (6.6)

Thus the latest partner dichotomy can now be sharpened to:

1. `max_j q_j<=1/2`: the completed null-hub mixed-Fresnel theorem gives a continuous `C_0` density with universal bound `<12.927`;
2. some heavy anchor has `q_i>1/2` and `kappa_i>=1/10`: the present pair-log transfer gives an essential density bound `<35.778`;
3. the only still-unpaid heavy-anchor state for this mechanism has a heavy witness with `kappa_i<1/10` (or `g_i=0`, which means `kappa_i=0`).

The threshold `1/10` is only a clean numerical splice. More generally, for any `tau>0`,

`q_i>1/2`, `r>=1/2`, `kappa_i>=tau`

imply

`boxed:
 ||p_Q||_infinity
 <8 sqrt(2) (10/tau)^(1/4).`                                      (6.7)

This is the requested completed-partner-to-actual-inequality transfer.

## 7. Correction audit

The proof deliberately preserves the live correction boundary.

- No spectral coordinates are declared independent.
- The pair-log theorem uses the two original independent coordinates `(X_0,X_i)` and explicitly permits remaining-variable-dependent shifts.
- LPP is applied only to the normalized original-source projection `u_i dot Z`.
- No arbitrary joint-density coarea inequality is used.
- No conditional density cap is promoted to independence.
- No positive moment/supremum of a conditional projection density appears.
- No law-uniform pointwise quadratic-phase decay is used.
- No fixed large physical minor is selected from the star ledger.
- No small coefficient is deleted or replaced by zero.

## 8. Continuity and remaining debt

The pair-log theorem used in Section 5 proves an essential `L^infinity` density bound but does not, by itself, prove continuity. Therefore continuity is NOT claimed for (5.3)/(6.6). The partner's diffuse branch remains separately continuous by its mixed-Fresnel theorem. Full-target continuity remains open.

The immediate remaining heavy-anchor obstruction is now quantitatively narrower: a heavy transverse anchor with a near-singular physical pair `B_i`, `kappa_i<1/10`. Because

`B_i=[[0,g_i],[g_i,a_i]]`,

this can arise from a tiny coupling `g_i` or a large diagonal shear `|a_i|/|g_i|`; neither may be discarded. A next useful implication would route this near-singular pair into an existing scalar-pivot/high-slope grouped-coordinate theorem or derive a pair-log envelope adapted to the zero-pivot triangular structure that does not pay `kappa_i^-1/4`.

This report does NOT prove arbitrary exact rank three and does NOT prove the full owner conjecture.

## 9. Literature status

The targeted primary-theorem check found no published theorem whose stated hypotheses directly imply the full arbitrary non-iid cap-one QFORM target. The LPP theorem matches the linear projection used here exactly; stronger-looking quadratic-form concentration results found in the literature typically impose additional subgaussian, Gaussian-functional, log-concave, or moment hypotheses. This is only a hypothesis comparison, not a novelty claim from absence.

## 10. Algebra regression

The Schur identity (3.7) was independently checked symbolically before publication: for one generic remainder coordinate, SymPy reduces the exact Schur complement to

`d*(beta_i*g_- - beta_-*g_i)^2/g_i^2`,

which is the scalar specialization of (3.7). The proof itself is the exact matrix algebra above; the symbolic calculation is only a regression check.
