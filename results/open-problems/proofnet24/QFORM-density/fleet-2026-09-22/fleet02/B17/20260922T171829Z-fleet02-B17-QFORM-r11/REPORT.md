# fleet02/B17 — shared-coordinate infinitesimal closure and one-heavy eigenaxis no-escape

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T171829Z-fleet02-B17-QFORM-r11`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `PROVED_SUPPORTING_LEMMAS / EXACT_STRESS_FAMILIES`  
**Full quadratic-form conjecture:** **OPEN / NOT PROVED**  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication and source status

The previous fleet02/B17 run produced two facts that must be kept simultaneously:

1. the normalized 4x4 Hadamard source refutes a universal pointwise conditional active-3D density cap;
2. a six-variable shared-frame source has exact peak `4.063070616806...`, above the designated partner's finite rotated witness but below `3 sqrt(2)`.

The remaining witness question was therefore not another conditional-cap estimate. It was whether **shared-coordinate loading itself** can escape the `3 sqrt(2)` diffuse ceiling once the physical rows are genuinely mixed, and, after that, whether a first macroscopic row can do so.

This report closes two source-valid subbranches:

* every convergent **infinitesimal shared-coordinate Parseval frame** has at least the universal Gaussian covariance floor `I/12` in its infinitely-divisible limit, hence its fixed-rank quadratic limit has density at most `3 sqrt(2)`;
* replacing one diffuse Gaussian row-direction by one arbitrary cap-one macroscopic physical input **along an eigendirection** cannot increase the zero-level saddle peak above `3 sqrt(2)`.

Neither statement controls arbitrary finite-row spikes, two or more interacting macroscopic rows, a macroscopic row mixing positive and negative eigenspaces, or off-center levels. Therefore neither proves the full conjecture.

## 2. Completed partner result actually used

The designated partner fleet03/B17 completed `QFORM-DISJOINT-THREE-BANK-2PI-v1`, canonical report

`yspennstate/math-open-problems@d53ca1d541b2b2dbf861ec39fda699209b267158`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260922T160432Z-fleet03-B17-QFORM-r12/REPORT.md`.

It proves `||p_Q||_infinity <= 2 pi` for three active spectral vectors on pairwise disjoint physical supports and gives the exact rotated six-variable stress `91/36+(13/6)log 2 = 4.02959666899...`. Its explicit next implication is to leave disjoint-bank geometry and test shared-coordinate active frames.

The present run follows that implication. In the stress family of Section 5 every physical row loads all three active directions, so the partner's disjoint-bank independence theorem is deliberately unavailable. The new limit argument replaces bank independence by an exact Gaussian-covariance floor.

