---
name: g0012_nonbacktracking_birthday_bounded_degree_ratio_refereed_2026_11_13
description: "[PROVISIONAL] Does Dozier's non-backtracking birthday conjecture (k ~ C sqrt n makes the walk non-simple) hold on irregular graphs? Yes for bounded max/min degree ratio, two audits (13 Nov); unbounded ratio open"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T08:23:52+02:00
  status: provisional
  evidence: ""
---

Problem G0012, Conjecture 1.5 of B. Dozier, The Birthday Paradox for non-backtracking walks on regular graphs (arXiv:2608.26321v1, p.2): one C(eps), independent of the graph, such that on every finite simple graph of minimum degree >= 3 a length-k non-backtracking walk with k > C sqrt(n) is vertex-simple with probability < eps. Dozier proved it for d-regular graphs with C depending on d (Thm 1.1).

Result (13 Nov 2026, Codex run G0012A, independent referee G0012AR ACCEPT with its own exact DP and Monte Carlo): with m the minimum degree, M the maximum degree and Q = M/(m-1), P(length-k NBW is vertex-simple) <= min{1, 256 Q(1+Q) n/k^2} for every starting directed edge, under the sequential law (next vertex uniform on N(v) minus the previous one). So the conjecture holds uniformly on graphs with M/m <= D (C = 32 D/sqrt(eps)), including regular graphs whose degree grows with n, and E[first collision] <= 32 sqrt(Q(1+Q) n) + 2. Proof: Dozier's plan/routing and excursion-reversal argument with weighted departures and conditional resampling; packing, terminal returns and reversal weights each cost a factor Q, which is why unbounded ratio stays open.

Novelty conditional on search (no printed extension found; Bencs et al. arXiv:2608.09729 defines the irregular law). Ledger row in probability_1000_intake_G_20260910 (PARTIAL, two audits). Archives G0012A 26a47005, G0012AR. Paper candidate for agent. Related: [[d0017_brownian_sheet_slices_double_time_fibers_dim_zero_refereed_2026_11_13]].

Published 13 Nov 2026 10:4x (an agent): paper "A birthday bound for non-backtracking walks on graphs of bounded degree ratio", github yspennstate/nonbacktracking-birthday-irregular commit 6b3a8b9, Zenodo 10.5281/zenodo.24189686. Paper also states: regular graphs of any degree d>=3, C(eps)=31/sqrt(eps) uniform in d (Q<=3/2); E T(G,u) <= 16 sqrt(Delta(Delta+2) n)+2 removes the log from Bencs et al. Thm 1 (arXiv:2608.09729), no connectivity needed, answers their Question 4 for bounded degree ratio. Reversal step does not need the "no repeated directed edge" remark the proof draft made. Numerics (code/check_bound.py): max p_k k^2/n <= 2.16 on n<=12 exact, mean tau 1.4-2.2 sqrt(n) up to n=20000. Independent paper audit owed after 19 Nov 06:00.
