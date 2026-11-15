---
name: stale_paper_pdf_scan_commit_times_and_the_mirror_2026_11_13
description: "[VERIFIED] Posted paper PDF older than its referee-corrected tex? Compare last-commit times of PDF vs .tex in blob-less clones (S/stale_pdf_scan.py); 4 papers were stale on 13 Nov, and the math-brain-public mirror carried the stale copies too"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T18:10:20+02:00
  status: provisional
  evidence: ""
---

13 Nov 2026 17:44, an agent. Scan of the 100 newest public repos: for each committed PDF with a .tex beside it, compare git log -1 commit times (blob-less bare clones, no REST API). Real hit: trace-reinforced-ants-dead-branches (PDF from a52b6c0, referee corrections 0c93518) - fixed GitHub af9adbf, Zenodo 24201434. Earlier the same day arc-transitive, stationary-cover and variation-threshold had the same fault. False alarms: figure PDFs (fig_density, alpha_curve, ratio) and a PDF whose own tex never changed while a sibling tex did; read the flagged tex diff before acting. AFTER fixing a paper repo, fix the math-brain-public mirror too: it held the old PDFs of three of the four (fixed de7ddcba); mirror copies are built without the email line (source repos keep it), so rebuild with that line removed and check the text diff is only the email. scan_secrets.py refuses shallow clones with --range: scan the files as positional paths. Related [[final_sha_pdf_label_does_not_prove_build_commit_2026_11_13]].
