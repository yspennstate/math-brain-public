# Correction log — 20261019T204506Z-fleet01-B16-A078-two-sided-central-band-repair

## Primary correction to prior run v6

The prior proof defined `A_old = {"K_s >= s/3 for every s"}` and then asserted `N_s=s-K_s >= s/3` on `A_old`. This implication is false: `K_s=s` lies in `A_old` but yields `N_s=0`. Therefore the v6 extension-Chernoff step was not justified by its stated event. The finite verifier checked exact restriction identities and numeric constants but did not test this logical implication; its PASS did not detect the proof gap.

## Repair in this run

Use `A = {s/3 <= K_s <= 2s/3 for every s in [m,n-2]}`. Both tails are controlled by binomial symmetry and the same Chernoff exponent. The bad-event union bound receives a factor of two, still less than `1/6144` for `m>=1024`. On this repaired event, `N_s=s-K_s >= s/3`, and the upper-extension Chernoff chain is valid. The random-walk event lower bound and the constants `1/6144`, `1/24576`, `1/100`, and `1/2,457,600` remain valid as stated.

## Provenance

The complete prior v6 directory and exact prior v6 archive tree are included under `PRIOR_EVIDENCE/`. They are preserved as historical artifacts, not represented as corrected versions. The current proof and verifier are new files produced in this run. No independent review is claimed.
