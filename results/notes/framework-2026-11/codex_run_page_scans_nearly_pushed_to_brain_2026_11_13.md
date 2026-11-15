---
name: codex_run_page_scans_nearly_pushed_to_brain_2026_11_13
description: "Archiving a Codex run folder? Runs rasterise source papers into data/*/page-*.png - copyrighted scans; drop them before push"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T04:01:55+02:00
  status: verified
  evidence: "arch_d0037a.log staged 7 page-*.png; push killed before commit; archive_run.sh excludes added"
---

Codex open-problem runs on Mac mini 1 sometimes rasterise the papers they read into page images under data/ (D0037A, 13 Nov:
data/helson_sarason/page-06..12.png, scans of the Helson-Sarason paper). archive_run.sh excluded sources/, literature/ and *.pdf
but not page images, so the archive staged 7 copyrighted page scans for a brain push. Caught in the staged-file list before the
commit (the push was killed by PID before its "pushed" line; the scans never reached GitHub), deleted locally, re-pushed without.

How to apply: before any archive or push of a run folder, read the staged file list for page-*.png, page-*.jpg, scans/ or other
rasterised source pages and drop them; archive_run.sh now excludes 'page-*.png', 'page-*.jpg' and scans. Originals stay on mini1.
Related: [[e0018_switching_rate_instability_two_intervals_resolved_unrestricted_2026_11_13]] (same archive pipeline).

