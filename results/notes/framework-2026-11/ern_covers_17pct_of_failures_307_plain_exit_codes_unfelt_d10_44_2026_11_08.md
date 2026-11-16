---
name: ern_covers_17pct_of_failures_307_plain_exit_codes_unfelt_d10_44_2026_11_08
description: "[VERIFIED] No ledger feed (8 Nov): D10 #44's bets-from-errors is refused by design (no denominator); the felt error now covers 98 of 588 failed calls in 48 h (was 0), and 307 of the 467 unflagged are a plain Exit code N, 159 of them not grep or display, so an exit-code signature could reach about 45%"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:23:49+04:00
  status: verified
  evidence: "d10_44_ern_missed_failures_2026_11_08.py; ern_calibration.py --since-hours 48"
---

Should every felt error go into the prediction ledger as a missed "no error expected" bet, as 1000-ways D10 #44 asks? No. ern_calibration.py already refuses that by design: outcomes.jsonl holds only the calls where the ERN fired, so the bets would add misses and never a hit. It measures against every tool call instead. The open part of D10 #44 is the measure itself, the felt error's coverage of real failures. Measured 8 Nov by an agent over 48 h on the Mac.

- Coverage is up from 0 of 280 on 30 Oct, when failed calls never reached the hook ([[the_felt_error_never_saw_a_failed_call_posttoolusefailure_2026_10_30]], wired that day), to 98 of 588 failed calls (17%). Precision is 0.22: 346 of 445 fires land on calls that worked. Every miss is a Bash call. Edit and Write failed 7 times each, with no fire, but those are tool refusals.
- The 475 missed Bash failures: 467 match no ERN signature, 5 were held by the 120 s same-signature dedup and 3 are unexplained.
- Of the 467: 307 are a plain "Exit code N" with text that names nothing the signatures know, and about 110 are hook refusals or permission denials. The refusals are feedback in their own right, so the ERN rightly stays quiet on them.
- Of the 307: 125 end in a search or display command (grep, ls, cat, diff, test), where exit 1 often just means no match. 159 end in another command and print text after the exit line, and those are the likely real failures nobody felt.

A signature for "Exit code [1-9]" whose last command is not search or display would take coverage from 99 to about 258 of 574 Bash failures (45%), at a precision nobody has measured. It is a hook change, so it waits as a W112 proposal. Hand-judged 8 Nov (one judge, 25 of the 159, seed 44): 3 are real failures (a Python traceback, a refused mesh claim, an HTTP 409 on a push), 2 unclear, 20 benign: loop tails whose last grep matched nothing, pgrep or which probes, cut after a grep, expected diffs, full-path /usr/bin/grep that the display test misses. Precision 0.12 to 0.20, below the 0.22 the ERN has now, so the signature as proposed would add more noise than signal and should not be built. One narrower flaw: hits_for tests only the first command against DISPLAY_CMD, so cat f | python3 hides a traceback; that hid 4 of the 467 in 48 h, too few to be worth a hook change on its own. Verdicts: d10_44_exit_code_sample_judged_2026_11_08.txt.

Check: d10_44_ern_missed_failures_2026_11_08.py [hours], read only. Control: hits_for finds a planted traceback and nothing on a clean output. Gotcha: hits_for drops every match when the command is a display command (DISPLAY_CMD: ls, cat, grep...), so test it with a real command.

