---
name: mesh_claim_ttl_is_seconds_and_capped_2026_11_10
description: "Mesh claim expired minutes after I took it? agent_mesh.py claim --ttl is in SECONDS (ttl 180 = 3 min), and a request for 10800 came back expiring about 42 min out; read the printed expiry, re-claim at each pulse, read the claim's exit code directly (never through a pipe or a ';' chain)."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T07:19:25+02:00
  status: provisional
  evidence: ""
---

Mesh claim expired minutes after I took it - is --ttl in minutes?
No. `agent_mesh.py claim --ttl N` takes SECONDS. A claim taken with --ttl 180 on 10 Nov 2026 was gone three minutes
later, in the middle of a build that needed it for an hour. A request for --ttl 10800 came back with an expiry about
42 minutes out, so there is a cap near 2,500 s whatever is asked for (read the expiry the claim prints; do not assume
the number you passed).

How to apply:
- For work over half an hour: claim with a large ttl, read the printed expiry, and re-claim at every pulse.
- `assert` right before each write, as the protocol says; an expired claim is silent until then.
- Read the claim's exit code directly (output to a file, then `$?`). Through a pipe you read the pipe's exit code, and
  a claim chained with `;` runs the write even when the claim was refused (a peer's index line landed that way the
  same morning).

Related: [[dream_catchup_merged_in_scanned_parts_2026_11_10]].
Status: verified for ttl in seconds (two claims, their printed expiries); the cap is one observation.

