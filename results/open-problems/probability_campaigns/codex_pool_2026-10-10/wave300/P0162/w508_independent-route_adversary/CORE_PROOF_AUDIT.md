# Adversarial check of w507 L1-L3

2026-10-10. Read w507/ATTEMPT.md only after saving ATTEMPT.md and the original INDEPENDENT_DERIVATION.md. This is a proof check, not a review of a review. Assigned final referee: w509.

Verdict: KEEP the narrowly stated L1-L3 as analytically sound draft results. They do not prove P0162.

L1: The pair masses A_T^2+B_T^2=(u_T^2+v_T^2)/2 sum to one by Parseval. Entropy decomposes exactly into the entropy of these masses plus weighted binary entropy. Subtracting the averaged restriction entropies gives Jensen-Shannon divergence plus that binary term. Both are nonnegative. The influence identity pairs weights |T| and |T|+1. No joint independence is assumed.

L2: The two-bit Walsh transform is (1,1,1,-1)/2. Tensor multiplication is valid because the inputs are disjoint. The one-point indicator has every coefficient 1/N, so B_T=1/N, I_y=1/N, r_T=(N-2sigma_T sqrt(N)+2)/N^2 and q_T=1/(N-2sigma_T sqrt(N)+2). The denominator is positive even at m=2. The lower bound follows by dropping a nonnegative divergence and using binary_entropy(q)>=q log_2(1/q). It tends to infinity with even m. The quantifier being refuted is 'for every f and every i'.

L3: For an original coordinate j, flipping g(0) toggles the single undirected edge {0,e_j}. This was a non-boundary edge since g(0)=g(e_j)=1, so I_j(h) increases by exactly 2/N, not 1/N. Averaging the restrictions gives I_j(F)=1/2+1/N. The selector is uniquely least influential. The asserted total influence follows by summing. H(F)<=m+1 and m+1<=3 I(F) for m>=2 are valid, including the boundary case m=2.

Attempted breaks and limits: no failure from the 0log0 convention, m=2, the two-endpoint influence count, or dependent spectral coordinates. The construction is not monotone; it supplies no counterexample within the monotone class. Neither an arbitrary-coordinate obstruction nor failure of the minimum-influence rule refutes a well-chosen-coordinate induction.

Hardest remaining piece: prove a dimension-free coordinate-selection or aggregate-charge lemma for all Boolean functions. The proposed sufficient selection premise remains unproved. A successful finite verification or a source receipt would not close it.

NEXT: w509 checks the actual mathematical statements independently; w508's sparse-flip extension is in INDEPENDENT_DERIVATION.md.
