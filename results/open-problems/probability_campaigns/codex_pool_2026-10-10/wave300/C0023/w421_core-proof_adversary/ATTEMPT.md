Independent checkpoint, 2026-10-10. Saved before reading w420's proof.

For nearest-neighbour Bernoulli bond percolation, finite-box one-arm probabilities decrease to theta. Their continuity proves right-continuity of theta but does not prove left-continuity at p_c. The crucial unresolved input is a decay or a uniform parameter-continuity estimate for one-arm events at arbitrarily large scales. Claim C0023-w421-001 gives the elementary reduction and explicitly leaves critical decay open.

Independent obstruction saved before reading the paired prover, 2026-10-10:

Let X_1,X_2,... be independent Bernoulli(p), S_k=sum_{i<=k} X_i, and
A_n=intersection_{1<=k<=n}{S_k >= k/2 - 2 k^(2/3)}.
These are increasing, nested cylinder events. Every a_n(p)=P_p(A_n) is a continuous polynomial. Nevertheless f(p)=lim_n a_n(p) has critical point 1/2 and f(1/2)>=253/256, while f(p)=0 for every p<1/2.

For p<1/2 the strong law gives S_k/k -> p, so the constraint fails eventually. At p=1/2, E exp(-t(X_i-1/2))=cosh(t/2)<=exp(t^2/8). Chernoff's bound with t=8 k^(-1/3) gives P(S_k<k/2-2k^(2/3))<=exp(-8 k^(1/3)). The union bound and monotonicity of this last function give
sum_{k>=1}exp(-8 k^(1/3)) <= integral_0^infinity exp(-8 x^(1/3)) dx = 6/8^3=3/256.
Thus P_{1/2}(intersection_n A_n)>=1-3/256. Increasingness in p makes f positive for p>=1/2, establishing its critical point.

This is a counterexample to a general limit argument based on independent product measures, increasingness, nested cylinder events and finite-event continuity. It is NOT a counterexample to nearest-neighbour lattice percolation: the constraints have no translation-invariant local connectivity rule. A lattice proof must supply an additional estimate using its geometry.

Candidate missing input: a modulus of left continuity for finite-box one-arm events uniform in box size. Ordinary continuity gives a parameter interval depending on the box and cannot justify exchanging the parameter and volume limits.

Primary-source checkpoint: Cerf, arXiv:2608.23661v1 (24 Aug 2026), section 1 and Conjecture 1.1, still formulates critical non-percolation as a conjecture for site percolation. The experimental HTML contains only the introduction and references although the abstract announces another result; it cannot support a full proof audit of that announced result. Fitzner--van der Hofstad, arXiv:1506.07977v2 (23 Mar 2017), is explicitly nearest-neighbour percolation in d>=11. Exact intake model scope and owner solved/retired checks remain pending.

NEXT: Recover the C0023 intake row; formalize the uniform pivotal-integral criterion and audit the paired route.
