---
name: a_scan_whose_tool_is_missing_reports_zero_hits_2026_11_15
description: "[VERIFIED] Secret scan says hits_total 0 before a bucket lock? Check the tool ran: on 15 Nov the rg prefilter was not installed (rc 127), the window file was empty and the exact scan printed 0 hits over 12.46 GB it never read"
metadata:
  node_type: memory
  type: feedback
  created: 2026-11-15
  created_at: 2026-11-15T02:29:11+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-15T09:40:10.725Z
---

On 15 Nov, scan_fast.sh piped rg output into the exact scanner before locking a cloud archive bucket. rg is not on this workstation's PATH (no ripgrep binary at all), so rg exited 127, windows.bin was 0 bytes and scan_windows.py printed 'hits_total 0'. The script kept going because nothing checked rg's exit code. A retention lock cannot be undone, so a fake clean would have frozen anything inside for a year.

**Why:** a downstream step that counts hits in its input reports zero when the input is empty, for any reason. Zero hits and zero bytes scanned look the same unless the scanner prints what it read.

**How to apply:** a scanner prints bytes scanned and files opened next to the hit count, and the caller refuses a clean result whose bytes scanned is far below the bytes on disk, or whose upstream tool exited non-zero (set -o pipefail, check rc). Run a positive control through the same pipeline, not a separate one. Replacement used: scratch area scripts/scan_py.py, pure Python, reads plain, .gz, .tar/.tgz members and gzip inside tar, controls passed both ways. Related: [[an_absence_check_against_a_missing_reference_passes_2026_11_14]], [[a_retention_lock_freezes_any_secret_inside_scan_before_locking_2026_11_14]]. Method drawn from this (15 Nov nap): [[method_a_check_prints_what_it_read_beside_its_verdict_2026_11_15]].
