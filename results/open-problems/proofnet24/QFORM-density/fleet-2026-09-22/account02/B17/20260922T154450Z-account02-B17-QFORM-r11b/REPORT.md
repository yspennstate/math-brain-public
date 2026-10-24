# account02/B17 — infinitesimal fragmentation no-escape at the 3sqrt(2) ceiling

**Programme:** `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
**Run:** `20260922T154450Z-account02-B17-QFORM-r11b`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / GENERAL_INFINITESIMAL_BANK_LIMIT_NO_ESCAPE`  
**Full quadratic-form conjecture:** **OPEN / NOT PROVED**  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and source pins

The full target remains: for every dimension, every independent real input family with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal dimension-free essential-density bound for `X^T A X`, or give a valid target-level counterexample.

This run applies the completed designated-partner result account03/B17, `QFORM-RARE-FRAGMENT-CP-NOESCAPE-v1`, canonical report `yspennstate/math-open-problems@d6150b6de22e898de442e821e42c2ddc09604a0d`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260922T153529Z-account03-B17-QFORM-r11/REPORT.md`. That result proves that finite-intensity rare fragments converging to Gaussian plus compound-Poisson shifts cannot raise the limiting density ceiling above `3 sqrt(2)`.

Its Gaussian input is the completed theorem `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T120821Z-account01-B17-qform-sharp-constant-v1/ADDENDUM_NONCENTRAL_GAUSSIAN.md`: if `G~N(m,Sigma)` with `Sigma >= sigma^2 I` and `A` has at least three eigenvalues of modulus at least one, then `||p_{G^T A G}||_infinity <= 1/(2 sqrt(2) sigma^2)`.

The live correction inbox was consumed before this proof. No pointwise oscillatory decay, rotated-coordinate independence, fixed fragment-count reduction, conditional cap preservation, one-minor extraction, or cross-minor-only implication is used.

## 2. New lemma: cap-one inputs force a Gaussian variance floor in every infinitesimal diffuse array

Let `nu` be a finite subprobability measure on `R` of total mass `p` with Lebesgue density bounded by `M`. Define

`V(nu) = int x^2 dnu(x) - (int x dnu(x))^2`.

Then

`V(nu) >= p^3/(12 M^2)`.                                            (2.1)

Indeed, normalize `mu=nu/p`. Its density is at most `M/p`. The sharp one-dimensional variance floor for a probability density bounded by `L` is `Var(mu)>=1/(12L^2)`, attained by a uniform interval. Hence `p Var(mu)>=p^3/(12M^2)`, while

`V(nu)=p Var(mu)+p(1-p)(E_mu X)^2 >= p Var(mu)`.

Now consider an infinitesimal triangular array

`Z_{m,k}=a_{m,k} X_{m,k}-c_{m,k}`,

where the `X_{m,k}` are independent and have densities at most one, the deterministic coefficients satisfy

`sum_k a_{m,k}^2 = 1`,   `max_k |a_{m,k}| -> 0`,                    (2.2)

and the row sums `sum_k Z_{m,k}` converge in distribution. For fixed `eps>0`, put

`p_{m,k}(eps)=P(|Z_{m,k}|<=eps)`.

The density of `Z_{m,k}` is bounded by `1/|a_{m,k}|`. Applying (2.1) to its restriction to `[-eps,eps]` gives

`V_{m,k}(eps) >= a_{m,k}^2 p_{m,k}(eps)^3 / 12`.                    (2.3)

For an infinitesimal convergent triangular array, the Levy triangular-array theorem gives, at every continuity radius of the Levy measure,

`T_m(eps):=sum_k P(|Z_{m,k}|>eps)=O_eps(1)`.                         (2.4)

Since `(1-q)^3 >= 1-3q`, (2.2)--(2.4) imply

`sum_k a_{m,k}^2 p_{m,k}(eps)^3`
` >= 1 - 3 sum_k a_{m,k}^2 P(|Z_{m,k}|>eps)`
` >= 1 - 3 (max_k a_{m,k}^2) T_m(eps) -> 1`.                       (2.5)

Therefore

`liminf_m sum_k V_{m,k}(eps) >= 1/12`.                              (2.6)

The canonical small-jump covariance formula in the Levy-Khintchine triangular-array theorem identifies the limiting Gaussian variance as the `eps downarrow 0` limit of these truncated variance sums. Thus every limiting infinitely divisible law has Gaussian variance

`boxed(sigma^2 >= 1/12)`.                                            (2.7)

No moment, support-diameter, fragment-count, fragment-scale, symmetry, or identical-distribution assumption is used beyond the stated infinitesimal triangular-array convergence.

## 3. Main theorem: arbitrary infinitesimal fragmentation cannot beat 3sqrt(2) in disjoint banks

### Theorem `QFORM-INFINITESIMAL-BANK-NOESCAPE-v1`

For `j=1,2,3`, let

`Y_{j,m}=sum_k a_{j,m,k} X_{j,m,k}-b_{j,m}`

be three mutually independent rows of arrays satisfying the cap-one hypothesis, coefficient normalization and infinitesimality (2.2), and suppose `Y_{j,m} => Y_j`.

Then each `Y_j` admits a Levy-Khintchine decomposition

`Y_j = G_{0,j} + R_j`,                                               (3.1)

where the `G_{0,j}` are independent `N(0,1/12)` variables and the residual vector `R=(R_1,R_2,R_3)` is independent of `G_0` (it may contain additional Gaussian variance, arbitrary drift, and an arbitrary Levy jump part).

Consequently, for

`Q_infinity = Y_1^2 + Y_2^2 - Y_3^2`,                               (3.2)

there is a bounded continuous density satisfying

`||p_{Q_infinity}||_infinity <= 3 sqrt(2)`.                          (3.3)

### Proof

Section 2 gives a Gaussian component variance `sigma_j^2>=1/12` in every `Y_j`. Split its Gaussian component as `N(0,sigma_j^2)=G_{0,j}+H_j`, where `G_{0,j}~N(0,1/12)`, and absorb `H_j`, the Levy jump part and drift into `R_j`. Mutual independence of the three physical banks yields independent Levy limits and a realization with `G_0` independent of `R`.

Condition on `R=r`. Then `G_0+r ~ N(r,(1/12)I_3)`. Apply the completed noncentral Gaussian theorem to `A=diag(1,1,-1)` and `sigma^2=1/12`. Every conditional quadratic law has a bounded continuous density `p_r` with

`||p_r||_infinity <= 3 sqrt(2)`.                                    (3.4)

Averaging over `R` gives `p_{Q_infinity}(x)=E[p_R(x)] <= 3 sqrt(2)`. Continuity follows by dominated convergence from the same uniform bound. QED.

## 4. Sharpness and stress interpretation

The theorem is sharp as a limiting statement. Take every physical marginal `Unif[-1/2,1/2]`, take `m` equal coefficients `a_{m,k}=m^{-1/2}` in each bank, and use

`A_m=diag(J_m/m,J_m/m,-J_m/m)`.

Its nonzero spectrum is `{1,1,-1}` for every `m`. The normalized sums converge to independent `N(0,1/12)` variables, and the limiting mixed-sign quadratic density attains

`p(0)=3 sqrt(2)=4.242640687119285...`.

Thus the account03/B17 finite compound-Poisson theorem extends to **every convergent infinitesimal disjoint-bank triangular-array witness**, including divergent fragment alphabets and arbitrary infinite-activity Levy limits: the cap-one condition forces enough Gaussian smoothing to keep the macroscopic limiting peak at or below `3 sqrt(2)`.

## 5. Remaining escape mechanisms

The unrestricted QFORM conjecture remains OPEN. The theorem leaves three precise threats:

1. **non-infinitesimal / mixed leverage:** some physical coordinates retain macroscopic influence after projection;
2. **finite-row local spikes:** weak convergence alone does not control `sup_m ||p_{Q_m}||_infinity`; narrow spikes can disappear in the macroscopic limit;
3. **shared-coordinate frames:** one physical coordinate may load several active spectral directions, so the three independent-bank reduction fails.

Accordingly, the next sharp-witness attack should target a source-valid mixed-leverage/shared-coordinate construction above `3 sqrt(2)`, or prove a uniform local-limit upgrade for the infinitesimal branch. This theorem is a mechanism restriction, not a proof of the universal conjecture and not evidence that `3 sqrt(2)` is globally sharp.

## 6. Verification

`CHECK.py` verifies the sharp subprobability variance identity on interval extremizers, `(1-q)^3>=1-3q`, equal-weight rare-tail convergence of the lower bound to `1/12`, and the numerical value of `3sqrt(2)`. These checks support algebra only; the Levy triangular-array theorem is the analytic input.
