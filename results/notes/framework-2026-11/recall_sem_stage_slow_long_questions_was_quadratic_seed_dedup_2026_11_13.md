---
name: recall_sem_stage_slow_long_questions_was_quadratic_seed_dedup_2026_11_13
description: "Recall stage:sem 2-9 s on long questions? It was a quadratic list-membership dedup of seeds in _semantic_scores, not I/O; set + partition top-256 gave 3.1 -> 0.19 s at 3000 seeds, identical output (13 Nov, commit 006fffe7)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T04:32:24+02:00
  status: verified
  evidence: "sem_verify.py old-vs-patched on 6 seed sets, identical incl order; brain repo commit 006fffe7368e blob 632a92bc; ledger row an agent-20261113-sem-top256-partition-set-dedup"
---

Recall's stage:sem took 2-9 s on long questions (hundreds to thousands of lexical seeds) while ordinary calls took about 0.1 s. The cause was not file I/O or contention: `_semantic_scores` in brain.py appended each seed to the top-256 candidate list only after checking `all(s != existing for existing, _ in candidates)`, a scan of a list that grows with every append. That is quadratic in the seed count. At 3,000 seeds it took 3.1 s of pure Python on its own. A full Python sort of all 65k embedding rows came on top, about 0.06-0.37 s on every call.

Fix (13 Nov 2026, an agent, brain repo commit 006fffe7368e): the dedup uses a set, and the top 256 come from np.partition plus a stable argsort over that slice, so ties keep their idx_e order exactly as the stable sort did. BRAIN_EMB_LAZY=1 still takes the old sorted walk.

Measured with embeddings memoised on the loaded workstation, old vs new: 1 / 5 / 30 / 200 / 800 / 3,000 seeds took 0.093 / 0.088 / 0.099 / 0.135 / 0.195 / 3.107 s before and 0.066 / 0.027 / 0.025 / 0.041 / 0.067 / 0.187 s after. The output dict was identical, order included, on all six sets (scratch sem_verify.py). Recall answers are therefore unchanged.

Lesson for the next speed hunt: when a stage's cost grows with query length, look for a Python membership test against a list before blaming stat or hash I/O. I first blamed contention and then I/O; both were wrong.

What would change this: a seed source that hands duplicate slugs (seeds is a dict, so none today), or BRAIN_EMB_LAZY becoming the default.

