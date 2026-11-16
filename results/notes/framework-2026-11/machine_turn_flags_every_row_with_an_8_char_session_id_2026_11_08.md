---
name: machine_turn_flags_every_row_with_an_8_char_session_id_2026_11_08
description: "Re-testing stored prompt rows with machine_turn() flags all 3,008 hourly-JSON rows: their 8-char session ids read as synthetic; test by text (is_agent_authored) instead"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T06:18:44+02:00
  status: verified
  evidence: "brainloop_c462/brains_tick_1108.json, 8 Nov 06:01 and 06:02 runs: 3008/3008 by machine_turn, 0/3008 by is_agent_authored"
---

**Trap.** `prompt_origin.machine_turn(text, cwd, session)` treats any session id that is not a full uuid or the ledger's 12-char form (8 hex, dash, 3-4 hex) as a harness's synthetic session. The hourly prompt JSON (`owner_prompts_hourly` output, read by `owner_prompts_hook.load()`) stores the session as 8 hex chars only, so calling `machine_turn` on its rows flags every one: 3,008 of 3,008 on 8 Nov 06:01 (an agent, brain loop tick 52).

**What to do.** Re-test stored rows by their text (`is_agent_authored(text)`), or pass the ledger's 12-char session id. On text alone the same 3,008 rows gave 0 machine rows and 0 loop ticks, so the "important prompts" block (`owner_prompts_brains.py`) was already clean after the 05:28 hourly rebuild.

**Why it matters.** A filter that drops "every machine row" and silently empties a view looks like a successful fix. Count the rows kept, not just the rows dropped: a view that falls to zero is the bug, not the cure.

Evidence: brainloop_c462/brains_tick_1108.json; IMPROVEMENT_LEDGER row 27. Related: [[loop_tick_prompts_were_stored_as_his_words_2026_11_08]].

