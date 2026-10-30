# B17 / A082 — all-arity structural bridge for the block half-tax

**Verdict:** the dimension/arity tail of the block half-tax is closed.  The
result is an all-finite-arity uncertainty lemma, not universal GU; full FEI
remains open.

## Frozen target

- Primary packet: **A082 (finite inequalities / exhaustiveness lemma)**.
- Stable gap: `FEI-GAP-HALF-TAX-ARITY-BRIDGE`.
- Attempt: `A082-SCHWONNEK-ADDITIVITY-1`.
- Claim: `B17-A082-ALL-ARITY-HALF-TAX-v1`.
- Prior bound: the repaired scalar/two-parameter certificate gave the local
  coefficient `1/2`, but no theorem in the B17 chain made a finite
  two-variable certificate exhaustive over block arity.

For `Delta(p)=h2(p)+log2(max(p,1-p))`, freeze the source local inequality

\[
H(|z|^2)+H(|U_pz|^2)\ge h_2(p)-\tfrac12\Delta(p)
\]

for every unit qubit state `z`.  The question is whether tensoring the
physical block permits an entangled coefficient vector to beat the sum of
these local constants.

## Theorem

For every finite block `A`, every product-bias vector
`(p_i) in [0,1]^A`, and every unit vector `w` in `C^(2^|A|)`,

\[
\boxed{
H(|w|^2)+H(|(\otimes_{i\in A}U_{p_i})w|^2)
\ge \sum_{i\in A}\left(h_2(p_i)-\tfrac12\Delta(p_i)\right).}
\]

The constant is independent of arity and the state may be complex and
entangled.  Therefore the exact block reduction gives

\[
\boxed{J_A\le M_A+\tfrac12\sum_{i\in A}\Delta(p_i)}
\]

for every finite product-biased block and every normalized child family,
hence for every genuine Boolean application.

## Proof and coverage

The computational basis and the `U_p`-rotated basis are two nondegenerate
projective measurements on one qubit.  Schwonnek's Proposition 1 proves
additivity of the optimal linear Shannon-entropy uncertainty constant for
two product projective measurements, including arbitrary entangled states;
Corollary 1 iterates it to every finite number of parties.  Taking weights
`(1,1)` and the local constants from the repaired scalar theorem gives the
displayed bound immediately.

This is a structural reduction, not an inference from finite maxima.
There is no omitted large dimension: the quantifier is every finite `A`.
Biases `p_i=0` or `1` contribute a signed-permutation factor and zero to the
right side, so they are deleted exactly.  The balanced endpoint `p_i=1/2`
is included.  Zero probabilities use the continuous `0 log 0=0`
convention.  No Boolean spectral law was substituted for an arbitrary law;
the uncertainty theorem is stronger than required and is only applied back
to genuine Boolean children through the exact block identity.

The primary external source was read at its theorem statement, not merely
cited from a summary: R. Schwonnek, *Additivity of entropic uncertainty
relations*, Quantum 2 (2018), 59, DOI `10.22331/q-2018-03-30-59`,
Proposition 1 and Corollary 1; arXiv `1801.04602v4`.

## GU implication and remaining unpaid line

This theorem removes the higher-arity/compactness premise from the
uncertainty step.  In any exact GU hierarchy ledger, every occurrence of
`J_A` can now be replaced uniformly by
`M_A + (1/2) sum_i Delta(p_i)`, with no hidden dimension constant.
Universal GU would follow only after a separate signed hierarchy estimate
that retains and pays all surviving `M_A` boundary/terminal terms and
charges the half-taxes with single-use physical influence.  The accepted
OR-defect family rules out setting those `M_A` terms to zero or cancelling
them blindly.  Thus the first unsupported line is now exactly the terminal
`M` reserve, not block arity.

No claim is made that this proves `G<=aI+bU`; it is one exact restricted
lemma needed by such a proof.  Independent end-to-end review is pending.

## Validation

`verify_all_arity_additivity.py` tested 4,750 deterministic random complex
states through arity eight, including deterministic, rare, balanced, and
reflected biases.  It found no violation; the smallest observed formula
margin was `0.028202984492943672`.  Product-state tests reproduced the sum
of independently minimized local entropies to `8.882e-16`.  These floating
tests are diagnostics only; the proof is the theorem transfer above.

## Next action

Derive the first three-bit/shared-core hierarchy identity with every
terminal `M_A` term explicit, then test a signed potential that pays it once.
Reviewers A090/A094 should independently verify the mapping from the block
Fourier rotation to Schwonnek's two global product measurements.

Model/effort: `UNKNOWN`.

