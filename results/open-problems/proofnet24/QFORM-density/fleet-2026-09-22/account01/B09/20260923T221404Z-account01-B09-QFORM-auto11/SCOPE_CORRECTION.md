# Scope correction after late same-slot memory refresh

The initial `REPORT.md` in this run independently rederived the third-compound overlap ledger and the `Omega_0` random-cut payment. A late refresh of the guarded account01/B09 memory pointer showed that the immediately preceding same-slot run

`yspennstate/math-open-problems@b08aeb182c7e4448b960e93db1953cb06cbccb9f`
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T214821Z-account01-B09-QFORM-auto11/REPORT.md`

had already proved the stronger named results

- `QFORM-C3-PHYSICAL-OVERLAP-LEDGER-v1`,
- `QFORM-OMEGA0-DOMINANT-v1`, and
- `QFORM-OVERLAP1-HUB-SCHUR-HALFRIESZ-v1`.

Therefore **the overlap ledger and Omega_0 payment in this run are NOT claimed as new progress**. They are preserved as an independent rederivation/check, in accordance with the instruction to preserve failed or duplicate work rather than erase it.

The genuinely new mathematical advance of the current run is in `ADDENDUM_OMEGA2.md`:

`QFORM-OMEGA2-INVERTIBLE-PAIR-COMPILER-v1`.

It analytically pays a fixed positive two-overlap slice carried by an invertible physical shared pair, with a direct O(interval length) bound, and reduces the global `Omega_2` debt to aggregation across pairs / singular-near-singular pair collars. The full QFORM problem remains OPEN.
