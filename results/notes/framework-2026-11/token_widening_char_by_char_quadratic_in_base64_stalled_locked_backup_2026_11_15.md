---
name: token_widening_char_by_char_quadratic_in_base64_stalled_locked_backup_2026_11_15
description: "[VERIFIED] Brain backup packer crawling at ~4 KB/s on transcripts? build.scanner_spans widened every match one char at a time - quadratic inside pasted-image base64 (1.06 MB line 665 s). Fixed with token runs + bisect, byte-identical on 6,036 lines, 180x faster"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T20:26:39+02:00
  status: provisional
  evidence: ""
---

Symptom: full_brain_backup.py (locked-bucket pack, 15 Nov) sat for hours on one transcript; the .part stopped growing. prof_redact.py found the time in build.redact -> scanner_mask -> scanner_spans: for each regex match it walked left and right one character while the neighbour was a token character. A pasted image is one long base64 run, so every match inside it walked the whole run: O(matches x run length). One 1.06 MB line took 665 s; known_secrets() spent 505 s in the same loop.

Fix (build.py, 15 Nov ~20:2x, an agent): find the maximal token runs once per text with one regex ([A-Za-z0-9_\-.+/=]+, equal to _TOKCH), and widen each match by bisecting the run that holds t[a-1] and t[b]. Runs are computed lazily on the first surviving match, so texts with no hit pay nothing.

Checks: old vs new spans on 952 + 4,842 + 242 transcript lines (up to 2 MB) and 20,010 random edge-case strings: all identical. Timing on the long lines: 1,244 s old vs 6.8 s new.

Lesson: a 'widen to the surrounding token' loop is quadratic whenever the text can hold one giant token. Look for it in any redactor or scanner that runs over transcripts, which carry base64 images. known_secrets() was still 580 s after the fix, so something else costs time there (file reads on a slow disk); it is paid once per packer start.

Related: [[packer_json_redump_and_scanner_named_files_block_a_locked_backup_2026_11_15]] [[a_retention_lock_freezes_any_secret_inside_scan_before_locking_2026_11_14]]
