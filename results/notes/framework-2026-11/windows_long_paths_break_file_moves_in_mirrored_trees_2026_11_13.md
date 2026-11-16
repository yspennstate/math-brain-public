---
name: windows_long_paths_break_file_moves_in_mirrored_trees_2026_11_13
description: "An offload tool that moves files into a tree mirroring their absolute path (hold, quarantine, archive) failed on Windows as soon as a mirrored path passed 260 characters: rename raised WinError 3 after two files, the uploader then failed the same way, and read-only directories refused removal. Fixes: the long-path prefix on both ends of every move, long files packed into one tar with each member's sha256 read back before the originals go, and the read-only bit cleared before rmdir."
metadata:
  type: project
  created: 2026-11-13
  status: verified
---

The setting. An offload tool uploads a folder to GitHub, checks the copy and then deletes the local one. Before the
upload it moves any file that matches a credential pattern into a holding folder, under a path that repeats the
file's own absolute path. One archive folder held copies of nested agent worktrees, so its paths were already deep.

Three failures in one morning, each on the same folder.
1. The move. The holding path passed 260 characters and `os.rename` raised WinError 3 after two files had moved.
   The run stops before any upload, so nothing was uploaded or deleted; the two moved files were listed.
   Fix: on Windows both source and destination get the `\\?\` long-path prefix before `mkdir` and `rename`.
   Tested with a 432-character rename.
2. The upload. The uploader opened files without the prefix and failed the same way. Fix: before the upload, every
   file whose path is 240 characters or more goes into one `_LONG_PATHS.tar` in that folder (PAX format, relative
   names). Each member's sha256 is read back from the tar, and only then are the originals removed. The tar uploads
   like any file; a restore downloads the folder and untars it in place. On the first folder: 1,837 files, 35 MB.
3. The cleanup. The worktree copies carried read-only directories, so removing the emptied directories raised
   WinError 5. Fix: clear the write-protect bit, then `rmdir`.

A rerun right after the pack was refused as "still being written", because the tar was new; the tool's quiet-period
check is right to do that, and a rerun passes a shorter quiet period.

How to apply. On Windows, any program that moves files into a tree mirroring their original paths needs the
long-path prefix on both ends. Reads often succeed without it while moves do not, so a tool can pass its tests on
short paths and fail on the first deep tree. Pack what cannot be moved, verify the pack member by member, and only
then delete.

Related: [[git_bash_tar_reads_drive_letter_as_remote_host_2026_11_16]].
