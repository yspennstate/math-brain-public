VERDICT: PROVED exact shortest-crossing generating function and conditional length asymptotics for the two-row square-lattice ladder at p=1/2

For the ladder with columns 0 through n and two rows, let H_n denote an open left-right crossing and let S_n be its shortest edge length, with free boundary endpoints. PROOF.md establishes

\[
\sum_{n\ge0}\mathbb E[\mathbf1_{H_n}t^{S_n-n}]z^n
=\frac{1-(1+t)z/8}{(1-z/4)(1-(5+t)z/8+z^2/16)}.
\]

The expectation in this notation is the marked sum over crossing configurations; S_n need not be defined off H_n. In particular,

\[
\mathbb E[S_n\mid H_n]=(1+1/(2\sqrt5))n+O(1),\qquad
\operatorname{Var}(S_n\mid H_n)=7n/(20\sqrt5)+O(1).
\]

The same linear constant governs all fixed interior conditional quantiles. The proof is self-contained and uses a decomposition by forced rail changes. finite_checks.csv contains exact configuration counts for n=1,2,3, derived by hand in the proof. No novelty claim is made for this strip formula.

The literature search found no later solution beyond the supplied status. The paper actually opened was Irina Đanković, Maarten Markering, Jason Miller, and Yizheng Yuan, *The scaling limit of random walk and the intrinsic metric on planar critical percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122), including its [full HTML](https://arxiv.org/html/2604.14122v1). It proves existence of the triangular-lattice exponent; the checked material does not determine its value or establish square-lattice universality. The bounded search cannot exclude a missed paper. Queries and source details are in LOG.md.

Validation: crossing probabilities were re-derived with a separate two-state connectivity transfer matrix; the mean and variance coefficients were differentiated both from a radical expression and implicitly from its quadratic; and the first three finite distributions were obtained both by direct cut classification and by coefficient extraction. Boundary rungs, empty cuts, absent forced constraints, and disjointness of the required rung intervals are treated explicitly.

Commands: no computational run is needed to reproduce the result; every calculation is displayed in PROOF.md. The resource probe `env OMP_NUM_THREADS=1 nice -n 15 /bin/date '+%Y-%m-%d %H:%M:%S %Z'` returned `nice: setpriority: Operation not permitted`. A second harmless probe confirmed this restriction. No substantive numerical program was run, and no compiler or simulation was started. File and memory reads, web queries, and file writes were the only other operations. All new files are in this folder.

What failed and what remains open: the monotone-path argument fails already on three rows, as shown by a seven-edge crossing written out in PROOF.md. On a fixed-width ladder, crossings at p=1/2 are exponentially unlikely; this is a different regime from planar critical box crossings. No new bound on the planar chemical-distance exponent, value of that exponent, or universality theorem follows. Whether the exact strip formula already appears in the literature was not investigated.

Next worker: use this formula as a check for an independently implemented wider-strip algorithm. At three rows, retain enough information to allow three traversals of a vertical cut; the explicit backtracking example must be accepted. Any eventual application to T088 will also need estimates uniform in strip width. Simply taking the fixed-width linear exponent and sending the width to infinity has no justification.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 21:57 +04 (first recorded shell clock).
