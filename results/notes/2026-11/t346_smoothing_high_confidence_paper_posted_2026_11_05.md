---
name: t346_smoothing_high_confidence_paper_posted_2026_11_05
description: "[VERIFIED] T346 posted 5 Nov: smoothing-high-confidence repo; second-moment noise cannot certify beyond 8 sigma sqrt(log(16/a)) d^(1/p-1/2), Gaussian optimal within 25x; check.py ALL PASS"
metadata:
  type: project
  created: 2026-11-05
  created_at: 2026-11-05T08:44:50+02:00
  status: verified
  evidence: "github.com/yspennstate/smoothing-high-confidence: 5 blobs verified against remote tree by t346_verify.py; code/check.py ALL PASS (gaussian/student5/cube)"
---

T346 (randomized smoothing at high confidence) was posted on 5 Nov 2026 as the public repo
github.com/yspennstate/smoothing-high-confidence: README, paper/main.tex and main.pdf (4 pages), code/consts.py and code/check.py.
All 5 remote blobs match the local files by git sha.

The theorem: if E||eta||^2 <= d sigma^2, 0 < alpha < 1/4 and d >= 1012 alpha^-2 log(16/alpha), then no certificate
that holds for every base classifier at confidence 1-alpha exceeds 8 sigma sqrt(log(16/alpha)) d^(1/p-1/2) in l_p, for 2 <= p <= inf.
That is within 25x of the Gaussian radius sigma Phi^-1(1-alpha) d^(1/p-1/2), and the ratio tends to 8/sqrt2 as alpha -> 0.
Card claim_407b00d8095e7704cdd9566f8ea75eb55181728682a8a1fd9607ee8e51aaa3eb.

The proof: a thin shell (Lemma 3.1), then a Hoeffding sign direction with Markov over the signs (Lemma 3.2), then the set B0 = {|y| <= rho, X_s <= T} and the shift v = -eps s.

check.py builds rho, B0 and v from one sample and measures q on a fresh one. Setup: alpha = 0.24, d = 73,787, three laws (Gaussian, multivariate t5 scaled to unit second moment, uniform cube).
Result: q(B0) >= 0.996 and q(v+B0) = 0 for all three; ALL PASS.
How it works: membership in B0 depends only on ||eta||^2 and <eta,s>, so the Gaussian and t5 laws are sampled exactly through those two statistics.
The theorem's d is huge, so the check passes with large margin. It tests the construction's logic, not tightness.

The paper loop now has 9 of 10 posted; QFORM stays private and waits on him.
PAPER_CANDIDATES.md row 10 is marked POSTED.
How to apply: a later tick that finds T346 open in any list should read this memory, not re-post.

