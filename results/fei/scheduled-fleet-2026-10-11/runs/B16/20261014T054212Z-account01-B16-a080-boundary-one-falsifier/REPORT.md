# B16 / A080 — the boundary pair `(1,0)` is false on a growing Boolean family

**Status:** PROVED asymptotic falsifier, pending independent review. **Universal GU and full FEI remain OPEN.**

## Frozen target and prior bound

- Primary packet: **A080 (Universal-counterexample standard)**.
- Attempt: `A080-BOUNDARY-ONE-2`.
- Stable gap: `GU-UNIVERSAL-PAIR-BOUNDARY`.
- Claim version: `B16-A080-BOUNDARY-ONE-v1`.
- Frozen pair: `(a,b)=(1,0)`, i.e. `G(f)<=I(f)` for every genuine Boolean `f`.

The previous growing-rank OR theorem proved only `G/I->1`, with an unsigned error `O(r2^-r)` in the ratio. It therefore forced `a+b>=1` but did not decide the boundary pair `(1,0)`.

## New all-parameter family theorem

Let `k=2^r`, partition the cube into `k` disjoint `r`-bit blocks, and let

\[
f_r=1-2\mathbf 1\{\text{at least one block equals a fixed point}\}.
\]

The exact unequal-child formula is retained for every physical restriction. Writing `epsilon=2^-r` and `P=(1-epsilon)^(1/epsilon)`, the middle term of `U` has the exact decrement

\[
G_M=I(f_r)\bigl(1+2\epsilon(r-2)\bigr).
\]

The constant-frequency and logarithmic-normalization terms contribute only `O(r epsilon)` to `G` because `P->e^-1 != 1/2`, so their symmetric child difference is second order. Consequently

\[
\boxed{G(f_r)-I(f_r)=4e^{-1}r^2 2^{-r}+O(r2^{-r}).}
\]

In particular, `G(f_r)>I(f_r)` for every sufficiently large `r`. The high-precision reconstruction finds the sign already positive for every `2<=r<=60`, but the finite table is diagnostic; the analytic positive leading term proves the unbounded family statement.

The complete asymptotic ledger is

\[
I=2e^{-1}r+O(r2^{-r}),\quad H=8e^{-1}r+O(1),\quad U=2e^{-1}r+O(1),
\]
\[
\boxed{G/I=1+2r2^{-r}+O(2^{-r}),\qquad U/I\to1,\qquad H/I\to4.}
\]

## Exact GU implication

The universal pair `(1,0)` is **REFUTED**. This strictly sharpens the earlier necessary line `a+b>=1`: the endpoint at `b=0` is not admissible.

This does not refute GU. For any fixed `b>0` on `a+b=1`, the positive term `b(U-I)` is polynomially larger than the exponentially small `G-I` excess on this family. The next relevant target is therefore a concrete boundary pair with `b>0`, retaining the full `U-I` compensation. No ratio here diverges, and tensoring a fixed ratio is not used.

If a universal pair is eventually proved, the source reduction still gives

\[
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\]

## Verification and scope

`verify_boundary_one.py` uses 100-digit Decimal arithmetic to reconstruct the exact heterogeneous-child formula and the exact middle-term identity for `2<=r<=60`. It reports `G-I>0` throughout and shows the normalized excess tending to one. No random seed is used.

The proof is in `BOUNDARY_ONE_FALSIFIER.tex`; the finite run is not treated as an all-dimensional certificate. Independent review is requested from A092, A090, and A094.

## Next unpaid step

Freeze a boundary pair with `b>0`—preferably `(a,b)=(3/4,1/4)`—and compute the exact residual `G-aI-bU` on a family whose `U-I` compensation is of the same order as `G-I`. The present OR family cannot falsify such a pair asymptotically.

