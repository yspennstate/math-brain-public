/-
Prints the axioms each theorem depends on. Every theorem should depend only on
`propext`, `Classical.choice` and `Quot.sound` (the standard axioms of Mathlib);
none may depend on `sorryAx`.
-/
import CoverTime.CliqueStar
import CoverTime.DecoratedCore

open CoverTime.CliqueStar CoverTime.DecoratedCore

#print axioms target_leaf
#print axioms target_leaf_from_leaf
#print axioms target_centre
#print axioms target_gateway
#print axioms target_clique
#print axioms comparison_polynomial
#print axioms comparison_positive
#print axioms table_max
#print axioms excursion_transform
#print axioms geometric_parameters
#print axioms mean_random_sum
#print axioms variance_random_sum
#print axioms num_one
#print axioms den_one
#print axioms hasDerivAt_num
#print axioms hasDerivAt_den
#print axioms hasDerivAt_transform
#print axioms taylor_certificate
#print axioms variance_from_transform
#print axioms mgf_step
#print axioms mgf_series_bound
#print axioms stage_marginals
#print axioms stage_moments
#print axioms stage_third_moment
#print axioms stage_third_moment_bound
#print axioms d_identity
#print axioms c_identity
#print axioms leaf_departure_mean
#print axioms clock_mean
#print axioms trap_clock_variance
#print axioms leaf_departure_variance
#print axioms trap_leaf_covariance
#print axioms clock_variance
#print axioms cube_sum_bound
#print axioms centred_cube_bound
#print axioms initial_variance_clique
#print axioms clique_cover_tail
#print axioms moderate_deviation_scaling
#print axioms interpolation_exponent
#print axioms harmonic_bounds
#print axioms mean_expansion
#print axioms variance_coefficient_expansions
#print axioms sum_mulVec_eq_zero
#print axioms perturbation_coefficients
#print axioms two_vertex_eigenvalue
#print axioms threshold_upper_tail
#print axioms threshold_lower_tail
#print axioms leaf_elimination
#print axioms leaf_elimination_target
#print axioms dirichlet_linearity
#print axioms pendant_value
#print axioms double_star_hitting
#print axioms double_star_max
#print axioms double_star_from_formula
#print axioms path3_core_hitting
#print axioms two_vertex_pseudoinverse
#print axioms two_vertex_G
#print axioms two_vertex_G_moments
#print axioms harmonic2_le
#print axioms star_hitting
#print axioms star_variance_bound
#print axioms double_star_constants
#print axioms geometric_mean_ratio
#print axioms holding_time_variance
