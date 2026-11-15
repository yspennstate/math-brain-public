---
name: paper_commit_inputs_an_untracked_file_builds_locally_only_2026_11_12
description: "Paper pushed and builds here, but does the pushed commit build? Not if main.tex inputs a file git never tracked (notation_appendix.tex, 12 Nov 711afce). Before a paper push: git status --short on the paper dir shows no untracked source, or build a fresh clone of the commit."
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T09:03:58+02:00
  status: verified
  evidence: "yspennstate/ising-perceptron-margin common-slope: 711afce main.tex line 1148 inputs notation_appendix.tex, absent from git log until 0815fbd"
---

12 Nov 2026, margin paper (yspennstate/ising-perceptron-margin, branch common-slope): commit 711afce added \input{notation_appendix} to main.tex while notation_appendix.tex stayed untracked. The local build passed (26 pages, 0 undefined), so nothing flagged it; the pushed branch could not compile. Found an hour later by git status, fixed in 0815fbd.

**Why:** a local build reads the working tree, not the commit. Any check run in the working copy shares the gap.

**How to apply:** before a paper push, `git status --short` on the paper directory must show no untracked .tex, .bib, .bst or figure that the source inputs; for a release, build from a fresh clone of the pushed commit. Related: [[sha256sums_hash_the_stored_blob_not_the_crlf_working_copy_2026_11_12]].

