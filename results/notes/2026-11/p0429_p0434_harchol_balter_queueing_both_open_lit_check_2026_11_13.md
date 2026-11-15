---
name: p0429_p0434_harchol_balter_queueing_both_open_lit_check_2026_11_13
description: "P0429 (fork-join k(n) growth for asymptotic independence) and P0434 (sharp M-SERPT vs Gittins ratio, conjectured 2) both still open on 13 Nov 2026; best published fork-join exponent is still k=o(n^{1/4}) (Wang et al 2018; Mohanty-Gautam-Aggarwal-Parag ToN 2024 heterogeneous servers, same exponent, d_TV = O(k^2/sqrt n)); M-SERPT proven ratio 5 (3 for load <= 8/9)"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T14:30:11.952Z
---

Both come from Harchol-Balter, "Open problems in queueing theory inspired by datacenter computing" (QUESTA 2021).

P0429 (rank 24): how fast may k(n) grow with the k(n) stationary queues still asymptotically independent?
- Published: Wang, Harchol-Balter et al., "Delay asymptotics and bounds for multitask parallel jobs" (Queueing Systems
  2018, arXiv 1710.00296): k(n) = o(n^{1/4}).
- Mohanty, Gautam, Aggarwal, Parag, "Analysis of fork-join scheduling on heterogeneous parallel servers", IEEE/ACM ToN
  32(6), Dec 2024: slow and fast servers, Theorem 1 gives d_TV = O(k^2/sqrt n), so again o(n^{1/4}). No published
  improvement of the exponent found (arXiv search plus web search, 13 Nov).
- Ours: 6 Sep first pass (cubic collision heuristic) and R7-01 (17 Sep, "successful for the universal source class",
  charging removed parent arrivals by their stationary influence lifetime). R7-01 is our own unrefereed claim and is the
  thing to referee next if this problem is picked up: if it beats n^{1/4} it would be new.

P0434 (rank 25): sharp worst-case mean-response ratio of M-SERPT (or another simple age-based policy) against Gittins in M/G/1.
- Published: Scully, Harchol-Balter, Scheller-Wolf, "Simple near-optimal scheduling for the M/G/1" (arXiv 1907.10792,
  POMACS 2020): M-SERPT is a 5-approximation for all loads, 3 for load <= 8/9; Conjecture 8.1 says the sharp ratio is 2,
  with an example reaching 2. No proof of the conjecture found as of 13 Nov 2026.
- Ours: R7-04 (17 Sep) a finite-law structural lemma toward Conjecture 8.1, PROVED PARTIAL, not the full statement.

Searches: arXiv covers queueing poorly (SIGMETRICS/QUESTA papers often are not there), so a web search was run as well. A
miss here is weaker evidence than a miss in probability.
Related: [[p0151_fixed_outdegree_pa_critical_window_open_jmm_independent_edge_analogue_2026_11_13]] (same tick's sweep).
