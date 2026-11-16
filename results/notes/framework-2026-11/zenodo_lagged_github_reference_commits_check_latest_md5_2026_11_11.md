---
name: zenodo_lagged_github_reference_commits_check_latest_md5_2026_11_11
description: "Paper citation pass done on GitHub but Zenodo record still empty References / old PDF? Compare the Zenodo latest file md5 with main; same bytes = fill refs in place, else new version. bibtex from TeX folder."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T18:41:28+02:00
  status: verified
  evidence: "11 Nov 2026 session agent: classify.txt (22 empty-ref records: 17 AHEAD, 5 SAME), zen1111/api_published.tsv and addrefs.tsv rows, zen_verify.py on 24141500/24141501/24141614 (quote normalisation only)"
---

A citation pass that commits new references to GitHub is not finished until Zenodo carries them. On 11 Nov 2026, 24 of the 57 Zenodo records of 8-10 Nov had an empty References field (hook C14 unmet), and 17 of those had "add references" commits on GitHub main that were never posted: the paper had been judged clean by reading GitHub HEAD while Zenodo still served the older PDF.

The check that finds it: for each record, follow /api/records/<id>/versions/latest, take its isSupplementedBy GitHub tree link and its one file md5, find the PDF at that commit with the same md5, and compare with the same path on main. Same bytes on main = fill the References field in place (deposition actions/edit, PUT metadata.references, publish: no new version, file untouched). Different bytes = post a new version from main. Scripts: zen_classify.py, zen_addrefs.py, ahead_one.sh in the 11 Nov citation-pass of session agent (copies should move to the paper tooling).

Before writing a list: every reference's longest title words must appear in the pdftotext of the PDF being posted (refs_in_pdf.py); 0 misses on all 22 records.

Two traps met on the way:
- A repo with a .bib and no .bbl: pdflatex -output-directory=build, then run bibtex FROM THE TeX's FOLDER as `bibtex build/<stem>`. Run inside build/, bibtex finds some other references.bib on the MiKTeX search path and writes an empty bibliography with "didn't find a database entry" warnings.
- After publish, Zenodo stores curly quotes as straight quotes, so an exact compare of stored references against the sent list reports CHECK; compare after normalising quotes.

Result 11 Nov: 17 new versions (24141479..24141658) and 5 in-place fills (24063833, 24069879, 24069931, 24070253, 24072301), every file md5 equal to the GitHub PDF.


Third trap (11 Nov evening): a record whose DOI is a ResearchGate DOI (10.13140/rg...) instead of 10.5281/zenodo refuses actions/newversion with "403 Permission denied" every time; Zenodo versions only DOIs it issued. Those records (11 October papers, 2332xxxx) keep their PDF; fill the References field in place from the bibliography of the PDF on the record (zen_addrefs.py, md5-gated). Check the deposition's `doi` before trying a new version. A SHA256SUMS that fails only on files untouched since it was written was usually hashed over a CRLF checkout: rewrite it from the committed blobs.
