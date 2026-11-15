---
name: method_watch_a_periodic_pass_by_its_output_2026_11_12
description: "[PROVISIONAL] Method: a periodic maintainer (nightly pass, cron, dream section) whose non-run prints the same nothing as a clean run is watched by COUNTING ITS OUTPUT per period from the wake - rows produced per completed day against rows due - and trips on a completed period with input and no output; built 12 Nov 2026 for the prompt-class ledger after three dark spells nobody saw"
metadata:
  node_type: memory
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T02:49:00+09:00
  status: provisional
  priors: "a promise that a pass will run is not a signal; only the pass's product, counted per period by something that runs anyway, is"
  originSessionId: agent-2c25-4a49-9a43-6448840c2424
  modified: 2026-11-12T00:47:19.353Z
---

**The move.** For any job that is supposed to run on a schedule and leave a product (classified rows, a commit, an
index, a log line), put a line in the thing that already runs every wake (hook_liveness.py's DERIVED ARTIFACTS
block) that counts the PRODUCT per completed period against the INPUT due in that period, prints the last few
periods as `period done/due`, and trips when a completed period had input and zero product. Never watch the promise
(the task exists, the script compiles); watch what it left behind. Give the job one full period of grace (day-2
trips alone; day-1 only after the pass's usual hour) so the alarm is not red every morning before the pass runs.

**Where it worked (so far one build, 12 Nov 2026).** The prompt-class ledger: the SWS dream's section P owns
`class_model` on PROMPTS.jsonl, and it went dark three times with no alarm - 07-14/15, 09-08..11 (353 prompts; the
09-12 correction asked for exactly this alarm and nobody built it), 11-08..12 (3,401 prompts). The line installed
12 Nov prints `11-08 0/93, 11-09 0/197, 11-10 0/576, 11-11 0/1578, 11-12 0/172 - DARK 2 completed day(s)
unclassified` from a 16 MB tail read, and adds to the wake's not-clean list. The reflex that goes with it:
`periodic_pass_output_needs_a_freshness_alarm`. Kin incidents, same shape, each found late: the dream's repo commit
silently deferred six days ([[the_dream_has_not_committed_since_08_27_and_its_reason_was_swallowed_2026_09_02]]),
the BM25 index frozen 25.8 h with 136 memories invisible (the first DERIVED ARTIFACTS line), the math hook silent
four days. Dream record: [[dream_2026_11_12]].

**Where it would NOT work.** A job whose product is not countable per period (a judgement, a reflex that fires "when
needed") - there the only watch is a positive control that forces one output. A job whose input is also zero in a
quiet period reads as a clean 0/0 and should not trip (the line requires input > 0). And a tail read bounds what
the wake can see: a period outside the tail is "no rows", not "dark" - the first draft of this very line needed two
dark days in view, saw only one in a 4 MB tail, and printed "ok" over a ledger that was 0 for 3,401 rows.

**The one check that breaks it.** On the night it is installed, the alarm must trip on the live subject (positive
control) and the counts it prints must equal an independent count over the whole file (11-09 197, 11-10 576, 11-11
1578 matched on 12 Nov). A line that is green on a subject you know is dark is the bounded-probe scar
([[port_filter_is_a_bound_never_declare_a_service_down_from_it_2026_08_24]]) pointed the other way. Second
independent case still wanted before this leaves provisional.
