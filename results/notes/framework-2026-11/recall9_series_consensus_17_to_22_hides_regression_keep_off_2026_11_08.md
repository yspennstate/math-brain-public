---
name: recall9_series_consensus_17_to_22_hides_regression_keep_off_2026_11_08
description: "Does ranking by series consensus fix status-question recall? (RECALL9) Registered-member top-1 17 to 22 of 30, but it hid a regression (an unregistered relevant note got pushed down); keep off; 14 of 24 old misses never reach the top 20"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T23:23:01+04:00
  status: verified
  evidence: "codex_fleet/20261108_pro/workers/RECALL9 REPORT.md, test_metrics.json, promotion_audit.json, prior_diagnosis.json; the private repository c970c5c7c1"
---

Can recall find the right series first, then order inside it? (RECALL9, Codex gpt-6.1-sol high, reviewed by an agent 8 Nov 23:2x.) Keep it off.

Method: a consensus re-rank. Among the baseline top 20, sum 1/(20+rank) per registered series, require at least two members, and move the strongest series' best member to first. On a new frozen bank (30 series, 157 members, 2 user-style questions each, 30 controls, split 15/15 by series), held-out registered-member top-1 went from 17/30 to 22/30 (5 gained, 0 lost, series-bootstrap 95% CI +6.67 to +30 points). Top-3 went 22 to 25, top-10 26 to 27, newest-member top-1 5 to 7. All 30 controls kept their ordered top ten. The fake-series plant was not promoted.

Why it stays off: the audit found that the gain partly hides a regression. For "is the one copy obstruction settled now" the baseline's top hit was a relevant Bernoulli one-copy note that the small registry had left out. Consensus replaced it with a neural-network obstruction note from a registered series, and the metric scored both as wrong. A second "gain" swapped a relevant unregistered Bernoulli density note for a registered rigidity note. Scored against a registry, a series re-ranker can promote a registered sibling over a better unregistered answer. So any rollout needs a complete membership audit and wrong-subtopic controls.

Two more findings worth keeping. On RECALL8's 24 tune questions the right series was not in the top 20 at all for 14 of them: 12 wrong topic, 3 sibling series, and 7 with no shared content words. A re-ranker cannot fix that; the miss is coverage, as in [[recall6_split_bundled_recall_21_to_21_bodies_not_ranking_2026_11_08]]. And the new bank is much easier (baseline 17/30 against 2/24), because the implementer wrote its questions from the descriptions. Same lesson as [[recall8_series_registry_top1_2_to_4_of_24_keep_off_2026_11_08]] and [[recall7_status_newest_top1_2_of_30_series_head_fails_2026_11_08]]: the next bank must be written independently.

Full graph brain-graph-full-2026-11-07 (376,111 nodes, 16,811,666 edges, 243,031 sidecar links). The bank is burned. Pushed without keys or bank rows to the private repository, 12_cognitive_architecture/brain_improvement/recall9_series_consensus_2026_11_08 (c970c5c7c1).

