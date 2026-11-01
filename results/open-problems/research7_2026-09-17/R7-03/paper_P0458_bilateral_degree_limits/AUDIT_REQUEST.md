# P0458 independent audit checklist

This file is an audit request/checklist only. It is **not** an independent audit and must not be counted as one.

Target: `P0458`  
Paper: `research7_2026-09-17/R7-03/paper_P0458_bilateral_degree_limits/main.tex`

The closure protocol requires two genuinely independent full-proof audits:

1. one actual P26 audit;
2. one distinct OTHER-track audit.

Each auditor should read the paper from the source definition forward rather than relying on R7-03 summaries.

## Required proof checks

1. Verify the score-orientation equivalence and the exact definition of `LK(n,k)` against the final Dabirian–Subramanian paper.
2. Verify the conditional order-statistic statement: given the root cutoff `X`, the selected root scores are iid `Uniform(0,X)` and the non-root edge scores retain the required independence.
3. Verify `T_i ~ Beta(k,n-k-1)` and the exact rejection equivalence `U_i >= T_i`.
4. Re-derive the unique-shared-edge covariance bound, including the exact beta integral `1/(n-2)` and the use of Popoviciu's inequality.
5. Check the good-event tail estimate for `X`, the bound on `E Var(H|X)`, and the claim that conditional noise is `o(s_n^2)` uniformly throughout every sequence `k→∞`, `n-k→∞`.
6. Check the beta CLT/Wasserstein argument, the identity `k q_n(X)/s_n = [k/(nX)] g_n(U_n)`, and first-two-moment convergence.
7. Independently compute `E g(Z)=1/sqrt(pi)` and `Var(g(Z)) = 1/3 + (sqrt(3)-2)/(2*pi)`.
8. For fixed complement `r`, verify the upper-tail coordinate representation and the exact mark probability `Bin(n-2,y/n) <= r-1`.
9. Verify the finite-window marking lemma: after deleting candidate-candidate edges the endpoint stars are disjoint, and the probability any deleted edge changes the finite mark vector is `O(m^2 L/n)`.
10. Check the uniform integrable envelope used to remove the compact cutoff, including the corresponding second-factorial-moment bound needed for variance convergence.
11. Verify the mixed-Poisson representation and the exact formula for `Lambda_r(a)`.
12. Independently recompute `mu_r`, `M_{2,r}`, and `nu_r`; in particular verify `r=1` gives `nu_1=7/12` and `r=2` gives `nu_2=433/432`.
13. Check the beta–gamma alternate derivation of `mu_r` as a genuinely independent calculation.
14. Check the `r→∞` gluing argument, especially the sign convention in `E[(V_r-U_r)_+|U_r]`; distributional equality with `g(Z)` uses symmetry of the standard normal.
15. Check the subsequence classification and that the fixed-`k` use of the EWT theorem has the correct model specialization.
16. Check source scope: the source asks for the standardized degree law and explicitly flags the variance dependence problem; do not broaden the audit verdict to the separate degree-concentration question.
17. Check the dated prior-art review separately from the mathematical proof. A proof PASS does not certify novelty.

## Verdict format requested

An audit should say one of:

- `PASS_FULL_MATHEMATICAL_PROOF` — source-scope theorem and all necessary moment/standardization steps verified;
- `PASS_WITH_NONSUBSTANTIVE_EDITS` — proof is complete but exposition/notational corrections are needed;
- `FAIL_REPAIRABLE` — identify exact lemma/equation and a concrete repair;
- `FAIL_MATHEMATICAL` — identify the first invalid source-level step and whether the main theorem survives.

The audit should give its own immutable report path and creation commit. Repeated reviews by the same track count as one auditor.
