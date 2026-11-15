---
name: reader_proposed_text_entered_paper_unchecked_2026_11_13
description: "Paper in a fresh-reader audit loop: a reader's proposed statement or proof went into the paper in the reader's wording and the next reader made it a must-fix (or nobody checked it)? Check reader-proposed mathematics yourself before it enters, name it as new to the next reader, list declined items"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T08:17:13+02:00
  status: verified
  evidence: "loops/agent_loop_1112/AGENT_AUDIT.md entries 28 and 29; audits/reports/2026/11/13/paper_audit_planar_switching_two_instability_intervals_paper_main_91d723 (4th read l.280, 5th read section 8); paper_audit_excited_walk_zero_speed_non_transience_paper_main_faff4c (4th read S1)"
---

Two papers on 13 Nov 2026, both in a read-revise loop with fresh first readers (planar switching, five reads;
excited walk, four reads). Found while auditing the finished reads (loops/agent_loop_1112/AGENT_AUDIT.md
entries 28 and 29). A second mechanism beside the one in [[fresh_reader_audit_loop_does_not_converge_without_memory_2026_11_13]].

What happened.
- Planar switching: the fourth reader's should-fix 5 told the author to "state the fact once, as a proposition:
  if A_0 and A_1 are normal and Hurwitz, then lambda(r) ...". The author did, in the reader's wording. The fifth
  reader made that wording a must-fix: lambda(r) is defined only where the limit is shown to exist, and the proof
  gives a pathwise bound, not a statement about lambda. The loop spent a round correcting its own last round.
- Excited walk: the fourth reader's strongest should-fix was two new statements with the reader's own proofs
  ("checked twice"). They were in the paper as a corollary twenty minutes later, and a fifth read was launched on
  it. Checked by hand afterwards, with the survey's hypotheses read: it holds. It was right, but nothing in the
  loop had checked it before the next reader.
- Same day, same paper: a should-fix of the third read (a wrong justification, with the repair written out) was
  left through two rounds, and the fifth reader found it again and wrote the same repair.

The rule.
- A first reader's report is a list of objections. When it contains a statement, a proof or a replacement theorem,
  that text is unrefereed mathematics by an agent who did not write the paper. Before it enters, the author checks
  it independently (hypotheses of every cited result read at the source, the definitions it uses checked against
  the paper's own) and says so in the reply. "Applied in the reader's wording" is a flag, not a virtue, for
  anything that is a statement.
- Any statement that entered from a report is named to the next reader as new, so it is read as new.
- A should-fix that is declined is listed as declined with the reason and handed to the next reader; otherwise it
  comes back.
- Checksums of the paper files are regenerated as the last step of each round; every read here named them stale.

Not checked: the other items of those reports; whether later rounds follow this.


Third instance, same morning (entry 30): the fifth read of the excited-walk paper had three must-fix, and all
three corrected text an earlier reader had proposed (two from the fourth read's replacement blocks, one from the
second read's paragraph, which had passed reads three and four). The read found nothing to fix in the author's
own text. Counts over reads two to five were flat (must-fix 4, 3, 3, 3). Stopping rule that follows: stop when a
read finds no must-fix outside text changed in the round before it, and the author has checked that round's
changes by hand.
