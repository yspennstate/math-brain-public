---
name: github_graphql_create_commit_on_branch_lands_when_rest_quota_is_zero_2026_11_08
description: "[VERIFIED] REST core quota 0 (403 rate limit) blocks the Git Data API lander: land with one GraphQL createCommitOnBranch (expectedHeadOid = head read in the same script, base64 additions), verify by GraphQL Blob fetch + cmp"
metadata:
  type: reference
  created: 2026-11-08
  created_at: 2026-11-08T06:39:49+02:00
  status: provisional
  evidence: ""
---

On 8 Nov 06:3x the Git Data API lander and same.py both died with HTTP 403 'API rate limit exceeded' (REST core at 0) while GraphQL had 4,893 points left. createCommitOnBranch landed math-brain-public 4fb59c23 in one call. Read the head oid in the same script and pass it as expectedHeadOid so a moved branch refuses rather than overwrites. Script: a 40-line GraphQL lander (gql_land.py pattern). Verify by fetching the blob through GraphQL (raw fallback past 512 KB, see [[github_graphql_blob_text_truncates_at_512kb_fetch_raw_2026_11_08]]) and comparing bytes. Limit: GraphQL additions are base64 in one request, so keep each landing to a few MB.
