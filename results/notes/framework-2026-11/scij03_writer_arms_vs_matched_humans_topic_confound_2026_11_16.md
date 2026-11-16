---
name: scij03_writer_arms_vs_matched_humans_topic_confound_2026_11_16
description: "[PROVISIONAL] Can a brain or revision arm make Codex writing pass as human? SCIJ03: no arm comes close (AUC 1.0 vs matched humans); brain -1.2 and revision -1.4 points P(machine) near the ceiling; design confounds topic"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T06:48:13+02:00
  status: provisional
  evidence: ""
---

Question: does the writing brain, a revision pass from a blind judge's notes, or a length range move Codex prose toward human, judged blind beside matched human texts?

Answer (16 Nov 2026, SCIJ03, one fresh Codex detect judge plus one grade judge, 108 pieces from 18 runs on six briefs plus 64 human controls from eLife digests and decision letters, Wikinews 2008-2020 and published methods passages): mean P(machine) plain 96.8, brain 95.3, plain revised 95.1, brain revised 94.2, range briefs 96.4/95.5; humans 5-18. AUC of every arm against the matched humans is 1.0 in every kind. Run-level permutation (6 against 6, 924 splits): brain below plain p 1/924, revised below original p 9/924, range no effect (p 0.45).

Size of doubt: five of six kinds sit at 94-99, so the gaps are ranks near the ceiling, not movement toward human; only the essay (81-93) has room, and there brain and revision each take off 6-7 points. One judge, three runs per arm.

Why the separation is perfect, from the judge's reasons: the batch held 18 versions of the same six briefs (an obvious same-topic cluster) and the briefs ask for exhaustive coverage of the facts; the human texts are on other topics and leave things out. The grade judge gave accuracy 3 to all 90 fact-bound pieces because it lacked the data files the writers had (fixed in score_writing.py pack --data-dir, 16 Nov).

What would change it: SCIJ04 with distinct hunt questions per run (no repeated topic in a batch), briefs that ask for what a professional would include, and the grader given the sources. The answer key and the pieces are kept private.
