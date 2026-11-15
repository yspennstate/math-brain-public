---
name: zenodo_record_exists_but_pdf_lags_2026_11_12
description: "All GitHub papers have Zenodo records but are their served PDFs the latest version?"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:32:16+02:00
  status: provisional
  evidence: ""
  lesson: true
---

The 12 Nov audit found 138 published records and one record for each of 114 matched public paper repos. Of those PDFs, 90 matched GitHub main by MD5 and 24 differed, with GitHub commits later than the corresponding Zenodo file dates. Two other paper repos contained older versions linked to records through other repos, and 8 records had empty References fields. These measurements do not establish that record coverage means synchronization; no upload or false completeness report is recorded.

A record link establishes presence, not byte identity. Shared brain/site credit links can also look like paper links if all related identifiers are counted. Contents of the 24 differing PDFs were not compared.

**Why:** Publication presence and publication version are separate checks.

**How to apply:** Match paper repo related identifiers after excluding shared credits, compare served PDF checksums with main, and inspect commit dates for mismatches; rerun after versions change and do not infer upload authorization from this audit.

[[github_papers_vs_zenodo_24_files_lag_two_old_repos_2026_11_12]]

Drafted by Codex worker W07 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

