---
name: paper_checksums_hashed_crlf_checkout_2026_11_12
description: "SHA256SUMS txt incorrect hashes Windows CRLF working copy staged Git blob"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:41:27+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 12 Nov 3 of 5 P0178 SHA256SUMS.txt entries were wrong. They had been computed from the CRLF working copy; the manifest was repaired using index blobs.

Why it happened: The checkout bytes differed from the bytes Git stored.

**Why:** A repository checksum must describe the stored artifact it claims to authenticate.

**How to apply:** For a Git-file manifest hash staged blobs, and verify the manifest against those blobs; exported binary artifacts still need their own byte hashes.

[[p0178_p0209_independent_referee_passes_sound_2026_11_12]]

Drafted by Codex worker W01 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

