---
name: sha256sums_hash_the_stored_blob_not_the_crlf_working_copy_2026_11_12
description: "SHA256SUMS in a paper repo wrong after a Windows edit? autocrlf working copies are CRLF: hash git show :path blobs (sums_from_git.py), alarm = more changed lines than edited files"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T03:32:51+02:00
  status: verified
  evidence: "P0243 e311262: 4 of 6 lines mismatched the stored blobs; fixed 4acce9f; sums_from_git.py reports 0 mismatches at HEAD for P0032, P0033, P0243"
---

SHA256SUMS.txt in a paper repo must list the hashes of the files as git stores them. On this workstation core.autocrlf is true, so a text file in the working copy (tex, py, lean, txt) has CRLF line endings while the stored blob has LF; hashing the working copy gives a hash nobody who clones on Linux or downloads from GitHub can reproduce.

What happened: on 12 Nov my helper sha256sums_update.py hashed working files. For P0243 (variation-threshold-stationary-times, commit e311262) four of six lines were wrong for about an hour; PDFs and files without line endings to convert were right, which is why a spot check on the PDF passed. Caught when the same script reported 5 of 6 lines changed on P0033 after I had edited only two files. Fixed in P0243 commit 4acce9f; P0033 went out correct (ae7926d).

How to apply:
- Stage the changed files, then hash `git show :<path>` (the index blob) for every line of SHA256SUMS.txt; write the file with LF; stage it; verify again against HEAD after the commit. Script: ~/agent_run/sums_from_git.py <repo> [--write] [--ref HEAD] (prints MISMATCH lines; 0 mismatches is the pass).
- A count of changed lines larger than the count of files you edited is the alarm.
- To audit an existing repo: python sums_from_git.py <repo> --ref HEAD.
- Checked on 12 Nov: of my 13 working clones only P0032, P0033 and P0243 carry a SHA256SUMS.txt; all three now show 0 mismatches at HEAD. Other agents' paper repos were not checked.

What would change this: a repo with a .gitattributes that pins eol (then working copy and blob agree), or a sums file documented as covering release archives instead of repo files.

