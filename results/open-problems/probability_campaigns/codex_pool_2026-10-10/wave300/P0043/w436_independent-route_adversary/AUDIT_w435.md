# Independent audit of the original w435 auxiliary proofs

The degree-9 dyadic tree and its second-moment proof were saved in INDEPENDENT_DERIVATION.md before w435/ATTEMPT.md was read. This audit examines the author's proofs, not a review of them.

L1: KEEP as an auxiliary result. Independently fix rational r<1, sample the two independent edge fields, and observe that their product has parameter p_c r<p_c. Its probability of any infinite component is zero. Conditioning on the p_c field gives a nonnegative conditional probability of expectation zero; it is zero almost surely. The countable rational intersection and monotonicity handle all r<1 and all components at once. The conclusion p_c(C)=1 is correct and does not require quasi-transitivity.

L2: KEEP as a sufficient condition. For two length-n simple prefixes with k common undirected edges, their union contains exactly 2n-k edges. Edge independence gives r^(2n-k), and normalization gives the second moment E r^(-k), bounded by I_r. Cauchy-Schwarz is justified. The events of an open path of length n, rather than the potentially non-nested events Y_n>0, are used for continuity from above; local finiteness supplies an infinite ray. No product of exploration probabilities is used.

L3: KEEP with the stated finite-degree, finite-cutset assumptions. A simple ray has signed divergence 1 at o and 0 at every other vertex. Integrating is valid because each vertex has finite degree. Tonelli and |f(e)|<=a_e give the energy bound. Boundary flux is 1 even if a ray crosses a boundary repeatedly; entries and exits cancel. Square-ball boundaries have 8j+4 edges and are disjoint, so their reciprocal sum diverges. This is a limitation of the ray-energy method, not a counterexample to critical extinction.

L4: KEEP as a counterexample outside the conjecture's class. Independently grouping n between k^2 and (k+1)^2-1 gives 2k+1 indices with floor(sqrt(n))=k. The series sum (2k+1)2^(-k) equals 5, so the displayed energy is 7/2. The first-moment decay below 1/2 and unique degree-4 root arguments are correct.

G1 / proposed completion: FIX — leave unproved. Finite ray energy on the host graph does not transfer to a critical component. A concrete separate example is the saved dyadic tree: its host has finite uniform-ray energy I_(1/2)=5/4 and critical survival at least 4/5, while almost surely every surviving critical component has quenched threshold 1 and hence admits no finite I_r measure for any r<1. This follows by independently repeating the thinning argument for this explicit tree and then applying the independently checked L2 contrapositive.

Minimal missing premise for the intended completion: a consequence of the full quasi-transitive hypotheses which, under hypothetical critical survival, constructs a ray measure on a surviving critical component with finite I_r for some r<1; recurrent classes also need another argument. This premise would contradict the valid L1 and prove critical extinction, but no derivation of it is supplied. The obstruction is not itself quasi-transitive, so it does not disprove that implication with the full P0043 hypotheses.

The full P0043 verdict is UNPROVED BY THIS ROUTE. The independent referee w437 should review the original auxiliary proofs and this obstruction; the main theorem has not been promoted.
