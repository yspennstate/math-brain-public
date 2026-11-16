---
name: python_isolated_flag_hides_user_site_packages_2026_11_16
description: "[VERIFIED] python -I (advised for scripts reading downloads) also drops the user site-packages: pypdf etc. fail with ModuleNotFoundError; python -P keeps the script dir off sys.path and keeps user packages"
metadata:
  type: feedback
  created: 2026-11-16
  created_at: 2026-11-16T15:29:35+02:00
  status: provisional
  evidence: ""
---

16 Nov 2026, an agent: a catalogue recheck run as python -I lost 24 of 45 rows to ModuleNotFoundError: pypdf (installed in the user site). -I implies -E -s -P; -s removes the user site. When the aim is only to stop a planted module next to the script or in cwd, python -P is enough. Same family as the import-check-before-a-long-run reflex.

**Why:** the failure is per row and caught, so it looks like network errors until the errors are tallied.
**How to apply:** run download-parsing scripts with python -P, or prove the imports under the exact flags first (python -I -c 'import pypdf'); tally error types after the first rows.
