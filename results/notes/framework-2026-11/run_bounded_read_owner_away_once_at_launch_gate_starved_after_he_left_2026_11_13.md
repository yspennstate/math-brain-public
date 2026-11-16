---
name: run_bounded_read_owner_away_once_at_launch_gate_starved_after_he_left_2026_11_13
description: "Bounded job (regression gate, dream, hourly index) starved or INCONCLUSIVE though the owner left hours ago? run_bounded read the away verdict once at launch; since 13 Nov it raises the job to Normal once the owner leaves"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T06:17:00+02:00
  status: verified
  evidence: "regression_gate_bounded.log 13 Nov 04:16-05:57; test arms A and B; live sha 6496c4d2b19511ae, backup run_bounded.py.bak_lateraise_20261113"
---

Bounded job (regression gate, dream step, hourly index) slow or INCONCLUSIVE all night although the owner left hours ago? Until 13 Nov 2026 run_bounded.py asked "is the owner away" once, at launch. A job that started while the owner was at the keyboard kept the caller's BelowNormal class for its whole run, however long the owner had been gone.

**What happened.** The math-brain regression gate (task BrainMathRegressionGate, regression_gate_launcher.vbs, RUN_BOUNDED_NORMAL_PRIORITY=1) started 13 Nov 04:16 with the owner present, so run_bounded logged "owner present - the NORMAL CPU raise is honoured only while he is away" and kept BelowNormal. The owner left about 04:29 (owner_idle_s 5798 at 06:05). The gate ran 100 minutes on a full box: hook-path pass 1,565 s, fresh recall 1,036 s, real prompts 724 s, then eval_locate_reach hit its 1,200 s cap, value-in-block hit 258 s, three evaluators were skipped, and the mesh got "regression gate INCONCLUSIVE". The same gate finished clean on 11 Nov (raised to Normal at launch, owner away) and on 12 Nov (present, lighter box).

**The fix (run_bounded.py, the wait loop).** A job that asked for Normal and was refused only because the owner was present is raised - every process of its job object, memory and I/O priority with it - the first time the governor says away; it asks once a minute. One way only: nothing is lowered again when the owner comes back, the same as a job that started while the owner was away. The log line is "run_bounded: owner away now - N of M processes of pid P raised to NORMAL priority". Backup beside the live file: run_bounded.py.bak_lateraise_20261113; rollback is copying it back.

**Controls (rb_late_test.py, the away check stubbed, the live state file untouched).** Positive arm: the test process drops itself to BelowNormal, the stub says present at launch and away after; the child read 0x4000 for two rows, then 0x20 for itself and for a grandchild it spawned for seventeen rows; the raise line is in the log; rc 0. On this box the BelowNormal rows took 30 s each and the Normal rows 7.8 s, the same loop. Negative arm: the stub says present throughout (asked four times); all seven rows the child wrote read 0x4000 for itself and the grandchild, no raise line is in the log, and the job ran into its 200 s cap at about 29 s a row, so that arm's rc is 124 and the test script prints FAIL for it on the rc alone. Read the rows, not the rc.

**What it does not change.** A job that never asked for Normal stays where it started. While the owner stays at the keyboard the job stays BelowNormal and the gate's deadline-partial samples are still the design. owner_away() still reads a stale or distress state as present, so a governor in distress keeps everything low.

Seventh case of [[gist_belownormal_starvation_on_a_saturated_box_2026_11_13]]; the rule it respects is that no running work is stopped to free resources (nothing is stopped, the job is only scheduled).

