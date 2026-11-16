---
name: pw1k_lint_hides_weights_gate_zenodo_posts_2026_11_15
description: "[VERIFIED] Zenodo post: does pw1k lint pass at weight 7? Its printout hides weights; run lintgate.py (P1052 waived under the credit policy)"
metadata:
  type: feedback
  created: 2026-11-15
  created_at: 2026-11-15T05:18:38+02:00
  status: provisional
  evidence: ""
---

`pw1k.py lint` prints rule id, chapter, line and message, but not the weight. The posting rule says findings of weight 7 or more are fixed before a Zenodo post, so the printout alone cannot show whether a paper may go out. On 15 Nov I read two printouts as style notes and posted beta-splitting v1.1 (Zenodo 24237789) and first-passage v1.1 (24237877), both with unread weight-7 and weight-8 findings. Checked afterwards:
- the weight-8 P0999 hits were false alarms, because Lambda_n and kappa_alpha are defined in the same sentence or display;
- P1052 (an AI declaration over about 150 words) is waived, because the credit policy puts the acknowledgement of the mathematicians in that declaration;
- P1001 (the notation table misses symbols or names the wrong first place) was real in beta-splitting and in derrida-retaux.

How to apply: before any post, run `python -X utf8 lintgate.py <main.tex>`. It prints every finding of weight 7 or more and exits 4 unless each one is waived. P1052 is always waived. Pass others in `LINT_WAIVE=` only after reading the hit and finding it false. Every posting script runs the gate and refuses `post` on exit 4. The weights live in pw1k.lint(), as the first tuple element.

Status: verified on 15 Nov (the gate refused the derrida post on P1001).

