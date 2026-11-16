---
name: dream_pool_arm_skipped_the_usage_governor_under_python_s_2026_11_10
description: "Pool log says 'governor check failed ... No module named psutil'? The caller ran the pool under python -s (hides the user site where psutil lives) and the governor fails open. The dream did until 10 Nov 09:24: rem_arm_order.py now imports _usersite, run_dream.ps1 launches the pool without -s."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T09:26:15+02:00
  status: provisional
  evidence: ""
---

Pool log says "governor check failed for claude2: No module named 'psutil'"? The caller started the pool with `python -s`. Until 10 Nov 2026 09:24 the dream did, so its pool arm was never held by the usage governor.

**The bug.** `claude_pool.governor_allows` imports `usage_governor`, whose `pool_sessions()` imports psutil. psutil is installed only in the Roaming user site, and `python -s` hides that site. The import raised, and `governor_allows` answers `(True, "governor unavailable")` on any exception. `run_dream.ps1` ran both `rem_arm_order.py` (which loads the pool to pick an account) and `claude_pool.py exec auto` (which starts the pool session) under `-s`, so the weekly-limit hold on a pool account was skipped at both steps.

**Measured.** A probe that calls `governor_allows` for the three pool accounts: under `-s` all three "allowed (governor unavailable)"; plain python: one allowed, one refused ("claude3 is at its weekly limit until Tue 10 Nov 18:00"), one allowed with no fresh reading. `claude_pool/logs/pool.log` has the fail-open line on 4, 5, 6 and 9 Nov (two each night, the dream's pool arm) and 127 + 65 on 13 and 23 Oct.

**The fix (dream files only, the pool's files and policy untouched).**
- `rem_arm_order.py` 90bc603ed551a8ed (was d7701dca5b6fba79): imports `_usersite` (the shim that re-adds the user site) before it loads the pool; prints `# governor: UNAVAILABLE ...` into the `rem arms:` lines of the dream log if the governor still fails open; selftest 21 checks, two of them live (psutil imports under `-s`; the live pool's governor answers).
- `run_dream.ps1` efa218043cd1b7c6 (was 191eb02cd67d21ca): the pool launch is `python claude_pool.py exec auto`, no `-s`.
Controls both ways in the scratch area: without the shim file the selftest fails on the two live checks and the run prints the UNAVAILABLE line; with it 21 of 21 pass and the output is the same with and without `-s`. Backups `*.bak_govshim_20261110`.

**What it leaves open.** Any other caller that starts `claude_pool.py` or imports it under `python -s` still fails open (none found in `~/.claude/dreaming` or the pool folder on 10 Nov). The durable fix is in the pool: a missing psutil should be a loud state there, not "allowed". Not mine to change; told on the mesh.

**The general form.** A guard that fails open on an import error is only as present as the interpreter flags of whoever calls it. When a launcher uses `python -s`, `-S`, `-I` or `-E`, run the guard once under the same flags and read its answer, not its exit code. Related: [[dream_rem_died_on_weekly_limits_arms_now_by_live_usage_codex_last_2026_11_10]].

