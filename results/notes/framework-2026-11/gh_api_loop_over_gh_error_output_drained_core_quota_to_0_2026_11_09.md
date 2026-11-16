---
name: gh_api_loop_over_gh_error_output_drained_core_quota_to_0_2026_11_09
description: "[VERIFIED] No: a for-loop of gh api calls over a list holding gh's own error lines burned ~50 core calls and took the shared quota to 0 at 10:27; check rate_limit and clean the list first"
metadata:
  type: feedback
  created: 2026-11-09
  created_at: 2026-11-09T13:21:06+04:00
  status: verified
  evidence: "an agent session 9 Nov 10:27, rate_limit 0/5000"
---

Is it safe to loop gh api calls over a list built from earlier gh output? No (9 Nov 2026 10:2x, an agent): one for-loop over a list that held gh's own error lines fired about 50 core API calls in seconds and took the fleet's shared allowance (5,000 an hour, already drained by offloads) to 0 at 10:27; every agent's gh calls failed until the reset.

How to apply: before any loop of gh calls, read `gh api rate_limit --jq .resources.core.remaining`, stop if under ~500, build the list into a file and check it has only real items (no 'HTTP 4xx' or error lines), cap the loop, and prefer one recursive tree call or GraphQL over a call per item.

