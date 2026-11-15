---
name: mesh_wait_victims_hide_reader_2026_11_12
description: "Mesh commit waits show only waiting claim and release processes instead of the reader"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:18:13+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: At 01:24 on 12 Nov 2026 a claim waited 17.11 seconds for COMMIT and rolled back; releases waited 11 and 16 seconds to open. The slow log showed waiting mesh commands, but the roughly 24-second reader was not identified.

Why it happened: A rollback-journal COMMIT waits for readers, including scripts opening SQLite directly. The old log observed mesh calls, not every process holding the file.

**Why:** A list of slow writers identifies victims, while even a file-holder list can include those same victims.
**How to apply:** Compare the new holders lines (default threshold 5 seconds) with same-time open_wait and commit_wait entries; do not name workspace.py as the original culprit without evidence.

[[mesh_slow_log_names_who_has_the_file_open_2026_11_12]]
[[workspace_report_reads_mesh_messages_newest_first_in_chunks_2026_11_12]]

Drafted by Codex worker W06 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

