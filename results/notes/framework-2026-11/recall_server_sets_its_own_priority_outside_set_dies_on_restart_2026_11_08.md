---
name: recall_server_sets_its_own_priority_outside_set_dies_on_restart_2026_11_08
description: "Served recall 5.6 s on a 100 pct box / priority lost after server restart: server now raises itself to AboveNormal in code; median 5.60 -> 2.28 s at equal load"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:25:51+02:00
  status: verified
  evidence: "IMPROVEMENT_LEDGER row 28; brainloop_c462/servedcpu_split2.json"
---

**What happened.** On 8 Nov the workstation sat at 100 pct of its 16 cores (about 26 Claude sessions plus math jobs at Normal). The served recall (`brain_recall_server.py`, Normal priority) spent most of each call waiting for a core: 04:00-06:32, n=238, median wall 5.60 s against median CPU 3.15 s, so about 2.6 s of every call was queueing. In the quiet hours 01-04 the same calls took 2.73 s.

**What fixed it.** Raising the server to AboveNormal by hand at 06:33 brought the median to 2.23 s (n=7). At 06:38 the server restarted itself on a code change and came back at Normal: 6.65 s (n=6). A priority set from outside does not survive the server's own restart or recycle. Since 06:53 the server sets it itself (`raise_priority()` at the top of `main()`, Windows only; `BRS_PRIORITY=normal` turns it off; server.log prints "priority AboveNormal: True"). 06:54-07:16: n=36, median 2.28 s, wait -0.71 s, box still at 100 pct in five samples. Cost: about a tenth of a core.

**How to apply.** A long-lived brain service that restarts itself must set its own priority in code. A one-off `Set-Process` or `wmic setpriority` holds only until the next restart. To tell CPU starvation from slow code, compare wall with CPU per call (`ms` and `cpu_ms` in calls.jsonl): wall well above CPU means queueing, and no code change will fix it.

Evidence: IMPROVEMENT_LEDGER row 28; brainloop_c462/servedcpu_split2.json, row28_before.json; commit 5c04af67. Related: [[belownormal_recall_eval_cpu_starved_not_slow_code_2026_11_08]], [[served_recall_is_cpu_bound_onnx_spin_off_saves_40ms_2026_11_07]].

