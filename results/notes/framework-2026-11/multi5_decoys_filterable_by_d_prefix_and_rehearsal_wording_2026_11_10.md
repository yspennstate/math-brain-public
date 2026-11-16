---
name: multi5_decoys_filterable_by_d_prefix_and_rehearsal_wording_2026_11_10
description: "[PROVISIONAL] No: MULTI5's 4,000 decoys are dropped by one grep (d-prefixed ids, 'rehearsal' wording); classifier 1.0; scripted decoys cut a full run 24,432 -> 432 calls"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T00:57:58+04:00
  status: provisional
  evidence: "codex_fleet/20261108_pro/workers/MULTI5D-SCALE/REPORT.md, evidence/decoy_classifier.json, evidence/scale_measurement.json"
---

No (MULTI5D-SCALE, 10 Nov 00:5x): the 4,000 MULTI5 decoy diagnoses do not hide among the real ones. Their task ids all start with "d" and their findings describe "provisional rehearsals", so an agent reading the NOTES file can drop them with one grep. A logistic-regression classifier on length, punctuation and word TF-IDF told scripted decoys from model-written notes at held-out balanced accuracy 1.0 (6 model notes plus 2,400 decoys for training, 4 plus 1,600 held out; the positive sample is small). The d-prefix and the rehearsal wording come from the inherited bank, so the model-written decoys of MULTI5/5B/5C carry the same tell.

What the decoys still do: the NOTES file is 2.87 MB, and the first customer/date grep on t21 prints 101 lines (72,715 bytes) against the 8,192-byte repair budget. Brute reading still does not fit; only the "haystack" label overstates how hard filtering is.

Cost fix, same worker: writing the decoys with a seeded script instead of a model session each cuts a full run from 24,432 model calls (4,041 diagnoses + 31 repairs, x3 arms x2 runtimes) to 432, about 9 h of wall time including two 2 h gaps.

**Why:** a NOTES-arm result on this bank cannot be quoted as "found the needle among 4,000 look-alikes".

**How to apply:** any MULTI5 brain-vs-notes result names this limit. A later bank that wants a true haystack gives decoys ids from the same space as real tasks and real-sounding findings, then reruns the classifier check (it must fall below 0.75). Related: [[multi_harness_brain_arm_is_bm25_only_no_vectors_no_graph_2026_11_09]].

