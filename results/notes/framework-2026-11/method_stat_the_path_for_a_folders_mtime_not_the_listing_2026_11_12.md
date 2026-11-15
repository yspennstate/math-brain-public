---
name: method_stat_the_path_for_a_folders_mtime_not_the_listing_2026_11_12
description: "[PROVISIONAL] Method: on Windows/NTFS, a folder's change time taken from a directory LISTING (os.scandir DirEntry.stat, dir, Get-ChildItem) can be stale because the parent index updates lazily; a freshness or 'did it change' verdict on a folder calls os.stat on the folder's own path (or stats a file inside it); from the 11 Nov film unregistered-verdicts fault"
metadata:
  node_type: memory
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T02:50:00+09:00
  status: provisional
  priors: "a listing is a cached view; the entry's own stat is the record"
  originSessionId: agent-2c25-4a49-9a43-6448840c2424
  modified: 2026-11-12T00:47:47.988Z
---

**The move.** When a verdict depends on WHEN a folder last changed (a watcher deciding "nothing new here", a verdict
file deciding the film did not move, a sync deciding to skip), do not take the mtime from the directory listing's
entry; call `os.stat(path)` on the folder itself, or stat the newest file inside it. NTFS writes the parent's index
entry lazily, so the listing can show the old time after the folder has in fact changed.

**Where it worked.** The film unregistered-verdicts check on 11 Nov 2026 read a stale listing mtime and judged
folders unchanged that had changed; the os.stat on the path gave the live time
([[ntfs_listing_mtime_of_a_folder_is_stale_stat_it_film_unreg_verdicts_2026_11_11]]). Same family as the stale
status-file scars: the artifact is the live state, the cached view is not
([[retry_reads_the_status_not_the_work_2026_07_15]]).

**Where it would NOT work.** A folder whose own mtime does not move on the change you care about (a file edited in
place inside a subfolder two levels down does not touch the top folder's mtime on NTFS) - there stat the file, or
walk. On Linux ext4 the listing and the stat agree and the move is harmless but unnecessary.

**The one check that breaks it.** Change a file in a folder, list the parent at once, and compare the entry's mtime
to os.stat of the folder: if they always agree on this file system, the method is not needed there. One case so
far; provisional until a second folder-freshness fault is caught by it.
