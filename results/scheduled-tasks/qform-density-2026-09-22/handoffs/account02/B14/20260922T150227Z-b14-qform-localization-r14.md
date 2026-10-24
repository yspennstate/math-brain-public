# account02/B14 handoff — three-point inverse-gap localization

Run `20260922T150227Z-b14-qform-localization-r14`. Programme `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`. Full QFORM remains **OPEN / NOT PROVED**. Execution `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics:

`yspennstate/math-open-problems@3f241388d9bcacf1379ef8ef640b35d7d14aad91`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T150227Z-b14-qform-localization-r14/REPORT.md`

## Partner results applied

Consumed account03/B14's completed select-before-localize theorem at `yspennstate/math-open-problems@2208c3f666582999f1fbc7e55921a4530cbe2789` and its latest no-fixed-fragment-count obstruction at `yspennstate/math-open-problems@54f2d04e936d0dfefe345d17ee18a46b35039d7e`. The active triple is therefore kept unfragmented; arbitrary outside laws are handled by deterministic-outside uniformity.

## New theorem

For independent cap-one densities and exponents `a,b,c<1` with `a+b+c<2`,

`E[|X1-X2|^-a |X2-X3|^-b |X3-X1|^-c] <= C(a,b,c)`,

with the explicit beta-function constant stated in the canonical report. For `a=b=c=1/2`,

`C = 61 + 12*pi < 98.70`.

The proof expands only the near-diagonal pieces. One-edge and two-edge terms use the density cap and independence. The genuine three-edge term is split into the six orderings; after writing ordered gaps as `u,v`, the common-translation integral of the three density factors is at most one, and the remaining simplex integral is exactly `B(1-p,1-q)/(2-a-b-c)`.

The threshold is sharp for this raw absolute compiler: iid `Uniform[0,1]` gives logarithmic divergence at total exponent `2` and power divergence above `2`.

The estimate is uniform under arbitrary separate deterministic shifts of the three active coordinates. Consequently, if a deterministic-outside shell estimate has the form

`P{Q(X_S,z) in J} <= K |J| E prod_{r<s}|(X_r+tau_r(z))-(X_s+tau_s(z))|^-theta_rs`

with each `theta_rs<1` and total exponent `<2`, then the full arbitrary-support product law satisfies

`P{X^T A X in J} <= K C(theta) |J|`

with no moments, support-radius, translation, or fragment-count loss.

## First unpaid implication

For the remaining heavy/localized three-coordinate branch, derive such a deterministic-outside pair-gap shell inequality, or prove that the quadratic shell singularities necessarily exceed the subcritical pair-gap budget. If three square-root pair gaps appear, this handoff pays them immediately by `61+12*pi`. If total exponent reaches `2`, the uniform-law counterexample in the report proves that a different cancellation/aggregation mechanism is required.

Source-control snapshot before the scientific write: `yspennstate/math-research-brain@da8225a364f8b6ff706a10485f1f5ff7f1bf5729`. Live corrections were reread and no refuted premise is used.
