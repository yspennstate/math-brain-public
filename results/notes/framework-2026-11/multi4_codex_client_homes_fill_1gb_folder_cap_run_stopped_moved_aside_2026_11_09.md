---
name: multi4_codex_client_homes_fill_1gb_folder_cap_run_stopped_moved_aside_2026_11_09
description: "[VERIFIED] No (MULTI4, 9 Nov): a three-arm pilot does not fit the harness 1 GB folder check; per-step Codex client homes (~2.3 MB, ungraded) filled it at BRAIN's 182nd diagnosis and the launcher stopped 14:02; moved aside to MULTI4-CLIENTSTORE, resumed 14:39"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T14:39:19+04:00
  status: verified
  evidence: "runs/multi4_pilot01_codex_launch.1.log; harness/run_step.py:114; incidents/20261109_1402_disk_reserve_resume.txt; 199 dirs 463.3 MB moved"
---

Does a MULTI3/MULTI4-style scored run fit its harness's 1 GB worker-folder check for a whole three-arm pilot? No (MULTI4, 9 Nov 2026, an agent).

Each Codex step leaves a client home (config, sqlite state, a 480 KB models_cache.json, 400 KB of skills) of about 2.3 MB. By BRAIN's 182nd diagnosis the run tree was 477 MB, 428 MB of it client homes, and with the 361 MB sandbox memory and the 40 MB index staging copy the check in harness/run_step.py:114 refused. The launcher then stopped with "Unrecorded infrastructure failure". A full pilot is 549 diagnoses plus 93 repairs, about 1.5 GB in all.

grade.py never reads step*/client, so moving finished client dirs out of the worker folder frees the space without touching the frozen harness. I moved them to workers/MULTI4-CLIENTSTORE, with the same relative paths and a manifest, and a 15-minute sweep keeps the folder under the cap. The step the check refused started no model, so resuming is not a retry. The client homes can hold an env copy, so they stay local and never go to GitHub.

Two process lessons. At 13:30 I saw the launcher pid alive, and for 35 minutes after it died I kept reporting "step 2 under way" from that one read. Check the pid every round, not once. And size a harness's disk check against arms × tasks × per-step bytes before launch, not after the first arm.

Related: [[multi4_phase_all_runs_three_arms_in_turn_grading_late_harness_frozen_2026_11_09]] - the same run's timing and freeze.

