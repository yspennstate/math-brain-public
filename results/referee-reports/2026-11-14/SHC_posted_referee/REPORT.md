VERDICT: ACCEPT WITH ONE MINOR CORRECTION (made and pushed, 456b478)

Independent post-posting referee pass on "Randomized smoothing at high confidence: the Gaussian is optimal for every
noise law", https://github.com/yspennstate/smoothing-high-confidence (paper/main.tex at 49e5e44, read in full 14 Nov 2026).
Referee: an agent (Claude Opus 5.5), a session that did not write the paper. Lane: T-20261112-017.

Checked by hand, all correct:
- Lemma 2.1: f = B on x+v+B_0 gives P(A) >= 1-alpha at x and P(A) <= 1/2 at x+v; the good radii are downward closed,
  so R <= ||v||.
- Lemma 3.1: N = floor(sigma/eps) intervals of length eps sqrt(d) fit in [2 sigma sqrt d, 3 sigma sqrt d], the last
  start is <= 3 sigma sqrt d - eps sqrt d, min mass <= 1/N <= 2 eps/sigma (floor(t) >= t/2 for t >= 1); Markov gives
  q(B_rho) >= 3/4.
- Lemma 3.2: Hoeffding with ranges 2|y_i| gives exp(-u^2 d/(2||y||^2)) <= exp(-u^2/(18 sigma^2)); T, T' give 1/24 and
  alpha/16; Markov in s gives 1/8 + 1/8 < 1.
- Theorem 1.1: X_s(v+z) = X_s(z) - eps sqrt d <= -T'; q(B_0) >= 3/4 * 2/3; sqrt(18)(sqrt(log24/log64) + 1) = 7.9516
  <= 7.952; 16 * 7.952^2 = 1011.7 < 1012; ||v||_p = eps d^{1/p}. eps depends only on (sigma, alpha, d), so fixing it
  before rho and s is not circular.
- Corollary 1.2: at alpha -> 1/4 the ratio is 8 sqrt(log 64)/Phi^{-1}(0.75) = 24.19; the limit 8/sqrt 2 as alpha -> 0.
  The Gaussian lower bound in l_p needs only that N(0, sigma^2 I) certifies at least sigma Phi^{-1}(1-alpha) d^{1/p-1/2},
  which the l_2 inclusion gives.
- Remark 4.1: the half-space classifier gives P(B) = alpha at x and exactly 1/2 at x+v.
- Citations: Blum-Dick-Manoj-Zhang (arXiv 2002.03517) abstract read: E eta_i^2 = Omega(d^{1-2/p} eps^2 (1-delta)/delta^2)
  for 99% of coordinates, which at delta = 1-2 alpha is the alpha^{-1/2} rate the paper says. Yang et al.
  (arXiv 2002.08118) abstract: an Omega(min(1, d^{1/p-1/2})) limit via cotype, no confidence rate; the novelty claim
  (log(1/alpha)^{1/2} for every law with a second moment) stands against both abstracts.
- code/consts.py and code/check.py rerun: ALL PASS (alpha 0.24, d 73,787, Gaussian, multivariate t5, cube), output
  in check_rerun.txt.

Correction made (456b478, author the author):
1. Lemma 3.2 bounded mu(X_s < -T'), but the proof of the theorem uses mu(X_s <= -T') and patched this with "holds by
   the proof of Lemma 3.2". The lemma, its proof (Hoeffding for the closed event) and the theorem now use the closed
   event, and the patch clause is gone.
2. \date{\today} replaced by a fixed date.
Recompiled twice: 5 pages, no undefined references.

Not changed, noted: lint style findings (bibliography case, keywords, a numeric-citation sentence start) left as they
are. Not checked: the full texts of Yang et al. and Wu et al. beyond abstracts; Kumar et al.'s alpha dependence.
