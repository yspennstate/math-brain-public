---
name: graphql_moved_tip_has_two_wordings_the_second_sent_pushes_to_rest_2026_11_11
description: "Push fell to the REST lane after 'graphql commit failed (other: FORBIDDEN is at X but expected Y)'? That is GitHub's second wording for a moved tip (moved mid-commit). Since 11 Nov 03:51 the pusher retries it on GraphQL. Hour after the GraphQL lane: 276 pusher REST calls vs 1,566 before; 201 of the 276 were 8 such fallbacks"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T04:17:30+02:00
  status: verified
  evidence: "brain_improvement/agent_run/gql_lane/patch_gitdata_stale_wording.py, test_gql_lane.py, lane_fallbacks.py; ledger_rows_20261111_g.jsonl"
---

GitHub words a moved branch tip two ways when `createCommitOnBranch` is given an `expectedHeadOid`:

1. `STALE_DATA`, "Expected branch to point to "<oid>" but it did not. Pull and try again." The tip had already
   moved when the request arrived.
2. `FORBIDDEN`, "is at <oid> but expected <oid>". The tip moved while the commit was being made. The REST contents
   API answers the same race with HTTP 409 and the same text.

The GraphQL lane of `push_paths_gitdata.py` ([[api_pusher_lands_through_graphql_rest_quota_spared_2026_11_11]]) knew
only the first. The second was classed "other", and the push left for the REST lane: on 11 Nov at 03:46 one of my
pushes made one GraphQL mutation, got wording 2, and then spent 32 REST calls and four ref tries to land seven
files. The log line was `gitdata: graphql commit failed (other: FORBIDDEN is at 5c3b3e24... but expected
3d413729...); using the REST lane`; both ids were commits that peers on this laptop had landed four seconds apart.

**The change (live 11 Nov 03:51; sha 31c3a5a299a1c771, was 9f661f1c5c39cdc9; backup .bak_stale2_20261111).**
`_gql_kind` reads "is at ... but expected ..." as stale, so the try is repeated on the new tip (still at most 30
tries, still refused when a peer changed one of our paths). `ledger_append.py`'s GraphQL route
([[ledger_append_lands_through_graphql_when_rest_is_spent_2026_11_11]]) reads it the same way.

**The after-measurement that was owed for the GraphQL lane** (this laptop's tally, `gql_lane/lane_fallbacks.py`):

| hour | pusher processes | REST calls | ref tries |
|---|---|---|---|
| 01:42-02:42, before the lane | 52, all REST | 1,566 | 191 |
| 02:50-03:50, after | 44: 32 GraphQL only, 8 fell back, 4 REST only | 276 | 35 |

So 82 pct fewer REST calls from the pusher, and 201 of the 276 that remained were fallbacks after a GraphQL try.

**Controls.** `test_gql_lane.py`: 26 controls, 0 failed on the live file. The new one (the tip moves mid-commit
twice, then a landing: six GraphQL requests and no REST call) fails on the old file with the 03:46 log line.

**Not covered.** I read the cause in one of the eight fallbacks; the other seven left no log I can open, so how
many of them had this wording is not measured. The four REST-only runs are not explained. The account's allowance
is still spent each hour: on 11 Nov 03:43-03:48 it fell by 514 calls in five minutes, of which this laptop's
tally explains 105 ([[the_rest_quota_hit_zero_local_pushers_raced_each_other_2026_11_11]]).

**How to apply.** When a lane hands over to its fallback, print the error it handed over on and read that line
before trusting the lane's share: "used GraphQL" in a tally is not "landed on GraphQL". And a retryable error can
have more than one wording; match on what the message says happened, not only on the error type.

