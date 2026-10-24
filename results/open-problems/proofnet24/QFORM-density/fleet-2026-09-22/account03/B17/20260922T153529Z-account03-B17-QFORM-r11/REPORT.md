# account03/B17 — rare-fragment compound-Poisson no-escape theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T153529Z-account03-B17-QFORM-r11`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / MESOSCOPIC_FRAGMENT_NO_ESCAPE`  
**Full quadratic-form conjecture:** **OPEN / NOT PROVED**  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and why this branch matters

The target remains: for every dimension, every independent real input family with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal dimension-free essential-density bound for the quadratic form, or produce a valid counterexample.

Earlier B17 work proved the exact variance floor and stability inequality for density-cap-one marginals. It left one sharp-witness escape route explicitly open: fragmentation energy may become asymptotically negligible in the three active frame directions while the projected law remains genuinely non-Gaussian/mesoscopic. The present run attacks precisely that route.

The designated account04/B17 partner still has no completed QFORM handoff or canonical report visible at the fresh partner scan, so no account04/B17 theorem is invented here. I apply two completed compatible results instead:

1. **account04/B14 extreme-product reduction**, `yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`: for every interval event, the exact product-law optimum is attained in the closure of marginals `1_E`, `|E|=1`, with compact finite unions of intervals sufficient and no loss in constant.
2. **account01/B17 noncentral Gaussian ceiling**, theorem `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1`, source `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T120821Z-account01-B17-qform-sharp-constant-v1/ADDENDUM_NONCENTRAL_GAUSSIAN.md`: if `G~N(m,Sigma)`, `Sigma >= sigma^2 I`, and the quadratic matrix has at least three eigenvalues of magnitude at least one, then its quadratic output has a bounded continuous density with norm at most `1/(2 sqrt(2) sigma^2)`. At `sigma^2=1/12`, the sharp ceiling is `3 sqrt(2)`.

The current correction set is respected: no pointwise van-der-Corput envelope, no rotated-coordinate independence, no single-minor extraction, no conditional-density-cap substitution, and no bounded-fragment-count reduction is used.

## 2. Exact source-valid fragmented stress family

Fix, for each bank `j=1,2,3`, a finite symmetric jump specification

`nu_j = sum_{ell=1}^{L_j} (alpha_{j,ell}/2)(delta_{a_{j,ell}}+delta_{-a_{j,ell}})`,

where `alpha_{j,ell}>0`, `a_{j,ell}>0`, and let

`alpha_j = sum_ell alpha_{j,ell}`.

For every sufficiently large integer `m>alpha_j`, define a measurable set `E_{j,m}` of total Lebesgue measure exactly one as follows:

- a central interval centered at zero of length `1-alpha_j/m`;
- for every `ell`, two tail intervals centered at `+a_{j,ell} sqrt(m)` and `-a_{j,ell} sqrt(m)`, each of length `alpha_{j,ell}/(2m)`.

For large `m` the pieces are pairwise disjoint. Let every physical coordinate in bank `j` have density

`f_{j,m}=1_{E_{j,m}}`.

These are exact admissible input laws: `0<=f<=1`, `int f=1`, compact support for each fixed `m`, and finite interval unions. They lie exactly in the extreme-product class supplied by account04/B14.

Take three independent banks, each of size `m`, and write

`Y_{j,m}=m^{-1/2} sum_{k=1}^m X_{j,k}`.

Define

`Q_m = Y_{1,m}^2 + Y_{2,m}^2 - Y_{3,m}^2`.

Equivalently, the physical `3m x 3m` quadratic matrix is

`A_m = diag(J_m/m, J_m/m, -J_m/m)`.

Its nonzero spectrum is exactly

`{+1,+1,-1}`

for every `m`; hence every member of the sequence satisfies the exact three-large-eigenvalue hypothesis.

## 3. Exact one-step characteristic function

For one bank, suppress `j`. Let `alpha=sum alpha_ell`. The characteristic function of `X_m/sqrt(m)` is exactly

`psi_m(t)`
` = (1-alpha/m) sinc( t(1-alpha/m)/(2 sqrt(m)) )`
`   + sum_ell (alpha_ell/m) cos(a_ell t)`
`       * sinc( t alpha_ell/(4 m^(3/2)) )`,

where `sinc(u)=sin(u)/u` and `sinc(0)=1`.

For every fixed `t`, Taylor expansion gives

`psi_m(t)`
` = 1 + m^{-1}[ -t^2/24 + sum_ell alpha_ell(cos(a_ell t)-1) ]`
`   + O_t(m^{-2})`.

Therefore

`psi_m(t)^m -> exp( -t^2/24 + sum_ell alpha_ell(cos(a_ell t)-1) )`.      (3.1)

The right side is the characteristic function of

`Y = G + S`,

where `G~N(0,1/12)` and `S` is an independent symmetric compound-Poisson variable with Levy measure `nu`. Thus, by Levy continuity,

`Y_{j,m} => G_j + S_j`,

jointly for the three independent banks, with the three limits independent.

By the continuous mapping theorem,

`Q_m => Q_infinity := (G_1+S_1)^2 + (G_2+S_2)^2 - (G_3+S_3)^2`.        (3.2)

This is a genuinely mesoscopic non-Gaussian limit whenever at least one `nu_j` is nonzero: the rare physical fragments occur with probability `Theta(1/m)` per coordinate, but their locations are `Theta(sqrt(m))`, so each surviving event produces an `O(1)` jump after block normalization.

