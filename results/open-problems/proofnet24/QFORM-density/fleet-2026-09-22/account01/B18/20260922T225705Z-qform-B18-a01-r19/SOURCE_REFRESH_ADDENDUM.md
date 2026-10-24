# Source refresh addendum for account01/B18 r19

This addendum records the required pre-publication refresh after the immutable `REPORT.md` was written. The full target remains **OPEN / NOT PROVED**.

## Later owner/source refresh consumed

Fresh brain main advanced during this run to `yspennstate/math-research-brain@4e6486221a7a5fdf1767dd607cab24706f6c5e22`. The new owner-requested source `QFORM-CLAUDE-LATEST-20260922T225732Z` keeps the same QFORM-only target and OWNER CONTROL revision `2026-09-22.15`. It requires B18 to verify primary-source inputs needed for the live proof and forbids treating search misses as novelty evidence.

The updated Claude-attributed QFORM source was read at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. Its new theorem D' raises the row-marginal threshold for the *decoupled cross-block* volume theorem to every `h<3/4`, and D_5 removes the marginal condition when a nonzero fifth cross volume is available. Those results do not subsume the present Fresnel theorem: the present theorem concerns an exact three-dimensional coefficient map `A=L^T D L`, and the explicit six-column application has natural one-sided rank-three leverage `4/5` on three columns, above the D' threshold; moreover an exact-rank-three cross block has no fifth exterior volume. No novelty claim is made from this distinction.

The primary inputs used in `REPORT.md` remain Beckner's sharp Hausdorff--Young theorem and the Gaussian-exhaustion form of Brascamp--Lieb due to Lieb/Bennett--Carbery--Christ--Tao. The updated Fourier report independently uses/checks the same sharp-Hausdorff--Young and Gaussian Brascamp--Lieb normalizations, providing a campaign-level consistency check on the constants.

## New correction closure

Two correction events appeared after the initial source snapshot and were read before the handoff was published:

- `QFORM-RAW-DESMOOTHING-COMPACTNESS-FALSE-v1`: there is no target-uniform raw-output L1 translation/BV/Besov/desmoothing modulus under only cap-one inputs.
- `QFORM-NO-UNIFORM-COEFFICIENT-PERTURBATION-CONTINUITY-v1`: small matrix-coefficient perturbations need not produce law-uniform TV-small output perturbations because fragmented supports can move by reciprocal scales.

Neither correction is used or contradicted by `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`: the proof is exact at the given coefficient matrix, uses no desmoothing limit and no perturbative replacement.

The designated partner source remains `yspennstate/math-open-problems@0a28faf7bf87a49a9df787eb276b449aee3d9c47:proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T221352Z-account02-B18-QFORM-r11/REPORT.md`; no newer completed account02/B18 handoff was present at the refreshed brain snapshot.

## Status after refresh

The mathematical statement and constants in `REPORT.md` survive the newer source/correction closure unchanged. The exact unpaid implication remains structural: in the partner Schur-isotropic map `L=[u,V^T]`, prove a universal lower bound on the best capped-basis determinant-entropy score relative to `det(LL^T)`, or route its failure to a previously paid localized/hub/physical-pivot branch without coefficient perturbation.
