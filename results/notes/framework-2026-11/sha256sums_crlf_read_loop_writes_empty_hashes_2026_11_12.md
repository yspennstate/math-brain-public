---
name: sha256sums_crlf_read_loop_writes_empty_hashes_2026_11_12
description: "[VERIFIED] SHA256SUMS recompute wrote e3b0c442... for every file? The file had CRLF lines; 'while read h p' keeps the CR, git cat-file fails, sha256sum hashes empty input, and a verify through the same loop agrees with itself."
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T00:35:24+02:00
  status: provisional
  evidence: ""
---

When recomputing a repo's SHA256SUMS from staged blobs, strip CR first (tr -d '\r' < SHA256SUMS.txt | while read ...), refuse any hash equal to the empty-input hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, and verify from an independent path: a fresh clone with core.autocrlf=false and sha256sum -c (a normal Windows clone converts text files to CRLF and every text line FAILS for that reason alone). Seen 12 Nov on partition-qso-empty-body: bad checksums pushed in 4d4185c, fixed in 64848e9. **Why:** a self-consistent check is not a check. **How to apply:** every paper push that touches SHA256SUMS.
