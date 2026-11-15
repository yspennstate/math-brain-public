---
name: public_push_secret_scan_refuses_npy_in_text_list_2026_11_15
description: "[VERIFIED] math-brain-public push_rest stops at 'SECRET SCAN ERROR: content had ambiguous NUL-heavy text encoding / REFUSED rc 2' and every later pass repeats it? A binary (.npy) sits in the TEXT order list; find it by NUL count, drop it or ship it with the binaries."
metadata:
  node_type: memory
  type: project
  status: verified
  created: 2026-11-15
  evidence: "B16/17 push 15 Nov 16:56-17:03: chunks 00-03 landed (origin bd6a4f8ed), chunk 04 and three retry passes rc 2, 551 of 1351 pending; culprit fei-solve-2026-11/codex/workers/FEIB21/inputs/pm_record_spectrum.npy (2,091,605 NUL bytes)"
  originSessionId: agent-4b92-4833-bcc3-a3ab8aa26344
  modified: 2026-11-15T17:00:30.836Z
---

On 15 Nov 2026 the B16/17 push to math-brain-public landed four chunks of 200 and then stopped. Every retry pass failed on the same chunk with rc 2. The log only showed `rc 2`. The push client's own output (`<tag>_last_push.txt`) ended with `SECRET SCAN ERROR: content had ambiguous NUL-heavy text encoding` and `REFUSED: scan not clean (rc 2)`.

Cause: tree_select.py had put a NumPy array (`.npy`) into the text list, not the `_bin` list. The secret scanner will not judge a file that is mostly NUL bytes, so it refuses the whole commit. push_rest.sh then breaks the pass, and passes 2-4 retry the same chunk and fail the same way.

Fix: count NULs in each pending path (`tr -dc '\000' < f | wc -c`), drop the file from the order list (or route it with the binaries), and rerun push_rest.sh. It resumes by blob comparison, so nothing that already landed is pushed again.

Second case, the same day (B22, 18:37): `SECRET SCAN: 3 possible secret(s) ... long API key ... REFUSED: scan not clean (rc 1)`. The scanner names no file. The cause was a worker's bookkeeping script whose route notes ran words together in camel case (a 49-character run of the form C037uniformfullbox... with no separators). That string is 40 or more letters and digits in mixed case, so it reads as a key. The fix: drop that file from the order list and rerun push_rest.sh.

How to apply: when a push_rest pass reports rc 2 with nothing pushed, read `<tag>_last_push.txt` before retrying. Add `.npy`, `.npz`, `.pkl`, `.pt` and `.parquet` to tree_select's binary extensions. See [[public_push_resume_by_blob_compare_chunks_of_200_2026_11_15]] and [[crlf_copy_list_left_uf00d_in_file_names_git_cannot_open_2026_11_15]].
