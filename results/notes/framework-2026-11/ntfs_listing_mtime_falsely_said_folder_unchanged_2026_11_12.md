---
name: ntfs_listing_mtime_falsely_said_folder_unchanged_2026_11_12
description: "NTFS scandir DirEntry stat Get-ChildItem folder mtime stale freshness verdict"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:11:15+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: The 11 Nov film unregistered-verdicts check read a stale folder time from a parent listing and judged changed folders unchanged. os.stat on the folder's own path gave the live time. The 12 Nov method records 1 incident, with no exact number of affected folders.

Why it happened: NTFS can update the parent's index entry lazily. A directory listing's cached entry was treated as the folder's own current record.

**Why:** A cached listing can hide work from a freshness gate even when its comparison logic is correct.

**How to apply:** Use os.stat(folder_path) for that folder's freshness, and stat the actual file or walk when an in-place nested edit would not change the folder's own mtime; keep the NTFS explanation provisional until independently reproduced.

[[method_stat_the_path_for_a_folders_mtime_not_the_listing_2026_11_12]]

Drafted by Codex worker W05 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

