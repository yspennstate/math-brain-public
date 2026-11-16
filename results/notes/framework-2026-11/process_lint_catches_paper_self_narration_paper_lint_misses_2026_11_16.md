---
name: process_lint_catches_paper_self_narration_paper_lint_misses_2026_11_16
description: "Paper has 'not proved here', 'we took six draws', 'AI agents' in the introduction, 'we are not aware of'? paper_lint passes these; framework/writing_brain/creative/process_lint.py flags them: 5 of 5 must-fix process sentences from eleven first-reader audits, no flags on 8 clean papers."
metadata:
  type: feedback
  created: 2026-11-16
  status: verified
---

A paper should state mathematics and attributions, not narrate its own making. The general paper linter
(`framework/paper_writing_hooks/paper_lint.py`) passed three released sources with no must-fix item, yet first-reader
audits on 16 November 2026 marked five sentences about the paper as must-fix: "is not treated here", "is not proved
here", "We took ... six draws of W", "A direct numerical minimization ... returns the same values", and "The result
below was proved by AI agents" in an introduction.

`framework/writing_brain/creative/process_lint.py` looks for that shape:

    python -X utf8 process_lint.py paper/main.tex
    python -X utf8 process_lint.py --selftest

Kinds: scope-here, lab-diary, search ("we are not aware of", "we found no"), ai-in-body, history ("an earlier version
of this paper"), plus two reference checks (a lemma cited as a theorem; a repeated statement). It skips the AI
declaration, the acknowledgments, the data and code availability sections and the bibliography, where naming the
process is proper.

Scored against the eleven audit reports of that day: every must-fix process sentence was caught where the source still
matched the audited one (5 of 5), and none of the 8 clean papers drew a flag. Not caught: plan-of-the-paper sentences
and paraphrases of the form "Theorem X says that ...", which the auditors judged case by case.

A scar from building it: a case-insensitive "AI" in the section-title regex matched `thm:main` and blanked a whole
proof section. Match "AI" case-sensitively, as a word.

How to apply: run it beside paper_lint and the citation check before a paper goes to GitHub, Zenodo or a preprint
server. A flag is a sentence to read, not a verdict: "we do not need X here" inside a proof is mathematics.
