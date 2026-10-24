# C0054 statement-only packet for independent adversary w601

2026-10-10; no proof route is included in this first packet.

Exact recovered intake statement (problems.jsonl, line 54): "For d = 2 and fixed band width W, all bulk eigenvectors of the random band matrix on a box of side N are localised with localisation length of order exp(W^2), and the local eigenvalue statistics are Poisson as N -> infinity."

Primary source: P. Bourgade, Random band matrices, ICM 2018, https://math.nyu.edu/~bourgade/papers/ICMProceedings.pdf. Conjecture (0.2), page 2; discussion in Section 2.2, page 7. The lattice is a periodic box of side N, not a matrix of dimension N: in d=2 there are N^2 sites. Entries are centered real independent random variables up to H_xy=H_yx. H_xy=0 beyond periodic l1 distance W. Nonzero variances are comparable and have row sum one. Bulk means |E|<2-kappa with fixed kappa>0. The conjectural crossover is W_c approximately sqrt(log N); the associated predicted length grows exponentially in W^2.

Quantifier caution: this survey statement is not a fully specified universal theorem for every entry law. The claim about order exp(W^2) refers to varying W and needs explicit constants and a definition of localization length; holding W fixed only asks for a finite localization length. Exponential resolvent decay alone also needs separate spectral-statistics hypotheses and argument before claiming Poisson statistics.

Precise first test model: W>=1 is an integer, N>2W, off-diagonal support is 0<|x-y|_1<=W on (Z/NZ)^2. Let M=2W(W+1) and sigma=(M+1)^(-1/2). All unordered off-diagonal entries are independent sigma times N(0,1); diagonal entries are independent sigma times N(0,1), independent of the off-diagonals. Then every row variance sums to one. Finite Dirichlet submatrices use the same entries without renormalization.

A precise sufficient localization target for this Gaussian subclass is: for each fixed W and kappa, find s in (0,1), C<infinity and mu>0, independent of volume, E in [-2+kappa,2-kappa] and eta>0, such that E|((H_Lambda-E-i eta)^(-1))_xy|^s <= C exp(-mu |x-y|_1) in every finite box Lambda. This is a proposed sufficient formulation, stronger than a mere statement that eigenvectors localize. It does not include a proved exp(W^2) asymptotic or Poisson theorem.

Current-openness status: UNKNOWN after a bounded literature and local prior-record check. Recent primary references are arXiv:2503.07606v1 and arXiv:2609.24426v2 (6 October 2026); these give growing-W delocalization/lower bounds, not a fixed-W localization proof. No novelty or parent-solution claim.

Independent task: challenge the assumptions/quantifiers and seek an independent obstruction or proof route before reading ATTEMPT.md. Send any new lemma for review by w602; w605 is the independent reviewer for w602's own new results.
