---
name: show_or_hold_trial_off_on_mac_allowlist_unported_2026_11_08
description: "[VERIFIED] Did the reflex show-or-hold trial run on the second machine? No, 28 Oct to 8 Nov 02:16: its allowlist primary_ab_eligible_v1.txt was never ported and a missing list holds nothing, silently; restored byte for byte (155 of 166 ids pass the live gates), rows flow again"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T02:17:11+04:00
  status: verified
  evidence: "list absent on Mac since 28 Oct; Mac log frozen at 8,175 rows (15 Oct); after copy: 24.3% held of 33,200 synthetic splits, humility_check 32 PASS, first live row 02:16"
---

The reflex show-or-hold trial ([[show_or_hold_trials_and_the_exact_name_trigger_2026_10_06]], his order of 6 Oct) never ran on the second machine. The trial holds one in four eligible reflexes per (session, reflex) and logs both arms to instinct_primary_ab.tsv, which is the only randomized way to tell whether a shown reflex changes what happens next.

Cause: instinct_prime reads its frozen allowlist from primary_ab_eligible_v1.txt, and a missing list means "hold nothing". The worker machine install copied the hooks but not this .txt (it is in the brain repo at 12_cognitive_architecture/dreaming/). So every Mac fire since 28 Oct went out as "open", with no row and no error. The worker machine's instinct_primary_ab.tsv is the workstation's file as copied at install, 8,175 rows ending 15 Oct 17:29, and its mtime is the install time. GitHub's copy also ends 15 Oct. Whether the workstation still runs the trial is not visible from here.

Fix, 8 Nov 02:16: the list was copied byte for byte from the brain repo. Nothing in the code changed.
- Of its 166 ids, 161 still exist among the 381 live reflexes; all 161 are mode fire with no safety word, and 155 have live charge at most 0.83 (the item gate).
- Split check: 200 synthetic sessions x 166 ids give 24.3% held (designed 25%), and a safety-word id stays open.
- humility_check: rc 0, 32 PASS after the change.
- Live: the first Mac row came at 02:16 (another session, arm shown); the log had not grown since install.
- Off: INSTINCT_PRIMARY_AB=0, or remove the list.

This is the randomized hold-out that D6 #55 ([[scar_notes_flag_risky_calls_11pct_vs_5p9_err_no_prevent_d6_55_2026_11_03]]) said it needed, and the one D6 #71 (somatic-marker validity) needs. The worker machine rows start 8 Nov. Read them only by the trial's frozen rules: from T1_VALID, with the coverage and watermark conditions in the trial memory, session-clustered.

How to apply: when a hook reads a data file whose absence means "off" (allowlists, eligibility lists, frozen banks), a port has to carry that file too. A missing file there is silent by design, so check for it by name.

Sweep, 8 Nov 02:17: of 102 data filenames the second machine's dreaming code joins to its own folder, 26 are absent here; only 2 are in the brain repo mirror (.claim_blocked.json, .retraction_blocked.json), and both are the workstation's per-session state from Aug-Sep that must not be copied. The other 24 are runtime files written on first use or test scratch. So the allowlist was the only one. Script: unported_data_files_2026_11_08.py.

The other two trials of 6 Oct on the second machine: trial 3 (exact-name, exact_name_ab.tsv) runs, and its log was written at 02:15. Trial 2 (memory and place lines) is off together with the whole graph membrane, by the 6 Nov decision in [[graph_membrane_never_enabled_on_mac_no_hook_enabled_file_0_real_fires_2026_11_06]] (no HOOK_ENABLED, no sidecar graph).

Reading it: the trial's reviewed analysis (spec v3) is trial_analysis.py in research-repo scheduled_tasks/work/shared/brain-improvement-2026-10-03/an agent/showhold_20261006/code/. It is not installed on the second machine or in the brain repo, and it uses .claude paths that are the same here. A scratch copy with OUT and CACHE pointed at a scratch folder ran on the second machine at 02:20 in 0.2 s, rc 0. Trial 1 admitted 0 units: 2,967 workstation rows have no transcript on the second machine, 370 have unproven coverage, 41 are pre-coverage, and 5 Mac units were still inside their 30-minute window. Trial 3 had 5,619 exposures (4,361 shown, 1,258 held) in 229 sessions, outcome not wired. Rerun in a week or so, once Mac units close.

Laptop (an agent, a fleet message, 8 Nov 00:3x +02): the trial runs there. Its live log is 5.2 MB, newest row 8 Nov 00:27 +02; the newest 3,000 rows (5-8 Nov) are 2,217 shown and 783 held (26.1%), and its allowlist is present (6,772 B, 6 Oct). Only the brain repo copy of the log is stale (1.1 MB, 16 Oct). So the trial's analysis should read the workstation's live log plus the second machine's rows from 8 Nov, not the repo copy.
