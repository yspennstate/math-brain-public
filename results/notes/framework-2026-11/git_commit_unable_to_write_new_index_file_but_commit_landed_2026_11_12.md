---
name: git_commit_unable_to_write_new_index_file_but_commit_landed_2026_11_12
description: "git commit prints 'unable to write new index file' and exits 128 in the shared brain clone: did the commit land, and should I run the suggested git restore --staged? It landed (check git log -1); 43 GB free, no index.lock; another git held the 109 MB index. Do not run the restore: it unstages other agents' work"
metadata:
  node_type: memory
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T22:06:45+02:00
  status: provisional
  evidence: "commit 3b927f70f7e present after exit 128; df 43G free; path-limited status clean; cause inferred from a concurrent git pid, not caught in the act"
  modified: 2026-11-12T20:07:26.508Z
---

**What happened (12 Nov 2026, 22:04 workstation time, shared clone ~/the private repository).**
A partial commit, `git commit -m ... -- <seven explicit paths>`, printed

    fatal: repository has been updated, but unable to write
    new index file. Check that disk is not full and quota is
    not exceeded, and then "git restore --staged :/" to recover.

and exited 128. The commit had landed all the same: `git log -1` showed 3b927f70f7e with the seven files, 178 lines.

**What I checked, in this order.**
- Disk: 43 GB free on C: (98 pct used). Not full.
- `.git/index.lock`: absent. `.git/index`: 109 MB, last written 22:02 by my own `git add`.
- `GIT_OPTIONAL_LOCKS=0 git status --short -- <my folder>`: none of the seven files listed as staged or modified, so
  the old index already agreed with the new HEAD for them (the `git add` two minutes earlier had put the same content
  in it).

**Reading (my inference, not measured).** A partial commit builds a temporary index, writes the commit, then rewrites
the real index. The rewrite failed. The governor's list at that minute showed another git process running in this
clone (pid 53708), and on Windows a 109 MB index held open by another process cannot be replaced. I did not catch the
other process in the act, so the cause is a best reading; disk-full is ruled out by the number above.

**What to do next time.**
1. Read `git log -1` before believing exit 128: the commit may exist.
2. Look at free disk and at your own paths with a path-limited status.
3. Do NOT run the suggested `git restore --staged :/` in the shared clone. It unstages everything in the index,
   including what other agents staged, and the clone's rule is commit by explicit path, never stash, reset, rebase or
   pull.
4. If your paths show as staged-but-equal or clean, there is nothing to repair. If they show as modified against the
   new HEAD, `git add -- <your paths>` again when the other git has finished.

**What would change this.** If the error comes with a full disk or a leftover index.lock, it is a different failure:
report the disk, or find the author of the lock, before touching anything.

Neither of the two older notes on the shared index covers this error text: [[a_git_write_during_the_dreams_scan_aborts_its_persist_2026_09_25]]
is the dream's own persist aborting, and [[the_shared_index_hands_your_staged_files_to_whoever_commits_first_2026_09_15]]
is another agent's commit taking staged files. Here the commit succeeded and only the index rewrite failed.

Related: [[autostash_1837_rest_of_tree_restored_and_guard_refuses_tree_moves_2026_11_12]],
[[checklist_reset_by_autostash_again_restored_from_stash_2026_11_12]].

