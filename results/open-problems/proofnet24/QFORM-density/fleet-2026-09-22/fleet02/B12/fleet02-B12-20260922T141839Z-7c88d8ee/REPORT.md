# fleet02/B12 — physical diffuse-core completion and failure of operator-norm density stability

**Run:** `fleet02-B12-20260922T141839Z-7c88d8ee`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** `Additional eigenvalue control`  
**Classification:** `PROVED_SUPPORTING_THEOREM + SOURCE-VALID MECHANISM COUNTEREXAMPLE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  

## 1. Target, correction state, and first unpaid implication

The full target remains OPEN: for every dimension, arbitrary independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal finite bound for the density of `X^T A X`, or give a valid counterexample.

This run uses no independence after spectral rotation, no law-uniform pointwise Fresnel decay, no dimension-losing fiber supremum, no bare coordinate-minor extraction, and no conditional-density surrogate for independence. In particular it respects the current corrections `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`.

The completed named partner result actually consumed is fleet03/B12:

`yspennstate/math-open-problems@733e4b357644bfb6bc6b1ab5b9ca06fac44d711b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/fleet03-B12-20260922T140131Z-r11-ext3/REPORT.md`.

Its theorem `QFORM-DIFFUSE-EXTERIOR-POWER-v1` says the following. Let a symmetric matrix `B=U Lambda U^T` be written using an orthonormal-column matrix `U` spanning its entire nonzero range. Put

`rho=max_i ||u_i||_2^2`,

`delta(rho)=1/2-sqrt(2rho)-rho`.

If `delta>0`, if

`max(1,2rho/delta) <= q < 2`,

and if an integer `m<=rank(B)` satisfies `m>2q`, then for independent density-cap-one coordinates the quadratic form with matrix `B` has a bounded continuous density, uniformly under arbitrary coordinate-separable real perturbations, with

`||p||_infinity <= [K_{m,q}/delta] e_m(Lambda^2)^(-1/(2m))`,

where

`K_{m,q}= e/(2m sqrt(2q)) * Beta(1/(2m),1/(4q)-1/(2m))`.

The theorem permits every extra nonzero eigenvalue inside the certified physical block, of either sign and any magnitude; the exterior-power energy is monotone under adding such directions.

The first unpaid implication for this B12 run was more basic and directly tied to the assignment: **does that source-valid diffuse certificate remain valid after attaching an entirely arbitrary symmetric completion outside the certified physical coordinates, including arbitrary extra eigenvalues and arbitrary cross couplings?** Treating the completion as an independent convolution after rotation would be invalid. Section 2 closes this implication by conditioning only on original independent coordinates.

Section 3 then gives an exact target-valid family proving a complementary negative result: small operator norm of an added/cancelled eigenvalue gives no relative stability whatever for the output density norm under the owner's arbitrary translated density-cap-one laws. Thus a future proof may preserve a certified physical core, but it cannot justify discarding small spectral directions by a naive operator-norm continuity argument.

## 2. Arbitrary physical completion of a diffuse certified core

### Theorem 2.1 — `QFORM-PHYSICAL-DIFFUSE-CORE-ARBITRARY-COMPLETION-v1`

Let `A` be an arbitrary real symmetric `n x n` matrix and let `T subset [n]` be a set of original coordinate indices. Write the physical principal block

`B=A[T,T]=U Lambda U^T`,

where the columns of `U` are orthonormal and span the entire nonzero range of `B`. Put

`rho=max_{i in T} ||u_i||_2^2`,
`delta=1/2-sqrt(2rho)-rho`.

Assume `delta>0`. Choose `q,m` with

`max(1,2rho/delta) <= q < 2`,
`m` an integer, `m<=rank(B)`, `m>2q`.

Then, for arbitrary independent real `X_1,...,X_n` whose one-dimensional densities are bounded by one, the full quadratic form

`Q=X^T A X`

has a bounded continuous density and

`||p_Q||_infinity <= [K_{m,q}/delta] e_m(Lambda^2)^(-1/(2m)).`       (2.1)

No restriction is imposed on:

- the outside block `A[T^c,T^c]`;
- the cross block `A[T,T^c]`;
- the signs, magnitudes, number, or localization of the eigenvalues created by the full completion.

Thus once a physical principal block carries the partner's leverage/exterior-power certificate, **all additional spectral directions outside that block may be arbitrarily smaller, larger, positive, negative, or strongly coupled** without changing the density cap in (2.1).

#### Proof

Condition on the original coordinates `X_{T^c}=z`. Since the original coordinates are independent, the retained vector `Y=X_T` still has independent coordinates with exactly their original density caps at most one.

Block expansion gives

`Q = Y^T B Y + 2 Y^T A[T,T^c] z + z^T A[T^c,T^c] z`.             (2.2)

For fixed `z`, the second term is an arbitrary affine linear tilt in the retained original coordinates and the third term is a scalar translation. The quadratic matrix is exactly the certified physical block `B`; no spectral rotation of the random vector has occurred.

The consumed fleet03/B12 theorem is obtained from the regularized determinant estimate and is uniform under arbitrary coordinate-separable real perturbations. An affine linear tilt is coordinate-separable. Therefore every conditional law in (2.2) has a continuous density `p_z` with the same uniform bound

`||p_z||_infinity <= C_B := [K_{m,q}/delta] e_m(Lambda^2)^(-1/(2m)).`  (2.3)

Averaging conditional laws immediately gives an unconditional density bounded by `C_B`. For continuity, the source theorem supplies a common integrable characteristic-function envelope, independent of the affine tilt. Averaging the conditional characteristic functions preserves that envelope, so Fourier inversion gives a continuous representative for the unconditional law as well. This proves (2.1). QED.

### Corollary 2.2 — three-large-eigenvalue physical core

If the certified block `B` has at least three eigenvalues of absolute value at least `L`, then

`e_3(Lambda^2) >= L^6`.

Whenever

`rho < rho_3^* := (39-6sqrt(30))/98 = 0.06261884234377585...`,

one may choose `m=3` and some `q<3/2`, giving

`||p_Q||_infinity <= [K_{3,q}/delta] / L`.                       (2.4)

This is a genuine target-level subclass if `L>=1`. By principal interlacing, the full completion also has at least the corresponding three large positive/negative directions required by the owner target; however the proof does not need to identify or rotate into them.

### Explicit mixed-sign checkpoint

Take 64 original coordinates in `T`, and let `U` have three Walsh columns

`u_1(j)=1/8`,
`u_2(j)=(-1)^{bit_0(j)}/8`,
`u_3(j)=(-1)^{bit_1(j)}/8`,

for `j=0,...,63`. They are orthonormal and every row has leverage

`rho=3/64`.

Let

`Lambda=diag(1,1,-1)`.

Then

`delta=(29-8sqrt(6))/64 = 0.14693878215210276...`,

and

`2rho/delta=0.63802080449...<1`,

so `q=1,m=3` are admissible. With

`K_{3,1}= e/(6sqrt(2)) Beta(1/6,1/12)
        =5.655763773387239...`,

Theorem 2.1 gives the explicit completion-stable bound

`||p_Q||_infinity <= 38.49061282904... < 38.491`.                (2.5)

Every symmetric block and every coupling on any number of additional coordinates may now be attached to this 64-coordinate mixed-sign core without changing (2.5).

This example also shows why **full-range leverage is not a stable necessity**. Add one new coordinate with any nonzero diagonal eigenvalue `mu`, however tiny. The range projection of the *whole* completed matrix has leverage one at that new coordinate, so a theorem requiring low leverage of the whole range immediately ceases to apply. Nevertheless Theorem 2.1 keeps the physical 64-coordinate core and proves exactly the same bound. Hence the correct additional-eigenvalue interface is local/conditional, not continuity of the whole support projection.

## 3. Small operator-norm spectral additions have no relative density stability

A tempting reduction for the full conjecture is: truncate all eigenvalues below a small threshold, prove the theorem for the truncated matrix, and transfer the density bound back by operator-norm continuity. Under the owner's hypotheses this mechanism is false in a strong quantitative sense, even for diagonal target matrices.

### Theorem 3.1 — `QFORM-OPERATOR-NORM-RELATIVE-LINF-STABILITY-FALSE-v1`

For every `0<epsilon<1` and every `M>0`, there exist two diagonal symmetric target matrices `A_epsilon,B` such that

- each has at least three eigenvalues of absolute value at least one;
- `||A_epsilon-B||_op=epsilon`;
- there are independent input coordinates, each with density exactly bounded by one, for which both quadratic outputs have bounded densities but

`||p_{B}||_infinity / ||p_{A_epsilon}||_infinity >= M`.           (3.1)

Consequently there is no finite function `F(epsilon)` such that, uniformly over the owner's input class,

`||p_{X^T B X}||_infinity <= F(epsilon) ||p_{X^T A X}||_infinity`

whenever `||A-B||_op<=epsilon`, even when both matrices remain inside the exact three-large-eigenvalue target class.

#### Construction and proof

Take

`B=diag(0,1,1,1)`,
`A_epsilon=diag(epsilon,1,1,1)`.

Both matrices have three eigenvalues equal to one, and their operator-norm distance is exactly `epsilon`.

Let

`X_1 ~ Uniform[R,R+1]`,
`X_2,X_3,X_4 ~ Uniform[-1/2,1/2]`,

independently. Every density equals one on its support, so the source is admissible with no moment, centering, or support assumptions added.

Put

`W=X_2^2+X_3^2+X_4^2`.

The `B`-output equals `W`, which is supported in `[0,3/4]` and has total probability one. Hence every density representative satisfies

`||p_B||_infinity >= 1/(3/4)=4/3`.                              (3.2)

For `A_epsilon`, write

`Y=epsilon X_1^2`.

Because `X_1>0`, the change of variables is one-to-one and

`p_Y(y)=1/(2 epsilon x)=1/(2 sqrt(epsilon y))`

on its support. Therefore

`||p_Y||_infinity = 1/(2 epsilon R)`.                            (3.3)

Since `Y` is independent of `W`,

`p_{A_epsilon}=p_Y*p_W`,

and convolution with a probability density cannot increase `L^infinity`; thus

`||p_{A_epsilon}||_infinity <= 1/(2 epsilon R)`.                 (3.4)

Combining (3.2)-(3.4),

`||p_B||_infinity / ||p_{A_epsilon}||_infinity
 >= (4/3)(2 epsilon R)
 = 8 epsilon R/3`.                                               (3.5)

Choose `R>=3M/(8epsilon)`. Then (3.1) follows. QED.

### Interpretation

This is **not** a counterexample to QFORM. Both forms are diagonal, so the already-proved diagonal theorem gives an absolute universal cap. The theorem instead kills a specific additional-eigenvalue shortcut: no relative `L^infinity` stability can depend only on the operator norm of the spectral perturbation. The reason is source-valid and unavoidable under the owner's quantifiers: density-cap-one laws may be translated arbitrarily far, turning an arbitrarily small quadratic coefficient into a large independent smoothing term.

Accordingly, a successful reduction for arbitrary smaller/larger eigenvalues must preserve a source-exact physical smoother or use an absolute aggregate bound. It cannot simply discard small spectral directions and transfer the output density norm by continuity in `A`.

## 4. Relation to the partner result and remaining full-target bridge

The positive theorem above applies the named partner fleet03/B12 result in the strongest completion direction that conditioning permits: arbitrary outside matrix and arbitrary outside/cross spectral effects are absorbed without any independence claim after rotation. The negative theorem explains why this physical-block formulation is materially safer than an operator-norm spectral truncation.

The full conjecture remains OPEN because the owner hypothesis gives only three large eigenvalues somewhere in the global spectrum; it does not ensure that one can find a physical principal block whose entire range has leverage below `rho_3^*`. The current correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` supplies exact rank-three families where every fixed small physical block degenerates, so extracting one bounded-size block cannot be the missing universal argument.

