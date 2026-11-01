# Source-bound reviews and scope

## Prior A003 claims

Consume A004 run 20261013T235034Z REVIEW.md and REPORT.md: A003-ONCE-SLICED-MAJORITY-ERASURE@1 and A003-TWO-QUERY-ELIGIBLE-PREFIX@1 independently HOLDS at their original abstract scopes, with statement/hypothesis hashes 4c5518b43c13eabc5828606942a620d4257f6e51e2fdfe28607e62c4f84489f3 and b95bc46e28f201fe75376df07dbde98584cc26b50ba192c171d582ae9e7033e9. No instantiated B05 or universal FEI acceptance is inferred. The original run is preserved unchanged; acceptance is recorded as a consumed source in this run.

## A026 signed-row transfer v1

Verdict: HOLDS at its stated scalar, disjoint-composition and encoder-only variance scope. Reconstruction: let L(x)=Phi_nat(x^2,1). Its derivative 2x ln(1+x^-2) has exactly one maximum because L''/2=-ln(1-v)-2v, v=1/(1+x^2), crosses zero once. At a positive interior maximum of L(x+y)-L(x)-L(y), x and y must both lie on the increasing derivative branch, hence x=y. Boundary values or limiting maxima are nonpositive. Writing u=x^2, the diagonal derivative is 4ln(1+1/(4u))-2ln(1+1/u); its sign is that of 1-8u. The maximum u=1/8 gives ln(32/27). Opposite signed amplitudes have nonpositive excess by monotonicity.

In the coherent composition packets, applying this bound with (a,b,c)=(Ahat,mu Dhat,gamma Dhat) cancels delta Phi(mu^2,gamma^2) exactly. For 0<=t<=1 the difference t Phi(a,b)+tb log2(1/t)-Phi(a,tb) is decreasing in a and tends to zero at infinity, hence is nonnegative. Applying t=gamma^2 leaves gamma^2 B_z(f), with its stated logarithmic correction. Boolean derivative averaging gives |gamma|<=d, which bounds the correction by [log2(32/27)+2/(e ln2)]delta d. The encoder-only mean martingale pays gamma^2 once as a variance drop, independent of query order.

The bent-flip shadow coefficients and packet lower bound are reconstructed directly in DERIVATION section 3. They establish A026's encoder-only no-go, and the new interleaved witness adds the actual unlocking data-bit budget. No repair to A026 was needed and no independent review of unrelated source chains is asserted. A003's earlier slice input is not needed for this acceptance of A026's self-contained scalar/interface/ownership proof.

## A096 witness consumption and nonduplication

Read REPORT.md and DERIVATION section 4 of A096 run 20261014T013836Z. Reuse its explicit g and parity duplication f=G, rather than inventing another local KL witness. Its correct physical influence I(G)=k/2+(k+2)delta differs from I(g) and from the new majority substitution I(F); these are three distinct functions. The present result translates that source's informative-partner obstruction into signed shadow-variance transport. It does not independently certify its complete conditional-KL claim or claim a new Boolean family.

The optional A024 new-run REPORT read failed because that run contains only a .final marker. No mathematical premise is attributed to an unavailable A024 proof. Its rolling status is navigation only. A027's new REPORT was read to distinguish its single physical point-event projection from our spectral-shadow account; no A027 theorem is used as a proof premise.
