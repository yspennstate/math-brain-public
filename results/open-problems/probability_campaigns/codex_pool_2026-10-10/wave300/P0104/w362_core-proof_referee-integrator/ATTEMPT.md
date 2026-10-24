# P0104 referee checkpoint

The original ranking is a dated pointer, not a complete theorem statement. The exact P0104 record was recovered at ~/Downloads/Probability_1000_20h_20260906/problems.jsonl:175. It groups Questions 13 and 15 of Auffinger--Damron--Hanson, *50 years of first passage percolation*. In checked arXiv v2 both questions occur on PDF page 37. Their requests are strict subdiffusivity in dimensions at least two, exponent 1/3 in dimension two under suitable edge-law conditions, and a positive exponent in a suitable dimension. Section 3.1 explicitly leaves the meaning of the variance asymptotic open. The source supplies no single complete universal hypothesis package.

For this proof attempt only, choose nearest-neighbor undirected Z^2 with iid Uniform[1,2] edge weights, T_n=T(0,n e1), and ask for Var(T_n)=n^(2/3+o(1)). This is an explicit restricted target, not a claim that the source chose these hypotheses. Neither limit-shape curvature nor exponent existence is assumed proved. Current openness on 10 October 2026 remains UNKNOWN under the targeted status check; the April 2026 primary paper arXiv:2604.01214 still describes the lattice polynomial improvement as open. Its proved polynomial improvement concerns a different, rotationally invariant Riemannian model.

Two independently checked partial inputs are now saved in PEER_REVIEWS.jsonl. w360-C1 makes this bounded-edge problem exactly a finite product-space function, without a cutoff extrapolation. w361-C001 refutes multiplying conditional selected-path probabilities merely because the original edges were iid.

## A rigorous route that preserves the open input

Let f=T_n on the finite edge set supplied by w360-C1. Refresh each coordinate independently at rate one, and write W^t for the environment after time t, with one-coordinate retention probability exp(-t). A product-space orthogonal expansion gives

    Cov(f(W),f(W^t)) = sum_{S nonempty} exp(-|S| t) ||f_S||_2^2,
    H_n(t) = sum_{S nonempty} |S| exp(-|S| t) ||f_S||_2^2,
    Var(T_n) = integral_0^infinity H_n(t) dt.

H_n is nonnegative and decreasing. An independent derivation of these identities, including the required orthogonality, is the next proof step. This is a covariance identity, not a product of selected-path events.

The hardest missing input for this route is a scale-sharp noise crossover, not the formal covariance integral. A sufficient single two-sided lemma would give, for every epsilon>0 and all large n,

    H_n(n^(-1/3-epsilon)) >= c_epsilon n,
    integral_{n^(-1/3+epsilon)}^infinity H_n(t) dt <= C_epsilon n^(2/3+epsilon).

Together with H_n(0)<=K n this would imply Var(T_n)=n^(2/3+o(1)). BOTH crossover inequalities remain unproved. The scale n^(-1/3) is an input to be justified by planar optimization; it cannot be chosen because it yields the desired answer. An estimate at an arbitrary polynomial scale would only prove an unspecified improvement, not exponent 1/3.

NEXT: Prove a quantitative coupled-threshold estimate after separating first-order energy; the covariance reduction and received peer claims are audited.

Final peer revision: FIRST_ORDER_FLOOR_AUDIT.md separates the unweighted first-order floor from its remainder. The finite-time weighted-energy calibration above remains valid. R004 records the provisional-route FIX and R007/R008 the independently checked repair.
