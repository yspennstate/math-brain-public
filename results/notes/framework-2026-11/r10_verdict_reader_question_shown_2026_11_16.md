---
name: r10_verdict_reader_question_shown_2026_11_16
description: "Can a reader asked one question find where a narrator passes a verdict on what the page showed? Yes: listed sentences faulted by blind readers at 4.6x and 7.1x the base rate (tool verdict_read.py); a list of candidates, sort with line_read.py"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T06:12:30+02:00
  status: provisional
  evidence: "the writing-brain test record R10_RESULT.md commit 25b49b08e90a; R10_PREREG.md 8a42de1e"
---

R10, 16 November 2026: can a reader asked one question find the sentences where a narrator passes a verdict on
what the page has just shown? Yes, by the registered bars (R10_PREREG.md, 8a42de1e), on both test texts.

One gpt-6.1-sol run (high, Mac mini 1) per text, asked only for those sentences, scored against blind readers'
ten-weakest lists (readers who were asked nothing about verdicts):

- current chapter one (4 readings): 54 listed of 439 narrated sentences, 9 faulted. 17 pct against a base rate of
  3.6 pct, lift 4.6. Bar: two at lift 2.
- pass 45 of the second chapter (16 readings): 25 listed of 560, 15 faulted. 60 pct against 8.4 pct, lift 7.1 (corrected 16 Nov: first given as 26, 16, 62, 8.6 and 7.2; the matching rule had counted a three-word sentence that ends a longer quoted one).
  Bar: three at lift 2.
- second runs: lift 5.1 and 6.2; two runs share about four listed sentences in five (44 of 54, 19 of 25).
- tokens 192,769 for four runs.

The regular-expression version, R9 ([[r9_narrator_verdict_regex_not_shown_2026_11_16]]), flagged three
sentences a text and failed: the fault lies between a sentence and the paragraph before it.

How to use it: `writing_brain/turn/verdict_read.py make <text> --out <dir>`, readers, then `collect <dir>
--targets <file>`, then `line_read.py` on the targets. The list is candidates, not faults: in the current
chapter 45 of the 54 listed were sentences no reader had faulted, and one listed sentence is the line four
readers ranked first of twelve to keep in CH1T ([[ch1t_readers_cut_four_of_his_six_keep_two_2026_11_16]]). Cut
only what the keep-or-cut reading cuts.

A scoring scar found on the way: the R9 scorer grouped readings by packet text, and two reads carried copies of
pass 45 that differ by a few characters, so twelve of sixteen readings were silently dropped (13 faulted
reported, 47 true). The count of readings it printed was still 16. When readings of one text come from two
packet sets, pool the quotes by the text's name and count the faulted sentences a second way.

Limits: the same model asked the question and wrote the blind readings; the question was worded after reading
notes on pass 59, close kin to pass 45; two first-person chapters of one manuscript. What would change it: the
keep-or-cut read of pass 61 (CH1U) keeping the listed sentences as often as its controls.

