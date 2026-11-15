---
name: recall_lost_before_fusion_is_reworded_miss_not_a_cap_2026_11_10
description: "Recall loses the right memory before fusion on ~43 pct of reworded bank questions: raise BRAIN_LEX_TOPK / QSEM_K? No - vectors all current, widening to 500 puts 0 of 26 recovered golds in the fused top 10; real paraphrase misses in a 4x larger store"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T22:29:46+02:00
  status: verified
  evidence: "rs_implement fitw_lost_interim.json, fitw_vec_check.py output 224/224 current, fitw_wide.py --report on 52 reruns at K 500 (10 Nov 22:26)"
---

Recall misses the right memory before fusion on about 43 pct of the 22 Sep bank's paraphrase questions (203 of 470 measured,
10 Nov, through a copy of brain.py with an env-gated dump at the z fusion and the resident server off). Neither cap nor
vector health is the cause, and widening the lists does not help:

- Every lost gold has a current row in the vector sidecar (224 of 224; sidecar 61,473 rows). A gold that does reach the
  bm25 body always has a cosine (274 of 274).
- With BRAIN_LEX_TOPK and BRAIN_RECALL_QSEM_K raised from 60 to 500 (52 lost questions rerun): the gold enters either list
  within 100 on 4, within 200 on 11, within 500 on 25, and is past 500 in both on 27. Of the 26 it becomes a candidate on,
  its fused rank at w 0.3 is in the top 10 on 0 and the top 60 on 2. (Fusion stage only: the graph lane and the later
  steps are not in this rank, so an end-to-end check could still lift a few; 0 of 26 leaves little room for that.)
- The rivals above it are ordinary memories (cosine top 20: 607 of 720 ordinary; checklist entries 27, compaction nodes 5),
  not machine-written nodes crowding the store.

So these are reworded questions whose words and meaning both sit far from the memory, against a store about four times its
September size. R11's September figure for reworded questions was hit@10 220 of 494, the same order. A fix has to change
what the query or the memory says (query rewriting, a description written in the asker's words, a second query from a
different angle), not how many candidates are kept. Do not raise the two caps for this.

What would change it: a bank written after November, or a store pruned back toward its September size, measured the same way.
Scripts: brain_improvement/rs_implement_21ba_2026_11_10/ (fitw_lost.py, fitw_vec_check.py, fitw_wide.py).

Related: [[use_graph_walk_push_loses_to_eight_steps_2026_11_10]] (same campaign, the walk side).

Full rerun (10 Nov 22:57, all 211 lost questions at caps 500): the gold enters either list within 100 on 23, within 200 on 53, within 500 on 99, past 500 in both on 112. Of the 99 it becomes a candidate on, fused rank at w 0.3 is top 10 on 0, top 60 on 9, median 189. Same conclusion as the 52-question cut: do not raise the caps. (fitw_wide_fused.py)
