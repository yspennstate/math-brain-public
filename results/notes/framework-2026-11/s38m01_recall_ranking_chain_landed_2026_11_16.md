---
name: s38m01_recall_ranking_chain_landed_2026_11_16
description: "Recall ranking: five segments now chained, not concatenated (S38M01, landed bed48fd1dc72); outputs identical, ranking peak 891KB->2KB"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T13:06:19+02:00
  status: verified
  evidence: "AUD_S38M01/AUDIT.md (release swarm-s38-20261116); commit bed48fd1dc72; six live recalls diffed identical 16 Nov"
---

brain.py recall consumes its five ranking segments (bm25 block, lexical, graph, semantic tails, demoted) through itertools.chain instead of building one list; ranked is read once, in the scoring loop (zipped with _gpos when present). Audited by AUD_S38M01: 256/256 frozen recalls byte-identical, hit@1 136/256 and hit@5 175/256 unchanged, ranking-stage peak 891,352 -> 1,924 bytes, ranking 1.92 -> 1.65 ms/query. Six live recalls identical before/after on 16 Nov. Small gain; empty or singleton segments allocate slightly more. If anything later reads ranked twice (len(), indexing, a second loop), it must become a list again. Ledger IL-20261116-S38M01. Related: the recall-speed task.
