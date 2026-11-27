---
name: dream_methods_section_k_named_producer_consumer_2026_11_10
description: "Does the dream write methods or only what happened? Since 10 Nov dream_methods.py builds agenda section K (measured-change memories with no method near them) and the prompts ask for method_* memories; before: 45 method memories in 59,000 files, none asked for. Header pattern: producer, consumer, freshness, failure, test. Not yet seen in a real dream."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T07:27:03+02:00
  status: provisional
  evidence: ""
---

Does the dream write methods (what to do next time), or only what happened?
Until 10 Nov 2026 only what happened. The brain held 45 method_* memories among about 59,000 files, the newest from
29 Oct, and no dream prompt asked for one. Written at the author's request.; and 11 Jul: "make sure that all the memories and methodologies and so
on from all the agents that were working during the night is deeply embedded in the brain".

What exists now (dream_methods.py, live and on GitHub):
- PRODUCER  dream.py calls agenda_section(mems, recent, kind) while it writes DREAM_AGENDA.md, section K. It ranks
  recent memories that carry a measured change ("183s to 22s", "26 -> 32/139", "4x faster") and shows, for each, the
  nearest existing method memory, so the dream extends a method instead of writing a twin.
- CONSUMER  the dream session, through the K paragraph of dream_prompt*.md: it writes or extends method_*.md memories.
- FRESHNESS every agenda build appends one row to dream_methods_log.jsonl (candidates shown, method count).
- FAILURE   an exception is caught by dream.py and the agenda carries a visible "K. METHODS - DEGRADED" line.
- TEST      python dream_methods.py --selftest (fixture corpus: ranking, exclusions, nearest method, the log row).
- STATUS    python dream_methods.py --status (method memories: total, last 7 and 30 days; the last builds).
It reads memory records only and writes nothing but its own log.

That five-line header is the 10x-brain requirement applied to one component: "a named producer, a named consumer,
a freshness rule, a failure state, and a test proving the data path actually ran". Use the same header on any new
dream component.

How to check it worked: after a dream on the new code, `--status` shows a build row for that dream and the method
count has moved, and the journal has a METHODS line. Measured before the change: mistakes were about 10 pct of journal
text against the rule that 30% of the dreaming should be about mistakes, and 5 of the last 14 journals were mechanical stubs
(REM died), so the first thing a methods section needs is a REM that runs
([[dream_rem_died_on_weekly_limits_arms_now_by_live_usage_codex_last_2026_11_10]]).

Related: [[dream_judge_sheet_skipped_builder_killed_at_120s_2026_11_10]], [[dream_catchup_merged_in_scanned_parts_2026_11_10]].
Status: provisional - selftest passes; no dream has run on it yet.

