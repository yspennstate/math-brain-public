---
name: project_review_due_lines_share_one_line_per_call_2026_11_12
description: "Hot hook printed one 'Hourly review N is due for <project>' line per project (eight an hour for one session, 60,000 chars in 27 h)? Since 12 Nov the reviews due in one call share one line naming each project; one alone keeps the old sentence. Stamps, acks and the line budget unchanged. Tested old against new 14 of 14; seen at a receiver 12 Nov 02:00 and 02:09"
metadata:
  node_type: memory
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T01:18:18+02:00
  status: verified
  evidence: agent_run/project_context/test_combined_result.txt; ledger row of 12 Nov (f); the one line for 8 projects arrived in session agent at 02:00 and 02:09 on 12 Nov (PreToolUse context in its transcript)
  originSessionId: agent-4b92-4833-bcc3-a3ab8aa26344
  modified: 2026-11-12T00:10:50.799Z
---

The hot hook (`~/.brain-framework/runtime/project_memory_hot_hook.py`) tells a session about every project whose hourly review it has not acknowledged. A session is offered every project one of its prompts was ever classed to, and each project got its own line carrying the same 150-character command. One session measured eight such lines an hour: 288 lines, about 60,000 characters, in 27 hours.

Since 12 Nov 2026 the reviews that are due in one call share one line:

    [project-context] Hourly reviews are due for 8 projects (occurrences in brackets): live-brain (979), unknown (...), ... Read one with: "python" "...project_memory_cli.py" read-latest --project <name> --session <id>

One review alone keeps the old sentence word for word. Every due review is still named and still stamped as delivered, an acknowledged window is still left out, a failed attempt still gets its own "is unresolved" line, and a withheld line is still not stamped (the hook's invariant against silent retirement). The line budget counts the combined line as one.

Measured on a signed throwaway cache with eight due reviews: 8 lines and 2,552 characters before, 1 line and 482 after. `agent_run/project_context/test_combined.py` runs each case on the old and the new file (14 of 14); the hook's own suite gives 50 passed on both. Backup `project_memory_hot_hook.py.bak_combined_20261112`.

Seen at a receiver: session agent got "Hourly reviews are due for 8 projects (occurrences in brackets): unknown (1000), shared-brain (1000), ..." as one line at 02:00 and again at 02:09 on 12 Nov, so the status is verified. The index row in MEMORY.md may still say provisional until the dream rewrites it.

`project_memory/hook.py` `_render_hot` (the lifecycle path) got the same rule at 01:25 the same night. Not changed: the reviews themselves are still far too long to read (live-brain: 56 shards of about 48,000 characters). The reader crash that made them unreadable at all is [[project_review_reader_crashed_on_cp1252_again_after_the_wrapper_switch_2026_11_12]].

