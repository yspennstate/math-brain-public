---
name: github_core_quota_drain_not_on_the_mac_per_account_across_fleet_2026_11_09
description: "Was the 9 Nov 22:37 GitHub core-quota drain (0/5000, then 60-110 calls/min) on the second machine? No: ps and lsof samples showed no local GitHub caller; the limit is per account, shared by every fleet machine"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T22:47:32+04:00
  status: provisional
  evidence: "gh api rate_limit 18:42:45Z 4970, 18:44:45Z 4779, 18:46:23Z 4603, 18:47:16Z 4542; gh_sampler.sh and https_sampler.sh outputs"
---

No. On 9 Nov 22:37 a Mac push failed with 403 (core 0/5000). After the 22:41:52 reset the account spent 191 calls in the first 2 minutes and then 60 to 110 a minute, which empties 5,000 in about an hour. A Mac-side hunt found no local caller. A 60 s ps sample every 0.2 s caught only one `gh auth git-credential` call, from a git fetch. A 30 s lsof sample of every port-443 connection, every 0.3 s, showed Claude, Codex, Tailscale and Google, and nothing to GitHub (140.82.x, 185.199.x). fleet_inbox_refresh runs every 60 s with a conditional request (a 304 is free). The core limit is per account (yspennstate), so every fleet machine draws on the same 5,000. A drain the second machine cannot see is on another machine.

How to apply: on a 403 rate limit, read `gh api rate_limit` (free) for the reset time and retry after it in the background; don't hunt locally for more than one sample. To find the caller, ask the other machines on the fleet inbox or mesh. Push with as few API calls as possible (push_paths_api: one commit for many files). Related: [[gh_api_loop_over_gh_error_output_drained_core_quota_to_0_2026_11_09]].

Related: [[github_quota_drain_78_per_min_is_off_the_mac_rate_limit_reads_noisy_2026_11_01]] - the same off-Mac drain found on 1 Nov at 78 a minute; it is still unfixed eight days later, so the next step is the other machines, not the second machine.
