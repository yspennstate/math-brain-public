---
name: merge_branch_api_403_merge_through_graphql_mergebranch_2026_11_11
description: "[VERIFIED] merge_branch_api.py says 'refused: branch is at - (status 403)' after a branch push? The REST quota is at 0; merge through GraphQL mergeBranch (own quota) with math-brain-build/local/ct_e431/gql_merge.py, read back with gql_readback.py"
metadata:
  type: reference
  created: 2026-11-11
  created_at: 2026-11-11T04:46:37+02:00
  status: verified
  evidence: "math-brain-build/local/ct_e431/push_e29.out (REST 403) and gql_merge29.out (merge 0acdea0d), 11 Nov 04:3x; gh_readback29.out"
---

When the GitHub REST quota for the account is spent, `merge_branch_api.py` cannot read the branch ref and prints "refused: branch is at - (status 403), expected <sha>". The branch push itself went through (git push over HTTPS does not draw the REST quota). Only the merge step fails.

The fix is GraphQL, which has its own hourly budget (about 5,000 points; one merge costs a few). `math-brain-build/local/ct_e431/gql_merge.py` reuses the token from `~/.claude/dreaming/merge_branch_api.py`, reads the branch head through GraphQL, refuses unless it equals the expected oid, and then calls `mergeBranch`:

    python -s gql_merge.py yspennstate/brain-repo <branch> <full head oid> <message file>

Exit 0 means merged, 3 a conflict, 4 anything else. Take the mesh claim `git:brain-repo/main` first and gate the merge on it with `&&`.

`gql_readback.py <files>` compares local files with `main:<folder>/<file>` through GraphQL. A DIFF whose byte gap equals the file's line count is CRLF on disk against LF in git (a builder written by Python in text mode on Windows), not a content change.

Seen: merges 5839c5c6 (E27), 2bd62c98, 0acdea0d (E29, 11 Nov 04:3x) went through GraphQL while REST said 403; REST was back by 03:47 (merge 6c3113af went through the REST path). Related: api_pusher_lands_through_graphql_rest_quota_spared_2026_11_11, the_rest_quota_hit_zero_local_pushers_raced_each_other_2026_11_11.

