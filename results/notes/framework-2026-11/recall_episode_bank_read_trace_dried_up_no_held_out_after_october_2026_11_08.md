---
name: recall_episode_bank_read_trace_dried_up_no_held_out_after_october_2026_11_08
description: "[VERIFIED] Held-out recall test from real use? retrievals.tsv (file Reads) logs 3-13 rows/day since mid-Oct; 1 usable episode since 30 Oct of 139; count the held-out side first"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T06:14:42+02:00
  status: provisional
  evidence: ""
---

The real-prompt episode bank that eval_prompt_recall_fullstack.episodes() builds (ground truth = the memory files a session
Read, from dreaming/retrievals.tsv) cannot test anything landed after about mid-October 2026. Measured 8 Nov 2026
(recall_xc_1d48/dev/semr/heldout_why.py, output beside it): retrievals.tsv logs 3-13 rows a day from 3-8 sessions since
mid-Oct (August had hundreds a day), 6 sessions first seen since 30 Oct, and 1 of them passes the episode filters (2..25
reads and a plain-language prompt of 6+ tokens). The prompt ledger meanwhile holds many November prompts. Agents now take memories
from recall output, --id and node views instead of Reading the files, so the Read trace has dried up.

Consequence: a "held out from 30 Oct" split on this bank has n = 1. The paired semantic-rescue run of 8 Nov (139 episodes)
would only have measured August-era episodes, which the lane's own tuning may have seen.

How to apply: before building a held-out recall test from real use, count the bank's episodes on the held-out side first
(seconds, no brain import: heldout_count.py). For post-October ground truth use another signal: a recall followed by a
node/--id/Read of a memory in the same session's transcript, or the brain_graph live judgments; size it from file tails, not
a full transcript scan. Status: verified (counts), the cause (agents stopped Reading memory files) is inferred from the
counts, not traced in transcripts.

