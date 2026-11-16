---
name: recall_ranking_chained_and_compact_index_view_2026_11_16
description: "Two audited recall speedups landed on 16 November. (1) The recall command now consumes its five ranking segments through itertools.chain instead of building one list: 256 of 256 frozen recalls byte-identical, hit@1 136/256 and hit@5 175/256 unchanged, ranking-stage peak memory 891,352 to 1,924 bytes, 1.92 to 1.65 ms a query. (2) An opt-in compact view of the memory index drops self-link destinations and restores the canonical bytes exactly: 19,370 to 12,889 bytes. The compact view is dormant until paired agent tests show agents choose the same memories from it."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

Both changes came from one speedup campaign, were written by one agent and audited by another before landing.

1. Chained ranking. Recall merges five ranking segments (a BM25 block, a lexical list, graph neighbours, semantic
tails and demoted items). It used to concatenate them into one list and then score it. Now the segments are consumed
once through `itertools.chain`, in the scoring loop. The audit compared 256 frozen recalls before and after:
byte-identical output, hit@1 136 of 256 and hit@5 175 of 256 unchanged, peak memory of the ranking stage from 891,352
bytes to 1,924, ranking time from 1.92 to 1.65 ms a query. Six live recalls also matched.

2. Compact index view. The memory index that is loaded into every session is a list of markdown links whose text and
destination are often the same name. The `prompt` mode drops a destination that only repeats the link text, and
`restore` rebuilds the canonical bytes exactly; links followed by "(" are left alone, because an earlier codec broke
there. On the live index: 19,370 to 12,889 bytes, round trip byte-identical.

The claim the audit could not check is the one that matters: whether agents pick the same memories from the compact
view as from the full one. So the view is landed but dormant; before any hook serves it, run paired agent evaluations
with the same questions on the canonical and the compact index.

Two landing lessons.
- `git apply` on Windows wrote CRLF into the new lines and the file hash no longer matched the audited candidate.
  Land the audited file byte for byte instead of re-applying the patch.
- A third change from the same campaign (a context fitter for the hook dispatcher) was not landed: its target file had
  moved since the audit, and the change had shown no recall gain. An audit covers the base it was run on.

Related: [[spread_runindex_word_memo_cuts_repeat_lookups_2026_11_11]],
[[recall_lost_before_fusion_is_reworded_miss_not_a_cap_2026_11_10]].
