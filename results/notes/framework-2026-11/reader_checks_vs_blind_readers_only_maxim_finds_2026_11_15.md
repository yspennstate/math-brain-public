---
name: reader_checks_vs_blind_readers_only_maxim_finds_2026_11_15
description: "Do the writing-brain sentence checks find what blind readers fault? Only the narrator's-maxim check does (5 of its 9 flags faulted, lift about 12). About 60 percent of reader faults are about meaning, and no check flags them."
metadata:
  type: project
  created: 2026-11-15
  status: provisional
---

Which sentence checks in `framework/writing_brain/turn/reader_checks.py` point where blind readers point? Sixteen
readings of two versions of one draft chapter (eight each); each reader names the chapter's ten weakest sentences.

Rule fixed before the run: a sentence is faulted when a reader quotes it as weakest and flagged when a check names it;
lift is the share of flagged sentences that are faulted over the share of all sentences faulted; a check finds reader
faults at lift 2 or more with 5 or more faulted sentences flagged.

- The readers repeat themselves: 80 picks fell on 29 distinct sentences of the first version (618 sentences) and 35 of
  the second (764). That is one model's repeatability, not agreement between people.
- Only the narrator's-maxim check (R7) meets the bar: 5 of its 9 flags on the first version (lift 11.8; that version
  was never edited against the check), 2 of 4 on the second.
- Short-sentence runs (4 of 26, 3 of 18) and ", which" clauses (2 of 20, 3 of 15) point the right way, under the bar.
  Comparison forms: 0 of 24, then 4 of 14; not established.
- Short It/That statements, denial pairs, one-line paragraphs, short closers and the handed-on noun: 34 flags across
  the two versions, none faulted (about 1.6 expected by chance). Weak evidence that readers do not mind those shapes.
- 17 of 29 and 23 of 35 faulted sentences are flagged by no check. The readers' reasons are about meaning: a maxim put
  in a character's mouth, a scene's meaning stated after the scene showed it, the narrator describing his own manner,
  a result announced without grounds, a stock figure, a vague magnitude, an unclear antecedent.

How to apply: keep the shape checks at zero, but do not read a clean sheet as a cleared chapter; spend rewrite effort
on maxims (in narration and in speech) and on sentences that state what a scene has already shown. The single question
in `turn/verdict_read.py` was built from this result ([[r10_verdict_reader_question_shown_2026_11_16]]).

What would change this: readings by people, a different reader model, a chapter by another hand.
