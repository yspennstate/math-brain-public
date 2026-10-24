# account03/B17 — sharp variance rigidity forces interval-like diffuse witnesses

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T130502Z-account03-B17-QFORM-r12`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / SHARP_WITNESS_RIGIDITY`  
**Full quadratic-form conjecture:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and dependencies

The exact target remains: for independent real coordinates with densities bounded by one and every real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a universal dimension-free essential-density bound for `X^T A X`, or give a valid counterexample.

This run does **not** assume that the original inputs have moments as part of the target. The new variance lemma is an exact structural statement: when the variance is finite it yields a quantitative penalty, and when the variance is infinite the inequality is trivially true in the extended sense. Its Gaussian-limit consequence applies only to witness mechanisms that actually converge in covariance/local law to a Gaussian. It is therefore a witness-side exclusion theorem, not a proof of the full conjecture.

Fresh corrections used include the failure of law-uniform pointwise quadratic Fourier decay, dimension loss of naive fiber suprema, failure of single-minor/Schur extraction as a universal closure, and the newer warning that arbitrary finite-fragment extreme sets cannot be replaced by bounded-diameter or single-interval supports.

The requested partner `account04/B17` still had no completed QFORM artifact visible at the prepublication check. I therefore did not fabricate one. I applied two compatible completed results:

1. `account04/B14`, `QFORM extreme-product reduction`: for every interval event, the full product-density extremum reduces with no constant loss to marginals `f_i=1_{E_i}`, `|E_i|=1`, and further to compact finite unions by total variation. Source path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`.
2. `account01/B17`, `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1`: if `G~N(m,Sigma)`, `Sigma >= sigma^2 I`, and `A` has at least three eigenvalues of absolute value at least one, then
   `||p_{G^T A G}||_infinity <= 1/(2 sqrt(2) sigma^2)`, sharply. At `sigma^2=1/12` this is `3 sqrt(2)`.

The already-proved target lower bound `C >= 3 sqrt(2)` is used only as context for sharpness.

## 2. Sharp one-dimensional variance stability

### Theorem `QFORM-DENSITYCAP-VARIANCE-RIGIDITY-v1`

Let `X` have probability density `f` satisfying `0 <= f <= 1`. Let `mu=E X` when the first moment exists, and write

`I_mu=[mu-1/2,mu+1/2]`.

If `Var X < infinity`, define

`delta = int_{I_mu^c} f(x) dx`.

Because `|I_mu|=1` and `int f=1`, this also equals

`delta = int_{I_mu} (1-f(x)) dx = (1/2)||f-1_{I_mu}||_1`.

Then

`Var X >= 1/12 + delta^2/2`.                                            (2.1)

The coefficient `1/2` is sharp for every `0<=delta<=1`. In particular

`Var X = 1/12`

forces `delta=0`, hence `f=1_{I_mu}` almost everywhere. Thus a density cap of one has a rigid variance floor: the centered unit interval is the unique equality law up to translation.

### Proof

Translate so that `mu=0`. Then

`Var X - 1/12`
`= int_{|x|>1/2} x^2 f(x) dx - int_{|x|<=1/2} x^2(1-f(x)) dx`.          (2.2)

Both the outside mass and the missing inside mass equal `delta`. Under the pointwise capacity bound one, the outside second moment is minimized by placing mass in the closest available outside strips, so the bathtub principle gives

`int_{|x|>1/2} x^2 f(x) dx`
`>= 2 int_{1/2}^{1/2+delta/2} x^2 dx`
`= ((1+delta)^3-1)/12`.                                                (2.3)

Likewise the missing inside second moment is maximized by deleting mass from the boundary strips of the unit interval:

`int_{|x|<=1/2} x^2(1-f(x)) dx`
`<= 2 int_{1/2-delta/2}^{1/2} x^2 dx`
`= (1-(1-delta)^3)/12`.                                               (2.4)

Subtracting (2.4) from (2.3),

`Var X - 1/12`
`>= ((1+delta)^3+(1-delta)^3-2)/12`
`= delta^2/2`,

which proves (2.1).

Sharpness is attained for every `delta` by the symmetric measure-one set

`E_delta = [-1/2-delta/2,-1/2]`
`          union [-1/2+delta/2,1/2-delta/2]`
`          union [1/2,1/2+delta/2]`,

with density `1_{E_delta}`. It has mean zero, outside mass `delta`, and both bathtub inequalities are equalities. QED.

If the variance is infinite, the extended inequality `Var X >= 1/12+delta^2/2` is automatic whenever the mean/centering is interpreted through a finite first moment; no finite-variance conclusion is inferred for arbitrary target inputs.

## 3. Rank-three frame covariance penalty

Let `R` be an `n x 3` matrix with orthonormal columns and rows `r_i^T`, so

`sum_i r_i r_i^T = I_3`.

For independent coordinates with finite variances define `delta_i` by the preceding theorem and set

`Y = R^T(X-E X)`,
`Sigma = Cov(Y)`,
`M_delta = sum_i delta_i^2 r_i r_i^T`,
`eta = lambda_min(M_delta)`.

Independence and (2.1) give the Loewner inequality

`Sigma = sum_i Var(X_i) r_i r_i^T`
`>= (1/12) I_3 + (1/2) M_delta`
`>= (1/12 + eta/2) I_3`.                                               (3.1)

This is exact at the level of the one-dimensional variance penalty. It says that non-intervality is harmless to the covariance floor only if its weighted frame energy fails to span all three spectral directions.

## 4. Applying the completed Gaussian sharp-ceiling theorem

Apply the completed `account01/B17` theorem to any Gaussian comparison/limit having covariance `Sigma` from (3.1). For every target matrix with at least three eigenvalues of absolute value at least one,

`||p_{G^T A G}||_infinity`
`<= 1/[2 sqrt(2)(1/12+eta/2)]`
`= 3 sqrt(2)/(1+6 eta)`.                                               (4.1)

Therefore a Gaussian/local-limit witness can attain the known lower-bound ceiling `3 sqrt(2)` only if `eta -> 0`. Any fixed positive full-rank amount of density-cap non-intervality creates a quantitative strict gap.

This is stronger than merely observing the universal variance floor `1/12`: it gives an explicit stability modulus in the exact frame directions used by the quadratic form.

## 5. Applying the completed account04 extreme-product reduction

The `account04/B14` reduction says the full interval-small-ball supremum may be sought, with no constant loss, among extreme marginals

`f_i=1_{E_i}`, `|E_i|=1`,

including arbitrary compact finite unions. This remains compatible with the newer correction forbidding bounded-diameter localization: no diameter or connectedness restriction is used here.

For such an extreme marginal, let `mu_i` be its mean when finite and `I_i=[mu_i-1/2,mu_i+1/2]`. Then

`delta_i = |E_i\I_i| = (1/2)|E_i triangle I_i|`.

Thus (3.1) becomes

`Sigma >= (1/12)I_3 + (1/8) sum_i |E_i triangle I_i|^2 r_i r_i^T`.       (5.1)

Define

`eta_E = lambda_min(sum_i |E_i triangle I_i|^2 r_i r_i^T)`.

Every Gaussian comparison/limit of this exact extremal class therefore satisfies

`||p_{G^T A G}||_infinity <= 3 sqrt(2)/(1+(3/2)eta_E)`.                 (5.2)

This is the target-relevant partner implication: the full QFORM problem reduces to arbitrary fragmented measure-one sets, but within any Gaussianizing witness sequence, fragmentation that has nonvanishing full-rank energy across the three active frame directions can only **decrease** the sharp Gaussian peak away from `3 sqrt(2)`.

## 6. Consequence for the sharp-constant search

The combination of (5.2) with the known lower bound `C>=3 sqrt(2)` rules out a broad witness mechanism.

A valid target witness with limiting density peak strictly above `3 sqrt(2)` cannot be obtained from an extreme-product sequence whose relevant three-dimensional projection Gaussianizes while `eta_E` stays bounded below. Any such stronger witness must instead exploit at least one of:

- asymptotically rank-deficient fragmentation energy (`eta_E -> 0`), even if individual marginals are highly fragmented;
- a genuinely non-Gaussian mesoscopic/local limit;
- finite-dimensional effects not captured by Gaussian comparison;
- or another coupling mechanism outside this covariance-controlled witness route.

This complements the existing fixed-periodic Edgeworth result, which approaches `3 sqrt(2)` from below, by identifying a quantitative law-side rigidity condition rather than another frame-specific expansion.

## 7. What remains unpaid

The full arbitrary-law conjecture remains OPEN. The new lemma does not turn covariance control into a density bound for the original product law, and target inputs may have no finite moments. The first essential sharp-witness question is now whether an extreme fragmented sequence with `eta_E -> 0` can nevertheless use non-Gaussian/mesoscopic structure to exceed `3 sqrt(2)` while the quadratic form still has three large eigenvalues.

A distinct next attack should construct or exclude such rank-deficient fragmentation witnesses directly, rather than repeat Gaussian CLT or single-minor arguments.

No claim of continuity is made for the full target. The completed Gaussian comparison theorem supplies continuity only within its Gaussian scope.
