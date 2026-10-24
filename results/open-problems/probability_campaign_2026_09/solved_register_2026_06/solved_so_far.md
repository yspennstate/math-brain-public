# Solved so far

Date: 2026-06-01

## Publishable / manuscript-level

1. Gaussian real phase-retrieval stability scale.
   - Result: `omega(A)=4^{-m+o_P(m)}` for real Gaussian `A in R^{(2m-1) x m}`.
   - Artifact: `~\phase_retrieval_omega\paper`.
   - Novelty/publishability: project-original; publishable theorem-paper result.

2. Dyson-index square-submatrix generalization.
   - Result: real/complex extremal square-submatrix least-singular-value exponent
     `-(1/beta) log(gamma^gamma/(gamma-1)^(gamma-1))`.
   - Artifact: included in the phase-retrieval/RMT manuscript.
   - Novelty/publishability: project-original strengthening; publishable with the main paper.

## Publishable supporting theorems

3. Fixed-apex overlap combinatorics.
   - Result: exact overlap identities and finite second-moment envelope estimates, Lean-supported.
   - Artifact: `OmegaComb.Basic`.
   - Novelty/publishability: supporting formal/combinatorial machinery, not standalone.

4. Deterministic row-Gram/order-statistic bridge.
   - Result: Lean formalization of selected-row Gram forms, min-over-subsets, sorted-prefix
     `k`-smallest identities, and lower-bound transfer.
   - Artifact: `OmegaComb.DeterministicWidth`.
   - Novelty/publishability: verified infrastructure for the deterministic Balan-Wang route.

5. Sign-free `K5` star-ratio relaxation.
   - Result: nonnegative `K5` edge weights satisfy
     `min_d min_j w_dj/sum_{k != d,j} w_dk <= 1/3`, sharp only at uniform weights.
   - Artifact: `notes/k5_signfree_star_ratio_2026_06_01.md`.
   - Novelty/publishability: useful barrier proposition, not standalone.

6. Exact real `Gr(2,5)` star-ratio theorem.
   - Result: sharp bound `(4-sqrt(5))/11`, attained by the dual regular pentagon.
   - Artifact: `notes/gr25_star_ratio_theorem_2026_06_01.md`.
   - Novelty/publishability: compact publishable base-case theorem for the deterministic Plucker route.

7. Exact real `Gr(2,n)` star-local Plucker theorem.
   - Result: sharp bound `alpha_n/(1-alpha_n)`, `alpha_n=(2/n)sin^2(pi/n)`, attained by the
     regular projective `n`-gon.
   - Artifact: `notes/gr2n_star_ratio_theorem_2026_06_01.md`.
   - Novelty/publishability: apparently project-new after a quick literature smoke check; publishable
     as a proposition in the deterministic Plucker/Balan-Wang note after a final citation pass.

8. Bounded-density one- and two-dimensional local CLT inputs for P1.
   - Result: bounded density plus RV-scale delocalization removes the temporary `phi_X in L^1`
     assumption in the pair local CLT.
   - Artifact: `notes/p1_pair_local_clt_bounded_density_upgrade_2026_06_01.md`.
   - Novelty/publishability: supporting proposition for non-Gaussian universality; full theorem still
     depends on random-matrix delocalization/correlation inputs.

9. P1 averaged-delocalization fixed-apex criterion.
   - Result: the all-subsets RV-scale delocalization target is stronger than needed and inaccessible by
     a union bound; the correct fixed-apex criterion is a large good family plus an averaged
     correlation kernel.
   - Artifact: `notes/p1_averaged_delocalization_reduction_2026_06_01.md`.
   - Novelty/publishability: proof-strategy proposition for the non-Gaussian universality route.

10. P1 random-subset exchangeability reduction.
   - Result: single-submatrix null-normal delocalization implies typical-good-family delocalization by
     exchangeability; random-pair kernel expectations control empirical fixed-apex kernel averages.
   - Artifact: `notes/p1_random_subset_reduction_2026_06_01.md`.
   - Novelty/publishability: supporting reduction that turns the P1 random-matrix burden into
     single-submatrix and random-pair estimates.

11. Top-top Plucker template scalar Lean lemma.
   - Result: Lean verifies the scalar numerator inequality behind the 3-term top-top packet pressure.
   - Artifact: `OmegaComb.PluckerTemplate`.
   - Novelty/publishability: proof infrastructure, not standalone.

12. Fixed-apex Poisson first-two-moment reduction.
   - Result: at the first-moment threshold, the fixed-apex count has
     `E Z_t -> lambda` and `E[Z_t(Z_t-1)] -> lambda^2`, with explicit
     regular-overlap and exponentially small high-overlap bookkeeping.
   - Artifact: `notes/fixed_apex_poisson_moments_2026_06_01.md` and
     `numerics/fixed_apex_poisson_moments.py`.
   - Novelty/publishability: apparently project-new subproblem solution;
     publishable as supporting Poisson-limit infrastructure, not the full
     exact subexponential law.

