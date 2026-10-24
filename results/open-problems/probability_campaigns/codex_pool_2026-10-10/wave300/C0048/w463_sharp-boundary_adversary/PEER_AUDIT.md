# Independent audit of w462's C0048 packet

Auditor w463; 2026-10-10. Audited author proof: ~\brain_workers\w462\ATTEMPT.md. SHA-256 at review: 295fd69a107e196d7bc92b356a086d0e4c5a6a38330d6df7eac17a355e90ee2b. The independent minimax derivation in this worker's ATTEMPT.md was saved before the paired proof was opened. This reviews the author's proof, not a review of it.

KEEP L1, L2 and L3 with exactly their saved assumptions. L1 correctly conditions each factor on earlier events. Uniform conditional closure survives partial conditioning by the tower property; disjointness makes the prefix measurable outside the next block. The finite-volume inequality is uniform in boundary partition and passes to finite cylinder events in a weak limit. L2 uses ordinary physical paths and a finite-width cross-section. Boundary coloring only needs an ordinary path to either physical end, even when those ends are wired together. L3 checks degree, transitivity and the explicit amenability ratio and clearly distinguishes the strip from Z^3.

Three necessary qualifiers have exact failure controls, checked by python -X utf8 check_peer_bound.py:

* Disjointness: at q=1,p=1/2, counting the same one-edge set twice gives actual intersection 1/2 but the proposed product 1/4.
* q>=1: on a free one-edge graph at q=p=1/2 the open probability is 2/3, above the putative upper bound p=1/2.
* Ordinary paths: on -1--0--1--2 with end vertices wired, at q=3,p=1/2 the ordinary right-crossing probability is 1/11, while wired connectivity to the right end is 7/22>1/4. The ordinary two-cut upper bound is 1/4. A proof silently replacing ordinary crossing by wired connectivity would fail.

The same eight-state q=3 calculation gives P(A1 intersection A2)=3/22>P(A1)P(A2)=15/121 for A1=left edge open and A2=at least one right edge open. Thus multiplying unconditioned marginal upper bounds really fails, while w462's uniform conditional bound, 3/8, remains valid. At q=1 the disjoint-block bound is attained exactly.

These controls do not refute any of w462's properly scoped lemmas. They delimit what can safely enter the brain. The hardest remaining gap is theta^wired(pc,3)>0 on Z^3; none of these upper bounds supplies it. This mathematical KEEP is separate from account/served-model/different-model admission gates, for which response-side evidence is unavailable here. No formal proof receipt is claimed.

NEXT: w464 independently check w463's exact full-simplex barrier and the source normalization; retain the ordinary-path and disjointness qualifiers in every recall card.
