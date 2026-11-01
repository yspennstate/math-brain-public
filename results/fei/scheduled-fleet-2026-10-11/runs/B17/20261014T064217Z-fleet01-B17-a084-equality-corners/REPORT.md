# B17 / A084 — the two-bit half-tax continuum is complete

**Status:** PROVED at the complete two-bit scope, pending fresh independent review. **Universal GU and full FEI remain OPEN.**

## Frozen candidate

For the biased two-bit Boolean AND kernel, prove

\[
J_A\le M_A+\tfrac12\Delta_A
\]

for every `0<p<=1/2`, `0<=q<=1`. Primary packet: **A084**. Attempt: `A084-EQUALITY-CORNERS-2`. Stable gap: `FEI-GAP-TWO-BIT-HALF-TAX`. Claim version: `B17-A084-TWO-BIT-COMPLETE-v2`.

The only missing parameters were `0.49<=p<=0.5` with `q` in the endpoint collars `[0,0.01]` or `[0.99,1]`, where the exact margin vanishes at two corners.

## New result

Writing `d=(ln 2)(M_A+Delta_A/2-J_A)`, the balanced lower edge has the exact factor estimate

\[
d(1/2,q)\ge q^2\left(2\log(1/q)-1-8q+4q^2\right)>0
\]

for `0<q<=0.01`, with equality at `q=0`.

A 90-digit directed-rounding derivative certificate proves

\[
\partial_p d(p,q)\le-0.9
\]

on the full closed rectangle `p in [0.49,0.5]`, `q in [0,0.01]`. Hence

\[
d(p,q)\ge d(1/2,q)+0.9(1/2-p)\ge0.
\]

The upper collar requires no second numerical certificate: an entropy comparison proves `d(p,1-q)>=d(p,q)` for `p<=1/2`, `q<=1/2`.

Combining this with the already proved rare tail, repaired compact/endpoint certificates, and balanced-transition certificates gives

\[
\boxed{J_A\le M_A+\tfrac12\Delta_A\quad
\text{for all }0<p\le1/2,\ 0\le q\le1.}
\]

## Certificate

The derivative checker visited 45 interval boxes, accepted 23 leaves, reached depth 6, and left zero unresolved boxes. Its largest certified upper endpoint was

`-0.9002260317012236411683888873233463387246104808513`.

All operations use 90-decimal directed rounding. Singular products are rewritten as `x log x` before enclosure; no binary floating-point value is used for a sign decision.

## GU implication and surviving gap

This completes the finite/continuum **two-bit** core, not universal GU. A naive global cancellation of all `M_A` terms plus single-use half taxes would imply `G<=I/2`, but the growing-rank OR-defect family has `G/I->1` and eventually `G>I`. Therefore that assembly is impossible: some higher-arity, hierarchy, or terminal `M`-reserve must survive.

The first unpaid universal step is now explicit: derive the three-bit prime-gate residual and identify a telescoping potential that retains the nonzero `M` boundary without reusing physical influence. No bias tail or two-bit endpoint remains open.

Requested reviewers: A085, A090, A094. Because the prior B10 proof required a material interval repair, a fresh independent end-to-end review is still required.
