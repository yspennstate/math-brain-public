---
name: patch_landed_on_repo_copy_not_the_file_the_task_runs_2026_11_12
description: "Patched a live brain script and the task still runs the old code? Check the path: on 12 Nov the mirror patch went onto the repo copy (12_cognitive_architecture/dreaming/...), not ~/.claude/dreaming/..., and never ran for four hours. Land on the file the launcher names; count it only when a live row shows it"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T08:49:51+02:00
  status: verified
  evidence: "12_cognitive_architecture/brain_improvement/agent_run/mirror_rate/live_vs_repo1.txt"
  lesson: true
---

**What happened (12 Nov 2026, an agent).** At 04:19 I wrote a tested patch (the memory mirror claims in batches
of 25) over `brain-repo/12_cognitive_architecture/dreaming/memory_mirror/memory_mirror.py`, recorded
"Live sha 97b3668a" and filed [[memory_mirror_claims_in_batches_six_mesh_calls_for_sixty_files_2026_11_12]]. The task
BrainMemoryMirror runs `~/.claude/dreaming/memory_mirror/memory_mirror.py` (its `launch_mirror.vbs` names
that path). The live file stayed at b339529484aa for four more hours: every run still took a claim and an assert per
file, the "watch the next live run" check could not have seen the patch, and the repo copy sat changed and unpushed.

**How it was found.** At 08:33 I went to patch the mirror again, hashed both files before copying, and they differed.

**Fixed.** 08:39:35: the batch patch plus a new one (the listing call's rate headers in the `plan` and `list_fallback`
log rows) landed on the live file, sha b8389e56483091d4, backup `memory_mirror.py.bak_batchrate_20261112`, the same
bytes in the repo and pushed (brain main b3a38e9412f4). Tests on the combined copy: batch claims 16 of 16 on a
throwaway mesh, rate headers 5 parts with the live file failing the same check. First live row, 08:42:28:
`list_fallback` 403 with `rate: remaining 0, limit 5000, used 5206, reset_at 08:43:58`, so the patch runs, and the
REST quota of the shared token was spent at that minute. Before, that row said only "403".

**The rule.** The file to land on is the one the launcher names. Read the launcher (the .vbs, the task action, the
hook list) before copying, and count a landing only when a live row or log line shows the new code ran. A repo path
that mirrors a live path is a copy, not the target.

**Sweep.** `live_vs_repo.py` (agent_run/mirror_rate/) compares every script under the repo's dreaming folder with
the same path under ~/.claude/dreaming: 977 pairs, 5 differed at 08:41. Repo newer (the same shape):
gh_offload/gh_offload.py (told an agent) and library_push/library_push.py (a tool of the deleted research box).
Live newer (landed, never pushed): google_movie_money_hook.py (told an agent), graph_fire/monitor.py and
job_cycle/job_proc.py (6 Nov; I pushed the live bytes).

**Size of the doubt.** The batch path itself (2 or more files in one run) has not yet been seen on a live run; the
08:42 run skipped at the listing. Read the next run with a batch in `memory_mirror/memory_mirror.jsonl`.

