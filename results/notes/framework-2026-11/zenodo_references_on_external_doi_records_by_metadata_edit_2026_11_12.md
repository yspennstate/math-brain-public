---
name: zenodo_references_on_external_doi_records_by_metadata_edit_2026_11_12
description: "[VERIFIED] Zenodo record with a ResearchGate/arXiv DOI has empty References but refuses a new version? Metadata edit fills it, files and DOI kept; read the list from the record's own PDF with PyMuPDF hanging-indent lines (pypdf kept a page number)"
metadata:
  type: reference
  created: 2026-11-12
  created_at: 2026-11-12T01:55:32+02:00
  status: verified
  evidence: "7 records edited 12 Nov, public API readback; 139-record sweep 0 empty"
---

A Zenodo record whose DOI was minted elsewhere (ResearchGate 10.13140, arXiv 10.48550) refuses a new version, but it takes a metadata edit: POST actions/edit, PUT the metadata with `references` filled, POST actions/publish. The files and the DOI stay as they are. On 12 Nov 2026 this filled the empty References on seven records (toeplitz-hankel 23329816, Ross 23329698, outer-vertex 23329719, relu 23329744, maximal-kemeny 23329546, 24063842, 24063846); a sweep of all 139 records on the account then found none empty.

The list has to be the one printed in the record's own PDF (citation hook C14), which is often not the repo's current source. First look for a commit whose PDF has the record file's md5 and read that commit's bibliography (Ross: commit 41edcbd, the source sat inside a zip). When no commit matches, read the PDF itself.

For reading the PDF, PyMuPDF line positions beat pypdf text. An entry starts at a line on the left margin; indented lines continue it. That handles numbered and author-year lists alike. pypdf splits words ("V oigtlaender", "math-bra in-public"), drops spaces ("Probab.30"), and kept a page number: the first toeplitz edit went out with " 12" at the end of entry 10 and had to be redone. Run both extractors and compare the lists before publishing. They agreed on relu and outer-vertex; the one difference was that page number.

Readback: Zenodo stores a curly apostrophe (’) as a straight one ('), so compare after mapping it, or a correct edit reads as a mismatch.

Tools (scratch scripts, 12 Nov): zen_editrefs.py RECID REFS.json [--dry]; pdf_refs_ay.py PDF OUT.json; rec_pdf_commit.py RECID CLONE PDF_PATH OUTDIR; zen_emptyrefs.py (account sweep).

Would change this: if Zenodo starts versioning externally-minted DOIs, the new-version path (zen_api.py vers) becomes the better route, since it uploads the final PDF as well.


Related: [[zenodo_refs_from_the_pdf_accents_labels_and_tails_2026_11_11]], [[zenodo_lagged_github_reference_commits_check_latest_md5_2026_11_11]], [[github_papers_vs_zenodo_24_files_lag_two_old_repos_2026_11_12]].

Count check, 12 Nov 02:0x: all 139 records compared with their main PDF (zen_refcount.py). 130 matched the PyMuPDF splitter exactly; 5 differed only by an address line or figure caption the splitter caught; 4 (bracket-label layouts the splitter cannot split) matched on a count of labels in the reference section. No record carries a References list that disagrees with its PDF.
