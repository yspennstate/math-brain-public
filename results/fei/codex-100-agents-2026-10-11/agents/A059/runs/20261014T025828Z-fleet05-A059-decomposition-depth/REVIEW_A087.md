# Independent scope reconstruction of A087's controller residuals

Source: agents/A087/runs/20261014T020842Z-fleet05-A087-restriction-referee,
PROOF.md, REPORT.md and CLAIMS.json. Only the new killed-child and independent-
child controller residual theorem is reviewed; bundled A064 assertions are
not accepted by this file.

For a killed +1 child and a live child with mean profile g, pair all nonempty
data rows. Their erasure entropy cancels the fine reserve release. Nonempty
controller rows of the mean profile survive as Var(g)/2. The remaining mean
packet is Phi((1-d)^2,d^2), d=(1-Eg)/2. Since Var(g)/2<=2d(1-d), A091's
scalar inequality prices the sum by 3d. Physical JS adds at most 2d/ln2.

For independent data blocks in the two children, the same direct frequency
separation leaves [Var(g0)+Var(g1)]/2 and the packet of squared half-sum and
half-difference means. The first part is <=2d, the packet <=2d by
Phi(a,b)<=2 sqrt(ab), where d=(1-mu0 mu1)/2. Thus the residual is bounded by
(4+2/ln2)d. The Boolean child mismatch is d because the blocks are disjoint.

Verdict: ACCEPT_AT_STATED_SCOPE_NO_REPAIR. This is an analytic reconstruction
independent of A087's program. Own 81734-assertion mixed-state validation
additionally exercises killed-child states. This verdict does not extend the
independent-child hypothesis to repeated fallback data. PRIORITY_PROOF.md
is a separate authored extension addressing exactly that excluded geometry.
