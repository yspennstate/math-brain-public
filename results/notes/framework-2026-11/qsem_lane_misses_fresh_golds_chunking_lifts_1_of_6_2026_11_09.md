---
name: qsem_lane_misses_fresh_golds_chunking_lifts_1_of_6_2026_11_09
description: "[PROVISIONAL] No, chunking is not the fix (9 Nov, W06): 6 plain-language questions on tonight's memories, every gold has a vector, the query lane ranks them 90-466 or >2000; max-over-2000-char-chunks lifts 1 of 6 past the lane's 60th row"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T03:49:21+04:00
  status: provisional
  evidence: ""
---

Question: why do plain-language paraphrases miss memories filed tonight (W06 spot check, 1 of 6 golds in recall's top 10)?

Coverage is not the cause. All six golds have a vector (5 in the 15-min fresh overlay, 1 in the sidecar). The query-embedding lane (_query_semantic_scores) ranks them 281, >2000, >2000, 249, 466, 90; gold cosines 0.63-0.70 against top rows 0.72-0.82. The lane passes only its top 60 into z fusion (BRAIN_RECALL_QSEM_K), so none reach fusion through meaning.

The 2,000-char cut is large across the corpus: _text_for embeds the description plus the first 2,000 prose chars, and 38,309 of 50,871 memories (75.3%) run past it; 52.7% of all memory text is never embedded; 299 have a dated or correction paragraph past the cut (past2000.py). So an amended conclusion is invisible to vectors.

But re-embedding the tail does not rescue these golds. Max cosine over 2,000-char chunks (description kept as a title on later chunks) against the lane's 60th-row cosine: 0.669 vs 0.673, 0.628 vs 0.688, 0.663 vs 0.676, 0.736 vs 0.726 (LIFTS), 0.674 vs 0.713, 0.677 vs 0.684. One of six. The gap to the cut is 0.004-0.06, so the lever is the pool size or the lane's discrimination, not coverage. K 300 would admit four of six by rank; whether it costs precision elsewhere is untested and needs a bank run (plain-voice 56 plus BRAINDEV check half), not six items.

Six items, one runtime, one index generation: provisional. Related: [[fuse1_recall_misses_meaning_far_qsem_w45_plus_0p012_no_default_2026_11_08]], [[recall_health_semantic_arm_ignored_fresh_overlay_false_degraded_2026_11_09]]. Scripts: qsem_audit.py, chunk_test.py, past2000.py (an agent).

Related: [[fresh_memories_at_query_cosine_top10_land_rank_20_to_40_in_recall_2026_11_02]] - the 2 Nov half of the same miss: there the golds were cosine top-10 and fusion buried them; here the author-style wording never gets them into the cosine top 60 at all.

End to end (9 Nov 04:49, asked by an agent): the six questions through brain.py recall -n 40 with only BRAIN_RECALL_QSEM_K changed rank the golds K60/K300 at 9/10, out/out, 10/10, 7/6, out/out, out/out (out = past 40). Top 8 is 1 of 6 in both arms: letting 4 of 6 into the 300-row semantic pool does not lift them through z fusion. Together with QSEMK1 (121 real prompts, hit@8 33 -> 34) K 300 costs nothing and gains about nothing; the fresh-gold miss lives in the fusion weights or the vectors, not the pool size.
