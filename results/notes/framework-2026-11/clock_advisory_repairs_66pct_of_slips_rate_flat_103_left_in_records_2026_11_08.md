---
name: clock_advisory_repairs_66pct_of_slips_rate_flat_103_left_in_records_2026_11_08
description: "[VERIFIED] Does the clock-stamp advisory change anything on the Mac? Not the rate (20-96 fires a day, 29 Oct-8 Nov, no trend), but 286 of 436 real slips were repaired within 3 calls; into records 151 of 254, so 103 stayed wrong in ten days"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:56:03+04:00
  status: verified
  evidence: "clock_advisory_follow_2026_11_08.py on 535 fires, 523 matched to their call; control finds the 05:53:20 W111 fire; 10+10 hand-checked samples"
---

Does the clock-stamp advisory change anything on the Mac? It does not lower the rate of fast stamps, but it gets about two of every three repaired: of 436 real slips from 29 Oct to 8 Nov, 286 were fixed within the next three calls. Slips into records that stay (status lines, checklist notes, memories, mesh sends) were fixed 151 times of 254, so about 100 stayed wrong in ten days. Measured 8 Nov 2026 by an agent for the REM 2026-10-09 open question.

How. clock_advisory_follow_2026_11_08.py reads every fire in ~/.claude/compute/clock_stamp_hook.log (535, 29 Oct to 8 Nov), finds the tool call it fired on in that session's transcript (the last call at or before the fire that carries the flagged stamp; 523 matched), and reads the next three calls. A fire counts as repaired when one of them edits or corrects that stamp (sed, old_string, "Correction", "should read"), or sends the same call again with the stamp gone. A fire is benign when the call it fired on is itself a sed or edit of the stamp (87 of 523). Control: it finds this session's own 05:53:20 fire on the W111 status line stamped 06:03.

Numbers:
- Fires per day, 29 Oct to 8 Nov: 20, 64, 59, 77, 24, 96, 40, 36, 44, 50, 25 (the last day is partial). No trend. As on Windows in Sep-Oct, the habit itself does not move.
- Real slips: 436. Repaired within 3 calls: 286 (66%).
- Into persistent records: 254, repaired 151 (59%), left 103. Elsewhere (scratch files, wait loops): 182, repaired 135 (74%).
- Hand check: of 10 sampled repairs under a looser first rule, 7 were real and 3 were retries that still carried the stamp; the rule above drops those. Of 10 sampled "left" persistent slips, about 8 are real fast stamps left in checklist notes or status lines; 2 are calls the persistent pattern caught too loosely (a git fetch, a build command).

What it means for the gate the question proposed (block Write/Edit/heredoc into records, advisory elsewhere): the gate would catch about 10 slips a day that the advisory lets through, at the cost of the benign class it must exclude (50 seds on records in ten days, about 5 a day). The advisory is read, not read past, about 60% of the time on records, so the earlier "zero change" was about the rate, not about whether agents act on it. Building the gate is a hook change; it stays a proposal.

How to apply: when the advisory names your stamp, fix it in the next call (a sed with the shell's date, or a correction line). Better, stamp from $(date '+%H:%M') inside the command itself, which the hook never flags.

Related: [[clock_stamp_hook_blind_to_dated_stamps_and_run_ids_2026_11_01]], [[the_ack_gate_mostly_stopped_good_commands_2026_09_25]].

