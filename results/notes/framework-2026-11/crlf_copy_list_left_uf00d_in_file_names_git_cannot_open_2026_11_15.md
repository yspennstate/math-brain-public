---
name: crlf_copy_list_left_uf00d_in_file_names_git_cannot_open_2026_11_15
description: "[VERIFIED] git hash-object 'No such file' on a file ls shows? A CRLF copy list read by a bash loop left a CR on each name, stored as U+F00D (dir shows '?'); strip CR before copying"
metadata:
  type: feedback
  created: 2026-11-15
  created_at: 2026-11-15T15:36:13+02:00
  status: provisional
  evidence: ""
---

15 Nov 2026, math-brain-public B13: the binary copy list b13_bin.tsv had CRLF line ends; a bash while-read loop copied each binary to a destination ending in a carriage return. Git Bash stores that CR in the Windows name as U+F00D, so ls and dir list the file (dir prints a trailing ?) but git hash-object and ls on the clean path both say No such file. 51 files in results/ had it; none reached origin (git ls-tree found 0). Fix: rename with fix_names.py (rstrip of \r, \n, U+F00D, U+F00A), and in any copy loop use tr -d '\r' on the list or read with IFS=$'\t' after stripping. **Why:** the push stopped at the 15th path with hash-object rc 128 and the cause was invisible to ls. **How to apply:** when a file is listed but cannot be opened by name, print repr(os.listdir()) before anything else. Related: [[public_push_resume_by_blob_compare_chunks_of_200_2026_11_15]].
