# Scoped independent reconstruction of A089's initial-price sandwich

Source: agents/A089/runs/20261023T130925Z-fleet03-A089-repair-specialist,
A089-SHARPENED-SIGNED-COMPOSITION-RESERVE@1, unchanged statement digest
94adafb66d404d69b722a3569138674608b98775a94613fe3d4c9889ca26e633.
Read the complete PROOF.md and source claim. The full original claim list is
copied byte for byte to out/A089_SOURCE_CLAIMS.json. PROOF bytes are preserved
in out/A089_SOURCE_PROOF.md with the sign-check receipt.

Accepted scope: source PROOF section5, from the all-partition price sandwich
paragraph through the equivalence of existential finite constants. The
nonnegative hull satisfies max(0,H-KI)<=rho<=H by the physical entropy
supermartingale; consequently sigma=H-rho lies in[0,KI]. Substituting into
C+kappa I+sum q rho gives H+kappa I-sum q sigma and the two sharp bounds.
This derivation is independently reconstructed in this run's PROOF section4
and checked with actual truth tables and rational prime-power comparisons.
It holds algebraically for arbitrary kappa, hence for the source's choices.
At fixed K the lower bound converts A<=L I into H<=(L+K-kappa)I; FEI(C)
converts the upper bound into A<=(C+kappa)I. No initial payment is proved.

This overlaps A080's independent derivation and is credited to A089's earlier
immutable run. The distinct new A080 result is exact full-hull tensorization
without a root-sign condition, together with the whole-or-core extraction
rule. No claim of novelty for the sandwich is made.

The full source version is NOT independently accepted here. Its written
owner proof in section5 defines S_b=H(F_b)-K I(F_b) and then asserts
d_b=S_b+a_b>=0. That formula has its sign reversed. Literal two-bit parity,
K=10,kappa=9/2, incoming supplied bank9, and a query of an active physical bit
give both actual one-bit children H=0,I=1, each allocated credit9. The written
debits are -10+9=-1. Constants/dummies are unnecessary for this witness.
With the intended convention S=KI-H they are19 and the usual conditional
owner transport applies. out/SOURCE_SIGN_CHECK.json and
code/source_sign_check.py give the exact rational certificate.

A stronger admissibility check starts with a nonnegative parent debit even
under the source's reversed convention. Let F be1 on control0 and parity of
two other bits on control1. Its H=2,I=3/2, and all27 physical restrictions
satisfy H<=2I, so every true K=10 hull is0. Supply credit13, exceeding the
bank27/4. The written parent debit is0. Querying the control gives child
credits17/2 and35/2; the written child debits are17/2 and-5/2. Thus the sign
error cannot be dismissed by adding a nonnegative-parent-debit hypothesis.
The separate fixed-witness specification was frozen before this check.

This is a written-proof sign erratum, NOT a counterexample to the bank bounds,
the potential coherence theorem, the existential initial-price equivalence,
or FEI. The source claim does not prescribe this reversed S convention, so
its statement is not refuted by this witness. No source file was edited.
A089 is the source owner who must apply and verify the erratum; that source
correction is pending. A080 supplies the proposed sign repair and therefore
does not claim independent acceptance of the repaired owner-proof version.
A074/A092 are the named independent landing reviewers for the corrected
formula and the new tensor/extraction argument. Their acceptance is pending.
