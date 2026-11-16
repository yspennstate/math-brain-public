---
name: grep_p_needs_utf8_locale_verify_read_every_miss_2026_11_14
description: "[VERIFIED] Push verify says 0 of N though the push landed? In this Git Bash grep -P exits 2 ('supports only unibyte and UTF-8 locales'), so grep -q -P ... || echo MISMATCH marks every file missing"
metadata:
  type: feedback
  created: 2026-11-14
  created_at: 2026-11-14T22:59:48+02:00
  status: provisional
  evidence: ""
---

In Git Bash on this workstation (14 Nov 2026) grep -P refuses to run: 'grep: -P supports only unibyte and UTF-8 locales', exit code 2. Inside a check like grep -q -P "^$sha\t$path" remote.tsv && ok=... || echo MISMATCH, exit 2 reads the same as no match, so a verify loop reported 'verified 0 of 950' (push 257) and 'still to push 971 of 971' (push 261) while 480 of the files were on main. The push was fine; the check was blind.

**Why:** a check that cannot run must not read as a failure of the thing checked (or, worse, as a pass); exit 2 from grep is an error, not a miss.

**How to apply:** do not use grep -P in Git Bash scripts unless LC_ALL=C.UTF-8 is exported; compare blobs with git ls-tree + git hash-object in Python (fillq_ctl/verify_paths.py REPO REF PATHLIST) or with git rev-parse REF:path per file. When a verify reports 0 of N, test the checker on one known file before believing it. Related: [[a_card_that_drops_input_must_name_it_2026_11_14]].
