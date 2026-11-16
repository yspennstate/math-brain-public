---
name: an_ab_whose_harness_hardcodes_the_tool_path_compares_nothing_2026_11_08
description: "[VERIFIED] Before/after eval of a tool version: nav_eval.py hard-codes nav_query's path, so copying old/new nav_query beside it ran the SAME version twice; check which file the harness imports/execs before trusting an A/B"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T13:11:39+02:00
  status: provisional
  evidence: ""
---

8 Nov 12:5x: I sent two peers 'stem patch drops nothing, 8/10 same as before' from an A/B where nav_eval.py (rank 7 folder) has Q = r'<folder>/nav_query.py' on line 3, so both arms ran the patched copy. Redone with the path pointed at each version (before ff4a25d82 / after 99e932371): live map 9->9, old map 9->8, one question moved to the top-5 edge. Correction sent 13:0x.

**Why:** an A/B run through a harness that resolves the tool by an absolute path measures one arm twice and looks like 'no change'. That is the most flattering wrong answer, and it got sent to peers before anyone tried to break it.
**How to apply:** before comparing versions, grep the harness for the tool's path or import, and print each arm's file hash in its output. Two arms that give identical per-question lines are a red flag, not a result. Related: [[report_surprising_number_before_break_it_2026_07_12]].
