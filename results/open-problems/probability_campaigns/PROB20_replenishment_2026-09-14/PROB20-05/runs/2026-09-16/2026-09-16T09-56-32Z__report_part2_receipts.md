# PROB20-05 — n=17 checkpoint delivery receipts

This append-only receipt records actual GitHub creation commits, exact-commit readbacks, and completed checker outputs for the `2026-09-16T09-56-32Z` checkpoint.

## Main mathematical report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T09-56-32Z__report.md`

Creation commit:

`1b5b45455db009f4abb9f319a8c999075a5667ea`

Exact-commit readback blob:

`488b6c6ebd98dd7d8f41b8c2185bffa448a0068b`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## Exact phase-one checker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T09-56-32Z__s11_n17_phase1_exact.cpp`

Creation commit:

`ee1f4dade617b9bf967fab9757e009b3ff300243`

Exact-commit readback blob:

`9e142e26c5e25c0c593f19c6ece4e64748aa2186`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

The program verifies every `10^-15` radical enclosure by integer squaring, uses the resulting sign-aware integer lower bound for every deterministic domino certificate, and after each floating-point Hungarian locator for `k=0,1` accepts the proposed assignment only when the same exact lower bound is positive.

Completed asserted outputs:

`k=0 total=39916800`

`universal_pass=19376735 universal_fail=20540065 min_pass=2 max_fail=-8`

`fixed_exact_pass=20454983`

`adaptive_exact_pass=82413 nonzero_tilings=149`

`remain=2669 canonical_reps=1681`

`S11 N17 EXACT PHASE1 PASSED`

`k=1 total=39916800`

`universal_pass=11216695 universal_fail=28700105 min_pass=2 max_fail=-8`

`fixed_exact_pass=28683934`

`adaptive_exact_pass=15615 nonzero_tilings=83`

`remain=556 canonical_reps=362`

`S11 N17 EXACT PHASE1 PASSED`

`k=2 total=39916800`

`universal_pass=5989097 universal_fail=33927703 min_pass=2 max_fail=-8`

`fixed_exact_pass=33920087`

`adaptive_exact_pass=0 nonzero_tilings=0`

`remain=7616 canonical_reps=5383`

`S11 N17 EXACT PHASE1 PASSED`

`k=3 total=39916800`

`universal_pass=4349090 universal_fail=35567710 min_pass=2 max_fail=-8`

`fixed_exact_pass=35561443`

`adaptive_exact_pass=0 nonzero_tilings=0`

`remain=6267 canonical_reps=2238`

`S11 N17 EXACT PHASE1 PASSED`.

## Exact balanced-cell postchecker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T09-56-32Z__s11_n17_cell_postcheck.py`

Creation commit:

`d41ce0b4e6830a8fd44b72dfb2aaf5cb70607dab`

Exact-commit readback blob:

`8736a9e7545eb540555d42a1ef1ea5e3a8b7dac0`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

A first create-file attempt for this artifact encountered an ordinary GitHub contents-API branch conflict (`409`: branch head had advanced concurrently). Per owner instructions it was retried once, on the same unique append-only path, and succeeded. No access/workflow/settings change or bypass was attempted.

Completed bounded exact cell checks:

- `k=0`: `total=1681`, `success=1679`, minimum successful integer margin `1776`; failures are identity `(-1944,W=38712)` and the global adjacent transposition `(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,15)` with margin `-504`, `W=38808`.
- `k=1`: `total=362`, `success=361`, minimum successful margin `1776`; sole failure identity.
- `k=2`: `total=5383`, `success=5382`, minimum successful margin `3336`; sole failure identity.
- `k=3`: `total=2238`, `success=2237`, minimum successful margin `4716`; sole failure identity.

The `k=0,1` outputs were rerun directly on the finalized phase-one residual files. The completed `k=2,3` bounded checks were run on exact-fixed residual files generated immediately before finalizing phase one; sorted SHA-256 comparison proves those sets are identical to the finalized phase-one sets:

- `k=2`: `e1164d55628fe0f39ff919c76cfd15fce3940fb50afcdfa893e9cb91f9b32008`;
- `k=3`: `14b9660ac310d315ebb3194abfe3272d3e075ad288db2c8f2b8da72996696acc`.

A later attempt to run all four cell classes in one wrapper hit the execution limit before returning a combined final line. Nothing was inferred from that interrupted wrapper; the theorem uses the completed bounded class checks above.

## Mathematical status

The complete eleven-bin positive-shuffle case is now proved/self-checked for global resolutions `n=11,12,13,14,15,16,17`. The full continuum Catalano–Lavenant conjecture remains open. These are explicit transport and exact computational/self-check certificates, not independent external or formal proof-assistant verification.