## 4. Main theorem: compound-Poisson fragmentation cannot raise the limiting sharp constant

### Theorem `QFORM-RARE-FRAGMENT-CP-NOESCAPE-v1`

For every finite symmetric jump specification above, the limiting random variable `Q_infinity` has a bounded continuous density and

`||p_{Q_infinity}||_infinity <= 3 sqrt(2)`.                           (4.1)

Moreover, allowing the zero jump measure shows that the supremum of the limiting density norm over this whole rare-fragment family is exactly `3 sqrt(2)`.

### Proof

Condition on the compound-Poisson vector

`S=(S_1,S_2,S_3)=s`.

Then

`G+s ~ N(s, (1/12) I_3)`.

The quadratic matrix on the three projected coordinates is exactly

`J=diag(1,1,-1)`,

whose three eigenvalues have magnitude one. Apply the completed noncentral Gaussian theorem with `sigma^2=1/12`. Conditional on every `s`,

`Q_infinity | (S=s)`

has a bounded continuous density `p_s` satisfying

`||p_s||_infinity <= 3 sqrt(2)`.                                      (4.2)

Now average over the compound-Poisson law:

`p_{Q_infinity}(x)=E[p_S(x)]`.

Hence pointwise

`p_{Q_infinity}(x) <= E[3 sqrt(2)] = 3 sqrt(2)`,

proving the essential-supremum bound. Continuity follows from dominated convergence: every `p_s` is continuous and the family is uniformly dominated by `3 sqrt(2)`.

If all jump intensities vanish, `S=0` and the centered Gaussian mixed-sign case attains the sharp value `3 sqrt(2)`. Therefore the supremum over the class, including the zero-jump endpoint, is exactly `3 sqrt(2)`. QED.

## 5. Why this genuinely escapes the previous variance-rigidity theorem

In the symmetric construction, each physical marginal has mean zero and its mass outside the centered unit interval is exactly

`delta_{j,m}=alpha_j/m`.

For the block frame, every physical row in bank `j` is `e_j/sqrt(m)`. Therefore the previous fragmentation-energy matrix is exactly

`M_delta,m`
` = diag(alpha_1^2/m^2, alpha_2^2/m^2, alpha_3^2/m^2)`,

so

`eta_m=lambda_min(M_delta,m)=min_j alpha_j^2/m^2 -> 0`.                (5.1)

Thus this family lies precisely in the `eta -> 0` escape regime not excluded by the earlier covariance-stability theorem. Nevertheless, the new compound-Poisson disintegration proves that this entire finite-intensity `sqrt(m)` rare-fragment mechanism still cannot raise the limiting sharp constant above `3 sqrt(2)`.

This is the target-relevant mathematical advance of the run.

## 6. General compensated finite-jump extension

The symmetry assumption is not essential. Let finite jump data be `(alpha_ell,b_ell)` with total intensity `alpha` and `B=sum alpha_ell b_ell`. Make the central interval have length `1-alpha/m` and center

`c_m = -B/[sqrt(m)(1-alpha/m)]`,

and place a tail interval of length `alpha_ell/m` at `b_ell sqrt(m)`. Then the physical marginal has mean exactly zero. Its normalized block sum converges to

`G + S_comp`,

where `G~N(0,1/12)` and `S_comp` is the compensated compound-Poisson law with exponent

`sum_ell alpha_ell ( exp(i b_ell t)-1-i b_ell t )`.

Conditioning on the resulting shift vector and applying the same noncentral Gaussian theorem again gives the same bound `3 sqrt(2)` for the limiting quadratic density. Thus the no-escape theorem holds for arbitrary finite jump measures, not just symmetric ones.

## 7. Exact connection to the account04 extreme-product theorem

Account04/B14 says that, for any fixed small-ball interval, the global product-density extremum reduces without constant loss to indicator densities of measurable measure-one sets, and compact finite unions are dense for the same optimum. The present construction is not an artificial smooth subclass: every marginal is itself one of those exact extreme finite-union densities.

The new implication is therefore concrete: **one entire source-valid extreme-product mesoscopic branch is now closed at the sharp lower-bound ceiling.** Finite-intensity fragments whose mass is `Theta(1/m)` and displacement is `Theta(sqrt(m))` survive aggregation as compound-Poisson jumps, but conditional Gaussian smoothing prevents them from increasing the limiting density norm above `3 sqrt(2)`.

## 8. What this does not prove

The unrestricted QFORM conjecture remains OPEN.

The theorem is a limiting witness exclusion, not a uniform finite-`m` bound for every `Q_m`. Weak convergence alone does not exclude a sequence of ever-narrower finite-`m` density spikes invisible at fixed macroscopic scale. The theorem also does not cover:

- fragment intensities diverging with `m`;
- jump locations at scales different from `sqrt(m)`;
- several mesoscopic scales interacting simultaneously;
- non-block frames in which one physical coordinate loads several active directions;
- arbitrary full matrices with extra spectral directions;
- or heavy-tailed laws without this finite-jump triangular-array structure.

Thus the next sharp-witness attack should change mechanism: either prove a local-limit upgrade that rules out hidden finite-`m` spikes for this branch, or move to multi-scale fragmentation / shared-coordinate mesoscopic frames. Repeating ordinary Gaussian or fixed-period Edgeworth perturbations would be redundant.

Continuity is proved here only for the limiting compound-Poisson/Gaussian quadratic law, not for the full target.
