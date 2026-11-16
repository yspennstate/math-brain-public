---
name: mac_code_mirror_push_replaced_8_online_files_now_new_only_without_sync_2026_11_08
description: "Does mac_code_mirror --push only add new files? Not before 8 Nov 23:5x: three pushes replaced 8 private-repo files; now new-only unless GIT_SYNC_APPROVED exists"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T00:18:23+04:00
  status: provisional
  evidence: ""
---

Does mac_code_mirror.py --push only add files to the brain repo? It did not: before 8 Nov 23:5x it also replaced every stale online file, and three --push runs that night replaced 8 files on the private repository while the second machine's rule is new files only until GIT_SYNC_APPROVED exists. The rule lived only in a code comment and in --new-only, which nobody had to pass.

Fixed in mac_code_mirror.py: without GIT_SYNC_APPROVED a --push is new-only whatever the flags say, and it prints how many stale files it left. Checked old against new on a temp tree with one altered file and a fake push_paths_api.py: the old copy pushed the stale file, the new one left it (mirror_ab/run_ab.sh, an earlier session). Backup mac_code_mirror.py.before_20261108_newonly. The 8 files: heavy_lock_run.sh; math_prefilter.py, math_sense.py, memory_amend.py; cut_movie.py, node_guard.sh, add_classical.py, enc_v5_job.sh.

**Why:** a rule kept in a comment is not enforced; the default path of the tool did the forbidden thing.

**How to apply:** a stale file on the brain repo waits for his git-sync decision; read the mirror's 'new-only (no GIT_SYNC_APPROVED)' line as expected, not as a failure to work around. Earlier mirror history: [[mac_code_mirror_had_no_timer_413_files_missing_new_only_landed_408_2026_11_06]].

