# Referee report: survival asymptotics and moment predictions for the Derrida-Retaux recursion

Paper: yspennstate/derrida-retaux-moment-conjecture at bb0e790 (main.tex, 718 lines). Referee: an agent, 14 Nov 2026.
Subject: Conjectures 1-4 of Chen, Derrida, Hu, Lifshits and Shi (arXiv:1705.04787v2). The paper proves that
q_n ~ A n^{-b} (b > 1) forces the geometric conditional limit with all conditional moments and exponential moments
below m (Theorem 1.1), that under criticality Conjectures 1 and 3 are equivalent (Theorem 1.2), and records that the
sparse law of the companion paper breaks every moment prediction at once (Corollary 1.3).

## Verdict

SOUND. No change needed. Two optional one-line additions are listed at the end.

## Proofs checked

- Lemma 2.1: G_{n+1}(s) = G_n(s)^m/s + (1 - 1/s)(1 - q_n)^m and mu_{n+1} = m mu_n - 1 + (1 - q_n)^m. Correct; the
  second is also confirmed numerically (below).
- Lemma 3.1 (path bound). On E_v the leaf value drops by exactly one per level and stays positive; the m-1 sibling
  roots at level i (i = 0..t-1) have law X_{n+i}, leaf sets disjoint, so P(E_v) is the stated product. Disjointness
  via the lowest common ancestor is right: the child subtree containing w is a zero sibling on E_v and lies on w's
  positive path on E_w. Correct.
- Corollary 3.2. Product positive by summability of q_i; B_N = P_N^{-1}. Correct; no monotonicity used.
- Lemma 3.3. q_{n+1} = 1 - (1-q_n)^m - m p_{n,1}(1-q_n)^{m-1} (next value zero iff child sum <= 1); the split
  p_{n+1,k} = m(1-q_n)^{m-1} p_{n,k+1} + R, 0 <= R <= C(m,2) q_n^2; induction from p_{n,1}/q_n -> (m-1)/m; total
  variation by the tail argument. Correct.
- Proposition 3.4 (weak limit iff q_{n+1}/q_n -> 1). Correct.
- Theorem 1.1. q_{n+t}/q_n <= 4 (n/(n+t))^b <= 4 from the two-sided bounds, hence nu_n([k,inf)) <= 4 B_N m^{-(k-1)}
  uniformly; uniform integrability for every r > 0 and dominated convergence for s < m. Limits M_r(m) and
  (m-1)s/(m-s) recomputed. Correct.
- Theorem 1.2. c(r,m) = (4/(m-1)^2) M_r(m) = (4/(m-1)) sum k^r m^{-k}; c(1,m) = 4m/(m-1)^3. (ii) => (i) from
  1 - (1-q_n)^m = m mu_n - mu_{n+1} ~ (m-1) mu_n. The generating-function identity G_n(s) - 1 = q_n(E[s^X | X>0] - 1)
  and m(s-1)/(m-s) give exactly CDHLS (5). Under criticality q_n -> 0 by (2.4) ((m-1)q_n <= G_n(m) - 1) and
  Proposition 3.4 applies. Correct.
- Corollary 1.3. x^r >= 1{x>0} on Z_+ along the subsequence with n^2 q_n -> infinity; finite-time moments from
  G_{n+1}(m) <= G_n(m)^m. Correct. The remark that the liminf bound of the heavy-tail paper cannot give this is right.
- Section 5.3. E[m^X | X>0] = 1 + (G_n(m)-1)/q_n; with CDHLS Theorem 3 and (1.3) this is of order n. Correct.

## Citations checked against the sources

