---
name: recall8_series_registry_top1_2_to_4_of_24_keep_off_2026_11_08
description: "Barely (RECALL8): explicit series registry lifts held-out newest-memory top-1 2/24 to 4/24, CI 0..+21 pts; the gap is finding the series, keep off"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T19:05:45+04:00
  status: verified
  evidence: "workers/RECALL8 metrics.json audit.json; recheck by an agent; commit 2716132120"
---

Does an explicit series registry get the newest memory of a series to the top for status questions? Barely (RECALL8, 8 Nov): held-out top-1 went from 2 of 24 to 4 of 24 (+8.3 points, paired series-bootstrap 95% CI 0 to +20.8), top-3 3 to 4, top-10 9 to 10, two gains and no losses. All 40 non-status controls kept the identical top ten. I recomputed these counts from paired_rows.jsonl against keys/gold.json with my own script (recheck_agent.py): same numbers, tune 0 to 2.

Why it stays off: the read patch (series_read.patch, gated by BRAIN_RECALL_SERIES_REGISTRY=1) only moves a known series head next to an older member already in the top three. For held-out questions any member of the right series is at top-1 for only 4 of 24, so the real gap is finding the series from the user's wording, not ordering inside it. A registered head about office supplies was still promoted in the plants: the registry records succession, not whether the head answers.

Registry: 24 series, 67 memberships, 152 source-checked quotes, 41 rejected candidates; a scoped seed, not full coverage. Both patches unapplied. Bank burned. Full graph 376,111 nodes, 16,811,666 edges, 243,031 sidecar links.

Next: current-status clauses with provenance in the memories themselves, and series retrieval from user wording, tested on new series.

Pushed to brain-repo 12_cognitive_architecture/brain_improvement/recall8_series_registry_2026_11_08 (commit 2716132120), without bank, keys or events.

Related: [[recall7_status_newest_top1_2_of_30_series_head_fails_2026_11_08]], [[recall_status_questions_miss_newest_series_memory_3_of_5_2026_11_08]]

