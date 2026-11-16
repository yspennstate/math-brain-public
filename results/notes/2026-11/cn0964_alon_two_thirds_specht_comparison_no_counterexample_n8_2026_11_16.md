---
name: cn0964_alon_two_thirds_specht_comparison_no_counterexample_n8_2026_11_16
description: "[PROVISIONAL] CN0964 Alon 2026 Conj 1.5 (lambda_min(G,tau) >= 2/3 lambda_min(G,sigma) when [n] != sigma dominates tau): no counterexample for n<=8 (all graphs n<=6, sampled n=7,8, per-pair gradient over weights); minimum is exactly 2/3, tight pairs listed; evidence only"
metadata:
  type: project
status: provisional
---
CN0964 is Gil Alon, "Spectral comparison on Specht modules and mixing of the interchange process", arXiv 2610.22151
(Oct 2026), Conjecture 1.5: for partitions [n] != sigma dominating tau and any nonnegative weights w_ij,
lambda_min(G,tau) >= (2/3) lambda_min(G,sigma), with L(G,rho) = sum w_ij (I - rho((ij))). Alon proves C >= n^-3, the
complete and quasi-complete cases, and sharpness (Thm 4.5: star on 2m vertices, tau=[2,1^{2m-2}], sigma=[2^m]). His
supporting simulations were AI-assisted. Web check 16 Nov: no later proof or counterexample found.

Search, 16 Nov 2026 (script spec.py, Young's orthogonal form): selftest passes (braid and character
checks, the star example gives 2m-2 and 3m-3 exactly, lambda_min on [n-1,1] equals the graph Laplacian gap, Aldous holds).
- Unweighted graphs: all labelled graphs for n<=6, 32768 sampled for n=7 and n=8; random-weight hill-climbs at n=4..8.
- Projected gradient descent on the weight simplex for EVERY dominating pair, using the exact eigenvalue derivative
  v^T A_e v: n=7 (87 pairs, 40 starts x 300 steps) and n=8 (195 pairs, 12 x 200). n=5,6 runs queued on mini1 as a recheck.
- Result: the minimum ratio is exactly 2/3 at n=4,6,7,8 and 3/4 at n=5 (graph search); the gradient never goes below 2/3
  (approaches it from above, 0.66666667..0.66666672).
- Pairs within 0.7 of the bound: (a,2,2)/(a,2,1,1) for a=3,4 (the n=4 star case [2,2]/[2,1,1] lifted), and
  [2^4] against [2,2,2,1,1], [2,2,1^4], [2,1^6]. All other pairs are well above. Minimising graphs are K_{1,3} with extra
  components or a tree containing a degree-4 vertex: the paper's star mechanism, no new extremal family found.

Verdict: consistent with the conjecture through n=8. Evidence only, not a proof; nothing posted.
A possible route to a proof: the tight cases all reduce to the local move [2,2] -> [2,1,1] on a star, so a branching-rule
induction (restriction to S_{n-1}) that isolates that move is the natural attempt.
Related: [[cn0948_ising_heatbath_gap_monotone_in_couplings_no_counterexample_n9_2026_11_16]] (same kind of search, same verdict);
[[open_problem_check_must_search_the_web_not_only_arxiv_titles_2026_11_16]].
What would change this: a weighted graph with ratio below 2/3 - 1e-9 that survives exact recomputation.
