# B13 addendum — fresh lower-bound correction and complementary handoff

This addendum preserves the immutable `REPORT.md` and records two post-write updates from fresh peer reads at the same scientific frontier.

## 1. Minor cross-reference correction

In `REPORT.md` Section 2, the sentence saying “Section 6 below shows rigorously that this constant cannot simply be inserted as a uniform bound on `MI_A`” should point to **Section 8**, not Section 6. No formula or conclusion changes.

## 2. Freshest balanced lower bound

After the report write, I read account02/B17's complete `20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`. It gives a balanced 162-bit shared-core graft with

`H/(I-1) > 6.521850083658612443633672199029299526203969333...`,

sharper than the `6.521845710923046575...` value quoted in B13 Section 6.

Therefore the forced lower bound on B13's within-scale residual improves from the report's `0.079150670034083...` to

`C_within/I > 6.5218500836586124436... - (5+log2(e))`

`            > 0.079155042769648...`

for that balanced construction. Full FEI remains open; this is only a lower stress value for the new residual.

## 3. Complementary scope after fresh B14--B18 reads

The new B13 object

`C_within = sum_A int_0^1 (1-s)^|A| E_A'(s) I_{A,s} ds`

is distinct from the neighboring active routes and gives them a concrete target rather than duplicating their work.

- **B14 (restriction selector):** its latest non-read-once top-flip witness keeps the existential restriction ratio near the width-two-tribes benchmark. It is a natural finite test of whether large restriction decrement corresponds to small or large B13 fixed-scale residual; B13 does not re-search selector witnesses.
- **B15 (packet arithmetic):** its punctured-majority family proves packet-local free-energy payment can fail logarithmically while global influence grows on the `sqrt(n)` scale. This is fully compatible with B13's majority obstruction to prefix-local `MI_A` bounds and reinforces the same conclusion: the payment must be global/cross-component. B13 does not re-prove packet arithmetic.
- **B16 (shared-variable coherent product ledger):** B16 retains signed coherent transport, XOR multiplicity, KL refund and physical-overlap corrections. B13's fixed-scale conditional law (a normalized noised higher-derivative spectrum) is a plausible input object for that ledger if a genuine shared-product representation can be found. No such representation is claimed here.
- **B17 (balanced support-deficit equivalence):** its new balanced lower bound supplies the corrected residual stress number above. Its Bellman/support-deficit route is FEI-complete already; B13 instead isolates one component of the random-chain branch term.
- **B18 (product-phase total-correlation stability):** B18 identifies a Hellinger-scale Boolean phase stability bound and an outstanding KL-scale phase-discrepancy problem. B13's `I_{A,s}` is itself a KL/mutual-information quantity. A successful bridge would need B18-type phase constraints uniformly across the beta/noise scale, with bounded overlap in `A`; merely inserting B18's existing Hellinger bound is not enough.

This coordination suggests the next B13 step precisely: try to express the **integrated** fixed-scale branch mutual information as a KL/total-correlation charge to which the B18 phase constraints or the B16 signed-coherence ledger can be applied with bounded ancestor multiplicity. Majority and the one-point defect remain mandatory stress tests.
