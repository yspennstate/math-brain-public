---
name: git_bash_tar_reads_c_colon_as_remote_host_use_relative_path_2026_11_16
description: "[VERIFIED] Git Bash tar on a C:/ archive path fails 'Cannot connect to C: resolve failed' and leaves a stale partial extraction looking complete; cd into the dir and pass a relative name (or --force-local), then count files"
metadata:
  type: feedback
  created: 2026-11-16
  created_at: 2026-11-16T12:05:10+02:00
  status: provisional
  evidence: ""
---

16 Nov 2026 (an agent): tar tzf/xzf on C:/.../s38full.tgz failed silently inside a script; the S38M07 frozen fixture held 55 of 331 files from an earlier extraction of a truncated download, and stop-study printed 0 routes. Fixed by cd + relative path. **Why:** tar treats host:path as a remote archive. **How to apply:** in Git Bash never hand tar a drive-letter path; after any extraction, compare the file count with tar tzf | wc -l. Related [[checklist_task_20261115_024]].
