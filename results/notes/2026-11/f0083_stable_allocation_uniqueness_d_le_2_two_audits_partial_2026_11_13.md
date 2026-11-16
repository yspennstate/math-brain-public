---
name: f0083_stable_allocation_uniqueness_d_le_2_two_audits_partial_2026_11_13
description: "[PROVISIONAL] HHP 2006 problem (i), nonunique stable allocations: none in d=1,2 for any locally finite centre set; in all d none if sum 4^k/(1+N(2^k))=inf. Two audits (referee MINOR), PARTIAL; an extension of HHP's proof."
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T11:00:29+02:00
  status: provisional
  evidence: ""
---

Problem F0083 = Hoffman-Holroyd-Peres, A stable marriage of Poisson and Lebesgue, Ann. Probab. 34 (2006), arXiv:math/0505668, open problem (i), reprint p.31: is there a discrete centre set in R^d with two stable allocations differing on a nonnull set? HHP note such a set needs superquadratic growth (Thm 2) and cannot come from a translation-invariant process (Thm 3).

Result (claim run F0083A, Codex gpt-6.1-sol on worker machine 1, 13 Nov 2026; independent referee F0083AR MINOR with its own grid Gale-Shapley code): (a) for every locally finite centre set in d = 1 or 2 and every appetite 0 < alpha < infinity the stable allocation is a.e. unique, with no growth assumption; (b) in every d uniqueness holds when sum_k 4^k/(1 + N(2^k)) = infinity (N(r) = centres in B(0,r)), for example N(r) = O(r^2 log r log log r). Proof: directed disagreement graph between the site-optimal and centre-optimal allocations; receiving centres are sated with strictly decreasing radii; sated territories inside a radius-R neighbourhood are disjoint, so the reachable subgraph has O(r^d) growth even when the whole set is dense; then HHP's Proposition 13 flow and a Nash-Williams cut count. The referee found no mathematical gap; its corrections are bibliographic (Haji-Mirsadeghi-Khezeli is EJP 21 (2016) paper 51). Value: an extension of HHP's own proof by one packing observation, priority open; d >= 3 superquadratic sets stay open. Ledger row intake_F (two audits, PARTIAL). Archives F0083A 05d109fc, F0083AR (13 Nov).
