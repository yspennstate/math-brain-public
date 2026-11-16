---
name: process_presence_gut_mac_line_pgrep_stopped_lists_2026_11_08
description: "[VERIFIED] 8 Nov: process_presence_is_not_life's 140 Mac fires were pgrep checks and its gut was all Windows; a measured Mac line now goes first (stopped job still matches pgrep; zombie in ps only; pgrep skips ancestors)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:11:13+04:00
  status: verified
  evidence: "pgrep_stopped.py output 8 Nov (stopped listed True, zombie listed False); man pgrep -a; pp_branches.py 108 of 140 on pgrep; reflex_precision.json n 119 on 33 useful 0; instincts.py rc 0, 1 row changed"
---

Does process_presence_is_not_life tell a Mac reader anything? Since 8 Nov about 08:10, yes. Before that its gut named only Get-Process, Win32_Process, taskkill and pinned handles, while all 140 Mac fires from 1 to 8 Nov were pgrep liveness checks (108 matched the trigger on 'pgrep' alone; the other 32 matched past the cut-off in the fire log). Stored judgments: on-domain 33 of 119, useful 0, followed 12.

The gut now opens: "A listed process is not a live one. Mac: a pgrep hit can be a stopped job (ps STAT T) doing nothing, and a zombie (STAT Z) shows in ps but not in pgrep; prove life by the job's own output growing, or ps -o time= advancing between two reads. Windows: ..." The old gut is kept as gut_before_20261108_mac in instincts_learned.json. Recompiled with instincts.py (rc 0, 1 tsv row changed, same ids, 364 load). Script: process_presence_mac_gut.py. Backup: instincts_learned.json.before_20261108_pp.

Mac facts measured before writing the line (pgrep_stopped.py, macOS 15 / Darwin 24.5):
- A SIGSTOPped child still matches pgrep -x and pgrep -f, with ps STAT T.
- An exited, unreaped child shows in ps as STAT Z, and pgrep does not list it.
- macOS pgrep never matches itself or its ancestors unless given -a (man pgrep). A probe `pgrep -f <unique pattern>` from the Bash tool, and from inside zsh -c '...', both returned nothing. So the self-match worry that check_shares_its_subject raises for `ps | grep` does not apply to a bare pgrep here. It still applies to `ps ... | grep` (the grep -c probe counted 2) and to sibling shells.
I nearly wrote "pgrep -f matches the shell running this line" into the gut from memory; the probe showed that is false on the second machine.

Windows readers lose the tail of the old gut past the 600-character clip ("These clear only on reboot. RECALL BEFORE THE FIRST MEASUREMENT."); Windows machines keep their own instincts_learned.json. Same pattern as the compute_distress fix in [[mac_reflex_guts_named_windows_paths_mac_line_past_clip_fixed_2_2026_11_08]]; the four reflexes gated off the second machine the same morning are in [[windows_tool_reflexes_off_mac_3_dropped_1_gated_2026_11_08]].

