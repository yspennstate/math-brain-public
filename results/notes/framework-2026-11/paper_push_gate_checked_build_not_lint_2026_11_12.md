---
name: paper_push_gate_checked_build_not_lint_2026_11_12
description: "[VERIFIED] Paper pushed with a MUST finding? A push guard that tests only build errors and overfull lines lets lint MUSTs through; gate on the MUST count too"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:16:35+02:00
  status: provisional
  evidence: ""
---

On 12 Nov 2026 (filtration-witness, commit 5303fb9) a shortened abstract was pushed although paper_lint reported 1 MUST (W16: three named results, none defined). The push condition was [ "$E$O" = "00" ] - errors and overfull lines only; the lint ran and printed, but nothing read its count. Fixed in c3aea40 by saying each result in words. **Why:** the author's 12 Nov order that a paper leaves publishable as is; W49 requires zero MUST before a push. **How to apply:** compute M from 'paper_lint.py main.tex | grep "MUST findings"' and gate on "$E$O$M" = "000"; a lint whose result is printed but not tested is decoration. Related: [[pw1k_thousand_paper_writing_rules_one_word_one_thing_2026_11_12]].
