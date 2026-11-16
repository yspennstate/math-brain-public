---
name: paper_hooks_audit_pattern_lists_measure_their_own_sentences_2026_11_12
description: "Paper-writing hooks pass a clean lint, is the paper edited? No: a Fable audit reworded the faults and the hooks caught 0 of 38, 2 of 24, 5 of 14; gate on an independent reader's verdict for the exact source, test real command shapes, never edit a live hook in place"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T08:33:29+02:00
  status: verified
  evidence: "12_cognitive_architecture/audits/reports/2026/11/12/paper_writing_hooks_audit/REPORT.md (F01-F20); brain main def73b333fc5; live selftest ALL PASS 12 Nov 08:22"
  lesson: true
---

A Fable 5.2 agent audited the 50 paper-writing hooks on 12 Nov 2026 (20 findings, 11 high; report
`12_cognitive_architecture/audits/reports/2026/11/12/paper_writing_hooks_audit/REPORT.md`, fixes on brain main
def73b333fc5). What it taught, in the order it will matter again:

1. A pattern list measures the sentences it was written from. The auditor put the same faults in new words three
   times; the hooks caught 0 of 38, then 2 of 24 after I widened the patterns to its first files, then 5 of 14.
   Widening to the test file moves the number on that file only. So a clean lint is a floor and is never reported as
   "the paper is edited". The gate that means something is a reader that did not write the paper: W43 now reads the
   verdict on record for the sha256 of the .tex (ready = "SEND AS IS" and "MUST-FIX: 0"), not whether a report exists.
2. A gate that tests for a file's existence passes on a report that says NOT READY. Read the verdict.
3. Test the command shapes people really type, in the real repository. A push from the root of the repository that
   holds the papers, `git -C`, Push-Location, a list-form Codex command, a bare `make`, and a push on one line with
   another command all printed nothing while every selftest passed. A runner prefilter keyed on words (".tex",
   "push") silently drops a call that names none of them.
4. Never edit a live hook file in place. For about a minute every command case failed with a NameError and nothing
   said so, because a hook that raises prints nothing. Develop in a copy, run the selftest and the case list there,
   then swap whole files in (.tmp beside the target, os.replace) and run the live selftest.
5. Speed: the engine resolved the outgoing files twice and re-read each paper's \input tree once per candidate file
   (34 times on the real repository), 12-24 s per push. Memoising the tree and computing the channels once gives
   2.5-3.5 s.
6. Check the rules file against the user's words with dates. Two dates were wrong, three quotes were about other
   documents (a proposal, the research statement, a pitch-deck slide), and five house-style rules stood beside the
   owner's orders with the same weight. Each rule now carries its source: the user's words, the editor's letter, or house style.
7. The 2 Nov house rule (overfull line, funding statement, AI acknowledgment) had no check at all among the 50.
   W51 and the log check now cover it. The AI-acknowledgment question (every paper, per 2 Nov, or "when he asks",
   per the 15 Sep text) went to the owner on 12 Nov; until it is answered the check follows
   the later words and a file NO_AI_DECLARATION beside the .tex exempts a paper.

What would change this: an answer on the declaration and on whether upload and submission should refuse without a
SEND AS IS record; a held-out file with a line-level key, so the selftest can print a real catch rate.


Related: [[ptrf_declined_for_unedited_introduction_not_for_mathematics_2026_11_12]], [[no_self_introspection_in_a_paper_2026_09_15]], [[research_writing_human_voice_2026_06_10]], [[agents_audit_check_scars_smell_test_2026_07_31]].
