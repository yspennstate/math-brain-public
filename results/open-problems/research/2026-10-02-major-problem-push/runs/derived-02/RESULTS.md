# General-service queueing extension and strict-comparison corollaries

2 October 2026. These results strengthen the earlier finite-phase counterexamples. Historical priority and definitive present open status of Whitt's assertion remain unverified. They do not settle FEI, the full forest conjecture, Sidorenko, K-theory, or Whitt's weaker mean waiting-time statement.

## General coefficient theorem

The standalone proof `whitt_general_service_light_traffic_proof.md` derives the first service-sensitive coefficient of the stationary delay probability for every c>=2 and every strictly positive service law with finite second moment. Discrete, continuous and mixed laws are allowed. The proof compares the waiting queue with the insensitive loss queue using a regenerative Poisson potential. Fixed-time stationary Dynkin, a linear workload bound, and an integrable single-server busy-period dominator justify the unbounded potential and the rate-zero limit. A Stieltjes integration-by-parts calculation verifies the loss product-residual stationary law. The remainder is little-o; no general analyticity claim is made.

Both independent reviewers checked the proof. Their full reports are archived, including the reasoning behind the moment hypotheses and localization.

## General positive decreasing-hazard counterexamples

For any strictly positive law with finite continuous nonconstant decreasing hazard bounded below by a positive constant, and for every fixed c>=2, the coefficient theorem yields a counterexample with an explicitly specified strictly positive two-exponential comparator. The comparator has the same mean, strictly larger stop-loss transform at every positive service threshold, and strictly smaller stationary probability of waiting at all sufficiently small positive arrival rates.

The explicit epsilon is given in `whitt_general_DFR_positive_comparator.md`. Its two-region argument proves the service-law comparison globally, including arbitrarily small and arbitrarily large thresholds. The symmetric odds inequality bounds the comparator's coefficient excess by one quarter of the base excess. This removes the analytic gap recorded in the earlier exploratory `whitt_general_DFR_route.md`; that old file remains an immutable record of the earlier state.

The theorem includes decreasing-hazard laws outside finite exponential mixtures, such as a continuous hazard that decreases linearly and then becomes constant. The general small-rate interval is existential. The earlier nine-state and strictly positive certificates provide explicit finite-rate instances independently.

## Strict comparison at zero as well

The existing finite-rate equal-mean H2 certificate already defeats the strict-stop-loss strengthening suggested after Whitt's equation(2.5) for every positive threshold. A further explicit scaling by10001/10000 gives a comparator with strictly larger mean and strict increasing-convex domination at every nonnegative threshold, including zero.

The fresh exact rational certificate `whitt_strict_mean_increase_exact.py` verifies a delay-probability gap greater than12/5000 at lambda=11/10, with two servers, and a waiting-tail reversal greater than23/10000 at the positive waiting threshold1/100000. Its full proof, model-bound output and independent audit are archived. The scaled comparison law remains a mixture of two strictly positive exponentials. This statement concerns stochastic waiting-time order; it does not address the weaker mean waiting-time conjecture.

## Status and sources

The original mathematical assertion is Whitt(1983), Conjecture1.1, "Comparison conjectures about the M/G/s queue", Operations Research Letters2,203-209, https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf . Its Section2 notes the inconclusive leading light-traffic comparison at equal means and waiting threshold zero, and suggests a strict stop-loss strengthening in equation(2.6). The derived counterexamples address both statements.

Bounded searches of the original title, delay probability plus convex-order comparisons, higher light-traffic coefficients, and multiserver counterexamples did not establish definitive historical priority. Whitt's separate 1984 GI/G/1 counterexamples have non-Poisson arrivals and do not by themselves resolve this M/G/c assertion. An original paper from1983 and absence of a located earlier disproof do not certify that an assertion is still open in2026. Subsequent work must keep priority unverified until a sufficient primary-source review is completed.

The more famous FEI and full forest negative-correlation targets are being pursued separately. New subsidiary theorems on those targets must be presented with their full hypotheses, proof and independent audit, rather than as solutions of the full conjectures.
