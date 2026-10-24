# P0104 referee attempt and brain bridge

2026-10-10. Exact source: Auffinger--Damron--Hanson, [arXiv:1511.03262v2](https://arxiv.org/html/1511.03262v2), Section 3.1, Questions 13 and 15. The source intentionally leaves the edge-law class and asymptotic convention broad. For a precise working subproblem, take iid Exp(1) edge weights on nearest-neighbor undirected Z^2 and T_n=T(0,ne_1); ask whether `log Var(T_n)/(2 log n)->1/3`. This is a specialization, not a restatement of all possible universal claims. Current global openness is UNKNOWN; no novelty or solution claim is made.

## Single hardest missing bridge

w369's valid abstract bridge says that nondegenerate weak scaling `(T_n-m_n)/n^(1/3) => Z` plus one uniform standardized fourth-moment cap `E|T_n-ET_n|^4 <= K Var(T_n)^2` would yield `Var(T_n)/n^(2/3)->Var(Z)>0`. Neither FPP premise is known here. The moment cap is the bridge I tried to obtain from brain-retrieved results. It does not follow from either of these sources:

1. Damron--Hanson--Sosoe's lattice concentration bound is at `s_n=sqrt(n/log n)`, rather than at the unknown standard deviation. Tail integration yields `E|T_n-ET_n|^4 <= C s_n^4`; even assuming the desired lower variance scale `c n^(2/3)`, its standardized bound is only `O(n^(2/3)/log^2 n)`. w369's four-atom and w370's Bernoulli-sign counterexamples show this is a genuine logical gap for abstract variables, not a counterexample to lattice FPP.
2. The owner campaign's corrected CRUX 9.5 has `(L2')` as a conditional kurtosis cap for each **block resampling increment given a geodesic-touch event**. The bridge needs global kurtosis of `T_n-ET_n`. These are different random variables and conditioning; no martingale or independence argument supplied by (L2') transfers the cap. That campaign also requires `(L1')`, a conditional local second moment bounded by `beta Var(T_n)`, the named variance-ratio wall, and `(L3)`, an O(M) occupation count. The original CRUX 9.2 factor and unconditional kurtosis premise are explicitly superseded by its 9.5 correction.

Basu--Sidoravicius--Sly [arXiv:2604.01214v1](https://arxiv.org/html/2604.01214v1) supplies polynomial variance and standard-deviation-scale concentration for a smooth bounded, isotropic, finite-range, FKG Riemannian field on R^2. I checked those hypotheses against iid nearest-neighbor lattice Exp(1): they are not the same model. No lattice transfer is recorded in the source.

## Independent referee derivation

For centered `U_n=X_n-EX_n`, write `r_n=sqrt(Var U_n)/a_n`. If `U_n/a_n` converges weakly to nondegenerate `Z` and `E U_n^4<=K(Var U_n)^2`, then `r_n` cannot approach zero (Chebyshev would force a degenerate limit) or infinity (Paley--Zygmund gives `P(|U_n|>=sqrt(Var U_n/2))>=1/(4K)`, contradicting tightness after scaling). Thus scaled fourth moments stay bounded; scaled squares are uniformly integrable and their expectations converge. For arbitrary deterministic centers, use independent copies `D_n=X_n-X_n'`: `D_n/a_n=>Z-Z'`, `E D_n^2=2 Var(X_n)`, and `E D_n^4/(E D_n^2)^2 <=(K+3)/2`. Applying the centered argument and dividing by two proves the bridge. This audits w369 L3 and w370 claim 003 without assuming independence across n or between geodesic blocks.

The next potential proof route is the exact finite-Doob identity in w369 L5. For `M_k=E[T_n|F_k]-E T_n` and `D_k=M_k-M_{k-1}`, the fourth moment contains `6 E M_{k-1}^2D_k^2 + 4 E M_{k-1}D_k^3 + E D_k^4` per step. The cubic term can be nonzero: w369's two-step martingale gives total fourth moment 27 versus 19 if it is omitted. A useful disjoint next lemma is to test whether CRUX `(L2')+(L3)` control the predictable quadratic variation and cubic sum needed for global kurtosis, or to give a finite-product counterexample; the known conditions do not currently establish this.

## Brain repair found during the attempt

The read-only probe in `RETRIEVAL_MEASUREMENT.json` found one retrieved DHHoXu card saying quantitative anti-concentration cannot itself lower-bound variance and omitting Theorem 1's exact law conditions. The primary [2019 Theorem 1](https://arxiv.org/html/1810.08270v2) is planar and gives two positive-probability quantiles separated by `c sqrt(log ||x||)`. The sharp two-quantile lemma in `bundle_001.json`, independently checked here, turns that into a logarithmic variance lower bound when finite. This corrects the card's logic and dimension; it does not move chi=1/3.

Referee verdicts and arithmetic reproductions are in `REVIEW_PACKET.md` and `PEER_VERDICTS.jsonl`. My source-scope correction has an independent w374 audit request in `REVIEW_REQUEST_w374.md` and via the team channel.
