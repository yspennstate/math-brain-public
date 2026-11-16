---
name: p0073_ants_dead_branches_paper_posted_2026_11_11
description: "P0073 (Kious-Mailler-Schapira trace-reinforced ants, Conjecture 1.1) paper posted? Yes, github.com/yspennstate/trace-reinforced-ants-dead-branches 36e5a3c (11 Nov): Theorem 2 dead branches refutes part (b) on a 2-connected graph, Theorem 5 shadowed neighbours of F (3-connected example, mean-field only), dead-set conjecture exact on 22,828 cases n<=7 (computed, mean-field flow); independent referee (agent) found no gap in Theorem 2 and Lean-checked its deterministic steps; paper_release_guard checklist inside"
metadata:
  node_type: memory
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:07:04+02:00
  status: provisional
  evidence: repo main 227e6bc; code/table_out.txt; Mac 2 ~/p0073/ex7.jsonl
  modified: 2026-11-11T01:50:40.640Z
---

# P0073 ants paper posted: "Dead branches in the trace-reinforced ant process"

Posted 11 Nov 2026 03:0x local by an agent (standing rule: solved but unposted problems get audited, written up and posted).

- Public repo: github.com/yspennstate/trace-reinforced-ants-dead-branches, main = 227e6bcddc55cd14642a85edb30c753a1e22f7a3. 8 pages, code/, data/ (census n = 3..6).
- Brain mirror: the private repository, 06_math_research/p0073_ants_2026_11_10/census_agent/ (paper, code, data, NOTES_dead_branches.md, raw/ exploratory scripts). Working copy: ~/agent_run/p0073/ (repo/ is the git clone).
- Problem: Kious, Mailler, Schapira, arXiv 2106.10559, Conjecture 1.1: (a) W(n)/n converges a.s. to a deterministic limit; (b) every edge has a positive limit when dist(N,F) >= 2.

What the paper proves and what it only computes:

- Theorem 2 (proved, about the process itself): u a neighbour of F, H a vertex set without N, F, u joined to the rest of G - F by the single edge {u,y}. Then W_f(n)/n -> 0 a.s. for every edge f with an endpoint in H. The 4-cycle N,a,F,b plus a vertex y joined to a and F is 2-connected with dist(N,F) = 2, so part (b) fails as stated.
- Theorem 5 (proved, about the mean-field map only): if some neighbour of F has no neighbour in I = component of N in G - F - N(F), there is no equilibrium with all coordinates positive, so (a) and (b) cannot both hold there. K_{3,3} with N, F on one side plus the edge {x,F} is a 3-connected example. This does not by itself say which edge dies in the process.
- Conjecture 9 (not proved): the set of edges with limit 0 is an explicit set D(G,N,F) (code/dead_set.py). Mean-field census: zero set = D in 1,738 of 1,738 cases with 3..6 vertices, one flow limit from six starts in every case, largest real part of an eigenvalue on the support -0.054.
- Proposition 10: equilibrium on theta graphs, sum alpha_i^{L_i} = 1 with (1 - alpha_i)/(1 - alpha_i^{L_i}) constant; equal lengths alpha = k^(-1/L).
- Simulation (1e7 ants): dead edges decay like 1/log n (C4 + detour: W_ay/n 0.060 at 1e3, 0.040 at 1e7), so a simulation to 1e7 still shows a few percent on an edge whose limit is 0. Do not read a slow decay as a positive limit.

UPDATE 11 Nov 03:50 local (measured, Mac 2 census, public commit 36e5a3c): the seven-vertex census finished, 21,090 cases; with n = 3..6 that is 22,828 cases, one flow limit and zero set = D in all of them. One case (n = 7, cid 3769, N adjacent to F) was split by the classifier: edge {1,4} of D decays like 1/t (0.63/t) and one start began at 2.4e-5, so the "fell 20 pct between T and 2T" test missed it at T = 2000; at T = 20,000 all six runs agree (code/rerun_3769.py). Lesson for the next census: a zero test by relative decay misses a 1/t coordinate that starts tiny; rerun any split case at 10x T before calling it a second limit. Over n <= 7: largest real part on the support -0.0153, smallest positive coordinate 0.0019; distance >= 2 reduced 9,806, dead edge in 4,118, of which 2-connected 1,643 and 3-connected 247, and those are exactly the cases where Theorem 5 applies. The paper now cites Mailler and Varin, arXiv 2601.22855 (two-nest ants) as related work.

Size of the doubt: the proof of Theorem 2 was audited line by line by its author agent, then read by an independent referee (an agent, audit_agent in the same brain folder), whose verdict at 03:1x on 11 Nov was no gap, keep the repo as it is. The same agent checked the deterministic steps of the proof in Lean (geom_e, geom_a, drift, sum_by_parts, block; standard axioms, no sorry): brain main 98b53434, 06_math_research/lean_checks_agent/p0073_dead_branch/. The probabilistic steps (the martingale and Borel-Cantelli parts) are not formalised. The seven-vertex census (21,090 cases) was 12,800 done on Mac 2 (~/p0073/ex7.jsonl) at filing; the table in the paper covers n <= 6 only.

Posting scars from this one (apply to the next paper repo):
1. A new public paper repo is refused at push by ~/.claude/dreaming/paper_release_guard.py unless the tex has: funding section, competing-interest declaration, Declaration of generative AI, acknowledgment naming Claude and Codex with Math Brain cited, links to math-brain-public, brain-framework-public and math-brain-2026-10-24, a code and data availability section, and no Overfull hbox over 1pt. Model block: 06_math_research/fei_papers_agent/p6/main.tex (tail). Write it before `gh repo create --push`; the create succeeds and the push fails otherwise.
2. `gh` on the workstation has no stored login: export GH_TOKEN from `git credential fill` (never echo it). REST quota can sit at 0 until the hour turns; `gh api rate_limit` is free.
3. `git commit` in a fresh clone has no author: pass -c user.name / -c user.email (the noreply address used by the earlier paper repos).
4. Long URLs in the bibliography overflow the line: put the URL on its own line after `\\`.
5. Before writing: list every yspennstate repo and check the public papers table for a duplicate (memory duplicate_paper_posted_for_t067_withdrawn_check_public_table_first_2026_11_10).

What would change it: the referee finding a gap in the drift argument of Theorem 2; an n = 7 case with two limits or a zero set different from D; a published proof or refutation of KMS Conjecture 1.1(b) that predates this. Two web searches on 11 Nov returned only the KMS paper (arXiv 2106.10559v2, 2 Oct 2023) and arXiv 2601.22855 (two-nest ants on triangle-series-parallel graphs, which sets the trace-reinforced version aside); no resolution of the conjecture. A citation-list read of 2106.10559 has not been done.

Related: [[p0073_ants_unique_fixed_point_all_graphs_to_7_vertices_2026_11_10]], [[fei_p6_sparse_linear_dnf_posted_2026_11_11]], [[duplicate_paper_posted_for_t067_withdrawn_check_public_table_first_2026_11_10]].


Update 11 Nov (citation pass, his 07:06 order): the repo is now at main 6e54ad0d402359c6b81012f1b3a04190c7b0be7a with the related work added (18 references). Public table copy math-brain-public bff0a19962e6a50e26fdc49097418d99772a39d6; Zenodo new version 10.5281/zenodo.24126620 (uploaded by an agent, md5 matches the GitHub PDF); brain mirror 06_math_research/p0073_ants_2026_11_10/census_agent (dead_branches.tex, dead_branches.pdf, NOTES_dead_branches.md).
