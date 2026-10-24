# account01/B15 — affine homogenization closure and third-eigenvalue normal form

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Worker:** account01/B15  
**Run:** `20260922T170451Z-account01-B15-qform-r11`  
**Assignment:** Absolute continuity and regularity  
**Status:** ESSENTIAL_STEP_APPLIED / EXACT_AFFINE_CLOSURE_AND_NORMALIZATION  
**Full universal-constant QFORM:** OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target

For independent real `X_1,...,X_n` with probability densities `0<=f_i<=1` and real symmetric `A` having at least three eigenvalues of modulus at least one, the open target is a universal finite `C` such that

`P(X^T A X in I) <= C |I|`

for every interval `I`, uniformly in dimension, matrix and input laws. Continuity is a separate stronger conclusion.

This run proves an exact closure principle useful in Schur/completing-square arguments: adding an arbitrary deterministic affine term costs **zero** in the sharp universal constant. It also gives an exact `s_3(A)=1` normal form, where `s_3(A)` is the third largest singular value (equivalently third largest eigenvalue modulus for symmetric `A`).

## 2. Concentration seminorm and weak-limit closure

For a real random variable `Y`, define

`D(Y) = sup_{I open interval} P(Y in I)/|I|`,

allowing `+infinity`.

If `D(Y)<infinity`, then the law of `Y` is absolutely continuous and has a density with essential supremum at most `D(Y)`; conversely a density `p` has `D(Y)=||p||_infinity`. This follows from the interval domination `mu(I)<=D|I|` and the Lebesgue differentiation theorem.

### Lemma 2.1 — lower semicontinuity under weak convergence

If `Y_k => Y`, then

`D(Y) <= liminf_k D(Y_k)`.

**Proof.** For every open interval `I`, Portmanteau gives

`P(Y in I) <= liminf_k P(Y_k in I) <= |I| liminf_k D(Y_k)`.

Take the supremum over `I`. QED.

This lemma requires no moment, support or smoothness assumptions.

## 3. Spectral count is preserved by one-coordinate homogenization

Let `A` be an `n x n` real symmetric matrix, and let

`M = [[A,u],[u^T,a]]`

be any real symmetric `(n+1)x(n+1)` extension having `A` as a principal submatrix.

Write

`N_+(A)=#{lambda(A)>=1}`, `N_-(A)=#{lambda(A)<=-1}`.

### Lemma 3.1 — protected-sign interlacing

`N_+(M)>=N_+(A)` and `N_-(M)>=N_-(A)`.

**Proof.** Order eigenvalues decreasingly. If `lambda_r(A)>=1`, Cauchy interlacing gives `lambda_r(M)>=lambda_r(A)>=1`. If `A` has `s` eigenvalues at most `-1`, then `lambda_{n-s+1}(A)<=-1`; interlacing gives

`lambda_{n-s+2}(M) <= lambda_{n-s+1}(A) <= -1`,

so the final `s` eigenvalues of `M` are at most `-1`. QED.

Therefore, if `A` has at least three eigenvalues of modulus at least one, **every** one-coordinate symmetric extension `M` also has at least three such eigenvalues. No strict spectral margin and no perturbative Weyl argument are needed.

## 4. Exact affine homogenization theorem

For admissible independent `X`, define the affine quadratic

`Q_{A,b,c}(X)=X^T A X + 2 b^T X + c`.

Let

`C_hom = sup D(X^T A X)`

over all owner-target instances, and

`C_aff = sup D(Q_{A,b,c}(X))`

over the same target matrices and admissible inputs, with arbitrary deterministic `b in R^n`, `c in R`.

Both suprema are allowed to be infinite.

### Theorem 4.1 — affine terms cost exactly zero

`boxed(C_aff = C_hom)`.

**Proof.** The inequality `C_hom<=C_aff` is immediate by taking `b=c=0`.

For the converse fix one affine target instance `(A,b,c,X)`. The additive constant `c` only translates the output and does not change `D`, so first take `c=0`.

For `R>0`, let `U` be independent `Uniform[0,1]` and set `Y_R=R+U`; its density is exactly one on `[R,R+1]`, hence admissible. Define the symmetric extension

`M_R = [[A,b/R],[b^T/R,0]]`.

By Lemma 3.1, `M_R` satisfies the same three-large-eigenvalue target condition for **every** `R>0`. The homogeneous target variable in dimension `n+1` is

`Z_R = (X,Y_R)^T M_R (X,Y_R)
     = X^T A X + 2 (Y_R/R) b^T X`.

Under the above coupling `Y_R/R=1+U/R -> 1` almost surely. Since every coordinate of `X` is finite almost surely,

`Z_R -> X^T A X + 2 b^T X`

almost surely, hence weakly. Lemma 2.1 yields

`D(Q_{A,b,0}) <= liminf_{R->infinity} D(Z_R) <= C_hom`.

