# C0044 review packet — w581

## Source status

The historical target is Drewitz and Ramírez, *Selected Topics in Random Walks in Random Environment*, arXiv:1309.2589v1, Open Question 3.2 (PDF page 42). Its (E) means strictly positive nearest-neighbor transition probabilities almost surely; (IID) means independent identically distributed site rows. It asks whether the annealed probability of escape in each fixed direction is zero or one. The restriction d >= 3 selects the historically open dimensions.

The public September 23, 2026 manuscript *A directional zero–one law under strict ellipticity* claims to prove exactly this target, and the OpenAI math scope page says it is formalized. The linked public `ComparatorChallenges/DirectionalWalk.lean` contains the matching theorem statement but ends the proof with `by sorry`. That comparator statement is not a proof receipt. The manuscript is saved as `public_directional_zero_one_2026.pdf` (SHA-256 `245e917113b3545b311c4c9eab739227d530f527081c1b0be4a92ea904559683`); its proof still needs mathematical and formal artifact review. Current independent solution status: **UNKNOWN / new claimed solution requires audit**.

## w580 verdicts

Three KEEP verdicts are recorded in `VERDICTS.jsonl`, with algebra and conditional-expectation reproductions. The hardest checked step is the invariant-density zero-set argument plus the harmonic-energy identity in C0044-w580-003. The result is conditional on a stationary Q absolutely continuous with respect to the environment law. That existence is the unresolved parent gap. None of these KEEPs is a C0044 solution verdict.

## w581 contribution awaiting independent referee

`ATTEMPT.md` and `CLAIMS.jsonl` give the all-start positivity lemma and the resulting product-ergodic zero-one law for *existence of positive quenched escape probability*. w584 should audit these two lemmas before any store theorem promotion. The remaining gap is exclusion of mixed values 0 < q_omega(x) < 1.

NEXT: Inspect w579's completed exact claims, check its hardest step, then determine whether the new manuscript's proof claim warrants a corrected problem-status row.
