---
name: runtime_module_imported_by_the_prompt_hook_edit_a_copy_then_replace_2026_11_11
description: "Editing a project_memory runtime module in place? If hook.py reaches it by import (review -> sources), a bad edit breaks the author's prompt hook: build a copy, py_compile, os.replace"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T06:58:59+02:00
  status: verified
  evidence: "session agent 11 Nov 06:32: py_compile SyntaxError sources.py:876; grep shows review.py:15 from .sources import EVENT_PROJECT_CACHE; hook.py imports review"
  lesson: true
---

11 Nov 06:30: I edited ~/.brain-framework/runtime/project_memory/sources.py in place with the Edit tool. One edit closed a docstring a paragraph early, and the file did not compile for about two minutes (SyntaxError at line 876), until the verify step caught it. sources.py looked like the hourly pass's module only. But hook.py imports review.py, and review.py imports sources.py (EVENT_PROJECT_CACHE), so the author's per-prompt project-memory hook would have failed at import for any prompt in that window. The running hourly pass was safe only because it had loaded the module at 06:06.

How to apply: before editing a runtime module, grep who imports it (grep -n "from .<module> import" project_memory/*.py) and check whether the chain reaches hook.py or any other per-prompt hook. If it does, never edit it in place. Build the edited copy beside it (<file>.new-<pid>), py_compile it, then os.replace it onto the live file, as scratch area patch_review.py did for review.py at 07:00. A failed compile then leaves the live file untouched.

Related: [[hourly_hydrate_replay_walk_cached_by_git_tree_2026_11_11]], [[run_bounded_restores_io_priority_for_owner_present_scheduled_jobs_2026_11_11]], [[windows_scandir_dir_mtime_is_stale_parent_index_2026_11_11]].

