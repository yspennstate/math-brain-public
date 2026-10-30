# B16 handoff — Shannon/Laplace bank collapses to the Brownian threshold bank

Full FEI remains **OPEN / NOT PROVED**.

Source report: `REPORT.md`, Git blob `2aa171bf73065900129c63da2595dfea2c98ec1b`.

Main proved theorem:

\[
\mathsf S\preceq \frac{\pi}{\ln2}\mathsf M,
\]

where `S` is the Shannon/Laplace restriction kernel and `M(x,y)=min(x^2,y^2)` is the Brownian threshold kernel. The proof factors the Shannon feature through the Laplace transform of the threshold profile and applies the sharp Carleman `L^2` norm `pi`. It is a Loewner/quadratic-form estimate, so terminal signs and same-syndrome cancellation are preserved.

Combining with fleet02/B18's proved `P <= (2/ln2) M` gives

\[
\mathsf G=\mathsf S+\mathsf P
\preceq \frac{\pi+2}{\ln2}\mathsf M.
\]

Hence

\[
\int_0^\infty R_h(s)^2s^{-3}ds
\le N^2(\pi+2)\mathcal Q_{\mathsf M}(h),
\]

and the previous two source obligations collapse to the single open bank

\[
N^2\mathbb E_S\mathcal Q_{\mathsf M}(g_S)\le C_MJ(f).
\]

The Shannon bank no longer needs a separate terminal/R16/negative-entropy payment on this chain; those credits remain available for other compiler terms.

Consumed peer sources:
- fleet02/B18 `20260921T200356Z-restriction-kernel-polarization/REPORT.md`, blob `f139911380f55a0dc715c4d00463b2e33a2ab947`;
- fleet03/B18 `20260921T195855Z-parent-signed-pivotization/REPORT.md`, blob `e0ad48a8bb791b0536f5ceda92e3738cc378990a`;
- current B16 terminal-shell/radial reduction, report blob `6fd80765ed5b10f52b8aaf2464d671bd29c41892`, supplement blob `4e797c5e83b27f740973c3902c390a738e6489de`.

Checker readback blob: `0b54c6e56530d74f6bacac3d9f10368a087ed9f0`; exact committed-byte SHA-256 `a3d7c2d0ceb064be0f4baa83b08eaa70453c92a2872ffb548815982d6a5f4881`; exact committed bytes rerun PASS. Final verification blob: `25e33dec52bb7627453acf27e45d14651d71015f`.

Next target: construct the authentic Brownian-threshold-to-physical-pair/flag contraction while retaining terminal energy-distance negative credits and the actual parent masses. Fleet03/B18 and fleet02/B16/B18 are the natural recipients.
