---
name: recall_long_prompt_lex_was_fold_scorer_python_loop_2026_11_13
description: "Recall lex.score slow (0.8-2.6 s) on long prompts? The plural-fold scorer took every long prompt and scored in Python dicts; exact numpy path landed, 12x"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T09:51:56+02:00
  status: verified
  evidence: "IMPROVEMENT_LEDGER an agent-20261113-fold-numpy; commit 5d0affc6"
  lesson: true
---

Recall's lexical step (served `sub:lex.score`) took 800-900 ms on the first call of each prompt, the one carrying the whole prompt text, and 1-2.6 s in-process on 2,500-character questions. The profile pointed away from the index: 4.4 of 4.75 s was in `bm25_fold.score`, mostly `dict.update` (2.2 s) and `arrays` (0.9 s).

Why: the plural fold (bm25_fold.py) takes over whenever one query word folds (`settlement`/`settlements`, both forms under df 200). A prompt with a few hundred distinct words almost always has one, so the fold scorer, not the overlay's own numpy scorer, scored every long prompt, one posting at a time in Python dicts.

Fix (13 Nov 2026, an agent, commit 5d0affc6, bm25_fold.py md5 752acb11): `_score_np` plus `np_arrays` on the overlay and sidecar sources. It uses the same expression and operand order, units in sorted order, each document's sum starting from 0.0, and ties by position. It returns to the loop when a unit's positions repeat. `BRAIN_FOLD_NUMPY=0` turns it off.

Measured: the lists were identical (slugs and float scores) on 33/33 served overlay calls (one rerun with 23 re-read and 30-33 fresh documents in the overlay) and on 66/66 direct sidecar calls at topk 20/60/400. Fold scoring went from 29.0 to 2.4 s over 45 served recalls, and from 43.2 to 8.4 s on the sidecar.

The general lesson: a speed fix to one scorer misses when a wrapper picks a different scorer for the very queries that are slow. Profile the slow call itself before choosing the lever. The overlay numpy scorer landed earlier the same day and never ran on long prompts.

