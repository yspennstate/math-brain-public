---
name: sha256sums_on_windows_hash_the_committed_blob_not_the_working_copy_2026_11_11
description: "[VERIFIED] SHA256SUMS in a repo cloned on Windows: hash git cat-file blob HEAD:<path>, never the working file or a git archive export (autocrlf turns LF to CRLF in both)"
metadata:
  node_type: memory
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T09:55:10+02:00
  status: provisional
  evidence: ""
  originSessionId: agent-82f2-44c5-b3e3-c0011e4a519a
  modified: 2026-11-11T14:48:22.090Z
---

A paper repo (nonnormal-orbit-quotients, 11 Nov) keeps SHA256SUMS.txt. I refreshed it with sha256sum on the Windows working copy and pushed hashes that did not match the committed README.md, main.tex and check.py: core.autocrlf had turned their LF into CRLF on checkout. A git archive | tar export is no check either; it applies the same conversion and reported FAILED for good sums. Hashing the raw blob with 'git cat-file blob HEAD:<path> | sha256sum' reproduced the original README and check.py sums exactly, and the fix went up as 734f027. Binary files (PDF) are unaffected, which is why they looked fine. **Why:** a checksum file that does not match the repo makes the release look tampered with. **How to apply:** whenever a repo carries SHA256SUMS, MANIFEST hashes or similar, compute every entry from git cat-file blob after the commit, then verify each line against the blob before the push.

Second trap, same day (rrt-layer-tail, 7ba831a): a helper that refreshed the sums BEFORE the commit used "working file has CRLF, so read the index blob instead". A PDF holds \r\n byte pairs, so the rebuilt main.pdf was hashed from the index, which still held the OLD pdf; the pushed line was stale. Fixed in 7cde025. Before a commit, decide text vs binary by git's own verdict (`git diff --no-index --numstat /dev/null <path>` prints `-\t-` for binary), hash binaries as they are on disk and text with CRLF folded to LF; the index is never a source for a file not yet staged. The check that caught it: after the push, hash every listed file from raw.githubusercontent at the new commit and compare it with the pushed SHA256SUMS (strip \r from that file first).

Third trap (11 Nov 17:0x, cantor-harmonic-codings-singular): some repos commit CRLF blobs (code/check_gap_output.txt was pushed with CRLF inside the blob), so "fold CRLF to LF" broke a line that had been right. The rule that holds in every case: a file unchanged against HEAD hashes as its HEAD blob; a changed file hashes as the blob `git hash-object -w` makes from it, then `git cat-file blob <oid>`. scratchpad fix_sums.py v3 does this; commit d8471db fixed the sums, and all six lines were checked against raw.githubusercontent at that commit. Check against raw GitHub after every sums refresh, not before.
