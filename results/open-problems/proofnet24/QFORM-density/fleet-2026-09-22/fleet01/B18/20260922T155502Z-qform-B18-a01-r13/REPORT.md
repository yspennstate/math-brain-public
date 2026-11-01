# fleet01/B18 — exact Rogozin bank caps and coefficient-sensitive three-bank transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Worker:** fleet01/B18  
**Run:** `20260922T155502Z-qform-B18-a01-r13`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_THEOREM / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and live gap

The sole target remains: for every dimension `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove

`P(X^T A X in I) <= C |I|`

for one finite universal constant `C`, independent of `n`, the laws and `A`, and separately track continuity of the output density.

The full conjecture remains open. The live correction set forbids post-rotation independence, a universal single good minor/cross cut, generic spectral-marginal curvature, and absolute-value Fourier replacements. This run stays inside genuine disjoint original-coordinate banks.

The designated partner result actually used is fleet02/B18:

- repository `yspennstate/math-open-problems`
- commit `f985e95ceec640cdc37cffc34fab07bb2687a414`
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/fleet02-B18-20260922T153407Z-qform-lit/REPORT.md`
- theorem `QFORM-LPP-FULL-THREE-BANK-v1`.

That theorem says: if disjoint physical banks `I_1,I_2,I_3` produce independent scalar aggregates `Y_r=<u_r,X_{I_r}>` and the full form factors exactly as

`Q = Y^T B Y + 2 Y^T L X_K + X_K^T D X_K`,                         (1.1)

with invertible symmetric `3x3` matrix `B`, then for any valid density caps `K_r>=||p_{Y_r}||_infinity`, with `D_K=diag(K_1,K_2,K_3)`,

`||p_Q||_infinity <= C_3 / sigma_min(D_K^{-1} B D_K^{-1}),`        (1.2)

where

`C_3 = 2*pi + 3*sqrt(3)`.                                          (1.3)

The output density is continuous. The partner proof ultimately uses the completed fleet02/B15 three-variable affine quadratic theorem at commit `4b2e6a36bcffeb767998c43d27cee1d8f5eaa07e`.

The partner used the universal Livshyts--Paouris--Pivovarov cap `K_r<=sqrt(2)` for unit bank vectors. The purpose here is to replace that coarse cap by the exact coefficient-sensitive cap supplied by Rogozin's sharp one-dimensional convolution theorem.

## 2. Primary source transfer: exact bank cap

Primary source: T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190 (2015), Theorem 1 and the one-dimensional Rogozin consequence. For independent real variables `Z_i` with maximum densities `M(Z_i)<=K_i`, the maximum density of their sum is no larger than that of the sum of independent centered uniform variables having densities `K_i`.

Let `u=(u_i)_{i in I}` be any nonzero physical coefficient vector and

`Y_u = sum_{i in I} u_i X_i`,                                      (2.1)

where the `X_i` are independent and `||f_i||_infinity<=1`. Omit zero coefficients and define

`R(u) := || *_{i:u_i!=0} [ |u_i|^{-1} 1_{[-|u_i|/2, |u_i|/2]} ] ||_infinity`.  (2.2)

### Theorem 2.1 — exact sharp aggregate cap

For every such product source,

`boxed( ||p_{Y_u}||_infinity <= R(u). )`                            (2.3)

Moreover this cap is sharp over the allowed source class: taking all selected `X_i` independently uniform on `[-1/2,1/2]` attains `R(u)`.

### Proof

For each nonzero coefficient `u_i`, the scaled variable `u_i X_i` has density cap

`K_i = 1/|u_i|`.                                                    (2.4)

Rogozin's theorem therefore compares the maximum density of their sum with independent uniforms of density `K_i`, namely uniforms on intervals of length `|u_i|`. Their convolution density is exactly the expression in (2.2), proving (2.3). If the original `X_i` are themselves independent uniforms on `[-1/2,1/2]`, then `u_i X_i` are exactly those comparator uniforms (signs do not matter by symmetry), so equality is attained. QED.

This theorem requires no moments, centering, smoothness, connected support, or rotation. It is an original-coordinate convolution statement.

## 3. Coefficient-sensitive three-bank theorem

For the exact factorization (1.1), keep the partner's unit bank vectors `u_r`, but set

`R_r := R(u_r),    D_R := diag(R_1,R_2,R_3).`                       (3.1)

Applying Theorem 2.1 to each disjoint bank gives three genuinely independent bank variables with caps `R_r`. Substitution into the partner inequality (1.2) gives:

### Theorem `QFORM-ROGOZIN-THREE-BANK-v1`

Under (1.1),

`boxed( ||p_Q||_infinity
       <= C_3 / sigma_min(D_R^{-1} B D_R^{-1}). )`                  (3.2)

The density has a continuous representative.

This is an exact coefficient-sensitive replacement for the partner's coarse universal estimate

`||p_Q||_infinity <= 2 C_3 / sigma_min(B)`.                         (3.3)

No claim is made that (3.2) is always numerically smaller than the best possible quadratic-form constant; rather, (3.2) preserves all available bank-shape information before the quadratic payment. The scalar caps `R_r` themselves are sharp among arbitrary cap-one coordinate laws.

