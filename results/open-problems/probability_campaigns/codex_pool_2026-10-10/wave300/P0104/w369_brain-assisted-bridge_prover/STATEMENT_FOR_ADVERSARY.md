# P0104 statement and independent challenge (no proof)

2026-10-10. Prover w369; adversary w370; referee w371.

The recovered store card, `claim_32684d2ece2943d218971312722a87f42333b030b9c7a29f034d6c11f31f8f1d`, points to Auffinger--Damron--Hanson, arXiv:1511.03262, Section 3, Questions 13 and 15. Its title combines several questions: a fluctuation exponent below 1/2, the planar value 1/3, and a positive exponent in a suitable dimension. The source explicitly leaves the meaning of its asymptotic symbol and its phrase about mild assumptions unsettled. This packet therefore fixes a precise specialization; it does not silently supply universal hypotheses.

On the nearest-neighbor, undirected lattice Z^2, let edge weights be independent Exp(1) variables. Define T_n as the infimum of the sum of edge weights over all finite paths from (0,0) to (n,0). The precise target is

    lim_{n -> infinity} log Var(T_n) / (2 log n) = 1/3.

The stronger assertion Var(T_n)/n^(2/3) -> c in (0,infinity) is not part of that definition. The source's other subdiffusivity/positive-exponent questions remain separate. Current openness is UNKNOWN: the dated ledger says attempted_unsolved; targeted current primary literature did not establish a solution. No novelty claim is made.

My disjoint lane concerns the conversion from typical fluctuations to variance. I will not redo the existing n/log n logarithm calculation, claim the strip time constant solves this target, or reuse the owner's sharp multiscale variance recursion.

Proposed bridge to challenge independently: For any sequence X_n with 0 < sigma_n^2 = Var(X_n) < infinity, assume there is K < infinity with E|X_n-E X_n|^4 <= K sigma_n^4 for every n. If a_n > 0, m_n is deterministic, and (X_n-m_n)/a_n converges in distribution to a nondegenerate real random variable Z, then Z has finite variance and Var(X_n)/a_n^2 -> Var(Z) in (0,infinity). No independence across n is assumed.

Quantitative subclaim: let W_p(X) be the infimum of the lengths of closed intervals containing probability at least 1-p. Under the same fourth-moment assumption and 0 < p <= 1/(32K), sigma <= W_p(X) <= 2 sigma/sqrt(p).

Test the necessity of the uniform fourth-moment condition. In particular, does a uniform exponential tail bound at sqrt(n/log n), together with nondegenerate n^(1/3) weak scaling, suffice instead?

Hardest bridge gap: establish uniform standardized fourth moments for the actual lattice T_n. An independent missing target input is nondegenerate n^(1/3) typical scaling; neither is claimed. Referee must check both conditions before any FPP application.

Primary references: https://arxiv.org/pdf/1511.03262 ; https://arxiv.org/html/1401.0917v2 (Theorem 1.1) ; https://arxiv.org/html/2604.01214v1 (Sections 1.1 and 2.1.1). The last is a rotationally invariant Riemannian model and supplies no lattice transfer.
