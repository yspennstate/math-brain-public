---
name: zenodo_refs_natbib_doi_macro_and_master_branch_repos_2026_11_11
description: "[VERIFIED] Zenodo refs refused 'TeX left' with \\doi10... or \\natexlabb, or a repo 'fetch failed' as AHEAD? natbib .bbl macros: \\doi{x} prints 'doi: x', \\natexlab{b} prints b - map them before brace stripping (zen_refs.plain). A repo whose default branch is master (DNNaic) was classed AHEAD against a missing origin/main; it was in sync. Check git ls-remote HEAD before calling a repo ahead."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T21:17:53+02:00
  status: provisional
  evidence: ""
---

Found 11 Nov 2026 in the Zenodo citation pass (session agent). DNNaic 23329784: 23 of 29 entries carried \doi10.x after brace stripping; with the two maps all 29 matched the Zenodo PDF (refs_in_pdf missing 0) and were filled in place. The same pass: ahead_one.sh now builds a missing .bbl (pdflatex into build/ + bibtex, PDF md5 checked unchanged), which unblocked quantile-process-lp (16 refs, 10.5281/zenodo.24144481). ResearchGate-DOI records take no new version: a citation pass on GitHub (uniform-condensation-windows 674b00a) leaves the Zenodo record on its own PDF's reference list.
