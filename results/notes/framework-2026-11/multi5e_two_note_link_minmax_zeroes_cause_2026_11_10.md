---
name: multi5e_two_note_link_minmax_zeroes_cause_2026_11_10
description: "[PROVISIONAL] Why recall misses the second note of a join (MULTI5E): min-max scaling of a two-note link list gives the cause zero credit; a co-touch walk lifts dummy calibration 11->18/30 offline, held-out replay pending"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T02:34:36+04:00
  status: provisional
  evidence: "codex_fleet/20261108_pro/workers/MULTI5E-RECALLDIAG/REPORT.md"
  originSessionId: 472b1d4f-77c3-4c94-8b40-709cb36c538f
---


In the MULTI5 dummy calibration, all ten joins have a private co_touch edge of weight 1.0. Eight seed the link walk: cause PPR rank 2 with score 0.33331298828125 becomes zero after min-max normalization of the two-note list. Seven corresponding causes are missed at top eight; one succeeds through other signals. Two joins miss the landing before the link seed cutoff. The synthetic control independently reproduces the zero-credit mechanism.

A preregistered first-four unique strong co_touch walk improves complete task reach from 11/30 to 18/30, with an independent repeated-default disagreement count of 0. Joins improve 1/10 to 8/10; haystacks remain 10/10; paraphrases remain 0/10. Six paraphrase golds are outside semantic top 60, while four enter but lose in fusion; t17 moves semantic 7 to final 51. All 30 default result lists reproduce the host source exactly.

The existing DIAG30–32 historical receipts cover 30 runs and 2176 question groups. The default graph has zero co_touch edges, so this typed proposal is unchanged there; top-eight gold counts stay 515 with zero repeated-default noise. This is only a scoped invariance result. Fresh host replay with the private calibration corpus is pending, no live code changed, and no model/scored accuracy claim follows.

Related: [[diag36_graph_dial_holds_tuned_gain_reverses_held_out_2026_11_09]], [[recall_ab_separate_passes_read_moving_index_2026_11_09]], [[multi_harness_brain_arm_is_bm25_only_no_vectors_no_graph_2026_11_09]]. Do not supersede those notes: this extends the private semantic/link-enabled calibration diagnosis, with the fresh held-out qualification still open.

