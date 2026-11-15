---
name: final_sha_pdf_label_does_not_prove_build_commit_2026_11_13
description: "[VERIFIED] A PDF named final_<sha>.pdf is not proof it was built from <sha>: three papers (arc-transitive-edge-heat, stationary-cover-time-four-states, variation-threshold-stationary-times) went to GitHub, Zenodo and ResearchGate with PDFs predating their 12 Nov referee-correction commits; check: git log -1 -- paper/main.tex newer than git log -1 -- paper/main.pdf means stale"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T17:28:38+02:00
  status: provisional
  evidence: ""
---

13 Nov 17:2x. The 'final_e5e491f/d634194/d40693b' PDFs were byte-identical to the repo PDF committed one commit EARLIER; the referee-corrections commits changed main.tex only. pdftotext showed the old wording ('to 120 terms', 'Both theorems hold', 'have been checked in Lean'). Fix: rebuilt from HEAD, pushed GitHub dbb7c77/984b772/6c845dc, Zenodo new versions 24201010/24201019/24201020 (md5 read back), RG file replacement queued in researchgate_queue/q4/RG_REPLACE_FILE_1114.txt. Check before any upload: for the repo, the last commit touching the PDF must be at or after the last commit touching the .tex (and any \input file); and grep the PDF text for a phrase only the newest tex has. A scan over 35 local paper clones found exactly these three. Related: [[w07_zenodo_compare_pdf_version]] [[check_the_rendered_pdf_cleveref_mislabels_2026_08_04]]
