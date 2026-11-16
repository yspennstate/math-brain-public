---
name: sed_on_next_prefix_rewrote_all_history_lines_2026_11_13
description: "[VERIFIED] sed s/^NEXT: .*/ on a STATE.md whose old NEXT lines are history rewrote all 108 of them; recover from the session transcript, never global-sed a shared prefix"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T22:40:39+02:00
  status: verified
  evidence: "agent_run/STATE.md 13 Nov 22:23: 108 NEXT lines rewritten; 170 recovered from transcript"
---

A `sed -i 's/^NEXT: .*/NEXT: (new)/'` on a loop's STATE.md rewrote every dated NEXT line in the file (108 of them) to the same new text, because the file keeps old NEXT lines as history and the pattern is anchored on the prefix, not on the last line. Seen 13 Nov 2026 22:23 in agent_run/STATE.md (no backup, not a git tree).

Recovery that worked: walk the session transcript JSONL for every distinct "NEXT: ..." string (sed replacement bodies, echo >> lines, lines in tool results) and append them, in transcript order, under a dated "recovered" heading; keep one current NEXT line at the end. Positions in the file are lost; the text is not. The scan of a 200+ MB transcript takes over two minutes on the workstation, so run it in the background, not under `timeout 110`.

How to apply: to change the current NEXT line of an append-only log, delete all `^NEXT: ` lines and append the new one (`grep -v '^NEXT: ' f > t && printf '%s\n' "$N" >> t && mv t f`) only when old NEXT lines are not history; when they are, append a new line and leave the old ones alone. Never a global sed on a prefix that history lines share. Copy the file aside before any in-place edit of a log with no other copy.

