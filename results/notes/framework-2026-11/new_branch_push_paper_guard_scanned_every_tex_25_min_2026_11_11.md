---
name: new_branch_push_paper_guard_scanned_every_tex_25_min_2026_11_11
description: "[VERIFIED] Push of a new branch to the brain repo stuck 25+ min in pre-push? paper_release_guard listed all 8,320 .tex and git-showed each when the anonymous API was rate-limited; now diffs vs merge-base and caches visibility (0.4 s)"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T17:36:05+02:00
  status: verified
  evidence: "11 Nov 17:3x: push 96 pre-push 25+ min with git show a713fa15:<path>.tex children of github_push_cost_guard.py; ls-tree count 8320 .tex; patched guard --selftest PASS, pre_push on a713fa15 0.4 s, throwaway-repo control reads only the new paper"
  lesson: true
---

A push of a NEW branch to the brain repo (push_frontier.py and every agent that pushes claude-<id>-<topic> branches) sat 25+ minutes in the pre-push hook on 11 Nov 2026. The cost guard calls paper_release_guard.pre_push first. For a new branch (remote sha all zeros) it listed EVERY .tex in the tree - 8,320 in brain-repo - and, whenever repo_is_public could not get an answer from the anonymous GitHub API (403 rate limit, 60 calls an hour shared by every agent on the box, or a timeout), it treated the private repo as public and ran one `git show <sha>:<path>` per paper. On a box where one process start can take 30 s, that is the whole push window. The same push had taken 56 s an hour earlier.

Fixed 11 Nov 17:3x (an agent, claim file:~/.claude/dreaming/paper_release_guard.py, backup paper_release_guard.py.bak_20261111_newbranch):
- a new branch is measured against its merge-base with origin/HEAD, origin/main or origin/master, then its first parent; the whole tree only when none exists;
- repo_is_public keeps each repo's known answer a day in ~/.claude/dreaming/logs/paper_guard_visibility.json, so a rate-limited API falls back to the last real answer instead of "cannot tell: check it" (an unknown repo is still checked).
Controls: the guard's own --selftest passes; push 96's commit now clears the guard in 0.4 s; a throwaway repo with three papers on main and one new paper on a new branch has exactly the new paper read, both with an origin ref and through the first-parent fallback.

How to apply: a hook that is slow on a new branch is usually diffing against nothing. Look for `rsha == zero` / an all-zero remote sha that falls back to `ls-tree -r`, and measure against the merge-base instead. A "cannot tell, so check everything" branch also needs a cached last answer, or a rate limit turns it into the slow path for everyone.

