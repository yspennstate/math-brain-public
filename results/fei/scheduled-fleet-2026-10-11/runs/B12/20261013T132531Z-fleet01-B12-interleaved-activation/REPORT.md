# B12 / A057 — disjoint interleaved activation is monotone

**Run:** `20261013T132531Z-fleet01-B12-interleaved-activation`  
**Primary packet:** A057 (Coherent restriction remainder)  
**Attempt:** `A057-INTERLEAVED-ACTIVATION-19`  
**Stable gap:** `B12-A057-COHERENT-HIERARCHY-v19`  
**Status:** new interleaved-activation theorem PROVED by contributor; full FEI OPEN.

## Previous exact status

The preceding run proved that, for one fixed disjoint activation pair,

`R_v=J_{a,b}(h_v)-E[J_{a,b}(h_child)|v]`

and paid the complete adaptive hierarchy for an arbitrary Boolean source at the one-bit selector interface. It left the inter-node mismatch from a changing activation pair unpaid.

## New mathematical movement

### 1. Sharp scalar kernel positivity — PROVED

For

`K(x,y)=psi(x)+psi(y)-[psi(x+y)+psi(x-y)]/2`,

whenever `|x|+|y|<=1`,

`0 <= K(x,y) <= psi(y)+3y^2`.

The lower bound follows by homogeneity and a one-variable entropy derivative. The upper bound is the convexity of `psi(t)+3t^2` on `[-1,1]`; the coefficient `3` is sharp as `x` tends to one and `y` tends to zero.

Consequently every physical Fourier-entropy split decrement of a Boolean function is coefficientwise nonnegative. The corresponding activation-channel upper envelope is derivative entropy plus three times activation influence.

### 2. Arbitrarily interleaved disjoint activation — PROVED

Let `W` be an activation block and `X` a disjoint Boolean source block. For

`F=a(W)+h(X)b(W)`, `a±b` Boolean,

consider any adaptive tree that may interleave queries from `W` and `X` and is complete on `X`. At each source query use the exact current biased remainder `R_v`. Then

`sum_{source nodes v} w_v R_v <= J(a,b;h)`.

More precisely,

`sum_source w_v R_v = J_root - sum_leaf w_l J_l - sum_activation w_v D_i(F_v)`.

Both subtracted terms are nonnegative. The key point is that at an activation query the average child activation energy equals the parent energy by Parseval, so the defect-potential decrement is exactly the physical split decrement `D_i(F_v)>=0`.

This covers arbitrary Boolean activation branches, arbitrary Boolean sources, any dimension, any adaptive interleaving, changing restricted activation weights, all bias paths, and all coherent collision ratios. It is not limited to an affine, threshold, or bounded-piece source.

### 3. Selector hierarchy with changing activation weight — PROVED

For the one-bit selector interface with arbitrary Boolean indicator `s` of mean `p`, the root potential is the scalar `Q(p)` from the preceding run. Hence every interleaving of the selector query and the source queries obeys

`sum_source w_v R_v <= Q(p) <= 8p ln2 <= 32 ln2 I(d)`

in nats, or constant `32` in bits. Querying the selector first can reduce the source-remainder sum to zero; querying source coordinates first can retain the full endpoint. There is no depth, address-count, or changing-weight loss.

The public fresh-selector composition theorem remains established and is not being presented as new. The present contribution is the exact monotonicity bridge that pays the campaign's complete biased remainder under arbitrary disjoint activation/source interleaving.

## Exact two-state mismatch formula

If one activation bit chooses child pairs `(a_+,b_+)` and `(a_-,b_-)`, write

`a=A+zC`, `b=B+zD`.

For a Boolean source of mean `mu`, the activation decrement is

`D_z(F)=sum_S K(A_S+mu B_S,C_S+mu D_S)+(1-mu^2) sum_S K(B_S,D_S)`.

Thus it depends on the source only through its mean and variance, not its full spectrum. Every term is nonnegative under Boolean realizability. This is the requested coefficientwise two-state activation calculation.

## Verification

`check_interleaved_activation.py` used no randomness and checked:

- 1,000,001 scalar boundary points for kernel positivity and the sharp coefficient-three envelope;
- 6,072 Boolean activation/source triples through two variables in each block;
- 11,616 activation-node split decrements;
- all adaptive next-coordinate choices for those triples by dynamic programming;
- 282 selector-source controls, including every Boolean source through three variables and selected rare/parity/half-space sources on four variables.

The minimum activation decrement was zero and the maximum adaptive source-remainder excess above the root defect was zero. All checks passed. The universal statements rest on the analytic proof, not finite extrapolation.

## Mandatory controls

- **Dummy cylinders:** their split decrement and remainder are exactly zero.
- **Parity-zero erasure:** no division by a singleton coefficient occurs.
- **Rare restrictions:** exact reach weights telescope; the selector reserve remains `O(p)`.
- **Whole-set addressing:** the tree may choose the next disjoint source or activation coordinate from the full prior transcript.
- **Near tensors and prime gates:** both activation branches and the source are arbitrary Boolean functions.
- **Changing bias/collision ratios:** the proof is exact and uses no Taylor expansion.
- **Changing activation weights:** allowed when caused by restriction of the disjoint block `W`.
- **Reused selectors/shared coordinates:** explicitly excluded and still open.

## Exact remaining universal gap

Stable gap `B12-A057-COHERENT-HIERARCHY-v19` is now:

> Pay a physical query that simultaneously changes the activation pair and the source. In this shared-coordinate case the four-channel crossed terms prevent the Parseval cancellation used here. A multi-query block identity must retain the source, crossed, and signed-remainder channels until a future-activation cancellation or a single terminal reserve becomes available.

The earlier `mu=O(alpha)` nonuniformity is no longer an obstruction for fixed or disjointly changing activation. It survives only inside the shared-coordinate coupling.

## Acceptance and review

- Complete biased remainder over fixed activation: **PROVED pending review**.
- Arbitrarily interleaved disjoint activation/source restrictions: **PROVED pending review**.
- Selector class with changing restricted activation weight: **PROVED pending review**.
- Shared-coordinate/reused-selector hierarchy: **OPEN**.
- Independent review: **none observed**; route to A091, then A090.
- Full FEI: **OPEN**.

## Next concrete action

Return to the exact shared four-channel decomposition from run `20261012T074154Z`. Form the two-query commuting square for two shared coordinates and retain `S_i+X_i+R_i^sh` as one block. Determine whether the crossed terms cancel after the second query or leave a signed boundary term controlled by derivative entropy plus the sharp `3 I` activation envelope proved here. Test first on the certified three-bit activation-irreducible falsifier and then exhaust all Boolean triples through dimension three.

## Configuration and delivery

Contributor proof and deterministic self-check only. No independent acceptance, native ingestion, merge, deployment, scheduler edit, new worker, protected source, held reroute, public release, email, or paid resource was used. The exposed runtime did not provide model or reasoning-effort telemetry. Delivery/readback is recorded separately and does not imply mathematical review.

