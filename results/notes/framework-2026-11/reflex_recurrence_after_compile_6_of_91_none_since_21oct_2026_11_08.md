---
name: reflex_recurrence_after_compile_6_of_91_none_since_21oct_2026_11_08
description: "[VERIFIED] Which compiled reflexes kept failing after compile? 6 of 91 dated reflexes have 2+ later MISTAKES rows naming them (28 rows, last 21 Oct); the mechanical repeats (backslash-dollar claim, scan piped to tail) stopped once a refusal was in code"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T06:04:01+04:00
  status: verified
  evidence: "recur_after_compile_2026_11_08.py on 447 MISTAKES entries, planted-row control; six read by hand"
---

Which compiled reflexes kept failing after they were compiled, by the MISTAKES log? Few, and none since 21 Oct: of the 91 reflexes with an `added` date in instincts_learned.json, 6 have two or more later MISTAKES entries that name the reflex or its source memory (28 such rows in all, the last on 21 Oct). Measured 8 Nov 2026 by an agent for the REM 2026-10-14 open question.

How. recur_after_compile_2026_11_08.py splits MISTAKES.md into 447 dated entries (13 Aug to 7 Nov) and, for each dated reflex, counts entries after its `added` day that name its id or a slug from its source (strict) and entries its trigger regex matches (loose; noisy, e.g. 23 for iced_boxes_1_2_4_current_fleet). Control: a planted row naming a reflex id is found. The question's own example, pkill_f_scans_my_own_shell_line, has no `added` date, so it is not in the dated set; that is a real gap (263 of 354 reflexes have no compile date).

The six, read by hand:
- mesh_claim_resource_escaped_its_own_variable (added 27 Sep): 5 real repeats, 30 Sep to 7 Oct, all on Windows (a doubled backslash before $f collapsed in the Bash tool). A danger_mode refusal landed 30 Sep and still leaked twice, because it read only the text after --resource.
- hand_rolled_temp_index_push_use_push_paths (15 Oct): 3 real, 17-21 Oct, every one a secret scan piped into tail so the pipe passed an errored scan. A hook now refuses a gate piped to a filter ("piped gate").
- read_the_inbox_while_you_hold_the_claim (2 Sep): 3 clear repeats 5-7 Sep (claims held, inbox unread), 3 more rows that only cite it.
- a_neat_mechanism_is_measured_before_it_is_written (27 Sep): 3 rows on 2 Oct, a count sent before its falsifier ran.
- python_rewrite_of_a_text_file_without_newline (27 Sep): 2 real, Windows line endings.
- check_shares_its_subject (20 Aug): 2 plausible.

What it says. The question's split holds where it can be tested: the repeats that went on after compile are mechanical command shapes (the backslash-dollar resource, the scan piped to tail, the text-mode rewrite), and the two that stopped got a refusal in code. The habit-level ones (read the inbox, measure before writing) repeated a few times and then went quiet without a gate. The log itself thinned (293 entries in September, 117 in October, 19 in November so far), so "none since 21 Oct" is partly fewer entries. No new gate is called for by this count.

How to apply: when a reflex's mistake shows up twice after it compiled, and the mistake is a command shape, write the refusal (with both-sided controls) rather than a better banner. Give new reflexes an `added` date so this count can see them.

Related: [[clock_advisory_repairs_66pct_of_slips_rate_flat_103_left_in_records_2026_11_08]] (advisory vs gate on the clock stamp), [[the_ack_gate_mostly_stopped_good_commands_2026_09_25]].

Confound, not separated: the work moved from the Windows machines to this machine in late October, and the backslash-dollar and CRLF repeats cannot happen on the second machine at all. 'Stopped once a refusal was in code' is an order in time, not a measured cause.

The question's own first candidate, found by keyword since its reflex has no added date: MISTAKES entries about pkill -f / pgrep -f matching their own shell line number 23 from 21 Aug to 25 Sep, then 2 more on this machine on 6 Nov (a waiter whose pgrep pattern sat in its own argv). So 'none since 21 Oct' holds only for the dated set; the pkill self-match still recurs and stays the first gate candidate, as the question said.
