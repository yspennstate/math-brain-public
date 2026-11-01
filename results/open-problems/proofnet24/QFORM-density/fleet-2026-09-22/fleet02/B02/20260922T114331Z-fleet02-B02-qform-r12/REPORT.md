# fleet02/B02 — integrated Fourier bound for delocalized rank-three forms

**Run:** `20260922T114331Z-fleet02-B02-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** fleet02/B02, `Integrated Fourier estimate` / pathway `FOURIER`  
**Classification:** `ESSENTIAL_STEP_APPLIED / INTEGRATED_FOURIER_DELOCALIZED_RANK3 / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Scope, corrections and dependencies

The later owner order supersedes this worker's earlier FEI assignment. The live target is the universal bounded-density conjecture for `Q=X^T A X` when the independent real inputs have densities at most `1` and `A` has at least three eigenvalues of magnitude at least `1`.

I consumed the three required route corrections from the current programme state:

1. `QFORM-POINTWISE-DECAY-FALSE`: arbitrary bounded input densities can be phase-aligned, so no law-uniform pointwise one-dimensional Fresnel decay may be assumed.
2. `QFORM-FIBER-SUP-DIMENSION-LOSS`: an unrestricted spectral-fiber supremum can lose dimension.
3. `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: diagonalizing `A` does not preserve independence.

The named partner `fleet03/B02` had no completed current-programme handoff at the fresh snapshot, so I did not wait. I applied two exact peer sources instead.

* `fleet02/B15`, immutable report `yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8:qform/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`, proves a three-physical-coordinate theorem but exhibits a flat rank-three Hadamard projector for which every fixed principal triple is small.
* `fleet02/B06`, immutable report `yspennstate/math-open-problems@6902eb62f21a7c833ca27dcca69f34d50e711a7d:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`, strengthens the obstruction to the indefinite Hadamard family `A=U diag(1,1,-1)U^T`, where every fixed-size physical compression has norm `O(m/n)`.

The external analytic input is Mark Rudelson and Roman Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015, no. 19, 9594–9617, DOI `10.1093/imrn/rnu243`, arXiv `1402.4492`. I use their Lemma 3.1 and Proposition 5.1 **at the proof level**, not merely the stated projection-density conclusion. In the small-coordinate regime `||Pe_i||<=1/2`, their Brascamp–Lieb argument proves an absolute Fourier integral bound

`int_{R^d} |phi_{RX}(xi)| dxi <= B_RV^d`

for one absolute finite constant `B_RV` when every input density is at most `1` and `RR^T=I_d`. Their published proof writes this bound as `(2C)^d`; I set `B_RV:=2C`. This distinction matters because a mere `L^infinity` bound on the projected density would not suffice for the indefinite quadratic shell.

## 1. New Fourier-algebra lemma for a delocalized three-dimensional projection

Let `U` be an `n x 3` real matrix with orthonormal columns, and write its rows as `u_i in R^3`. Let

`Y=U^T X`,

where the coordinates of `X` are independent and have densities at most `1`. Assume the leverage bound

`max_i ||u_i|| <= 1/2`.  (1.1)

Since `P=UU^T` is the orthogonal projection onto the column space of `U`,

`||P e_i||=||u_i||`.

Therefore the small-coordinate hypothesis of Rudelson–Vershynin Proposition 5.1 is exactly (1.1). Their proof identifies the characteristic function

`Phi_Y(xi)=prod_i phi_i(<u_i,xi>)`

and applies Brascamp–Lieb with weights `||u_i||^2`; using their rearrangement estimate from Lemma 3.1 gives

`boxed( ||Phi_Y||_{L^1(R^3)} <= B_RV^3 ).`  (1.2)

This is strictly stronger than only knowing that `Y` has a bounded density. It is also source-valid under arbitrary densities `0<=f_i<=1`; no moments, continuity, centering or log-concavity are used.

## 2. Fresnel transfer: an `L^1` Fourier projection gives `|t|^{-3/2}` for the quadratic output

### Theorem 2.1 — `QFORM-DELOCALIZED-RANK3-INTEGRATED-FOURIER-v1`

Let

`A=U Lambda U^T`,

where `U^T U=I_3`, `Lambda=diag(lambda_1,lambda_2,lambda_3)`, and

`|lambda_j|>=1` for `j=1,2,3`.

Thus `A` has rank exactly three, with arbitrary signature. Assume (1.1). For independent inputs with densities at most `1`, put

`Q=X^T A X=Y^T Lambda Y`, `Y=U^T X`.

Then the characteristic function of `Q` obeys, for every `t!=0`,

`boxed( |phi_Q(t)| <= K_RV |det Lambda|^{-1/2} |t|^{-3/2} ),`  (2.1)

where

`K_RV := B_RV^3/(8 pi^{3/2})`.

Consequently

`boxed( int_R |phi_Q(t)| dt <= 2 + 4 K_RV ),`  (2.2)

and `Q` has a bounded **continuous** density satisfying

`boxed( ||p_Q||_infinity <= 1/pi + B_RV^3/(4 pi^{5/2}). )`  (2.3)

The constant is universal and independent of `n`, the input laws, the signs of the three eigenvalues and their magnitudes above `1`.

### Proof

By (1.2), `Phi_Y` is integrable. Hence `Y` has a bounded continuous density `h` represented by the absolutely convergent inverse Fourier formula

`h(y)=(2pi)^{-3} int exp(i <xi,y>) Phi_Y(xi) dxi`.

Fix `t!=0`. Directly substituting this inverse formula into the oscillatory integral for `phi_Q(t)` is not absolutely justified in `y`, so regularize. For `epsilon>0`, define

`I_epsilon(t)=int h(y) exp(-epsilon |y|^2) exp(i t y^T Lambda y) dy`.

The Gaussian factor makes Fubini valid. Thus

`I_epsilon(t)=(2pi)^{-3} int Phi_Y(xi) G_{epsilon,t}(xi) dxi`,

where

`G_{epsilon,t}(xi)=int exp[-y^T(epsilon I-i t Lambda)y+i<xi,y>] dy`.

The standard complex Gaussian integral gives

`G_{epsilon,t}(xi)=pi^{3/2} det(epsilon I-i t Lambda)^{-1/2}`

times an exponential factor whose modulus is at most `1`, because the real part of `(epsilon I-i t Lambda)^{-1}` is positive definite. Hence

`|G_{epsilon,t}(xi)| <= pi^{3/2} prod_j (epsilon^2+t^2 lambda_j^2)^{-1/4}`

`<= pi^{3/2}|t|^{-3/2}|det Lambda|^{-1/2}`.  (2.4)

Using (1.2),

`|I_epsilon(t)| <= (2pi)^{-3} pi^{3/2} B_RV^3 |t|^{-3/2}|det Lambda|^{-1/2}`

`= K_RV |t|^{-3/2}|det Lambda|^{-1/2}`.

Since `|exp(-epsilon |Y|^2)|<=1`, dominated convergence in the original expectation gives `I_epsilon(t)->phi_Q(t)` as `epsilon downarrow 0`, proving (2.1).

Now use `|phi_Q(t)|<=1`. On `|t|<=1` the integral contributes at most `2`; on the two tails, (2.1) and `|det Lambda|>=1` give

`2 K_RV int_1^infinity t^{-3/2}dt = 4 K_RV`.

This proves (2.2). Since `phi_Q in L^1(R)`, Fourier inversion gives a bounded continuous representative of the density and

`||p_Q||_infinity <= (2pi)^{-1} ||phi_Q||_1`,

which is exactly (2.3). `QED`.

## 3. This closes the previously exposed flat Hadamard obstruction

The B15/B06 obstruction uses a normalized Hadamard `U` with three columns. Every row has

`||u_i||=sqrt(3/n)`.

Thus for every Sylvester order `n>=16`,

`sqrt(3/n)<=1/2`,

so Theorem 2.1 applies immediately. In particular it handles both

* the positive rank-three projector `A=UU^T` from B15, and
* the genuinely indefinite flat form `A=U diag(1,1,-1)U^T` from B06,

with a universal integrated-Fourier and output-density constant, despite the fact that every fixed-size physical coordinate compression has vanishing curvature as `n->infinity`.

This is the substantive bridge: the determinant mass spread over many tiny coordinate minors is captured globally by the Brascamp–Lieb Fourier integral, so no single large principal triple is required in the delocalized regime.

## 4. A decisive boundary: projection-Fourier `L^1` is sufficient here, but not necessary

One must not overextend (1.2) to localized frames. Take `n=3`, `U=I_3`, and let each `X_i` be uniform on `[0,1]`. Then

`Phi_Y(xi)=prod_{j=1}^3 exp(i xi_j/2) * 2 sin(xi_j/2)/xi_j`.

The one-dimensional integral of `|sin(s)|/|s|` diverges, so

`||Phi_Y||_{L^1(R^3)}=infinity`.

Nevertheless `Q=X_1^2+X_2^2+X_3^2` lies in the already proved diagonal branch. More specifically, each square density is in `L^{3/2}` with a universal norm bound, so Hausdorff–Young places each square characteristic function in `L^3`; Holder then gives `phi_Q in L^1`.

Therefore the auxiliary implication

`projection characteristic Phi_{U^T X} in L^1  =>  quadratic characteristic phi_Q in L^1`

is useful but **not reversible**, and `||Phi_{U^T X}||_1<infinity` is not a valid universal prerequisite. This explains why the Rudelson–Vershynin large-coordinate part of their projection theorem cannot simply be substituted into the present Fresnel argument: their full density theorem uses concentration/tensorization after the small-coordinate Fourier regime rather than establishing this global Fourier-algebra norm.

## 5. Conditional end-to-end picture and first unpaid implication

For rank-three forms, two complementary mechanisms are now rigorous.

1. **Localized physical curvature:** B15 proves a universal bound when some physical principal triple is uniformly nonsingular; B06/B12 supply sharper special physical blocks.
2. **Delocalized spectral frame:** Theorem 2.1 proves a universal bound when every spectral-row leverage satisfies `||u_i||<=1/2`.

The flat Hadamard adversary, which killed fixed-triple localization, lies entirely in branch 2 for large `n` and is therefore no longer an obstruction.

The first exact missing implication for the rank-three problem is a **hybrid large-row reduction**:

> If some row of the three-eigenvector frame has norm `>1/2`, prove that either a product-preserving physical block is strong enough for the B15/B12/B06 conditioning estimates, or remove that large row while retaining a two-dimensional integrated-Fourier resource strong enough to combine with the remaining quadratic direction.

This is a finite-leverage regime: because `sum_i ||u_i||^2=3`, only finitely many rows can exceed any fixed threshold. The difficulty is not cardinality but possible indefinite cancellation (`u_i^T Lambda u_i` can be small even when `||u_i||` is large) and preserving independence while exploiting the residual frame.

For the **full owner target** with more than three nonzero eigendirections, one additional implication is required even after rank three is closed: a three-eigenvalue spectral truncation cannot simply be convolved with the remaining quadratic part because both depend on the same original independent coordinates. Any extension must preserve that dependence rather than pretending the spectral pieces are independent.

## 6. Status

**PROVED / supporting:** `QFORM-DELOCALIZED-RANK3-INTEGRATED-FOURIER-v1`, including `|t|^{-3/2}` decay, a uniform `L^1` characteristic-function bound, and a continuous bounded density for the stated delocalized rank-three class.

**ESSENTIAL_STEP_APPLIED:** this theorem closes the explicit delocalized Hadamard rank-three family that defeated every fixed-size physical-coordinate localization.

**CANDIDATE_REFUTED / mechanism only:** requiring `||Phi_{U^T X}||_1<infinity` as a universal projection prerequisite; the localized cube example has infinite projection Fourier `L^1` although the quadratic output is in the known bounded diagonal branch.

**OPEN:** the large-leverage hybrid for arbitrary rank-three eigenframes, the passage from three selected eigendirections to arbitrary additional coupled eigendirections, and the full owner conjecture.

No novelty or publication-priority claim is made. No numerical experiment was needed in this run; the argument is analytic and source-bound.
