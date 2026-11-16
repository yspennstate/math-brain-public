---
name: gh_offload_hold_secrets_rename_failed_past_260_chars_2026_11_13
description: "[VERIFIED] gh_offload --hold-secrets died with WinError 3 on codex worktree copies (paths past 260 chars); fixed 13 Nov with the long-path prefix on rename src and dst; nothing uploaded or deleted by the failed run"
metadata:
  node_type: memory
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T05:06:39+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-13T04:16:25.038Z
---

gh_offload.py --hold-secrets moves credential-pattern files to gh_offload_scratch/held_secrets under their own absolute path. On codex_worktree_archive_2026_07 (Codex worktree copies of the brain repo nested deep, e.g. claude/plugins/marketplaces/...) the held path passes 260 characters and os.rename raised WinError 3 after two files had moved. The run stops before any upload, so nothing was uploaded or deleted; the moved files are listed in held_secrets/LIST.tsv.

Fix (13 Nov 05:1x, backup gh_offload.py.bak_longpath_1113): on Windows both src and dst get the long-path prefix before mkdir and rename. Tested with a 432-character rename.

Second and third failures the same morning, same folder (2026-07-18):
- ghstore put opens files without the prefix, so the upload itself hit WinError 3. Fix: pack_long_paths() in gh_offload.py (backup .bak_packlong_1113) runs before the put. Every file whose path is 240+ characters goes into <folder>/_LONG_PATHS.tar (PAX, relative names), each member's sha256 is read back from the tar, then the originals are removed. ghstore uploads the tar like any file. Restore: ghstore get the folder, then untar _LONG_PATHS.tar in place. 07-18 packed 1,837 files into 35 MB.
- The Codex worktree copies carry read-only directories, so rmdir of the emptied long dirs raised WinError 5. Fix: clear S_IWRITE, then rmdir.
- A rerun right after the pack is refused "still being written" (the tar is new). Pass --quiet-min 5 on a rerun; a first run packs after the quiet check, so it needs nothing.
Long files left in the other date folders (13 Nov): 07-12 17,944, 07-13 9,902, 07-14 35,943, 07-19 17,035, 07-20 6,387, 07-21 1,596. Committed in the brain repo as 22e2c8aab43 (not pushed yet: local main was 123 commits ahead of origin).

How to apply: any Python file move on Windows into a mirrored path tree (hold, quarantine, archive) needs the prefix; reads may work without it while MoveFile does not. Related: [[gh_offload_scan_never_looked_inside_gz_npz_fixed_placeholder_only_2026_11_09]].
