SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T10:30:46.596981Z.
attacking: a rigorous replacement for the previously invalid arbitrary-joint localized coarea step, by compiling the rank-two affine half-Riesz and physical-pair logarithmic theorems into a uniform original-coordinate 3x3 principal-block bound.

# account03/B13 r24 — localized 3x3 principal-block compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Control read at start: `yspennstate/math-research-brain@317f3f9f57ccaf91d0806998c9aee04a9d0eb313`; refreshed before publication at `b97015da7b6cc5d00c515d8c508de5693c67db9c`; OWNER CONTROL revision `2026-09-22.15`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Full QFORM: OPEN. Full continuity: OPEN.

## 1. New theorem

### QFORM-LOCAL-3X3-PRINCIPAL-COMPILER-v1

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by one, and let `A` be real symmetric. Suppose there is a set `I` of three ORIGINAL coordinates such that the `3 x 3` principal block

`B=A[I,I]`

is invertible with

`sigma_min(B) >= s > 0`.

Then the FULL ambient quadratic form

`Q=X^T A X`

has an essentially bounded density and

`||p_Q||_infinity <= (128 * 2^(1/4))/s < 152.219/s`.      (1.1)

All coefficients outside `I`, including arbitrary outside quadratic terms and arbitrary cross couplings into `I`, are unrestricted. No moment, support, regularity, sign, or post-rotation independence assumption is used.

This theorem repairs the useful localized branch by a product-preserving argument. It does NOT use the refuted arbitrary-joint three-dimensional coarea claim.

## 2. Dependencies actually used

Two completed supporting theorems were read at their immutable sources.

