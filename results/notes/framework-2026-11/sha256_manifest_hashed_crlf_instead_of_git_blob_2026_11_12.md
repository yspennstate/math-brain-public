---
name: sha256_manifest_hashed_crlf_instead_of_git_blob_2026_11_12
description: "SHA256SUMS paper repo Windows autocrlf hash mismatches Linux clone; git index blobs"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:00:59+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 12 Nov 2026, sha256sums_update.py hashed working files for P0243 commit e311262. Four of six manifest lines disagreed with stored Git blobs for about one hour. A PDF spot check passed because the PDF had no converted text line endings. Five of six lines changing on P0033 after only two file edits exposed the problem. P0243 was fixed in 4acce9f; P0032, P0033 and P0243 then had zero HEAD mismatches.

Why it happened: core.autocrlf=true made Windows text working copies CRLF while Git stored LF. The helper hashed a different byte representation from the manifest's promised repository files. Only three of the author's thirteen clones had these manifests; other agents' repositories were not checked.

**Why:** A checksum is a claim about a specific byte representation, not merely a filename.

**How to apply:** For repository-file manifests, stage the edits and hash git show :path blobs, write the manifest with LF and verify against HEAD after commit; investigate excess changed sum lines and honor a different documented archive or line-ending contract.

[[sha256sums_hash_the_stored_blob_not_the_crlf_working_copy_2026_11_12]]

Drafted by Codex worker W03 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

