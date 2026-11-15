---
name: timed_out_audit_inherited_the_previous_report_2026_11_12
description: "[VERIFIED] Paper audit shows a fresh verdict but the reader never finished? A run killed at its time limit picked up the previous run's REPORT.md in the same folder"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T18:11:00+02:00
  status: provisional
  evidence: ""
---

paper_audit.py run killed at its 80-minute limit (rc -9) still logged report_ok and wrote audit_index.json, because the REPORT.md it checked was the previous read's, left in the same folder. Seen 12 Nov 2026 on the margin paper: index row said MINOR EDIT / 5 must for text sha 5b42... that no reader had finished; W43 would have passed a release on it. Fixed 18:1x: success needs getmtime(REPORT.md) >= run start. General rule: an output file only proves a run if it was written after the run started (or the folder is cleared first); rc -9 plus a pre-existing output is the shape. Also: 80 min is short for a 1300-line paper at high effort (2 of 3 runs hit it); resume the killed session with --resume rather than starting cold. status: verified. Related [[paper_audit_dies_in_seven_seconds_on_the_fable_limit_2026_11_12]].
