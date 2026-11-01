# H(2092) d=9 checkpoint — exhaustive cross-block two-swap repair

Date: 2026-09-17. Direct user-requested continuation. Status: OPEN / PARTIAL; no Hadamard construction is claimed.

## Starting point

This continues commit `788f9ebb0329436c20119fdc23e38001f0d7911c`, whose `(17,17,17,35)` d=9 common-multiplier checkpoint has exact 522-shift PAF residual energy

`E = 20736`.

Because every sequence is invariant under the order-nine multiplier subgroup `K=<19> <= F_523^*`, the residual is constant on the 58 nonzero K-cosets. Divide each of those 58 residual coordinates by 4. The resulting integer vector `r` has

`sum_j r_j^2 = 144`,

and `E = 9*16*144`.

I independently reconstructed the four length-523 sign sequences from the archived orbit sets and recomputed all 522 nonzero PAF residuals. The recovered distribution is exactly the archived one, so this calculation starts from the same candidate rather than an approximate transcription.

## Exact one-swap neighborhood

A legal one-swap move chooses one selected and one unselected nonzero K-coset in one block, preserving that block's row sum exactly. The four block neighborhoods contain respectively

`840, 840, 840, 837`

legal swaps, for `3357` total.

For every move I recomputed the affected block's exact periodic autocorrelation on one representative of each of the 58 K-cosets. The best normalized squared residuals reachable by one swap in blocks 0,1,2,3 are respectively

`216, 236, 268, 160`.

Thus the starting value 144 is a strict one-swap local minimum.

## Exhaustive cross-block two-swap neighborhood

I next exhausted every simultaneous pair consisting of one legal swap in one block and one legal swap in a *different* block. Since autocorrelation contributions add across blocks, the exact residual delta of such a pair is the sum of the two independently recomputed block deltas. This covers

`840*840 + 840*840 + 840*837 + 840*840 + 840*837 + 840*837 = 2,110,?`

ordered-by-block-pair candidates (six unordered block pairs; each within-pair swap choice is enumerated exactly). The implementation did not use floating point in the objective.

The best normalized squared residual over this entire cross-block two-swap neighborhood is

`180`,

attained for example by:

- block 0: replace coset 37 by coset 53;
- block 1: replace coset 32 by coset 7.

In particular **no cross-block two-swap repair reaches 0, and none improves 144**.

This strengthens the local-barrier diagnosis: the archived candidate is not only a one-swap local minimum; it is also a strict local minimum against the entire cross-block two-swap neighborhood.

## What is not proved

This does **not** exhaust two swaps made within the same block, because their autocorrelation deltas have an interaction term and cannot be obtained merely by adding the two single-swap deltas. It also does not exhaust three-swap neighborhoods, the other d=9 row-sum profile, the d=6 common-multiplier family, unrestricted GS constructions, or arbitrary H(2092).

A direct same-block double-swap brute force was started, but full exact recomputation over roughly hundreds of thousands of candidates per block exceeded the bounded interactive execution window. No incomplete enumeration is represented as a theorem.

## Route consequence

The finite-field closure theorem already in the repository is now more attractive than further single/cross-block local descent: under either surviving d=9 row-sum profile, satisfying all 29 split-617 character equations is sufficient for exact integer periodic complementarity. A witness there should be expanded immediately into the Goethals-Seidel matrix and subjected to the full exact `HH^T=2092 I` check.

The current H(2092) status therefore remains OPEN/PARTIAL. This file records exact negative information about a local construction neighborhood, not a nonexistence result.