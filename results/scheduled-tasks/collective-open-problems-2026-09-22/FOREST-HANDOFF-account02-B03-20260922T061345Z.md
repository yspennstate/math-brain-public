# FOREST handoff — account02/B03 — 20260922T061345Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent FOREST: `OPEN`  
Context: `WITHOUT_VERIFIED_BRAIN`  
Canonical run report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B03/20260922T061345Z-b03-forest-r11/attempt_report.md`.

## Source state consumed

- Lead account01/B01 `20260922T050946Z-b01-forest-auto11`, shared blob `4cee205cb7d254caf785692838111988a0b8a155`: triangle-free third edges are handled by Simpson/minimality/rank budget; first missing case is triangle contraction creating a `{1,2}` weighted star.
- Named partner account03/B01 `20260922T053534Z-account03-B01-forest-r11`, shared blob `c49d586a18b973280db00e48457a4c2929775ec8`: STAR-2 contraction equals the source-simple conditional law `Cov_J(e,f | u not~v)` after splitting the contracted terminals; coordinatewise star-doubling monotonicity is false.

## New decisive correction: universal STAR-2 is parent-hard

For arbitrary simple `H` with marks `e,f`, attach a fresh triangle `u-v-z-u` to `H` only at a vertex `z`, and contract `g=uv`. The contraction quotient is `H` plus a pendant edge `xz` of weight 2. Thus for each of `Z,Z_e,Z_f,Z_ef` the quotient count is exactly `3` times the count in `H`, and

`Delta_{G/g}(e,f)=9 Delta_H(e,f)`.

Therefore proving **all** source-generated nonempty STAR-2 quotients negatively correlated, or proving `Cov_J(e,f | u not~v)<=0` for arbitrary `J`, is parent-hard and is not a smaller induction lemma. Minimal-counterexample irreducibility must be retained.

## New exact simultaneous-doubling adversaries

The Rayleigh gap has neither a universal submodular nor supermodular sign in doubled-star coordinates.

Negative mixed difference: on `K4` edges `02,03,04,23,24,34`, center `3`, variables `23,34`, marks `03,24`, the four gaps are

`6,12,12,16`,

so the mixed forward difference is `-2`.

Positive mixed difference: on edges `01,02,03,12`, center `0`, variables `02,03`, marks `01,12`, the four gaps are

`8,24,18,54`,

so the mixed forward difference is `+20`.

Hence no additive repair based on a fixed sign for pairwise star-doubling interactions is valid.

## Exact local identity

For one unmarked edge fugacity `t`, write

`q(t)=D0+M t+D1 t^2`.

Then

`q(2)=2q(1)-D0+2D1`,

so doubling is safe iff

`D0 <= 2q(1)+2D1`.

This is an exact certificate, not a monotonicity claim. For multiple doublings it cannot simply be summed because of the mixed-sign witnesses above.

## Corrected source-valid sufficient statement

Forest partition functions factor over blocks. Thus in a STAR-2 contraction quotient:

- if marks `e,f` lie in different blocks, their covariance is zero;
- if they lie in a common block `B`, all other blocks multiply the four marked counts by one positive common factor, so `Delta_Q=K^2 Delta_B`;
- if `B` contains no doubled edge, minimality applies to the smaller ordinary unit-simple block and the contraction case is safe.

Therefore the genuinely unresolved triangle-contraction configuration is narrower:

**`e`, `f`, and at least one doubled star edge must lie in one common 2-connected block.**

This removes the parent-hard pendant/separable embeddings and isolates the overlapping-cycle geometry. The next attack should apply account03/B01's component-factor identity only in this irreducible common-block configuration, using a global signed coupling/flow; coordinate monotonicity and fixed-sign star interactions are now ruled out.

## Exact regression

Checker blob `183dfcf54dc1f0601a39344ac8b3180e2a480e55`; output blob `8e3aba77935ca63e221410792452675424981120`; output ends `STATUS=PASS`. It verifies both mixed witnesses, verifies factor-9 pendant scaling on 11,766 marked instances through base order 5, and exhausts the conditional endpoint-disconnection inequality through order 6 (377,425 marked instances total) with zero failures. Finite PASS is regression only, not universal closure.
