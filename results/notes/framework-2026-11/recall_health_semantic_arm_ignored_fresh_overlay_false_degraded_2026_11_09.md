---
name: recall_health_semantic_arm_ignored_fresh_overlay_false_degraded_2026_11_09
description: "[VERIFIED] No (9 Nov): check_brain_recall_health said SEMANTIC DEGRADED (306 missing) but the fresh overlay covered all but 11 system files; arm now counts the overlay, control still trips"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T03:32:40+04:00
  status: verified
  evidence: "vec_cover.py 03:3x: 51,083 files, sidecar 50,553, overlay 1,097, 11 in neither; A/B live DEGRADED vs candidate HEALTHY; 30-file control trips; becafc553b"
---

Is semantic recall really degraded when check_brain_recall_health.py says "SEMANTIC DEGRADED - 306 memories have no vector"? No, not on 9 Nov 03:3x. The check's semantic arm read only .embedding_status.json. It never counted memory_embeddings_fresh.npz, the overlay that fresh_vectors.py rewrites every 15 minutes and that brain.py has read since 13 Oct (R13).

On this machine the full sidecar is rebuilt only by the nightly dream (run_dream.py, the embedding refresh+publish step), so `missing` grows all day. The arm's "expected lag" rule was written for the Windows box's 3-hourly refresh (behind <= 25, age <= 6 h) and fired red all day here. Its fix text still pointed at the Azure box.

Measured (vec_cover.py): there are 51,083 memory files. The live sidecar b24a0a59 holds 50,553 rows and the overlay 1,097. 530 memories are not in the sidecar, and only 11 are in neither: the all-caps system files (AUTOBIOGRAPHY, CONSCIENCE, MISTAKES and so on). Of the 509 stale (edited) rows, the overlay holds 462; the other 47 still use their older sidecar vector.

The fix (an agent): when the overlay is under an hour old, the arm counts memories that neither the sidecar nor the overlay covers, skipping all-caps names. It passes at <= 25 uncovered with a sidecar under 48 h and a clean shape, and otherwise prints the uncovered count and points to fresh_vectors.py and run_dream.py.
- A/B: the live check said DEGRADED and the candidate HEALTHY (0 uncovered, 47 on an older vector).
- Control: a fake memory dir of 30 uncovered files still trips DEGRADED with "30 have no row in the fresh overlay".
- Backup: check_brain_recall_health.py.pre_overlay_20261109. Mirrored to the private repository: 12_cognitive_architecture/dreaming as becafc553b.

No scheduled job runs this check. Agents run it by hand while auditing (FULL_BRAIN_MAP.md lists it), so the cost of the false red was misdirected audits, not missed alarms. One gap remains: the printed sidecar age comes from the status file's checked_at (9.2 h) while the real age was about 16 h.

Related: [[recall_enumeration_overlay_closes_vector_gap_in_minutes_2026_10_31]], [[fresh_recall_misses_were_wording_not_embedding_lag_with_vectors_d3_44_2026_11_02]], [[a_red_that_is_always_red_stops_being_read]], [[mac_embedding_generations_never_pruned_21_files_1p34_gb_pruner_unwired_2026_11_01]].

Closed 03:3x: the arm now takes the sidecar age from built_at against now (15.9 h, not the status file's 9.2 h).

Correction 03:3x: the 47 'edited, no overlay row' are not stale vectors. All 47 were touched by one 22:05 (8 Nov) sweep that left their canonical text unchanged; fresh_vectors.py --dry finds 1,101 memories without a current sidecar row (by text hash) and all 1,101 have overlay rows. The status file counts stale by stat, the recall path by text hash. So semantic coverage was complete apart from the 11 all-caps system files.
