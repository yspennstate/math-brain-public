# Hostile audit of the second attempt — 12 October 2026

## Exact conditional transition

The reduction is for mean-n exponential *edge weights with shortest-path NUV*, from a fixed or independent start. A start chosen after inspecting the graph would spoil the initial product-law conditioning; the transition theorem does not cover that case. The deterministic covering/moment bounds do cover every start.

The internal metric used in the cut minimum is the metric of the visited induced graph. It is not silently replaced by the full-graph metric between visited vertices. The first-unvisited-prefix proof shows why this cut minimum nevertheless selects precisely the same next target as the full NUV rule.

Conditioning on a zero-probability winning time is justified by the explicitly stated joint density. Losing edges have separate lower truncations, with the same row threshold for every still-unvisited label. Revealing the winner's other old-vertex edges does not reveal any edge to the remaining unvisited vertices. This is the crucial independence check. Conditional on T, winning rows are uniform only over active rows, not over all visited vertices.

The transition state grows in size and changes its remaining fraction k/n at every step. It is not a fixed-state-space stationary Markov chain. No ergodic theorem or density-dependent fluid theorem is invoked without proof of its hypotheses.

## Metric and height identities

The one-vertex metric closure accounts for all possible new shortcuts. Its expression for b_z+b_z' might concatenate a walk with repeated vertices, but loop removal and the zero-or-one occurrence of the new vertex give both required distance inequalities.

The maximum of two 1-Lipschitz height functions stays 1-Lipschitz. New incident edge weights are at least the updated endpoint heights. This prevents new shortcuts from invalidating the old height differences. Lean checks these two real-order algebra steps in `ThresholdUpdate.lean`; it does not formalize the entire stochastic transition.

The cone formula uses *current* visited distances, even if an old distance has shortened. Its reverse inequality follows from the preserved Lipschitz heights, so old cones cannot raise a height beyond the actual updated height. Recovering the discovery prefix from the current visited metric uses the fact that each original winning prefix already lay in this visited set, and that restriction cannot shorten any full-graph distance. The argument does not recompute shorter-prefix induced metrics or assume all old pairwise distances stay fixed.

## Moment and martingale reduction

FPP ball growth rates are j(n-j)/n. For the expected covering bound the ball is compared **from below** with a rate-1/2 Yule process, stopped at floor(n/2); for the earlier first-attempt resampling bound it was compared from above with a rate-one Yule process. These opposite directions serve different inequalities and are not interchangeable.

For a fixed outside root, ball labels conditional on size are uniform by symmetry. The chosen centers are fixed labels, not adaptive centers selected from that ball. The rounding ceil(n exp(-r/4)) and the case s=n are handled separately. The cap satisfies floor(n/2)-1>=n/4 for n>=8.

The covering number stays at least one at arbitrarily large r; integrating it to infinity would diverge. All integrals are stopped at diameter/2, and their tail is bounded by a covering number times a diameter power. The root exploration supplies the second, fourth and all required even diameter moments explicitly, so no unproved diameter concentration is needed.

The factor in the square layer-cake identity is 8r, not 4r. The moment proof uses N(b)^2<=nN(b) and Cauchy–Schwarz, rather than falsely assuming independence between diameter and covering number. In the p-th moment extension p is fixed independently of n.

The untruncated martingale differences are square-integrable by the finite-n diameter moments. Their variance sum bounds the error from the *random* drift A_n. It does not prove Var(A_n)->0. Bounded second moments alone would not imply L2 convergence to a probability limit; the explicit fourth-moment result supplies the needed uniform integrability of squared errors. The exact missing assertions are convergence of E A_n and vanishing Var(A_n).

## Checks actually performed

`deferred_checks.json`: 250 fully presampled graphs of size 25, giving 6,000 transitions. Each transition checked its next target/time against ordinary all-pairs shortest-path NUV, its cut lower thresholds, internal metric update, and Lipschitz height constraints. All deterministic checks passed. The transformed innovations had mean 1.00619, Exp(1) KS statistic 0.00849 (p=0.776), and adjacent correlation -0.000389; these are diagnostic evidence, not a substitute for the product-density proof. Direct and deferred length samples at n=12,40,80 did not reveal a discrepancy (two-sample KS p-values 0.894,0.702,0.120); these modest sample sizes do not certify equality in law.

The exact n=3 expectation 15/4 was compared with 5,000 deferred samples: mean 3.75538, standard error 0.03824. Its proof is the explicit two-activation calculation, not the Monte Carlo result. The asymptotic 1/12 error of a zero-threshold reset is a second-step calculation; it is not extrapolated to a bulk constant discrepancy.

The initial generic quadrature hit subdivision/roundoff warnings, although the maximum error was below its 1e-5 tolerance. A separate independent quadrature with activation breakpoints resolved the issue: 100 cases, maximum error 2.16e-13 against the analytic piecewise integral. These results are preserved in `deferred_followup.json`.

The follow-up checked 1,140 visited states for the exact cone identity, reconstructed NUV prefix and unchanged old step distances; all passed. Another 300 fixed-center covering-count cases passed. Drift samples at n=40,100,200 were recorded, including sample variances. The drift's observed standard deviation was not monotone (only ten samples at n=200), so no drift concentration or limiting constant is inferred.

Lean's first run failed because a variable was named the reserved word `by`; the failure log is preserved. Renaming it yielded an exit-zero run in 180.61 seconds. Both threshold-update and shortcut-height lemmas were accepted with kernel-checked tactic proofs, no sorry/native_decide, and narrow imports.

## Outcome

The second attempt provides an exact finite mean-field process, a history-cone characterization, stronger integrability than source tightness, and an L2 reduction of the NUV LLN to its predictable drift. It does not prove convergence or identify a constant in any of the three intended models. Novelty of these reductions is not certified. The previously established heavy-tail grid obstruction and lower bounds are unchanged.
