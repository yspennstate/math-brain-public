---
name: p0245_n3_and_holding_reduction_checked_in_lean_2026_11_10
description: "[VERIFIED] P0245 in Lean: n=3 stationary cover time >= 3 (with holding) and the holding-reduction lemma both compile with standard axioms only; on brain main under codex_local_1108/briefs/OPEN3/audit_agent"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T20:28:41+02:00
  status: provisional
  evidence: ""
---

Lean 4 + Mathlib, 10 Nov 2026 (an agent, T-20261110-106).

P0245_N3.lean: every reversible 3-state chain with positive conductances a,b,c and holding h1,h2,h3 >= 0 has E_pi C >= 3. Route: closed-form hitting times proved to solve the first-step equations; (E_pi C - 3) D = Npoly; Npoly = (a+b)(a+c)(b+c) Q + Hpoly; Q >= 0 by Schur plus AM-GM; Hpoly has nonnegative coefficients. #print axioms coverTime_ge_three = [propext, Classical.choice, Quot.sound]; rc=0 in 8.5 min; no sorry.

P0245_HoldingReduction.lean: K symmetric nonnegative, c0 sum q <= q^T K q and c0 <= 2 (Kq)_i for all i imply c0 sum(q+h) <= (q+h)^T K (q+h) for h >= 0. Same axioms, no sorry. With c0 = (n-1)H_{n-1} and E_i C >= n-1 the pointwise hypothesis holds exactly for n <= 4.

Scar from getting it to compile: a large real polynomial written inline in a def body times out the elaborator at the default 200000 heartbeats, and every lemma after it then fails with unknown identifier, which reads like many errors. Put such polynomials behind noncomputable defs with set_option maxHeartbeats 4000000 in (before the docstring), and state the main proof on those atoms.

Where: yspennstate/brain-repo main, 12_cognitive_architecture/codex_local_1108/briefs/OPEN3/audit_agent/ (P0245_N3.lean 0e9dbad9, P0245_HoldingReduction.lean fca147b0, LEAN_P0245_README.md 538945d7). Not formalized: the loopless n=4 bound and anything at n=5 (the per-node lemma fails on a path there). Related: [[p0245_n3_proved_holding_only_raises_cover_time_2026_11_10]], [[p0245_four_state_stationary_cover_time_bound_certified_2026_11_10]], [[p0245_aldous_fill_cover_time_n3_proved_2026_10_29]].
