from pathlib import Path
s=r'''

The graph-specific median version of Corollary C also holds for the locally centred statistic. To avoid a notation collision, let p_G be the occupied median called q_G in ATTEMPT.md, and q(G)=1-p_G be the vacancy density. Centre and normalize H_t using h_t(q(G)) and sigma_t(q(G)), and condition on M<nq(G)-K sqrt(n). The preceding moment estimates are uniform over q in any fixed compact interval, so they remain valid when q is chosen as a function of G. Their deterministic Gaussian approximation initially uses rho_t(q(G)) and b(q(G)). These parameters converge in graph probability to the deterministic parameters at q*=1-p*:

- ATTEMPT.md Proposition 1 gives q(G)-q*=O_P(n^-1/2).
- |h'_t|<=S_t, |h''_t|<=2S_t^2 follow by differentiating a Boolean expectation coordinate by coordinate. Each covariance in (A4) involves at most 2S_t bits, so its derivative is bounded by 4S_t; consequently |(sigma_t^2)'|<=4S_t S_{2t}.
- On the compact interval sigma_t^2>=exp(-O(S_t))=n^{-o(1)}. Differentiating rho_t=sqrt(q(1-q))h'_t/sigma_t therefore gives a uniform bound |rho'_t|<=n^{o(1)}. Hence rho_t(q(G))-rho_t(q*)=o_P(1); b(q(G))-b(q*)=o_P(1) as well.
- The Gaussian rectangle ratio in (D5) is uniformly continuous for rho in [0,1] and b in the compact interval dictated by c,K, because the denominator is bounded away from zero and both Gaussian marginals have continuous distributions even at rho=1.

Thus Q_G concentrates around (D5) evaluated at q*. This is a median-density local-surrogate analogue of the exact remaining replica criterion. The centre n h_t(q(G)) is explicitly graph-dependent; no claim of concentration around the uncorrected centre n h_t(q*) is made.
'''
p=Path('SECOND_ATTEMPT.md');p.write_text(p.read_text(encoding='utf8')+s,encoding='utf8')
