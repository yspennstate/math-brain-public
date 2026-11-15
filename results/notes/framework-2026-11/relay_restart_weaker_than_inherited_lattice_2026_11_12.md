---
name: relay_restart_weaker_than_inherited_lattice_2026_11_12
description: "RL2 lwe19 lattice restart weaker than inherited checkpoint resume older state"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:46:00+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: As recorded on 2026-11-12, RL2 shift 6 added 0 stations and its handoff warned the next thread to resume an older lattice state because the lwe 19 restart was weaker. The three stations from shifts 7-8 all came from jobs begun in earlier shifts. The source does not isolate how many minutes the restart alone lost.

Why it happened: The newest attempt was not the strongest inherited state. A new thread had to recover the prior work before continuing; later shifts often spent substantial time reaching their first new station.

**Why:** Recency of a checkpoint does not establish its search quality.

**How to apply:** Read the handoff, compare candidate states and resume the stronger older state when directed; preserve the commands and artifacts needed to continue existing jobs.

[[relay_hunt_rl2_warm_87_of_100_first_hour_68_2026_11_12]]

Drafted by Codex worker W02 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

