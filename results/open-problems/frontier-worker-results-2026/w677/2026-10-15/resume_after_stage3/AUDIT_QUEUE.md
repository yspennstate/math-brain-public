claim_id | version | proof_file | statement
S1_HJJ_known | 1 | proofs/S1_HJJ_known_v1.md | Verify prior-source statement, HJJ Theorem 1 and Conjecture 2; no novelty claim.
C1_uniform_obstruction | 1 | proofs/C1_uniform_obstruction_v1.md | All positive exponential weights fail for the specified 27-type T4 upper comparison; exact AM–GM certificate; does not classify T4.
C2_ternary_single_entry | 1 | proofs/C2_ternary_single_entry_v1.md | Candidate analytic E[V] <= 3 log((7+sqrt(17))/8) < 1 for the restricted single-entry ternary model; no original-model classification.
C2_ternary_single_entry | 2 | proofs/C2_ternary_single_entry_v2.md | Same analytic bound; supersedes v1 with finite-time agreement proof instead of cutoff monotonicity; corrected binary equation locator.
C3_activation_identity | 1 | proofs/C3_activation_identity_v1.md | Standard full-model first-moment identity; activation event independent of its own sleeping frog path; no novelty or summable tail claimed.
C2_ternary_single_entry | 3 | proofs/C2_ternary_single_entry_v3.md | Supersedes v2: sharpened exact mean <=3(3 sqrt(17)+5)/64<1 via finite-depth mean recursion; restricted model only.
C4_biased_bootstrap | 2 | proofs/C4_biased_bootstrap_v2.md | PRIORITY: candidate recurrence at original p=27/100 for all d>=3, exact interval bootstrap plus GTW/Mathews transfer; T127 itself remains open.
C2_ternary_single_entry | 4 | proofs/C2_ternary_single_entry_v4.md | Supersedes v1-v3: E[V]<=3/4 in restricted ternary model, exact five-iteration certificate plus finite-time limit argument.
C5_blocked_simple_walk | 1 | proofs/C5_blocked_simple_walk_v1.md | Fixed finite-block cap with ordinary walks is transient at every finite sleeper mean; exact absorption contraction, no original-model classification.
C4_biased_bootstrap | 3 | proofs/C4_biased_bootstrap_v3.md | PRIORITY, supersedes v2: candidate S_3<=133/500=0.266, 41,258 exact intervals, analytic tail, published GTW/Mathews transfer. Unbiased T127 open.
C6_three_step_obstruction | 1 | proofs/C6_three_step_obstruction_v1.md | All r>0 fail for specified 27-type three-step T4 matrix; exact positive Bernstein coefficients, no ordinary classification.

RECEIVED: C4_biased_bootstrap v3 PASS (correctness), AUDITS_FROM_REVIEWER.tsv; textual erratum saved. Current unaudited versions: C1 v1, C2 v4, C3 v1, C5 v1, C6 v1. Earlier C2/C4 versions are superseded.
C7_first_exit_comparison | 2 | proofs/C7_first_exit_comparison_v2.md | Exact finite exit PGFs and uniform 48-type matrix obstruction; no infinite-model classification.
C10_finite_start_bootstrap | 1 | proofs/C10_finite_start_bootstrap_v1.md | PRIORITY: candidate S_3<=53/200=0.265, exact 600-step grid starts g_20; analytic bootstrap only a>=20.
C11_finite_start_criterion | 1 | proofs/C11_finite_start_criterion_v1.md | Finite-start Poisson criterion with exact nonfinal-cell bounds and final convex-chord slope; elementary, novelty not asserted.
C10_finite_start_bootstrap | 2 | proofs/C10_finite_start_bootstrap_v2.md | PRIORITY, supersedes v1 parameter: S_3<=2649/10000=0.2649, 2000 exact grid steps to g_20 and analytic tail; all arithmetic/replay checks complete.
C10_finite_start_bootstrap | 3 | proofs/C10_finite_start_bootstrap_v3.md | PRIORITY: same p=0.2649 certificate as v2, corrects S_3=sup_{d>=3}p_d definition. v2 withdrawn for definition error; audit v3.
C12_self_similar_transience | 1 | proofs/C12_self_similar_transience_v1.md | PRIORITY after C10 v3: E[V]<1.41 in ternary self-similar model at p=0.2648; exact continuous polygon subsolution and finite-time cutoff argument.

C13_star_exit_obstruction | 1 | proofs/C13_star_exit_obstruction_v1.md | Specified 48-type T4 matrix has rho>1 at every positive spatial weight; no infinite-model claim.

C14_pair_cluster_obstruction | 1 | proofs/C14_pair_cluster_obstruction_v1.md | Two finite adjacent-pair maps cannot contract at r=27/10; original model unclassified.

