---
name: git_crash_leaves_index_lock_judged_by_age_and_open_handle_2026_11_10
description: "Every git write in the brain clone says index.lock: File exists and the dream does not clear it? A git.exe crash (0xc0000005, 10 Nov 08:08) left the lock; the old rule wanted no git process alive on the machine, never true here. Clear-StaleIndexLock judges age, an exclusive open and older git processes, then renames; 7 controls pass"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T08:34:30+02:00
  status: provisional
  evidence: ""
---

Every git write in the brain clone fails with "Unable to create .git/index.lock: File exists", and the dream's own cleanup does not remove it? Found 10 Nov 2026.

**What left the lock.** git.exe 2.53.0.2 crashed with an access violation (0xc0000005, Windows Application log, event 1000, faulting module git.exe) at 08:08:03 during a checkout move of local main in ~\private-repo; the 0-byte index.lock is stamped 08:07:53. It is the only git.exe crash event in fourteen days, so the crash is rare, but one is enough: a lock nobody owns blocks `git add`, `checkout`, `reset` and the dream's persist until someone renames it. (Earlier locks set aside the same way sit beside it as `index.lock.stale_removed_*`.)

**Why the dream's rule never fired.** run_dream.ps1 set a lock aside only when it was older than ten minutes AND no git process was alive anywhere on the machine (`@(Get-Process -Name git).Count -eq 0`). On this box that is almost never true: a `git credential-manager get` has been hung since 8 Nov 21:01 (pid 32944, reported, not killed), and other sessions fetch and push all day. So the rule logged "leaving it" and the add below failed.

**The rule now** (`Clear-StaleIndexLock` in dream_git_sync.ps1, called before the persist and at the start of `Sync-LocalMainToAdvertised`): the lock is judged on its own evidence.
1. older than 10 minutes (later of creation and last write);
2. nobody holds it open: an exclusive open succeeds. A writing git keeps the lock file open, so the open fails while it works;
3. no git process that started before the lock was born is still alive, not counting helpers that never write an index (credential, remote-https, fsmonitor). Past 60 minutes rule 3 is waived.
Then the lock is renamed to `index.lock.stale_removed_<yyyyMMdd_HHmmss>`, never deleted, and the log says so.

**Controls** (`test_clear_stale_index_lock.py`, 7 arms, 0 failed): no lock; a fresh lock is left; a 30-minute-old unheld lock is set aside with its bytes kept and `git add` works after; a lock another process holds open is left; a real git (`git update-index --stdin`, which takes the index lock and waits) is left alone with "a process holds the lock open", which is the proof that rule 2 sees a live git; an older live git in another repository keeps the lock under the hour; the same past the limit is set aside.

**Live use.** 08:26:53 the function set the real lock aside ("stale: 19 min old, not held open, no older git process").

**If you meet one by hand:** check its age, try the exclusive open (PowerShell `[IO.File]::Open(path,'Open','Read','None')`), look for a git older than the lock, then rename. Do not delete it and do not kill a git to free it.

Related: [[git_index_lock_stale_in_brain_clone_set_aside_by_rename_2026_11_10]], [[dream_commit_pushed_through_side_branch_server_merge_2026_11_10]], [[gist_a_process_named_is_not_a_process_found_2026_11_10]].

