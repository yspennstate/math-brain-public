---
name: shared_github_token_quota_saturates_hourly_not_live_inbox_2026_11_12
description: "Shared GitHub token near 5000/h REST limit by mid-hour: who spends it? Not live_inbox's 3 s 304 polls; mirror ~n+5 per batch"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T16:31:59+02:00
  status: provisional
  evidence: ""
---

Measured 12 Nov 16:13-16:27 (an agent) on the workstation's shared token (credential store git:https://github.com): core used 3811 at 16:13, 4209 at 16:17, 4464 at 16:22, 4979 at 16:27, reset 16:44 - about 85 calls a minute, so the hour's 5000 is gone about 40 minutes into each window and late callers get 403 until reset. live_inbox.py polls every 3 s with If-None-Match on the message tree: 20 conditional GETs (all 304) raised the counter 94 and 77 against 134 for 20 plain GETs in the same 45 s windows; the background (other agents, ~1.5-2.5 calls/s) swamps a 20-call test, so this is consistent with GitHub's documented rule that an authorised 304 is free but does not prove it. memory_mirror.py costs about one call per file plus five per batch (26 files 16:13, 7 files 16:22) - a few hundred an hour, not the spender. A 2-minute Win32_Process tally of new processes showed no single local REST hammer; candidates not measured: release-asset uploads and digest checks of the novel picture offload, and the worker machines if they share this account. push_paths_gitdata.py already waits out a rate 403/429 (Retry-After or reset), so pushes are delayed, not lost. What would change this: a per-caller count (log X-RateLimit-Used before and after each script's calls) - the token has no per-caller breakdown on GitHub's side. Do not run quota experiments late in the window: this test itself spent ~60 of the last 100 calls.

Same pattern as [[the_shared_github_token_runs_dry_every_hour_2026_10_04]] and [[github_core_quota_drain_130_a_minute_suspects_gitdata_pushers_2026_11_09]] (gitdata pushers suspected there; 12 Nov rate ~85 a minute, lower than 9 Nov 130); [[api_pusher_lands_through_graphql_rest_quota_spared_2026_11_11]] is the route that spares REST. New here: the live_inbox 304 poll measured, not the spender.
