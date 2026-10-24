# P19 immutable readback receipt — 2026-09-16 18:58:33 run

Canonical report:

`proofnet24/P19-hadwiger-nelson/runs/2026-09-16/2026-09-16_18-58-33__run-report.md`

Creation commit: `0953f105fb39de04ee08981f467129daae722b6b`

Verified report blob: `dfd274da721571f65e6f5a1e08518a1bcc75e549`

Readback at the exact creation commit was performed in contiguous ranges through the terminal marker `**END OF CANONICAL REPORT**`. A separate fetch from current `master` returned the identical blob.

Exact finite-certificate artifacts were also read back at their own creation commits:

- `proofnet24/P19-hadwiger-nelson/artifacts/2026-09-16_18-58-33__parts509_d3_noforceddiff_exact.py` — commit `71ca3f9317388265f3174aa8a3244cdd40abea47`, blob `7211f1ec51d84565ba7a27962e3b69d1958c1329`;
- `proofnet24/P19-hadwiger-nelson/artifacts/2026-09-16_18-58-33__parts509_d3_noforceddiff_exact.out` — commit `2b4f4001a6f266f4eac64208f9a9efbb2aa34808`, blob `9ad3786a2ea879286ac1a0c90177ac95285ba251`, ending `ALL_EXACT_CHECKS_PASSED`;
- `proofnet24/P19-hadwiger-nelson/artifacts/2026-09-16_18-58-33__audit_p20_twolevel_transform_exact.py` — commit `65ef955b45f5b4d6d5ca7ae1d4b3a626afbe1959`, blob `1a0d209ad746801231e4dbfeae94338ea7a0fe60`;
- `proofnet24/P19-hadwiger-nelson/artifacts/2026-09-16_18-58-33__audit_p20_twolevel_transform_exact.out` — commit `a9fb4e9ca261b068e4cb0f3f7943c1ef7ce64586`, blob `4b9cd4622a977ccb8aac48f99849961c617bb99b`, ending `ALL_EXACT_CHECKS_PASSED`.

Status preserved: P19 Hadwiger-Nelson OPEN / PARTIAL; tracked metric 509 -> 509, no movement; no six-chromatic pure unit-distance candidate found. The Parts-509 exact `sqrt(3)` forced-different pair route selected by STUCK RECOVERY 2 is exhausted by explicit equality-colouring witnesses for all 1175 terminal pairs.
