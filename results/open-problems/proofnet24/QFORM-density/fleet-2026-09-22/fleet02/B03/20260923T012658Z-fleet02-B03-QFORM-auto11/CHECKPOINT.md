SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-23T01:26:58Z.
attacking: rank-two decoupled volume plus an aggregate square channel, preserving sum/difference dependence and paying the half-Riesz endpoint before any local coefficient inversion.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Source actually used: fleet03/B03 `QFORM-VOLUME-MARGINAL-WEIGHTED-RIESZ-v1`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T235821Z-fleet03-B03-QFORM-r22/REPORT.md` (search-visible at repository state `370534c8763da810a1b81945e0e44344feab0b75`), itself derived from the pinned Claude volume-sampling decoupling theorem in `interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md` at `e5f71d79eff325201dd0274053d20268ce65b837`.

Let R be a quadratic-plus-linear polynomial on disjoint original-coordinate banks I,J with cross block M=A[I,J]. Put

Z2=e_2(M^T M)>0,

and let h be the maximum I-row marginal of the squared 2x2-minor volume-sampling law. If h<1 and q=max(1,2h), the partner theorem gives, without declaring any conjugate sum/difference variables independent,

sup_s E|R-s|^{-1/2} <= C2(h) Z2^{-1/8},
C2(h)=8/(2-q)*(e/q)^{1/4}.

New implication: let Y be an independent scalar with density cap M_Y, while m(W) and R(W) may be arbitrarily dependent functions of all other active variables W. Then

Q=lambda [Y+m(W)]^2+R(W), lambda !=0,

satisfies

||p_Q||_infinity <= C2(h) M_Y |lambda|^{-1/2} Z2^{-1/8}.

Proof: conditioned on W, the translated square has density at u bounded by M_Y |lambda|^{-1/2}|u|^{-1/2}. Averaging gives p_Q(s)<=M_Y|lambda|^{-1/2} E|s-R|^{-1/2}, then apply the partner endpoint. This immediately extends the physical-square transducer to an entire disjoint original-coordinate aggregate bank: for Y=v^T X_K, the standard one-dimensional product-projection bound gives M_Y<=sqrt(2)/||v||_2.

A second, additive-square estimate is being derived directly from the same decoupled envelope by Holder with the sharp square L^r density calculation. It will yield an L1 characteristic function and therefore a continuous density when the aggregate square shift depends only on conditioned outside coordinates.
