---
name: github_graphql_http_499_on_a_big_mutation_ask_again_2026_11_11
description: "ledger_append.py 'commit failed (other HTTP_499)' then REST 403 and no row? GitHub gave up on the 2 MB GraphQL mutation; since 11 Nov 06:40 408 and 499 are sorted as network (read the tip again, add only missing rows) like a 5xx. 12 controls pass"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T06:42:52+02:00
  status: verified
  evidence: "brain_improvement/agent_run/ledger_append.py, gql_lane/test_ledger_http_codes.py; ledger_rows_20261111_m.jsonl"
---

**Symptom.** `ledger_append.py` prints `graphql: commit failed (other HTTP_499 ); taking the REST route`, the REST route
then fails 403 (allowance spent) and the row is not appended.

**Cause.** On 11 Nov at 06:30 GitHub answered HTTP 499 with an empty body to the 2 MB `createCommitOnBranch` mutation.
The tool sorted HTTP errors as rate (403, 429), network (500 and up) or other; 499 fell in "other", which gives up the
GraphQL route. A 499 or 408 is the server giving up on a slow request, the same situation as a 5xx or a cut-off reply.

**Fix.** `gql()` sorts 408 and 499 as network: the append reads the tip again and adds only the rows that are not there,
so a commit that did land behind the lost answer is not sent twice.

**Measured.** `gql_lane/test_ledger_http_codes.py`: 12 controls pass, among them a 499 after a landing (rc 0, the row on
the branch once, one mutation). The 16 older controls still pass.

**How to apply.** Any tool with a GraphQL write lane should treat 408 and 499 like a 5xx, and must be able to tell on the
next read whether its write landed. One sighting so far; the pusher (`gql/push.sh` lane) and `fleet_board.py` were not
checked for the same sorting. Related: [[ledger_append_lands_through_graphql_when_rest_is_spent_2026_11_11]].


Added 11 Nov 06:55: the path pusher push_paths_gitdata.py had the same sorting and has the same fix (408 and 499 are asked again on both lanes; 8 new controls in gql_lane/test_gql_lane.py; backup push_paths_gitdata.py.bak_http499_20261111). fleet_board.py's own GitHub calls were not read for it.
