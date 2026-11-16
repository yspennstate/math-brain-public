---
name: lumping_raises_mixing_time_at_most_n_minus_2_and_k4_is_2_2026_11_12
description: "Lumping a reversible chain: how much can the stopping-rule mixing time grow? At most n-2 (eigentime bound on the quotient), and K(4)=2 exactly via an explicit family"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T18:35:57+02:00
  status: provisional
  evidence: "Codex referee REPORT.md sections 1 and 7, P0242 f27880c; exact recheck agent_run/referee_1112/LUMP/check_k4_family.py"
---

Lumping a reversible chain can raise the stopping-rule mixing time by at most a factor n-2 (n >= 3 states), and on four states the sharp factor is exactly 2. Found by the Codex referee of lumping-mixing-time (P0242, f27880c) on 12 Nov 2026; the paper had max(1, floor((n-2)/2)) <= K(n) <= n-1 and a four-state ratio of 1.274.

Upper bound: apply the eigentime bound to the QUOTIENT, not the original chain. A genuine lumping has q <= n-1 states, so tmix(hX) <= tau0(hX) <= (q-1) tau2(hX) <= (q-1) tau2(X) <= (n-2) tmix(X). The relaxation time only shrinks under lumping (quotient eigenfunctions lift), and the last step is tau2 <= tmix. A bijection preserves the chain and a one-state quotient has tmix 0, so K(n) <= max(1, n-2).

Lower bound at n = 4: weights w02 = w12 = 1, w03 = w13 = t, loops w00 = w11 = t^2 - 1, w33 = t^6, lump {2,3}. With W = t^6 + 2t^2 + 4t + 2, tmix(X) = (t+1)(t^6+t^5+4t+2)/W and tmix(hX) = 2t(t^6+t^2+3t+2)/W; the ratio tends to 2 (1.999996000006 at t = 10^6; below 1 at t = 2). The sup is approached, not attained. Rechecked exactly by an agent with the Lovasz-Winkler formula tmix = max_{i,j} (E_i T_j - E_pi T_j) on Fractions at t = 2, 3, 10, 100, 10^6: both formulas equal.

Use: whenever an eigentime or Kemeny bound is applied to compare a chain and its quotient, count the quotient's states, not the original's; it costs one off the constant for free. The shape of the family (two leaves on a heavy-loop hub, the lump hiding a heavy state behind a light one) is a template for other "lumping slows mixing" searches.

Report: the private repository, 06_math_research/referee_reports/2026-11-12/LUMP/REPORT.md; sent to an agent (mesh topic referee/P0242), which posts the paper. Related: [[weighted_cayley_counterexample_lifts_to_simple_graph_by_cliques_2026_11_12]].

