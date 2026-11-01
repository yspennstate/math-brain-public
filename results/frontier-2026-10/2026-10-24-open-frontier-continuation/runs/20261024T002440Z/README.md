# T384: selected two-input critical-GD law

Run 20261024T002440Z. Full catalog T384 remains **OPEN**. This package advances one precise unpaid obstruction from the previous checkpoint: selecting the actual discrete-GD limit from original endpoint marks, instead of merely specifying a differential inclusion.

For two unit inputs with -1<rho<0, iid original-coordinate symmetric alpha-stable weights (0<alpha<2), fixed input dimension, output normalization (m log m)^(-1/alpha), rate multiplier (log m)^(2/alpha), and physical GD step gamma/(log m)^(1/alpha), the event R1<0<R2 admits the explicit selected limit

\[
r(t)=\exp[-(C+\operatorname{diag}(P_1^\gamma,P_2^\gamma))t]R.
\]

The masses are selected from the original marked Poisson initialization by an exact discrete corner-crossing rule. Every retained endpoint becomes dead or supported by just one input; the limiting residual stays in the mixed cone on every finite horizon. This is an internally proved and separately reviewed restricted theorem, not a full nonorthogonal/deep-network settlement or external novelty claim.

Read `agents/f03_cone.md` for the complete theorem, `agents/f01_entrance.md` for the exact selector, and `CONDITIONAL_LAW.md` for the conditional Levy law. `reviews/MARGINAL_LAW_REVIEW.md` proves that step multipliers 1 and .1 give distinct conditional output path laws, and indeed disjoint sets of unconditioned subsequential path laws. The proof uses a bounded measurable initial-slope observable; it does not mistake natural-coupling separation for marginal-law separation. `agents/f02_separation.md` independently proves positive-probability fixed-time separation under the shared initialization.

Pre-step tangent Grams converge in L1 on finite horizons and uniformly away from time zero **in this mixed cone only**. No such claim is made for general sliding regimes. Kernel J1 convergence across the initial boundary layer is not claimed.

Three reproducible checks were executed and independently rerun with identical complete stdout; see `outputs/ROOT_EXECUTION_READBACK.json`. Numerical checks support the algebra and do not replace proofs. Agent-selected model settings were gpt-6-sol/max; actual serving metadata and root configuration are UNKNOWN. Four mathematical workers were used within the available concurrency limit, not thirty simultaneously.

Read `CLAIMS.json`, `DIRECTIONS.md`, `LITERATURE.md`, and `PROVENANCE.json` before continuing. Exact dependencies are the preceding run's initialization, boundary-grid, and macro compactness proofs; immutable commit pointers are recorded in provenance. All new claims are private research-package records. Native claim IDs and ingestion receipts are not yet established.
