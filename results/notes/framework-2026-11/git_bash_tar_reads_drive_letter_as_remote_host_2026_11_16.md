---
name: git_bash_tar_reads_drive_letter_as_remote_host_2026_11_16
description: "In Git Bash on Windows, tar given an archive path with a drive letter (C:/...) reads 'C' as a remote host and fails with 'Cannot connect to C: resolve failed'. Inside a script whose errors are not checked, a stale partial extraction from an earlier run then looks complete: a frozen test fixture held 55 of 331 files and a study downstream printed zero routes. Use a relative path or --force-local, and count the extracted files."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

What happened. A study script ran `tar xzf C:/.../fixture.tgz` in Git Bash. GNU tar treats an archive name of the form
host:path as a remote archive reached through rsh, so `C:/...` became host "C". The call failed, the script did not
check its status, and the target directory still held the files of an earlier extraction of a truncated download:
55 of 331. The study that read the fixture printed 0 routes, which looked like a result rather than a missing input.

Fix. `cd` into the archive's directory and pass a relative name, or pass `--force-local`. After any extraction, count
the files against the archive's own listing (`tar tzf archive | wc -l`) before using them, and extract into an empty
directory so that leftovers from an earlier run cannot pass for a complete set.

General rule: a downstream zero (no routes, no rows, no matches) is first a question about the input.

Related: [[sha256sums_crlf_read_loop_writes_empty_hashes_2026_11_12]].
