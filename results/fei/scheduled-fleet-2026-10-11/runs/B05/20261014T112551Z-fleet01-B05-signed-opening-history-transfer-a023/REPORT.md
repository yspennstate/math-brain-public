# B05 / A023 — signed-opening activation history transfer

**Run:** `20261014T112551Z-fleet01-B05-signed-opening-history-transfer-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B05-A023-SIGNED-OPENING-HISTORY-TRANSFER-v1`  
**Status:** **AUTHOR-PROVED PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Exact candidate and prior scope

The independently reviewed fresh/disjoint theorem proves, with

\[
c_* = \frac{29}{2}+\frac4{\ln2},
\]

that a fresh fair activation contracts `L+2Phi`. It did not explain how to
open a block of already reused core coordinates without charging a positive
orbit potential.

This run freezes the signed node criterion

\[
\Delta_xL_{c_*,\eta}+2(R-O)\le0,
\qquad 0<\eta\le1, \tag{SOLD}
\]

and tests it at one outer activation selector while allowing an arbitrary
core block `X`.

## Result

Let `F=A(f)` be a fresh fair activation with selector `z`. At the selector
node, inherit the empty block, open the arbitrary active block
`X union {z}`, query `z`, and pass `X` to the core child. Then

\[
R-O=\Phi(F)-\frac12\Theta_X(f).
\]

Since `Phi(f)<=Theta_X(f)`, the reviewed half-packet contraction gives

\[
\boxed{
\Delta_zL_{c_*,\eta}(F)+2(R-O)
\le\Phi(f)-\Theta_X(f)\le0.}
\]

Thus an outer activation can transfer an arbitrary history block of reused
core coordinates to its core child with no extra dimension, depth, bias,
overlap, or block-size charge. The opening refund is essential and is not
replaced by a positive influence budget.

If the core has a complete adapted tree starting with inherited block `X`
and satisfying (SOLD), prepending this selector node produces a complete
paid tree with empty root history. At `eta=1`, the resulting endpoint is

\[
G\le\left(\frac{33}{2}+\frac4{\ln2}\right)I<22.270781I,
\]

and

\[
H\le\left(35+\frac8{\ln2}\right)I<46.541561I.
\]

This is a one-node history-transfer theorem, not A023 closure. The selector
is still fresh and fair; the inherited core tree, data-query nodes, and
biased/nonfresh selector nodes remain unpaid.

## Why this matters

The naive positive orbit lift fails because it charges `Theta_{X+z}`
without subtracting the opening. Here `Theta_{X+z}` cancels identically
between `R` and `O`; only `Phi(F)-Theta_X(f)/2` remains. This is the first
activation bridge in this route that permits an arbitrary reused block at
the core interface without a `|X|` or rare-logarithmic loss.

## Verification

`CHECK.py` independently evaluates all Boolean cores through three
variables and seeded cores through seven variables. It tests every block
through dimension three and sixteen declared blocks per larger core.

- 358 Boolean cores;
- 6,804 signed selector-node checks at `eta=1/4` and `eta=1`;
- maximum orbit activation identity error `3.56e-15`;
- maximum signed node drift `0` at recorded precision.

The theorem is analytic; the floating checks are regression evidence only.

## Before / after

| Item | Previous | New |
|---|---|---|
| Activation-core interface | empty/fresh history only | arbitrary inherited core block `X` transferred exactly |
| Opening payment | positive orbit lift would overcharge | signed `R-O` cancels the entire opened orbit potential |
| Parameter loss | possible `|X|`, depth, or rarity loss | none at this selector node |
| Universal closure | open | still open at inherited core/data-query nodes |

## Next action

Test the inherited-block core criterion on the smallest two-level overlap
`{x,y}->{y,z}`. Expand the complete signed `Delta U=B-Gamma+KL` term inside
`Delta L` and keep `R-O` before any upper bound. Route to A087/A094 for
independent reconstruction and B20 for assembly.

Model: Codex. Reasoning-effort metadata: UNKNOWN.

