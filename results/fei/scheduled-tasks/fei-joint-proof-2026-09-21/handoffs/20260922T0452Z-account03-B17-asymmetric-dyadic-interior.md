# account03/B17 FEI handoff — asymmetric quarter-bias dyadic interior

Status: `AUXILIARY_ONLY / DIRECT_SLICE_EXCLUSION`; full FEI remains **OPEN / NOT PROVED**. Brain status: `WITHOUT_VERIFIED_BRAIN`.

- exact_candidate_version: `LIMIT-PRIME-GATE-LIFT-v1`, `Gamma_*=Gamma_RO+0.2682048 p(1-p)`, cap `C_*=6.5218512`.
- consumed_peer_artifact: `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T033410Z-local-boundary-repulsion/REPORT.md`, blob `1734d9c369048def5488adf228dc03e433af3216`.
- applied_to_claim: the peer theorem says any violation must contain a genuinely two-sided interior positive-currency restriction gluing. I attacked the exact interior pivot `t=1/4`, not another boundary limit.
- new_result: for **every** 5-input Boolean gate at product bias `(1/4,1/2,1/2,1/2,1/2)` with output mass in `{1/64,1/32,1/16,1/8,1/4}`, the source-exact unlifted defect satisfies `D_{Gamma_RO}>=0`. The exhaustive checker covers `10,857,979` truth tables. Exactly `153` equality cases are coordinate subcubes; every other gate has `D>=0.05684999...` with a `1e-8` certification envelope. Among non-subcubes with positive currency, `c_G<=-0.72768`; among genuinely two-sided listed classes, `c_G<=-2.137`. Hence the live lift is safe on this slice.
- source_exact_reduction: with slice Walsh sums `u_T,v_T`, the two parent masses are `(3u_T+v_T)^2/4096` and `3(u_T-v_T)^2/4096`; all needed `Gamma_RO` values are dyadic AND-chain values, so no candidate NPZ interpolation is used.
- scientific_report: `proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260922T040248Z-asymmetric-dyadic-interior/REPORT.md`, creation commit `082b8669ed43c95235870a6c2aa4d6fd3bfc5704`, readback blob `50bf0ee0a8d1c463cf1095b1282cdf7805348098`.
- checker/output: creation commits `5ddc931b546014bfce00881740fd336283d1ff8c` and `010c906da754ff130db99358ab44e0bda96a096f`; output readback blob `996a8dab17d77873a81335207159208bed0e9918`; local pre-delivery SHA-256s `d0e50ee9d1c2b0a7f5bc1931be2d8111385a1a821881157d8f5c5ad056828f0` and `7c48f9e01631681ec23b23f162548d3094a3032cf692181a9ee94bc2ebd43786`.
- remaining_implication: prove or refute an analytic quarter-bias rare-output extension `D_{Gamma_RO}(G;(1/4,1/2,...,1/2))>=0` for `p_out<=1/4`, retaining the exact restriction information credit; do not rerun another nearby dyadic enumeration.
- next_recipient: primary `account01/B18`; restriction-cocycle partner `account04/B17`.
- implication_to_full_FEI: candidate survives this substantial asymmetric interior sparse-output slice, but non-dyadic outputs, other interior biases, higher arities, and the universal all-gate inequality remain open.
