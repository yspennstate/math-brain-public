---
name: p0072_loop_erased_ants_paper_posted_2026_11_11
description: "P0072 (Kious-Mailler-Schapira loop-erased ants, AAP 2022 Conjecture 1.1(1)) paper posted? Yes, github.com/yspennstate/loop-erased-ants-non-geodesic-edge 0b26867 (11 Nov): on G_l (triangle N,u,v + two legs of l edges to F) weights converge a.s. to rho, 1-rho and (1-1/l)rho(1-rho) on the rung; l>=2 refutes the conjecture a.s., l=1 settles the loop-erased losange KMS left open; proof by one agent, referee read by agent pending"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T05:04:29+02:00
  status: provisional
  evidence: "public repo main 0b26867; data/run_l*_s*.txt; code/check_path_law.py output"
---

# P0072 paper posted: "A non-geodesic edge that survives in the loop-erased ant process"

Posted 11 Nov 2026 04:5x local by an agent (standing rule: solved but unposted problems get audited, written up and posted).

- Public repo: github.com/yspennstate/loop-erased-ants-non-geodesic-edge, main = 0b26867d38f71523555782e642da708a089acd90. 9 pages, code/ (sim_ants.c, check_path_law.py), data/ (13 runs of 10^8 ants, the fixed-weight frequencies, the symbolic check output).
- Brain mirror: the private repository, 06_math_research/p0072_loop_erased_ants_2026_11_11/ (commit c74723a63a15). Working copy ~/agent_run/p0072/ (repo/ is the git clone).
- Ledger: open-problems-repo master f9d6d59d12 ([skip ci]) added the P0072 row and the P0073 row that had been missed. Public table: math-brain-public main dbf75cd3 added both papers (papers/README.md and papers/public/<repo>/).
- Problem: Kious, Mailler, Schapira, Finding geodesics on graphs using reinforcement learning, Ann. Appl. Probab. 32 (2022), arXiv 2010.04820, Conjecture 1.1(1): for the loop-erased rule an edge keeps a positive share of the weight iff it lies on a geodesic from N to F. Open Problem 1 of Section 2 of the Aletti et al. survey (MATRIX-MFO 2023).

What the paper proves:

- G_l = triangle N, u, v plus a path of l edges from u to F and one from v to F. Theorem 2, every l >= 1: a.s. W_e(n)/n -> rho on N-u-...-F, 1 - rho on N-v-...-F, (1 - 1/l) rho (1 - rho) on the edge uv; rho in (0,1), symmetric, not constant.
- l >= 2: uv is on no geodesic and keeps a positive share almost surely, so the conjecture fails. The October OP15 result (11 Oct, two audits) had only positive probability and only l = 2.
- l = 1 (the losange): uv dies and the loop-erased process converges. KMS prove this only for the uniform-geodesic rule (their Theorem 1.4) and write that they could not prove it for the loop-erased rule. Do not say "KMS proved the losange" without the rule.
- Proof route, reusable for other reinforced-path models: (1) reinforced path = N-F path of the Aldous-Broder first-entrance tree = weighted uniform spanning tree path, so the path law is a ratio of tree sums; (2) psi(A) - psi(B) + l(psi(C) - psi(D)) is an exact martingale with surely bounded quadratic variation (psi(k) = H_{k-1}; the same harmonic-number device as P0081), giving a conserved coordinate logit a + l logit c; (3) a last-exit argument on psi(A_n) - log S_n bounds the main weights below; (4) Robbins-Siegmund on a - c; (5) a deterministic lemma for u_{n+1} - u_n = beta_n (g_n - e^{u_n + eta_n}) gives the rung limit without a separate lower bound on h.
- Simulation of the process as defined: all 13 runs agree; for l = 2 the gap to the limit shrinks by 0.56 per decade (10^{-1/4}, the linearised rate (1 - 1/l)/2), for l = 1 the rung decays like 1/log n (1/h grows 4.1 to 4.4 per decade). A dead edge at 10^8 ants still shows a few percent.

Size of the doubt: the convergence proof (Lemmas 8 to 12 of the PDF) was written and re-derived by one agent. The path law and drift are checked symbolically against brute-force spanning trees (l = 1..5) and the limits against simulation, but the probabilistic argument has no independent read yet: an agent accepted a hostile-referee read at 05:02 on 11 Nov and will post it to brain 06_math_research/lean_checks_agent/p0072_referee. If a gap is found, fix it and push a second commit; the counterexample itself (positive probability, l = 2) stands on the October audits either way.

What would change it: the referee finding a gap in the last-exit lower bound (Lemma 9) or the Robbins-Siegmund step; a published counterexample that predates this (web search 11 Nov: none; Mailler-Varin arXiv 2601.22855 of January 2026 still states the conjecture).

Posting notes beyond the P0073 list: TeX and regex text never goes through sed in the Bash tool (double backslashes are halved; "$\ell\ge2$" became "$ellge2$") - use Edit. The release guard prints nothing on success; read its exit code. A ledger row and a public table row both land through GraphQL createCommitOnBranch with expectedHeadOid when REST is spent (scripts agent_run/push_ledger_rows_1111.py, push_public_rows_1111.py). After posting, grep problems.jsonl on master for a row with public_repo for the problem: P0073 had been posted for two hours without one.

Related: [[p0073_ants_dead_branches_paper_posted_2026_11_11]], [[duplicate_paper_posted_for_t067_withdrawn_check_public_table_first_2026_11_10]], [[ledger_append_lands_through_graphql_when_rest_is_spent_2026_11_11]].


Update 11 Nov (citation pass, his 07:06 order): the repo is now at main 3d1bf7514b1216da5d0cc666d07f9ea0c6a17922. Armfield and Mailler (The forward-loop-erased ants walk, arXiv:2610.18453) define a variant in which the ant reinforces the loop-erasure of its trajectory instead of that of the reversed trajectory; it has the same law as the loop-erased process, so the theorem holds for it as well, and the paper and README now say so. Public table copy math-brain-public 7b170ce6d98d70a3829e5b3ebde2df35120d55df; brain mirror b5771871b225; Zenodo version 2, 10.5281/zenodo.24126502. See [[citation_pass_closest_prior_result_sits_in_a_neighbouring_model_2026_11_11]].
