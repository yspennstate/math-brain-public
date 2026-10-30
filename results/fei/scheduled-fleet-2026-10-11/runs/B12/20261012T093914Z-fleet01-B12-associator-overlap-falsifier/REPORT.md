# B12 / A057 — overlap-only associator payment is impossible

Run ID: `20261012T093914Z-fleet01-B12-associator-overlap-falsifier`  
Primary packet: **A057 — Coherent restriction remainder**  
Attempt: `B12-A057-ATTEMPT-10`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v10`  
Status: **SCALABLE BOOLEAN FALSIFIER; FULL FEI OPEN**

## Outcome

The previous run proved an exact nonnegative overlap refund in the aggregate
selector-channel influence.  This run tests the natural next mechanism:
pay the positive signed channel associator by that refund together with the
already-paid selector `alpha^2 log(1/alpha^2)` envelope.

That mechanism is false for a genuine Boolean family.  On an `n`-cube let
`N=2^n`, choose a coordinate character `chi` and a point `y` with
`chi(y)=-1`, and set

`g_-=chi`, `g_+=chi+2 1_y`, `h=-chi`.

For the full physical block there is one selector channel.  Its signed
associator is

`Omega_N=Phi(1-2/N)+(N-1)Phi(2/N)-Phi(1-1/N)-(2N-1)Phi(1/N)`.

It satisfies

`N Omega_N = 4 ln N + 2 - 8 ln 2 + O((ln N)/N)`.

The selector alpha-log cost is exactly zero and the collision refund is
`2 Overlap=1/N`.  Hence `Omega_N/(2 Overlap)=N Omega_N -> infinity`.
No finite coefficient repairs the associator using only those two credits.

The same family identifies the correct missing scale.  Its source function
is the point mass `b=1_y`, with `I(b)=n/(2N)`, and

`Omega_N/I(b) -> 8 ln 2`.

Thus a one-use source-influence or terminal derivative-entropy budget has
the correct order, whereas overlap alone is logarithmically too small.

## Why this moves the gap

The previous state left open whether the signed entropy interference could
be paired directly with the exact `-2 Overlap` influence credit.  The new
family rules that out even when the selector singular envelope vanishes
identically.  It does not merely give one finite bad constant: the required
overlap coefficient diverges like `4 ln N`.

At the same time, the source-influence ratio converges to the finite constant
`8 ln 2`.  This sharply selects the next surviving mechanism: retain source
influence (or an exactly equivalent terminal reserve) in the block ledger.

## Verification

`python3 check_associator_family.py`

The checker constructs the genuine Boolean family, verifies the composition
and Fourier identities with exact `Fraction` arithmetic for dimensions
`3..16`, and evaluates the displayed logarithmic quantities at 80 decimal
digits.  It confirms the exact alpha-log, overlap and source-influence
formulas and the increasing overlap ratios.  The unbounded and finite limits
are proved analytically in `ASSOCIATOR_OVERLAP_FALSIFIER.tex`; they are not
inferred from finite computation.

## Controls

- Genuine Boolean realizability: explicit for every `n`.
- Physical overlap: computed from the actual shared coordinate character.
- Parity-zero/activation equivalence: the selector is a character and both
  source branches are physically realized; no free spectral law is used.
- Rare logarithmic cost: present as the point-defect `ln N/N` scale.
- Tensor/near-tensor issue: the family itself has unbounded dimension and
  does not rely on an additive finite defect.
- Full FEI: not refuted; the actual missing cost is paid at constant order by
  source influence.

## Remaining gap

Prove a block inequality in which the signed associator and selector-channel
entropy are charged jointly to a single-use source influence or terminal
derivative-entropy reserve.  The exact family forces any such coefficient to
be at least `8 ln 2` in natural-log units if the reserve is precisely `I(b)`.
The B01/A003 KL/JS falsifier independently requires retaining signed
alignment rather than replacing it by ordinary restriction JS.

New claims await independent A091/A090 review.  Full FEI remains open.

