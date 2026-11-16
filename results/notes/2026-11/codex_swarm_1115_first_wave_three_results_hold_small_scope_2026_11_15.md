---
name: codex_swarm_1115_first_wave_three_results_hold_small_scope_2026_11_15
description: "[VERIFIED] Codex swarm 15 Nov: which results survived two independent checks? PROBM03, COMP01, COMP05 hold (Codex audit + Fable + Claude recompute) but each is small; 74 briefs done on worker machine 1, Codex audits never said wrong"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T09:26:33+02:00
  status: provisional
  evidence: ""
---

15 Nov 2026, swarm codex_swarm_1115. worker machine 1 (gpt-6.1-sol high, normal speed) finished 74 briefs by 09:20; workstation Codex failed all morning with 'workspace routing discovery timed out' before any model turn.

Three results checked three ways (Codex AUD_ worker, an agent Fable FABLE_AUDIT.md with fable_checks/, an agent CLAUDE_AUDIT.md):
- PROBM03 (D0010): every unimodal polynomial density of degree <= 3 on [0,1] with mean 1/3 is 3-completely mixable; a strictly unimodal quartic at the same mean is not. Scope: boundary mean 1/n only.
- COMP01 (graph reconstruction): minimum number of fixed raw (n-1)-card multiplicity coordinates separating all n-vertex graphs is 1,3,8,22 for n=3..6, with 2,4,37,4 optima; complement-closed minimum 23 at n=6 (not rerun). Scope: fixed raw coordinates, order <= 6; the conjecture is untouched.
- COMP05: every member of the Strassen sandwich orbit needs exactly 18 XOR gates with all three linear phases at depth <= 2 (costs 5,5,8; 36 term sets). Scope: one orbit, depth two; 18 is Strassen's own count.

How to apply: a card for any of these carries the scope sentence; novelty is unestablished for all. The 33 Codex audits all returned holds/corrected, none wrong: same-family checking, treat as a first pass and get a Fable or recompute check before a card or paper. Folders: the private repository, 12_cognitive_architecture/codex_swarm_1115/briefs_mini1/<ID>. Related [[codex_mac_mini1_only_acc2_runs_gpt61_sol_refused_start_no_rollout_2026_11_15]] [[codex_brief_report_and_exit_0_without_the_work_count_the_files_2026_11_15]]