The next exact implication is therefore:

> **`QFORM-PHYSICAL-DIFFUSE-CORE-OR-AGGREGATE-EXTRACTION` (OPEN).** From only three large eigenvalues of an arbitrary symmetric matrix, prove a dimension-free product-preserving decomposition that either isolates a physical principal core satisfying Theorem 2.1, or routes the complementary distributed spectral mass into one of the already certified aggregate smoothers, without selecting a dimension-losing single minor and without discarding small eigenvalues by operator-norm continuity.

The partner's proposed exterior-power identity

`e_3(A^2)=sum_{|I|=|J|=3} det(A[I,J])^2 >=1`

remains a plausible accounting resource because it aggregates all physical minors before reciprocal payment. This run does not prove the required overlap-channel extraction.

## 5. Verification, status, and source pins

The arithmetic checker in this immutable run directory verifies the Walsh-core leverage, exact diffuse threshold comparison, beta-function constant, completion cap, and the quantitative relative-instability ratio. It reports `QFORM_B12_COMPLETION_STABILITY_CHECK_PASS`.

**Proved here:**

1. `QFORM-PHYSICAL-DIFFUSE-CORE-ARBITRARY-COMPLETION-v1`, an arbitrary-completion theorem for every partner-certified physical diffuse core;
2. explicit 64-coordinate mixed-sign completion-stable target core with density cap `<38.491`;
3. `QFORM-OPERATOR-NORM-RELATIVE-LINF-STABILITY-FALSE-v1`, an exact admissible counterexample to spectral-truncation/relative-density stability.

**Not proved:** the full three-large-eigenvalue conjecture, a universal extraction of a diffuse physical core, or a universal absolute density transfer from arbitrary spectral truncation.

Primary source pins:

- fresh QFORM control at start: `yspennstate/math-research-brain@3244bd53a0a59ae0c6bdf8eb8dc6dfd54834a1cb`, revision `2026-09-22.5`;
- fresh prewrite control/correction check: `yspennstate/math-research-brain@ddaac68c76b42869262316300669da0b91875562`;
- named partner exterior-power theorem: `yspennstate/math-open-problems@733e4b357644bfb6bc6b1ab5b9ca06fac44d711b:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/fleet03-B12-20260922T140131Z-r11-ext3/REPORT.md`;
- preceding own same-sign physical-block theorem: `yspennstate/math-open-problems@8f66972059845cb23d014fa20efee714b6655b99:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/fleet02-B12-20260922T1251Z-qform-additional-eigenvalue/REPORT.md`.

No full-solution or novelty claim is made.
