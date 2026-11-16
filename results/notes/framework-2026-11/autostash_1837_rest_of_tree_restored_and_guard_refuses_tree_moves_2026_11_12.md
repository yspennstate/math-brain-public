---
name: autostash_1837_rest_of_tree_restored_and_guard_refuses_tree_moves_2026_11_12
description: "Brain wake says runtime-canonical-drift, or the brain clone's files look days old? An unpopped autostash reset the tree; how the other 1,048 files were restored and the guard that now refuses pull/stash/rebase/reset --hard there"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T19:04:34+02:00
  status: verified
  evidence: "git hash-object verify 1048/1048; guard selftest 14/20; live refuse + allow controls"
---

12 Nov 18:37 an autostash in the the private repository clone (stash c112bb0c, pinned as branch rescue/autostash_20261112_1839) held 1,053 uncommitted files and left the tree at HEAD 5b53e8a. The reflog shows no pull or rebase entry after the 18:35 commit, so the command stashed and then never finished (a timeout between the stash and the pop is enough). The checklist store was restored at 18:43 by an agent. Everything else stayed reset for about twenty minutes, and that is what the wake alarm "runtime-canonical-drift" on bm25.py, brain.py, hook_liveness.py and spread_recall.py was: the canonical copies under 12_cognitive_architecture/dreaming had gone back to their committed versions while the live files had not moved.

What I did (an agent, 18:50-18:57, claim topic:autostash-1837-restore-nonchecklist):
- Classified each path of `git diff --name-status base..stash` by `git hash-object` of the working file against the stash, base and HEAD blobs. 1,044 were still the reset version with HEAD equal to the stash base, 4 had been rewritten since (the three checklist files and fei_papers_agent/LOOP_STATE.md), 1 was a deletion recorded in the stash (left alone).
- Wrote the safe class back from `git cat-file --batch` (raw blobs; core.autocrlf is false and no path has a filter attribute), checking that the bytes hash to the stash blob id before each write and that the working file was still the HEAD blob. Index untouched. 1,048 non-checklist files now hash to their stash blob (verified with the same hash-object instrument). The four brain sources match the live files again.
- Scripts and log: 12_cognitive_architecture/audits/reports/2026/11/12/autostash_1837_restore/ (restore_log_pass2.json covers the last 168 files; the first 873 were written by a run that crashed on a too-long backup path before it wrote its log, and are covered by the final verify).

Two mistakes of mine on the way, both caught by the verify step:
- `git cat-file --batch --filters` on this git prints the header and then dies with "missing path" when fed rev:path lines. My first pass trusted the header, read nothing, and wrote an EMPTY file over 01_ai_consciousness/claude/CLAUDE.md (a mirror; repaired in the second pass). A restore must check length and blob hash before it writes, and stop at the first bad header.
- A backup tree under the audit folder doubled the path and hit WinError 206. The bytes being replaced were HEAD's blob, which git already holds, so no file backup was needed.

The guard: brain_checkout_guard.py (PreToolUse, Bash and PowerShell, run by hook_dispatch) now refuses pull, stash (except list/show), rebase (except --abort), reset --hard and merge --autostash when the git command's own target (its -C, else the last cd before it, else the session cwd) is the brain clone. Selftest 14 refused / 20 allowed; live controls both ways (it refused a test command of mine that contained the pull text; a status call passed). The reflex a_tree_touching_git_command_in_the_shared_brain_repo had fired on the 2 Oct command and was not obeyed; a reflex asks, this refuses. NOT covered: Codex sessions (codex hooks.json does not run this guard; adding a Codex hook needs the author's /hooks trust review) and git run by scripts outside a tool call.

What would change this: if the dream's own sync or a launcher needs one of the refused verbs through a tool call, it will be refused; the fix is the temp-index push in the refusal text, not an exception.

Related: [[checklist_reset_by_autostash_again_restored_from_stash_2026_11_12]], [[the_checklist_store_was_reverted_by_a_git_autostash_2026_09_19]], [[brain_repo_worktree_is_13gb_use_temp_index_2026_09_28]].

