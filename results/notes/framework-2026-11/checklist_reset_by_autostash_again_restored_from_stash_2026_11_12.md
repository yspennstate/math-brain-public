---
name: checklist_reset_by_autostash_again_restored_from_stash_2026_11_12
description: "[VERIFIED] Checklist suddenly shows only Sep entries and today's ids restart at 001? A git autostash in the brain tree; restore from the stash"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T18:45:30+02:00
  status: provisional
  evidence: ""
---

12 Nov 18:37:03: a git pull --autostash in the brain-repo working tree (just after the 18:35 commit 'paper audit: 150 min limit') stashed the live task_checklist files as stash@{0} and never popped them. The store fell back to the committed 20 Sep copy (427 entries, ledger 1,561 lines); checklist notes failed with 'no entry', and the hook re-issued T-20261112-001..003. Third time after 19 Sep and 2 Oct (20 Oct had no stash). Sign: state.json under 1 MB, ledger about 1,561 lines, 'git stash list' shows a fresh autostash. Fix used at 18:43 by an agent: task_checklist/restore_from_autostash_20261112.py (under the hook's lock: stash state + stash ledger + post-reset ledger lines, new ids renumbered after the stash maximum; read the ledger with newline='' or the committed-prefix check fails on line endings). 7,575 entries back; T-20261112-001/002/003 became 119/120/121; backups in task_checklist/recovery_20261112/. stash@{0} left in place. Rule unchanged: never pull/stash/rebase/checkout in the brain tree; commit by path and push. Related [[the_checklist_store_was_reverted_by_a_git_autostash_2026_09_19]].
