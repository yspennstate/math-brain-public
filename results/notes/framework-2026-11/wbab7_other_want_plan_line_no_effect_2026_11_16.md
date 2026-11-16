---
name: wbab7_other_want_plan_line_no_effect_2026_11_16
description: "Plan line asking for another person's want (turn.py plan --want): does it make a better page? No: mean rank 6.61 against 6.39 blind, p 0.61, 36 pages, four judges. The five-line plan already draws opposing wants; kept as an option, not shown."
metadata:
  type: project
  created: 2026-11-16
  status: provisional
---

Does adding a plan line that asks for "the other want" (a second person who wants something the main person does
not, and what they do about it) make a better page? No, not on a 330-word scene.

Design, with the rules registered before any page was written: `turn.py plan --want` (six lines) against
`turn.py plan` (five lines); six writers an arm (one OpenAI model at normal settings), three new tasks, 36 pages, four
blind judges, and the experimenter's own blind ranking saved before the key was read.

- Mean rank, treatment 6.61, control 6.39 (1 best of 12); the treatment page was better in 149 of 324 pairs,
  p 0.61. Flags: treatment 2, control 4.
- By writer 18 of 36 pairs. The judges split two and two. By task, control against treatment: 5.42/7.58,
  6.50/6.50, 7.25/5.75. The experimenter's ranking: treatment 6.67, control 6.33, same directions by task.
- The treatment arrived: all 18 treatment plans fill the new line with a second person's want and act. The control
  plans show why it adds nothing: line 2 of the five-line plan (a habit or want for each person) already draws wants
  that pull against each other, and in almost every page of both arms somebody asks for something and is put off
  (a reading, not a count).

Room to fail: the same harness found a gap of 3.47 ranks for plan against no plan
([[wbab6_plan_wins_by_rule_second_reader_sees_no_gap_2026_11_16]]). Shuffling arm labels within task, a gap of 1.11
ranks reaches p 0.10 and 1.42 reaches 0.05 (shuffled-gap sd 0.86), so a true gain of one rank would be found about half
the time; judge agreement is weak (0.36, 0.18, 0.56), so half a rank could hide.

Decision, as registered: the default plan keeps five lines; `plan --want` stays as an option marked not shown. The
fault that readers of a long draft named, "people who only agree", belongs to a whole chapter, where everyone the main
character meets speaks for one idea; a single page with two people does not have it, so a page test cannot see a cure.
Earlier checks on finished pages also failed to separate: [[wants1_ask_order_refuse_turns_do_not_separate_2026_11_16]].

How to apply: do not hand writers the sixth line as a tested step. When a reader of a long text says the people only
agree, look at who appears across scenes and what each wants that has nothing to do with the main question; do not add
conflict line by line.

Limits: the judges are one model, the one that wrote the pages; no person ranked anything.
