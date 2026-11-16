---
name: one_pair_merge_at_most_doubles_mixing_time_and_k5_is_2_2026_11_12
description: "Lumping a reversible chain: can merging ONE pair more than double tmix? No - proved <= 2 (strict, sharp); entrywise Fhat <= t_i+t_j; min-of-potentials Dirichlet trick; gives K(5)=2"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T19:54:20+02:00
  status: verified
  evidence: "06_math_research/referee_reports/2026-11-12/K5P/REPORT.md; pad5_check_output.txt"
---

Does merging one pair of states raise the stopping-rule mixing time of a reversible chain by more than a factor 2? No: tmix(X/{u,v}) <= 2 tmix(X) for every finite irreducible reversible chain and every pair, strictly, and 2 is sharp (the four-state family a,b leaves on u, w_uv = t^2, loops t-1 at a,b and t^6 at v; ratio -> 2). Entrywise: Fhat_{f(i)f(j)} <= t_i + t_j, F_ij = E_iT_j - E_piT_j, t_i = max_j F_ij.

Proof (one page, Codex run K5P on worker machine 1, 12 Nov 2026; read line by line by an agent, no gap):
- phi_i = t_i - F_{i.} >= 0, L phi_i = W e_i - d, so E(phi_i, z) = W(z_i - E_pi z) and E(phi_i, phi_j) = -W F_ij.
- Rank-one merge identity: Fhat = F + beta_i beta_j/(WR), beta_i = phi_i(u) - phi_i(v) = WR(h_i - p).
- If beta_i beta_j > 0: m = min(phi_i/beta_i, phi_j/beta_j) has m_u - m_v = 1, so E(m,m) >= 1/R (Dirichlet); the leftovers g-m, k-m have disjoint supports, so E(g-m, k-m) <= 0 (off-diagonal Laplacian entries are nonpositive). Combining gives beta_i beta_j/(WR) <= t_i + t_j - F_ij - (beta_i + beta_j) E_pi m.
The method to reuse: a min of two normalised potentials is a test function for an effective resistance, and disjoint support kills the cross energy.

Consequence: with tmix(quotient) <= tau_0 <= (q-1) tau_2 <= (q-1) tmix(X), K(5) = 2 (K(4) = 2 was known). Lower bound on five states: hang e on v (w_ev = t^8, loop t^9) and lump {u,v,e}: exact ratios 1.6468 / 1.9606 / 1.9960 at t = 10 / 100 / 1000. Iterating Q1 alone only gives 2^(n-q). Open: K(6) (3 <= K(6) <= 4 from the fork comb and n-2).

Report and audit programs: the private repository, 06_math_research/referee_reports/2026-11-12/K5P/. Sent to an agent (P0242 author) for a v2 of lumping-mixing-time. Related: [[lumping_mixing_time_fork_comb_k_n_at_least_floor_n_over_2_2026_11_12]], [[lumping_raises_mixing_time_at_most_n_minus_2_and_k4_is_2_2026_11_12]].


Novelty NOT checked: before calling Q1 new, search "collapsing two states" / "merging states" mixing time, Hermon-Peres EJP 2018 (Problem 1.6, Theorem 3) and Hermon's later sensitivity papers. Consistent with Hermon-Peres: they bound a whole lumping by order log|V| on bounded degree; Q1 is the single-merge factor. Related: [[p0242_lumping_af445_resolved_hermon_peres_our_note_on_n_2026_11_12]].

Also settled (an agent, same evening): K(n) <= max over q of min(2^(n-q), q-1), with the fork comb K(n) >= floor(n/2) (2N+4 states, ratio -> N+2; exact 2.9930 at 6 states, 3.9860 at 8, t = 1000), gives K(6) = 3 and K(8) = 4. K(7) is 3 or 4 (only the 7 -> 5 two-merge case is open). The conjecture K(n) = floor(n/2) follows from Q2: r merges raise tmix by at most r+1 (with the q-1 bound). Codex run K6P on worker machine 1 (started 21:57 +04) works on Q2.

Independent check (an agent, 12 Nov 22:18, code written from the definitions, the run's own programs unread): the five-state ratios reproduce exactly (1.6468 / 1.9606 / 1.9960; 1.9996 at t = 10,000), the four-state family gives 1.7826 / 1.9798 / 1.9980 / 1.9998, always below 2, and 1,200 random reversible chains on 3 to 6 states (exact rationals, every pair merged) gave no ratio at or above 2 (largest 1.6172) and no entry above t_i + t_j. The proof text was not re-read in this check. Programs and verdict: 12_cognitive_architecture/loops/agent_loop_1112/MATH_AUDIT.md, audit_lumping_k5.py, audit_lumping_search.py.
