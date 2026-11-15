---
name: ab_arm_treatment_failed_to_load_and_the_run_went_on_2026_11_11
description: "A/B or brain-vs-no-brain arm scored as treated when its treatment never loaded? Launcher must stop on the install step and verify presence; brain.py remember refuses --mesh-agent without --repair-index"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T00:51:39+02:00
  status: verified
  evidence: "HH1/lessons_filed.log: five rc=1 lines, 11 Nov 00:4x"
---

An A/B arm whose treatment fails to load runs anyway and gets scored as the treatment, unless the launcher stops on the load step's exit code.

11 Nov 2026, harder grand hunt pilot HH1 (an agent): pilot_harder.sh filed the brain arm's five lessons with export_lessons.py file, which passed --mesh-agent to brain.py remember. remember accepts --mesh-agent only together with --repair-index, so every filing exited 1. The launcher never read that exit code and started all three arms. Arm A ran with hooks on and no lessons: the brain arm without its brain. Caught by reading lessons_filed.log while the sessions were running, before any score was quoted.

How to apply:
- A step that installs the treatment (lessons filed, hooks on, a model loaded, a flag set) is a gate: the launcher exits if it fails, and it checks the treatment is PRESENT (recall the memory back, read the settings the session will load), not just that the command returned.
- Before quoting an arm, check from its transcript that it saw the treatment (a recall hit, a hook line, the notes file read).
- Do not repair a running A/B by adding the treatment mid-run; it reaches the control arms too (shared brain) and makes the treated arm half-treated. Keep the run as an extra control and rerun the arm (rerun_arm.sh in the grand_hunt folder).
- brain.py remember: no --mesh-agent unless --repair-index; it claims the index itself.


Related: [[grand_hunt_opus_hooks_on_vs_off_measured_the_box_not_the_brain_2026_11_10]] [[gist_a_check_that_shares_its_subject_cannot_see_it_2026_08_20]]