Adding back `c` leaves `D` unchanged. Taking the supremum over affine instances gives `C_aff<=C_hom`. QED.

### Consequence 4.2 — proof architecture

Any universal interval-density theorem established for homogeneous target quadratics automatically holds, with the **identical constant**, for arbitrary deterministic affine quadratics with the same Hessian `A`. Thus deterministic linear leakage produced by a global completion of squares need not be paid separately in a final universal proof.

This statement must not be misused after conditioning on a small block whose Hessian itself no longer has three protected eigenvalues; Theorem 4.1 preserves the target condition on the full Hessian, not on arbitrary conditional subblocks.

## 5. Assigned-partner theorem applied to an actual inequality

I use the completed `account02/B15` result exactly as proved at

`yspennstate/math-open-problems@28ddaf28bf6779837fb1212a025d8a8b9d329f8a`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T160529Z-account02-B15-qform-r4/REPORT.md`.

That report proves: every real symmetric `A` of rank at least three has a bounded continuous output density in `C_0(R)` for arbitrary independent cap-one marginals, and if `B=A_{J,J}` is any invertible physical principal block of order `d=3` or `4`, then the conditional affine block theorem gives the uniform-in-outside-variables height

`||p||_infinity <= C_d/sigma_min(B)`,

where

`C_3 = 2*pi + 3*sqrt(3)`,

`C_4 = 4*pi + 8`.

The local theorem explicitly permits arbitrary affine terms. Therefore for the **global affine** variable of Theorem 4.1, conditioning on `X_{J^c}=w` gives

`Y^T B Y + 2(A_{J,J^c}w+b_J)^T Y + c_w`.

Applying the partner inequality pointwise in `w` and integrating gives the actual bound

`boxed(||p_{Q_{A,b,c}}||_infinity <= C_d/sigma_min(B))`.

The partner's `C_0` tail/continuity argument is also uniform in the affine vector at the height step, so dominated convergence gives

`boxed(p_{Q_{A,b,c}} in C_0(R))`

for every fixed rank-at-least-three `A`, arbitrary deterministic `b,c`, and every admissible product input. This is qualitative/matrix-dependent regularity, not the missing universal constant.

In particular, for every affine owner-target instance, `D(Q_{A,b,c})` is an **attained pointwise maximum** of its canonical continuous density.

## 6. Exact third-singular-value normal form

For symmetric `A`, let `s_3(A)` be the third largest singular value, i.e. the third largest `|lambda_j(A)|`. On the owner target `s_3(A)>=1`.

For any affine target instance put

`B=A/s_3(A)`, `beta=b/s_3(A)`, `gamma=c/s_3(A)`.

Then `s_3(B)=1` and

`Q_{A,b,c}=s_3(A) Q_{B,beta,gamma}`.

Hence

`D(Q_{A,b,c}) = s_3(A)^(-1) D(Q_{B,beta,gamma}) <= D(Q_{B,beta,gamma})`.

The reverse inequality is trivial because the normalized class is a subclass. Therefore both sharp constants admit the exact normal form

`boxed(C_hom = C_aff
 = sup_{s_3(A)=1, admissible X, b,c} D(Q_{A,b,c})
 = sup_{s_3(A)=1, admissible X} D(X^T A X))`.

Using the partner `C_0` theorem this can be written pointwise as

`boxed(C_* = sup_{s_3(A)=1, admissible X} max_t p_{X^TAX}(t)
            = sup_{s_3(A)=1, admissible X, b,c} max_t p_{Q_{A,b,c}}(t))`.

Thus a proof may normalize the third protected eigenvalue modulus to exactly one. In that normalization every further eigenvalue (fourth and below in modulus order) has modulus at most one; only the top two protected eigenvalues can remain arbitrarily large.

## 7. What changed and what remains unpaid

**New proved implication.** The sharp universal homogeneous target constant is exactly unchanged by arbitrary deterministic affine terms, proved by one-coordinate cap-one homogenization plus Cauchy interlacing. The sharp problem is also exactly reducible to `s_3(A)=1`, and every such fixed affine output has an attained `C_0` density by the completed assigned-partner theorem.

This directly removes deterministic affine leakage as a separate endgame obstruction and gives proof-assembly workers a canonical spectral scale.

**Still unpaid.** Nothing here bounds

`sup_{s_3(A)=1} max_t p_{X^TAX}(t)`

uniformly. The reciprocal-principal-minor factor in the partner theorem can still diverge on delocalized matrices. The latest correction ledger also rules out replacing that missing aggregate step by a uniformly good small principal block, a rank-three cross cut, rotated independence, projection-only density control, or law-uniform pointwise quadratic Fourier decay.

The next central implication remains the product-preserving aggregate high-leverage/near-isotropic bridge, now allowed to carry arbitrary deterministic affine terms for free and to work at the exact normalization `s_3(A)=1`.

No claim of a full solution is made.
