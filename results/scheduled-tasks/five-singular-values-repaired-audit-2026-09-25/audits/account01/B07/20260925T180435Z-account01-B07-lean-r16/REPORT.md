# account01/B07 repaired-paper Lean audit r16

Objective: QFORM-FIVE-270-REPAIRED-AUDIT-20260925

Exact paper: yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa
paper.tex blob: 98e45d53d106db9a205051a4dd4917fc39dc2e3a
source SHA-256: 90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb
source length: 683 physical lines

Fresh AGENTS.md, CURRENT_OBJECTIVE.md, scheduled_tasks/README.md and the repaired audit package were read before work. The later owner order remains in force: verify the repaired paper in Lean, nothing else.

Own acknowledgement was written first and read back:
- commit 9558cf784b19b8d7e8df388e96b79361a34bf2ed
- blob ead4b7b57a74e1ab9835e2e0518bb184e793d3fd

B07 independent findings:

1. Lemma 2.7, L163-L173: PASS.
   FiveS2Minors.lean blob ca08ebcb54c2895a26fd599fc406f80bd3b4e66d supplies the principal-minor/spectral bridge, Gram-form Cauchy-Binet and determinant-square bridge. Its log blob a92dbb5e41697abf6784031190e87d6a7097ab26 ends EXIT 0 and prints only propext, Classical.choice and Quot.sound.
   FiveS2Gram.lean blob 360efa2362bc150e4d21666b9b5ba15f3cbcfdec supplies the projected Gram factorization; current repaired-source log blob 57a8b38bb3e08a046d871beaf7970c51cbbdb000 is the corresponding successful axiom log.

2. Crossing-volume identity, L243-L249: PASS.
   It is the direct specialization of the independently inspected compiled Lemma 2.7(a).

3. Lemma 4.2, L260-L269: PASS.
   B07 reopened the exact entropy_bound statement in FiveS4.lean. FiveS4_axioms.log blob 33ea507a1dfddad18e2c855cb3f4b230016f2f23 ends rc=0 and uses only the standard three axioms.

4. Theorem 4.1 greedy row promotion, L380-L386: PASS for the finite component.
   hub_selection, decay_const_ratio, decay_const_le and decay_const_identity were reopened. FiveS4Thm.lean blob 8c44a7e9e72f79400f57c4a76da0f4944eb86c83 packages the stopping/retained-mass/diffuse/constant argument. Its log blob afa1abf0df09c7a633bb4fd5764ca11f2c9bd5bb ends EXIT 0 and uses only the standard three axioms.

5. Full Theorem 4.1: GAP through Lemma 4.3.
   thm41_of_hub takes Lemma 4.3's bound as an explicit hypothesis.

New work on Lemma 4.3 Step 3, L345-L351:
- The B07 Holder WIP was checked statically against the exact project Mathlib revision 5e932f97.
- Exact APIs confirmed at that revision: ENNReal.lintegral_prod_norm_pow_le, ENNReal.prod_rpow_of_nonneg, ENNReal.mul_rpow_of_nonneg, Finset.prod_comm', and Finset.prod_le_prod_of_subset_of_le_one'.
- Added explicit dependent-product import.
- Added positive_weight_member_has_positive_marginal: w_T>0 and i in T imply alpha_i>0 from the marginal definition.
- Added positive_weight_set_subset_active: every positive-weight set lies in I'_+.
- The WIP now isolates zero-weight removal, inactive-factor removal using |psi_i|<=1, kappa reconstruction, marginal exponent reconstruction, dependent-product interchange, and finite weighted Holder.
- Local WIP: 392 lines, SHA-256 6d4a35f8f9641749586d1d2987dcc5d55f0bc5f0c1e9dd69e9e41c2fa228fce4, no sorry/admit/new axiom found.
- UNBUILT: no lean/lake executable is exposed in this runtime; no install or remote workflow was used.

Remaining load-bearing formal work for B07: instantiate Step 3 with the manuscript's actual kappa_epsilon and |psi_i| functions plus AEMeasurable obligations, then compile; formalize Lemma 4.3 Steps 1-2 (complex measure nu_x, total variation/density, L2 measurability/mollification, Plancherel/Cauchy-Schwarz, Jensen and dominated convergence).

No FALSE mathematical/formal clause was found. Rendered PDF remains UNCHECKED. Brain status WITHOUT_VERIFIED_BRAIN; full_brain_connected:false. Model GPT-5.6 Sol; effort UNKNOWN.
