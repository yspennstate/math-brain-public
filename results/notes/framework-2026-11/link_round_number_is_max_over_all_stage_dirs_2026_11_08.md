---
name: link_round_number_is_max_over_all_stage_dirs_2026_11_08
description: "[VERIFIED] New math-store link round overwrote an old one / skipped as already landed: picked the round number with a stage_r5* glob that missed r6xx; take the max over ALL stage_r* folders and refuse an existing folder"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T22:53:36+02:00
  status: provisional
  evidence: ""
---

On 8 Nov my math-store link round for the one isolated served claim was staged as `stage_r600` in
`math-brain-build/local/links_20261028_c462/`. Rounds there had already run to r612. I had picked the next number
with `ls -d stage_r5* | sort -V | tail -1`, and that glob cannot see a folder named r6xx. So the new staged_edges.jsonl
wrote over round 600's file. land_links.py then skipped my two edges as "already landed", because their round name was
already in the landed record.

Nothing in the store was lost: round 600's 74 edges had landed long before. I rebuilt the staged file from the store
using that round's landed ids (verify: present 74 bad 0) and left RESTORED_FROM_STORE.txt next to it. My edges went in
as stage_r613 and verified present 2 bad 0.

**How to apply:** pick a new round number as the maximum over every `stage_r*` folder, parsed as integers, for example
`ls -d stage_r* | sed 's/.*stage_r//' | sort -n | tail -1`. Never use a glob tied to the current hundred. Before writing,
check that the target folder does not exist, and refuse if it does. The same applies to any numbered batch folder
(push_rNNN, land_rNNN.sh). Ledger row 59 of IMPROVEMENT_LEDGER.jsonl records it.

