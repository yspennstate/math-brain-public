---
name: seed_lane_skips_fresh_overlay_tag_only_rank_same_80_of_80_2026_11_09
description: "Do memories filed since the last sidecar build lack semantic recall? No: the query lane reads the fresh overlay; only the seed lane and its sem tag skip it; patching it changed 0 of 80 gold ranks, tag 0->33 of 39"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T12:13:11+04:00
  status: verified
  evidence: "semfresh_ab.py 40 fresh + 40 older body-sentence queries, rank identical 80/80; ov_current_probe 1404/1405 current; qlane_probe golds nominated 7/21/13 of 60"
---

No, recall order is unaffected; only the label is wrong. brain.py has two meaning lanes. The query-vector lane (`_query_semantic_scores`, `_qlane_cosines`) reads the fresh overlay memory_embeddings_fresh.npz, so a memory filed since the last sidecar build is ranked by meaning like any other. The seed-centroid lane (`_semantic_scores`) reads only the sidecar, and the `sem` tag in recall output comes from that lane's score. So all ~1,400 overlay-only memories (everything since the sidecar build, back to late October) print as `lex` or `lex+graph`, never `sem`, even for a query that is their own description. On 9 Nov I first read this as fresh memories having no semantic recall; that was wrong.

Measured in-process on the live brain.py (nothing in .claude changed): 40 overlay-only and 40 sidecar memories, each queried with the first body sentence of its own file, both arms on the same queries. Patching the seed lane to read the overlay (fresh seeds join the centroid, top overlay rows scored) changed the gold's rank in 0 of 80 items; hit@1 35/40 fresh and 32/40 older in both arms. The only change was the tag: fresh golds shown with `sem` 0 -> 33 of 39. Not deployed. The bank was easy (35 of 40 at rank 1), but identical orders across all 80 items do not depend on that.

Also checked: the overlay's rows pass `embedding_row_current` (1,404 of 1,405; the one rejected was a memory edited minutes before), and for three plain-language questions recall missed in the top 8, the query lane nominated the fresh gold at ranks 7, 21 and 13 of 60, so those misses are ordinary ranking, not a dead overlay. Reading a missing `sem` tag on a recent memory as "no semantic match" is the mistake to avoid. Related: [[qsem_lane_misses_fresh_golds_chunking_lifts_1_of_6_2026_11_09]]. Scripts: semfresh_ab.py, qlane_probe.py, ov_current_probe.py (session scratch, 9 Nov).


The same fact was first filed 30 Oct as [[recall_row_tags_never_show_the_query_meaning_lane_2026_10_30]] (the tag never shows the query lane; 6 of 7 fresh golds ranked in its top 17); a synonym-row test met it too. This note adds the 80-item measurement that the order does not change. W06 9 Nov 12:2x: an plain-language question about it found the 30 Oct memory at rank 3 and this one not in the top 8.
