---
name: frontier_gate_read_an_offloaded_audit_path_every_dl_row_shut_2026_11_16
description: "Why did the frontier gate say every deep-learning row was 'not audited yet'? Its audit path pointed at a worker folder that had been moved into the repository; opening a missing file returned nothing, so every row read as unaudited. Fixed by globbing audits/*/AUDIT_*.jsonl."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

The frontier gate (the script that decides which open-problem rows are ready to work on or post) closed all 68
deep-learning rows, 61 of them as "deep-learning row not audited yet", although an auditor had audited twenty of them
a month earlier.

Cause. The gate and the board builder both named the auditor's output by an absolute path into a worker's scratch
folder. When finished worker folders were moved into the repository (the rule that AI outputs live on GitHub, not on
the laptop), the file moved to `audits/<auditor>_<date>/` inside the problem collection. The reader opened a missing
file, got nothing, and raised no error, so every row read as unaudited, and a board rebuild would have printed no
auditor lines.

Fix. Both readers now glob `audits/*/AUDIT_*.jsonl` (the old path kept as a fallback), so a later audit wave lands by
dropping its file beside the others. After the fix the twenty audited rows show only "literature check is N days old";
two rows outside the audited twenty still show unaudited, as they should; the gate's tests pass. In the same session
the gate crashed on an hour-only timestamp ("23:3x"), now read with the minute digit as 0.

Mechanism for the next reader: moving worker folders silences any live tool that holds an absolute path into them,
without an error. Before trusting a gate or a board that reads a worker's output, check the path exists, not just that
the code runs. A scan found about 2,100 lines in the repository naming worker folders; nearly all are archived worker
scripts naming their own folder, and these two were the only live readers.
