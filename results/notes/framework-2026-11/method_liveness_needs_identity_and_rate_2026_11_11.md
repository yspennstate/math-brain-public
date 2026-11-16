---
name: method_liveness_needs_identity_and_rate_2026_11_11
description: "Is it running? A name answers the ghost direction badly and the starved direction not at all: take identity (PID/resolved path/lock owner) against a ghost, a rate over a named window against reading a live job as dead"
metadata:
  type: reference
  created: 2026-11-11
  created_at: 2026-11-11T18:59:59+02:00
  status: provisional
  evidence: ""
---

**The move.** A liveness question - is it running, is it still working, is one already going - is never
answered by a NAME or by a SNAPSHOT. It needs two things, and which one you need depends on which way the
answer can be wrong: a **resolved identity** (which process, by PID / full script path resolved against
that process's own cwd / interpreter path / a lockfile owner that still exists) to rule out a GHOST, and a
**rate over a named window** (completions per hour, first-and-last timestamps, bytes written since the last
look) to rule out a CORPSE-READING of something alive. Ask which direction would hurt here, then take that
instrument. Name-only answers the first badly and the second not at all.

**Why both.** Liveness fails in two independent directions and we have repeatedly guarded one while being
bitten by the other:

- GHOST - it says running, nothing is. `pgrep -f "<service script>"` matched the agent's own ssh
  command line and aborted a deployment (2026-07-17 and again 2026-11-11, "third self-match this week");
  "another assemble.py still running" was world_history_series' own `assemble.py` in a different folder, and
  cost ~15 minutes of waiting (2026-09-25); 432 Stop-Process calls chased exited processes pinned by open
  handles (2026-08-23). Instrument: identity.
- CORPSE-READING - it says idle or dead, it is working. a research box read 12 lanes from a wrapper
  `pgrep` while load average sat at 32 on 16 cores - 200 pct oversubscribed, the fleet was FULL
  (2026-08-23); "are the boxes running full time?" was answered NO from correct current-minute numbers
  (zero engines, 10-27 pct util) when an hourly histogram showed ~12,000 lanes in 18 hours
  (2026-08-30); a BelowNormal job at zero CPU on a busy box is queued, not hung
  (`process_ready_at_belownormal_is_starved_not_hung_2026_11_11`). Instrument: rate.

**Where it would NOT work.** When nothing has had time to produce yet, a rate is zero for an honest
reason - a job 30 seconds into a 20-minute first unit has no rate, and demanding one re-reads a cold start
as a death. There, identity is the whole answer. And for a genuinely single-instance resource the cheap
correct instrument is an OS-level exclusive lock (an O_EXCL lockfile carrying the PID, a named mutex), not
any amount of process inspection - this method is for when you are stuck reading someone else's running
world, not for designing a new guard.

**The one check that breaks it.** Name ONE way the liveness answer could have come back different. For a
ghost: the PID, the resolved path, a second machine. For a corpse: widen the window and see whether the
count moves - if it moves, the count was the instrument. If no such way can be named, nothing has been
checked (`check_shares_its_subject`).

**What the 11 Nov REM pass added.** The reflex wall was measured and found ASYMMETRIC in a second sense -
not only ghost-vs-corpse but author-vs-consumer. Of seven phrasings tested against the five relevant
triggers, typing `pgrep -f` fired three reflexes; four of five phrasings of a guard's verdict *coming
back* ("the deployment aborted: the service is RUNNING") fired none. Hence
`liveness_verdict_without_its_mechanism` (instincts_learned.json #371, mode fire, controls 7/7 positive
and 8/8 negative in both raw and `json.dumps` form): it fires when a liveness verdict sits next to a
decision to abort, wait or skip, which is the moment the verdict costs something.

**Links.** [[gist_a_check_that_shares_its_subject_cannot_see_it_2026_08_20]] (the mechanism underneath -
an instrument sharing a channel with its subject), [[a_true_snapshot_that_lies_about_the_night_2026_08_30]]
(the rate half), [[win32process_presence_is_not_proof_of_life_2026_08_12]] (the pinned-corpse half),
[[process_ready_at_belownormal_is_starved_not_hung_2026_11_11]] (the starved half, this week),
[[scar_pkill_matches_the_whole_shell_line_2026_08_23]], [[a_bounded_read_is_a_sample]].

status: provisional - two independent directions each backed by lived cases with numbers, but no number in
this memory was re-derived tonight; they are quoted from the source memories above. What would break it:
a liveness failure that is neither a ghost nor a corpse-reading - for instance a process that is the right
identity and producing at a healthy rate while doing the wrong work entirely.