For the final conditional quadratic step I also use the completed theorem `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1`, source path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260922T120821Z-fleet01-B17-qform-sharp-constant-v1/ADDENDUM_NONCENTRAL_GAUSSIAN.md`.

It says that if `G~N(m,Sigma)`, `Sigma >= sigma^2 I`, and `A` has at least three eigenvalues of magnitude at least one, then `||p_{G^T A G}||_infinity <= 1/(2 sqrt(2) sigma^2)`, uniformly in the mean and extra spectral directions.

## 3. Sharp subprobability variance lemma

### Lemma 3.1

Let `nu` be a finite measure on `R` with total mass `p in [0,1]` and density bounded by `M`. Then

`int x^2 dnu(x) - (int x dnu(x))^2 >= p^3/(12 M^2)`.

### Proof

If `p=0` there is nothing to prove. Normalize `mu=nu/p`. Its density is bounded by `M/p`. Every probability density bounded by `L` has variance at least `1/(12L^2)`; the extremizer is the uniform density on an interval of length `1/L`. Hence

`Var_mu >= p^2/(12M^2)`.

Writing `m=int x dmu`,

`int x^2 dnu - (int x dnu)^2 = p Var_mu + p(1-p)m^2 >= p Var_mu >= p^3/(12M^2)`.

QED.

## 4. Shared-coordinate infinitesimal covariance floor

### Theorem `QFORM-SHARED-INFINITESIMAL-COVFLOOR-v1`

Fix `r`. For every `m`, let `a_{m,k} in R^r` be deterministic row vectors and let `X_{m,k}` be independent real random variables with probability densities bounded by one. Assume

`sum_k a_{m,k} a_{m,k}^T -> G`

for a fixed positive semidefinite matrix `G`, and

`max_k ||a_{m,k}|| -> 0`.

After arbitrary deterministic rowwise centering, suppose the vector triangular array `Z_{m,k}=a_{m,k} X_{m,k}-c_{m,k}` is infinitesimal and its row sum converges in law to an infinitely divisible random vector `Y`. Let `Sigma_Gauss` be the Gaussian covariance matrix in the Levy--Khintchine decomposition of `Y`. Then

`Sigma_Gauss >= G/12`

in Loewner order.

In particular, for a Parseval spectral frame, `G=I_r`, every such limit contains an independent Gaussian component `N(0,I_r/12)`.

### Proof

Fix `theta in R^r` and project the triangular array onto `theta`. Put `b_{m,k}=theta^T a_{m,k}`. Then

`sum_k b_{m,k}^2 -> theta^T G theta`

and `max_k |b_{m,k}| ->0`. The projected array is infinitesimal and converges to `theta^T Y`.

Fix `epsilon>0`. Let `F_{m,k}` be the law of the projected summand and let `p_{m,k}=F_{m,k}([-epsilon,epsilon])`. When `b_{m,k} !=0`, the density of the projected summand is at most `1/|b_{m,k}|`, independently of its deterministic translation. Apply Lemma 3.1 to the restriction of `F_{m,k}` to `[-epsilon,epsilon]`:

`int_{|x|<=epsilon} x^2 dF_{m,k} - (int_{|x|<=epsilon} x dF_{m,k})^2 >= b_{m,k}^2 p_{m,k}^3/12`.

Terms with `b_{m,k}=0` contribute zero to the right side. Since the array is infinitesimal,

`q_m(epsilon):=max_k [1-p_{m,k}] ->0`.

Therefore

`sum_k b_{m,k}^2 p_{m,k}^3 >= (1-q_m(epsilon))^3 sum_k b_{m,k}^2 -> theta^T G theta`.

The canonical triangular-array formula for the Gaussian variance of the infinitely divisible scalar limit is obtained by taking the limit of these truncated centered second moments and then `epsilon downarrow0`. Hence

`theta^T Sigma_Gauss theta >= (theta^T G theta)/12`.

This holds for every `theta`, proving `Sigma_Gauss >= G/12`. QED.

### Corollary 4.2 — fixed-rank quadratic limit ceiling

Assume `G=I_r` and let `Lambda` be a fixed real symmetric `r x r` matrix with at least three eigenvalues of magnitude at least one. Then the limiting quadratic variable

`Q_infinity = Y^T Lambda Y`

has a bounded continuous density with

`||p_{Q_infinity}||_infinity <= 3 sqrt(2)`.

Indeed the Levy--Khintchine decomposition and the matrix inequality above permit `Y = Z + R` with `Z~N(0,I_r/12)` independent of `R`. Conditional on `R=r`, apply the completed noncentral-Gaussian theorem with `sigma^2=1/12`; then average the conditional densities.

This statement is about the **limiting law**. It does not assert `limsup ||p_{Q_m}||_infinity <= 3 sqrt(2)`: weak convergence alone does not control prelimit `L^infinity` spikes.

## 5. Exact fully shared Parseval stress attaining the limiting ceiling

Let `N=4m`. Use the four sign patterns

`p1=(1,1,1)`, `p2=(1,-1,1)`, `p3=(1,1,-1)`, `p4=(1,-1,-1)`,

each repeated exactly `m` times, and let every physical row of `U_N` equal its pattern divided by `sqrt(N)`.

The exact integer identity

`sum_{a=1}^4 p_a p_a^T = 4 I_3`

gives `U_N^T U_N = I_3`. Every physical row has leverage exactly `||u_i||^2 = 3/N ->0`, and every physical coordinate loads **all three** active spectral directions.

Take iid `X_i~Uniform[-1/2,1/2]`, put `Y_N=U_N^T X` and

`A_N=U_N diag(1,1,-1) U_N^T`.

Then `A_N` has exact nonzero spectrum `{1,1,-1}` for every `N`. By the multivariate Lindeberg CLT,

`Y_N => N(0,I_3/12)`,

so

`X^T A_N X => Z_1^2+Z_2^2-Z_3^2`, `Z_j iid N(0,1/12)`.

At zero the limiting density is exactly `3 sqrt(2)`. To see the constant directly, `Z_1^2+Z_2^2` is exponential with rate `6`, while `Z_3^2` has the scaled chi-square-one density. Their convolution at zero equals `1/(2 sqrt(2) sigma^2)` with `sigma^2=1/12`, hence `3sqrt(2)`.

Thus the covariance-floor theorem is sharp even under fully shared physical loading. This source does not improve the known universal lower bound; it proves that shared loading by itself does not invalidate the sharp diffuse endpoint.

## 6. A one-heavy-row Laplace domination theorem

The previous B17 memory identified the next credible escape as one or more macroscopic rows plus diffuse residual. The first aligned endpoint can also be closed exactly.

### Lemma `QFORM-ONE-HEAVY-LAPLACE-DOMINATION-v1`

Let `0<=ell<=1`. Let `H` be any real random variable with probability density at most one, and let

`G_ell ~ N(0,(1-ell)/12)`

be independent of `H`. Define

`Y_ell = sqrt(ell) H + G_ell`.

Then for every `c>0`,

`E exp(-c Y_ell^2) <= (1+c/6)^(-1/2)`.

The right side is exactly `E exp(-c Z^2)` for `Z~N(0,1/12)`.

### Proof

Set `d=1+c(1-ell)/6`. Conditioning on `H=x` and integrating the Gaussian gives

`E[exp(-cY_ell^2)|H=x] = d^(-1/2) exp[-(c ell/d)x^2]`.

The integrand is symmetric decreasing in `|x|`. Among all probability densities bounded by one, the bathtub principle therefore maximizes its integral at `H~Uniform[-1/2,1/2]`. Put

`alpha = c ell/(4d)`.

It remains to prove

`I(alpha):=int_0^1 exp(-alpha u^2) du <= (1+2alpha/3)^(-1/2)`.  (6.1)

This elementary inequality is sharp at `alpha=0`. Let

`J(alpha)=int_0^1 u^2 exp(-alpha u^2) du`.

Integration by parts gives `I-2alpha J=e^{-alpha}`. Also

`I = e^{-alpha} int_0^1 exp(alpha(1-u^2)) du >= e^{-alpha}[1+alpha int_0^1(1-u^2)du] = e^{-alpha}(1+2alpha/3)`.

Therefore `J/I >= 1/(3+2alpha)`. Consequently

`d/dalpha log I = -J/I <= -1/(3+2alpha) = d/dalpha log[(1+2alpha/3)^(-1/2)]`.

Both sides equal one at `alpha=0`, proving (6.1). Finally,

`d^(-1/2)(1+2alpha/3)^(-1/2) = [d+c ell/6]^(-1/2) = (1+c/6)^(-1/2)`.

QED.

## 7. Exact consequence: one macroscopic eigendirection cannot beat the saddle endpoint

Consider the mixed-sign three-mode limit with coefficients `(1,1,-1)` and a single macroscopic physical input placed along an eigendirection, while the remaining Parseval mass in that direction and the other two directions is supplied by diffuse cap-one uniform rows.

### Minority-sign heavy row

Let `Y_1,Y_2 iid N(0,1/12)` and let `Y_3=Y_ell` from Lemma 6. Then `S=Y_1^2+Y_2^2` is exponential of rate `6`, so

`p_{S-Y_3^2}(0)=6 E exp(-6Y_3^2) <= 6/sqrt(2) = 3sqrt(2)`.

This covers **arbitrary cap-one law** for the macroscopic physical input and every `ell in [0,1]`.

For the extremal centered interval one can write the exact formula

`p(0)= 6/sqrt(2-ell) int_0^1 exp[-3ell u^2/(2(2-ell))] du`,

which is decreasing from `3sqrt(2)` at `ell=0`.

### Same-sign heavy row

By rotational symmetry inside the positive eigenspace, take the heavy direction to be the first positive eigendirection. Let `Y_1=Y_ell`, while `Y_2,Y_3 iid N(0,1/12)`. The difference

`D=Y_2^2-Y_3^2`

has density

`p_D(x)=(6/pi) K_0(6|x|)`.

Using the positive integral representation

`K_0(z)=int_0^infinity exp(-z cosh s) ds`

and Tonelli,

`p_{Y_1^2+D}(0) = (6/pi) int_0^infinity E exp[-6 cosh(s) Y_1^2] ds`.

Apply Lemma 6 pointwise in `c=6 cosh s`. The result is no larger than the same integral with `Y_1` replaced by `N(0,1/12)`, which is exactly the centered Gaussian saddle value `3sqrt(2)`.

Therefore a single macroscopic cap-one row **aligned with either eigenspace** cannot improve the `3sqrt(2)` zero-level lower bound when the complementary frame is diffuse Gaussian in the limit.

This is a limiting stress theorem, not a finite-dimensional density bound and not an off-center theorem.

## 8. What remains after this run

The witness search is now sharper.

* Pairwise disjoint active banks: finite-dimensional `2pi` bound from fleet03/B17.
* Fully shared but infinitesimal Parseval frames: every infinitely-divisible fixed-rank limit retains Gaussian covariance at least `I/12`, so the quadratic limit is bounded by `3sqrt(2)`.
* One macroscopic cap-one row aligned with an eigenspace plus diffuse complement: its zero-level limiting peak is also at most `3sqrt(2)`.

A witness above `3sqrt(2)`, if one exists, must therefore use at least one mechanism not covered here: a macroscopic row mixing the positive and negative eigenspaces, two or more interacting macroscopic rows, a genuinely finite-row spike not reflected in the weak limit, an off-center level, growing active rank, or additional spectral components coupled to the physical heavy rows.

For proof synthesis, Theorem 4 gives a useful quantitative dichotomy target: if an infinitesimal grouped-coordinate subarray carries Gram `G >= kappa I` and converges separately, it supplies a Gaussian core of covariance at least `kappa I/12`, hence a conditional quadratic density bound `3sqrt(2)/kappa`. The remaining grouped-coordinate reduction only has to handle the complementary branch in which macroscopic rows consume a nontrivial fraction of the active spectral Gram. That is exactly where current heavy-coordinate/rank-two affine tools should be spent.

The unrestricted product-law quadratic-form conjecture remains **OPEN / NOT PROVED**.

## 9. Verification scope

The accompanying checker verifies exactly:

* the four-pattern Gram identity and Parseval normalization;
* row leverage `3/N`;
* the nonzero target spectrum `{1,1,-1}`;
* the constant `3sqrt(2)`;
* numerical sanity of the sharp integral inequality (6.1) on a wide deterministic grid and of the one-heavy exact formulas.

The checker is not the proof of Lemma 3.1, Theorem 4, or Lemma 6; those are analytic arguments above.

## 10. Corrections and provenance

Consumed live corrections include the standing pointwise-decay, fiber-supremum, rotated-independence, conditional-cap, conditional-independence, local-cross-rank and fiberwise-trace warnings, together with the preceding B17 event `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1`. No refuted intermediate is used.

No correction to the full target is asserted in this run. No claim is made that weak convergence controls prelimit `L^infinity`, and no arbitrary rotated coordinate is treated as independent.
