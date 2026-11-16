---
name: lumping_r_merges_partial_one_block_lemma_k7_open_2026_11_12
description: "Lumping r merges: tmix grows at most r+1? Partial (12 Nov): one merged block of any size keeps its row <= T, two pairs <= 2T, no counterexample; K(7) still 3 or 4"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T20:29:42+02:00
  status: verified
  evidence: "brain 06_math_research/referee_reports/2026-11-12/K6P/VERDICT.md and K7P/VERDICT.md"
---

Question: when a reversible chain is lumped by r = n - q merges, does the stopping-rule mixing time grow by at most r+1
(the conjecture that would give K(n) = floor(n/2))?

Status 12 Nov 2026: partial, no counterexample. Codex run K6P (worker machine 1), checked by an agent.

Proved (checked by hand and by direct hitting solves on 400 random chains):
- Rank-r update: Fhat = F - F C (C^T F C)^{-1} C^T F, columns of C the r differences e_a - e_b inside blocks.
  F_ij = E_i T_j - E_pi T_j (symmetric for reversible chains), T = max F.
- One merged block of ANY size: Fhat_{B,f(j)} <= t_j <= T, t_j = max_k F_jk. Proof: h = E.T_B, nu = (d - L h)/W is a
  probability on B, h - E_pi h = sum_b nu_b F_{.b}; the quotient's entry equals the left side since the chains agree off B.
- Two disjoint merged pairs: every entry touching a merged pair is <= 2T.
- The Q1 minimum-potential trick extends to any partition when the boundary vectors C^T phi_i, C^T phi_j are proportional.
Open: entries between two untouched singletons with non-proportional boundary vectors (exact 7-state witness defeats the
method, not the claim). 3 <= K(7) <= 4 (an interval: K is a supremum over real conductances, no integrality is known); K(8) = 4. Near-sharp exact families: r=2 -> 3 at n = 6,7,8; r=3 -> 4 at n = 8.
Refuted in passing: That <= T + kappa - kappa_hat (Kemeny constant).

Before calling any of this new, check Hermon-Peres (EJP 2018, DOI 10.1214/18-EJP154) and Hermon's sensitivity papers
(scar p0242_lumping_af445_resolved_hermon_peres_our_note_on_n_2026_11_12). agent owns that check and lumping v2.
Records: brain 06_math_research/referee_reports/2026-11-12/K6P/ (REPORT.md, VERDICT.md, indep_check*.py).
Related: [[one_pair_merge_at_most_doubles_mixing_time_and_k5_is_2_2026_11_12]], [[lumping_mixing_time_fork_comb_k_n_at_least_floor_n_over_2_2026_11_12]].

Update 12 Nov 2026 (Codex run K7P, checked by an agent): 3 <= K(7) <= 4 still; the run narrows nothing. Writing it "{3,4}" was a mistake: it went into lumping v2 Theorem 1 as a two-value claim and the LUMP2 referee (12 Nov) flagged it as unproved.
- Proved and checked exactly: projection-cost (diagonal) routes are dead. Family (a,b,u,v), w_au=w_bu=1, w_uv=t^2,
  loops t-1,t-1,t^6: merging {u,v} gives a_a = Fhat_aa - F_aa = t^2(t^4+1)^2/W while T = N/W, so a_a/T ~ t^3
  (891 at t=10). Clones carry it to 5-7 states for both r=2 shapes. Cauchy-Schwarz and sequential row-max budgets
  also fail on exact witnesses.
- Proved (read, not computed): orthogonal-minimum bound Fhat_ij <= t_i + t_j - (1+1/lambda) E_pi m; its natural
  sufficient bound fails exactly, so it does not give 3.
- Evidence: ~836k exact rank-two evaluations n=6-8, best pairs ratio 3 - 6e-12, triple 2 - 2e-12.
Next idea if anyone returns: an estimate that uses both boundary vectors at once (rank-two structure), not per-state costs.
Records: brain .../2026-11-12/K7P/ (REPORT.md, VERDICT.md, indep_check_agent.py).
