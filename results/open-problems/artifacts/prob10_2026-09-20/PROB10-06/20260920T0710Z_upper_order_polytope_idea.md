# PROB10-06 idea before code — upper-score order polytope

Runtime metadata available to this worker: model family GPT-5.6 Sol; reasoning effort is not authenticated by the scheduler and is therefore UNVERIFIED. GPT-6/maximum is not claimed.

Parent source remains the Lyons–Pemantle–Peres speed-monotonicity conjecture for a supercritical Galton–Watson tree without leaves, `P(nu=0)=0`, `m=E nu>1`. Child-bias `beta` gives each child weight `beta` relative to parent weight 1 and increases outward drift; parent-bias `lambda=1/beta` gives parent weight `lambda` relative to each child weight 1 and increases inward drift. The source asks whether the parent-bias speed `ell_lambda` is nonincreasing throughout `0<=lambda<m` (equivalently child-bias speed increases on `beta>1/m`).

Consumed own endpoint: `runs/prob10_2026-09-20/PROB10-06/20260920T0638Z_quantitative_branch_ratio_monotone_polytope_9c41e7b2.md` proves for `P(nu=2)=1-p, P(nu=3)=p`, every `p in [0,1]`, strict decrease through `lambda=1.85527`. Its lower `h_3/c_3` bound uses the exact monotone order polytope for conditional escape weights, but its upper `h_2/c_2` bound still discards those weights via reverse Chebyshev.

Three materially different attacks for this iteration:

1. **Upper-score order-polytope compression (primary).** For the three-branch term defining `h_2/c_2`, condition on exactly `m=0,1,2,3` type-3 branch roots. The conditional escape weights `Z_m=E phi(T_m)` are increasing in `m`, while the available upper score constants `R_m^U` are decreasing. Instead of reverse Chebyshev, retain the inherited exact interval envelopes `lo_m<=Z_m<=hi_m` and optimize the linear-fractional ratio
   `sum pi_m Z_m R_m^U / sum pi_m Z_m`
   over the monotone order polytope. As for the lower-score polytope, extrema occur at vertices. This should strictly lower the upper score for interior `p`, where the all-mixture certificate is tightest.

2. **p-dependent branch-ratio localization.** The previous bound `c_3/c_2 <= (4-lambda)/(2(3-lambda))` uses only the global pathwise lower escape `B>=(2-lambda)/2`. Try to replace this by a mixture-dependent lower bound on `B` or on the leave-one-out ratio using the probability of type-3 offspring. Any valid `p`-dependent upper bound on `t=c_3/c_2` shrinks the dangerous tilted interval for `theta=p t/(1-p+p t)`.

3. **Expectation-level derivative contraction near lambda=2.** The prior pathwise inverse-escape derivative contraction fails sharply because `lambda sum_i w_i^2=1` at a degree-two equal-child configuration when `lambda=2`. Test whether conditioning on a genuinely random `{2,3}` offspring law yields a strict expectation-level factor `<1` for `p>0`, using the type-3 mass and the inverse-escape moment bound. If the best bound still reaches 1, record the exact obstruction rather than forcing a sign claim.

No finite simulation will be treated as source progress. The primary computational task, if the first route survives algebraic falsification, will be an exact rational/Bernstein checker for a candidate enlarged all-mixture endpoint. Source status remains OPEN regardless of a restricted-family improvement.