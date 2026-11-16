---
name: gh_release_not_found_was_core_budget_0_of_5000_not_a_missing_release_2026_11_08
description: "Scar (8 Nov): gh says 'release not found' for a release you just made? Check the shared core budget first: at 0/5000 gh release view/upload print not-found for the 403; gh release list (GraphQL) still showed it"
metadata:
  type: reference
  created: 2026-11-08
  created_at: 2026-11-08T10:30:13+04:00
  status: verified
  evidence: "8 Nov 10:27-10:28: release view 'release not found', gh api 'rate limit exceeded' core 0/5000 reset 06:40:51Z, release list shows the tag"
---

Does gh saying "release not found" mean the release is missing? Not when the shared core REST budget is spent. On 8 Nov 10:27 a `gh release upload` and a `gh release view` on brain-codex-fleet-20261029-real-2026-11-08, created 20 minutes earlier, both printed only "release not found". `gh release list` (GraphQL) still showed it, and `gh api` on any REST path then answered "API rate limit exceeded ... 0/5000", reset 06:40:51Z. gh's release commands turn the 403 into a not-found message.

I first suspected that ghstore's test fake (tests/fake_gh.py, which prints the same words) had landed on PATH; gh was the real Go binary from 28 Oct. Check the budget before the binary.

How to apply: on any gh "not found" for something you just made, run `gh api rate_limit -q .resources.core` and one real REST call on the object. If core is 0, wait for the reset and gate the retry on a real call succeeding, not on rate_limit's own numbers ([[github_rate_limit_endpoint_reads_fresh_while_calls_are_throttled_2026_09_25]]). An upload-then-delete script must stop at the first failed upload (set -e) so a throttled run deletes nothing; real_offload.sh did. Who drains the budget: [[github_quota_drain_78_per_min_is_off_the_mac_rate_limit_reads_noisy_2026_11_01]].

Symptom as an agent meets it (SYMLEAD1, 8 Nov, written from this note alone): gh release upload and gh release view print "release not found" for a release I created minutes ago, but gh release list still shows it. A REST request through gh api reports "API rate limit exceeded", with the core budget at 0/5000.
