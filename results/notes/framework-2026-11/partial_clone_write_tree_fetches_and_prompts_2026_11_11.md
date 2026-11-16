---
name: partial_clone_write_tree_fetches_and_prompts_2026_11_11
description: "[VERIFIED] Private-repo push through a temporary index hung 13 min at git write-tree, then a 'Username for github.com' window: write-tree on the partial clone (filter=blob:none) lazily fetches missing blobs over https"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T08:48:21+02:00
  status: provisional
  evidence: ""
---

11 Nov 08:22-08:38, an agent, push_e40.sh (temp GIT_INDEX_FILE, read-tree FETCH_HEAD, update-index, write-tree, commit-tree, side-branch merge). The brain repo clone is partial (filter=blob:none), so write-tree checks that every blob in the tree exists and starts 'git fetch --filter=blob:none --stdin' for the missing ones. That fetch needs credentials. With the credential manager holding two github.com accounts the GCM get hung for 13 minutes on 1 s of CPU. When I stopped the GCM process, git fell back to git-askpass.exe, which put a username window on screen. Fixes in the script: export GIT_ASKPASS= GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never before any git call (an empty GIT_ASKPASS skips the askpass program), and stop a stuck chain by pid from the top (write-tree down), then remove the temp index's .lock, or the next read-tree refuses. Second trap in the same script: set -e does nothing inside '( ... ) || rc=$?', so a failed TREE=$(git write-tree) ran on with an empty tree; give write-tree and commit-tree explicit '|| exit'. The secret scan refused the empty commit, so nothing bad was pushed. Rerun at 08:42 merged ba75a38014bf, 15/15 read back. What would change this: a full (non-partial) clone, or push_paths.sh, which avoids the hand-built tree. Related [[github_push_fails_two_accounts_in_credential_manager_2026_11_11]], [[git_credential_window_under_git_bash_empty_git_askpass_2026_11_11]].