C15_four_child_bootstrap | 1 | proofs/C15_four_child_bootstrap_v1.md | Recurrence at original p=19/80 for every d>=4, exact 1000-step finite start and analytic all-a>=20 bootstrap.

C16_four_child_transience | 1 | proofs/C16_four_child_transience_v1.md | Four-child restricted self-similar E[V]<0.99 at original p=0.2367; no ordinary transience or critical lower bound.

C17_three_site_comparison | 2 | proofs/C17_three_site_obstruction_v2.md | Specified4260-type uniform three-site map cannot contract at r=27/10; finite result only.

C19_fair_cluster_upper_coupling | 1 | proofs/C19_fair_cluster_upper_coupling_v1.md | Conditional ordinary transience from fair conservative cluster contraction; activation-closure and expected-weight proofs.

15Oct retarget: C10v3/C12v1 now PASS. Finite-cap T4/C19/C20 work is parked; please prioritize target1 simulations and any ensuing full lower-model proof. No audit of the unfinished C20 model is requested.

C25_joint_ordinary_excursions | 1 | proofs/C25_joint_ordinary_excursions_v1.md | MODEL/NUMERICS REVIEW ONLY: ordinary joint multi-entry sampler; no phase theorem.

C28_fixed_cap_sterile_barriers | 1 | proofs/C28_fixed_cap_sterile_barriers_v1.md | PRIORITY target1 route-failure: independent sterile barriers imply sup_h E R_h(k)<=(k+4^(K+1))/3 at p=1/4 for every fixed ordinary cap K; full T127 remains open.

C26_absorbing_extinction_floor | 1 | proofs/C26_absorbing_extinction_floor_v1.md | Target1 special: An absorbing-parent ordinary lower model started with one incoming frog and one resident has P(V=2)>=p^2 and E[s^V]>=p^2*s^2; positive limiting PGF alone does not exclude positive-probability infinite returns. Proof unaudited; no Lean formal-verification PASS.

C27_joint_response_queue | 1 | proofs/C27_joint_response_queue_v1.md | Target1 special: A persistent cumulative K-input child-response queue defines an exact finite-depth ordinary excursion lower comparison and is monotone in cumulative child laws; positive uniformly accessible tails would imply full recurrence, but that hypothesis is not established and C28 rules it out for every fixed K at p=1/4. Proof unaudited; no Lean formal-verification PASS.

C27 v1 WITHDRAWN/SUPERSEDED: review v2; clarification restricts the cited zero-one implication to ordinary p=1/4.
C27_joint_response_queue | 2 | proofs/C27_joint_response_queue_v2.md | Target1 special: exact cumulative response operator, monotonicity and lower coupling; ordinary recurrence criterion only at p=1/4. No phase conclusion and no Lean formal PASS.

C30_linear_truncated_mean_criterion | 1 | proofs/C30_linear_truncated_mean_criterion_v1.md | Target1 criterion: positive linear finite-height lower mean implies ordinary recurrence via an independent all-active envelope; no growth bound established.

C29_logarithmic_caps | 1 | proofs/C29_logarithmic_caps_v1.md | MODEL/NUMERICS ONLY: unequal input/child cap recursion and independent finite-tree checks; no phase claim.

C31_unequal_cap_response_operator | 1 | proofs/C31_unequal_cap_response_operator_v1.md | Unequal-cap finite RDE, cumulative monotonicity and original-path lower coupling; explicitly outside C29v1 audit.

C29_logarithmic_caps | 2 | proofs/C29_logarithmic_caps_v2.md | Numerical update:24 complete roots through H128; no inherited-error or phase bound; separate C31v1 PASS.

C32_forced_input_child_coverage | 1 | proofs/C32_forced_input_child_coverage_v1.md | Deterministic-input binomial child coverage; no actual input-delivery or recurrence claim.

C33_site_block_upper_comparison | 1 | proofs/C33_site_block_upper_comparison_v1.md | Retained-motion finite-site upper coupling, exact independent-range closure and potential criterion; no T4 contraction claim.

C34_copied_block_infinite_mean | 1 | proofs/C34_copied_block_infinite_mean_v1.md | Exact n=4 first-return witnesses close C33 five-/nine-site unbounded-entry copied upper comparisons for finite mean; no ordinary T4 result.
C36_inherited_range_obstruction | 1 | proofs/C36_inherited_range_obstruction_v1.md | Full unbounded ancestry-range memory without post-split sharing still has infinite expected root absorptions on T4; exact quartic certificate; no ordinary phase conclusion.

C37_shared_site_block_screen | 1 | C37_SHARED_BLOCK_NOTES.md | NUMERICAL EVIDENCE ONLY: review finite block model, mean estimators and reported limitations; not a proof or ordinary T4 result.
