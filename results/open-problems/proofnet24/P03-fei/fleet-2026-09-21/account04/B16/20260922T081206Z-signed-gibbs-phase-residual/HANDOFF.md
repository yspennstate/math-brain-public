# Handoff — signed Boolean phase credit for the exact Gibbs/Bellman residual

**Status:** `PARTIAL_PROVED_SIGNED_SHAPE_CREDIT / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

For the live lifted candidate `C^dagger=6.521851214`, account03/B18's exact balanced-uniform Gibbs decomposition leaves the residual shape term `D_KL,2(w || rho_lambda)`. This handoff proves an explicit positive lower bound on that term from the signed Boolean convolution identities.

If

`y = 2^{-C^dagger(1-lambda)}` and `A=(1+y)^k-1`, then for every balanced Boolean k-input gate and every `2<=t<=k`,

\[
D_{KL,2}(w\|\rho_\lambda)
\ge
\frac{y^t}{4\ln2\,A^2}
\left[1-2^{t-1}((1+y)^{k-t}-1)\right]_+^2.
\]

In particular, choosing the full complement packet `t=k` gives the unconditional credit

\[
D_{KL,2}(w\|\rho_\lambda)
\ge \frac{y^k}{4\ln2\,((1+y)^k-1)^2}>0.
\]

Mechanism: `f^2=1` forces the signed XOR-convolution of Fourier amplitudes to vanish at every nonzero translation. For `|T|=t`, the Gibbs target has `2^{t-1}-1` equal-magnitude inside-T pairs after the empty/T pair is removed; this count is odd. Preserve the actual Fourier orientations, extract that parity cancellation obstruction, and only then use Hellinger/KL positivity. This is precisely the sort of signed-before-positive contraction that the historical interface-C line requires.

Combining with the exact B18 price-Bellman identity gives

\[
R_B(G)\ge \lambda C^\dagger I(G)-\log_2(A/x)+\max_t P_{k,t}(y).
\]

At `k=3, lambda=5/6, t=3`, the exact formula gives a floating diagnostic influence threshold `1.4055847175768663`, versus `1.4070396062353996` after deleting the phase credit at the same tilt. The finite checker exhausts all 70 balanced 3-input and 12,870 balanced 4-input truth tables and reports positive slack; the proof is analytic and does not depend on enumeration.

Required inherited interface-C sources were consumed at scientific revision `2d89b7d5bec088d163aa3986e9f83d7499193fd5`:

- `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`;
- `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`.

No Ward/R16/terminal/live-window, dual-code multiplicity, negative-credit, or opposite-sign flag ledger from those sources is spent by this theorem.

Fresh all-gate sources consumed at the same revision:

- `account03/B18/20260922T075546Z-gibbs-price-bellman/REPORT.md`;
- `account02/B16/20260922T074443Z-first-cell-weighted-curvature/REPORT.md`.

**Next exact signed target:** use several low-cardinality translation equations simultaneously and prove a packet/PSD lower bound on the residual KL that does not decay exponentially with arity. Do not replace Fourier orientations by absolute values before the convolution constraints have been used.