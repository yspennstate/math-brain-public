---
name: fleet_reply_refused_as_taken_when_own_mesh_session_lapsed_2026_11_10
description: "[VERIFIED] No: 'another agent on this computer is answering' from a fleet --reply-to meant my own mesh session had lapsed (exit 3 'is not live'); hello then reply posted; claim_reply now says so, test 3/3"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T04:04:38+04:00
  status: provisional
  evidence: "a fleet message POSTED after hello; scratchpad fb_test.py 3/3 new, old fails lapsed case"
---

No: a `fleet_board.py broadcast --reply-to` that prints "another agent on this computer is answering" did not always mean someone else held the reply. On 10 Nov 03:3x it meant my own mesh session had lapsed: the reply claim goes through agent_mesh.py, which refuses any claim from an agent that is not live with exit 3, and claim_reply printed every exit 3 as a holder. Nobody held a fleet message; after `agent_mesh.py hello` the same reply posted (a fleet message, board ok, mirror ok).

The first attempt was also hidden by `| tail -1`, which printed nothing, so the round almost went on as if the reply had gone out. A reply counts as posted only when the output says "POSTED; board ok".

Fix on the Mac's live copy (~/.claude/dreaming/fleet_board.py): an exit 3 whose text says "is not live" now prints "not posted: <agent> has no live mesh session. Run agent_mesh.py hello ..., then reply again." Test with a faked mesh: 3 of 3 on the new copy, and the old copy fails the lapsed case (control). The GitHub copy lives in yspennstate/brain-framework dreaming/fleet_board.py (sanitized, older, same line at 280) and waits for the next daily brain-framework push.

How to apply: in a long loop session, run `hello` before any fleet reply or mesh claim, since presence lapses between rounds.


Related: the hidden refusal is the same pipe failure as [[a_scanner_piped_to_tail_fails_open_2026_09_10]]; a lapsed session also refuses claims as in [[chain_past_claim_two_instances_2026_08_18]].
