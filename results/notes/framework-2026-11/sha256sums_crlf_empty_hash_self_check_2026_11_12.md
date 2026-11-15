---
name: sha256sums_crlf_empty_hash_self_check_2026_11_12
description: "SHA256SUMS every entry is empty-input digest after CRLF shell read loop"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:36:09+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 12 Nov staged-blob checksum rebuilding in partition-qso-empty-body wrote the empty-input hash for every listed path. Bad checksums were pushed in 4d4185c, then fixed in 64848e9; verification using the same loop had agreed. The source does not give the number of manifest entries.

Why it happened: A shell read retained CR in each path, Git blob retrieval failed, and the downstream hasher consumed empty input. Reusing that path for verification reproduced the failure.

**Why:** A check with the same failing input path can certify its own error.

**How to apply:** Strip CR from manifest paths, fail on retrieval errors, refuse unexpected empty-input digests and verify independently in a clean checkout with core.autocrlf=false using sha256sum -c.

[[sha256sums_crlf_read_loop_writes_empty_hashes_2026_11_12]]

Drafted by Codex worker W08 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

