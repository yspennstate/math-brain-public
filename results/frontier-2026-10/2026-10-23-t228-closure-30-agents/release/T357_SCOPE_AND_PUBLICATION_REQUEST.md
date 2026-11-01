# T357 scope assessment and public-repository request

Updated: 2026-10-24T01:43:50.679Z

## Assessment

The broad question of how overparameterization, training time, and early stopping affect population calibration is substantial enough for a serious curated list of 200 deep-learning theory problems. This is a judgment about the research question, not an independently established world ranking. The current proof is a specified Gaussian tanh random-feature theorem; it must not be described as a general solution of calibration for deep or feature-learning networks. Publication novelty and outside validation remain unconfirmed.

The completed theorem gives an exact finite-horizon ordinary-GD state evolution and score-conditional calibration for all fixed positive proportional ratios, a uniform positive calibration floor for arbitrary positive stopping times in an explicit bounded-MLE regime, and strict average overconfidence at the population-risk-optimal first-step scale. Near-boundary overconfidence does not mean overconfidence at every score: the same optimum is underconfident in the far tails.

## Current instruction and frontier

The owner requested that the work be saved in both Brains and that Claude agents make a public repository. The owner then instructed us to keep working until the full thing is solved. We are continuing beyond the completed regime theorem. Six GPT-6 max-effort workers are investigating late separable dynamics, uniform stopping, max-margin limits, and the exact boundaries of a broader theorem. No unproved extension is accepted yet.

Open extensions include late training outside the bounded-MLE regime, dimension-dependent step sizes, critical/intermediate proportional regimes, and learned features. The Gaussian random-feature model is the current concrete target; a universal theorem for arbitrary DNNs is not implied by it.

## Immutable source package

Math Brain: yspennstate/math-research-brain
- Commit b051fde9637a83edf725cd945e3f90aea3b1536a
- Prefix research_pushes/2026-10-23-t228-closure-30-agents/fullproof/

Brain: <private-repo>
- Commit 89e8c73de3ecd04f1f8b37165839e87b0356d982
- Prefix 06_math_research/frontier/worker_submissions/codex_20261023_t228_30agent/fullproof/

Files:
- T357_THEOREM_AND_SYNTHESIS.md SHA-256 7b773eba4446340893bd8e67a1397ba06b154bf79b9f89a348e68c1a93282d51
- T357_GAUSSIAN_COMPLETE_PROOF.md SHA-256 6e0331ef62b2a19218c914d7dc1cdf6034c151dbacf6f95214738f9eb173d3b3
- ACCEPTANCE.json, MANIFEST.json, T357_PRIMARY_SOURCE_COMPARISON.md
- Referenced proof modules, reviews, check_T357_finite_time.py and its saved results

## Claude release task

Create a new public research repository, suggested name t357-gaussian-calibration, containing only the T357 mathematical manuscript and relevant reproducibility code. Use a fresh repository history; do not fork or copy the private Brain history. Inspect and sanitize the current fullproof package instead of bulk-publishing the ZIP. Include only material needed for this result; exclude private coordination, unrelated research, account details, credentials, personal records, and private Brain links. Preserve accurate mathematical attribution and use only owner-approved licensing.

Present the result as a Gaussian random-feature regime theorem with clearly stated assumptions, internally reviewed and awaiting external verification. Include a visible open-frontier section and do not claim the broader DNN problem is solved. Existing T357 manuscript content is frozen; new proofs go into separately versioned extension files pending review.

Coordinate one responsible Claude release owner. Return the public URL, immutable public commit, published file manifest, reproduction commands and checks, and any real blocker. Continue broader mathematical collaboration without changing existing schedules, control files, or paid-compute settings. The owner has explicitly authorized this specific public repository; this is separate from any earlier request to publish the entire Math Brain.
