---
name: tool_scoped_reflexes_held_out_0p348_to_0p357_3pct_fires_d7_35_2026_11_08
description: "[VERIFIED] A little (8 Nov): D7 #35 per-reflex tool scope, chosen on fires before 1 Nov and scored after, removes 73 of 2,221 judged fires at 0.10 on-domain and lifts precision 0.348 to 0.357; parked as W112 (j)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:50:19+04:00
  status: verified
  evidence: "d7_35_reflex_precision_by_tool_2026_11_08.py, 4,442 judged fires joined to instinct_fires.tsv"
---

Would letting a reflex name the tools it fires on raise precision, as 1000-ways D7 #35 (tool-scoped triggers) asks? A little, and the gain holds out of sample, but it is small. Measured 8 Nov by an agent. instinct_prime has no per-reflex tool scope today; the only tool split is the act/write proxy used for context damping.

Method: I joined every hand-judged fire in judged_nightly.jsonl to its instinct_fires.tsv row by reflex and second (4,442 of 5,042 joined). The tool comes from the keys the logged input starts with; the log cuts inputs short, so json.loads fails on most and reading keys is needed. By tool: Bash 1,198 of 3,706 on-domain, Write 126 of 550, Edit 54 of 128, prompt 15 of 58.

- In sample, 23 reflexes are judged 8+ times on two tools, and several split sharply: voice_human Bash 8/38 vs Write 22/31, heredoc_verbatim_surgery Bash 54/88 vs Write 0/12, duration_question_needs_a_rate Bash 0/20 vs prompt 8/11, the_last_hard_mile Bash 4/45 vs Write 6/11. Dropping each tool under half its reflex's best removes 401 judged fires and loses 31 on-domain ones.
- Held out: I chose the pairs on fires before 1 Nov 02:29 (6 pairs) and scored the later 2,221 fires. Scoping removes 73 of them, only 7 on-domain (0.10 against 0.348 overall). Precision rises from 0.348 to 0.357, and 7 of 773 on-domain fires are lost.

So the removed fires are clearly worse than the rest, but they are 3% of fires. Judged fires are a stratified sample, so the live share may differ. Parked as W112 (j): a tools field per reflex, filled from the held-out pairs, off by default. It is a hook change and waits on the author. Related: [[a_fifth_of_reflex_fires_hit_two_codex_contexts_2026_09_24]], context, not tool, as the other axis of the same narrowing. Also [[low_precision_danger_reflexes_9pct_of_shown_fires_6_of_1338_hits_2026_11_08]]: W112 (g) mutes a whole low-precision reflex, while this narrows a reflex by tool, and the two stack.

Check: d7_35_reflex_precision_by_tool_2026_11_08.py [min_per_tool], read only. Control: planted command and old_string inputs are named Bash and Edit, and the join must match at least half the judged rows inside the fires log.

