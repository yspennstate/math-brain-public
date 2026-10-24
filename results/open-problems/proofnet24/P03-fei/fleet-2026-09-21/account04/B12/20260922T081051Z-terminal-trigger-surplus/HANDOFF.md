# Source-bound handoff: terminal trigger-surplus obstruction

Primary report:
`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`

Report blob: `d283c7b495316959312155f8ba68fb83569d9633`.
Report creation commit: `fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`.

Consumed newest compatible account02 result:
`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`, blob `68e838a493671ed5c27a29468dfcce7bb621d860`.

Exact implication used from account02/B13: any finite-dimensional terminal-class obstruction may be chosen centered, essential and tensor-primitive, and satisfies `U_A >= K D_A` for every nonempty physical block. The formerly used fixed `Gamma^dagger` is explicitly preserved as refuted and is not revived.

Preserved account04/B18 source:
`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`, blob `0e8c2cc28da81af8843b565cb47285684b164480`, supplying `sum_{i != k} p_ik <= 4 d_k` and the warning that raw `sum_k d_k` is not automatically `O(J)`.

New result. If derivative row `i` has support within relative error `eta` of a coordinate subcube on trigger set `F_i`, then in an all-block terminal core

`sum_{k in F_i} [h_2(q_k)-K q_k] >= (1-eta)[K+j'(q_i)]q_i`.

For any family of such rows,

`sum_i q_i^2 [K+j'(q_i)] <= 2/((1-eta)(1-2eta)) * sum_k [h_2(q_k)-Kq_k] d_k`.

At `eta=1/16` the exact coefficient is `256/105`. Thus medium/heavy robust rows force a dimension-free surplus-weighted depth bank without any ambient-coordinate-name payment. No claim is made that the weighted bank, or raw `sum d_k`, is universally `O(J)`.

Checker blob `166886104992ef4570277e137d5f02e053f72d5c`; output blob `bd6df720e25503b4767792296b9cc8358a1f0b34`; checker SHA-256 `36cee49a1955e93c509761a6eaf4ca590c730edef9f6dc3ff6d059c0d000ca09`; exact regression result `PASS`.

Full uniform-cube FEI remains OPEN / NOT PROVED. Next recipient should attack the surplus-weighted depth bank on the all-block terminal class or use the scale obstruction to eliminate robust rows before treating the remaining small-influence/nonrobust rows by a distinct mechanism.
