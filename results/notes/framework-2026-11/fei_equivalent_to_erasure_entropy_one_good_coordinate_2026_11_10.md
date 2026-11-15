---
name: fei_equivalent_to_erasure_entropy_one_good_coordinate_2026_11_10
description: "FEI equivalent local form? Yes: FEI <=> sum_i H(1[i in U] | U minus i) <= C I (erasure entropy of the spectral sample) <=> every Boolean g has ONE coordinate with H(1[i in U]|U-i) <= C Inf_i; exact decision-tree path formula; checked on all n<=5. PRIOR WORK (found 10 Nov 17:3x): the split D_i = E_i + J_i, J <= 4 Inf and the sufficiency (one good coordinate at every node => FEI) are in Gonzalez-MacManus-Pereyra arXiv 2606.00246 eq (32), Lemma 8.1, Ansatz 1.1, (22). New here: the converse (necessity), sharp 2/ln2, pseudo-likelihood form - see fei_one_coordinate_step_is_in_gonzalez_macmanus_pereyra_2606_00246_2026_11_10"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T02:04:40+02:00
  status: provisional
  evidence: 06_math_research/fei_solve_2026_11_09/code/check_erasure.py and check_erasure_*.txt; FLOW.md section 7
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-10T15:31:30.663Z
---

**Answer.** FEI (H(fhat^2) <= C I(f) for every Boolean f) is equivalent, with constants changing by at most 2/ln 2, to each of:

1. **Erasure form.** With U drawn from the spectral measure mu = fhat^2: sum_i H(1[i in U] | U minus i) <= C I(f). The left side is the erasure entropy H^- of U.
2. **Pseudo-likelihood form.** G := E_U sum_{i in U} log2(1 + mu(U minus i)/mu(U)) <= C E|U|. In words: each element present in U is predictable from the rest of U, on log average. G <= H^- <= G + I/ln 2.
3. **One good coordinate.** Every nonconstant Boolean g has ONE coordinate i with H(1[i in U] | U minus i) <= C Inf_i(g).

**Why.** Restrict coordinate i: D_i(f) := H(f) - (1/2)H(f_{i->+1}) - (1/2)H(f_{i->-1}) = E_i + J_i, where E_i = H(1[i in U] | U minus i) = sum_T (a^2+b^2) h(b^2/(a^2+b^2)) with a = fhat(T), b = fhat(T+i), and J_i is the Jensen-Shannon divergence of the two restrictions' spectra, 0 <= J_i <= (2/ln 2) Inf_i. Along any decision-tree order of the coordinates H(f) = E_path sum_k D_{i_k} and I(f) = E_path sum_k Inf_{i_k} exactly, so a good coordinate at every node gives FEI by induction; conversely FEI gives H^- <= H <= C I, and an average over i gives one good coordinate. Also H = integral_0^1 E[Psi(f restricted at rate p)] dp/p with Psi = sum_i D_i.

**Checked** (code/check_erasure.py, outputs code/check_erasure_*.txt in 06_math_research/fei_solve_2026_11_09): the identities hold to 1e-15 on all 65,536 four-variable functions and all 616,126 five-variable NPN classes (D_i also computed by actually restricting truth tables), on samples at n = 6, 7, 8 and on families to n = 14. sup H^-/I = 2.8836 for n <= 5 (truth table 0x1f), 3.598 on tribes 2x7. sup over functions of the best coordinate's D_i/Inf_i = 4.8677 for n <= 5 (AND_3), 5.997 on tribes 2x7. Majority and every odd or even function have H^- = 0. Bent: H^-/I = 2.

**What is false.** The per-coordinate version (every coordinate good) fails: bent inner product with one point replaced by a fresh dictator has worst D_i/Inf_i = 4.87, 8.03, 10.26, 12.31, 14.32, 16.33 at k = 2..12. The shortcut sum over edges |fhat(T) fhat(T+i)| <= C I is false too (bent with half its points replaced by fresh dictators: about 2^(k/2) against I about k/2).

**What it buys.** A coordinate with Inf_i >= 2^(-C) is good for free (E_i <= h(Inf_i)), so only functions all of whose influences are tiny matter, and an extremiser of C_n has Inf_i <= 2^(4.33 - C_(n-1)) for every i. The open core: for a tiny-influence coordinate, i in U must be recognisable from U minus i. Talagrand's inequality says the cluster of such a coordinate is large (size about log(1/Inf_i)); the form needs the posterior P[i in U | U minus i] >= 2^(-C) on log average, a conditional strengthening.

**Doubt to carry.** Status provisional: the equivalence is a short proof of mine checked numerically, not refereed by a second reader; whether the form is in the literature (Wan-Wright-Wu use the chain rule along decision trees; Chakraborty et al.) is not yet checked. Full text: FLOW.md section 7 in the same folder. Earlier forms: [[fei_l1_form_h_equals_2a1_plus_2gamma_chain_flow_codex_round1_2026_11_09]], [[fei_splits_into_containment_and_cancellation_n5_census_2026_11_09]], plan [[fei_solve_plan_up_ratio_form_h_le_2b_plus_2i_2026_11_09]].

