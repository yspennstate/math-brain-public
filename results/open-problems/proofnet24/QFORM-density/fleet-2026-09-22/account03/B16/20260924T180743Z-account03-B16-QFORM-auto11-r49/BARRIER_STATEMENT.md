# QFORM-SMALL-INDEFINITE-SOURCEBLOCK-PERTURBATION-FALSE-v1

For 0 < eps <= 1/2 let U1,V1,U2,V2 be independent Uniform[-1/2,1/2] variables and set

Q_eps = eps U1^2 + 2 U1 V1 + eps^(-1) V1^2 - eps U2^2 - 2 U2 V2 - eps^(-1) V2^2.

Equivalently,

Q_eps = eps (U1 + V1/eps)^2 - eps (U2 + V2/eps)^2.

The source block on (U1,U2) is diag(eps,-eps), whose norm tends to zero. The physical cross block from (U1,U2) to (V1,V2) is diag(1,-1), so det(B B^T)=1 for every eps. Nevertheless Q_eps has an essentially unbounded logarithmic density near zero.

This is NOT a counterexample to the owner target: the full coefficient matrix has spectrum {eps+eps^(-1), 0, -(eps+eps^(-1)), 0}, so only two eigenvalues are nonzero. It refutes only a perturbative extension of the exact-zero two-source shared-bank theorem to small indefinite source curvature with arbitrary same-bank curvature retained.
