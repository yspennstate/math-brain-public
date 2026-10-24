# account01/B17 — sharp centered-Gaussian ceiling for indefinite rank-three quadratic limits

Programme: `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`.
Run: `20260922T120821Z-account01-B17-qform-sharp-constant-v1`.
Assignment: `Sharp constant and witnesses` / pathway `STRUCTURE`.
Classification: `AUXILIARY_ONLY / SHARP_GAUSSIAN_LIMIT_CEILING`; full target remains OPEN / NOT PROVED.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source state and partner result actually applied

Fresh coherent control source was `yspennstate/math-research-brain@f22710549d776d9514d40c0ac84faf51dc0526ad`, revision `2026-09-22.5`. The later live correction snapshot at `fa9dd92ed4d35af5fb5572dbb1b37698806f3562` contains `QFORM-CROSSMINOR-ALONE-FALSE`; nothing below uses the refuted cross-minor-only implication.

Named partner account02/B17 was consumed at its complete immutable source:

- repository `yspennstate/math-open-problems`
- commit `4a3d4af77778f20a95855c6dfbf69540dcfa5fe4`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T114529Z-qform-sharp-witness/REPORT.md`.

That report proves the target-level lower bound `C >= 3 sqrt(2)` by a three-block diffuse uniform construction converging to `(Z_1^2+Z_2^2-Z_3^2)/12`, and notes only that `3 sqrt(2)` is the ceiling of the simple iid equal-variance block mechanism. The theorem below applies that lower-bound witness and proves that the same value is the exact ceiling for the much larger class of **all centered Gaussian rank-three indefinite limits whose covariance is compatible with the density-one variance floor**, allowing arbitrary correlations and arbitrary orthogonal eigenvector mixing.

## 2. Density-one variance floor

### Lemma 2.1
If a real random variable `X` has density `f<=1` and finite variance, then

`Var(X) >= 1/12`.

Proof. For every real `a` and `r>=0`,

`P(|X-a|<=r) <= 2r`.

Hence, with `a=EX`,

`Var(X)=int_0^infty 2r P(|X-a|>r) dr
       >= int_0^(1/2) 2r(1-2r) dr = 1/12`.

Equality is attained by a uniform distribution on an interval of length one. QED.

Consequently, if `X=(X_i)` has independent coordinates of finite variance with density caps one, `R` is any `n x 3` matrix with orthonormal columns, and `Y=R^T(X-EX)`, then

`Cov(Y)=R^T diag(Var X_i) R >= (1/12) I_3`.

This statement keeps the original-coordinate independence; no independence after rotation is asserted.

## 3. Main theorem: a sharp `3 sqrt(2)` ceiling for every centered Gaussian indefinite rank-three limit

### Theorem `QFORM-GAUSSIAN-INDEFINITE-CEILING-3SQRT2-v1`
Let `G~N(0,Sigma)` in `R^3`, with

`Sigma >= sigma^2 I_3`

for some `sigma>0`. Let `Lambda` be any real symmetric nonsingular `3 x 3` matrix of inertia `(2,1)` or `(1,2)` and suppose

`min_j |lambda_j(Lambda)| >= 1`.

For

`Y = G^T Lambda G`,

the density exists, is bounded and continuous, and

`||p_Y||_infinity <= 1/(2 sqrt(2) sigma^2)`.

If `sigma^2=1/12`, then

`||p_Y||_infinity <= 3 sqrt(2)`.

The constant is sharp: equality occurs for `Sigma=sigma^2 I_3` and `Lambda=diag(1,1,-1)` (or the sign-reversed case).

### Proof
Write `G=Sigma^(1/2) Z` with `Z~N(0,I_3)` and set

`B=Sigma^(1/2) Lambda Sigma^(1/2)`.

The matrix `B` is symmetric and has the same inertia as `Lambda`. Moreover

`B^(-1)=Sigma^(-1/2) Lambda^(-1) Sigma^(-1/2)`,

so

`||B^(-1)||op <= ||Sigma^(-1/2)||op^2 ||Lambda^(-1)||op <= sigma^(-2)`.

Because `B` is symmetric, every eigenvalue `mu` of `B` therefore satisfies

`|mu| >= sigma^2`.

After an orthogonal change of the standard Gaussian coordinates, and reversing the global sign if needed, we may write

`Y = a U^2 + b V^2 - c W^2`,

where `U,V,W` are independent standard Gaussians and

`a,b,c >= sigma^2`.

Put `S=aU^2+bV^2` and `T=cW^2`. The density of `T` is

`g_c(t)=(2 pi c t)^(-1/2) exp(-t/(2c)),  t>0`,

which is strictly decreasing. The density of `S` is

`h_{a,b}(s)= [2 sqrt(ab)]^(-1)
 exp(-(a+b)s/(4ab))
 I_0(|a-b|s/(4ab)),   s>=0`,

where `I_0` is the modified Bessel function. Let

`alpha=(a+b)/(4ab)`, `beta=|a-b|/(4ab)`.

Since `alpha>beta>=0` and `0<=I_1(x)/I_0(x)<1` for `x>=0`,

`d/ds log h_{a,b}(s) = -alpha + beta I_1(beta s)/I_0(beta s) < 0`.

Thus `h_{a,b}` is decreasing. It follows that the density of `Y=S-T` is maximized at zero. Indeed, for `y>=0`,

`p_Y(y)=int_0^infty h_{a,b}(y+t) g_c(t) dt <= p_Y(0)`,

while for `y<0`,

`p_Y(y)=int_0^infty h_{a,b}(s) g_c(s-y) ds <= p_Y(0)`.

It remains to bound `p_Y(0)`. Direct Gaussian polar integration in the `(U,V)` plane gives the exact representation

`p_Y(0)= (1/(4 pi)) int_0^(2 pi)
 [A(theta)(A(theta)+c)]^(-1/2) dtheta`,

where

`A(theta)=a cos^2(theta)+b sin^2(theta)`.

For completeness, this follows by integrating the delta constraint
`a u^2+b v^2=c w^2`: integrating first in `w` contributes

`(2 pi c)^(-1/2) [a u^2+b v^2]^(-1/2)
 exp(-(a u^2+b v^2)/(2c))`,

and the remaining radial Gaussian integral yields the displayed formula.

Since `A(theta)>=sigma^2` and `c>=sigma^2`,

`A(theta)(A(theta)+c) >= 2 sigma^4`.

Therefore

`p_Y(0) <= (1/(4 pi)) (2 pi)/(sqrt(2) sigma^2)
          = 1/(2 sqrt(2) sigma^2)`.

This is also the global density norm by the preceding monotonicity argument. Equality requires `A(theta)=sigma^2` for all theta and `c=sigma^2`, hence `a=b=c=sigma^2`; it is attained by the isotropic covariance and signature `(1,1,-1)`. QED.

## 4. Consequence for diffuse product-law CLT witnesses

Consider any sequence of centered independent-coordinate vectors `X^(m)` whose coordinate densities are at most one and whose coordinates have finite variance. Let `R_m` have three orthonormal columns and assume the projected vectors

`R_m^T X^(m)`

converge under a standard covariance-convergent CLT to a centered Gaussian `G~N(0,Sigma)`. By Lemma 2.1,

`R_m^T diag(Var X_i^(m)) R_m >= (1/12) I_3`,

so every covariance limit satisfies `Sigma >= I_3/12`.

For any fixed rank-three spectral form with one sign opposed to the other two and eigenvalue magnitudes at least one, Theorem 3 gives

`||p_{G^T Lambda G}||_infinity <= 3 sqrt(2)`.

The partner account02/B17 three-block uniform family has `Sigma=I_3/12`, `Lambda=diag(1,1,-1)`, and its limiting density has peak exactly `3 sqrt(2)`. Hence:

**Corollary `QFORM-CENTERED-GAUSSIAN-LIMIT-OPTIMALITY-v1`.**
`3 sqrt(2)` is the exact optimal peak within the entire centered Gaussian rank-three indefinite limit class compatible with the one-dimensional density cap, not merely within iid equal-block constructions.

Thus any target witness that pushes the universal lower bound strictly above `3 sqrt(2)` must escape this class. In particular it must exploit at least one genuinely non-Gaussian limiting mechanism, noncentral/linear effects that survive the limit, mesoscopic localization without a centered Gaussian reduction, extra spectral directions, or a finite-dimensional structure not captured by this Gaussian limit theorem.

This does **not** prove that the full universal target constant equals `3 sqrt(2)`, and it does not treat arbitrary noncentral Gaussian quadratic forms. The full conjecture remains OPEN.

## 5. Relation to the live correction and current upper-bound work

The live `QFORM-CROSSMINOR-ALONE-FALSE` correction concerns a rank-two cross-block implication. This report uses neither that implication nor any physical cross-minor criterion. It is compatible with the current rank-three cross-block Fourier theorem and the diffuse-rank-three upper bounds in the shared research archive.

The practical consequence for B17 stress testing is sharper than the previous partner conclusion: further searches for `C>3 sqrt(2)` should not spend effort on centered Gaussian CLT limits with arbitrary covariance/correlation. The next mathematically distinct witness search should target noncentral Gaussian limits, finite mesoscopic mixtures, or explicitly non-Gaussian stable/local-limit regimes while retaining the density-one coordinate constraint.

## 6. Status

- New proved theorem: exact `3 sqrt(2)` ceiling for every centered Gaussian rank-three indefinite limit with covariance floor `I/12` and spectral magnitudes at least one.
- Named partner applied: account02/B17 lower-bound witness, which attains equality and converts the upper ceiling into an exact mechanism-optimality theorem.
- Full QFORM conjecture: OPEN / NOT PROVED.
- No claim of global sharpness or novelty priority.
