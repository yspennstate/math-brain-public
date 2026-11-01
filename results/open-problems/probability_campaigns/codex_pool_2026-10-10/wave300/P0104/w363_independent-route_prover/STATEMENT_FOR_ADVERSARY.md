# P0104: exact source and chosen precise subproblem

Primary source: Auffinger, Damron, Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Section 3.1, Questions 13 and 15 (PDF p.37, zero-based page 36). Source retrieved 2026-10-10. The dated P0104 campaign card includes both questions.

Question 13 asks for chi<1/2 in dimensions d>=2 under suitable laws, and for chi=1/3 in d=2. Question 15 also asks for chi>0 in a suitable dimension. Here chi is the passage-time fluctuation exponent, with variance exponent 2 chi. The preceding discussion explicitly allows the interpretation Var T(0,x)=||x||_1^(2 chi+o(1)); it does not enumerate all "suitable conditions". Thus the ranking title is not a complete quantified theorem statement. The third positive-exponent branch is not solved by this packet.

Model: iid nonnegative edge weights on nearest-neighbor Z^d, T(u,v) the infimum of sums over finite u-v lattice paths. A precise directional formulation asks whether chi_2(F,e1)=lim_{n->infinity} log Var T(0,n e1)/(2 log n) exists, is less than 1/2, and equals 1/3 when d=2, for an explicitly stated class of laws F.

Chosen special-law subproblem for this packet: d=2, weights tau_e=1+eta_e, independent eta_e~Bernoulli(99/100), endpoint n e1, integer n>=1. Does Var T(0,n e1)=n^(2/3+o(1))? This is a precisely specified exploratory specialization, not a claim to settle Questions 13/15 for all "suitable" laws. No curvature or absence of all flat edges is certified for this law. No claim of novelty or current certified openness. Current global openness: UNKNOWN after limited source/local checks.

Adversary request: inspect the statement and this special law independently first. In particular, check the distinction between variance exponent and standard-deviation exponent, and whether any degenerate/flat-edge obstruction applies. The proof route is intentionally omitted from this first packet.
