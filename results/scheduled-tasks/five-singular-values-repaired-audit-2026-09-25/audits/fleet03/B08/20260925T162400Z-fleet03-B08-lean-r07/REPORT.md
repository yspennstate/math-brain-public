# fleet03/B08 Lean r07 — Lemma 4.3 Step 3 positive-support/Hölder bridge

SIGNED IN - formalizing the repaired five-singular-value paper in Lean, account fleet03, slot B08, 2026-09-25T16:24:00Z.

Fresh brain controls were read before mathematics. The 25 Sep 2026 12:29 owner message remains controlling: formalize and verify every result of the repaired five-singular-value paper in Lean only.

Exact paper: yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa, repaired-2026-09-25/paper.tex, blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a, SHA-256 90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb.

Current research main observed at c75954ae33a0d992a99f576e760ac2bff8c25786. Current LEAN_COVERAGE.md blob 76050ca34cfd051811d0d487855ef8bb1d095eb1 still lists Lemma 4.3 as partial: hub_constant, gram_orth_blocks and step5_log_identity are compiled; the Cauchy--Schwarz, Plancherel and generalized-Hölder steps are not formalized. No current repository result matching the B08 Step-3 theorem names was found.

This run targets repaired paper lines 345--351. The candidate Step3HolderCore_B08.lean isolates eight obligations:
- step3_positive_member_marginal;
- step3_coordinate_weights_sum_one;
- step3_drop_zero_marginals;
- step3_holder_of_ae_le;
- step3_kernel_weight_identity;
- step3_positive_support_sum_one;
- step3_positive_support_weight;
- step3_factor_aemeasurable.

The main advance over r06 is explicit treatment of the manuscript's positive determinant-weight support. step3_positive_support_sum_one proves that filtering a nonnegative probability vector by 0<w_T leaves total mass one, and step3_positive_support_weight exposes strict positivity of every retained Hölder weight. The common-kernel proof was rewritten with an explicit stronger finite-set induction so it does not rely on implicit generalization of the nonnegativity hypothesis. The zero-marginal product inequality was changed to the current ENNReal-specific Finset.prod_le_prod_of_subset_of_le_one interface.

Checked Mathlib interfaces: ENNReal.lintegral_prod_norm_pow_le, lintegral_mono_ae, ENNReal.rpow_add_of_nonneg, Finset.aemeasurable_prod, AEMeasurable.pow_const, Finset.prod_le_prod_of_subset_of_le_one, and Finset.sum_subset. These checks reduce signature risk but are not compilation evidence.

The remaining substantive Step-3 bridge is the finite incidence-product regrouping
prod_T (prod_{i in T} |psi_i|^(1/alpha_i))^(w_T) = prod_{i in I'_+} |psi_i|,
with T on positive determinant support. The intended Lean route is a finite product over incidences (T,i), ENNReal.rpow_mul, and collapse of the exponent at each coordinate using step3_coordinate_weights_sum_one. After that, step3_kernel_weight_identity, step3_factor_aemeasurable and step3_holder_of_ae_le supply the line 349--351 Hölder transition.

Verification status: this runtime exposes neither lean nor lake, including usual elan/opt locations. No installation or remote workflow was attempted or permitted. Therefore none of the eight r07 candidates receives formal credit. The candidate contains no sorry, admit or new axiom and includes #print axioms for every theorem, but those commands have not executed. Formal credit remains only with the central compiled files named in LEAN_COVERAGE.md.

Native receiver status: WITHOUT_VERIFIED_BRAIN. Unexposed model/effort: UNKNOWN.
