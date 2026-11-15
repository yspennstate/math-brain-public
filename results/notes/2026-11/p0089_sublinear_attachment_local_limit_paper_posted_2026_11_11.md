---
name: p0089_sublinear_attachment_local_limit_paper_posted_2026_11_11
description: "P0089 (Aletti et al. Open Problem 24, preferential attachment fixed m, non-affine f) paper posted? Yes, 11 Nov: github.com/yspennstate/sublinear-attachment-local-limit 3f3b952c. Partial: class inf f>0, bounded increments, f(k)/k->0; local limit tree with explicit ball integrals. No independent referee read of the manuscript yet."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T06:22:52+02:00
  status: provisional
  evidence: "public repo main 3f3b952c9050034bd852b831fe02d04342ea51f8; ledger master 45d7a4f3; public table 38c3765c; four simulation runs n=1e6"
---

# P0089 paper posted: "The local limit of sublinear preferential attachment graphs with fixed out-degree"

Posted 11 Nov 2026 06:03 local by an agent (his 10 Nov 17:13 ask, T-20261110-076: solved but unposted problems get audited, written up and posted).

- Public repo: github.com/yspennstate/sublinear-attachment-local-limit, main = 3f3b952c9050034bd852b831fe02d04342ea51f8. 16 pages; code/sim_check.py; data/ four runs of 10^6 vertices (seeds 11, 12, 21, 22).
- Working copy ~/agent_run/p0089/ (repo/ is the git clone, paper/ the build folder, PLAN.md the notes). Brain mirror: brain-repo 06_math_research/p0089_sublinear_attachment_2026_11_11/.
- Source of the result: OP15 solo arm, 11 Oct 2026, ~/brain_workers/OP15_PAIRED_20261011/audit/P0089/X/ (ATTEMPT.md, SUBLINEAR.md); second audit in 06_math_research/op15_paired_2026_10_11/second_audits/P0089/.
- Problem: Aletti et al., Open problems in stochastic reinforcement models (MATRIX-MFO 2023), Open Problem 24 (Deijfen, van der Hofstad): local limits of preferential attachment with a fixed number m >= 2 of out-edges beyond the affine case.

What the paper proves (class E1-E3: inf f > 0, bounded increments, f(k)/k -> 0; no monotonicity):

- S_n/n -> c_f a.s., c_f the unique root of sum_{k>=1} prod_{j<k} m f(j)/(c_f + m f(j)) = m.
- Empirical in-degree law -> p(c_f) a.s. in l1 (pure birth, rates m f(k)/c_f, killed at Exp(1)).
- Local convergence in probability to an infinite simple directed tree; ball probability P_H = A(H)^{-1} integral of Phi_H over ages, Phi_H a product of explicit vertex factors (Proposition 12 of the PDF). Parent-age density h(log(x/y))/(c x): not uniform unless f is constant.

Proof route, reusable for other non-urn attachment models: (1) empirical degree vector as a stochastic approximation in l1 on the compact set {mean <= m}; tails of the noise controlled by the recursion itself, no l1 martingale theorem; (2) the time change dz/dt = (s(z)/m) F(z) makes the limiting ODE linear, w' = Qw + e_0 s(w)/m, solved by a renewal equation; the key renewal theorem gives attraction uniform over the compact set, with no stability computation; (3) exact change of measure to a process with finitely many forced slots; a maximal coupling shows forcing moves the normaliser by O(1/n); (4) tagged in-degrees become independent birth processes in log-age; (5) embedding count plus a two-root second moment. For unbounded f the uniform edge bound is replaced by a moment bound E(D_i + a)^p <= K (j/i)^{p theta} and the kernel max^{theta-1} min^{-theta}, whose l2 norm is at most 2/(1/2 - theta).

Size of the doubt: partial answer (sublinear class only; f(k)/k -> gamma > 0, affine or not, is not covered, nor other conventions for the m edges). The October audits: blind Codex referee SOLVED_CORRECT; the second audit did not re-derive the forced-slot coupling. On 11 Nov I re-derived every step while writing, and the simulations were repeated on Mac mini 2 (seeds 11 and 12 reproduce the October numbers, seeds 21 and 22 are new): degree laws, mean parent age ratio 0.4452 and the radius-2 ball probability 0.010648 all within about 1.3 standard deviations. No independent read of the manuscript itself yet; a referee read was asked of an agent on 11 Nov.

What would change it: a gap found by the referee in Lemma 14 (forced process has the same normalisation) or Lemma 15 (tagged degrees), or in the sublinear section's use of the generator domain (Lemma 19); a prior paper with a fixed-m non-affine local limit (web search 11 Nov: none; Banerjee-Deka-Olvera-Cravioto arXiv 2302.00562 is the collapsed-tree model, a different model for non-affine f).

A mistake caught on the read-through: the introduction said the scalar equation "reduces to the known value for affine f", but affine f is excluded by f(k)/k -> 0. Read every sentence of an introduction against the hypotheses of the theorem it introduces.

Related: [[p0072_loop_erased_ants_paper_posted_2026_11_11]], [[p0073_ants_dead_branches_paper_posted_2026_11_11]], [[duplicate_paper_posted_for_t067_withdrawn_check_public_table_first_2026_11_10]].


Update 11 Nov 08:2x (citation pass, his 07:06 order): the repo is now at main 1a29cfcf510838ae2d8b9f506f81a1ee29ef225c ("Add related work"; PDF 16 pages, 460112 bytes, 23 bibliography entries). The closest earlier result is Choi, Sethuraman and Venkataramani, Random Structures Algorithms 48 (2016) 703-731, arXiv:1402.4088: a law of large numbers for degree counts under w(k)/k -> 0 in a model adding one edge per step, by the same time change; their Remark 2.4 expects it for finitely many edges per step. The paper now says part (ii) is the counterpart of their theorem for fixed out-degree and that for m = 1 the formula for p_k is the product form of Krapivsky-Redner-Leyvraz; part (iii), the local limit, is what answers Open Problem 24 under (E1)-(E3). Public table copy math-brain-public ee81237888d5c4500daa50d794bd3a66ab4aa775; Zenodo 10.5281/zenodo.24127161 (record 24127161, uploaded by an agent from 1a29cfcf, 23 references stored); brain mirror 06_math_research/p0089_sublinear_attachment_2026_11_11 (NOTES.md has the citation-pass section). See [[citation_pass_closest_prior_result_sits_in_a_neighbouring_model_2026_11_11]].
