---
name: dream_takes_15h_capped_tail_steps_budget_now_in_runpy_2026_11_10
description: "Why does a dream take 15 h and why are scheduled dreams skipped? 7-9 tail steps a night ran to the 2700 s cap and were killed; 4 of 14 starts found the lock held; 0 of 10 pushed. Since 10 Nov RunPy skips past the 6 h budget, short-caps after 3 caps, and writes dream_steps.jsonl; dream_health.py reads it"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T08:03:47+02:00
  status: provisional
  evidence: ""
---

Why does a dream take 15 hours, and why are scheduled dreams skipped? Measured 10 Nov 2026 on the last 14 dream logs (`python ~/.claude/dreaming/dream_health.py`).

**What the logs say.** Of 14 scheduled starts, 4 logged "another dream is in progress - exiting" and did nothing. Of the 10 that ran: REM finished 2, journal stub or missing 6, pushed to GitHub 0, median 15.1 h start to finish (longest 24.2 h). The hours are not REM. In the 7 Nov evening dream 15.2 of 17.0 h, and in the 8 Nov evening dream 15.2 of 16.0 h, sat in gaps of 20 minutes or more, and nearly every gap ends in a "STEP CAPPED ... exceeded 2700s and was killed" line: heed_audit trend, ensure_index, orphan_edges, build_series_edges, keyword_edges, the regression gate, embedding_coverage, eval_fok_abstention, eval_memory_age, reflex_audit, growth view refresh, network dream_grow, prompt ledger shards. Seven to nine steps a night ran the full 45 minutes and were then killed, producing nothing. The same dream on a quiet box (10 Nov 02:30) took 3.1 h with no capped step.

**Mechanism.** `run_dream.ps1` runs about sixty steps through `RunPy`, each with a 2700 s cap. The 6-hour tail budget (`TailOver`) was asked by one caller only (bm25). On a starved box each step runs to its cap in turn, the dream holds `dream.lock` for 15+ hours, and the next one or two scheduled starts exit on the lock.

**Fix, live 10 Nov 08:00** (`run_dream.ps1` sha16 628153e0bedff0a9, backup `.bak_stepbudget_20261110`; harness of 16 checks built from the patched RunPy text itself, in the session scratch area):
1. past the 6-hour budget RunPy skips a step and names it (`TAIL BUDGET: ... skipping <step>`, exit 198), except `verify_mirror` and `hook_liveness`, which the persist and the wake need;
2. after three capped steps in one dream, later steps get a short cap (1200 s; `DREAM_STEP_SHORT_CAP_S`), logged once as `STEP CAPS: three steps capped in this dream`;
3. every step appends a row to `~/.claude/dreaming/dream_steps.jsonl` (stamp, step, seconds, exit, state ok / failed / capped / skipped_budget / skipped_stop / threw).

On the 8 Nov pattern (13 caps) this is about 5.6 h of waiting instead of 9.75 h, and the budget ends the tail at 6 h.

**How to read it.** `dream_health.py` (table, `--summary`, `--record`, `--steps`, `--selftest` 36 checks) gives one row per dream (REM outcome and arm, journal real or stub, judge rows, methods, persist, capped and failed steps) and, from the next dream on, each step's last state and when it last finished. `brain_status.py` prints the summary under its DREAM line and records a permanent row per finished dream in `dream_health.jsonl`.

**Not yet proven.** No dream has run on the new runner (first one: 10 Nov 10:30). The 1200 s short cap is a first value with no step-duration data behind it; `dream_steps.jsonl` is what will say which steps legitimately need longer. Why the steps starve (59k memory files read per step, BelowNormal priority while the author is at the keyboard) is the cause still open; see [[dream_grow_capped_on_reading_59k_memory_files_now_cached_2026_11_09]] and [[evening_dream_steps_cap_5x_when_kept_belownormal_owner_present_2026_11_08]].

Related: [[dream_rem_died_on_weekly_limits_arms_now_by_live_usage_codex_last_2026_11_10]], [[dream_catchup_merged_in_scanned_parts_2026_11_10]], [[dream_judge_sheet_skipped_builder_killed_at_120s_2026_11_10]].

