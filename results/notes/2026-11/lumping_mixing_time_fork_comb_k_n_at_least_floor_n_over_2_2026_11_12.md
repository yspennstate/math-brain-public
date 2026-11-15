---
name: lumping_mixing_time_fork_comb_k_n_at_least_floor_n_over_2_2026_11_12
description: "Lumping a reversible chain: K(n) >= floor(n/2) by a fork comb (one better than P0242's comb); K(5) still between 2 and 3"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T19:04:41+02:00
  status: provisional
  evidence: "06_math_research/referee_reports/2026-11-12/K5/REPORT.md; agent_run/k5/check_fork_comb.py exact recheck"
---

How much can lumping raise the stopping-rule mixing time of a reversible chain on n states? K(n) >= floor(n/2) for every n, one better than the floor((n-2)/2) comb in lumping-mixing-time (P0242). With the quotient upper bound K(n) <= max(1, n-2) this gives K(4) = 2, 2 <= K(5) <= 3, 3 <= K(6) <= 4. Found by a Codex research run on Mac mini 1 (12 Nov 2026, 20:38-21:00 +04) started from the K(4) = 2 result.

Construction (fork comb, 2N+4 states): a, b, c, spine z_0..z_N, teeth y_0..y_{N-1}; t >= 2, r = t^3, alpha = t. Edges a-z_0 weight 1, z_k-z_{k+1} weight r^{k+1}, y_k-z_{k+1} weight alpha r^{k+1}, b-z_N weight alpha r^{N+1}, c-z_N weight r^{N+2}. Loops: t-1 at a, (t-1) alpha r^{k+1} at y_k, (t-1) alpha r^{N+1} at b, (N+2) r^{N+4} at c. Lump {z_k, y_k} for k < N and {z_N, c}; keep a and b. The quotient is a path from a to a heavy root with b as a second leaf, N+3 states, and tmix(quotient)/tmix(X) -> N+2 = q-1, so every inequality in the quotient upper-bound chain is tight in the limit. It uses N+1 pair merges.

Rechecked independently by an agent with a separate exact solver (Fraction hitting-time systems, tmix = max_{i,j} (E_i T_j - E_pi T_j)): ratios 1.998000000002 (4 states), 2.993012973055 (6), 3.986037899261 (8) at t = 1000, identical to the run's table to 12 digits. Script: agent_run/k5/check_fork_comb.py.

Not settled: K(5). The run's searches (all ten pair merges, Powell and differential evolution over 15 log-weights) plateau at 1.998 < 2, and the natural equal-leaf generalisation of the K(4) family stays at ratio 2 for every number of leaves (it loses at tmix <= tau0 of the quotient). The run conjectures K(n) = floor(n/2), and in particular that merging a single pair raises tmix by at most a factor 2. Useful exact identity from the run, lifted to original states: Fhat_{f(i)f(j)} = F_ij + W R (h_i - p)(h_j - p), with h the u-before-v harmonic function, R the u-v effective resistance, p = E_pi h; so an increase needs two unmerged states on the same side of p.

Status: provisional until the P0242 author folds it in with a proof read. Report: brain-repo 06_math_research/referee_reports/2026-11-12/K5/REPORT.md. Related: [[lumping_raises_mixing_time_at_most_n_minus_2_and_k4_is_2_2026_11_12]].

