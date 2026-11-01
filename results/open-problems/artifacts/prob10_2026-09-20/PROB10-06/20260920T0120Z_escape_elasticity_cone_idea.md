Model actually ran: GPT-5.6 Sol; reasoning level UNVERIFIED. Requested GPT-6 maximum is prompt-only in this runtime and is not claimed.

# PROB10-06 idea before code — bootstrap the logarithmic escape derivative

## Continuity / current baseline consumed

Parent problem: Lyons–Pemantle–Peres speed monotonicity for a supercritical Galton–Watson tree without leaves, `P(nu=0)=0`, in parent-bias `lambda`; child-bias is `beta=1/lambda`. Larger `lambda` is more rootward and the source conjecture asks for nonincreasing speed on `0<=lambda<E nu`; larger `beta` is more outward and reverses the monotonic direction.

This run consumes rather than duplicates:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0013Z_two_point_escape_derivative_bridge_4f6c2e91.md`: exact `{2,3}` cancellation, all mixture weights through about `1.811`;
- `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0104Z__adjacent-two-point-weight-optimization.md`: exact tilted-weight optimization, all `{2,3}` mixtures through the analytic threshold `Lambda_2=1.8402833144...` (clean endpoint `46/25`), and the adjacent `{d,d+1}` criterion;
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T00-31-00Z__rare-defect-escape-envelope.md`: rare-defect `{2,3}` mixtures through `lambda=19/10`;
- `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T00-58-12Z__run-report.md`: broad bounded-support covariance route;
- `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T010909Z__sharp-regeneration-bound-and-score-response.md`: corrected regeneration route and its remaining moment debt.

I do not claim any of those as new here.

## New route A — an invariant cone for `-B'/B`

For the infinite-tree escape probability at a vertex,

`B = S/(lambda+S)`, `S=sum_{j=1}^nu B_j`.

Write `U=-B'` and `q=U/B`. Differentiating the exact recursion gives

`q = (1 + lambda * sum_j B_j q_j / S)/(lambda+S)`.

If offspring is bounded by `D` and `lambda<d<=nu<=D`, the standard escape bound `B_j<=1-lambda/D` gives `lambda+S<=D`. Starting only from `q_j>=0`, this recursion bootstraps the deterministic lower bounds

`q >= m_1=1/D`,
`q >= m_{r+1}=(1+lambda m_r)/D`,

and hence, after letting `r->infinity`,

`q >= 1/(D-lambda)`.

For adjacent support `{d,d+1}` this becomes

`-B'/B >= 1/(d+1-lambda)`.

This is strictly stronger than the previous lower input `-B'/B>=0` used in the lower bound for the `(d+1)` branch. It is also exact on the deterministic `(d+1)`-regular tree.

## New route B — feed the cone into the current exact tilted-weight criterion

The inherited upper branch bound is

`h_d/c_d <= (d-1)/((d-lambda)(d-lambda/d))`.

The cone gives, for the lower branch,

`B+(lambda-1)U >= B * d/(d+1-lambda)`.

Together with `D_{d+1}<=d+1-lambda/(d+1)`, this should improve the previous lower ratio to

`h_{d+1}/c_{d+1} >= d(d+1)/((d+1-lambda)((d+1)^2-lambda))`.

Therefore replace the previous adjacent log-sensitivity budget by

`a_d^sharp(lambda) = (d-1)/((d-lambda)(d-lambda/d)) - d(d+1)/((d+1-lambda)((d+1)^2-lambda))`.

The exact tilted-weight optimization already proved by P03-A then gives strict monotonicity whenever

`lambda a_d^sharp(lambda) < K_d`,
`K_d=2d+1+2 sqrt(d(d+1))`.

For `d=2`, this is

`a_2^sharp = 2/((2-lambda)(4-lambda)) - 6/((3-lambda)(9-lambda))`.

Pre-code calculation predicts the all-mixture threshold moves from `1.840283...` to about `1.8473465`; a clean target is `lambda<=1847/1000`.

## Route C tested and expected obstruction — improve the pointwise upper elasticity

A symmetric attempt would replace the inherited `-B'/B<=1/(d-lambda)` by a smaller pointwise bound. This cannot work uniformly over all adjacent mixture weights: the endpoint law `p=0` is the deterministic `d`-regular tree and has equality `-B'/B=1/(d-lambda)`. Thus any further all-`p` improvement beyond the cone theorem must couple the singular binary-branch upper elasticity with the vanishing mixture factor, or use expectation-level information; a purely pointwise upper envelope is exhausted.

## Route D tested — repaired regeneration bridge

P03-B's current corrected coupling condition depends on the conditioned one-dimensional ratio

`P_tilde(B>=1)/E_tilde[B(4B+1)]`.

Near the present analytic boundary (`beta=1/lambda` about `0.54`) the source/campaign material consumed in this run gives no certified lower bound on that ratio strong enough to compare with the explicit right side. The sharp deterministic inequality `tau<=4B+1` goes in the wrong direction for this missing moment estimate. I therefore do not manufacture a coupling sign from it in this run. The exact remaining coupling debt is an upper bound on the conditioned second backstep moment at weak outward bias.

The finite checker, if the algebra above survives review, will only verify rational endpoint/root-isolation arithmetic and the monotonicity polynomial; the theorem proof itself stays on the page.