13. P2 subexponential threshold constants.
   - Result: the fixed-apex and all-apex distance proxy thresholds are
     `2 sqrt(2) pi lambda sqrt(m) 4^{-m}` and
     `sqrt(2) pi lambda 4^{-m}/sqrt(m)`, respectively, up to `1+O(1/m)`.
   - Artifact: `notes/subexponential_threshold_constants_2026_06_01.md` and
     `numerics/subexponential_thresholds.py`.
   - Novelty/publishability: project bookkeeping with sharp constants;
     publishable as supporting infrastructure for the P2 Poisson/swap-control
     route.

14. P1 conditional good-family second-moment reduction.
   - Result: a good fixed-apex family with the right one-slab asymptotic and
     averaged pair bound gives conditional success probability `1-o(1)`.
   - Artifact: `notes/p1_conditional_good_family_second_moment_2026_06_01.md`.
   - Novelty/publishability: project-new deterministic reduction; publishable
     as supporting infrastructure for non-Gaussian universality once the
     random-matrix good-family input is proved.

15. P1 single-normal delocalization and D-stratified pair target.
   - Result: for bounded-density subgaussian entries, Nguyen--Vu gives the
     required single-submatrix RV-scale null-normal delocalization after the
     exchangeability reduction; the remaining pair theorem has been sharpened
     to a conditional-overlap estimate
     `E[(1-rho_ST^2)^(-1/2) | D] <= 1+C/D+eta_m(D)` for `D>=3`, and then
     reduced further to a Gaussian-scale even-moment hierarchy
     `E[rho_ST^(2q)|D]=O_q(D^{-q})` plus a no-near-parallel tail estimate.
     The near-parallel edge now has deterministic slab, tail-to-kernel,
     least-squares/cap, Gaussian calibration, determinant-tilted density, and
     constant-audit reductions.
   - Artifact: `notes/p1_single_normal_delocalization_nguyen_vu_2026_06_01.md`,
     `notes/p1_overlap_stratified_kernel_2026_06_01.md`, and
     `notes/p1_kernel_moment_tail_reduction_2026_06_01.md`,
     `notes/p1_higher_angular_moments_2026_06_01.md`,
     `notes/p1_kernel_moment_ladder_2026_06_01.md`,
     `notes/p1_conditional_residual_line_model_2026_06_01.md`,
     `notes/p1_conditional_residual_covariance_2026_06_01.md`,
     `notes/p1_residual_near_parallel_tail_2026_06_01.md`,
     `notes/p1_near_parallel_beta_tail_2026_06_01.md`,
     `notes/p1_near_parallel_slab_reduction_2026_06_01.md`,
     `notes/p1_tail_to_kernel_edge_2026_06_01.md`,
     `notes/p1_cap_least_squares_reduction_2026_06_01.md`,
     `notes/p1_gaussian_least_squares_calibration_2026_06_01.md`,
     `notes/p1_least_squares_density_sufficient_condition_2026_06_01.md`,
     `notes/p1_least_squares_z_density_formula_2026_06_01.md`,
     `notes/p1_slab_constant_audit_2026_06_01.md`,
     `notes/p1_least_squares_density_probe_2026_06_01.md`,
     `notes/p1_sliced_row_determinant_factorization_2026_06_01.md`,
     `notes/p1_sliced_determinant_probe_2026_06_01.md`,
     `notes/p1_sliced_second_moment_bound_2026_06_01.md`,
     `notes/p1_sliced_covariance_determinant_bound_2026_06_01.md`,
     `notes/p1_sliced_density_frame_leverage_2026_06_01.md`,
     `notes/p1_frame_radius_window_2026_06_01.md`,
     `numerics/p1_overlap_stratified_kernel.py`,
     `numerics/p1_residual_line_model.py`, and
     `numerics/p1_residual_covariance_probe.py`,
     `numerics/p1_residual_tail_probe.py`,
     `numerics/p1_near_parallel_tail.py`,
     `numerics/p1_cap_least_squares.py`,
     `numerics/p1_slab_constant_audit.py`,
     `numerics/p1_least_squares_density_probe.py`,
     `numerics/p1_sliced_factor_constants.py`,
     `numerics/p1_sliced_determinant_probe.py`,
     `numerics/p1_frame_leverage_probe.py`,
     `numerics/p1_frame_radius_window.py`.
   - Novelty/publishability: supporting reduction and diagnostic evidence;
     publishable as proof infrastructure, not a standalone theorem.

## Still open

- Non-Gaussian bounded-density universal upper bound: local CLT side is clean, and the
  single-submatrix input is covered for bounded-density subgaussian entries; the main remaining input is
  rigorous conditional residual-line angular universality and a Haar-comparable anti-alignment/cap bound
  for overlapping null normals, now benchmarked by the exact Haar beta law for
  `1-rho^2` and reduced at the edge to slab/projection-density and
  determinant-aware least-squares density formulations.
- Deterministic Balan-Wang exponential conjecture: rank-two star-local model is solved, but the
  higher-rank Plucker imbalance theorem is still open.
- Exact subexponential law of the Gaussian minimum: first two fixed-apex Poisson factorial moments and
  threshold constants are solved; the full Chen-Stein/Poisson limit remains open.
- Complex phase retrieval at the true complex threshold.
