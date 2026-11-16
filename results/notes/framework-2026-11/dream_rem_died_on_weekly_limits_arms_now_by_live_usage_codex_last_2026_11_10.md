---
name: dream_rem_died_on_weekly_limits_arms_now_by_live_usage_codex_last_2026_11_10
description: "Dream REM dies / journal is a partial stub / log says only is_error=True? 37 REM results since 20 Oct: 4 ok, 15 weekly limit on every Claude login, 18 watchdog cuts. Since 10 Nov the arms are ordered by live usage (rem_arm_order.py), Codex is the last arm (rem_codex_arm.py), the reason is logged"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T05:44:44+02:00
  status: provisional
  evidence: ""
---

The dream's REM pass keeps dying / the journal is a `_partial` stub / "is_error=True turns=1 cost=0" in a dream log? Read this first.

**What was measured (10 Nov 2026, an agent).** 37 saved REM results since 20 Oct (`~/.claude/dreaming/logs/dream_2026*.out.json`): 4 ok, 15 "You've hit your weekly limit", 18 empty (cut by the 45-minute watchdog). On 5, 6 and 9 Nov the main login and both pool accounts (claude2, claude3) were spent together, so the pool arm fell back to the main login and met the same wall. 5 of the last 14 journals are stubs. The dream log printed only `result: is_error=True turns=1 cost=0`, so the cause had to be dug out of the .out.json files.

**What changed (live 05:40, run_dream.ps1 sha256 70e7e9835dbcdff2, backup `.bak_remarms_parts_20261110`).**
- The reason is logged: after an errored result the log carries `result text: <first 200 chars>`.
- `rem_arm_order.py` runs before the first REM launch. It reads the live usage of the main login (the one the open terminals use; owner 05:29: a note that other open terminals could serve as a fallback) and asks the pool which account has room. A login with usage goes first: main first when it is allowed; the pool on Fable then Opus when main is refused; Codex first when every Claude login reads spent. No reading keeps the old fixed order. Costs about 20 s. Log lines start `rem arms:`.
- `rem_codex_arm.py` is the last arm (`codex:gpt-6.1-sol`): one `codex exec` at normal speed (service_tier default, both fast modes off), high effort, no window, BelowNormal, hooks off, 40-minute cap, and it prints the same result json the dream parses. Its account is `~/.codex-img-acc4` unless `rem_codex_home.txt` beside it or `REM_CODEX_HOME` names another. Real one-turn test at 05:29: rc 0, 97 s, is_error false. With hooks on, that test filed the prompt as an ask of the author's (a checklist task, dropped), which is why hooks are off.
- `persist_batches.py` + a block in run_dream.ps1: when the staged secret scan cannot run because the set exceeds its bound ("bounded total scan size"), the set is committed in parts that each pass the same scan. Not yet seen in a real persist.

**Controls.** rem_arm_order.py --selftest 15 checks; rem_codex_arm.py --selftest 13; persist_batches.py --selftest 15; run_dream.ps1 parse errors 0. Live reading at 05:38: main allowed, 18% of the week used; claude2 free; claude3 refused until 18:00.

**Not yet proven.** No dream has run on the new file. Check the next dream log for the `rem arms:` lines and, on a failed attempt, the `result text:` line. The 18 watchdog cuts are a separate cause (a slow box, sessions with 0-5 turns in 45 minutes) and are not fixed by this. The REM model is still claude-fable-5-1[1m]; moving it needs a one-turn test first. `python -s` hides psutil from the pool's governor check (small, open).

**What would change this.** A night where main reads "allowed" and the first attempt still dies on a limit means the reading is wrong for the dream's model; then order by the model's own limit, not the login's.


**Added 10 Nov 08:5x.** The Codex arm tries the picture-free brain accounts in this order: acc4, acc3, acc5, acc2 (`DEFAULT_HOMES` in rem_codex_arm.py; `REM_CODEX_HOME` or rem_codex_home.txt overrides; acc6 is never in the list). It refuses to start under 6 GB of free physical memory or over 92 pct commit (it was 2.5 GB) and says so in the dream log as "codex arm held by its memory gate". Both are live and on GitHub main.