1. `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, source
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
   For an original-coordinate principal block of rank exactly three, `A_II=V M V^T`, and a nonzero physical diagonal entry `a=A_ii`, it gives

   `||p_Q||_infinity <= 128 [c_i |a| |det M|]^(-1/4)`,

   uniformly over arbitrary induced affine terms and arbitrary outside couplings.

2. `QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1`, source
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   If a rank-three original-coordinate principal block has nonzero eigenvalue magnitudes at least `s`, and an invertible indefinite physical pair `C` with `D=|det C|` and `kappa=sigma_min(C)`, then

   `||p_Q||_infinity <= 8 sqrt(5) (D kappa s)^(-1/4)`,

   again uniformly over arbitrary outside couplings and affine terms.

The live correction inbox was reread before publication. In particular this proof does not use arbitrary-joint coarea, conditional projected-density moments, cross-minor-alone boundedness, or a perturbative near-null deletion.

## 3. Proof of (1.1)

Condition on all original coordinates outside `I`. The three coordinates in `I` remain independent with their original cap-one densities. The outside variables contribute only deterministic affine terms plus a constant to the conditional three-variable quadratic polynomial. Both dependency theorems explicitly allow arbitrary such affine terms, with constants independent of the conditioning. It is therefore enough to prove the bound for the fixed `3 x 3` block `B`.

Let its eigenvalues be `lambda_1,lambda_2,lambda_3`. By hypothesis,

`|lambda_j| >= s`, hence `|det B| >= s^3` and `tr(B^2) >= 3 s^2`.  (3.1)

We split by the physical diagonal.

### Case A: a diagonal entry has magnitude at least `s/2`

Suppose `|B_ii| >= s/2`. Apply `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1` with `V=I_3`, so `c_i=1` and `M=B`. Using (3.1),

`||p_Q||_infinity`
` <= 128 ( |B_ii| |det B| )^(-1/4)`
` <= 128 ( (s/2) s^3 )^(-1/4)`
` = (128 * 2^(1/4))/s`.                                  (3.2)

### Case B: every diagonal entry has magnitude less than `s/2`

Now

`sum_i B_ii^2 < 3 s^2/4`.

Since

`tr(B^2)=sum_i B_ii^2 + 2 sum_{i<j} B_ij^2 >= 3 s^2`,

we get

`sum_{i<j} B_ij^2 > 9 s^2/8`.

There are three off-diagonal entries, so for some pair `(i,j)`,

`|B_ij| >= sqrt(3/8) s`.                                  (3.3)

Let

`C=[[B_ii,B_ij],[B_ij,B_jj]]`.

Because `|B_ii|,|B_jj|<s/2`, (3.3) gives

`det C = B_ii B_jj - B_ij^2`
` <= |B_ii B_jj| - B_ij^2`
` < s^2/4 - 3s^2/8 = -s^2/8 < 0`.

Thus `C` is invertible and indefinite.

Write `C=C_0+E` with

`C_0=[[0,B_ij],[B_ij,0]]`, `E=diag(B_ii,B_jj)`.

Both singular values of `C_0` equal `|B_ij|`, while `||E||_op < s/2`. Weyl's singular-value perturbation inequality therefore gives

`kappa:=sigma_min(C)`
` >= |B_ij| - ||E||_op`
` >= (sqrt(3/8)-1/2)s`
` = kappa_0 s`,                                           (3.4)

where

`kappa_0=(sqrt(6)-2)/4 = 0.112372435695...`.

For a `2 x 2` invertible matrix, `D=|det C|` is the product of its singular values, hence

`D >= kappa^2`.                                            (3.5)

Apply `QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1` and use (3.4)-(3.5):

`||p_Q||_infinity`
` <= 8 sqrt(5) (D kappa s)^(-1/4)`
` <= 8 sqrt(5) (kappa^3 s)^(-1/4)`
` <= 8 sqrt(5) kappa_0^(-3/4) / s`
` = 92.1679957028... / s`.                                (3.6)

This is smaller than the Case A constant. A fully algebraic comparison avoids reliance on decimal arithmetic: `sqrt(6)>12/5`, so `kappa_0>1/10`; hence the Case B constant is strictly below `8 sqrt(5) 10^(3/4)/s`, and

`(sqrt(5) 10^(3/4))^4 = 25000 < 131072 = (16*2^(1/4))^4`.

Therefore

`8 sqrt(5) 10^(3/4) < 128*2^(1/4)`.

Combining (3.2) and (3.6) proves (1.1). Averaging the conditional densities over the outside original coordinates preserves the same essential-supremum bound. QED.

## 4. Extremal-product formulation and designated partner application

The theorem implies, in particular, the following geometric inequality for every product of unit-measure measurable sets `E_i` and every interval `J`:

`| {x in prod_i E_i : x^T A x in J} |`
` <= (128*2^(1/4)/s) |J|`,                                (4.1)

whenever the same original `3 x 3` principal block has `sigma_min >= s`.

To apply the designated partner result at an actual inequality, use account04/B13's `QFORM` no-attainment purification theorem at

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1:proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

Its product-purification identity says that for the bounded slab kernel `K=1_{x^TAx in J}`, the supremum over arbitrary cap-one mass-one product densities equals the supremum over unit-measure product indicators, unchanged even if the latter are restricted to bounded finite unions of intervals (with no uniform diameter or fragment-count bound). Applying it to (4.1) transfers the same constant with zero loss to all admissible product densities. This is an actual application to the new localized slab inequality, not an interval-extremality assumption.

## 5. Quantitative structural consequence for the full target

Let

`L_* = 128*2^(1/4) < 152.219`.

For any admissible `(A,X)` define its interval concentration ratio

`R(A,X)=sup_{|J|>0} P(X^TAX in J)/|J|`.

If `R(A,X)>R`, then EVERY original-coordinate `3 x 3` principal block `B` must satisfy

`sigma_min(B) < L_*/R`.                                    (5.1)

Indeed, any block with `sigma_min(B)>=L_*/R` would force `R(A,X)<=R` by (1.1).

Thus any hypothetical counterexample sequence with slab ratios tending to infinity must satisfy

`max_{|I|=3} sigma_min(A[I,I]) -> 0`                       (5.2)

at least at the reciprocal rate dictated by its bad slab ratio. This rigorously isolates the remaining obstruction to the globally delocalized/grouped-bank regime: a genuinely uniformly well-conditioned physical triple is now completely paid without the false arbitrary-joint coarea lemma.

Statement (5.2) is a reduction of the search space, not a proof that such matrices are harmless.

## 6. Continuity and status

The present compilation proves essential boundedness in the localized `3 x 3` principal-block branch. The two dependency theorems do not establish a continuous representative in their full stated scopes, so continuity is NOT claimed here.

Full QFORM remains OPEN. The first remaining B13 structural implication is to combine (5.2) with product-preserving grouped-bank/ridge mechanisms: if all physical triples are quantitatively near-singular while `A` still has three eigenvalues of modulus at least one, extract a bank certificate whose product-set slab inequality is linear in `|J|`, without selecting a reciprocal tiny minor or deleting near-null curvature.

## 7. Numerical check values

`kappa_0 = sqrt(3/8)-1/2 = 0.11237243569579447...`

`128*2^(1/4) = 152.2185107203483...`

`8*sqrt(5)*kappa_0^(-3/4) = 92.16799570280665...`

The proof itself uses the exact inequalities above; the decimals are diagnostics only.
