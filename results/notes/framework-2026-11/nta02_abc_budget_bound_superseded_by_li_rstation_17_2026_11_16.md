---
name: nta02_abc_budget_bound_superseded_by_li_rstation_17_2026_11_16
description: "[VERIFIED] Swarm brief NTA02 abc exceptional set 3(1+lambda)/10 new? No: Li rStation paper 17 (9 Nov) runs BBLT program at budget lambda with 2^18 index sets, smaller values; ours correct but superseded, do not post"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T18:44:35+02:00
  status: provisional
  evidence: ""
---

Question: is the Codex swarm brief NTA02 (abc exceptional set, N_lambda << X^{3(1+lambda)/10+eps} for 9/11<lambda<1, from BBLT Prop 6.1 with the budget kept as lambda) new?

No. Hongmin Li, rStation math paper 17 v1 (9 Nov 2026, Zenodo 10.5281/zenodo.24082226, github Li-Hongmin/abc-exceptional-set-collision-inequalities) already runs the Bernert-Browning-Lichtman-Teravainen program at budget lambda with all 2^18 index sets (BBLT use 13) and certifies smaller values: base program 71/130 at 0.90, 86/167 at 0.85, and an envelope beta(mu) on [0.70,1.10] (0.583215 at 0.95, 857/1445 = 0.593080 on [0.97,0.99]).

What we checked (16 Nov, an agent): the finite LP lemma D <= 3(1+L)/10 exactly (Fraction family) and over all 8192 min-branches (scipy HiGHS on a second machine, max 0.30000000000000054); the transfer step: BBLT's own proof of Thm 1.3 writes ABC <= X^(lambda+3eps0), so L <= lambda+o(1) is already there. Correct, but a short corollary.

Ours is smaller than Li's tabulated beta only in a thin window near 0.955-0.977 (max ~0.002), and only because Li's beta there is an interpolated envelope; his larger program is <= ours at every budget by inclusion. Verdict: do not post; at most a remark citing Li.

How to apply: before any abc-exceptional-set claim, read Li's paper 17 and its Section 6 table. More generally, novelty searches must include rStation, Zenodo and GitHub: AI-produced preprints there now beat arXiv by days (see open_problem_check_must_search_the_web_not_only_arxiv_titles_2026_11_16). Record: 12_cognitive_architecture/codex_swarm_1115/CLAUDE_AUDIT.md (commit c945f0c2).

