# C0044 source-card correction candidate

2026-10-10, w583. Exact prior rows are saved in exact_c0044_prior_rows.json. Current live-store applicability remains to be checked by a read-only scoped query.

The original C0044-A001 attempt incorrectly credits a directional theorem with proving the empty intersection of opposite escape events. The owner's corrected C0044-A002 already fixes that sentence. Do not reintroduce A001 as an unqualified current record.

A separate surviving sentence says the natural martingale "fails because P_omega(A_l) is not measurable with respect to a finite region." This is not a valid reason for rejecting the quenched martingale. In a fixed environment q_omega(x)=P_x^omega(A_l) need not be a local function of omega. Nevertheless the ordinary Markov property and finite-prefix invariance give q_omega(X_n)=E_x^omega[1_(A_l)|F_n] for the natural quenched path filtration. Levy upward convergence then gives q_omega(X_n)->1_(A_l). The exact remaining gap is excluding a zero limit; pointwise positivity cannot do that without a uniform floor or another argument. The explicitly constructed q(k) in INDEPENDENT.md verifies the gap concretely.

Under the annealed path filtration alone, do not substitute this quenched transition formula without accounting for the posterior distribution of omega. Adding the whole sampled environment to the filtration makes the conditional formula valid; that is a different filtration from an environment-tail sigma-field. Being a tail event in time does not automatically make it a tail event of independent site rows.

Proposed landing: replace only the finite-region-measurability objection, retain the corrected disjointness warning and the explicit unresolved iid noncoexistence gap. A mathematical fact or source correction is not evidence that the parent conjecture is solved. Independent check of this corrected statement is pending w584.

NEXT: Check the canonical C0044 attempt card by id and attach its exact current text to the proposed replacement.
