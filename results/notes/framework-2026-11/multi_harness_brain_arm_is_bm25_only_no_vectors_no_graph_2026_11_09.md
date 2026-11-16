---
name: multi_harness_brain_arm_is_bm25_only_no_vectors_no_graph_2026_11_09
description: "[VERIFIED] No: the MULTI3/4/5 BRAIN arm is BM25 only (vectors off, test notes not in the graph); MULTI5 recall 10/30 (haystack 10, paraphrase 0, join 0)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T23:17:26+04:00
  status: provisional
  evidence: "MULTI5-BUILD evidence/calibration.json; harness/brain_cli.py lines 11-14"
---

No (MULTI5 host calibration, 9 Nov 23:16): the BRAIN arm of the MULTI3/4/5 handoff harness is a lexical index, not the brain. harness/brain_cli.py points spread_recall's EMB and EMB_AUTHORITY at files that do not exist ("vectors-not-built"), so both semantic channels are off, and the session-1 notes are indexed by BM25 only and never enter the graph (ARMS.md: "New notes receive lexical indexing but are not integrated into the graph"). The read-only graph knows none of the test's memories.

Measured on the MULTI5 bank with dummy session-1 notes, full repair prompt, top 8 (evidence/calibration.json in codex_fleet/20261108_pro/workers/MULTI5-BUILD):
- haystack (4,000 decoys): recall 10/10 at rank 1, scripted grep 0/10 (first grep prints 37 KB against the 8,192-byte budget)
- paraphrase (no shared content word): recall 0/10, grep 0/10
- join (cause note shares no word with the prompt): recall reaches the landing note at rank 1-3 on 10/10 and the cause note on 0/10; grep 10/10
Recall 10/30 is under the builder's 15/30 gate, so the bank as built cannot show a brain advantage on paraphrase or joins. That is a harness limit, not a brain result.

**Why:** MULTI4's "brain ties grep 30-30" compared BM25 with grep. The brain's lanes for wording-free and linked recall (vectors, graph and sidecar links) were never on.

**How to apply:** before quoting any MULTI-series BRAIN number, check that the arm gives the test's new memories what the live brain gives a new memory within the gap: a vector (the fresh overlay) and links (sidecar co-touch, [[ ]] mentions). Otherwise label the result lexical-only, a partial-brain result under the brain-test rules. Related: [[multi4_brain_ties_grep_notes_30_30_none_0_2026_11_09]], [[diag36_graph_dial_holds_tuned_gain_reverses_held_out_2026_11_09]].

