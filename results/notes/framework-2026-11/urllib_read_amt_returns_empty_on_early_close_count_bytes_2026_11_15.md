---
name: urllib_read_amt_returns_empty_on_early_close_count_bytes_2026_11_15
description: "[VERIFIED] Downloader marks GitHub assets 'BAD size/digest' with no retry logged? urllib's HTTPResponse.read(amt) returns b'' at early EOF instead of raising IncompleteRead, so a cut download looks complete; count bytes against the expected size and retry."
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T13:14:34+02:00
  status: provisional
  evidence: ""
---

15 Nov 2026 (an agent): ghkeep-1 (the GitHub-to-Google keeper, T-20261114-023) logged 53 ASSET BAD (size/digest) lines in film-pictures-archive with no retry line before them. A hand download of two of them on the same VM matched GitHub's size and sha256 exactly (world_history_ep02.part001.tar.s5 65,218,560 B, world_history_series_assets.part075.tar.s1 67,108,864 B), so the GitHub copies are sound and the fault was the downloader. CPython http.client readinto() closes the connection and returns 0 when the socket ends early ('Ideally, we would raise IncompleteRead ... but it might break compatibility'), so a loop over r.read(1<<20) ends quietly on a short file. Fix (ghkeep.py 9396b144 on the VM, old copy ghkeep.py.bak_1115): count bytes, raise on n != asset size, so the existing retry loop handles it. The keeper skips BAD assets, and its next pass picks them up (todo = assets whose bucket size differs). Rule: a streamed download is checked by counting bytes against Content-Length or the API size, never by the absence of an exception. Status: verified on two assets; the cause of the early closes (rate-limit sleeps, S3 redirect timeouts) not measured.
