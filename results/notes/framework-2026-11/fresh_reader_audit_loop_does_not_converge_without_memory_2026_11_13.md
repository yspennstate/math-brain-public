---
name: fresh_reader_audit_loop_does_not_converge_without_memory_2026_11_13
description: "Paper audited 14 times in a day by fresh readers, must-fix 12..3..6, verdict back to the first? A memoryless read-revise loop never closes: carry findings across rounds (new/still open/reopened), fix the stop rule first, read the series not the last report"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T01:04:36+02:00
  status: verified
  evidence: "loops/agent_loop_1112/AGENT_AUDIT.md entry 8; audits/reports/2026/11/12/paper_audit_ising_perceptron_margin_release_paper_main_9e0c23/REPORT_*_read_*.md"
  lesson: true
---

Ising perceptron margin paper, 12-13 Nov 2026. Found while auditing a finished checklist line (a checklist task,
loops/agent_loop_1112/AGENT_AUDIT.md entry 8).

What happened. The paper was put through a loop: a fresh first-reader agent audits main.tex with no memory of
earlier rounds, the writer revises, the next fresh reader audits. Fourteen rounds ran in one day. Verdict and
must-fix/should-fix by read: 1 REWRITE THE INTRODUCTION 12/19, 2 NOT READY 10/17, 3 MINOR EDIT 8/13, then 10/16,
6/14, 5/20, 6/15, 4/16, 5/14, 3/18, 4/10, 5/24, 6/36, and read 14 REWRITE THE INTRODUCTION 6/34. Must-fix fell to 3
by read ten and rose again; should-fix tripled after read eleven; the last verdict is the first one. A fifteenth
read was registered while the fourteenth was being closed. Each single read was honest and its numbers check
(report line, labels, the sha of the file read).

Why it does not close. A reader told to find faults, who has not seen the earlier reports, finds about half a dozen
in any twenty-page paper. Each revision rewrites sentences, and the next reader objects to the new sentences. The
count per read measures the reader's appetite, not the paper's distance from done. Nothing in the loop can tell a
finding that has survived five rounds from one created by the last edit.

The rule.
- A repeated audit needs memory across rounds. Hand the reader the earlier findings list (not the verdicts) and have
  each finding marked NEW, STILL OPEN, or REOPENED BY THE LAST EDIT. Track still-open plus reopened; that number can
  fall to zero, the raw count cannot.
- Decide the stopping rule before round one: for a paper, two readers in a row with no mathematical must-fix.
  Wording findings go on one list for one editing pass; they are not a gate.
- When the same top-level verdict comes back after ten rounds (here: rewrite the introduction), it is a choice about
  what the paper claims, and it is the author's. Put it to the author once instead of running another read.
- When auditing such a loop, read the series, not the last report. One table of verdict and counts by round shows
  in a minute whether it is converging.

Not checked: whether the individual findings of any read are right. Related:
[[timed_out_audit_inherited_the_previous_report_2026_11_12]] (the opposite fault in the same loop: a read that
carried the previous verdict without reading), [[a_red_that_is_always_red_stops_being_read]].


Addendum 13 Nov 02:3x (reads 15-16, measured): once each read was told what the previous one found (new / still open /
reopened), the series did close - read 16 marked most items STILL OPEN and listed only four must-fix. But it still caught
two false sentences, and one of them was put there by the read-15 fix itself: the introduction paragraph was replaced by
the reader's own draft, which described the fourth condition as an inequality over all functions Lambda, while the
condition is over a two-parameter family (the stronger statement is what the proof shows, not what is assumed). Lesson:
a rewrite taken from a referee's draft is new text and gets the same check as any other new text - read each of its
sentences against the formal statement it paraphrases before the next read. The stop rule held: after read 16 only the
false claims and wrong numbers were fixed (commits 28a2c5a, 3e33823), and the 31 wording items went to the author as one
list. Release node: [[audit_margin_paper_sixteen_reads_release_v2_1_2026_11_13]].
