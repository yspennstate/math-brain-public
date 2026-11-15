---
name: word_senses_from_contexts_lose_to_one_vector_old_shelf_2026_11_14
description: "[VERIFIED] Sense vectors for the writing brain? Tested 14 Nov: K=3 senses, centroid, top4 all lose to one SVD vector (top-1 .406 vs .33-.37, 3005 held-out passages); old shelf lacks modern senses"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T10:37:27+02:00
  status: provisional
  evidence: ""
---

senses.py (writing_brain/maths, commit 70eca08f) samples 48 window-6 contexts per word from 300 books of batch_001 and tests on 3,005 held-out passages of batch_101 (hidden word vs nine same-frequency words, brief = 30 words around it minus the word). Top-1/MRR: single SVD vector .406/.599; centroid .363/.555; senses K=3 max .351/.539; top4 .313/.509; centring by the shelf mean context (CENTER=1) gives .365/.328/.329, no better. Why: the SVD vector pools every occurrence; 48 samples are noisy and the max over senses rewards decoys with spread contexts. The queue-means-pigtail hole (NOTES Result 3) is the shelf: the biggest queue sense scores .12 on a cinema brief. Do not wire senses into context_fit.ctx on this shelf; what would change it is a modern shelf (twentieth-century fiction, screenplays). Related: [[writing_brain_ab_first_test_no_difference_writer_spread_dominates_2026_11_14]]
