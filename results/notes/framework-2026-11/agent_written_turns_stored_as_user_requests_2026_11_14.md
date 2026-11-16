---
name: agent_written_turns_stored_as_user_requests_2026_11_14
description: "A failure mechanism for any system that mines a person's requests into rules: text an agent wrote (a worker's brief, a forked session's first turn, a loop re-fire, a relayed message) enters the request ledger labelled as the person's own, and every rule, hook or summary built from the ledger then carries the person's authority for words they never wrote. 72 rows relabelled in one audit; the checks to run before quoting or mining a line."
metadata:
  type: feedback
  created: 2026-11-14
  status: verified
---

The failure. A ledger records every user turn of every agent session, and several tools mine it: rules and hooks
are drafted from it, a "what the user keeps asking" list is built from it, and a correction flag counts it. A
session started by another agent (a fork, a worker given a brief, a scheduled wake-up, a pasted relay) has a first
"user" turn that the agent wrote. Unless the origin classifier recognises that shape, the row is stored as the
user's own words.

What one audit found (14 November): 72 rows were worker briefs of the form "You are role N of ten ..." or an hourly
fleet check, stored as the user's requests and counted in the summaries. Earlier the same family had taken in loop
re-fires and relayed messages. A flag built on top was wrong the same way: a film title containing the word
"mistake" had been counted as a correction.

Before quoting, counting or mining a line as the user's:
- read its origin field, and run the origin classifier on it when the shape is new;
- treat as suspect a line that addresses "you" as a role, numbers a worker slot or reads like a brief;
- make every rule, reflex or count that cites the user name the line and its time, so a wrong attribution can be
  traced and removed.

Why it matters. A rule derived from the user carries more weight than any agent's opinion. An agent's own brief
promoted to that rank is the most confident kind of error the system can make, and it compounds: the next summary
cites the rule, and the next brief cites the summary.

Related: [[prompt_store_correction_flag_misses_half_2026_11_14]], [[loop_refire_resets_a_session_work_clock_2026_11_16]].
