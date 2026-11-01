# T356 Model collapse under recursive training on generated data

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
08:3x, the 16 Oct 07:07 audit (status PARTLY, KDE stability diagnostic)).

## STATEMENT
Repaired statement (the audit: fix the distance, expectation versus pathwise all-time control, bandwidth, sample size,
fresh versus reused real data, covariance convention and the replacement or accumulation protocol; bounded expected W2 can
coexist with variance collapse, a fixed-bandwidth KDE spreads its second moment instead, and the tail-loss alternative is
not universal): Gaussian-kernel KDE with bandwidth h and n samples per generation, a fraction r_t of each new sample drawn
fresh from the true law P and the rest from the generation-t estimate; give conditions on (r_t, h, n) under which
sup_t E W2(P_t, P) stays below a stated tolerance, and the rate at which a stated tail or variance criterion degrades
otherwise. Score-trained diffusion models are a separate question.

## FRONTIER
- Shumailov et al. arXiv:2305.17493: Gaussian MLE collapse.
- Dohmatob, Feng, Yang, Charton, Kempe arXiv:2402.07043: collapse as a change of scaling laws.
- Gerstgrasser et al. arXiv:2404.01413: accumulation keeps linear-regression error bounded.
- Bertrand, Bose, Duplessis, Jiralerspong, Gidel arXiv:2310.00429: iterative retraining is stable when the first model is
  close and the real-data fraction large enough.
- Borji arXiv:2410.12954: KDE resampling; collapse as a statistical phenomenon.
- Khelifa, Turner, Venkataramanan arXiv:2602.16601: diffusion models with fresh data each round: upper and lower bounds on
  the accumulated divergence, a discounted sum of score errors in one regime.
- Audit diagnostic: second moments obey m_(t+1) = r m2(P) + (1 - r) m_t + d h^2, so any fixed r > 0 keeps them bounded and
  r = 0 inflates them linearly.

## ARCHITECTURE
The recursion is a Markov chain on measures: P_(t+1) = (r P_hat + (1 - r) P_t_hat) * K_h with empirical measures of n
samples; the error has a contracting part (factor 1 - r) and fresh noise each generation (sampling error ~ n^(-1/d) in W2
plus bandwidth bias h). A geometric series gives sup_t E W2 <~ (n^(-1/d) + h)/r.

## FAILURE POINT
W2 is not convex along this mixture in the way the geometric series needs; W2 of a mixture against P is bounded by a
convex combination only for the squared distance.

## SHAPE
Days: the squared-W2 version of the geometric series with constants.

## OBSTRUCTION
Mixture convexity. Moves: use W2^2's joint convexity: W2^2(r A + (1 - r) B, P) <= r W2^2(A, P) + (1 - r) W2^2(B, P).

## TARGETS
1. sup_t E W2^2(P_t, P) <= C (n^(-2/d) + h^2)/r for fixed r > 0, with constants.
2. r = 0: the rate of variance growth (fixed h) versus collapse (h -> 0 with n).

## 2026-10-22 00:2x agent H: worker worker M's nine claims reviewed
All nine PASS on their exact versions (reviews_w703/AUDITS_FROM_REVIEWER.tsv, one row each with the proof sha256): C008 v1, C004 v2, C002 v3, C005 v2, C007 v1, C003 v2, C009 v1, C001 v3, C006 v2. Target 1 as stated is false unrestricted (C001: two atoms in d=1,2,3; C008: uniform square at h=1/n). It holds for d>=5 with a q-moment (C004/C005), for Lipschitz-curve laws (C007), and on the bandwidth intervals of C006 for compact support in d<=4. Open: small bandwidth for regular laws in d=3,4, where n^(-2/d) is the truth for the uniform cube but the dyadic method loses N^(-1/2) at coarse levels. Next route (reviews_w703/FEEDBACK.md): label variance for test functions, then the Bobkov-Ledoux Fourier argument on the labels.
