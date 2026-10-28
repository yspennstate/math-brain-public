# Author audit; not independent acceptance

1. Reconstructed the affine fallback from the literal point-defect spectrum:
   empty amplitude 1-u, all others magnitude u. There are 2^(D-1)-1 nonempty
   pairs, each contributing 2u^2; their sum is 2u(1-u). Character translation
   preserves conditional spectral entropy but may complement coordinate
   influence. Using u(1-u)=d(1-d) is essential; ordinary influence invariance
   under character multiplication would be false.
2. Reconstructed the quadratic pivot from actual physical edges: a nonconstant
   linear derivative is balanced, and one flipped vertex changes one edge out
   of 2^(D-1). The D<=2 cases are handled separately; the D>=3 lower bound is
   not applied at D=2. A zero-influence selected coordinate has zero erasure.
3. Exhaustion checks all 18032 normalized descriptions, not all Boolean
   functions. Removing only the constant coefficient is justified by global
   sign invariance. All coordinate restrictions were checked against literal
   truth-table restriction, not inferred from the polynomial implementation.
   Independent character sums on 16 fixtures check the Walsh convention.
   This second implementation is author verification, not independent review.
4. The binary activation check uses FULL physical spectra, including both child
   spectra and constants. The multi-input follow-up computes full OR truth
   tables; it does not merely re-evaluate the claimed transport formula.
   Specified prefix debits are retained. Added bad-node debit is zero; old
   prefix bad bills are not claimed bounded or forgiven.
5. Reordering the continuation invalidates reuse of the old fixed-tree Phi
   drift identity. We deliberately assert only the actual bad-node bill and
   full entropy/influence telescopes for the new tree. This is a policy repair
   on a hereditary class, not the missing universal net-price theorem.
6. The fan-in extension groups independent OTHER inner blocks into h. It uses
   no goodness assumption on h. The product formula for its negative mean
   uses physical disjointness. An arbitrary outer gate is not covered.
7. Written estimates include mean zero, mean +/-1, D=0, D=1 and constants;
   strict numerical relaxations are asserted only for positive influence.
   Corrected an initially strict displayed relaxation at constant functions
   before finalizing the report; the checkers already used non-strict signs.
8. No formal certificate is claimed. Current available memory was 2076 MB,
   below the serialized Lean launch floor 5500 MB; no compiler was requested.
   No process was stopped or left running. The largest enumeration completed
   in 38.34 seconds and uses only <=4-bit individual functions.
9. Fresh source reading was protocol, BOARD, B05 stream notes, own STATUS,
   prior claim/derivation/helper. Earlier source-paper and registry intake is
   inherited explicitly, not represented as a new full-paper audit.
10. No numerical failure was encountered. One patch with a nonexistent context
    line was rejected before changing files; its corrected patch succeeded.
    A UTF8 hook rejected a read command despite explicit encoding; the same
    read succeeded after acknowledging that all text reads use UTF8. No
    permission escalation or source mutation occurred.

First unsupported universal step: extend the affine single-point spectral
bound to a general edit set while preserving a good physical continuation
after restrictions. Taking a constant base phase includes every Boolean
function, so that extension cannot be treated as a routine corollary.
