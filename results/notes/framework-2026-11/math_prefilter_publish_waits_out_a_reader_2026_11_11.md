---
name: math_prefilter_publish_waits_out_a_reader_2026_11_11
description: "math_prefilter build died at os.replace with PermissionError WinError 5 (index .tmp -> .prefilter.pkl)? A reader had the index open; Windows refuses the move. Since 11 Nov 04:01 one publish step: temp name with pid and thread, the move retried up to 45 s, temp never left. 17 controls pass on live"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T04:17:56+02:00
  status: verified
  evidence: "brain_improvement/agent_run/prefilter_publish/patch_prefilter_publish.py, test_prefilter_publish.py; ledger_rows_20261111_h.jsonl"
---

The math index build (`math_prefilter.py build`) wrote `brain.sqlite3.prefilter.pkl.tmp` and moved it over the index with one bare `os.replace`. On Windows that move is refused (PermissionError, WinError 5) while any process has the destination open, and every math prompt opens the index to load it (35 MB, so the handle is held for a noticeable time). Nine builds in the logs to 10 Nov died at that line after doing all their work. The temp name was also fixed, so two builds at once wrote the same temp file.

Since 11 Nov 04:01 both published files (the index and the `.lexdf.pkl` table) go through one step, `_publish(dest, write, wait_s=None)`:
- the temp name is `<dest>.tmp.<pid>.<thread id>`;
- a refused move is tried again with a growing pause (0.05 s doubling to 1 s) until the reader lets go, 45 s in all (`MATHBRAIN_PREFILTER_PUBLISH_WAIT`), then the error is raised and the old index is still there;
- the temp file is removed in a `finally`, whatever happened.

Live sha256 53fcc21578f08f70 (was 1545436c060af419), backup `math_prefilter.py.bak_publish_20261111`, repo mirror equal.

Measured (`brain_improvement/agent_run/prefilter_publish/test_prefilter_publish.py <file>`, 17 controls, all pass on the live file; 3 of the 4 that apply fail on the old file):
- a bare `os.replace` over a file held open for reading is refused on this machine;
- a reader holding the file 1.2 s is waited out (1.56 s) and the publish lands;
- a reader that outlasts the wait raises PermissionError, the old file is intact, no temp file is left;
- a writer that dies mid-file leaves the old file and no temp file;
- three writers at once, 75 publishes, none fails, the file left is one writer's whole file;
- against a second process loading the file in a loop for 3 s: 17 publishes, none fails; the reader made 8,488 loads and was refused 11 times.

What it does not cover: no full build was run on the live store, so the proof is on the publish step alone. A reader that opens the index in the instant of the move gets a PermissionError of its own (11 of 8,499 in the control); `load()`'s callers were not each checked for that. A reader that holds the index longer than the wait still fails the build.

The same shape, for any file a hook reads on every prompt on Windows: publish through a temp name of your own and retry the move; never one bare `os.replace`.

