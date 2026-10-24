# B12 / A057 — exact shared-coordinate four-channel law

Run ID: `20261012T074154Z-account01-B12-shared-four-channel`  
Primary packet: **A057 — Coherent restriction remainder**  
Attempt: `B12-A057-ATTEMPT-07`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v7`  
Status: **SUBSTANTIVE MATHEMATICAL MOVEMENT; FULL FEI OPEN**

## Outcome first

This run derives an exact entropy-decrement identity for a physical coordinate
shared simultaneously by the Boolean source pair and Boolean selector.  It
splits the decrement into four signed channels:

`D_i(F)=S_i+X_i+q D_i(h)+R_i^sh`.

Here `S_i` is the source channel, `X_i` is the crossed channel created by the
simultaneous source/selector derivative, and `R_i^sh` is an exact polarized
interaction minus the physical child decrement.  The identity has no
disjointness, orthogonality, bias-floor, or collision-separation hypothesis.
It reduces exactly to the previously proved biased remainder `R_mu(alpha)` on
a disjoint child query, gives zero remainder on a source-only query, and
restores the cancellation on constant outputs that every nonnegative
output-only repair had lost.

The natural Bellman continuation nevertheless fails.  A new genuine
activation-irreducible three-bit example proves

`R_i^sh > -1/32 > Delta_i{C_* q I(h)+Var(h) E_raw(b)}`,

where `C_*=4+2 ln 2+2/e`.  Thus the exact signed remainder cannot be paid
separately by the old potential.  The source and crossed channels must remain
coupled to it across a block.  This is a rigorous obstruction to an auxiliary
composition mechanism, not an FEI counterexample.

## Frozen objective and prior status

The preceding run showed that the old two-term potential could increase under
a shared query, even for constant output, and that output-only local repairs
cannot see the defect.  Its next action was to retain the exact signed shared
remainder before applying a nonnegative envelope and determine whether the
gauge covariance cancels algebraically.

Previous tracked value: the disjoint changing-witness theorem was proved, but
the shared-coordinate step had only the covariance formula and negative
potential examples.  No exact extension of `R_mu(alpha)` to simultaneous
source/child restriction was available.

Bounded objective for this run: derive that exact extension, verify all
boundary cases, and decide the specific candidate inequality

`R_i^sh <= Delta_i P_*`, `P_*=C_* q I(h)+Var(h)E_raw(b)`.

## Exact theorem — PROVED

Write

`a=a0+x_i a1`, `b=b0+x_i b1`, `h=r+x_i s`

and define

`A=a0+r b0`, `B=a1+r b1`, `C=s b1`, `D=s b0`.

Then `F=a+hb=(A+C)+x_i(B+D)`.  For arbitrary functions on the remaining
cube set

`mathfrakD(p,q)=Eraw(p)+Eraw(q)-[Eraw(p+q)+Eraw(p-q)]/2`.

Define

`S_i=mathfrakD(A,B)`, `X_i=mathfrakD(C,D)`,

`Omega_i=mathfrakD(A+C,B+D)-S_i-X_i`,

`R_i^sh=Omega_i-q mathfrakD(r,s)`, with `q=||b||_2^2`.

Then, for every Boolean triple on every finite cube and every shared physical
coordinate,

`D_i(F)=S_i+X_i+qD_i(h)+R_i^sh`.

The proof is in `SHARED_FOUR_CHANNEL.tex`.  Products are physical products;
their Fourier transforms are the genuine signed convolutions, so no false
overlapping tensor rule appears.

### Boundary controls

- **Disjoint child query:** `a1=b1=0`, hence `S_i=X_i=0` and
  `R_i^sh=D_i(F)-qD_i(h)=R_mu(alpha)`, including `-qK(mu,alpha)`.
- **Source-only query:** `s=0`, hence `R_i^sh=0`; the full decrement is the
  source channel.
- **Constant output:** the four channels sum exactly to zero.  On the prior
  activation-irreducible witness their values in nats are approximately
  `0.2375964`, `0.1732868`, `0.625*0.8435027`, and `-0.9380724`.
- **Shared convolution:** no raw-convolution tensor additivity is used.

## Installed Bellman candidate — REFUTED

Take, in zero-based lexicographic order,

```text
g+ = (-1,-1, 1, 1,-1,-1, 1,-1)
g- = (-1,-1,-1, 1,-1,-1,-1,-1)
h  = (-1,-1, 1,-1,-1, 1,-1, 1)
```

and query coordinate `i=1`.  The disagreement support is exactly `[2,6]`,
and the selector signs there are `+1,-1`, so both branches are actually used
where they differ.

Exact Walsh arithmetic gives

`R_i^sh=-(11/4)ln2+(25/32)ln5+(9/16)ln3`

and

`Delta(qI)=-1/16`, `Delta(VZ)=(7/16)ln2`.

For `C_*=4+2ln2+2/e`, therefore,

`Delta P_*=-1/4-1/(8e)+(5/16)ln2`.

The exact certificates

`163*5^25*3^18 > 60*2^88`, `e>163/60`, and `ln2<7/10`

imply

`R_i^sh > -1/32 > Delta P_*`.

Numerically the gap is `0.048564471146550399...` nats.  The candidate fails
at one shared physical step.  This does not refute a different blockwise
potential, a future-activation gauge, or full FEI.

## Verification

Command:

```bash
python3 check_signed_shared_remainder.py
```

The checker uses exact `Fraction` Walsh coefficients and exact rational
coefficients of prime logarithms.  It:

- exhaustively verifies the four-channel identity for all Boolean triples and
  all queried coordinates through dimension two (`8,256` cases);
- verifies a disjoint child-query reduction;
- reconstructs the preceding constant-output cancellation;
- verifies every exact value in the new activation-irreducible falsifier;
- checks the integer and exponential-series sign certificates.

There is no random search in the archived checker and no seed.  The separate
discovery exploration used deterministic seed `20261012`; it is not relied on
for the proof.

## Case extension and controls

- **Starting class:** disjoint source/child coordinates with exact
  `R_mu(alpha)`, plus a two-term potential for interleaved disjoint
  restrictions.
- **New class:** every one-step shared-coordinate Boolean composition, with
  arbitrary coherent convolution on the remaining coordinates.
- **New constant:** identity is exact, so no dimension/overlap/bias constant;
  the specific installed Bellman coefficient is rigorously false.
- **Activation equivalence:** both branches are used on the falsifier's
  disagreement support.
- **Rare-event logarithms:** all prime-log terms are retained exactly.
- **OVERLAP_PRODUCT:** respected; physical products become signed
  convolutions and no disjoint additivity is asserted.
- **RAW_CONV_TENSOR:** respected; `Eraw` is used only inside exact kernel
  identities.
- **Near tensors/addressing/prime gates:** the theorem is exact at one shared
  step, but no universal sum is inferred; the falsifier is an actual Boolean
  prime table rather than a weighted relaxation.

## Acceptance and remaining gap

- A057-D1: **ADVANCED**.  The exact coherent remainder is now defined and
  proved for an arbitrary shared query, strictly beyond the disjoint theorem.
- A057-D2: prior balanced, biased, near-collision, parity and hierarchy
  controls remain intact.
- Complete A057 acceptance: **NOT MET**.  There is still no depth-uniform
  payment of the coupled `S_i+X_i+R_i^sh` ledger across an adaptive overlap
  hierarchy.
- Independent review: **PENDING** for both new claims.
- Full FEI: **OPEN**.

The precise surviving gap is now smaller and representation-aware:

> Sum the coupled block charge `S_i+X_i+R_i^sh` over an actual future-
> activation physical hierarchy, without separating the interaction from the
> two channels or recharging a terminal subtree.  Equivalently, find a
> blockwise gauge in which the four-channel cancellation telescopes.

The next bounded attempt should use two consecutive shared queries.  Expand
the eight resulting channel terms and test whether the internal `S/X`
channels cancel after conditioning on future activation.  A one-node
envelope for `R_i^sh` is now retired.

## Source and review status

Current control sources read in this run include the owner overlay
`ORDER.md`/`CASE_TARGETS.json`, current B12 compact contract, current status,
and obstruction registry at the source heads recorded in `SOURCE_PINS.md`.
The exact predecessor proofs are the immutable B12 biased-kernel,
changing-witness, shared-covariance and constant-output runs listed there.

Observed model metadata: `gpt-5` family Codex agent; an explicit scheduler
effort selector was not exposed.  Natural execution and local exact
verification are recorded; independent review and downstream native adoption
were not observed.
