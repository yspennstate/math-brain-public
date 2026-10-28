# Independent scoped review: A077 event-source reduction holds

Reviewed source: A077-COMPLETE-EVENT-SPECTRUM-TRANSFER@1, PROOF.md equations (7)-(9), run 20261027T084958Z-account04-A077-sparse-defect-towers. Original exact statement SHA256: 1efa805d5d6903430571d93310e74c5fc3af99df7b5b88f471e5d44c832ccb63. Verdict: HOLDS for the constant-carrier, one-private-sign activation identities and C*<=K*<=2C* reduction ONLY. The full transfer inequality (1) and recursive closure are not independently accepted by this review. No repair is supplied to the reviewed version.

For an event indicator a of mass 0<p<=1/2, put e=1-2a and W=1-a+ay, with y a fresh uniform sign. Its actual coefficients are 1-p at empty, -ahat(S) at nonempty shared-only S, and ahat(S) at every row containing the private coordinate. With phi(t)=-t log2(t) and all empty rows retained, this gives

 H(W)=phi((1-p)^2)+phi(p^2)+2 sum_{S nonempty}phi(ahat(S)^2),
 H(e)=phi((1-2p)^2)+4 sum_{S nonempty}phi(ahat(S)^2)-8p(1-p).

Both root terms in H(W) are nonnegative. For 0<=x<=1, phi(x)<=(1-x)/ln2<=2(1-x), using ln2>=1/2. Thus phi((1-2p)^2)<=8p(1-p), including x=0 by continuity, and H(e)<=2H(W).

Actual shared edges disagree exactly half as often as event-sign edges: J(W)=I(e)/2. The private influence is p, so I(W)=p+I(e)/2. A separate Parseval check gives I(e)>=Var(e)=4p(1-p)>=2p, hence I(W)<=I(e)=2J(W). This avoids importing edge isoperimetry for this particular reduction. Denominators J and I(e) are positive because a nonempty proper event is not constant.

Let C* be the supremum of H(e)/I(e) over nonconstant Boolean signs, and K* the supremum of H(W)/J(W) over all such minority events. Complementing a sign preserves H,I and ensures p<=1/2. The previous inequalities imply pointwise

 H(e)/I(e)<=H(W)/J(W),
 H(W)/J(W)<=2 C*.

Taking suprema proves C*<=K*<=2C*, also when infinite. No supremum attainment, limit exchange, or Boolean realizability assumption is omitted. Constants have zero entropy and need no ratio. The p=1/2 endpoint is valid; p=0 is excluded only from the ratios. A biased private profile is outside this reviewed claim.

The independent checker exhausts ALL 174 nonempty minority event tables on dimensions 1,2,3 without symmetry reduction. It reconstructs spectra by direct character sums and influence by physical edges, verifies both entropy identities, the complete H(e)<=2H(W) inequality and all original private/shared influence terms. Exact rational logarithm certificates are recorded in out/INDEPENDENT_REVIEW.json; finite checks support, and do not replace, the argument above. This is independent review of A077 by A078. The separate parity-family implementation remains a same-author code reproduction and is not independent mathematical review of A078.

Downstream implication: arbitrary-event shared-only pricing is already full-FEI strength, so it cannot be installed as an unexplained new source. The next arbitrary-core payment must retain the original unused source, old debits and BOTH full terminal potentials. No new class constant is inferred here.
