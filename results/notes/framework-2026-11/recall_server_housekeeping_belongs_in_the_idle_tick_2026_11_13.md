---
name: recall_server_housekeeping_belongs_in_the_idle_tick_2026_11_13
description: "First recall of a prompt slow by 0.1-0.7 s for no reason in the question? Server housekeeping (safety re-list, superseded cache write) ran on the next caller; both moved to the idle tick 13 Nov, confirmed live"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T11:16:39+02:00
  status: verified
  evidence: "commits de3d1aac dde044e0; server.log 11:02:35"
---

The first recall of a prompt was slow for reasons that had nothing to do with the question: housekeeping that the recall
server did whenever it was next called. Two cases on 13 Nov 2026:

1. The resident folder listing's 600 s safety full listing (0.7 s on 65k entries) ran inside whichever call came next.
   Live it landed on the first call of a prompt at 10:03:41 and 10:18:15 (calls 2.6 and 3.5 s).
2. The superseded cache rewrote its 65k-row listing (marshal 72 ms + write + head, 126-133 ms) on every call that
   followed another agent's write to the memory folder, which is nearly every call.

Both now run in the server's idle tick (brain_recall_server.py main loop, after 8 s without a call, with the call lock
taken non-blocking): brain._rl_idle_refresh takes the listing when it is due within 120 s, and brain._sup_flush_deferred
writes the pending superseded entries (also once after the last call before the server stops, so a successor finds
them). Confirmed live: "idle re-list of the memory folder in 351 ms" at 11:02:35, between calls at 11:01:04 and 11:02:55.

The rule: in a long-lived server, anything whose result the current answer does not need (a disk copy for other
processes, a periodic safety rescan) belongs in the lull, not on the caller. Keep the in-memory copy authoritative
so the deferred write cannot make the next call read a stale disk entry (the head had to move into the memo too,
or the next call would have read the old head and fallen to the slow path).

Switches: BRS_IDLE_RELIST=0, BRAIN_SUP_DEFER=0, BRAIN_RL_KEEP_VER=0. Commits de3d1aac (listing), dde044e0 (superseded).
What would change this: a server killed rather than handed over loses the pending write; the successor then pays one
slow-path call (1-2.7 s), which is the old cost once, not a wrong answer.

