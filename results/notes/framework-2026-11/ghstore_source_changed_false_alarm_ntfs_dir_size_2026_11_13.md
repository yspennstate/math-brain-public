---
name: ghstore_source_changed_false_alarm_ntfs_dir_size_2026_11_13
description: "[VERIFIED] ghstore put says 'source changed' on a DIRECTORY with nothing writing? NTFS dir st_size 0 -> 1048576 after listdir; signature() now ignores dir size on Windows"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T09:08:56+02:00
  status: provisional
  evidence: ""
---

gh_offload / ghstore put on Windows refused a whole folder with "source changed: <some directory>" although nothing touched it (07-20 codex worktree archive, twice).

Cause: an NTFS directory's st_size reads 0 from lstat until the directory has been listed, then 1048576. ghstore stats every entry, packs, and then re-stats each entry (line ~555) and the whole tree (scan before/after); signature() included st_size, so any directory that was first stat'ed before its listdir failed the comparison. Files are unaffected.

Fix (13 Nov 09:1x, an agent): signature() zeroes st_size for directories on Windows only; files keep size + mtime; POSIX unchanged. Backup ghstore.py.bak_dirsize_1113. Tested: a directory's signature is equal before and after listdir; a file's signature still carries its size.

How to apply: a "source changed" on a directory path (not a file) with no writer around is this, not a real change. A "source changed" on a FILE is still real - find the writer before rerunning.

Status: verified on one folder; the 07-20 rerun is the end-to-end check.

