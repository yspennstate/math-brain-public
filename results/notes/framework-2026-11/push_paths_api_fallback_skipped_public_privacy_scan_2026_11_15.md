---
name: push_paths_api_fallback_skipped_public_privacy_scan_2026_11_15
description: "[VERIFIED] Public push refused by [push-privacy] yet the text is on GitHub? push_paths.sh's API fallback skipped the pre-push hook; fixed 15 Nov 2026"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T01:27:23+02:00
  status: provisional
  evidence: ""
---

push_paths.sh falls back to the GitHub API (Git Data, then contents) when the tip race is lost. The API lanes never run git's pre-push hook, so github_push_cost_guard's private_text_check was skipped: on 15 Nov 2026 00:52 a batch the hook had refused six times landed through the API lane. Fix, same hour: the fallback runs private_text_check on C0 against PB before any API call and refuses on failure; ALLOW_PRIVATE_TEXT=1 is the same door. Tested both ways (refuses the bad batch, passes a clean one). Lesson: every lane that writes to a remote must run the same checks as the main lane; a fallback that skips a guard turns a refusal into a delay. Also: run the guard's own regex in the porting step (mbp_port.py GUARD lines) so the refusal never happens. History was not rewritten (force push on a shared public repo). status: verified. Related: [[a_hook_tested_with_plain_python_fails_open_under_dash_s_2026_11_11]]
