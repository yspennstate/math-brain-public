---
name: i0006b_critical_tail_paper_posted_2026_11_13
description: "I0006B sandpile gamma=d/2 endpoint: (log n)^{2/d}(loglog n)^{1-2/d}, posted divisible-sandpile-critical-tail 92ce2906 after two claim audits + paper referee ACCEPT"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T16:06:57+02:00
  status: verified
  evidence: "repo 92ce2906; I0006BR ACCEPT; I0006PR ACCEPT"
---

I0006B, the gamma = d/2 endpoint left out of Bou-Rabee and Panagiotis (arXiv:2609.02829v1, Theorem 1.3(iii)(b), p. 6), is posted as a paper:
github.com/yspennstate/divisible-sandpile-critical-tail, commit 92ce2906, 13 Nov 2026 (12 pp, amsart).

Result: d >= 5, u_{n+1} = (eta + P u_n)_+, centered i.i.d. scenery with an absolute exponential moment and
exp(-C t^{d/2}) <= P(eta < -t) <= exp(-c t^{d/2}) give E u_n(0) of order (log n)^{2/d} (log log n)^{1-2/d}.
Also, for 0 < gamma < 1 (stretched-exponential negative tail, exponential positive tail, no absolute exponential moment), E u_n(0) is of order (log n)^{1/gamma}.

Mechanism: sum over |y| <= R of G(0,y)^{d/(d-2)} grows like log R, so the Laplace bound picks up lambda^q log lambda and the cost is
Phi(s) = (1+s)^p / log(e+s)^{p-1}. Lower bound: exact discrete supersolution a log(1+|x|^2), whose boundary conditions are paid for with Harris-FKG.

Checks: claim run I0006B plus independent referee I0006BR (ACCEPT); paper referee I0006PR (ACCEPT, no fixes); my full read of main.tex, with the d = 3 and d = 4 orders (n^{1/4}, log n) checked against the companion's text.
paper_release_guard ok, paper_lint 0 MUST. Ledger row I0006 PAPER_POSTED.

Constants are not universal. The paper claims no leading constant and no LDP.

