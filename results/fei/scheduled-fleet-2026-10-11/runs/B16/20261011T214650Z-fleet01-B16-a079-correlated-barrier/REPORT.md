# B16 / A079 — correlated auxiliary energy barrier

**Run:** `20261011T214650Z-fleet01-B16-a079-correlated-barrier`  
**Primary packet:** A079 (Correlated auxiliaries)  
**Attempt:** `A079-SHARED-RARE-CELL-1`  
**Claim version:** `B16-A079-RARE-CELL-ENERGY-v1`  
**Gap:** `G-BIASED-TAX`  
**Status:** PROVED pending independent review. Full FEI remains OPEN.

## Exact result

The A077 tower showed a divergent biased helper but also an `rk` fair-bit
compensation.  This run asks whether shared/correlated physical auxiliaries
can evade that compensation while preserving the same B09 two-bit output
law.

They cannot.  For arbitrary deterministic encoders `U,V` on one uniform
cube with independent Bernoulli(`epsilon=2^-k`) outputs, let
`f=(-1)^(UV)`.  Its negative cell has density `delta=epsilon^2`, so cube edge
isoperimetry gives

`I(f) >= 2 delta log2(1/delta) = 4k epsilon^2`.

The exact B09 gain obeys

`J_k <= 4 epsilon^2 (k+log2(e))`.

Therefore

`J_k/I(f) <= 1+log2(e)/k`.

This is a sharp all-dimension barrier for every shared-variable or
spectrally correlated realization preserving that output law.  It is not a
proof of FEI and does not address different gates.

## Genuine correlated control

On uniform `a,b in F_2^k`, take `U=1[a=0]` and `V=1[a+b=0]`.  Both encoders
depend on `a`, but their outputs are independent.  The product spectral
label is `(S xor T,T)` for nonempty `S,T`; its coordinate-block labels are
correlated and satisfy `R!=T`, while

`H(R|T)=log2(2^k-1)`.

The negative cell is the singleton `a=b=0`, attaining the isoperimetric
bound.  Exact formulas give `I=4k 2^-2k` and `H/I -> 4`.  Thus shared
variables move the label geometry but do not create an unpaid FEI ratio.

## Validation

`verify_correlated_barrier.py` performs exact integer/Fraction Walsh and
influence calculations for `k=1,...,5`, verifies the correlated-label map
and mean degree, and prints high-precision entropy diagnostics.  The
all-`k` claim rests on the written edge-isoperimetric proof and elementary
entropy bounds, not finite extrapolation.

## Obstruction controls

- Actual Boolean functions on a uniform physical cube: yes.
- Shared variables: explicit; no disjoint-padding assumption.
- Conditional auxiliary entropy: retained exactly in the control.
- Added influence: bounded below for every realization of the gate law.
- Rare logarithm: exactly `2 delta log2(1/delta)`.
- Tensor guard: disjoint products add `H` and `I`; the ratio does not grow.
- Weighted examples: the divergent helper remains biased and is not called
  an FEI counterexample.

## Sources and dependencies

- B16 contract blob `319bbb049c631c103a842cf9a530c7be91a319d0`.
- Execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- A077 compensated tower, canonical commit
  `3428cf1d55810b1792ce2e38898f99229f6e428f`.
- A034 conditional phase theorem, canonical commit
  `10bd8f25e7f93509b1ccb4daf9d8999fcb776f98`.
- The cube edge-isoperimetric inequality is used as a known theorem.

## Remaining obligation

The same-gate correlated-encoder escape is closed.  A079 remains open for a
different genuine Boolean gate whose proposed gain is not simply the
boundary cost of a rare output cell.  The next attempt should freeze such a
gate before searching and must retain its full conditional spectral entropy.
Route this claim to A034/A080 and independent reviewers A092/A088.
