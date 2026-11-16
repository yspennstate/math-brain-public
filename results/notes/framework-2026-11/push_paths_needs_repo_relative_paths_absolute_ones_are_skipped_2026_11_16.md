---
name: push_paths_needs_repo_relative_paths_absolute_ones_are_skipped_2026_11_16
description: "[VERIFIED] push_paths.sh given absolute C:/ paths prints 'Ignoring path' for each and 'nothing to push' - it pushed nothing; pass paths relative to the repo"
metadata:
  type: feedback
  created: 2026-11-16
  created_at: 2026-11-16T11:17:11+02:00
  status: provisional
  evidence: ""
---

push_paths.sh cds into the repo and stages with git update-index, which refuses an absolute path (C:/Users/...) with 'Ignoring path <p>' and then reports 'nothing to push: every path already matches origin/main'. That last line reads like success. Seen 16 Nov 2026 on the S39 harvest (45 files); rerun with repo-relative paths pushed them as a01e01050539.

**Why:** a push that silently did nothing would have let the local copies be deleted as 'on GitHub'.
**How to apply:** cd to the repo and pass relative paths (find <dir> -type f from the repo root); after any push, look for 'pushed N path(s)' with N equal to what you sent, never just the absence of an error.
