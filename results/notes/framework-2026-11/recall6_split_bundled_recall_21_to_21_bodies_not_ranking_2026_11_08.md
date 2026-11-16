---
name: recall6_split_bundled_recall_21_to_21_bodies_not_ranking_2026_11_08
description: "Does splitting a bundled recall question find more? No (RECALL6): Codex 21 to 21, Claude 15 to 15 of 36; recall surfaced the sources, the arm lacked bodies"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:31:44+04:00
  status: verified
  evidence: "brain_improvement/DIAG7_20261108/split (5cd868bbaa)"
---

Does splitting a bundled recall question into one search per topic find more? No (8 Nov, RECALL6): Codex 21 to 21 of 36, Claude 15 to 15.

DIAG7's 30 recall-arm questions rerun offline through brain.py recall (-n 10, BRAIN_RECALL_LOG=0, BRAIN_RECALL_REFRESH=0, store brain-graph-full-2026-11-07). Each question ran as asked and split by a fixed rule (lead-in dropped, cut at commas, pieces interleaved to 10). Measure: plant-runs whose source memory is in a top 10. Prereg written before the run (split/PREREG.md; it needed +4 to call the split a help).

- Codex: 12 of 15 questions split; bundled 21, split 21.
- Claude: none split; 15 and 15.
- The bundled Codex questions surfaced more plant sources than Claude's one-topic ones (21 against 15). COMPACT_WINDOW ranked 3, 2 and 1 in the three Codex runs, but the Codex recall arm named it 0 times of 3.

So recall's ranking was not the bottleneck. The recall arm saw one description line per hit and had no calls left to read a body; the grep arm read whole files. This supersedes the bundling explanation in [[diag7_grep_32_recall_16_codex_17_15_agent_11_08]].

Next: a recall that prints more of the top hits' bodies (cause and fix lines), scored on the DIAG5 items.

Evidence: the private repository, 12_cognitive_architecture/brain_improvement/DIAG7_20261108/split (5cd868bbaa).

Correction (15:48): the explanation above does not hold. Most of the recall arm's misses were plants it never asked about (sources beyond rank 60 for every question the run sent: 12 of 20 Codex, 20 of 21 Claude); the limit was questions per call. With recall --each the same arm named 26 and 29 of 36. See [[diag8_recall_each_26_29_of_36_vs_16_15_coverage_not_bodies_2026_11_08]].
