# account03/B05 Lean r07

Target: repaired paper commit 4e530247ec0ef4101a6e5ecf621bd35a969c42aa, blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.

B05 continued Lean-only work on Lemma 3.2. Existing compiled FiveS3.lean already covers finite entropy, rpow, rescaling, and determinant steps. New WIP isolates the missing product-density marginal and orthogonal density transport, plus repaired zero-beta and p(y)=0 branches.

Status: UNCOMPILED WIP. No Lean/lake/elan is exposed; install and remote workflows are prohibited. No new theorem is claimed verified.

Fresh WIP theorem candidates: marginal_density_measurable, marginal_withDensity_fst, marginal_withDensity_fst_le, marginal_withDensity_fst_le_const, marginal_withDensity_fst_ac, map_withDensity_measurePreservingEquiv, map_withDensity_linearIsometryEquiv, zero_beta_row_of_dot, zero_beta_factor_independent, zero_beta_factor_le_one, zero_density_before_log.

Pinned Mathlib 5e932f97 was checked for the relevant APIs, including setLIntegral_prod, Measurable.lintegral_prod_right', withDensity_mono, MeasurePreserving.setLIntegral_comp_preimage, LinearIsometryEquiv.measurePreserving, and dotProduct_self_eq_zero.

Execution: WITHOUT_VERIFIED_BRAIN.
