---
name: i0103_paley_interval_not_novel_conj29_open_2026_11_13
description: "I0103 Paley ETF RIP (Randomstrasse Conj 29) still open: our interval sub-dictionary theorem is correct but classical (Burgess + Abel summation) and the source has no sub-dictionary alternative; referee MAJOR, NO_PROGRESS"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T20:59:49+02:00
  status: verified
  evidence: "I0103AR REPORT.md first line MAJOR (Mac 13 Nov); ledger row 13 Nov 20:50 laptop"
---

I0103 (Randomstrasse101 2025, arXiv:2603.29571v1, Entry 12, Conjecture 29 on p.10: Paley ETF RIP beyond the square-root bottleneck) is still open as of 13 Nov 2026. Our claim (I0103A) and referee (I0103AR, verdict MAJOR) agree on the following.

- Proved and correct: for 0<rho<1/16 and p = 1 mod 4, the interval sub-dictionary D_p = {0..L_p-1, inf} with L_p = floor(p^{9/16-rho}) satisfies ||Psi*Psi - I|| <= C p^{-rho/3} + sqrt(L_p/p), so every subset of D_p is uniformly well conditioned. The same holds for affine progressions a+dI. Route: Heath-Brown-Pierce 1404.1677 Thm 1.4 with r=3.
- Not progress on the conjecture. The source has no sub-dictionary alternative (an earlier brief misread it). Classical Burgess with a rational twist plus Abel summation gives the same interval bound, and untwisted Burgess on Fourier-row energy gives a stronger one. General column-selection theorems (restricted invertibility, almost isometric selection) already give tall, almost orthogonal Paley sub-dictionaries of this size.
- The Kuemmerle-Mixon absolute-value method (2611.14475) cannot work for Paley, because |G_S - I| = p^{-1/2}(J-I) for every support. This is correct, as a limit of that estimate only.

Ledger: NO_PROGRESS, 13 Nov 20:50. Report copied at agent_run/i0103ar_REPORT.md; runs archived from mini1 ~/agent_run/I0103A, I0103AR.
How to apply: do not write a paper on the interval theorem. Before claiming a sub-dictionary alternative, quote the source's exact clause.

