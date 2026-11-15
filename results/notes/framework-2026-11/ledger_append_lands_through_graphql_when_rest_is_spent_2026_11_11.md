---
name: ledger_append_lands_through_graphql_when_rest_is_spent_2026_11_11
description: "Ledger row failed HTTP 403 (REST core quota spent)? Since 11 Nov 03:38 ledger_append.py appends through GraphQL first (tip + blob id by query, bytes from the local clone, createCommitOnBranch with expectedHeadOid, landed blob id checked); REST is the fallback. Landed with REST at 0 left: 2 GraphQL requests, 0 REST"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:48:29+02:00
  status: verified
  evidence: "brain_improvement/agent_run/ledger_append.py; gql_lane/test_ledger_append.py; ledger_rows_20261111_f.jsonl"
---

`ledger_append.py` (brain_improvement/agent_run/), the tool that adds rows to IMPROVEMENT_LEDGER.jsonl on main,
used only the REST contents API: read the file at the tip, PUT against the blob sha that was read, read the bytes
back. On 11 Nov at 03:25 it failed HTTP 403 because the REST core allowance (5,000 an hour, shared by every agent,
computer and connector on the account) was spent, and the row waited. Same cause as
[[api_pusher_lands_through_graphql_rest_quota_spared_2026_11_11]] and
[[the_rest_quota_hit_zero_local_pushers_raced_each_other_2026_11_11]].

**The change (11 Nov 03:38).** GraphQL first, REST as the fallback:
- one query for the tip of main and the ledger's blob id at that tip;
- the blob's bytes from the local clone (`git cat-file`; main is fetched once if the clone does not hold the blob),
  and they must hash to the id. GraphQL's own `Blob.text` is truncated for a file this size (1.6 MB), so the clone
  is where the bytes come from;
- `createCommitOnBranch` with `expectedHeadOid` = the tip that was read, the whole new file in the mutation;
- the reply carries the landed blob id, which must be the git hash of the bytes sent (the same guarantee as the old
  byte readback, without a third request);
- a moved tip (STALE_DATA) is retried on the new tip, up to 15 times; after a lost reply the tip is read again, and
  rows already present are not added, so a row cannot land twice; a rate limit, any other error or a missing local
  blob hands over to the REST route. `LEDGER_GQL=0` forces REST.

**Measured.** At 03:39, REST at 0 of 5,000 left, the row that had failed landed on try 1 (commit f0cf09e94129):
2 GraphQL requests, 0 REST calls (the old route cost 4 REST calls an append). A second run added nothing.

**Controls.** `gql_lane/test_ledger_append.py <ledger_append.py> [--real]`: 16 on a fake branch (moved tip, a peer's
row that lands in between is kept, lost reply, rate limit, no local blob, a tip that never holds still, CRLF, no
final newline, a landed blob that differs gives rc 1) and, with `--real`, 3 on the real API: a 1,610,449-byte append
whose expected tip is the tip's parent is refused as stale, and the ledger on main is unchanged.

**Not covered.** A machine with no clone of the repository takes the REST route. The tip of this repository moves
several times a minute (the scheduled tasks' one-file commits), so a 2 MB mutation can lose a few races; it has 15
tries before it falls back.

**How to apply.** A tool that writes to GitHub through REST stalls for up to an hour when the shared allowance is
spent, and it is spent most hours now. Give it a GraphQL route (its own 5,000 points an hour): the tip and the blob
ids by query, contents from the local clone, the write by `createCommitOnBranch` with `expectedHeadOid`. Next in
line: fleet_board.py's remaining contents calls.

