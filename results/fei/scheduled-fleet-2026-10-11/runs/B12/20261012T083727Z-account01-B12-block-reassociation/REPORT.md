# B12 / A057 — block channelization and reassociation transfer

Run ID: `20261012T083727Z-account01-B12-block-reassociation`  
Primary packet: **A057 — Coherent restriction remainder**  
Attempt: `B12-A057-ATTEMPT-08`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v8`  
Status: **SUBSTANTIVE MATHEMATICAL MOVEMENT; FULL FEI OPEN**

## Outcome first

This run proves the promised multi-query extension of the shared-coordinate
four-channel identity.  For every physical block `B`, the genuine product
`F=a+hb` has one block-source channel and `2^|B|-1` nonzero selector-frequency
channels.  Their exact entropy ledger is

`D_B(F)=S_B+sum_{alpha!=0} X_{B,alpha}+qD_B(h)+R_B^sh`.

The block identity contains every signed coherent collision and has no
disjointness, orthogonality, bias-floor, or collision-separation hypothesis.
For a singleton block it is exactly the preceding one-query theorem.

The main new structural fact is an exact **reassociation transfer**.  The
complete entropy decrement is invariant under sequential query order, but
the source/crossed and child/remainder ledgers are not.  For each query order
`pi`, an exact signed term `T_pi` moves between them:

`L_pi=L_B+T_pi`, `M_pi=M_B-T_pi`, and `D_B(F)=L_pi+M_pi=L_B+M_B`.

A two-bit activation-irreducible Boolean witness has

`T_(0,1)=-2 ln2+(9/8)ln3<0`, while `T_(1,0)=0`.

Thus the hoped-for termwise cancellation of internal source/crossed channels
is false.  What telescopes is the complete block decrement; channel labels
reassociate in an order-dependent way.  This is not an FEI counterexample.

## Frozen objective and prior status

The previous run proved the exact one-query four-channel law and refuted the
attempt to pay its signed remainder separately by the installed one-node
Bellman potential.  Its required next action was to expand two consecutive
shared queries and determine whether internal source/crossed channels cancel
under coherent conditioning.

Previous tracked value: exact one-query identity, no multi-query closure, and
the specific remainder-only Bellman continuation false.

Bounded objective: construct the exact two-query/block ledger, identify any
internal cancellation, and certify a smallest genuine Boolean control.

## Exact block theorem — PROVED

Write, relative to a block `B`,

`a=sum_gamma chi_gamma a_gamma`, and similarly for `b,h`.

Physical multiplication gives the exact convolution

`F_gamma=a_gamma+sum_alpha h_alpha b_(gamma xor alpha)`.

Separate the zero selector frequency:

`A_gamma=a_gamma+h_0 b_gamma`,

`C^alpha_gamma=h_alpha b_(gamma xor alpha)` for `alpha!=0`.

Set `S_B=D_B(A)`, `X_{B,alpha}=D_B(C^alpha)`, and define the polarized
interaction and signed remainder by subtraction.  Then

`D_B(F)=S_B+sum X_{B,alpha}+qD_B(h)+R_B^sh`

exactly.  The detailed definitions and proof are in
`BLOCK_REASSOCIATION.tex`.  This is a physical-product convolution theorem;
it does not invoke the killed `RAW_CONV_TENSOR` or `OVERLAP_PRODUCT` claims.

## Exact reassociation theorem — PROVED

For an ordering `pi=(i_1,...,i_m)` of `B`, sum the local one-coordinate
four-channel identities over the induced restriction tree with the actual
weights `2^{-(t-1)}`.  Let `L_pi` be the weighted source-plus-crossed sum and
`M_pi` the weighted child-plus-remainder sum.  Let `L_B,M_B` be the analogous
simultaneous block split.  Then

`T_pi:=L_pi-L_B`, `M_pi=M_B-T_pi`.

This follows from the exact entropy tower

`D_B(f)=sum_nodes weight(node) D_query(node)(f_node)`.

The transfer is not assumed positive and is not an additional cost.  It is
the exact bookkeeping difference between two valid groupings.

## Small genuine Boolean witness

In zero-based lexicographic order take

```text
g+ = (-1,-1,-1,-1)
g- = (-1,-1, 1, 1)
h  = (-1,-1,-1, 1)
F  = (-1,-1, 1,-1)
```

The branches disagree at `[2,3]`, where `h` has signs `[-1,+1]`; both
branches are physically used on disagreement points.

For the full two-coordinate block:

- `S_B=(9/4)ln2-(9/8)ln3`;
- each of the three selector-frequency channels is `(1/4)ln2`;
- `D_B(h)=2ln2`, `q=1/2`;
- `R_B^sh=tau=-2ln2+(9/8)ln3`;
- `D_B(F)=2ln2`.

The sign certificate is `tau=(1/8)ln(3^9/2^16)<0`, since
`19683<65536`.

For query order `(0,1)`, the sequential source/crossed ledger is `ln2` and
the sequential remainder is zero, so `T_(0,1)=tau`.  For `(1,0)`, the
sequential source/crossed ledger equals the block ledger and the sequential
remainder is `tau`, so `T_(1,0)=0`.  The total is `2ln2` both ways.

## Exact finite verification

Command:

```bash
python3 check_block_reassociation.py
```

The checker uses exact `Fraction` Walsh coefficients and exact rational
coefficients of prime logarithms.  It exhaustively evaluates all `4096`
Boolean triples on two bits and both query orders.  Results:

- `2688` triples have nonzero reassociation transfer;
- `1792` have order-dependent transfer;
- `960` order-dependent triples use both selector signs on a nonempty
  disagreement support.

It also verifies every exact term and the integer sign certificate for the
displayed witness.  There is no random search and no seed.  Enumeration
checks the implementation; both identities and the witness calculation are
proved algebraically in the theorem artifact.

## Movement and remaining obstruction

The previous open phrase “make the internal S/X channels cancel” is now
resolved negatively at its exact scope.  They do not cancel termwise under
sequential conditioning.  Instead they exchange the signed transfer `T_pi`
with the remainder ledger.

This sharpens the universal gap:

> Pay the order-independent aggregate block ledger without separately
> enveloping its `2^|B|-1` selector-frequency channels, or construct a
> posterior/future-activation gauge whose reassociation transfer telescopes
> across adjacent blocks.

The exponential channel count is an algebraic warning, not a lower bound:
it shows why a channel-by-channel envelope cannot yet yield a
dimension-independent constant.  The complete changing coherent remainder,
activation witness, and one-budget hierarchy payment remain open.

## Controls and acceptance

- **Actual Boolean realizability:** all theorems apply to genuine Boolean
  triples; the witness is a genuine two-bit table.
- **Activation equivalence:** both selector signs occur on disagreement.
- **Rare-event logarithms:** prime-log coefficients are retained exactly.
- **Constant-output gauge:** the earlier constant-output witness remains a
  valid control; the new theorem does not replace it with a nonnegative
  output-only term.
- **Addressing, sparse defects, near tensors:** no universal payment is
  inferred from the block identity, so these controls remain obligations for
  the future aggregate bound.
- **A057-D1:** **ADVANCED** from one shared query to arbitrary finite blocks.
- **A057-D2:** exact order, activation, sign, and convolution controls added.
- **Packet complete:** **NO**; no dimension-free aggregate payment.
- **Independent review:** **PENDING** for both new claims.
- **Full FEI:** **OPEN**.

## Next bounded action

Do not split into all `2^m-1` channels and bound each separately.  For two
adjacent blocks, express `T_pi` directly as a conditional mutual-information
or KL-type associator of the normalized spectral mixtures.  Test whether
the associator satisfies a cocycle identity under three query orders and can
be charged once to terminal reserve.  A positive result would compress
reassociation without exponential channel loss; a negative exact Boolean
witness would retire that mechanism.

## Source, review, and execution status

The owner overlay, current B12 compact contract, current status and
obstruction registry were re-used at the immutable blobs recorded in
`SOURCE_PINS.md`.  Comparing the preceding B12 final commits to the current
repository heads showed no intervening B12 or campaign-control correction;
only other streams and Brain inbox metadata changed.

Observed model metadata: `gpt-5` family Codex agent; no explicit scheduler
effort selector was exposed.  Natural execution and local exact verification
are recorded.  Independent review and downstream native Brain ingestion were
not observed.