- CDHLS arXiv:1705.04787v2: Theorem 1 and 2 and Conjecture 1 on p. 3; Conjectures 2-4 and the integrability remark
  (E(X_0^3 m^{X_0}) < infinity) on p. 4; Theorem 3 on p. 5; Section 6 on pp. 13-15 with Lemma 4 on p. 14; Propositions
  4-5 on pp. 22-23 (harmonic averages). All as stated. The paper credits CDHLS Section 6 for Conjecture 1 => mean
  prediction (Lemmas 4-5), which is the one part of Theorem 1.2 already in the source; the new content is the uniform
  tail and the conditional and all-moment limits, stated as such.
- Chen-Hu-Shi arXiv:2108.05610v1: Theorem 1.2 (q_n, mu_n = n^{-2+o(1)} when E(t^{Y_0}) < infinity for some t > m) and
  the p. 3 remark that (1.4) is expected under E(Y_0^3 m^{Y_0}) < infinity. As stated.
- Chen-Shi arXiv:2006.06140 Theorem 1.1: under (1.4), P(Y_0 = k) ~ c0 m^{-k} k^{-alpha} with 2 < alpha < 4,
  c1 n^{alpha-2} <= prod_{i<n} [E m^{Y_i}]^{m-1} <= c2 n^{alpha-2}. As stated.
- Hu-Mallein-Pain arXiv:1811.08749 Theorem 1.9(iii): mean ~ 2/t^2 and conditional standard exponential limit. As stated.
- CDDHLS arXiv:1907.01601 Theorems 1.1-1.2: exponent 1/2 under the third tilted moment, power tails 2 < alpha <= 4.
  As stated.
- Companion papers: derrida-retaux-survival-constant README states Theorem 1.1 (every m >= 2, nonconstant critical
  law, limsup n^2 q_n = infinity) as cited; derrida-retaux-critical-survival states liminf n^2 q_n <= 3/2 for m = 2,
  P(X_0 = k) = c 2^{-k} k^{-3}, as cited (3/2 = b(b-2)/2 at b = 3, consistent with the companion's Theorem 1.3).
  Zenodo's API refused the record read (403), so the DOI was not opened.

## Numerical check (drm_tilted.py, output drm_tilted.out)

The paper has no computations. As a sanity check of Theorem 1.1's conclusions, the exact law recursion was run for
m = 2 and the critical law P(X_0 = 2) = 1/5, P(X_0 = 0) = 4/5, in tilted coordinates r_k = 2^k P(X_n = k) with direct
(exact-sum) convolution, truncation K = 3000 and 6000, and renormalisation of total mass each step. Two pitfalls met on
the way and worth recording: plain floating point doubles any total-mass error each step (M -> M^2), and a truncation
at K = 300 in untilted coordinates loses tilted mass and drifts the run subcritical within a few hundred steps.

    n      n^2 q_n   E[X]/q (->2)  E[X^2]/q (->6)  TV(nu_n, pi)  E[1.5^X | X>0] (->3)
    100    4.2506    1.9607        5.7280          0.0100        2.8865
    1000   4.0523    1.9960        5.9720          0.0010        2.9880
    3000   4.0218    1.9987        5.9907          0.0003        2.9960

Identical at K = 3000 and 6000. n^2 q_n is near 4 = 4/(m-1)^2 for this exponential-moment law, as Conjecture 1
predicts; the conditional quantities converge at rate about 1/n, as Theorem 1.1 says they must once q_n is regularly
varying. n(G_n(2) - 1) reads 2.01 at n = 1000 with K = 6000 (Conjecture 4b predicts 2) but depends on K: the tilted
mass spreads to large k, which is the paper's own Section 5.3 point that E[m^X | X > 0] grows like n.

## Optional additions (not required)

1. Theorem 1.2's last step uses q_n > 0 for all n under criticality. One line closes it: if q_n = 0 then
   P(child sum <= 1) = 1 forces X_{n-1} = 0 a.s., and inductively X_0 = 0, which is not critical.
2. Lemma 3.1's proof says "at height i above the leaves" for the siblings of law X_{n+i}; stating i = 0, ..., t-1
   would match the product index exactly.
