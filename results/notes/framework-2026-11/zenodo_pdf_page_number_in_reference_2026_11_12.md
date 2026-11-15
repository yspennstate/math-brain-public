---
name: zenodo_pdf_page_number_in_reference_2026_11_12
description: "Extracted Zenodo bibliography includes a page number or broken PDF words"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:29:05+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 12 Nov 2026 the first toeplitz metadata edit appended page number 12 to reference entry 10 and had to be redone. In the 139-record count check, 130 counts matched directly, 5 needed address-line or caption checks and 4 bracket-label layouts needed a label count.

Why it happened: Plain pypdf text retained a page footer and could split words or lose spaces. A raw text list was trusted without a layout comparison.

**Why:** PDF text extraction loses the positions that distinguish bibliography continuations from page furniture.
**How to apply:** Compare PyMuPDF hanging-indent lines with pypdf before publishing; inspect disagreements against the record's PDF and normalize curly apostrophes during metadata readback.

[[zenodo_references_on_external_doi_records_by_metadata_edit_2026_11_12]]

Drafted by Codex worker W06 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

