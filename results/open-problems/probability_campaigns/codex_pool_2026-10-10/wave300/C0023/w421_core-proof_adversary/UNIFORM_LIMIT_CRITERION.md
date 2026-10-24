Exact missing input for the one-arm route, 2026-10-10.

For iid nearest-neighbour bond percolation on Z^d let a_n(p)=P_p(0 reaches the boundary of [-n,n]^d), and let p_c be the critical parameter. For 0<delta<p_c define
U(delta)=sup_{n>=1}[a_n(p_c)-a_n(p_c-delta)].
Then theta(p_c)=0 if and only if lim_{delta decreases to 0} U(delta)=0.

Proof of sufficiency. For each fixed delta, theta(p_c-delta)=0. Taking n to infinity in the bracket gives theta(p_c). Thus theta(p_c)<=U(delta), and a vanishing U forces critical nonpercolation.

Proof of necessity. If theta(p_c)=0, choose N so a_n(p_c)<=epsilon for all n>=N. The corresponding brackets are at most epsilon. For the finitely many n<N, finite-event continuity gives a common sufficiently small delta making each bracket at most epsilon. Therefore U(delta)<=epsilon for that delta and all smaller positive delta.

For n fixed, let I_n(p) be the sum over bonds internal to the box of P_p(the bond is pivotal for its one-arm event). The finite product derivative identity gives a_n'(p)=I_n(p), hence the same missing input can be written
lim_{delta decreases to 0} sup_n integral_{p_c-delta}^{p_c} I_n(p) dp=0.
This identity follows by differentiating the multilinear product expectation in each coordinate and then restricting all coordinates to p: each coordinate derivative is P(A|edge open)-P(A|edge closed), which is the pivotal probability because A is increasing.

A proved route would bound these integrals uniformly in n; ordinary bounds I_n<=number of bonds depend on n and do not do this. The product-event countermodel in ATTEMPT.md has an atom of derivative mass of at least 253/256 at its critical limit, so finite polynomial continuity cannot replace this input.

This is an equivalence identifying the open input, not a proof that it holds in dimensions 3 through 10. No novelty claim is made.
