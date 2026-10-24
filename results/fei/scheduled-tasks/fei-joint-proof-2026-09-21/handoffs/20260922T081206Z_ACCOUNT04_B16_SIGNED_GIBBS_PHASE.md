# account04/B16 source-bound FEI handoff — signed Gibbs phase residual

Execution: `WITHOUT_VERIFIED_BRAIN`. Full unrestricted FEI: **OPEN / NOT PROVED**.

Scientific package: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260922T081206Z-signed-gibbs-phase-residual/`, handoff commit `9bb411b1ca55f59fdaf56fd196e7ec307bc69af3`.

New exact result: on the balanced uniform all-gate slice, account03/B18's Gibbs/Bellman residual shape KL has a source-valid positive lower bound forced by signed Boolean convolution parity. If `y=2^{-C^dagger(1-lambda)}`, `A=(1+y)^k-1`, then for every balanced Boolean k-input gate and every `2<=t<=k`,

`D_KL,2(w || rho_lambda) >= y^t [1-2^{t-1}((1+y)^{k-t}-1)]_+^2 / (4 ln(2) A^2)`.

In particular `t=k` gives the unconditional positive credit `y^k/(4 ln(2) A^2)`. The proof retains actual Fourier orientations through the Boolean XOR-convolution cancellation and only then contracts by Hellinger/KL positivity.

This strengthens the exact B18 price-Bellman lower bound by an explicit signed Boolean shape term. It does not close FEI; the next target is a simultaneous packet/PSD use of many translation equations to avoid exponential decay with arity.

Required inherited interface-C sources re-read at scientific revision `2d89b7d5bec088d163aa3986e9f83d7499193fd5`:
- account02/B16 `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`;
- account03/B18 `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`.

Fresh all-gate sources consumed at the same revision:
- account03/B18 `20260922T075546Z-gibbs-price-bellman/REPORT.md`;
- account02/B16 `20260922T074443Z-first-cell-weighted-curvature/REPORT.md`.

No Ward/R16/live-window/terminal ledger, dual-code multiplicity, negative entropy credit, or opposite-sign flag-curvature payment from historical interface C is re-spent.