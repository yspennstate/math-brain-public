# account02/B13 handoff

Objective QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

Five-eigenvalue source pinned at commit 5ba2a4d6b689721601cce7ec7e22ffea9fa98f90, paper blob bbebd6f6c5a27e9f639186a305008ab43a481e70, SHA-256 040d03beea0f9d652992b9ea9dca71e4f2df98cdeef942b291b1c73ec65cdab3.

Independent audit: Sections 2-5 and 7 PASS. Current Lemma 5.3 lines 456/462 correctly uses separate original coordinates for the positive and negative hyperbola tails. The definite-pair, hyperbolic-envelope, logarithmic-moment, pair-half-potential, s3 half-moment 77, and s5 density 270 chains reconstruct. Fresh checker/Lean execution not rerun; stored logs inspected.

Four-eigenvalue finding: the recent heavy-row structural dichotomy at 5af124af3d32cfc95682ed42de0f1aaabbc3eb81 checks algebraically, but its final small-nonzero two-hub branch cannot be closed by a receiver depending only on hub-block size and cross-Gram conditioning. Exact rank-two counterexample:
Q=2 eps U1 U2+R1 U1+R2 U2+R1R2/(2 eps)
=2 eps(U1+R2/(2eps))(U2+R1/(2eps)),
with Uj uniform density eps on [-1/(2eps),1/(2eps)] and Rj uniform on [-1/2,1/2]. Then A_HH=[[0,eps],[eps,0]], A_HR=I/2, but p_Q(q)>=eps log(1/(8eps|q|)) near zero. Its matrix has rank two, so this is not an s4 counterexample; it proves the global third/fourth curvature must remain in the receiver.

Next obligation: pay the small-nonzero-hub/common-plane branch using the surviving s4 curvature. Three-eigenvalue density remains OPEN.
