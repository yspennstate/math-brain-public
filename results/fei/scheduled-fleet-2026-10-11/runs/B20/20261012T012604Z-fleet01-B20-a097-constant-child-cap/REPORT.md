# B20 / A097 — sharp constant-child cap for critical FEI sources

**Run:** `20261012T012604Z-fleet01-B20-a097-constant-child-cap`  
**Primary packet:** A097 (Cross-route transfer)  
**Attempt:** `A097-CONSTANT-CHILD-TRANSFER-1`  
**Claim:** `B20-A097-CONSTANT-CHILD-CRITICAL-CAP-v1`  
**Gap:** `G-CRITICAL-STEP`  
**Status:** exact transfer proved; sharp source optimization and this transfer
await independent reconstruction. **Full FEI remains OPEN.**

## 1. Exact movement

Let `f` be a nonconstant genuine Boolean function on a finite uniform cube.
Call it restriction-critical if every nonconstant physical restriction `g`
has `H(g)/I(g) <= H(f)/I(f)`.

This run proves:

> If a restriction-critical `f` has a relevant coordinate with one constant
> physical child, then
> `H(f)/I(f) <= C_* < 4.872322`, where `C_*` is the sharp constant-branch
> selector tax from `B12-A060-SELECTOR-TAX-SHARPNESS-v2`.

Consequently, every restriction-critical source with ratio at least
`4.872322` has **two nonconstant children at every relevant coordinate**.
After the B01/B20 critical-prime descent, any hypothetical source above this
threshold may therefore be assumed tensor-prime and free of constant
codimension-one faces.

This is a proper structural restriction on near-extremizers. It neither gives
a dimension-independent bound on the surviving class nor proves full FEI.

## 2. Substitution with all constants

At the selected coordinate, multiply by the constant child sign and relabel
the selector so that

```text
K(+1,z)=1,   K(-1,z)=D(z).
```

Put `p=Pr[D=-1]`. The scalar packet formula, independently accepted by
B19/A094 at this scope, and the B12 sharp optimization give

```text
H(K) = H(D)/2 + p c(p),
I(K) = I(D)/2 + p,
c(p) <= C_*,
4.872321 < C_* < 4.872322.
```

The exact expression for `c(p)` and the one-variable derivative proof are in
`CROSS_ROUTE_SUBSTITUTION.tex`. No entropy, influence, selector probability,
normalizer, or child term is dropped.

Let `R=H(K)/I(K)`. Restriction-criticality gives `H(D)<=R I(D)` when `D` is
nonconstant. Therefore

```text
R(I(D)/2+p) = H(D)/2+p c(p)
             <= R I(D)/2+C_*p.
```

Because `p>0`, cancellation yields `R<=C_*`. If both children are constant,
relevance makes `K` a signed dictator and `H(K)=0`, so the conclusion still
holds.

The debt paid is exact: the A096 existential-coordinate problem is closed on
the entire constant-child stratum. The remaining stratum has two nonconstant
children at every relevant coordinate.

## 3. Why this is a genuine cross-route transfer

- **B05/B19 route:** supplies the complete arbitrary-Boolean-child packet
  against a constant, including the child entropy and phase contribution.
- **B12 route:** optimizes that exact packet over the physical bias and proves
  the sharp finite coefficient `C_*`.
- **B20/B01 route:** supplies restriction-criticality and the critical-prime
  normal form.

The result does not replace the target residual by FEI. It applies a scalar
proved identity and a one-variable proved bound to the exact critical-child
inequality. `TRANSFER_HYPOTHESIS_CHECK.json` records every matched and
unmatched hypothesis.

## 4. Counterexample and endpoint audit

- **Rare activation / sparse defects:** every fresh activation control has a
  constant inactive child. It cannot itself be a critical endpoint above
  `C_*`; the active child's full ratio is retained.
- **Addressing:** generally has two nonconstant children and survives. No
  address label is charged coordinatewise.
- **Bent selector:** generally has two nonconstant children and survives. The
  theorem does not assert a selector-only entropy payment.
- **Near tensors:** only constant-face surgeries are excluded. Arbitrary-core
  embeddings with two nonconstant faces remain live.
- **Shared variables:** no product, independence, or fresh-copy identity is
  used beyond the actual physical restriction coordinate.
- **Parity-zero erasure:** no erasure functional appears.
- **Actual prime gates:** the conclusion applies verbatim when a prime gate
  has a constant face; primitivity alone remains insufficient.
- **Endpoints:** `p=0` is an irrelevant coordinate; `p=1` gives a signed
  dictator with entropy zero; `p=1/2` is covered by the zero-log convention.

## 5. Exact validation

`verify_constant_child_cap.py` is independent of the B12 implementation. It
uses integer Walsh transforms, exact `Fraction` influence, and rational
prime-log signatures for entropy. It exhausts every Boolean child through
four variables, including both constant endpoints.

Command:

```text
python3 verify_constant_child_cap.py
```

Observed result:

```text
boolean_children 65814
exact_assertions 197442
random_seed None
PASS
```

The finite audit checks the two source identities and all normalizations. The
all-dimensional cap follows from the displayed algebra and the source-pinned
calculus/interval proof, not from the sweep.

## 6. Evidence and review states

Read and used:

1. B19 independent reconstruction of the B05 scalar packet formula:
   report blob `b9475660bd527124801ad48e9069985fc20ec300`, verdict blob
   `216b2023ce2f5377f5865d23f552fe7ff0fb4eff`, target commit
   `bdd93bb44cd0335a24e42e06dee81a73b5417768`. The scalar formula is
   **accepted at exact scope**.
2. B12 sharp selector-tax source: report blob
   `a239258721b7946e3f0c31fe84466bbfa1a063f8`, claim blob
   `3dcbb09960e817a56773b3610bb928d80d0be093`, interval output blob
   `363462188d3bd5a5988dc6b6f316930df6b1dc53`. It is **proved and
   source-complete, pending independent review**.
3. B20 critical-pruning source: report blob
   `b6e512b595f33e0fb9f34529cec92cab28d08625`, claim blob
   `3ae975b5b844696a6718c5abc20babecdae3f4a4`; pending independent review.
4. B01 critical-prime normal form: report blob
   `662411dfae5b8d91d0b07e449c59274537492500`; pending independent review.
5. B20 compact contract blob `d5872923b24d68dbcb93394134e3309302f5d034`,
   protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`, and stream-index blob
   `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.

No literature novelty claim is made. No public release, scheduler change,
additional worker, or native Brain ingestion is claimed.

## 7. Remaining obstacle and distinct next actions

The precise surviving universal gap is:

> Bound `min_i Delta_i H/I_i` on restriction-critical tensor-prime Boolean
> functions whose two children are nonconstant at every relevant coordinate,
> or construct a genuine family in this class where it diverges.

Distinct handoffs:

- **A090:** independently reconstruct the B12 calculus interval and the
  cancellation in this transfer.
- **A028/A087:** seek a coherent stopping potential only on the surviving
  two-nonconstant-child class; do not spend work on constant faces.
- **A054/A055:** test whether no-constant-face plus tensor-prime criticality
  forces a quantitative connectedness property, rather than qualitative
  primitivity.
- **A097 next cycle:** transfer the B06 modulation-block identity to show
  which common-square two-child layers are also incompatible with a
  high-ratio critical source, after its independent review state is resolved.