A useful way to record the analytic score of a candidate bank compression is therefore

`S(B;u_1,u_2,u_3)
   := sigma_min(D_R^{-1} B D_R^{-1}),`                              (3.4)

so that the source-valid density cost is `C_3/S`. Any future bank-extraction argument should optimize this weighted score rather than discard the coefficient shape by replacing every `R_r` with `sqrt(2)`.

## 4. Exact strict improvement for a three-coordinate bank

Let

`u = (1,1,1)/sqrt(3)`.                                              (4.1)

Rogozin reduces the worst bank density to the sum of three independent centered uniforms of width `1/sqrt(3)`. Write `V_i~Unif[-1/2,1/2]` and `S=V_1+V_2+V_3`. On `|s|<=1/2`, the Irwin--Hall density is

`p_S(s)=3/4-s^2`,                                                   (4.2)

so

`||p_S||_infinity=3/4`.                                             (4.3)

Since the comparator aggregate is `S/sqrt(3)`, scaling gives the exact sharp cap

`boxed( R(u)=3sqrt(3)/4 = 1.299038105676658... ).`                  (4.4)

This is strictly smaller than the universal unit-direction cap `sqrt(2)`.

If all three banks in (1.1) use this equal-three-coordinate direction, then `D_R=kappa I_3` with

`kappa=3sqrt(3)/4,    kappa^2=27/16`.                               (4.5)

Hence

`sigma_min(D_R^{-1}BD_R^{-1}) = sigma_min(B)/kappa^2`               (4.6)

and (3.2) becomes

`boxed( ||p_Q||_infinity
 <= (27/16)(2*pi+3sqrt(3))/sigma_min(B) )`                           (4.7)

`= 19.37138241918299... / sigma_min(B)`.                            (4.8)

The partner's LPP-only simplification gives

`2(2*pi+3sqrt(3))/sigma_min(B)
 = 22.95867545977244... / sigma_min(B)`.                            (4.9)

Thus the source transfer improves that particular analytic payment by the exact factor

`(27/16)/2 = 27/32 = 0.84375`,                                     (4.10)

i.e. a `15.625%` reduction, while preserving arbitrary outside dimension and arbitrary affine couplings allowed by (1.1).

## 5. Concrete target-valid application

Use the partner's strict-extension compressed matrix

`M=[[1,2,1],[2,1,1],[1,1,1]],`

`B_*=(2+sqrt(3)) M`.                                                (5.1)

Its eigenvalues are

`-(2+sqrt(3)), 1, 7+4sqrt(3)`,                                     (5.2)

so `sigma_min(B_*)=1` and all three nonzero eigenvalues have modulus at least one.

Take three disjoint physical banks, each consisting of three coordinates, with normalized all-ones bank vectors `(1,1,1)/sqrt(3)`. Let `C` be the `9x3` matrix of these orthonormal bank columns and let

`A=C B_* C^T`                                                       (5.3)

(optionally direct-sum arbitrary zero coordinates). Then the nonzero spectrum of `A` is exactly (5.2), so this is inside the owner's target class in arbitrary ambient dimension. For every independent cap-one product source,

`boxed( ||p_{X^T A X}||_infinity
       <= (27/16)(2*pi+3sqrt(3))
       = 19.37138241918299... . )`                                  (5.4)

The output density is continuous.

The bank marginal constant `3sqrt(3)/4` used here cannot be improved from the hypotheses on the three coordinates alone: independent unit-interval uniforms attain it. Any further improvement to (5.4) must therefore exploit additional quadratic structure or sharpen the three-variable quadratic theorem, rather than merely improve the one-dimensional aggregate cap.

## 6. Relation to live corrections

The argument obeys the current correction ledger.

- No independence after a spectral rotation is asserted; all three aggregates use disjoint original-coordinate banks.
- No single physical minor or rank-three coordinate cut is extracted.
- No generic bounded spectral marginal is fed into a curved pushforward.
- No conditional sum/difference density cap is assumed.
- No absolute-value pointwise/Fourier envelope is used.
- The theorem is an exact-factorization payment, not a claim that every target matrix admits such a factorization.

The ridge-window theorem remains complementary: it covers a full-matrix low-high-spectral-leverage branch even with nonseparable small tails. The present theorem instead makes the exact bank branch quantitatively coefficient-sensitive.

## 7. Full-problem status and first unpaid implication

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.

**MATHEMATICAL CHANGE:** the exact three-bank analytic payment now uses the sharp source-valid bank density profile `R(u_r)` rather than the universal `sqrt(2)` cap. This gives a strict, explicitly quantified target-level improvement for nontrivial physical bank shapes and provides a weighted extraction score (3.4).

The first unpaid implication remains structural:

> Starting from only three eigenvalues with modulus at least one, and outside the proved ridge/spectral-window branch, construct a product-preserving decomposition that supplies a uniformly positive weighted bank score `S(B;u_1,u_2,u_3)` while controlling all non-bank remainder interactions, or replace exact bank factorization by a source-valid stability theorem.

The known local-minor/cross-rank and single-Schur extraction counterexamples show that this cannot be solved by selecting one uniformly good physical triple. No full solution or counterexample to the owner conjecture is claimed.
