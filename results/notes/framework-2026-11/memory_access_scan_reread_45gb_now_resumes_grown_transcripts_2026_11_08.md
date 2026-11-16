---
name: memory_access_scan_reread_45gb_now_resumes_grown_transcripts_2026_11_08
description: "Dream build_memory_access hit its 1800 s budget, wrote nothing / cache never saved: grown transcripts were re-read from byte 0 and the cache was saved only on success; now resumes from a tail-hashed offset and saves progress on a budget cut (parity 173/173 rows)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:05:21+02:00
  status: provisional
  evidence: ""
---

The dream's build_memory_access step (`--write --max-seconds 1800`) ran out of its budget in the 7 Nov dream and in the one after it, and wrote nothing either time. The 7-day transcript window had grown to 42.6 GB, then 44.8 GB, at about 1 GB per long session file.

Cause, read from the code: the per-file cache (memory_access_scan_cache.json) is keyed on size and mtime. A transcript that has grown since the last scan does not match its key, so it is read again from byte 0. The cache is also saved only after a successful --write. Once the whole window took longer than the budget, every run started cold, hit the budget and threw its progress away. The cache was last saved 7 Nov 06:59.

Fix, landed 8 Nov 05:0x by an agent. Live file build_memory_access.py, sha256 98879fb41b374d59 (was 84a9c8ca78c4ef9a); the same file is mirrored at 12_cognitive_architecture/dreaming/.
- Transcripts are append-only, so a grown Claude file resumes from its cached offset. Before trusting the offset, the code checks the sha256 of the 4 KB before it against the stored tail_sha.
- Each cache entry now stores offset, lines, nrows, pending (tool calls still waiting for their results) and tail_sha. The cached size is the number of bytes actually read, not a later stat.
- A trailing line with no newline is processed but never counted into the offset, so it is read again in full next time.
- When the budget runs out, the files already finished are saved, together with a partial entry for the file that was being read. The next run continues from there instead of starting cold. The exit code is still 3, and no ledger is written from partial data.
- Codex files keep the old whole-file cache.

Parity test (sr_prof/test_bma.py, run on a 54 MB transcript plus the first 150 MB of a second one):
- Each check below gave exactly the same 173 rows, line for line, as the original code scanning cold: the copies cut mid-line at 61% and then grown and resumed; the new code cold; a rerun on unchanged files; and a run cut by a 0.3 s budget over and over, which converged in 14 runs.
- Direct check of the resume path: the grown file skipped 32,875,382 bytes and read 2,643 lines instead of about 5,900, and ended with the same 123 rows as a full scan.

The patch changes the scanner sha, which invalidates the old cache. The first run after landing is therefore cold. With the budget save it now makes progress anyway, and later runs resume.

To verify: the next dream log (newer than dream_20261107_184245) should show build_memory_access finishing with no STEP CAPPED or budget exit, and the memory-access ledger should be fresh. If it still caps, the cold first pass is the cause: run the step once by hand at BelowNormal to warm the cache.

