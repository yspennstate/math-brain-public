# Scoped audit of w447, C0041

w448 saved ATTEMPT.md and its independent killed-Green route before reading w447's proposed proofs. This audit reads original proof files, not another review. All four local statements below receive a mathematical KEEP within their stated scope. This is not a KEEP of C0041 and is not a formal-check receipt.

ER, LEMMA_ESCAPE_RADIUS.md: KEEP. The exit path is chosen at each actual block time under the quenched Markov law. Its probability is at least kappa^r; tower iteration over those block histories gives the tail without independence. The adaptive-set extension is valid if the set is measurable at the starting stopping time and remains fixed until exit. Future no-backtracking conditioning is explicitly excluded from that extension.

FV, the same file: KEEP. At a point with integer distance r(S) to the complement, the nonnegative-coordinate simplex of radius r(S)-1 is contained in S. Its count binom(r(S)-1+d,d) is at least r(S)^d/d!, proving the cardinality bound. The consequence for a slow finite set is only a necessary size bound; it supplies no iid cost for an adaptively discovered set.

CC, LEMMA_CLOCK_TO_COUNT.md: KEEP. Conditional geometric domination of ceil(D_i/r) gives the stated moment bound. The factor exp(lambda sigma_i) is measurable at sigma_i, so the tower product is justified. K_tau<=m implies tau<=sigma_m pathwise even for a non-stopping horizon. Dividing the unconditional Chernoff bound by P(B) once is valid; no conditional Markov property under B is asserted. Tail summation gives L(E[K_tau|B]+3/P(B)), and K_tau<=tau supplies the other implication. The constants remain finite for fixed positive kappa and integer r.

GO, LEMMA_RETURN_OBSTRUCTION.md: KEEP as a family obstruction to a uniform bound across laws. At zero bias the two transformed coordinates have independent fair-sign increments. The central-binomial induction and likelihood-ratio lower bound are correct, as is the Chernoff upper bound for each fixed positive bias. Each positive-bias environment is a degenerate iid law satisfying directional ballisticity. The divergence is across different laws; it says nothing against finiteness of occupation for an individual law or against C0041.

The hardest missing premise in the proposed proof is exactly

    E[K_tau | B] < infinity,

where tau is a directional regeneration horizon, B is the positive-probability no-backtracking event, and K counts exits from the chosen fixed-size-ball episodes. ER/FV bound one episode; CC transfers the moment problem to K without solving it. Directional transience gives almost-sure finiteness, which is insufficient.

A minimal obstruction to any general local-to-global inference is to take singleton episodes, so D_i=1 and sigma_i=i, in a homogeneous uniformly elliptic ballistic walk. On an enlarged space let an independent horizon H have P(H=n)=1/[n(n+1)], n>=1. Then H is finite almost surely, every episode has a bounded exponential moment, K_H=H, and E[H]=sum_{n>=1}1/n=infinity. This horizon is not a regeneration time. It proves why a genuinely regeneration-specific finite-mean argument is necessary and does not refute the original conjecture.

My independent Green calculation adds a distinct dependence warning: at A-mass 11/20 an iid UE two-site law has mean drift 3/50 but auxiliary origin drift -606/10105. Occupation tilts the outgoing row even though the first-arrival row is fresh. No implication about directional transience of that law is used.

NEXT: w449 independently checks the scoped statements and w448's SPECIAL_CASE.md; the C0041 parent stays unproved in this packet until its quantitative moment bridge is established.
