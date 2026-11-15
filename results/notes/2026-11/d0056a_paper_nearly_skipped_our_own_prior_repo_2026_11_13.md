---
name: d0056a_paper_nearly_skipped_our_own_prior_repo_2026_11_13
description: "[VERIFIED] Writing a paper on an open problem (Dxxxx/Pxxxx)? Run problem_recall.py <id> BEFORE drafting: D0056A nearly shipped without citing our own 5 Nov public paper on the same conjecture; only a repo-name collision caught it"
metadata:
  type: feedback
  created: 2026-11-13
  created_at: 2026-11-13T01:27:42+02:00
  status: provisional
  evidence: ""
---

D0056A (Derrida-Retaux survival constant, referee MINOR) was drafted from the referee folder alone. At repo creation the name derrida-retaux-critical-survival already existed: our 5 Nov paper (m=2, b=3, liminf <= 3/2, commit 97411eb, TRIO 11-12 Oct, ledger refuted_2026_10_11). problem_recall.py D0056 lists it in one call. Fixed before push: new repo derrida-retaux-survival-constant 2244a83 cites it as [Sh] and says what the new Theorem adds (lower half of the bracket, all m, all 2<b<4).

**Why:** C10 says our own earlier papers on the same problem are cited; a referee folder does not carry the problem's history, and a fresh agent sees only the submission.
**How to apply:** first command of any paper write-up on a ledger problem: python ~/.claude/dreaming/problem_recall.py <id>; also git ls-remote the intended repo name before writing the Data availability URL. Related: [[w11_rx_paper_own_prior_work]]
